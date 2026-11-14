"""Download and validate the Paris 2024 event-level medal table."""
from pathlib import Path
from urllib.request import Request, urlopen
import hashlib, io, json
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]
URL=('https://data.smartidf.services/api/explore/v2.1/catalog/datasets/'
     'paris-2024-resultats-des-medailles-pour-chaque-discipline-olympique/exports/csv'
     '?lang=fr&timezone=Europe%2FParis&use_labels=true&delimiter=%3B')
content=urlopen(Request(URL,headers={'User-Agent':'Olympics-data-audit/1.0'}),timeout=60).read()
raw=pd.read_csv(io.BytesIO(content),sep=';',encoding='utf-8-sig')
keys=['Code_Discipline','Event']
assert raw[keys].drop_duplicates().shape[0]==329
assert raw.loc[raw.Medal_code.eq(1),keys].drop_duplicates().shape[0]==329
assert raw.duplicated().sum()==0
raw.to_csv(ROOT/'02_交付数据'/'2024逐项获奖开放数据_原始快照.csv.gz',index=False,compression='gzip',encoding='utf-8-sig')
def joined(frame,column): return ' | '.join(dict.fromkeys(frame[column].astype(str)))
fallbacks={
 ('ATH',"Women's Heptathlon"):'https://olympics.com/en/paris-2024/results/athletics/women-s-heptathlon',
 ('GRY','Group All-Around'):'https://olympics.com/en/paris-2024/results/rhythmic-gymnastics/group-all-around',
 ('GRY','Individual All-Around'):'https://olympics.com/en/paris-2024/results/rhythmic-gymnastics/individual-all-around'}
records=[]
for (code,event),group in raw.groupby(keys,sort=True):
 row={'event_id':f'{code}::{event}','discipline_code':code,'discipline':group.Discipline.iloc[0],
      'event':event,'gender':joined(group,'Gender')}
 for medal_code,prefix in [(1,'gold'),(2,'silver'),(3,'bronze')]:
  medal=group[group.Medal_code.eq(medal_code)]
  row[f'{prefix}_name']=joined(medal,'Name'); row[f'{prefix}_country_code']=joined(medal,'Country_code'); row[f'{prefix}_country']=joined(medal,'Country')
 urls=group.url_event.dropna().astype(str)
 row['official_result_url']=urls.iloc[0] if len(urls) else fallbacks.get((code,event),'')
 row['url_resolution']='upstream record' if len(urls) else 'constructed from Olympics.com canonical event path'
 row['source_tier']='政府开放数据；事件链接指向Olympics.com官方结果页'
 records.append(row)
events=pd.DataFrame(records); assert len(events)==329
events.to_csv(ROOT/'02_交付数据'/'2024官方329小项奖牌表.csv',index=False,encoding='utf-8-sig')
print(json.dumps({'rows':len(raw),'events':raw[keys].drop_duplicates().shape[0],
                  'sha256':hashlib.sha256(content).hexdigest(),'source':URL},ensure_ascii=False,indent=2))
