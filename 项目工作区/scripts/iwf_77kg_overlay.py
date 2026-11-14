"""Reapply manually read IWF current 2016 men's 77kg ranking; IOC medals remain unknown."""
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力/08_逐项外部核验/历史910项来源覆盖总表.csv'
d=pd.read_csv(P)
i=d.index[(d.Year==2016)&(d.Event=="Weightlifting Men's Middleweight")]
assert len(i)==1
d.loc[i,'来源类型']='国际举联现行竞赛排名（IOC授牌待核）'
d.loc[i,'来源等级']='国际举联77公斤级总成绩：CHN第1、EGY第2、THA第3、KAZ取消资格；IOC奖牌重分配待核'
d.loc[i,'来源链接']='https://iwf.sport/results/results-by-events/results-by-events-upto2018/?event_id=362'
d.to_csv(P,index=False,encoding='utf-8-sig')
print('IWF 2016 men 77kg ranking marked; IOC reallocation not asserted')
