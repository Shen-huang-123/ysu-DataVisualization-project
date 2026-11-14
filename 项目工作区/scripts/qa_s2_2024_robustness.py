"""Validate the 2024-only sensitivity artifact and representative directions."""
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[2]
TASK=ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力'
s=pd.read_csv(TASK/'02_数据表/S2_2024逐大类剔除敏感性.csv')
d=pd.read_csv(TASK/'02_数据表/S2_2024代表团剔除敏感性.csv')
assert len(s)==36 and s.removed_family.nunique()==36
assert s.iloc[0].removed_family=='none' and s.iloc[0].official_events==329
assert len(d)==36*20 and d.groupby('removed_family').NOC.nunique().eq(20).all()
for noc,sign in [('ESP',-1),('NED',-1),('JPN',1),('UZB',1)]:
 v=d[(d.NOC==noc)&(d.removed_family!='none')].rank_shift_rows_minus_official
 assert len(v)==35 and (v*sign>0).all(),noc
assert s.iloc[1:].kendall_tau.between(.90,.95).all()
assert (TASK/'04_核心图表/S2_2024逐大类剔除稳健性.png').stat().st_size>100000
print('QA PASS: 329 official events, 35 leave-one-family-out trials, 20 top delegations, four stable directions')
