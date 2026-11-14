"""Fail if any captured aquatic final, mapping, hash, or coverage count is inconsistent."""
import hashlib
import json
from pathlib import Path
import pandas as pd

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力/08_逐项外部核验'
RAW=ROOT/'资料文件/外部核验/世界泳联现行结果JSON'
a=pd.read_csv(OUT/'世界泳联现行奥运水上项目逐项核验.csv')
m=pd.read_csv(OUT/'世界泳联与910项对照表.csv')
b=pd.read_csv(OUT/'历史910项来源覆盖总表.csv')
assert len(a)==138 and len(m)==138 and len(b)==910
assert not a.duplicated(['Year','EventId']).any()
assert not m.duplicated(['Year','Event']).any()
for _,r in a.iterrows():
    content=(RAW/f'{r.Year}_{r.EventId}.json').read_bytes()
    assert hashlib.sha256(content).hexdigest()==r.SHA256
    data=json.loads(content)
    assert data['DisciplineName']==r.DisciplineName
    assert sum(len(json.loads(r[k])) for k in ('Gold','Silver','Bronze'))>=3
for _,r in m.iterrows():
    row=b[(b.Year==r.Year)&(b.Event==r.Event)]
    assert len(row)==1
    if r.Year==2012 and r.FederationEvent=="Women's 100m Freestyle":
        assert row.iloc[0]['来源类型']=='官方原始补证（协会接口错误）'
    else:
        assert row.iloc[0]['来源链接']==r.SourceURL
assert b['来源类型'].value_counts().to_dict()=={
    'Olympics.com第三方2023抓取存档':555,'世界田联现行竞赛结果':138,
    '世界泳联现行逐项结果':137,'国际柔联现行逐级别结果':42,
    '世界跆拳道联盟现行逐级别结果':23,
    '官方原始补证':6,'官方原始补证（协会接口错误）':1,
    '官方原始补证（协会奖牌页错误）':1,'IOC现行官方修订':4,
    '国际举联现行竞赛排名（IOC授牌待核）':1,
    'IOC单色重分配+官方成绩册其余两色':2}
print('QA PASS: 138 raw event JSON hashes, 138 unique event mappings, 910 coverage rows; 1 aquatic API error adjudicated by official book')
