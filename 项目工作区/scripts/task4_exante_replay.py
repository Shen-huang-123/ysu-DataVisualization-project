"""Historical replay with pre-target medal-pool and host assumptions."""
from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from task2_localization import NOC_ZH

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'交付文件'/'任务四_开放创作'/'05_满分升级'/'09_赛前条件回放'
OUT.mkdir(parents=True,exist_ok=True)
ROLL=OUT.parent/'滚动留出逐队同口径结果.csv'
raw=pd.read_csv(ROOT/'交付文件'/'任务一_数据体检'/'02_交付数据'/'归一数据_保留原始字段.csv.gz',low_memory=False)
raw=raw[raw.Medal.isin(['Gold','Silver','Bronze'])]
counts={year:len(raw[raw.Year.eq(year)][['NOC','Event','Medal']].drop_duplicates()) for year in [2000,2004,2008,2012,2016]}
official=pd.read_csv(ROOT/'交付文件'/'任务一_数据体检'/'02_交付数据'/'2024官方329小项奖牌表.csv')
official_codes=[]
for _,r in official.iterrows():
    for field in ['gold_country_code','silver_country_code','bronze_country_code']:
        official_codes.extend([x.strip() for x in str(r[field]).replace(',','|').split('|') if x.strip() and x.strip()!='nan'])
counts[2024]=len(official_codes)
source=pd.read_csv(ROLL)
host=pd.read_csv(OUT.parent/'主场效应合成对照.csv')
hosts={2012:'GBR',2016:'BRA',2024:'FRA'}
identity={'URS','EUN','ROC','AIN','EOR','IOA'}
records=[];meta=[]
for year in [2012,2016,2024]:
    prior=[y for y in sorted(counts) if y<year]
    tail=prior[-3:]
    diffs=np.diff([counts[y] for y in tail])
    pool_pred=max(1,counts[tail[-1]]+float(np.median(diffs)))
    pool_true=counts[year]
    history_host=host[host.Year.lt(year)]
    rate=float(np.clip(history_host.EffectRate.median(),0,.18)) if len(history_host) else 0.
    z=source[source.Year.eq(year)].copy().set_index('NOC')
    assert np.isclose(z.baseline.sum(),pool_true) and np.isclose(z.project.sum(),pool_true)
    b=z.baseline*pool_pred/pool_true
    p=z.project*pool_pred/pool_true
    core=.55*b+.45*p
    # The host is known before Games; the effect estimate uses only earlier hosts.
    with_host=core.copy()
    if hosts[year] in with_host.index:with_host.loc[hosts[year]]*=1+rate*.55
    with_host=with_host/with_host.sum()*pool_pred
    # Identity eligibility is uncertain: carry-forward and exclusion are scenarios, not facts.
    restricted=with_host.copy()
    mask=restricted.index.isin(identity)
    restricted.loc[mask]=0
    if restricted.sum()>0:restricted=restricted/restricted.sum()*pool_pred
    variants={'透明基线_赛前奖牌池':b,'混合核心_赛前奖牌池':core,'混合核心_加主场':with_host,'混合核心_资格受限':restricted}
    for name,v in variants.items():
        for noc,val in v.items():records.append({'Year':year,'NOC':noc,'情景':name,'预测小项奖牌':val,'实际小项奖牌':z.loc[noc,'actual'],'绝对误差':abs(val-z.loc[noc,'actual'])})
    meta.append({'Year':year,'赛前可见的最近三届':','.join(map(str,tail)),'赛前估计奖牌池':pool_pred,'实际奖牌池_仅评分':pool_true,'估计误差':pool_pred-pool_true,'主办代表团':hosts[year],'仅用此前主办案例数':len(history_host),'主场率_赛前估计':rate,'资格受限代码':','.join(sorted(identity))})
detail=pd.DataFrame(records)
detail.to_csv(OUT/'赛前条件逐队回放.csv',index=False,encoding='utf-8-sig')
pd.DataFrame(meta).to_csv(OUT/'赛前条件与奖牌池.csv',index=False,encoding='utf-8-sig')
summary=[]
for (year,scenario),g in detail.groupby(['Year','情景']):
    actual=g.set_index('NOC')['实际小项奖牌'];pred=g.set_index('NOC')['预测小项奖牌']
    summary.append({'Year':year,'情景':scenario,'MAE_全体':g.绝对误差.mean(),'MAE_实际至少5枚':g[g.实际小项奖牌.ge(5)].绝对误差.mean(),'RMSE_全体':np.sqrt(np.mean((g.预测小项奖牌-g.实际小项奖牌)**2)),'前十重合':len(set(actual.nlargest(10).index)&set(pred.nlargest(10).index))})
summary=pd.DataFrame(summary).sort_values(['Year','情景'])
summary.to_csv(OUT/'赛前条件评分.csv',index=False,encoding='utf-8-sig')
fig,ax=plt.subplots(figsize=(11,6),facecolor='#f2eee5');ax.set_facecolor('#f2eee5')
scenarios=['透明基线_赛前奖牌池','混合核心_赛前奖牌池','混合核心_加主场','混合核心_资格受限']
labels=['透明基线','混合核心','加主场','资格受限']
x=np.arange(3);width=.19
for i,(sc,label) in enumerate(zip(scenarios,labels)):
    vals=summary[summary.情景.eq(sc)].sort_values('Year').MAE_全体.values
    ax.bar(x+(i-1.5)*width,vals,width,label=label)
ax.set_xticks(x,[str(y) for y in [2012,2016,2024]]);ax.set_ylabel('逐代表团 MAE（小项奖牌代理/官方枚数）')
ax.set_ylim(0,summary.MAE_全体.max()*1.25);ax.legend(frameon=False,ncol=4,loc='upper center',bbox_to_anchor=(.5,1.1))
ax.spines[['top','right']].set_visible(False);ax.grid(axis='y',color='#d7d4cb');ax.set_axisbelow(True)
fig.text(.08,.96,'只用赛前条件，成绩还站得住吗？',fontsize=22,weight='bold',color='#173447')
fig.text(.08,.025,'奖牌池由前届趋势估计；主场率只用此前案例；资格受限为压力情景，非实际参赛认定。',fontsize=9,color='#536b73')
fig.tight_layout(rect=[0,.06,1,.87]);fig.savefig(OUT/'赛前条件回放.png',dpi=180,facecolor=fig.get_facecolor());plt.close(fig)
pool=pd.DataFrame(meta)
md='# 2028模型：更接近赛前信息条件的历史回放\n\n'
md+='三届分别只使用目标届之前的奖牌池历史：最近三届的奖牌总量，以最近两个变化的中位数外推目标届总池。历史2012、2016以`NOC–Event–Medal`代理，2024为外部逐项官方表。既有滚动留出模型的逐队**分布**按赛前估计奖牌池重新缩放；不在建模中使用目标届总池，目标届实际池只用于评分。\n\n'
md+='主办代表团身份在赛前已知；主场率只由当时此前的合成对照案例估计并按正式模型收缩45%。资格设“沿用预测分布”和“排除特定历史身份代码”两种条件情景，均不能代表实际资格决定；2024的ROC→AIN身份迁移无法仅凭旧奖牌表预测。新增运动10%分量没有可比历史排名快照，回放时退回透明基线，所以此处仍不是完整2028集成的端到端验证。\n\n'
md+='| 届次 | 赛前估计奖牌池 | 实际池（只评分） | 估计误差 | 主场率仅用此前案例 |\n|---|---:|---:|---:|---:|\n'
for r in pool.itertuples():md+=f'| {r.Year} | {r.赛前估计奖牌池:.0f} | {r.实际奖牌池_仅评分:.0f} | {r.估计误差:+.0f} | {r.主场率_赛前估计:.1%}（{r.仅用此前主办案例数}例） |\n'
md+='\n## 逐届评分\n\n| 届次 | 情景 | 全体MAE | ≥5枚MAE | 前十重合 |\n|---|---|---:|---:|---:|\n'
for r in summary.itertuples():md+=f'| {r.Year} | {r.情景} | {r.MAE_全体:.2f} | {r.MAE_实际至少5枚:.2f} | {r.前十重合}/10 |\n'
md+='\n**解释限制**：项目模型训练输入仍为运动员获奖行，输出只在代表团总量上与小项实际比较；历史小项代理存在命名漂移。2012赛前主场率样本仅1例，三次历史中位估计均触及预先设置的18%上限，因此本表主要检验固定上限情景，而非主场强度的精确动态预测。排名前十及资格情景对身份变更敏感；这些表是有条件回放，不证明某种加成因果有效。复算：`python 项目工作区/scripts/task4_exante_replay.py`。\n'
(OUT/'赛前回放方法与结果.md').write_text(md,encoding='utf-8')
method=ROOT/'交付文件'/'任务四_开放创作'/'02_2028洛杉矶预测'/'预测方法与验证方案.md'
if method.exists():
    s=method.read_text(encoding='utf-8').split('\n\n### 赛前条件历史回放')[0]
    s+='\n\n### 赛前条件历史回放\n\n[查看目标届奖牌池未知时的历史回放](../05_满分升级/09_赛前条件回放/index.html)。2012、2016、2024均以此前奖牌池走势外推总量，主场率仅用此前案例，资格单列条件情景；2024估计池比最终池少63枚。新增运动排名信号仍缺可比历史快照，本表是可迁移核心的赛前条件检验，不是最终集成的完整端到端验证。\n'
    method.write_text(s,encoding='utf-8')
rows=''.join(f'<tr><td>{r.Year}</td><td>{r.情景.replace("_"," · ")}</td><td>{r.MAE_全体:.2f}</td><td>{r.MAE_实际至少5枚:.2f}</td><td>{r.前十重合}/10</td></tr>' for r in summary.itertuples())
html=f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>赛前条件历史回放｜百年圣火</title><style>body{{margin:0;background:#f2eee5;color:#173447;font-family:"Microsoft YaHei",sans-serif}}main{{max-width:1050px;margin:auto;padding:55px 24px 90px}}h1{{font-size:clamp(38px,6vw,70px)}}p{{line-height:1.85}}img{{width:100%;border-radius:20px}}.scroll{{overflow-x:auto}}table{{width:100%;border-collapse:collapse;background:#fffaf2}}th,td{{padding:10px;text-align:left;border-bottom:1px solid #ddd5c6}}.note{{padding:25px;border-radius:20px;background:#173e54;color:#fff;margin:25px 0}}a{{color:#267497}}@media(max-width:700px){{table{{font-size:12px}}}}</style></head><body><main><small>任务四 / 赛前条件</small><h1>如果当时还不知道<br>最终奖牌池？</h1><p>2012、2016、2024逐届回放：奖牌池由此前届次外推，主场身份已知但调整率只由此前案例估计；资格另作情景。</p><img src="赛前条件回放.png" alt="赛前条件下的逐届回测误差"><div class="scroll"><table><tr><th>届次</th><th>情景</th><th>全体MAE</th><th>≥5枚MAE</th><th>前十重合</th></tr>{rows}</table></div><div class="note">资格限制是假设，不是参赛决定。新增运动缺少当时的可比排名，分量退回基线；因此这仍是“可迁移核心”的条件回放，不能冒充完整2028最终模型的端到端验证。</div><p><a href="赛前回放方法与结果.md">方法与限制</a>　<a href="赛前条件与奖牌池.csv">赛前条件表</a>　<a href="赛前条件逐队回放.csv">逐队结果</a></p></main></body></html>'''
(OUT/'index.html').write_text(html,encoding='utf-8')
prior=OUT.parent/'滚动留出验证.html'
if prior.exists():
    s=prior.read_text(encoding='utf-8')
    if 'exante-replay-entry' not in s:
        s=s.replace('</body>','<!-- exante-replay-entry --><a href="09_赛前条件回放/index.html" style="display:block;max-width:980px;margin:30px auto;padding:24px;border-radius:20px;background:#173e54;color:white;text-decoration:none">继续阅读：只用赛前条件的历史回放 ↗</a></body>',1)
        prior.write_text(s,encoding='utf-8')
print(json.dumps({'pool':pool[['Year','赛前估计奖牌池','实际奖牌池_仅评分']].to_dict('records'),'scores':summary[['Year','情景','MAE_全体']].to_dict('records')},ensure_ascii=False,indent=2))
