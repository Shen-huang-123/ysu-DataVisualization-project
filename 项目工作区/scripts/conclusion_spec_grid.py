"""Predeclared specification grid for the most consequential cross-task claims."""
from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'交付文件'/'任务三_专题深挖'/'11_结论稳定性地图'/'02_量化口径实验'
OUT.mkdir(parents=True,exist_ok=True)
conc=pd.read_csv(ROOT/'交付文件'/'任务二_百年全景'/'07_结论压力测试'/'逐届集中度三口径.csv')
rank=pd.read_csv(ROOT/'交付文件'/'任务三_专题深挖'/'S2_口径的魔力'/'02_数据表'/'S2_2024三口径完整排名.csv').pivot(index='NOC',columns='lens',values='rank')
small=pd.read_csv(ROOT/'交付文件'/'任务三_专题深挖'/'S4_小代表团的大突破'/'02_客观样本'/'2000_2024全部候选及纳入判定.csv')
dyn=pd.read_csv(ROOT/'交付文件'/'任务三_专题深挖'/'S3_冠军的保质期'/'02_数据表'/'S3_逐小项冠军控制权转移.csv')
fixed=pd.read_csv(ROOT/'交付文件'/'任务三_专题深挖'/'S3_冠军的保质期'/'09_固定小项队列检验'/'固定小项逐届控制权转移.csv')
official=pd.read_csv(ROOT/'交付文件'/'任务一_数据体检'/'02_交付数据'/'2024官方329小项奖牌表.csv')
rows=[]
def add(claim,variant,metric,unit,rule,support,scope):
    rows.append({'结论':claim,'预设变体':variant,'检验值':float(metric),'单位':unit,'通过规则':rule,'方向仍成立':bool(support),'证据边界':scope})

# C1: direction of long-run deconcentration, windows and units fixed before evaluation.
for unit,early_end,modern_start,modern_end,label in [
    ('运动员获奖行',1936,1992,2016,'行口径，早期≤1936／现代1992—2016'),
    ('运动员获奖行',1936,1992,2024,'行口径，现代扩至2024'),
    ('运动员行·排除重复余量',1936,1992,2016,'排除重复余量'),
    ('同届项目奖牌组代理（≤2016）',1936,1992,2016,'历史奖牌组代理')]:
    z=conc[conc.unit.eq(unit)]
    early=z[z.Year.le(early_end)].top5_share.median()
    modern=z[z.Year.between(modern_start,modern_end)].top5_share.median()
    add('长期集中度下降',label,(modern-early)*100,'百分点','现代中位数−早期中位数 < 0',modern<early,'代理并非IOC官方小项；历史代表团不合并')

# C2: recent rebound; the mixed-unit variant is shown but not counted as comparable.
for unit,label in [('运动员获奖行','原始运动员行'),('运动员行·排除重复余量','删除重复余量')]:
    z=conc[conc.unit.eq(unit)].set_index('Year')
    diff=(z.loc[2024,'top5_share']-z.loc[2016,'top5_share'])*100
    add('2016—2024近期集中反弹',label,diff,'百分点','2024份额−2016份额 > 0',diff>0,'仅两届差值，不代表长期逆转')

# C3: medal-rank movement under alternative units and denominators.
for lens,label,subset in [('rows','运动员行／所有91队',rank),('rows','运动员行／官方前20',rank[rank.official.le(20)]),
                          ('fractional','团队内均分／所有91队',rank),('fractional','团队内均分／官方前20',rank[rank.official.le(20)])]:
    value=float((subset[lens]-subset.official).abs().mean())
    add('排名显著重排',label,value,'平均名次','平均绝对名次移动 ≥ 2',value>=2,'三种榜均按金银铜排序；衡量指标效应，不判定公平性')

# C4: small-delegation examples under fixed minimum edition count and quantile cutoffs.
old={'HKG','TPE','SGP','FIJ','BER','JOR','KOS'}
for q in [.25,.33,.50]:
    cutoff=float(small.median_participation_rows.quantile(q))
    cohort=small[small.median_participation_rows.le(cutoff)&small.medal_editions.ge(1)&~small.NOC.isin(['AIN','EOR','IOA'])]
    overlap=len(set(cohort.NOC)&old)
    add('原七例能代表最小代表团',f'参赛行中位数≤第{int(q*100)}百分位（{cutoff:g}行）',overlap,'七例中的入选数',
        '至少5／7案例符合统一门槛',overlap>=5,f'比较总体至少参加三届；此门槛筛出{len(cohort)}队')

# C5: dynasty trend under fixed/variable event sets and period choices.
for frame,label,first,last in [
    (fixed,'固定113小项，避开1980—1992', (1964,1976),(1996,2016)),
    (fixed,'固定113小项，保留转折期',(1964,1988),(1992,2016)),
    (fixed[fixed.Sport.ne('Athletics')],'固定小项，排除田径',(1964,1976),(1996,2016)),
    (dyn,'全部可比小项，项目组合变化',(1964,1976),(1996,2016))]:
    a=frame[frame.to_year.between(*first)].defended.mean();b=frame[frame.to_year.between(*last)].defended.mean()
    diff=(b-a)*100
    add('代表团小项卫冕率下降',label,diff,'百分点','后段卫冕率−前段卫冕率 < 0',diff<0,
        '不是个人冠军寿命；Event同名不保证规则完全不变')

tab=pd.DataFrame(rows)
tab.to_csv(OUT/'预设变体逐项结果.csv',index=False,encoding='utf-8-sig')
summary=tab.groupby('结论',sort=False).agg(变体数=('方向仍成立','size'),仍成立数=('方向仍成立','sum'),最小检验值=('检验值','min'),最大检验值=('检验值','max')).reset_index()
summary['仍成立比例']=summary.仍成立数/summary.变体数
summary.to_csv(OUT/'五个核心结论稳定性摘要.csv',index=False,encoding='utf-8-sig')
meta={'design':'五个跨任务核心结论，每个预设2—4个变体；不事后选择最有利口径',
      'interpretation':'变体高度相关，仍成立比例不是独立试验的概率或显著性检验',
      'historical_proxy':'2016及以前项目奖牌组不是IOC逐项官方表',
      'sample_selection':'固定小项队列只代表长期连续项目'}
(OUT/'方法边界.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8')

plt.rcParams['font.sans-serif']=['Microsoft YaHei','SimHei','DejaVu Sans'];plt.rcParams['axes.unicode_minus']=False
fig,ax=plt.subplots(figsize=(11.5,5.8),facecolor='#f2eee5');ax.set_facecolor('#f2eee5')
color=['#217485' if x==1 else '#bd6a4b' if x==0 else '#ae9052' for x in summary.仍成立比例]
bars=ax.barh(summary.结论,summary.仍成立比例*100,color=color,height=.57)
ax.invert_yaxis();ax.set_xlim(0,115);ax.set_xticks([0,25,50,75,100],labels=['0%','25%','50%','75%','100%']);ax.spines[['top','right','left','bottom']].set_visible(False);ax.grid(axis='x',color='#d7d6cb');ax.set_axisbelow(True);ax.tick_params(length=0)
for b,r in zip(bars,summary.itertuples()):ax.text(b.get_width()+2,b.get_y()+b.get_height()/2,f'{r.仍成立数}/{r.变体数}',va='center',color='#173447',fontweight='bold')
fig.text(.065,.94,'结论经得起多少种预设检验？',fontsize=22,fontweight='bold',color='#173447')
fig.text(.065,.88,'同一结论切换统计单位、观察窗口或样本门槛；比例为方向仍成立的变体数',fontsize=11,color='#5b7079')
fig.text(.065,.025,'变体相关且数量有限；比例不是“结论为真”的概率。逐项规则和结果见附表。',fontsize=9,color='#65777d')
fig.tight_layout(rect=[0,.06,1,.83]);fig.savefig(OUT/'核心结论量化稳定性.png',dpi=190,facecolor=fig.get_facecolor());plt.close(fig)

group_cards=''.join(f'''<details><summary><strong>{r.结论}</strong><span>{r.仍成立数}/{r.变体数} 个变体方向成立</span></summary><table><thead><tr><th>预设变体</th><th>检验值</th><th>规则</th><th>方向</th></tr></thead><tbody>{''.join(f'<tr><td>{x.预设变体}</td><td>{x.检验值:+.2f} {x.单位}</td><td>{x.通过规则}</td><td>{"成立" if x.方向仍成立 else "不成立"}</td></tr>' for x in tab[tab.结论.eq(r.结论)].itertuples())}</tbody></table></details>''' for r in summary.itertuples())
html=f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>核心结论量化稳定性</title><style>body{{margin:0;background:#f2eee5;color:#173447;font-family:"Microsoft YaHei",sans-serif}}main{{max-width:1050px;margin:auto;padding:62px 22px 90px}}h1{{font-size:clamp(40px,6vw,72px)}}p{{line-height:1.8}}img{{width:100%;border-radius:19px}}details{{border-bottom:1px solid #bfc6c0}}summary{{display:flex;justify-content:space-between;gap:15px;padding:23px 4px;cursor:pointer;font-size:20px}}summary span{{font-size:14px;color:#a65f43}}table{{width:100%;border-collapse:collapse;margin-bottom:20px;background:#fffaf2}}td,th{{padding:11px;text-align:left;border-bottom:1px solid #ded9cd}}.note{{background:#173d55;color:#fff;padding:25px;border-radius:20px;margin:28px 0}}a{{color:#247197}}@media(max-width:650px){{summary{{display:block}}summary span{{display:block;margin-top:7px}}table{{font-size:12px}}td,th{{padding:6px}}}}</style></head><body><main><small>百年圣火 / 结论压力测试</small><h1>把“稳健”变成<br>一道可复算的题。</h1><p>对五个最影响全篇叙事的结论，先定统计单位、时间窗、纳入门槛和通过规则，再观察方向是否改变。展开每条查看完整预设变体。</p><img src="核心结论量化稳定性.png" alt="五个核心结论的预设变体检验">{group_cards}<div class="note">变体不是独立重复试验；“4/4”并不等于结论有100%概率为真。排名大幅移动只发生在运动员行口径，团队内均分接近官方榜；原七个小队伍故事不满足最小四分位定义。所有历史小项代理和固定队列边界见逐项表。</div><p><a href="预设变体逐项结果.csv">下载逐项规则与结果</a>　<a href="../index.html">返回十专题证据入口</a></p></main></body></html>'''
(OUT/'index.html').write_text(html,encoding='utf-8')
print(summary.to_string(index=False))

# Keep the browser overview theme-native after rebuilding research outputs.
import runpy
runpy.run_path(str(Path(__file__).with_name('publish_spec_overview.py')))
