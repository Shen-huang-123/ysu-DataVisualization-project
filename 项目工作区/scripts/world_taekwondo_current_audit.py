"""Capture World Taekwondo Olympic medalist tables and compare 24 events."""
import hashlib,re
from pathlib import Path
import pandas as pd,requests
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力/08_逐项外部核验'
RAW=ROOT/'资料文件/外部核验/世界跆拳道联盟现行奖牌页';RAW.mkdir(parents=True,exist_ok=True)
SLUG={2008:'beijing-2008-og',2012:'london-2012-og',2016:'rio-2016-og'}
LEVEL={'-58':'Flyweight','-68':'Featherweight','-80':'Welterweight','+80':'Heavyweight','-49':'Flyweight','-57':'Featherweight','-67':'Welterweight','+67':'Heavyweight'}
rows=[]
for year,slug in SLUG.items():
 url=f'https://results.worldtaekwondo.org/competitions/{slug}/medalists'
 r=requests.get(url,timeout=30);r.raise_for_status();RAW.joinpath(f'{year}.html').write_bytes(r.content)
 found={}
 for tr in BeautifulSoup(r.content,'html.parser').find_all('tr'):
  cells=tr.find_all('td',recursive=False)
  if len(cells)!=4:continue
  cat=cells[2].get_text(' ',strip=True)
  m=re.fullmatch(r'(Men|Women)\s+([+-]\d+)kg',cat)
  if not m:continue
  gender,weight=m.groups();event=f"Taekwondo {gender}'s {LEVEL[weight]}"
  medal=cells[3].get_text(' ',strip=True).title()
  if medal not in ('Gold','Silver','Bronze'):continue
  noc=cells[1].select_one('.flag span')
  if not noc:continue
  found.setdefault(event,{'Gold':[],'Silver':[],'Bronze':[]})[medal].append(noc.get_text(strip=True))
 for event,medals in found.items():
  assert len(medals['Gold'])==1 and len(medals['Silver'])==1 and len(medals['Bronze'])==2,(year,event,medals)
  rows.append({'Year':year,'Event':event,**{k:'|'.join(sorted(v)) for k,v in medals.items()},'SourceURL':url,'SHA256':hashlib.sha256(r.content).hexdigest()})
 print(year,'events',len(found))
a=pd.DataFrame(rows);assert len(a)==24
a.to_csv(OUT/'世界跆拳道联盟现行奥运逐级别核验.csv',index=False,encoding='utf-8-sig')
o=pd.read_csv(OUT/'逐小项三色对照.csv')
b=pd.read_csv(OUT/'历史910项来源覆盖总表.csv')
d=a.merge(o,left_on=['Year','Event'],right_on=['Year','Event_proxy'],validate='one_to_one');assert len(d)==24
diff=[]
for _,r in d.iterrows():
 current={k:r[k] for k in ('Gold','Silver','Bronze')}
 if r.Year==2016 and r.Event=="Taekwondo Women's Featherweight":
  current['Bronze']=current['Bronze'].replace('RTA','IRI') # historical NOC at Rio, per IOC newsroom
 same=all(sorted(current[k].split('|'))==sorted(str(r[f'{k}_archive']).split('|')) for k in ('Gold','Silver','Bronze'))
 if not same:diff.append({'Year':r.Year,'Event':r.Event,**{k:r[k] for k in ('Gold','Silver','Bronze')},**{k+'_archive':r[f'{k}_archive'] for k in ('Gold','Silver','Bronze')}})
 idx=b.index[(b.Year==r.Year)&(b.Event==r.Event)];assert len(idx)==1
 if r.Year==2008 and r.Event=="Taekwondo Women's Flyweight":
  b.loc[idx,'来源类型']='官方原始补证（协会奖牌页错误）'
  b.loc[idx,'来源等级']='北京2008官方成绩册第111页：VEN/CUB两铜；世界跆拳道联盟当前奖牌页错列KEN'
  b.loc[idx,'来源链接']='https://digital.la84.org/digital/api/collection/p17103coll8/id/68173/download'
  continue
 b.loc[idx,'来源类型']='世界跆拳道联盟现行逐级别结果'
 b.loc[idx,'来源等级']='世界跆拳道联盟现行奥运奖牌页逐级别核验；不等同于IOC现行授牌结果' + ('；金米娅2016代表IRI，当前运动员代码RTA已还原赛时NOC' if r.Year==2016 and r.Event=="Taekwondo Women's Featherweight" else '')
 b.loc[idx,'来源链接']=r.SourceURL
b.to_csv(OUT/'历史910项来源覆盖总表.csv',index=False,encoding='utf-8-sig')
pd.DataFrame(diff,columns=['Year','Event','Gold','Silver','Bronze','Gold_archive','Silver_archive','Bronze_archive']).to_csv(OUT/'世界跆拳道联盟与旧存档差异.csv',index=False,encoding='utf-8-sig')
print('mismatches',len(diff));print(pd.DataFrame(diff).to_string(index=False) if diff else 'none')
print(b['来源类型'].value_counts().to_string())
