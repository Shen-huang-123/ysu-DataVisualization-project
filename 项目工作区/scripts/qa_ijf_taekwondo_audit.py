"""Verify saved first-party HTML hashes, coverage and medal counts for IJF/WT."""
import hashlib
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力/08_逐项外部核验'
checks=[('国际柔联现行奥运逐级别核验.csv','国际柔联现行结果页',42),('世界跆拳道联盟现行奥运逐级别核验.csv','世界跆拳道联盟现行奖牌页',24)]
for name,dirname,n in checks:
 d=pd.read_csv(OUT/name)
 assert len(d)==n and not d.duplicated(['Year','Event']).any()
 for _,r in d.iterrows():
  raw=(ROOT/'资料文件/外部核验'/dirname/f'{r.Year}.html').read_bytes()
  assert hashlib.sha256(raw).hexdigest()==r.SHA256
  assert len(r.Gold.split('|'))==1 and len(r.Silver.split('|'))==1 and len(r.Bronze.split('|'))==2
b=pd.read_csv(OUT/'历史910项来源覆盖总表.csv')
assert len(b)==910 and b['来源类型'].value_counts().to_dict()=={
 'Olympics.com第三方2023抓取存档':555,'世界田联现行竞赛结果':138,
 '世界泳联现行逐项结果':137,'国际柔联现行逐级别结果':42,
 '世界跆拳道联盟现行逐级别结果':23,'官方原始补证':6,
 '官方原始补证（协会接口错误）':1,'官方原始补证（协会奖牌页错误）':1,
 'IOC现行官方修订':4,'国际举联现行竞赛排名（IOC授牌待核）':1,
 'IOC单色重分配+官方成绩册其余两色':2}
print('QA PASS: IJF 42 + WT 24 results, saved HTML hashes, 910 coverage rows')
