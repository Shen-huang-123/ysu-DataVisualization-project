"""Decompose the 2024 female medal-row/participation-row share gap by sport family."""
from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from task2_localization import SPORT_ZH

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / '交付文件/任务二_百年全景/08_女性结构分解'
OUT.mkdir(parents=True, exist_ok=True)
df = pd.read_csv(ROOT/'项目工作区/outputs/olympics_flagged.csv.gz', usecols=['Year','Sex','Medal','sport_family','include_main'])
df = df[(df.Year == 2024) & df.include_main & df.Sex.isin(['F','M'])].copy()
df['medal'] = df.Medal.isin(['Gold','Silver','Bronze'])
part = df.groupby(['sport_family','Sex']).size().unstack(fill_value=0)
med = df[df.medal].groupby(['sport_family','Sex']).size().unstack(fill_value=0)
families = sorted(set(part.index) | set(med.index))
part, med = part.reindex(families,fill_value=0),med.reindex(families,fill_value=0)
for t in (part,med):
    for sex in ('F','M'):
        if sex not in t.columns:t[sex]=0
pt = part.sum(axis=1);mt=med.sum(axis=1)
pf = part.F / pt.replace(0,np.nan);mf = med.F / mt.replace(0,np.nan)
# No medal rows in a family: its medal weight is zero; set the unused local medal share to participant share.
mf = mf.fillna(pf).fillna(0);pf = pf.fillna(0)
pw = pt/pt.sum();mw = mt/mt.sum()
within = (mf-pf)*(mw+pw)/2
mix = (mw-pw)*(mf+pf)/2
table = pd.DataFrame({'sport_family':families,'运动大类中文':[SPORT_ZH.get(x,x) for x in families],
                      '参赛行':pt.values,'获奖行':mt.values,'女性参赛行占比':pf.values,
                      '女性获奖行占比':mf.values,'项目内结构贡献_百分点':within.values*100,
                      '项目权重贡献_百分点':mix.values*100,'合计贡献_百分点':(within+mix).values*100})
table = table.sort_values('合计贡献_百分点',ascending=False)
table.to_csv(OUT/'2024女性占比分解逐项目.csv',index=False,encoding='utf-8-sig')
gap = float(med.F.sum()/mt.sum()-part.F.sum()/pt.sum())
assert abs(float((within+mix).sum())-gap)<1e-12
summary = {'female_participation_share':float(part.F.sum()/pt.sum()),'female_medal_share':float(med.F.sum()/mt.sum()),
           'gap_pp':gap*100,'within_sport_pp':float(within.sum()*100),'sport_mix_pp':float(mix.sum()*100),
           'participation_rows':int(pt.sum()),'medal_rows':int(mt.sum()),
           'top_positive':table.head(5)[['运动大类中文','合计贡献_百分点']].to_dict('records'),
           'top_negative':table.tail(5)[['运动大类中文','合计贡献_百分点']].to_dict('records')}
(OUT/'女性结构分解摘要.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
plt.rcParams['font.sans-serif']=['Microsoft YaHei','SimHei','DejaVu Sans']
plt.rcParams['axes.unicode_minus']=False
rank=pd.concat([table.head(7),table.tail(7)]).sort_values('合计贡献_百分点')
fig,ax=plt.subplots(figsize=(11,8));fig.patch.set_facecolor('#f5f1e9');ax.set_facecolor('#f5f1e9')
colors=['#b16d51' if x<0 else '#11717c' for x in rank['合计贡献_百分点']]
ax.barh(rank['运动大类中文'],rank['合计贡献_百分点'],color=colors,height=.66)
ax.axvline(0,color='#52686b',linewidth=1);ax.spines[:].set_visible(False);ax.grid(axis='x',color='#d9dfd9',alpha=.7)
ax.set_axisbelow(True);ax.tick_params(length=0,labelsize=11);ax.set_xlabel('对总体女性获奖行占比 − 参赛行占比的贡献（百分点）',labelpad=12)
ax.set_title('50.3% 不是终点：哪些运动拉开了两条曲线？',loc='left',pad=25,fontsize=21,color='#15323a',fontweight='bold')
fig.text(.11,.02,'2024运动员记录行口径；项目贡献可正可负，总和为整体差值。不是个人获奖概率或制度公平度。',fontsize=9,color='#617578')
fig.tight_layout(rect=[0,.04,1,.94]);fig.savefig(OUT/'2024女性差值项目贡献.png',dpi=180,facecolor=fig.get_facecolor());plt.close(fig)

positive = '、'.join(f"{r['运动大类中文']}（+{r['合计贡献_百分点']:.2f}）" for r in summary['top_positive'][:3])
negative = '、'.join(f"{r['运动大类中文']}（{r['合计贡献_百分点']:.2f}）" for r in reversed(summary['top_negative'][-3:]))
report = f'''# 2024 女性获奖占比：1.18 个百分点来自哪里？

**任务二 C 与任务三 S8 交叉研究。** 2024 年女性参赛记录占 {summary['female_participation_share']*100:.2f}%，女性获奖记录占 {summary['female_medal_share']*100:.2f}%，相差 **+{summary['gap_pp']:.3f} 个百分点**。两者都按运动员记录行统计；参赛行 14,892 条、获奖行 2,281 条。

![2024 女性差值项目贡献](2024女性差值项目贡献.png)

## 一个更具体的问题

“超过 50%”可以由两种因素共同形成：不同运动在参赛与获奖记录中的权重变化，以及同一运动家族内部女性记录份额的变化。用对称分解把总差值写为两部分：**项目内部结构 +{summary['within_sport_pp']:.3f} 个百分点**，**运动权重差 {summary['sport_mix_pp']:+.3f} 个百分点**，两项合计 +{summary['gap_pp']:.3f} 个百分点。这里的“内部结构”仍是记录构成差，不是女性运动员的个人夺牌概率。

2024 年贡献较正的运动包括 {positive} 个百分点；较负的包括 {negative} 个百分点。正负项相互抵消，最后只留下 +{summary['gap_pp']:.3f} 个百分点。因此总比例接近 50%，不能说明各运动内部都接近平衡。

## 分解公式与处理

对运动家族 s，令 `P_s` 为该家族占全部参赛行的权重，`M_s` 为占全部获奖行的权重；`p_s` 与 `m_s` 分别是该家族参赛行、获奖行中的女性份额。则总差值为 `Σ(M_s m_s − P_s p_s)`，对称分解为 `Σ[(m_s−p_s)(M_s+P_s)/2] + Σ[(M_s−P_s)(m_s+p_s)/2]`。两部分精确相加回到总差值。无获奖行的家族令 `m_s=p_s`，其项目内部贡献为 0，避免给不可观察的局部比例赋予含义。

## 反例与证据边界

田径的负贡献与赛艇的正贡献都较大，说明整体 50.3% 是异质项目抵消后的结果。团队项目一个获奖小项会产生多条运动员行；项目配额和参赛记录也不是独立运动员。因此本分解不能支持“女性个体更容易夺牌”“某运动制度更公平”或因果解释。若要评价正式机会，应并列研究官方女子、男子、混合小项数和参赛名额。

运行 `项目工作区/scripts/gender_gap_decomposition.py` 复算。输入为任务一归一表中的 2024 届次；[逐运动家族结果](2024女性占比分解逐项目.csv)和[摘要 JSON](女性结构分解摘要.json)随本页交付。主分析排除 1906，2024 Sport 已按任务一运动家族归一。
'''
(OUT/'女性结构分解.md').write_text(report,encoding='utf-8')
html=f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>50.3%不是终点｜女性结构分解</title><style>*{{box-sizing:border-box}}body{{margin:0;background:#f5f1e9;color:#123139;font-family:Microsoft YaHei,system-ui,sans-serif}}a{{color:inherit}}header{{background:#102e36;color:#f6f2ea;padding:65px clamp(20px,6vw,90px)}}header a{{color:#e8c092;font-size:13px}}h1{{font:400 clamp(46px,7vw,92px)/1.1 SimSun,serif;max-width:1000px;margin:35px 0 20px}}header p{{max-width:800px;line-height:1.9;color:#cddbd7}}main{{max-width:1250px;margin:auto;padding:55px clamp(18px,5vw,75px) 100px}}figure{{margin:0 0 65px}}figure img{{width:100%;border-radius:18px;box-shadow:0 20px 50px #102e3620}}section{{border-top:1px solid #bfcbc5;padding:47px 0}}h2{{font:400 clamp(32px,4vw,52px)/1.2 SimSun,serif;margin:0 0 20px}}p{{font-size:16px;line-height:2;max-width:880px}}strong{{color:#a35b36}}.facts{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:38px 0}}.facts div{{padding:25px;background:#fffdf8;border-radius:18px;border-top:3px solid #b77d50}}.facts b{{display:block;font:400 40px Georgia,serif;color:#a35b36;margin-bottom:10px}}.facts span{{font-size:13px;color:#5e7276}}footer{{padding:34px 5vw;background:#102e36;color:#d8e3dd;font-size:13px}}@media(max-width:700px){{.facts{{grid-template-columns:1fr}}}}</style></head><body><header><a href="../05_交互总览/index.html">← 返回百年全景</a><h1>50.3% 不是终点。<br>差值从哪里来？</h1><p>2024 年女性获奖记录占比高于参赛记录占比 1.18 个百分点。把总量拆到运动大类后，正负贡献相互抵消，整体接近一半并不意味着每项运动都相同。</p></header><main><figure><img src="2024女性差值项目贡献.png" alt="各运动大类对女性获奖记录占比和参赛记录占比差值的正负贡献"></figure><div class="facts"><div><b>{summary['gap_pp']:+.3f}</b><span>总体差值 · 百分点</span></div><div><b>{summary['within_sport_pp']:+.3f}</b><span>项目内部结构贡献</span></div><div><b>{summary['sport_mix_pp']:+.3f}</b><span>项目权重贡献</span></div></div><section><h2>总数背后的抵消</h2><p>正向贡献较大的运动有 {positive} 个百分点；负向贡献较大的有 {negative} 个百分点。总差值只有 +{summary['gap_pp']:.3f} 个百分点，是多项结构变化相加后的结果。</p></section><section><h2>怎样复算</h2><p>对每个运动家族分别计算参赛与获奖行的权重、其中女性份额，再用对称分解将整体差值拆为“家族内部份额差”与“家族权重变化”。两部分相加严格等于总差值。<a href="2024女性占比分解逐项目.csv">查看逐项目数据 ↗</a>。</p></section><section><h2>哪些结论不能推出</h2><p>统计单位是运动员记录行，团队项目会产生多行；项目设置和参赛配额也不同。因此这些差值不是个人获奖概率，更不能直接判断某项运动的制度公平度。<a href="女性结构分解.md">阅读完整方法和局限 ↗</a>。</p></section></main><footer>晓组织 · 燕山大学　｜　2024 夏季奥运运动员记录行口径</footer></body></html>'''
(OUT/'女性结构分解.html').write_text(html,encoding='utf-8')

task2_report = ROOT/'交付文件/任务二_百年全景/01_报告与说明/01_百年奥运全景分析_高分版.md'
if task2_report.exists():
    text=task2_report.read_text(encoding='utf-8')
    start,end='<!-- GENDER_DECOMP_START -->','<!-- GENDER_DECOMP_END -->'
    if start in text and end in text:text=text[:text.index(start)]+text[text.index(end)+len(end):]
    add=f'''{start}
### C2. 50.3% 从哪里来？

![2024女性占比差值的项目贡献](../08_女性结构分解/2024女性差值项目贡献.png)

女性获奖行占比比参赛行高 {summary['gap_pp']:.3f} 个百分点。按运动家族作对称分解，项目内部结构贡献为 {summary['within_sport_pp']:+.3f} 个百分点，运动在两种记录中的权重差贡献为 {summary['sport_mix_pp']:+.3f} 个百分点。田径、体操等负贡献与赛艇、足球等正贡献抵消，因此总体接近 50% 不说明各运动同质。这里比较的是**记录构成**，不是个人获奖概率或制度公平度。完整公式、逐运动数据与反例见[女性结构分解](../08_女性结构分解/女性结构分解.md)。
{end}

'''
    text=text.replace('## D. 项目演化',add+'## D. 项目演化',1)
    task2_report.write_text(text,encoding='utf-8')

s8_report = ROOT/'交付文件/任务三_专题深挖/S8_她们登上领奖台/研究说明.md'
if s8_report.exists():
    text=s8_report.read_text(encoding='utf-8')
    start,end='<!-- GENDER_S8_START -->','<!-- GENDER_S8_END -->'
    if start in text and end in text:text=text[:text.index(start)]+text[text.index(end)+len(end):]
    block=f'''\n{start}\n## 跨任务机制分解\n\n2024 年女性获奖行占比与参赛行占比差 +{summary['gap_pp']:.3f} 个百分点。按运动家族对称分解：家族内部结构 +{summary['within_sport_pp']:.3f}，项目权重 {summary['sport_mix_pp']:+.3f} 个百分点。正负运动相互抵消，整体 50.3% 不能代替项目内部判断。详见[任务二女性结构分解](../../任务二_百年全景/08_女性结构分解/女性结构分解.html)。\n{end}\n'''
    s8_report.write_text(text+block,encoding='utf-8')

s8_page = ROOT/'交付文件/任务三_专题深挖/S8_她们登上领奖台/index.html'
if s8_page.exists():
    text=s8_page.read_text(encoding='utf-8')
    start,end='<!-- GENDER_S8_PAGE_START -->','<!-- GENDER_S8_PAGE_END -->'
    if start in text and end in text:text=text[:text.index(start)]+text[text.index(end)+len(end):]
    block=(start+'<aside style="margin:32px auto;padding:25px clamp(20px,5vw,65px);max-width:1100px;background:#173941;'
           'color:#f4f1e9;border-radius:20px;font-family:Microsoft YaHei,system-ui,sans-serif">'
           '<small style="color:#e8bd89">新增 · 2024 机制分解</small>'
           f'<h2>整体 +{summary["gap_pp"]:.2f} 个百分点，项目之间却在抵消。</h2>'
           '<p>分开看运动大类内部结构与项目权重，避免用一个 50.3% 代表全部项目。</p>'
           '<a href="../../任务二_百年全景/08_女性结构分解/女性结构分解.html" style="color:#f3c28d">打开图表和逐项目结果 ↗</a></aside>'+end)
    text=text.replace('<footer',block+'<footer',1)
    s8_page.write_text(text,encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False,indent=2))

# Restore S8 task-page presentation after generating content.
import runpy
runpy.run_path(str(Path(__file__).with_name("publish_women_topic_style.py")))
