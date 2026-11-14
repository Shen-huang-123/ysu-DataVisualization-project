"""Audit historical Olympic athletics events against live World Athletics finals.

World Athletics is the current primary competition-result authority for its
sport. This independently checks medals but does not claim IOC page access or
IOC medal-presentation decisions.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import hashlib
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'交付文件'/'任务三_专题深挖'/'S2_口径的魔力'/'08_逐项外部核验'
RAW=ROOT/'资料文件'/'外部核验'/'世界田联现行结果页'
RAW.mkdir(parents=True,exist_ok=True)
base=pd.read_csv(OUT/'历史910项来源覆盖总表.csv',dtype=str).fillna('')
archive=pd.read_csv(OUT/'逐小项三色对照.csv',dtype=str).fillna('')
todo=base[(base['来源类型']=='Olympics.com第三方2023抓取存档') & base.Event.str.startswith('Athletics ')][['Year','Event']].copy()
years={'2008':'the-xxix-olympic-games-6977748','2012':'the-xxx-olympic-games-6999193','2016':'the-xxxi-olympic-games-7093747'}
def make_url(year,event):
    if event.endswith("Men's Decathlon"):
        return f'https://worldathletics.org/competition/calendar-results/results/{years[year].rsplit("-",1)[-1]}?eventId=10229629'
    if event.endswith("Women's Heptathlon"):
        return f'https://worldathletics.org/competition/calendar-results/results/{years[year].rsplit("-",1)[-1]}?eventId=10229536'
    sex='women' if "Women's" in event else 'men'
    s=event.split("Women's ",1)[1] if sex=='women' else event.split("Men's ",1)[1]
    s=s.lower().replace(',','').replace(' x ','x').replace(' kilometres walk',' kilometres race walk')
    s=s.replace(' ','-')
    return f'https://worldathletics.org/competitions/olympic-games/{years[year]}/results/{sex}/{s}/final/result'
def get(row):
    year,event=row.Year,row.Event
    url=make_url(year,event)
    result={'Year':year,'Event':event,'official_url':url,'capture_date':'2026-11-13',
            'Gold_current':'','Silver_current':'','Bronze_current':'','http_status':'','html_sha256':'','status':''}
    try:
        for attempt in range(2):
            try:
                r=requests.get(url,timeout=(10,35),headers={'User-Agent':'Mozilla/5.0'},allow_redirects=True)
                break
            except requests.RequestException:
                if attempt:raise
        result['http_status']=str(r.status_code)
        if r.status_code!=200:raise ValueError(f'HTTP {r.status_code}')
        soup=BeautifulSoup(r.text,'html.parser')
        medals={1:[],2:[],3:[]}
        silver_rows=0
        for tr in soup.select('tr[role=row]'):
            cells=[td.get_text(' ',strip=True) for td in tr.select('td[role=cell]')]
            if not cells:continue
            m=re.fullmatch(r'=?([123])\.?',cells[0])
            if not m:continue
            rank=int(m.group(1))
            if rank==2:silver_rows+=1
            nocs=[c for c in cells[1:6] if re.fullmatch(r'[A-Z]{3}',c)]
            if nocs and nocs[0] not in medals[rank]:medals[rank].append(nocs[0])
        for rank,col in [(1,'Gold_current'),(2,'Silver_current'),(3,'Bronze_current')]:
            result[col]='|'.join(sorted(medals[rank]))
        tied_silver_without_bronze=bool(result['Gold_current'] and not result['Bronze_current'] and silver_rows>=2)
        if not result['Gold_current'] or not result['Silver_current'] or (not result['Bronze_current'] and not tied_silver_without_bronze):
            raise ValueError('missing ranked NOC(s)')
        raw=r.content
        result['html_sha256']=hashlib.sha256(raw).hexdigest()
        path=RAW/f'{year}_{hashlib.sha1(event.encode()).hexdigest()[:12]}.html'
        path.write_bytes(raw)
        result['saved_html']=str(path.relative_to(ROOT))
        result['status']='世界田联现行决赛三色已抽取（并列银牌无铜牌）' if tied_silver_without_bronze else '世界田联现行决赛三色已抽取'
    except Exception as e:result['status']='待人工复核：'+str(e)[:120]
    return result
with ThreadPoolExecutor(max_workers=5) as pool:
    futures=[pool.submit(get,r) for r in todo.itertuples(index=False)]
    rows=[f.result() for f in as_completed(futures)]
z=pd.DataFrame(rows).sort_values(['Year','Event'])
keys=archive[['Year','Event_proxy','Gold_proxy','Silver_proxy','Bronze_proxy','Gold_archive','Silver_archive','Bronze_archive']].rename(columns={'Event_proxy':'Event'})
z=z.merge(keys,on=['Year','Event'],how='left',validate='one_to_one')
def norm(v):return '|'.join(sorted({x.strip() for x in str(v).split('|') if x.strip() and x.strip().lower()!='nan'}))
for colour in ['Gold','Silver','Bronze']:
    z[colour+'_proxy_match']=z.apply(lambda x:norm(x[colour+'_current'])==norm(x[colour+'_proxy']) if x.status.startswith('世界田联现行决赛三色已抽取') else False,axis=1)
    z[colour+'_archive_match']=z.apply(lambda x:norm(x[colour+'_current'])==norm(x[colour+'_archive']) if x.status.startswith('世界田联现行决赛三色已抽取') else False,axis=1)
z.to_csv(OUT/'世界田联现行奥运田径逐项核验.csv',index=False,encoding='utf-8-sig')
print('requested',len(z),'extracted',int(z.status.str.startswith('世界田联现行决赛三色已抽取').sum()),'all_proxy_match',int(z[['Gold_proxy_match','Silver_proxy_match','Bronze_proxy_match']].all(axis=1).sum()))
