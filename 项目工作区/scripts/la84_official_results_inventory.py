"""Inventory primary Beijing 2008 / London 2012 results books at LA84.

These are contemporaneous organising-committee results, not the current IOC
medal table after later sanctions and reallocations.
"""
from pathlib import Path
import requests
import pandas as pd

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'资料文件'/'外部核验'/'官方成绩册索引'
OUT.mkdir(parents=True,exist_ok=True)
api='https://digital.la84.org/digital/api/search/searchterm/Official%20Results%20Book/field/title/mode/all/conn/and/maxRecords/200'
d=requests.get(api,timeout=30).json()
assert len(d['items'])==d['totalResults']
rows=[]
for item in d['items']:
    title=item['title']
    year=2008 if 'XXIX Olympiad' in title else 2012 if 'XXX Olympiad' in title and 'XXXI' not in title else None
    if not year or item['collectionAlias']!='p17103coll8':continue
    item_id=item['itemId']
    rows.append({'Year':year,'Title':title,'LA84_id':item_id,
                 'catalog_url':f'https://digital.la84.org/digital/collection/p17103coll8/id/{item_id}/',
                 'pdf_url':f'https://digital.la84.org/digital/api/collection/p17103coll8/id/{item_id}/download',
                 'source_grade':'当届组委会官方赛时成绩册；后续奖牌重分配须另核'})
z=pd.DataFrame(rows).sort_values(['Year','Title'])
assert len(z)>=70 and z.Year.value_counts().min()>=30
z.to_csv(OUT/'北京2008_伦敦2012_官方分项成绩册索引.csv',index=False,encoding='utf-8-sig')
print(len(z),z.Year.value_counts().sort_index().to_dict())
