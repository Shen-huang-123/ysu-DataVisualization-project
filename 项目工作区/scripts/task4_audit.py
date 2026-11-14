from pathlib import Path
import json,re
import numpy as np
import pandas as pd
from PIL import Image
ROOT=Path(__file__).resolve().parents[2]; TASK=ROOT/'交付文件'/'任务四_开放创作'; checks=[]
def add(n,ok,d=''): checks.append({'check':n,'passed':bool(ok),'detail':str(d)})
required=[TASK/'index.html',TASK/'01_交互式Dashboard'/'index.html',TASK/'03_数据新闻'/'index.html',TASK/'06_赛后验收单'/'index.html',TASK/'02_2028洛杉矶预测'/'index.html',TASK/'02_2028洛杉矶预测'/'LA2028奖牌预测完整榜.csv',TASK/'02_2028洛杉矶预测'/'LA2028机器学习集成预测榜.csv',TASK/'02_2028洛杉矶预测'/'代表团_项目级预测.csv',TASK/'02_2028洛杉矶预测'/'历史回测逐队结果.csv',TASK/'02_2028洛杉矶预测'/'预测方法与验证方案.md',TASK/'05_满分升级'/'新增项目权威排名特征.csv',TASK/'05_满分升级'/'主场效应合成对照.csv',TASK/'05_满分升级'/'升级模型验证摘要.csv']
for p in required:add('文件存在:'+p.name,p.exists() and p.stat().st_size>100,p.stat().st_size if p.exists() else 0)
pred=pd.read_csv(TASK/'02_2028洛杉矶预测'/'LA2028奖牌预测完整榜.csv'); add('预测榜非空',len(pred)>100,len(pred)); add('区间顺序正确',((pred.lower80<=pred.forecast_total_programme)&(pred.forecast_total_programme<=pred.upper80)).all()); add('资格未决有标注',(pred.loc[pred.NOC.eq('RUS'),'eligibility_note']=='资格情景未决').all()); add('官方排名字段存在','official_rank' in pred.columns)
pool=353+354+round(353*385/329); add('奖牌池守恒',abs(pred.forecast_total_programme.sum()-pool)<1e-6,pred.forecast_total_programme.sum())
back=pd.read_csv(TASK/'02_2028洛杉矶预测'/'模型回测摘要.csv'); add('回测误差披露',0<float(back.backtest_mae_all_nocs.iloc[0])<10,back.backtest_mae_all_nocs.iloc[0])
ens=pd.read_csv(TASK/'02_2028洛杉矶预测'/'LA2028机器学习集成预测榜.csv'); add('机器学习集成字段完整',{'ml_project_forecast','new_sport_ranking_bonus','synthetic_control_host_rate','ensemble_total','ensemble_rank'}.issubset(ens.columns)); add('集成奖牌池守恒',abs(ens.ensemble_total.sum()-pool)<1e-6,ens.ensemble_total.sum())
rank=pd.read_csv(TASK/'05_满分升级'/'新增项目权威排名特征.csv'); add('五项新增运动均有权威特征',rank['新增运动'].nunique()==5,rank['新增运动'].nunique()); add('新增项目有快照和来源',rank[['一手来源','快照日期']].notna().all().all())
host=pd.read_csv(TASK/'05_满分升级'/'主场效应合成对照.csv'); add('主场合成对照案例充足',len(host)>=5,len(host))
for p in (TASK/'02_2028洛杉矶预测'/'核心图表').glob('*.png'):
    try:
        with Image.open(p) as im:w,h=im.size
        add('图表完整:'+p.name,w>=1200 and h>=800,f'{w}×{h}')
    except Exception as e:add('图表完整:'+p.name,False,e)
for p in [TASK/'index.html',TASK/'01_交互式Dashboard'/'index.html',TASK/'02_2028洛杉矶预测'/'index.html',TASK/'03_数据新闻'/'index.html',TASK/'06_赛后验收单'/'index.html']:
    t=p.read_text(encoding='utf-8'); add('中文界面:'+p.parent.name,'lang="zh-CN"' in t and not re.search(r'>\s*(Dashboard|Overview|Download|Search|Filter)\s*<',t,re.I))
result={'passed':all(x['passed'] for x in checks),'checks':len(checks),'failed':sum(not x['passed'] for x in checks),'items':checks}; (TASK/'04_质量验收'/'任务四自动验收报告.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8'); print(json.dumps({k:result[k] for k in ['passed','checks','failed']},ensure_ascii=False,indent=2)); raise SystemExit(0 if result['passed'] else 1)
