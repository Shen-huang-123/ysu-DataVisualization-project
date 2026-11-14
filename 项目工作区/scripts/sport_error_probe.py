"""Sport-level historical diagnostic on a single athlete-medal-row unit."""
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from task2_localization import SPORT_ZH

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'交付文件'/'任务四_开放创作'/'05_满分升级'/'08_历史误差归因'
cube=pd.read_csv(ROOT/'交付文件'/'任务一_数据体检'/'99_运行生成'/'analysis_cube.csv')
row=cube[cube.Medal.ne('No medal')].groupby(['Year','NOC','sport_family'],as_index=False).records.sum()
records=[]
for target in [2012,2016,2024]:
    prior=row[row.Year.lt(target)]
    nocs=prior.groupby('NOC').records.sum().nlargest(100).index
    sports=prior.groupby('sport_family').records.sum().nlargest(45).index
    years=[y for y in [2000,2004,2008,2012,2016,2020,2024] if y<=target]
    idx=pd.MultiIndex.from_product([years,nocs,sports],names=['Year','NOC','sport_family'])
    p=row.set_index(['Year','NOC','sport_family']).reindex(idx,fill_value=0).reset_index()
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
    out=p.loc[test,['NOC','sport_family','records','lag1','lag2']].copy()
    out['model_raw']=np.maximum(0,.6*rf.predict(X.loc[test])+.4*gb.predict(X.loc[test]))
    out['baseline_raw']=np.maximum(0,.7*out.lag1+.3*out.lag2+.15*(out.lag1-out.lag2))
    # Both models use only earlier Games, no target sport pool normalization.
    out['Year']=target
    records.append(out)
detail=pd.concat(records,ignore_index=True)
detail['model_abs_error']=(detail.model_raw-detail.records).abs()
detail['baseline_abs_error']=(detail.baseline_raw-detail.records).abs()
detail['gain']=detail.baseline_abs_error-detail.model_abs_error
detail.to_csv(OUT/'运动员行口径逐队逐运动误差.csv',index=False,encoding='utf-8-sig')
by=detail.groupby(['Year','sport_family']).agg(cells=('NOC','size'),actual_rows=('records','sum'),baseline_MAE=('baseline_abs_error','mean'),model_MAE=('model_abs_error','mean'),mean_gain=('gain','mean')).reset_index()
by.to_csv(OUT/'逐运动行口径误差.csv',index=False,encoding='utf-8-sig')
summ=detail.groupby('Year').agg(cells=('NOC','size'),baseline_MAE=('baseline_abs_error','mean'),model_MAE=('model_abs_error','mean'),mean_gain=('gain','mean')).reset_index()
summ.to_csv(OUT/'运动员行口径总览.csv',index=False,encoding='utf-8-sig')
active=detail[(detail.records.gt(0))|(detail.lag1.gt(0))|(detail.lag2.gt(0))].groupby('Year').agg(cells=('NOC','size'),baseline_MAE=('baseline_abs_error','mean'),model_MAE=('model_abs_error','mean')).reset_index()
active.to_csv(OUT/'曾有获奖运动单元误差.csv',index=False,encoding='utf-8-sig')
weighted=by.groupby('sport_family').agg(actual_rows=('actual_rows','sum'),mean_gain=('mean_gain','mean'),editions=('Year','size')).query('editions==3 and actual_rows>=20').sort_values('mean_gain')
fig,ax=plt.subplots(figsize=(11,7),facecolor='#f2eee5');ax.set_facecolor('#f2eee5')
view=pd.concat([weighted.head(7),weighted.tail(7)]).drop_duplicates().sort_values('mean_gain')
ax.barh([SPORT_ZH.get(x,x) for x in view.index],view.mean_gain,color=['#b65f41' if x<0 else '#1b7487' for x in view.mean_gain]);ax.axvline(0,color='#173447');ax.spines[:].set_visible(False);ax.tick_params(length=0)
ax.set_xlabel('逐队逐运动平均绝对误差改善（运动员获奖行）')
fig.text(.08,.95,'项目模型在不同运动并非都更准',fontsize=22,weight='bold',color='#173447')
fig.text(.08,.015,'仅运动员获奖行口径；目标运动的最终规模没有用于归一化，不可视作小项奖牌回测。',fontsize=9,color='#526973')
fig.tight_layout(rect=[0,.04,1,.88]);fig.savefig(OUT/'逐运动同单位误差.png',dpi=180,facecolor=fig.get_facecolor());plt.close(fig)
md=OUT/'误差归因说明.md'
s=md.read_text(encoding='utf-8').split('\n## 运动员行口径补充验证')[0]
s+='\n## 运动员行口径补充验证\n\n为补足项目维度，额外对 2012、2016、2024 各届赛前训练项目模型，并在**逐队×逐运动的运动员获奖行**同一单位比较项目模型与简单上一届/上两届基线。两者均不使用目标届运动奖牌池归一化。该检验与前述官方/代理小项总量回测是**两套不同统计单位**，不能合并为同一 MAE，也不能声称已验证 2028 新增运动小项奖牌。\n\n'
s+='| 届次 | 单元数 | 行口径基线MAE | 行口径项目模型MAE |\n|---|---:|---:|---:|\n'
for r in summ.itertuples():s+=f'| {r.Year} | {r.cells} | {r.baseline_MAE:.2f} | {r.model_MAE:.2f} |\n'
s+='\n运动分类是清洗后的体育大类；仅覆盖历史前100代表团和前45运动以及训练时可见的类别。模型输出未经最终2028集成权重、主场和资格场景调整。逐运动结果与逐队逐运动误差在本目录公开。\n'
s+='\n大量逐队逐运动单元在三届都为零，简单基线可准确给零。为免零单元主导结论，再看目标届或此前两届任一获奖的单元：2012与2016项目模型仍较差，但2024模型MAE为2.65行，优于基线2.75行。此“活跃”定义含目标结果，**只可作赛后诊断**，不能用来赛前筛选模型。\n'
md.write_text(s,encoding='utf-8')
page=OUT/'index.html';html=page.read_text(encoding='utf-8')
insert='<h2>运动层面：另用运动员获奖行做同单位检验</h2><p>这张图比较历史赛前项目模型与简单历史基线。它与上方代表团小项奖牌回测使用不同统计单位，不能直接合并。</p><img src="逐运动同单位误差.png" alt="逐运动运动员行预测误差改善"><p><a href="逐运动行口径误差.csv">逐运动数据</a>　<a href="运动员行口径逐队逐运动误差.csv">逐队逐运动明细</a></p>'
if '逐运动同单位误差.png' not in html:html=html.replace('<div class="note">',insert+'<div class="note">',1)
html=html.replace('当前历史回测没有同单位运动级真值和预测，因此不声称已经完成运动级误差归因。','上方另做了运动员获奖行同单位验证：全体单元三届均不如简单基线；但在有历史或目标届获奖的单元中，2024项目模型反而改善。后者是事后分组，不能赛前用于选模，也不能替代官方小项奖牌的运动级回测。')
page.write_text(html,encoding='utf-8')
print(summ.to_string(index=False))
