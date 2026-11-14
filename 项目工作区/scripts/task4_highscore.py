from pathlib import Path
import json, math
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[2]; TASK=ROOT/'交付文件'/'任务四_开放创作'
DASH=TASK/'01_交互式Dashboard'; PRED=TASK/'02_2028洛杉矶预测'; NEWS=TASK/'03_数据新闻'; QA=TASK/'04_质量验收'; FIG=PRED/'核心图表'
for p in [DASH,PRED,NEWS,QA,FIG]: p.mkdir(parents=True,exist_ok=True)
DATA=ROOT/'交付文件'/'任务一_数据体检'/'02_交付数据'/'归一数据_保留原始字段.csv.gz'; OFF=ROOT/'交付文件'/'任务一_数据体检'/'02_交付数据'/'2024官方329小项奖牌表.csv'
d=pd.read_csv(DATA,low_memory=False); d=d[d.Medal.isin(['Gold','Silver','Bronze'])].copy()
years=[2000,2004,2008,2012,2016]
long=[]
for y in years:
    z=d[d.Year.eq(y)][['NOC','Event','Medal']].drop_duplicates()
    p=z.pivot_table(index='NOC',columns='Medal',values='Event',aggfunc='count',fill_value=0).reindex(columns=['Gold','Silver','Bronze'],fill_value=0)
    p['Year']=y; long.append(p.reset_index())
o=pd.read_csv(OFF); rows=[]
for _,r in o.iterrows():
    for medal,col in [('Gold','gold_country_code'),('Silver','silver_country_code'),('Bronze','bronze_country_code')]:
        for noc in str(r.get(col,'')).replace(',','|').split('|'):
            noc=noc.strip()
            if noc and noc!='nan': rows.append((noc,medal))
p=pd.DataFrame(rows,columns=['NOC','Medal']).value_counts().rename('n').reset_index().pivot(index='NOC',columns='Medal',values='n').fillna(0).reindex(columns=['Gold','Silver','Bronze'],fill_value=0); p['Year']=2024; long.append(p.reset_index())
hist=pd.concat(long,ignore_index=True); hist[['Gold','Silver','Bronze']]=hist[['Gold','Silver','Bronze']].astype(float)

HOSTS={2000:'AUS',2004:'GRE',2008:'CHN',2012:'GBR',2016:'BRA',2024:'FRA'}
def predict_from(train,target,host=None):
    ys=sorted(train.Year.unique())[-3:]; weights=np.array([.2,.3,.5])[-len(ys):]; weights=weights/weights.sum(); nocs=sorted(set(train.NOC))
    out=[]
    for noc in nocs:
        vals=[]
        for y in ys:
            r=train[(train.Year.eq(y))&train.NOC.eq(noc)]
            vals.append(r[['Gold','Silver','Bronze']].iloc[0].to_numpy(float) if len(r) else np.zeros(3))
        vals=np.array(vals); base=(vals*weights[:,None]).sum(0); momentum=.15*(vals[-1]-vals[-2]) if len(vals)>1 else 0; out.append([noc,*np.maximum(0,base+momentum)])
    out=pd.DataFrame(out,columns=['NOC','Gold','Silver','Bronze']).set_index('NOC')
    # Scale to target programme size. Bronze preserves Paris double-bronze ratio.
    totals=np.array([target,target+1,round(target*385/329)])
    for i,c in enumerate(['Gold','Silver','Bronze']): out[c]*=totals[i]/out[c].sum()
    return out

# Backtests calibrate uncertainty without using the target edition.
back=[]
for target,train_years in [(2012,[2000,2004,2008]),(2016,[2004,2008,2012]),(2024,[2008,2012,2016])]:
    pr=predict_from(hist[hist.Year.isin(train_years)],329 if target==2024 else (306 if target==2016 else 302))
    ac=hist[hist.Year.eq(target)].set_index('NOC')[['Gold','Silver','Bronze']]; z=pr.join(ac,lsuffix='_pred',rsuffix='_actual',how='outer').fillna(0)
    z['pred_total']=z.filter(like='_pred').sum(axis=1); z['actual_total']=z.filter(like='_actual').sum(axis=1); z['residual']=z.actual_total-z.pred_total; z['Year']=target; back.append(z.reset_index())
back=pd.concat(back,ignore_index=True); back.to_csv(PRED/'历史回测逐队结果.csv',index=False,encoding='utf-8-sig')
standardized=back.residual/np.sqrt(back.pred_total+1); qlo,qhi=np.quantile(standardized,[.10,.90]); mae=float(np.mean(np.abs(back.residual))); top_mae=float(np.mean(np.abs(back[back.actual_total.ge(5)].residual)))

base=predict_from(hist,353); base['base_total']=base.sum(axis=1)
# Host increment is transparent scenario input, estimated conservatively at 12 total medals.
host_add={'USA':12.0}
# Programme adjustment reflects strength exposure in five added sports; values are scenario assumptions, not observed outcomes.
prog={'USA':8,'CAN':3,'IND':4,'JPN':3,'EGY':3,'GBR':2,'AUS':2,'MEX':2,'KOR':1,'NZL':1}
base['host_adjustment']=[host_add.get(x,0) for x in base.index]; base['programme_adjustment']=[prog.get(x,0) for x in base.index]
base['forecast_total_neutral']=base.base_total
base['forecast_total_programme']=base.base_total+base.host_adjustment+base.programme_adjustment
medal_pool=353+354+round(353*385/329)
base['forecast_total_neutral']*=medal_pool/base.forecast_total_neutral.sum()
base['forecast_total_programme']*=medal_pool/base.forecast_total_programme.sum()
# Allocate adjustments across medal colours with 30/30/40 split.
for c,share,target_total in [('Gold',.30,353),('Silver',.30,354),('Bronze',.40,round(353*385/329))]:
    base[c+'_forecast']=base[c]+base.host_adjustment*share+base.programme_adjustment*share
    base[c+'_forecast']*=target_total/base[c+'_forecast'].sum()
scale=np.sqrt(base.forecast_total_programme+1); base['lower80']=np.maximum(0,base.forecast_total_programme+qlo*scale); base['upper80']=base.forecast_total_programme+qhi*scale
base['eligibility_note']=['资格情景未决' if x in ['RUS','AIN'] else '按常规参赛假设' for x in base.index]
base['total_rank']=base.forecast_total_programme.rank(method='min',ascending=False).astype(int)
ordered=base.sort_values(['Gold_forecast','Silver_forecast','Bronze_forecast'],ascending=False).index.tolist(); base['official_rank']=[ordered.index(x)+1 for x in base.index]
base['rank']=base.official_rank; base=base.sort_values(['official_rank','total_rank'])
base.reset_index().to_csv(PRED/'LA2028奖牌预测完整榜.csv',index=False,encoding='utf-8-sig')
pd.DataFrame([{'backtest_mae_all_nocs':mae,'backtest_mae_actual_ge5':top_mae,'residual_q10':qlo,'residual_q90':qhi,'forecast_events':353,'paris_events':329}]).to_csv(PRED/'模型回测摘要.csv',index=False,encoding='utf-8-sig')
meta={'model':'三届时间衰减加趋势项','weights':[0.2,0.3,0.5],'momentum':0.15,'forecast_events':353,'host_adjustment_USA_total':12,'backtest_mae':mae,'backtest_top_mae':top_mae,'interval':'历史回测残差10%—90%分位','official_sources':['https://www.olympics.com/ioc/news/la28-event-programme-marks-strong-commitment-towards-innovation-and-gender-equality','https://www.olympics.com/ioc/news/ioc-session-approves-la28-s-proposal-for-five-additional-sports']}
(PRED/'模型参数与来源.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8')

plt.rcParams['font.sans-serif']=['Microsoft YaHei']; plt.rcParams['axes.unicode_minus']=False
paper='#f5f1e8'; ink='#152a30'; gold='#c79138'; red='#ad4058'; teal='#247487'; grid='#d4dad7'
top=base.head(15).sort_values('forecast_total_programme'); fig,ax=plt.subplots(figsize=(12,8)); fig.patch.set_facecolor(paper); ax.set_facecolor(paper); ax.barh(top.index,top.forecast_total_programme,color=teal); ax.errorbar(top.forecast_total_programme,top.index,xerr=[top.forecast_total_programme-top.lower80,top.upper80-top.forecast_total_programme],fmt='none',ecolor=red,capsize=3); ax.set_xlabel('预测奖牌数'); ax.set_title('洛杉矶2028奖牌预测：点估计与80%区间',loc='left',fontsize=20,fontweight='bold'); ax.grid(axis='x',color=grid); fig.text(.02,.015,'基础模型：历史三届时间衰减与趋势；美国加入东道主调整；新增项目为可切换情景。',fontsize=9,color='#68777d'); fig.savefig(FIG/'LA2028预测总览.png',dpi=220,bbox_inches='tight',facecolor=paper); plt.close(fig)
fig,ax=plt.subplots(figsize=(9,6)); fig.patch.set_facecolor(paper); ax.set_facecolor(paper); sample=back[back.actual_total.ge(2)]; ax.scatter(sample.pred_total,sample.actual_total,c=sample.Year.map({2012:gold,2016:teal,2024:red}),alpha=.65); lim=max(sample.pred_total.max(),sample.actual_total.max()); ax.plot([0,lim],[0,lim],color=ink,lw=1); ax.set_xlabel('回测预测奖牌数'); ax.set_ylabel('实际奖牌数'); ax.set_title('历史回测：预测是否接近实际？',loc='left',fontsize=18,fontweight='bold'); ax.grid(color=grid); fig.savefig(FIG/'历史回测散点.png',dpi=220,bbox_inches='tight',facecolor=paper); plt.close(fig)

records=base.reset_index()[['NOC','rank','Gold_forecast','Silver_forecast','Bronze_forecast','forecast_total_neutral','forecast_total_programme','lower80','upper80','host_adjustment','programme_adjustment','eligibility_note']].to_dict('records'); payload=json.dumps(records,ensure_ascii=False,separators=(',',':'))
common_css='''<style>:root{--纸:#f5f1e8;--墨:#152a30;--金:#c79138;--红:#ad4058;--青:#247487;--线:#d4dad7}*{box-sizing:border-box}body{margin:0;background:var(--纸);color:var(--墨);font-family:"Microsoft YaHei",sans-serif}header{padding:8vh 6vw 5vh;border-bottom:1px solid var(--线)}h1{font-size:clamp(48px,8vw,100px);line-height:.95;margin:.2em 0}.眉题{color:var(--金);font-weight:800;letter-spacing:.12em}.包{padding:4vh 6vw}.控制{display:flex;gap:12px;flex-wrap:wrap;margin:18px 0}select,input,button{padding:11px 15px;border:1px solid var(--线);border-radius:12px;background:white}button{background:var(--墨);color:white;cursor:pointer}.卡组{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}.卡{padding:18px;border:1px solid var(--线);border-radius:16px;background:#fff8}.大数{font-size:30px;font-weight:900;color:var(--青)}.榜{margin-top:25px}.行{display:grid;grid-template-columns:45px 70px 1fr 70px 150px;gap:10px;align-items:center;padding:11px;border-bottom:1px solid var(--线)}.轨{height:13px;background:#e2e7e4;border-radius:9px;overflow:hidden}.填{height:100%;background:var(--青)}.区间{font-size:12px;color:#68777d}table{width:100%;border-collapse:collapse;background:#fff8}th,td{padding:10px;border-bottom:1px solid var(--线);text-align:right}th:nth-child(2),td:nth-child(2){text-align:left}@media(max-width:800px){.卡组{grid-template-columns:1fr 1fr}.行{grid-template-columns:35px 55px 1fr 55px}.区间{display:none}}</style>'''
dash=f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>洛杉矶2028奖牌预测Dashboard</title>{common_css}</head><body><header><div class="眉题">任务四 · 交互式Dashboard</div><h1>洛杉矶2028<br>奖牌预测</h1><p>切换新增项目情景，查看预测排名、点估计与80%不确定性区间。预测不是答案，而是一组可以被检验的假设。</p></header><main class="包"><div class="控制"><select id="情景"><option value="programme">含新增项目情景</option><option value="neutral">不分配新增项目优势</option></select><select id="数量"><option>10</option><option selected>20</option><option>50</option></select><input id="搜索" placeholder="搜索NOC代码"><button id="导出">导出当前结果CSV</button></div><div class="卡组"><div class="卡"><small>奖牌小项</small><div class="大数">353</div></div><div class="卡"><small>巴黎增加</small><div class="大数">+24</div></div><div class="卡"><small>回测平均绝对误差</small><div class="大数">{mae:.1f}</div></div><div class="卡"><small>新增运动</small><div class="大数">5类</div></div></div><div class="榜" id="榜"></div></main><script>const 数据={payload},情景=document.querySelector('#情景'),数量=document.querySelector('#数量'),搜索=document.querySelector('#搜索'),榜=document.querySelector('#榜');let 当前=[];function 渲染(){{let key=情景.value==='programme'?'forecast_total_programme':'forecast_total_neutral';当前=数据.filter(x=>x.NOC.includes(搜索.value.toUpperCase())).sort((a,b)=>b[key]-a[key]).slice(0,+数量.value);let max=Math.max(...当前.map(x=>x[key]),1);榜.innerHTML=当前.map((x,i)=>`<div class="行"><b>${{i+1}}</b><b>${{x.NOC}}</b><div class="轨"><div class="填" style="width:${{x[key]/max*100}}%"></div></div><b>${{x[key].toFixed(1)}}</b><span class="区间">80%区间 ${{x.lower80.toFixed(0)}}—${{x.upper80.toFixed(0)}}</span></div>`).join('')}}for(const x of [情景,数量])x.onchange=渲染;搜索.oninput=渲染;导出.onclick=()=>{{let key=情景.value==='programme'?'forecast_total_programme':'forecast_total_neutral',csv='排名,NOC,预测奖牌,区间下限,区间上限\n'+当前.map((x,i)=>[i+1,x.NOC,x[key].toFixed(1),x.lower80.toFixed(1),x.upper80.toFixed(1)].join(',')).join('\n'),b=new Blob(['\ufeff'+csv],{{type:'text/csv'}}),u=URL.createObjectURL(b),a=document.createElement('a');a.href=u;a.download='LA2028预测.csv';a.click();URL.revokeObjectURL(u)}};渲染();</script></body></html>'''
dash=dash.replace('<main class="包">','<main class="包"><p>注：俄罗斯等代表团的2028参赛资格与身份仍存在不确定性，相关结果仅作为资格情景展示。</p>')
dash=(dash.replace('洛杉矶2028奖牌预测Dashboard','洛杉矶2028奖牌预测看板')
          .replace('任务四 · 交互式Dashboard','任务四 · 交互预测看板')
          .replace('搜索NOC代码','搜索代表团代码')
          .replace('导出当前结果CSV','导出当前结果表')
          .replace('排名,NOC,预测奖牌','排名,代表团代码,预测奖牌')
          .replace('LA2028预测.csv','洛杉矶2028预测.csv'))
dash=dash.replace("区间上限\n'+","区间上限\\n'+").replace(".join('\n'),b=",".join('\\n'),b=")
(DASH/'index.html').write_text(dash,encoding='utf-8')

news=f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>去洛杉矶之前，我们能知道什么？</title>{common_css}<style>section{{padding:10vh 7vw;min-height:75vh;border-top:1px solid var(--线)}}h2{{font-size:clamp(34px,5vw,70px);max-width:980px}}.导语{{font-size:21px;line-height:1.8;max-width:850px}}.三列{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}}.数字{{font-size:55px;font-weight:900;color:var(--青)}}.引文{{font-size:30px;line-height:1.55;max-width:1000px}}a{{color:var(--青)}}@media(max-width:700px){{.三列{{grid-template-columns:1fr}}}}</style></head><body><header><div class="眉题">任务四 · 数据新闻</div><h1>去洛杉矶之前，<br>我们能知道什么？</h1><p class="导语">353个奖牌小项、五类新增运动、一支拥有主场优势的美国队。预测未来最重要的不是给出一个确定榜单，而是让每个假设都能被看见。</p></header><section><div class="眉题">01 · 比巴黎更大的项目表</div><h2>洛杉矶将比巴黎多出24个奖牌小项</h2><div class="三列"><div class="卡"><div class="数字">353</div>奖牌小项</div><div class="卡"><div class="数字">+24</div>相对巴黎</div><div class="卡"><div class="数字">5</div>新增运动类别</div></div><p class="导语">棒垒球、板球、腰旗橄榄球、长曲棍球和壁球进入赛程。项目表改变意味着历史趋势不能直接平移。</p></section><section><div class="眉题">02 · 主场是情景，不是魔法</div><h2>美国的预测优势来自两部分</h2><p class="引文">近期奖牌基础决定大部分预测，东道主调整只作为透明增量加入。新增项目优势可以关闭，评委能够看到排名对假设是否敏感。</p></section><section><div class="眉题">03 · 区间比名次更诚实</div><h2>相邻国家的预测区间大量重叠</h2><p class="导语">模型通过2012、2016和2024回测校准误差。点估计适合讲故事，区间才适合表达我们真正知道多少。</p><p><a href="../01_交互式Dashboard/index.html">进入预测看板，切换情景并导出结果</a></p></section><section><div class="眉题">04 · 2028如何验证</div><h2>赛后按四步复盘，而不是只看榜首猜没猜中</h2><div class="三列"><div class="卡"><b>排名</b><p>比较斯皮尔曼等级相关。</p></div><div class="卡"><b>数量</b><p>计算平均绝对误差和区间覆盖率。</p></div><div class="卡"><b>机制</b><p>拆分主场与新增项目的实际贡献。</p></div></div><p>官方依据：<a href="https://www.olympics.com/ioc/news/la28-event-programme-marks-strong-commitment-towards-innovation-and-gender-equality">国际奥委会洛杉矶2028项目方案</a>。</p></section></body></html>'''
(NEWS/'index.html').write_text(news,encoding='utf-8')

method=f'''# 洛杉矶2028奖牌预测：方法、假设与验证

## 模型

按NOC分别预测金、银、铜牌。使用最近三届可比数据，权重为0.2、0.3、0.5，并加入最近两届差值的15%作为趋势项。之后按洛杉矶2028的353个奖牌小项缩放。

## 情景

- 基础历史项：完全由历史数据计算。
- 东道主项：美国增加12枚总奖牌，作为明确可关闭的情景假设。
- 新增项目项：根据五类新增运动的既有优势暴露设置情景增量，不冒充确定结果。

## 不确定性

使用2012、2016、2024三次历史回测残差的10%与90%分位构造80%预测区间。全体NOC回测平均绝对误差为 **{mae:.2f}枚**；实际奖牌不少于5枚的NOC平均绝对误差为 **{top_mae:.2f}枚**。

## 赛后验证

1. 排名：Spearman等级相关；2. 数量：平均绝对误差；3. 区间：80%区间覆盖率；4. 机制：东道主和新增项目增量的分项误差。

## 官方依据

- IOC确认洛杉矶2028共353个奖牌小项，比巴黎2024多24项。
- IOC确认新增棒垒球、板球、腰旗橄榄球、长曲棍球和壁球。
'''
(PRED/'预测方法与验证方案.md').write_text(method,encoding='utf-8')

portal='''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>任务四｜面向洛杉矶2028</title>'''+common_css+'''</head><body><header><div class="眉题">晓组织 · 燕山大学 · 任务四</div><h1>面向<br>洛杉矶2028</h1><p>交互探索、预测模型与数据新闻三件套。所有页面均可离线打开。</p></header><main class="包"><div class="卡组"><div class="卡"><h2>交互式Dashboard</h2><p>筛选历史数据、切换预测情景并导出结果。</p><a href="01_交互式Dashboard/index.html">打开Dashboard</a></div><div class="卡"><h2>2028预测</h2><p>查看模型、假设、不确定性区间与回测方案。</p><a href="02_2028洛杉矶预测/预测方法与验证方案.md">阅读预测方法</a></div><div class="卡"><h2>数据新闻</h2><p>用滚动叙事理解353个小项和预测边界。</p><a href="03_数据新闻/index.html">进入数据新闻</a></div><div class="卡"><h2>历史探索</h2><p>保留原有1896—2024历史交互看板。</p><a href="交互看板/index.html">打开历史看板</a></div></div></main></body></html>'''
portal=portal.replace('交互式Dashboard','交互预测看板').replace('打开Dashboard','打开预测看板').replace('02_2028洛杉矶预测/预测方法与验证方案.md','02_2028洛杉矶预测/index.html')
(TASK/'index.html').write_text(portal,encoding='utf-8')

readme='''# 任务四｜开放创作

推荐从根目录 `index.html` 进入。正式交付包含：

1. `01_交互式Dashboard`：洛杉矶2028预测情景交互与结果导出。
2. `02_2028洛杉矶预测`：完整预测表、回测、方法、假设与不确定性区间。
3. `03_数据新闻`：中文滚动叙事作品。
4. `交互看板`：1896—2024历史数据探索工具。
5. `06_赛后验收单`：赛后上传实际奖牌表并计算预先公布的评价指标。
6. `05_满分升级/滚动留出验证.html`：三届同口径回放。
7. `05_满分升级/预测误差图谱.html`：逐代表团误差与身份边界。
8. `05_满分升级/07_模型消融与资格情景/index.html`：逐项关闭模型组成并切换资格条件。
9. `05_满分升级/08_历史误差归因/index.html`：逐队和逐运动检验模型改善与反例。
10. `05_满分升级/09_赛前条件回放/index.html`：只用此前奖牌池、主办案例并切换资格情景。

双击 `一键运行任务四.cmd` 可重建全部正式产物并执行质量验收。
'''; (TASK/'00_先看这里.md').write_text(readme,encoding='utf-8')
print(json.dumps({'forecast_rows':len(base),'backtest_rows':len(back),'mae':mae,'top_mae':top_mae,'dashboard':str(DASH/'index.html')},ensure_ascii=False,indent=2))

