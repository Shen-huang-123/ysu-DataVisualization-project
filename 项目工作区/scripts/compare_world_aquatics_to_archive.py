"""Compare captured federation medal tags to the old Olympics.com archive by event."""
import json
from pathlib import Path
import pandas as pd

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力/08_逐项外部核验'
a=pd.read_csv(OUT/'世界泳联现行奥运水上项目逐项核验.csv')
m=pd.read_csv(OUT/'世界泳联与910项对照表.csv')
o=pd.read_csv(OUT/'逐小项三色对照.csv')
d=m.merge(a,left_on=['Year','FederationEvent','SourceURL'],right_on=['Year','DisciplineName','SourceURL'],validate='one_to_one')
d=d.merge(o,left_on=['Year','Event'],right_on=['Year','Event_proxy'],validate='one_to_one')
rows=[]
for _,r in d.iterrows():
    record={'Year':r.Year,'Event':r.Event,'SourceURL':r.SourceURL}
    for color,field in [('G','Gold'),('S','Silver'),('B','Bronze')]:
        current=sorted({x['NOC'] for x in json.loads(r[field]) if x.get('NOC')})
        archive=sorted(set(str(r[f'{field}_archive']).split('|'))) if pd.notna(r[f'{field}_archive']) else []
        record[f'{field}_current']='|'.join(current)
        record[f'{field}_archive']='|'.join(archive)
        record[f'{field}_same']=current==archive
    rows.append(record)
z=pd.DataFrame(rows)
z['三色一致']=z[['Gold_same','Silver_same','Bronze_same']].all(axis=1)
z.to_csv(OUT/'世界泳联现行结果与旧存档三色差异.csv',index=False,encoding='utf-8-sig')
print('rows',len(z),'match',z['三色一致'].sum(),'disagree',(~z['三色一致']).sum())
print(z[~z['三色一致']][['Year','Event','Gold_current','Gold_archive','Silver_current','Silver_archive','Bronze_current','Bronze_archive']].to_string(index=False))
