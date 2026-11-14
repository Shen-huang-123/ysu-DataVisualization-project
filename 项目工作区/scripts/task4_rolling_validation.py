"""Historical replay of the transferable LA28 forecast core on event-medal units."""
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

ROOT=Path(__file__).resolve().parents[2]
PRED=ROOT/'交付文件'/'任务四_开放创作'/'02_2028洛杉矶预测'
OUT=ROOT/'交付文件'/'任务四_开放创作'/'05_满分升级'
cube=pd.read_csv(ROOT/'交付文件'/'任务一_数据体检'/'99_运行生成'/'analysis_cube.csv')
row_med=cube[cube.Medal.ne('No medal')].groupby(['Year','NOC','sport_family'],as_index=False).records.sum()
raw=pd.read_csv(ROOT/'交付文件'/'任务一_数据体检'/'02_交付数据'/'归一数据_保留原始字段.csv.gz',low_memory=False)
raw=raw[raw.Medal.isin(['Gold','Silver','Bronze'])]
official=pd.read_csv(ROOT/'交付文件'/'任务一_数据体检'/'02_交付数据'/'2024官方329小项奖牌表.csv')

ev=[]
for year in [2000,2004,2008,2012,2016]:
    t=raw[raw.Year.eq(year)][['NOC','Event','Medal']].drop_duplicates().groupby('NOC').size().rename('medals').reset_index()
    t['Year']=year;ev.append(t)
rows=[]
for _,r in official.iterrows():
    for field in ['gold_country_code','silver_country_code','bronze_country_code']:
        for noc in str(r[field]).replace(',','|').split('|'):
            noc=noc.strip()
            if noc and noc!='nan':rows.append(noc)
t=pd.Series(rows).value_counts().rename_axis('NOC').reset_index(name='medals');t['Year']=2024;ev.append(t)
events=pd.concat(ev,ignore_index=True)

def baseline(target):
    hist=events[events.Year.lt(target)]
    ys=sorted(hist.Year.unique())[-3:]
    w=np.array([.2,.3,.5])[-len(ys):];w=w/w.sum()
    wide=hist.pivot(index='NOC',columns='Year',values='medals').reindex(columns=ys).fillna(0)
    score=wide.to_numpy()@w
    if len(ys)>1:score+=.15*(wide[ys[-1]]-wide[ys[-2]]).to_numpy()
    score=pd.Series(np.maximum(0,score),index=wide.index)
    pool=float(events.loc[events.Year.eq(target),'medals'].sum())
    return score/score.sum()*pool

def project(target, pool):
    prior=row_med[row_med.Year.lt(target)]
    nocs=prior.groupby('NOC').records.sum().nlargest(100).index
    sports=prior.groupby('sport_family').records.sum().nlargest(45).index
    years=[y for y in [2000,2004,2008,2012,2016,2020,2024] if y<=target]
    idx=pd.MultiIndex.from_product([years,nocs,sports],names=['Year','NOC','sport_family'])
    p=row_med.set_index(['Year','NOC','sport_family']).reindex(idx,fill_value=0).reset_index()
    p['lag1']=p.groupby(['NOC','sport_family']).records.shift(1)
    p['lag2']=p.groupby(['NOC','sport_family']).records.shift(2)
    p['trend']=p.lag1-p.lag2
    p['noc_lag']=p.groupby(['NOC','Year']).lag1.transform('sum')
    p['sport_lag']=p.groupby(['sport_family','Year']).lag1.transform('sum')
    p=p.dropna().copy()
    X=pd.get_dummies(p[['NOC','sport_family','lag1','lag2','trend','noc_lag','sport_lag']],columns=['NOC','sport_family'])
    train=p.Year.lt(target);test=p.Year.eq(target)
    rf=RandomForestRegressor(n_estimators=100,min_samples_leaf=3,max_features=.65,random_state=28,n_jobs=-1)
    gb=GradientBoostingRegressor(n_estimators=100,max_depth=2,learning_rate=.035,loss='huber',random_state=28)
    rf.fit(X.loc[train],p.loc[train,'records']);gb.fit(X.loc[train],p.loc[train,'records'])
    pred=np.maximum(0,.6*rf.predict(X.loc[test])+.4*gb.predict(X.loc[test]))
    score=pd.DataFrame({'NOC':p.loc[test,'NOC'].to_numpy(),'pred':pred}).groupby('NOC').pred.sum()
    return score/score.sum()*pool

records=[];summaries=[]
for target in [2012,2016,2024]:
    actual=events[events.Year.eq(target)].set_index('NOC').medals
    pool=float(actual.sum());b=baseline(target);m=project(target,pool)
    idx=actual.index.union(b.index).union(m.index)
    z=pd.DataFrame({'actual':actual.reindex(idx).fillna(0),'baseline':b.reindex(idx).fillna(0),'project':m.reindex(idx).fillna(0)})
    z['blend']=.55*z.baseline+.45*z.project
    z['Year']=target;z['NOC']=z.index;records.append(z.reset_index(drop=True))
    for name in ['baseline','blend']:
        err=(z[name]-z.actual).abs()
        summaries.append({'Year':target,'model':name,'NOCs':len(z),'MAE_all':err.mean(),
                          'MAE_actual_ge5':err[z.actual.ge(5)].mean(),
                          'RMSE_all':np.sqrt(((z[name]-z.actual)**2).mean()),
                          'top10_overlap':len(set(z.nlargest(10,name).index)&set(z.nlargest(10,'actual').index)),
                          'observation_unit':'2024 official events; pre-2020 NOC-Event-Medal proxy'})
pd.concat(records).to_csv(OUT/'滚动留出逐队同口径结果.csv',index=False,encoding='utf-8-sig')
summary=pd.DataFrame(summaries)
summary.to_csv(OUT/'滚动留出同口径比较.csv',index=False,encoding='utf-8-sig')
with (OUT/'滚动留出验证说明.md').open('w',encoding='utf-8') as f:
    f.write('# 可迁移预测核心的滚动留出验证\n\n')
    f.write('分别留出 2012、2016、2024，训练时不使用目标届奖牌结果；全程以代表团小项奖牌总量评价。2024 使用已核验的官方 329 小项，历史届次使用 `NOC–Event–Medal` 代理，不能称为逐项 IOC 官方核验。\n\n')
    f.write('回放模型为 55% 历史基线 + 45% 项目级机器学习。最终 2028 版本中的 10% 新增运动信号，在这些历史届次没有同类项目与当时排名，因此回放时该分量退回基线；主场调整也不纳入这一可迁移核心的检验。故此表**不是完整 2028 最终集成的端到端验证**。\n\n')
    f.write('| 届次 | 模型 | 全体MAE | 实际≥5枚MAE | 前十重合 |\n|---|---|---:|---:|---:|\n')
    for r in summary.itertuples():f.write(f'| {r.Year} | {"透明基线" if r.model=="baseline" else "55/45可迁移核心"} | {r.MAE_all:.2f} | {r.MAE_actual_ge5:.2f} | {r.top10_overlap}/10 |\n')
    f.write('\n2012 年混合模型明显劣于基线；2016 年近似持平；2024 年误差降低，但前十重合从 9 降至 8。权重没有用这三次回放重新挑选。各届归一化使用目标届最终奖牌池，属于事后已知规模，因而此回测对真实赛前预测略有利；2028 年真实表现及区间覆盖必须赛后验收。\n')
html_rows=''.join(f'<tr><td>{r.Year}</td><td>{"透明基线" if r.model=="baseline" else "55/45可迁移核心"}</td><td>{r.MAE_all:.2f}</td><td>{r.MAE_actual_ge5:.2f}</td><td>{r.top10_overlap}/10</td></tr>' for r in summary.itertuples())
(OUT/'滚动留出验证.html').write_text(f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>2028预测历史回放</title><style>body{{margin:0;background:#eee9df;color:#182d43;font-family:"Microsoft YaHei",sans-serif}}main{{max-width:980px;margin:auto;padding:64px 24px}}h1{{font-size:clamp(38px,6vw,68px)}}p{{line-height:1.8}}table{{width:100%;border-collapse:collapse;background:#fffaf2;border-radius:18px;overflow:hidden}}td,th{{padding:14px;text-align:left;border-bottom:1px solid #ddd3c5}}.call{{padding:26px;border-radius:22px;background:#173958;color:#fff;margin:30px 0}}a{{color:#216399}}</style></head><body><main><small>洛杉矶 2028 / 历史回放</small><h1>模型进步，<br>必须经得起旧届次。</h1><p>依次留出 2012、2016、2024 年，用赛前可用的历史训练，统一在代表团小项奖牌总量上评分。2024 使用官方小项结果，较早届次使用项目代理。</p><table><thead><tr><th>留出届次</th><th>模型</th><th>全体MAE</th><th>实际≥5枚MAE</th><th>前十重合</th></tr></thead><tbody>{html_rows}</tbody></table><div class="call"><h2>结果并非一路领先</h2><p>2012 年混合模型明显更差；2016 年接近；2024 年总量误差改善，但前十重合少一席。这一反例反对“复杂模型必然更准”的结论。</p><p>历史回放只覆盖可迁移的 55% 基线＋45% 项目模型。2028 的新增运动排名信号与主场调整没有同类历史情景，不能冒充完整最终集成模型的端到端验证。各届用最终奖牌池归一化，较真实赛前预测略乐观。</p></div><p><a href="滚动留出逐队同口径结果.csv">下载逐队结果</a>　<a href="滚动留出同口径比较.csv">下载汇总</a>　<a href="../02_2028洛杉矶预测/index.html">返回预测方法</a></p></main></body></html>''',encoding='utf-8')
method=PRED/'预测方法与验证方案.md'
mt=method.read_text(encoding='utf-8').split('\n\n### 可迁移核心滚动回放')[0]
mt+='\n\n### 可迁移核心滚动回放\n\n[查看2012、2016、2024三次同口径留出验证](../05_满分升级/滚动留出验证.html)。2012年混合模型劣于基线，2016年近似持平，2024年平均误差改善但前十重合下降。此回放不覆盖新增运动排名与主场情景，目标奖牌池事后已知；不得当作完整2028集成的独立区间校准。\n'
method.write_text(mt,encoding='utf-8')
print(summary[['Year','model','MAE_all','MAE_actual_ge5','top10_overlap']].to_string(index=False))
