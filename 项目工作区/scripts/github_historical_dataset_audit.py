"""Compare a pinned GitHub Olympedia snapshot; never promote it to IOC evidence."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, io, json, re
import pandas as pd
import requests

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力/08_逐项外部核验'
OUT=BASE/'GitHub数据集实测核验_20261117'
OUT.mkdir(parents=True,exist_ok=True)
COMMIT='3ead732224293bd4ab9a8280fe01867243a54970'
URL=f'https://raw.githubusercontent.com/KeithGalli/Olympics-Dataset/{COMMIT}/results/results.csv'
SNAP=OUT/'GitHub三届原始赛果.csv.gz'
META=OUT/'数据来源与哈希.json'
if not SNAP.exists():
    response=requests.get(URL,timeout=45);response.raise_for_status()
    all_data=pd.read_csv(io.BytesIO(response.content),low_memory=False)
    chosen=all_data[all_data.Games.isin([f'{y} Summer Olympics' for y in [2008,2012,2016]])].copy()
    chosen.to_csv(SNAP,index=False,compression={'method':'gzip','mtime':0})
    metadata={'repository':'https://github.com/KeithGalli/Olympics-Dataset','commit':COMMIT,'url':URL,
              'retrieved_utc':datetime.now(timezone.utc).isoformat(),'upstream_full_csv_sha256':hashlib.sha256(response.content).hexdigest(),
              'full_rows':len(all_data),'subset_rows':len(chosen),'subset_sha256':hashlib.sha256(SNAP.read_bytes()).hexdigest(),
              'evidence':'GitHub转载的Olympedia历史抓取；与既有Olympedia对照同源，不是独立第三方或现行IOC结果。'}
    META.write_text(json.dumps(metadata,ensure_ascii=False,indent=2),encoding='utf-8')
else:
    metadata=json.loads(META.read_text(encoding='utf-8'))
    assert hashlib.sha256(SNAP.read_bytes()).hexdigest()==metadata['subset_sha256']
    chosen=pd.read_csv(SNAP,low_memory=False)

def sport(x):
    x=re.sub(r' \(.*','',x)
    if x.startswith('Cycling '):return 'Cycling'
    if x.startswith('Canoe '):return 'Canoeing'
    if x.startswith('Equestrian '):return 'Equestrianism'
    return {'Artistic Gymnastics':'Gymnastics'}.get(x,x)

def event(x,s):
    x=re.sub(r' \(Olympic\)$','',x)
    x=re.sub(r' \([CK][124]\)','',x).replace('Canadian','Canoe')
    if s=='Archery':x=x.replace(', Recurve','')
    if s=='Shooting':x=re.sub(r', (?:10|25|50) metres','',x)
    if s=='Gymnastics':
        x=x.replace('Horse Vault','Vault').replace('Individual All-Around','All-Around, Individual').replace('Team All-Around','Team').replace('Pommelled Horse','Pommel Horse')
    if s=='Cycling':
        x=x.replace(', 4,000 metres','').replace('Individual Time Trial','Time Trial, Individual').replace('Road Race, Individual','Road Race')
    if s=='Sailing':x=x.replace('-Person',' Person')
    return x.strip()

def countries(v):
    if pd.isna(v):return ''
    return '|'.join(sorted(set(re.findall(r'\b[A-Z]{3}\b',str(v)))))

chosen['Year']=chosen.Games.str[:4].astype(int)
chosen['sport_key']=chosen.Discipline.map(sport)
chosen['event_key']=[event(e,s) for e,s in zip(chosen.Event,chosen.sport_key)]
for discipline, label in [('Dressage','Dressage'),('Jumping','Jumping'),('Eventing','Eventing')]:
    mask=chosen.Discipline.str.startswith('Equestrian '+discipline)
    chosen.loc[mask,'event_key']=label+' / '+chosen.loc[mask,'event_key']
inventory=chosen[['Year','sport_key','Event','event_key']].drop_duplicates()
# Identity mapping uses names and sport only, never medal agreement.
lookup={key:g for key,g in chosen.groupby(['Year','sport_key','event_key'])}
reference=pd.read_csv(BASE/'Olympedia独立交叉核验/历史555项独立交叉对照.csv').fillna('')
rows=[]
for r in reference.to_dict('records'):
    key=(r['Year'],r['Sport'],event(r['Event_olympedia'],r['Sport']))
    if r['Sport']=='Equestrianism':
        label='Dressage' if 'Dressage' in r['Event'] else ('Jumping' if 'Jumping' in r['Event'] else 'Eventing')
        key=(key[0],key[1],label+' / '+key[2])
    g=lookup.get(key)
    row={k:r[k] for k in ['Year','Sport','Event','Event_olympedia','event_url']}
    row['配对方法']='预定义名称归一，届次+运动+小项严格匹配'
    if g is None:
        row['状态']='未匹配，保留人工检查';rows.append(row);continue
    distinct=g.Event.nunique()
    if distinct!=1:
        row['状态']='名称归一碰撞，禁止自动核验';rows.append(row);continue
    row['GitHub小项原名']=g.Event.iloc[0]
    equal=[]
    for medal in ['Gold','Silver','Bronze']:
        value=countries(' '.join(g.loc[g.Medal.eq(medal),'NOC'].dropna().astype(str)))
        ref=countries(r[f'{medal}_olympedia'])
        row[f'{medal}_github']=value;row[f'{medal}_olympedia']=ref
        equal.append(value==ref)
    row['状态']='三色集合一致（同源快照）' if all(equal) else '存在差异，不能自动裁定'
    rows.append(row)
result=pd.DataFrame(rows)
assert len(result)==555 and not result.duplicated(['Year','Event']).any()
result.to_csv(OUT/'555项GitHub快照对照.csv',index=False,encoding='utf-8-sig')
result[~result['状态'].eq('三色集合一致（同源快照）')].to_csv(OUT/'差异与未匹配清单.csv',index=False,encoding='utf-8-sig')
inventory.to_csv(OUT/'原始小项名称及归一映射.csv',index=False,encoding='utf-8-sig')
summary={'total':555,'status':result['状态'].value_counts().to_dict(),'current_ioc_verified_added':0,
         'method':'按小项/颜色汇总代表团集合，团队成员不重复计数；不比较运动员行总量，不用奖牌一致性选择配对。',
         'limitations':'同一国家同色多枚在集合中折叠；这不是完整奖牌枚数核验。同源快照一致不构成独立证据。'}
(OUT/'核验摘要.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False,indent=2))
