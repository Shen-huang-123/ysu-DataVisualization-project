"""Suggest original book pages for 2008/2012 historical audit events.

Candidates are search aids. A score or page link alone never constitutes an
individual medal verification; reviewer must read the final/result page.
"""
from pathlib import Path
from collections import defaultdict
import re
import sys
import pandas as pd

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'项目工作区'/'.runtime'))
import pymupdf
IN=ROOT/'交付文件'/'任务三_专题深挖'/'S2_口径的魔力'/'08_逐项外部核验'/'2008_2012小项至官方成绩册索引.csv'
OUT=IN.parent/'2008_2012官方成绩册候选页.csv'
data=pd.read_csv(IN,dtype=str).fillna('')
def norm(s):
    s=s.lower().replace('metres','m').replace('meters','m').replace('kilometres','km').replace('kilometers','km')
    s=s.replace('women’s',"women's").replace('men’s',"men's")
    s=re.sub(r'\b([0-9])\s*,\s*([0-9]{3})\b',r'\1\2',s)
    return re.sub(r'[^a-z0-9]+',' ',s).strip()
def terms(event,sport):
    if sport=='Weightlifting':
        men={'Bantamweight':'56kg','Featherweight':'62kg','Lightweight':'69kg','Middleweight':'77kg','Light-Heavyweight':'85kg','Middle-Heavyweight':'94kg','Heavyweight':'105kg','Super-Heavyweight':'105kg'}
        women={'Flyweight':'48kg','Featherweight':'53kg','Lightweight':'58kg','Middleweight':'63kg','Light-Heavyweight':'69kg','Heavyweight':'75kg','Super-Heavyweight':'75kg'}
        mapping=women if "Women's" in event else men
        for label in sorted(mapping,key=len,reverse=True):
            if event.endswith(label):return [mapping[label]]
    e=norm(event)
    s=norm(sport)
    if e.startswith(s+' '):e=e[len(s):].strip()
    stop={'individual','team','men','women','s','the','race','final','singles','doubles','relay','all','around','of'}
    return [t for t in e.split() if t not in stop and len(t)>1]
cache={}
manual_pages={(2008,"Judo Women's Heavyweight"):48,
              (2008,"Modern Pentathlon Women's Individual"):14}
rows=[]
for r in data.itertuples(index=False):
    file=str(ROOT/r.file)
    if file not in cache:
        doc=pymupdf.open(file)
        cache[file]=[(i,p.get_text()) for i,p in enumerate(doc)]
    ts=terms(r.Event,r.Sport)
    sex='women' if "Women's" in r.Event else 'men' if "Men's" in r.Event else ''
    scored=[]
    for page,text in cache[file]:
        header=norm(text[:650]);whole=norm(text)
        words=set(header.split())
        hits=sum(t in words or (t.endswith('kg') and t[:-2] in words and 'kg' in words) for t in ts)
        if not hits:continue
        ratio=hits/max(len(ts),1)
        if sex and sex not in header.split():ratio-=.15
        if 'final' in header.split():ratio+=.10
        if 'result' in header.split() or 'results' in header.split():ratio+=.05
        if 'medallists' in header.split():ratio-=.10
        scored.append((ratio,page,text[:450].replace('\n',' | ')))
    scored.sort(key=lambda x:(-x[0],x[1]))
    best=scored[:3]
    manual=manual_pages.get((int(r.Year),r.Event))
    if manual is not None:
        page_text=cache[file][manual-1][1]
        best=[(1.0,manual-1,page_text[:450].replace('\n',' | '))]+[x for x in best if x[1]!=manual-1][:2]
    rows.append({'Year':r.Year,'Event':r.Event,'优先级':r.优先级,'官方PDF':r.file,'官方PDF链接':r.pdf_url,
                 '候选页码_1基':';'.join(str(x[1]+1) for x in best),
                 '最高检索分':round(best[0][0],3) if best else 0,
                 '首选页开头':best[0][2] if best else '',
                 '核验状态':'自动定位候选页；尚未人工读取奖牌三色'})
pd.DataFrame(rows).to_csv(OUT,index=False,encoding='utf-8-sig')
print('Event page suggestions:',len(rows),'with candidates:',sum(bool(x['候选页码_1基']) for x in rows))
