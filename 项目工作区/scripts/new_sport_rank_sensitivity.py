"""Recompute LA28 ensemble with the unverified new-sport bonus disabled."""
from pathlib import Path
import numpy as np
import pandas as pd

ROOT=Path(__file__).resolve().parents[2]
PRED=ROOT/'交付文件'/'任务四_开放创作'/'02_2028洛杉矶预测'
OUT=ROOT/'交付文件'/'任务四_开放创作'/'05_满分升级'/'10_新增运动历史快照回测'
OUT.mkdir(parents=True,exist_ok=True)
d=pd.read_csv(PRED/'LA2028机器学习集成预测榜.csv').set_index('NOC')
pool=d.forecast_total_programme.sum()
host=float(d.synthetic_control_host_rate.iloc[0])
neutral=d.forecast_total_neutral
ml=d.ml_project_forecast
bonus=d.new_sport_ranking_bonus
def ensemble(include_bonus):
    raw=.45*neutral+.45*ml+.10*(neutral+(bonus if include_bonus else 0))
    raw.loc['USA']*=1+host*.55
    return raw/raw.sum()*pool
on=ensemble(True);off=ensemble(False)
assert np.allclose(on,d.ensemble_total,rtol=1e-10,atol=1e-8)
o=pd.DataFrame({'代表团':d.index,'已交付情景_总奖牌':on.values,'关闭未核排名_总奖牌':off.values,
                '关闭后变化':(off-on).values,'已交付情景_名次':on.rank(method='min',ascending=False).astype(int).values,
                '关闭后名次':off.rank(method='min',ascending=False).astype(int).values})
o['名次变化']=o['关闭后名次']-o['已交付情景_名次']
o.sort_values('已交付情景_名次').to_csv(OUT/'排名信号开关敏感性.csv',index=False,encoding='utf-8-sig')
top=o.nsmallest(10,'已交付情景_名次')
maxmed=o['关闭后变化'].abs().max();maxrank=o['名次变化'].abs().max()
with (OUT/'方法与结果.md').open('a',encoding='utf-8') as f:
    f.write(f'\n## 2028排名信号关闭测试\n\n保持其余权重、主场率和奖牌池不变，把未经逐条核验的排名奖励设为0，再归一化总量。全榜最大绝对总奖牌变化 **{maxmed:.2f}枚**，最大名次变化 **{maxrank}位**。前十名变化见下表，全部逐队结果见 `排名信号开关敏感性.csv`。这不是完整模型回测，只检验未核输入对结论的影响。\n\n| 代表团 | 已交付情景 | 关闭后 | 名次变化 |\n|---|---:|---:|---:|\n')
    for r in top.itertuples(index=False):
        f.write(f'| {r.代表团} | {r.已交付情景_总奖牌:.1f} | {r.关闭未核排名_总奖牌:.1f} | {r.名次变化:+d} |\n')
print('max medal difference',maxmed,'max rank difference',maxrank)
