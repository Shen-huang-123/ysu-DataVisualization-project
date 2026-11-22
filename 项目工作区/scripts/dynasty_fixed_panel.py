"""Test dynasty decline among identically named events held in every 1960–2016 edition."""
from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'交付文件'/'任务三_专题深挖'/'S3_冠军的保质期'
OUT=BASE/'09_固定小项队列检验';OUT.mkdir(parents=True,exist_ok=True)
src=BASE/'02_数据表'/'S3_逐小项冠军控制权转移.csv'
d=pd.read_csv(src)
years=list(range(1960,2017,4)); pairs=set(zip(years[:-1],years[1:]))
z=d[[ (a,b) in pairs for a,b in zip(d.from_year,d.to_year) ]].copy()
counts=z.groupby('event_key').apply(lambda x:len(set(zip(x.from_year,x.to_year))),include_groups=False)
keys=counts[counts.eq(len(pairs))].index
fixed=z[z.event_key.isin(keys)].copy()
assert len(fixed)==len(keys)*len(pairs) and not fixed.duplicated(['event_key','from_year','to_year']).any()
fixed.to_csv(OUT/'固定小项逐届控制权转移.csv',index=False,encoding='utf-8-sig')
early=fixed[fixed.to_year.between(1964,1976)].groupby('event_key').defended.mean()
late=fixed[fixed.to_year.between(1996,2016)].groupby('event_key').defended.mean()
event=fixed[['event_key','Sport','Event']].drop_duplicates().set_index('event_key')
event['early_rate']=early;event['late_rate']=late;event['late_minus_early']=late-early
event.reset_index().to_csv(OUT/'固定小项前后段卫冕率.csv',index=False,encoding='utf-8-sig')
rng=np.random.default_rng(42);delta=event.late_minus_early.to_numpy()
boot=rng.choice(delta,size=(10000,len(delta)),replace=True).mean(axis=1)
ci=np.quantile(boot,[.025,.975])
early_rate=float(early.mean());late_rate=float(late.mean());difference=late_rate-early_rate
all_early=float(fixed[fixed.to_year.between(1964,1988)].defended.mean())
all_late=float(fixed[fixed.to_year.between(1992,2016)].defended.mean())
sport_sensitivity=[]
for sport in sorted(event.Sport.unique()):
    other=event[event.Sport.ne(sport)]
    if len(other)<20:continue
    sport_sensitivity.append({'excluded_sport':sport,'remaining_events':len(other),
                              'late_minus_early_pp':100*other.late_minus_early.mean()})
sens=pd.DataFrame(sport_sensitivity).sort_values('late_minus_early_pp')
sens.to_csv(OUT/'逐运动排除敏感度.csv',index=False,encoding='utf-8-sig')
timeline=fixed.groupby('to_year').defended.agg(['size','mean']).reset_index()
timeline.to_csv(OUT/'固定队列逐届卫冕率.csv',index=False,encoding='utf-8-sig')
summary={'fixed_events':len(keys),'transitions':len(fixed),'early_editions':'1964–1976','late_editions':'1996–2016',
         'early_rate':early_rate,'late_rate':late_rate,'late_minus_early_pp':difference*100,
         'event_cluster_bootstrap_ci95_pp':[float(x*100) for x in ci],
         'broad_1964_1988_rate':all_early,'broad_1992_2016_rate':all_late,
         'leave_one_sport_out_pp_range':[float(sens.late_minus_early_pp.min()),float(sens.late_minus_early_pp.max())]}
(OUT/'固定小项检验摘要.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
plt.rcParams['font.sans-serif']=['Microsoft YaHei','SimHei','DejaVu Sans'];plt.rcParams['axes.unicode_minus']=False
fig,ax=plt.subplots(figsize=(11.8,4.6))
fig.patch.set_alpha(0)
ax.patch.set_alpha(0)
ax.spines[:].set_visible(False)
ax.set_axisbelow(True)
ax.grid(axis='y',color='#9baeb4',alpha=.45,linewidth=.7)
ax.axvspan(1978,1994,color='#a96b31',alpha=.11,linewidth=0)
ax.plot(timeline.to_year,timeline['mean']*100,color='#17627a',marker='o',markersize=4.5,linewidth=2.1,zorder=3)
ax.hlines([early_rate*100,late_rate*100],[1964,1996],[1976,2016],colors='#9c5024',linestyles='dashed',linewidth=1.4,zorder=2)
ax.text(1986,47,'1980—1992 · 不纳入主比较',ha='center',va='center',fontsize=10,color='#874727')
ax.set_ylim(0,50)
ax.set_xlim(1962,2018)
ax.set_yticks(range(0,51,10),[f'{value}%' for value in range(0,51,10)])
ax.set_xticks([1964,1972,1980,1988,1996,2004,2012,2016])
ax.tick_params(length=0,pad=7,labelsize=10,colors='#344e58')
ax.set_xlabel('卫冕目标届次',fontsize=10,color='#344e58',labelpad=12)
ax.set_title(f'固定 {len(keys)} 项的逐届卫冕率',loc='left',fontsize=18,fontweight='bold',color='#1b3947',pad=18)
fig.text(.058,.025,'虚线为各比较时段均值。小项身份采用历史 Event 代理。',fontsize=10,color='#344e58')
fig.tight_layout(rect=[0,.08,1,1])
fig.savefig(OUT/'固定小项王朝压力测试.png',dpi=190,transparent=True)
plt.close(fig)
md=f'''# 固定小项队列：王朝变短是否只是项目表更替？

从 S7 原有 4,511 次控制权转移出发，预先规定一个严格队列：同名 Event 在 **1960—2016 每届**均出现，且每两个相邻实际举办届次都有金牌代表团可比。得到 **{len(keys)} 个小项、{len(fixed)} 次转移**。这排除了项目新设、退出和名称显著变化所形成的机械组成效应，但保留稳定举办的小项存在选择偏差。

主比较避开 1980—1992 的抵制与政体转折，把 1964—1976 的 4 个目标届次与 1996—2016 的 6 个目标届次比较。固定小项卫冕率从 **{early_rate:.1%}** 降为 **{late_rate:.1%}**，差 **{difference*100:.2f} 个百分点**。按小项成组重抽样 10,000 次的差值 95% 区间为 **[{ci[0]*100:.2f}, {ci[1]*100:.2f}] 个百分点**。

保留中间转折期、改用 1964—1988 对 1992—2016 后，卫冕率为 {all_early:.1%} 对 {all_late:.1%}，差值减小。逐一排除一种运动后，主比较差值落在 **{sens.late_minus_early_pp.min():.2f} 至 {sens.late_minus_early_pp.max():.2f} 个百分点**。因此“固定项目后下降仍存在”有数据支持，但下降幅度依赖时间窗。

本结论描述的是**代表团对小项金牌的连续控制**，不是个人冠军寿命，也不能归因于运动员变弱。Event 名称相同不能保证项目规则完全不变；样本仅为长期存续小项，历史小项为主数据代理而非逐项 IOC 官方表。图、逐届转移、纳入队列与运动排除表可在本文件夹复核。运行 `python 项目工作区/scripts/dynasty_fixed_panel.py` 重建。
'''
(OUT/'固定小项队列研究.md').write_text(md,encoding='utf-8')
html=f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>王朝固定小项检验</title><style>body{{margin:0;background:#f2eee5;color:#173447;font-family:"Microsoft YaHei",sans-serif}}main{{max-width:1050px;margin:auto;padding:64px 24px 90px}}h1{{font-size:clamp(40px,6vw,72px);line-height:1.15}}p{{line-height:1.8}}img{{width:100%;border-radius:18px}}.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:15px;margin:28px 0}}.card{{padding:22px;border-radius:19px;background:#fffaf2}}.card b{{display:block;font:700 36px Georgia;color:#235e79}}.note{{background:#173e54;color:#fff;padding:25px;border-radius:20px}}a{{color:#23719b}}@media(max-width:700px){{.grid{{grid-template-columns:1fr}}}}</style><link rel="stylesheet" href="../../../共享组件/dynasty-fixed-reading.css?v=reading-background"></head><body><main class="dynasty-fixed-reading"><small>任务三 / S7 王朝寿命</small><h1>固定比赛项目后，<br>王朝仍在变短吗？</h1><p>保留 1960—2016 每届连续存在且名称稳定的 {len(keys)} 个小项，再比较同一代表团连续卫冕的比例。</p><div class="grid"><div class="card">早段 1964—1976<b>{early_rate:.1%}</b></div><div class="card">后段 1996—2016<b>{late_rate:.1%}</b></div><div class="card">差值 95% 区间<b>{ci[0]*100:.1f} 至 {ci[1]*100:.1f} pp</b></div></div><img class="chart-surface dynasty-fixed-trend" src="固定小项王朝压力测试.png" alt="固定小项逐届卫冕率"><div class="note"><h2>结论与边界</h2><p>项目新增和退出不能完全解释这一固定队列中的下降；改动观察窗口会改变幅度。结果仍不是个人冠军寿命，也不能证明竞技竞争加剧是唯一原因。历史 Event 为代理，且只选择长期存续项目。</p></div><p><a href="固定小项队列研究.md">完整方法与敏感度</a>　<a href="固定小项逐届控制权转移.csv">逐届原表</a>　<a href="逐运动排除敏感度.csv">运动排除表</a></p></main></body></html>'''
(OUT/'index.html').write_text(html,encoding='utf-8')
from publish_dynasty_fixed_table import publish_edition_table
publish_edition_table(OUT)
timeline_page=BASE/'06_冠军王朝时间轴'/'index.html'
if timeline_page.exists():
    text=timeline_page.read_text(encoding='utf-8')
    marker='<!-- fixed-dynasty-entry -->'
    if marker not in text:
        block=f'''{marker}<a href="../09_固定小项队列检验/index.html" style="display:block;max-width:1050px;margin:30px auto;padding:25px 28px;border-radius:20px;background:#173e54;color:#fff;text-decoration:none;font-family:'Microsoft YaHei',sans-serif"><small style="color:#b3d4df">S7 稳健性检验 / {len(keys)}个固定小项</small><strong style="display:block;font-size:25px;margin:8px 0">项目表不变，王朝仍会缩短吗？ ↗</strong><span style="color:#e0edf0">早段 {early_rate:.1%}，后段 {late_rate:.1%}；查看时间窗、运动排除与成组区间。</span></a>'''
        timeline_page.write_text(text.replace('</body>',block+'</body>',1),encoding='utf-8')
report=BASE/'01_报告与说明'/'S3_冠军的保质期_分析报告.md'
if report.exists():
    text=report.read_text(encoding='utf-8').split('\n\n## 固定小项队列检验')[0]
    text+=f'\n\n## 固定小项队列检验\n\n[查看完整固定队列分析](../09_固定小项队列检验/index.html)。1960—2016年每届连续且名称稳定的{len(keys)}个小项中，1964—1976与1996—2016的代表团卫冕率为{early_rate:.1%}与{late_rate:.1%}，差值{difference*100:.2f}个百分点；按小项成组重抽样95%区间[{ci[0]*100:.2f}, {ci[1]*100:.2f}]个百分点。结果描述代表团小项控制权，不代表个人冠军生涯或严格因果效果。\n'
    report.write_text(text,encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False))
