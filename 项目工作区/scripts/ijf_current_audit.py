"""Read 2008/12/16 IJF Olympic category standings and preserve source HTML."""
import hashlib,re
from pathlib import Path
import pandas as pd,requests
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力/08_逐项外部核验'
RAW=ROOT/'资料文件/外部核验/国际柔联现行结果页'
RAW.mkdir(parents=True,exist_ok=True)
SLUG={2008:'oi_2008',2012:'oly2012',2016:'oly2016'}
WEIGHT={'-60':'Extra-Lightweight','-66':'Half-Lightweight','-73':'Lightweight','-81':'Half-Middleweight','-90':'Middleweight','-100':'Half-Heavyweight','+100':'Heavyweight','-48':'Extra-Lightweight','-52':'Half-Lightweight','-57':'Lightweight','-63':'Half-Middleweight','-70':'Middleweight','-78':'Half-Heavyweight','+78':'Heavyweight'}
rows=[]
for year,slug in SLUG.items():
 url=f'https://ijf.org/events/{slug}/results'
 r=requests.get(url,timeout=30);r.raise_for_status()
 raw=r.content;(RAW/f'{year}.html').write_bytes(raw)
 soup=BeautifulSoup(raw,'html.parser')
 seen=set()
 for div in soup.find_all('div',class_='flex flex-col'):
  text=div.get_text(' ',strip=True)
  m=re.match(r'^(Men|Women)\s+([+-]\d+)\s+1\s+',text)
  if not m:continue
  gender,weight=m.groups()
  if (gender,weight) in seen:continue
  seen.add((gender,weight))
  medals={'Gold':[],'Silver':[],'Bronze':[]}
  for a in div.find_all('a',recursive=True):
   t=a.get_text(' ',strip=True)
   rank=re.match(r'^([123])\s+',t)
   flag=a.find('img',alt=re.compile('^[A-Z]{3}$'))
   if rank and flag:
    medals[{'1':'Gold','2':'Silver','3':'Bronze'}[rank.group(1)]].append(flag['alt'])
  if all(medals.values()):
   rows.append({'Year':year,'Event':f"Judo {gender}'s {WEIGHT[weight]}",'Category':f'{gender} {weight}',
                'Gold':'|'.join(medals['Gold']),'Silver':'|'.join(medals['Silver']),'Bronze':'|'.join(medals['Bronze']),
                'SourceURL':url,'SHA256':hashlib.sha256(raw).hexdigest()})
 print(year,'categories',len(seen),'extracted',sum(x['Year']==year for x in rows))
d=pd.DataFrame(rows)
d.to_csv(OUT/'国际柔联现行奥运逐级别核验.csv',index=False,encoding='utf-8-sig')
print(d.head(3).to_string(index=False))
