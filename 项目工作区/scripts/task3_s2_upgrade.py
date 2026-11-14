from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.stats import spearmanr,kendalltau
from task2_localization import NOC_ZH

ROOT=Path(__file__).resolve().parents[2]; TASK=ROOT/'交付文件'/'任务三_专题深挖'/'S2_口径的魔力'; TABLE=TASK/'02_数据表'; FIG=TASK/'04_核心图表'; DASH=TASK/'06_交互榜'; DASH.mkdir(exist_ok=True)
DATA=ROOT/'交付文件'/'任务一_数据体检'/'02_交付数据'/'归一数据_保留原始字段.csv.gz'; OFFICIAL=ROOT/'交付文件'/'任务一_数据体检'/'02_交付数据'/'2024官方329小项奖牌表.csv'
d=pd.read_csv(DATA); d=d[d.include_main.astype(bool)].copy(); o=pd.read_csv(OFFICIAL)
P={'paper':'#F7F3EB','ink':'#172A30','teal':'#247487','red':'#A64155','gold':'#C4903D','blue':'#65A9B4','grid':'#D9DEDC','grey':'#6C7A80'}
plt.rcParams.update({'font.family':'Microsoft YaHei','axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':P['paper'],'axes.facecolor':P['paper'],'savefig.facecolor':P['paper'],'savefig.dpi':220})
def split_codes(x): return [] if pd.isna(x) else [z.strip() for z in str(x).split('|') if z.strip()]
def rank_medals(frame,cols=('Gold','Silver','Bronze')):
    f=frame.copy(); keys=list(zip(*[-f[c] for c in cols])); ordered=sorted(keys); ranks={}
    for i,k in enumerate(ordered,1): ranks.setdefault(k,i)
    return pd.Series([ranks[k] for k in keys],index=f.index)
def pivot_counts(long,value='value'):
    x=long.pivot_table(index='NOC',columns='Medal',values=value,aggfunc='sum',fill_value=0).reindex(columns=['Gold','Silver','Bronze'],fill_value=0); return x
def save(fig,name,note): fig.text(.045,.012,note,fontsize=8.2,color=P['grey']); fig.savefig(FIG/name,bbox_inches='tight',dpi=220); plt.close(fig)

# Three 2024 lenses.
ol=[]
for medal,col in [('Gold','gold_country_code'),('Silver','silver_country_code'),('Bronze','bronze_country_code')]:
    for event_id,codes in zip(o.event_id,o[col]):
        for noc in split_codes(codes): ol.append({'NOC':noc,'Medal':medal,'value':1,'event_id':event_id})
official=pivot_counts(pd.DataFrame(ol)); official['rank']=rank_medals(official)
a=d[(d.Year.eq(2024))&d.is_medal.astype(bool)].copy(); a['group_n']=a.groupby(['NOC','Event','Medal']).source_row.transform('size'); a['fractional_weight']=1/a.group_n
fractional=pivot_counts(a[['NOC','Medal','fractional_weight']].rename(columns={'fractional_weight':'value'})); fractional['rank']=rank_medals(fractional)
rows=pivot_counts(a.assign(value=1)[['NOC','Medal','value']]); rows['rank']=rank_medals(rows)
three=[]
for lens,label,frame in [('official','官方小项',official),('fractional','组内均分',fractional),('rows','运动员行',rows)]:
    z=frame.reset_index(); z['lens']=lens; z['lens_label']=label; three.append(z)
three=pd.concat(three,ignore_index=True); three=three[~three.NOC.eq('AIN')]; three.to_csv(TABLE/'S2_2024三口径完整排名.csv',index=False,encoding='utf-8-sig')

# Cross-edition validation where Event is reliable.
hist=[]; detail=[]
for year in [2008,2012,2016]:
    x=d[(d.Year.eq(year))&d.is_medal.astype(bool)].copy(); x['group_n']=x.groupby(['NOC','Event','Medal']).source_row.transform('size')
    event=x.drop_duplicates(['NOC','Event','Medal']).assign(value=1); er=pivot_counts(event[['NOC','Medal','value']]); er['event_rank']=rank_medals(er)
    rr=pivot_counts(x.assign(value=1)[['NOC','Medal','value']]); rr['row_rank']=rank_medals(rr)
    z=er.join(rr,lsuffix='_event',rsuffix='_rows',how='outer').fillna(0); z=z[~z.index.isin(['AIN'])]
    common=z[(z.Gold_event.gt(0))&(z.Gold_rows.gt(0))].copy(); gold=x[x.Medal.eq('Gold')]; ggroups=gold.drop_duplicates(['NOC','Event','Medal']).groupby('NOC').size(); grows=gold.groupby('NOC').size(); gmulti=gold[gold.group_n.gt(1)].groupby('NOC').size(); mech=pd.DataFrame({'gold_groups':ggroups,'gold_rows':grows,'multi_rows':gmulti}).fillna(0); mech=mech[mech.gold_groups.gt(0)]; mech['factor']=mech.gold_rows/mech.gold_groups; mech['multi_share']=mech.multi_rows/mech.gold_rows
    rho,p=spearmanr(mech.factor,mech.multi_share); tau,tp=kendalltau(z.event_rank,z.row_rank); mad=float((z.event_rank-z.row_rank).abs().mean())
    hist.append({'Year':year,'eligible_nocs':len(mech),'mechanism_rho':rho,'mechanism_p':p,'rank_kendall_tau':tau,'rank_tau_p':tp,'mean_abs_rank_change':mad})
    z['Year']=year; z['rank_shift']=z.event_rank-z.row_rank; detail.append(z.reset_index())
hist=pd.DataFrame(hist); hist.to_csv(TABLE/'S2_跨届稳定性摘要.csv',index=False,encoding='utf-8-sig'); pd.concat(detail).to_csv(TABLE/'S2_跨届双口径排名.csv',index=False,encoding='utf-8-sig')

# Hero.
offrank=official.drop(index='AIN',errors='ignore'); rowrank=rows.drop(index='AIN',errors='ignore'); fracrank=fractional.drop(index='AIN',errors='ignore')
fig=plt.figure(figsize=(16,9)); ax=fig.add_axes([.05,.25,.58,.58]); top=offrank.sort_values('rank').head(12).sort_values('Gold')
y=np.arange(len(top)); ax.barh(y,top.Gold,color=P['gold'],label='官方金牌'); ax.barh(y,rowrank.reindex(top.index).Gold-top.Gold,left=top.Gold,color=P['red'],alpha=.82,label='额外运动员金牌记录'); ax.set_yticks(y,top.index); ax.grid(axis='x',color=P['grid']); ax.legend(frameon=False); ax.set_xlabel('金牌计数'); ax.set_title('同一届奥运，统计单位决定“谁被看见”',fontsize=22,fontweight='bold',loc='left')
cards=[('329','官方金牌单元','每个获胜小项计1'),('1.00','组内均分总权重','每组成员权重之和'),('2,281','运动员奖牌记录','每位获奖者计1'),('0.973','结构相关','多人组占比 vs 膨胀倍数')]
for i,(big,title,sub) in enumerate(cards):
    yy=.74-i*.145; fig.text(.68,yy,big,fontsize=28,fontweight='bold',color=[P['gold'],P['blue'],P['red'],P['teal']][i]); fig.text(.81,yy+.01,title,fontsize=12,fontweight='bold'); fig.text(.81,yy-.027,sub,fontsize=9.5,color=P['grey'])
fig.text(.05,.92,'S2 · 口径的魔力',fontsize=14,fontweight='bold',color=P['gold']); fig.text(.05,.12,'没有唯一“公平榜”：官方口径奖励小项胜利，行口径呈现获奖者覆盖，分数化口径连接两者。',fontsize=16,fontweight='bold',color=P['ink']); fig.text(.05,.075,'2024巴黎｜官方329小项｜三口径并列展示｜排除AIN排名',fontsize=9.5,color=P['grey'])
save(fig,'00_S2专题英雄图.png','金色为官方小项金牌；红色为运动员金牌记录相对官方金牌增加的部分。')

# Three-lens rank parallel plot.
focus=offrank.sort_values('rank').head(15).index.tolist(); pos={'official':0,'fractional':1,'rows':2}; fig,ax=plt.subplots(figsize=(12,8)); ax.set_xlim(-.2,2.2); maxrank=max(20,int(three[three.NOC.isin(focus)]['rank'].max())+1); ax.set_ylim(maxrank,.2); ax.axis('off')
colors={'official':P['gold'],'fractional':P['blue'],'rows':P['red']}; labels={'official':'官方小项','fractional':'组内均分','rows':'运动员行'}
for lens in pos: ax.text(pos[lens],0,labels[lens],ha='center',fontsize=15,fontweight='bold',color=colors[lens])
for noc in focus:
    vals=[]
    for lens in ['official','fractional','rows']:
        q=three[(three.NOC.eq(noc))&(three.lens.eq(lens))]; vals.append(float(q['rank'].iloc[0]) if len(q) else maxrank)
    ax.plot([0,1,2],vals,color=P['grey'],alpha=.65,lw=1.5); 
    for x,yv,lens in zip([0,1,2],vals,['official','fractional','rows']): ax.scatter(x,yv,s=42,color=colors[lens],zorder=3)
    name=NOC_ZH.get(noc,noc)
    ax.text(-.04,vals[0],f'{int(vals[0])} {name}',ha='right',va='center',fontsize=9); ax.text(2.04,vals[2],f'{name} {int(vals[2])}',ha='left',va='center',fontsize=9)
ax.set_title('同一排序规则，换一个统计单位就会改写名次',fontsize=19,fontweight='bold',loc='left',pad=22)
save(fig,'S2_三口径排名路径.png','官方口径来自329小项表；组内均分口径令每个NOC–Event–Medal组总权重为1；行口径每位获奖者计1。均按金银铜排序，排除AIN。')

# Historical validation.
fig,axes=plt.subplots(1,2,figsize=(13,5.8)); axes[0].bar(hist.Year.astype(str),hist.mechanism_rho,color=[P['teal'],P['blue'],P['red']]); axes[0].set_ylim(0,1.04); axes[0].set_ylabel('Spearman ρ'); axes[0].set_title('多人获奖结构与金牌行膨胀：跨届稳定',loc='left',fontweight='bold',pad=8); axes[0].grid(axis='y',color=P['grid'])
for i,r in hist.iterrows(): axes[0].text(i,r.mechanism_rho-.045,f'{r.mechanism_rho:.3f}',ha='center',fontweight='bold',color='white')
axes[1].plot(hist.Year,hist.rank_kendall_tau,marker='o',lw=2.7,color=P['gold'],label='两榜Kendall τ'); ax2=axes[1].twinx(); ax2.bar(hist.Year,hist.mean_abs_rank_change,width=2.1,color=P['red'],alpha=.22,label='平均绝对名次变化'); axes[1].set_ylim(0,1); axes[1].set_ylabel('排名一致性 τ'); ax2.set_ylabel('平均绝对名次变化'); axes[1].set_xticks(hist.Year); axes[1].grid(axis='y',color=P['grid']); axes[1].set_title('榜单总体相似，但局部重排持续存在',loc='left',fontweight='bold')
fig.suptitle('S2 历史验证：2008、2012、2016重复出现同一机制',fontsize=19,fontweight='bold',x=.04,y=.995,ha='left'); fig.subplots_adjust(top=.82,wspace=.25)
save(fig,'S2_跨届机制稳定性.png','历史小项代理口径：每个NOC–Event–Medal组合计1；Event字段在2008/2012/2016可用。相关为结构证据，不作因果解释。')

# Offline interactive ranking.
records=three[['NOC','Gold','Silver','Bronze','rank','lens','lens_label']].to_dict('records'); payload=json.dumps(records,ensure_ascii=False,separators=(',',':'))
html=r'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>S2 口径的魔力 · 交互榜</title><style>:root{--p:#f7f3eb;--i:#172a30;--t:#247487;--r:#a64155;--g:#c4903d;--b:#65a9b4;--l:#d9dedc}*{box-sizing:border-box}body{margin:0;background:var(--p);color:var(--i);font-family:"Microsoft YaHei",sans-serif}header{padding:32px 6vw 20px;border-bottom:1px solid var(--l)}h1{font-size:clamp(34px,5vw,66px);margin:0}.wrap{padding:24px 6vw}.controls{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:20px}select{padding:11px 16px;border:1px solid var(--l);border-radius:12px;background:white}.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.card{padding:18px;border:1px solid var(--l);border-radius:15px;background:#fff8}.big{font-size:30px;font-weight:800;color:var(--t)}table{width:100%;border-collapse:collapse;margin-top:20px;background:#fff8}th,td{padding:12px;border-bottom:1px solid var(--l);text-align:right}th:nth-child(2),td:nth-child(2){text-align:left}.bar{height:10px;background:var(--t);border-radius:9px;display:inline-block;margin-right:8px}@media(max-width:700px){.cards{grid-template-columns:1fr}}</style></head><body><header><div style="color:var(--g);font-weight:800">任务三 · S2</div><h1>口径的魔力</h1><p>切换统计单位，看同一届奥运如何生成不同奖牌榜。</p></header><main class="wrap"><div class="controls"><select id="lens"><option value="official">官方小项</option><option value="fractional">组内均分</option><option value="rows">运动员行</option></select><select id="sort"><option value="rank">按金银铜排名</option><option value="Gold">按金牌计数</option><option value="total">按奖牌总计</option></select><select id="limit"><option>10</option><option selected>20</option><option>50</option></select></div><section class="cards"><div class="card"><small>当前口径</small><div class="big" id="label"></div></div><div class="card"><small>榜首代表团</small><div class="big" id="leader"></div></div><div class="card"><small>榜首金牌计数</small><div class="big" id="gold"></div></div></section><table><thead><tr><th>名次</th><th>代表团</th><th>金</th><th>银</th><th>铜</th><th>总计</th></tr></thead><tbody id="body"></tbody></table></main><script>const data=__DATA__,q=id=>document.getElementById(id),lens=q('lens'),sort=q('sort'),limit=q('limit'),body=q('body');function render(){let a=data.filter(x=>x.lens===lens.value),key=sort.value;a.forEach(x=>x.total=x.Gold+x.Silver+x.Bronze);a.sort(key==='rank'?(x,y)=>x.rank-y.rank:(x,y)=>y[key]-x[key]||x.rank-y.rank);a=a.slice(0,+limit.value);q('label').textContent=a[0]?.lens_label||'—';q('leader').textContent=a[0]?.NOC||'—';q('gold').textContent=(a[0]?.Gold??0).toFixed(lens.value==='fractional'?1:0);let max=Math.max(...a.map(x=>x.Gold),1);body.innerHTML=a.map((x,i)=>`<tr><td>${key==='rank'?x.rank:i+1}</td><td><span class="bar" style="width:${x.Gold/max*110}px"></span>${x.NOC}</td><td>${x.Gold.toFixed(lens.value==='fractional'?1:0)}</td><td>${x.Silver.toFixed(lens.value==='fractional'?1:0)}</td><td>${x.Bronze.toFixed(lens.value==='fractional'?1:0)}</td><td>${x.total.toFixed(lens.value==='fractional'?1:0)}</td></tr>`).join('')}for(const e of [lens,sort,limit])e.onchange=render;render();</script></body></html>'''.replace('__DATA__',payload)
(DASH/'index.html').write_text(html,encoding='utf-8')
summary={'historical_validation':hist.to_dict('records'),'three_lens_rows':len(three),'dashboard':str(DASH/'index.html')}; (TABLE/'S2_升级关键指标.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8'); print(json.dumps(summary,ensure_ascii=False,indent=2))
