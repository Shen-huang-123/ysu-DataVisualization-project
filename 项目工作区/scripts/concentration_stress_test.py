"""Stress-test the work's deconcentration thesis under alternative units and windows."""
from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / '交付文件/任务二_百年全景/07_结论压力测试'
OUT.mkdir(parents=True, exist_ok=True)

cols = ['Year', 'NOC', 'Sport', 'Event', 'Medal', 'include_main', 'duplicate_excess']
df = pd.read_csv(ROOT / '项目工作区/outputs/olympics_flagged.csv.gz', usecols=cols)
df = df[df.include_main].copy()
medals = df[df.Medal.isin(['Gold', 'Silver', 'Bronze'])].copy()

def measures(frame, unit):
    result = []
    for year, group in frame.groupby('Year'):
        counts = group.groupby('NOC').size().sort_values(ascending=False)
        shares = counts / counts.sum()
        n = len(shares)
        hhi = float((shares ** 2).sum())
        result.append(dict(Year=int(year), unit=unit, medal_units=int(counts.sum()), medal_nocs=n,
                           top5_share=float(shares.head(5).sum()), hhi=hhi,
                           effective_nocs=float(1 / hhi),
                           normalized_hhi=float((hhi - 1 / n) / (1 - 1 / n)) if n > 1 else 1))
    return result

rows = measures(medals, '运动员获奖行')
rows += measures(medals[~medals.duplicate_excess], '运动员行·排除重复余量')
# Pre-2020 proxy is not an IOC medal total; generic Event values invalidate later years.
proxy = medals[medals.Year <= 2016].drop_duplicates(['Year', 'NOC', 'Sport', 'Event', 'Medal'])
rows += measures(proxy, '同届项目奖牌组代理（≤2016）')
tab = pd.DataFrame(rows).sort_values(['unit', 'Year'])
tab.to_csv(OUT / '逐届集中度三口径.csv', index=False, encoding='utf-8-sig')

wide = tab.pivot(index='Year', columns='unit', values='top5_share')
main = tab[tab.unit == '运动员获奖行'].set_index('Year')
proxy_tab = tab[tab.unit == '同届项目奖牌组代理（≤2016）'].set_index('Year')
summary = {
    '1896_top5_rows': float(main.loc[1896, 'top5_share']),
    '2024_top5_rows': float(main.loc[2024, 'top5_share']),
    '1904_top5_rows': float(main.loc[1904, 'top5_share']),
    '2016_top5_rows': float(main.loc[2016, 'top5_share']),
    '2016_top5_proxy': float(proxy_tab.loc[2016, 'top5_share']),
    '2016_effective_nocs_rows': float(main.loc[2016, 'effective_nocs']),
    '2024_effective_nocs_rows': float(main.loc[2024, 'effective_nocs']),
    '2024_top5_no_duplicate_excess': float(tab[(tab.unit == '运动员行·排除重复余量') & (tab.Year == 2024)].top5_share.iloc[0]),
    'modern_rows_spearman': float(main.loc[main.index >= 1992].index.to_series().corr(main.loc[main.index >= 1992, 'top5_share'], method='spearman')),
    'modern_proxy_spearman': float(proxy_tab.loc[proxy_tab.index >= 1992].index.to_series().corr(proxy_tab.loc[proxy_tab.index >= 1992, 'top5_share'], method='spearman')),
    'proxy_early_median': float(proxy_tab.loc[proxy_tab.index <= 1936, 'top5_share'].median()),
    'proxy_modern_median': float(proxy_tab.loc[proxy_tab.index >= 1992, 'top5_share'].median()),
    'rows_early_median': float(main.loc[main.index <= 1936, 'top5_share'].median()),
    'rows_modern_median': float(main.loc[main.index >= 1992, 'top5_share'].median()),
}
(OUT / '结论压力测试摘要.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
fig, (ax, ax2) = plt.subplots(2, 1, figsize=(12.5, 8.4), sharex=True, gridspec_kw={'height_ratios': [2, 1]})
fig.patch.set_facecolor('#f5f1e9')
for a in (ax, ax2):
    a.set_facecolor('#f5f1e9')
    a.spines[['top', 'right', 'left']].set_visible(False)
    a.grid(axis='y', color='#d9d8cf', alpha=.75, zorder=0)
    a.tick_params(length=0, colors='#4d666a', labelsize=10)
ax.plot(main.index, main.top5_share * 100, color='#0f6670', marker='o', markersize=3.5, linewidth=2.4, label='运动员获奖行', zorder=3)
ax.plot(proxy_tab.index, proxy_tab.top5_share * 100, color='#bd8054', marker='o', markersize=3.1, linewidth=2, linestyle='--', label='小项奖牌组代理（截至2016）', zorder=3)
ax.set_ylabel('前五代表团获奖份额（%）', color='#344e53', labelpad=16)
ax.set_ylim(0, 102)
ax.legend(loc='upper right', frameon=False, fontsize=10)
ax.annotate('1904 · 极端早期届次', (1904, main.loc[1904, 'top5_share'] * 100), xytext=(1924, 93), color='#9a603b', fontsize=10, arrowprops={'arrowstyle': '-', 'color': '#9a603b'})
ax2.plot(main.index, main.effective_nocs, color='#496f79', linewidth=2.2, marker='o', markersize=3.2)
ax2.set_ylabel('有效获奖代表团数 1/HHI', color='#344e53', labelpad=16)
ax2.set_xlabel('夏季奥运届次年份', color='#344e53', labelpad=12)
fig.suptitle('奖牌更分散了吗？换统计单位与时间窗口再看', x=.08, y=.98, ha='left', color='#112f36', fontsize=22, fontweight='bold')
fig.text(.08, .01, '主分析排除1906。小项奖牌组为历史代理，不等于IOC官方奖牌；2020起Event泛化，代理线止于2016。', fontsize=9, color='#5d7375')
fig.tight_layout(rect=[0, .035, 1, .94])
fig.savefig(OUT / '集中度三口径压力测试.png', dpi=180, facecolor=fig.get_facecolor())
plt.close(fig)

pp = lambda x: f'{x*100:.1f}%'
report = f'''# 结论压力测试｜奖牌更分散了吗？

**晓组织 · 任务二补充研究。** 主报告提出“扩张中的去集中化”：前五代表团获奖运动员行份额由 1896 年 {pp(summary['1896_top5_rows'])} 降至 2024 年 {pp(summary['2024_top5_rows'])}。这条长期叙事需要经得起统计单位、重复候选和观察窗口的检验。

![集中度压力测试](集中度三口径压力测试.png)

## 发现一：长期方向存在，但不是每届都下降

早期（1896—1936）前五份额的届次中位数为 **{pp(summary['rows_early_median'])}**，1992—2024 为 **{pp(summary['rows_modern_median'])}**。1904 年的 {pp(summary['1904_top5_rows'])} 是极端早期届次，不能让单个起点代替整个早期。改用各届中位数之后，长期下降仍然成立。

**反直觉的最近一段：**2016 年前五份额为 {pp(summary['2016_top5_rows'])}，2024 年回升到 {pp(summary['2024_top5_rows'])}；按 HHI 换算的“有效获奖代表团数”同期从 {summary['2016_effective_nocs_rows']:.1f} 降至 {summary['2024_effective_nocs_rows']:.1f}，尽管实际获得奖牌记录的代表团数从 {int(main.loc[2016,'medal_nocs'])} 增至 {int(main.loc[2024,'medal_nocs'])}。这说明“获奖代表团更多”与“奖牌分布更均匀”并非同一命题。本页不把两届波动推断成长期逆转。

## 发现二：团队成员行不是唯一解释

把 2016 年及以前的记录按“届次 × 代表团 × Sport × Event × Medal”合为一个奖牌组代理后，早期前五份额中位数为 **{pp(summary['proxy_early_median'])}**，1992—2016 为 **{pp(summary['proxy_modern_median'])}**。长期方向在这一替代单位下仍出现。2016 年运动员行口径的前五份额为 {pp(summary['2016_top5_rows'])}，代理口径为 {pp(summary['2016_top5_proxy'])}，具体水平并不相同。

这个代理**不是 IOC 官方小项奖牌表**：历史同名 Event、并列奖牌与记录缺口都可能影响组数。2020 起 Event 泛化，故代理线停在 2016；2024 只显示可审计的运动员行，不把泛化 Event 硬接到历史代理曲线。

## 发现三：重复候选处理不改变 2024 主结论

主分析保留任务一标记的重复候选；仅删除“重复余量”后的 2024 前五份额为 **{pp(summary['2024_top5_no_duplicate_excess'])}**，与保留时的 {pp(summary['2024_top5_rows'])} 相差 **{abs(summary['2024_top5_no_duplicate_excess']-summary['2024_top5_rows'])*100:.3f} 个百分点**。这只检验一项数据清洗决定，不能替代对所有源数据误差的评估。

## 机制、边界与复现

赛事扩容使更多代表团获得参赛和获奖机会；但项目组合、团队人数、主办与抵制背景会同时改变分配。因此本图支持“长期竞争格局更分散”的描述，却**不识别去集中化的单一因果机制**。HHI 为各代表团份额平方和，有效获奖代表团数为 `1/HHI`；它反映分配均匀度，与简单的获奖代表团数不同。

运行 `项目工作区/scripts/concentration_stress_test.py` 复算。输入为任务一归一表 `项目工作区/outputs/olympics_flagged.csv.gz`；完整逐届结果见 [逐届集中度三口径.csv](逐届集中度三口径.csv)，摘要见 [结论压力测试摘要.json](结论压力测试摘要.json)。主分析排除 1906，历史 NOC 不做政体合并，奖牌为运动员获奖行。图和报告可作为任务二正式报告 A 节的稳健性补充。
'''
(OUT / '结论压力测试.md').write_text(report, encoding='utf-8')
html = f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>奖牌更分散了吗｜结论压力测试</title><style>*{{box-sizing:border-box}}body{{margin:0;background:#f5f1e9;color:#123139;font-family:Microsoft YaHei,system-ui,sans-serif}}a{{color:inherit}}header{{background:#102e36;color:#f6f2ea;padding:65px clamp(20px,6vw,90px)}}header a{{color:#e8c092;font-size:13px}}h1{{font:400 clamp(46px,7vw,92px)/1.1 SimSun,serif;max-width:1000px;margin:35px 0 20px}}header p{{max-width:800px;line-height:1.9;color:#cddbd7}}main{{max-width:1250px;margin:auto;padding:55px clamp(18px,5vw,75px) 100px}}figure{{margin:0 0 65px}}figure img{{width:100%;border-radius:18px;box-shadow:0 20px 50px #102e3620}}section{{border-top:1px solid #bfcbc5;padding:47px 0}}h2{{font:400 clamp(32px,4vw,52px)/1.2 SimSun,serif;margin:0 0 20px}}p{{font-size:16px;line-height:2;max-width:880px}}strong{{color:#a35b36}}.facts{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:38px 0}}.facts div{{padding:25px;background:#fffdf8;border-radius:18px;border-top:3px solid #b77d50}}.facts b{{display:block;font:400 43px Georgia,serif;color:#a35b36;margin-bottom:10px}}.facts span{{font-size:13px;color:#5e7276}}footer{{padding:34px 5vw;background:#102e36;color:#d8e3dd;font-size:13px}}@media(max-width:700px){{.facts{{grid-template-columns:1fr}}}}</style></head><body><header><a href="../05_交互总览/index.html">← 返回百年全景</a><h1>奖牌更分散了吗？<br>换个单位，再看一遍。</h1><p>长期的去集中化是真实存在的描述，但最近两届出现反向波动。把结论放在不同分母、不同观察窗口和清洗决定下检验，才知道它能说到哪一步。</p></header><main><figure><img src="集中度三口径压力测试.png" alt="1896至2024年前五代表团份额，以及有效获奖代表团数趋势"></figure><div class="facts"><div><b>{pp(summary['rows_early_median'])}</b><span>1896—1936 前五份额中位数</span></div><div><b>{pp(summary['rows_modern_median'])}</b><span>1992—2024 前五份额中位数</span></div><div><b>{summary['2016_effective_nocs_rows']:.1f} → {summary['2024_effective_nocs_rows']:.1f}</b><span>2016—2024 有效获奖代表团数</span></div></div><section><h2>长期下降，也有局部反弹</h2><p>1896 年前五份额为 {pp(summary['1896_top5_rows'])}，2024 年为 {pp(summary['2024_top5_rows'])}。改用早期和现代各届中位数，下降方向仍在。但 2016 年的 {pp(summary['2016_top5_rows'])} 到 2024 年回升为 {pp(summary['2024_top5_rows'])}；获奖代表团从 {int(main.loc[2016,'medal_nocs'])} 增至 {int(main.loc[2024,'medal_nocs'])}，并不意味着份额同时更均匀。</p></section><section><h2>换统计单位，方向是否还在？</h2><p>2016 年以前，将同届、代表团、运动、小项和奖牌类型合为一个历史奖牌组代理；早期前五份额中位数 {pp(summary['proxy_early_median'])}，1992—2016 为 {pp(summary['proxy_modern_median'])}。方向仍在，但代理不是 IOC 官方小项表；2020 起 Event 泛化，不能继续接线。</p></section><section><h2>检查清洗决定</h2><p>2024 年保留重复候选余量时前五份额为 {pp(summary['2024_top5_rows'])}，删除重复余量后为 {pp(summary['2024_top5_no_duplicate_excess'])}，相差 {abs(summary['2024_top5_no_duplicate_excess']-summary['2024_top5_rows'])*100:.3f} 个百分点。该差异小，但只覆盖这一项处理选择。</p></section><section><h2>这张图不能证明什么</h2><p>赛事扩容、团队规模、项目设置、主办和抵制都可能改变分布；描述性趋势不能识别单一因果机制。有效获奖代表团数定义为 1/HHI，HHI 为各代表团份额平方和。<a href="结论压力测试.md">阅读完整方法、边界和复现说明 ↗</a></p></section></main><footer>晓组织 · 燕山大学　｜　运动员行口径；1906 排除；2020 后历史小项代理停用</footer></body></html>'''
(OUT / '结论压力测试.html').write_text(html, encoding='utf-8')

# Keep the new evidence reachable after the normal Task 2 regeneration pipeline.
dashboard = ROOT / '交付文件/任务二_百年全景/05_交互总览/index.html'
if dashboard.exists():
    text = dashboard.read_text(encoding='utf-8')
    start, end = '<!-- CONCENTRATION_START -->', '<!-- CONCENTRATION_END -->'
    if start in text and end in text:
        text = text[:text.index(start)] + text[text.index(end) + len(end):]
    promo = (start + '<aside style="margin:20px auto;padding:24px clamp(20px,5vw,70px);max-width:1280px;'
             'background:#173941;color:#f5f1e9;border-radius:22px;display:flex;align-items:center;'
             'justify-content:space-between;gap:25px;flex-wrap:wrap"><div><small style="color:#e6b483">新增 · 结论压力测试</small>'
             '<h2 style="margin:8px 0;font-size:clamp(22px,3vw,37px)">奖牌更分散了吗？</h2>'
             '<p style="margin:0;color:#d9e6de">双单位、早晚期与重复候选对照；2016—2024 出现反向波动。</p></div>'
             '<a href="../07_结论压力测试/结论压力测试.html" style="color:#f3c18d;font-weight:800;white-space:nowrap">打开证据图与方法 ↗</a></aside>' + end)
    text = text.replace('<main', promo + '<main', 1)
    dashboard.write_text(text, encoding='utf-8')

task2_report = ROOT / '交付文件/任务二_百年全景/01_报告与说明/01_百年奥运全景分析_高分版.md'
if task2_report.exists():
    text = task2_report.read_text(encoding='utf-8')
    start, end = '<!-- CONCENTRATION_REPORT_START -->', '<!-- CONCENTRATION_REPORT_END -->'
    if start in text and end in text:
        text = text[:text.index(start)] + text[text.index(end) + len(end):]
    insert = f'''{start}
### A2. 长期去集中化的压力测试

![换统计单位与观察窗口的集中度压力测试](../07_结论压力测试/集中度三口径压力测试.png)

前五代表团获奖行份额的早期届次中位数为 {pp(summary['rows_early_median'])}，1992—2024 为 {pp(summary['rows_modern_median'])}；把 2016 年及以前改为同届项目奖牌组代理，两个时期的中位数分别为 {pp(summary['proxy_early_median'])} 和 {pp(summary['proxy_modern_median'])}，长期下降方向仍在。但 2016—2024 的获奖行前五份额从 {pp(summary['2016_top5_rows'])} 回升至 {pp(summary['2024_top5_rows'])}，有效获奖代表团数从 {summary['2016_effective_nocs_rows']:.1f} 降至 {summary['2024_effective_nocs_rows']:.1f}，不能把长期趋势写成“每届持续下降”。历史代理不是 IOC 官方小项表，2020 起 Event 泛化后不再计算。完整分母、反例、逐届数据与复现见[结论压力测试](../07_结论压力测试/结论压力测试.md)。
{end}

'''
    text = text.replace('## B. 强国兴衰', insert + '## B. 强国兴衰', 1)
    task2_report.write_text(text, encoding='utf-8')

task2_report_html = task2_report.with_suffix('.html')
if task2_report_html.exists():
    text = task2_report_html.read_text(encoding='utf-8')
    start, end = '<!-- CONCENTRATION_HTML_START -->', '<!-- CONCENTRATION_HTML_END -->'
    if start in text and end in text:
        text = text[:text.index(start)] + text[text.index(end) + len(end):]
    block = (start + '<aside style="max-width:1200px;margin:32px auto;padding:28px clamp(20px,4vw,50px);'
             'background:#173941;color:#f4f0e8;border-radius:20px;font-family:Microsoft YaHei,system-ui,sans-serif">'
             '<small style="color:#e5bb88">新增 · 主结论稳健性</small><h2 style="margin:10px 0">长期分散，近期并非单调。</h2>'
             f'<p>2016—2024 前五代表团获奖行份额从 {pp(summary["2016_top5_rows"])} 回升到 {pp(summary["2024_top5_rows"])}；'
             '换统计单位与观察窗口的完整检验见 '
             '<a style="color:#f0c28c" href="../07_结论压力测试/结论压力测试.html">结论压力测试 ↗</a>。</p></aside>' + end)
    text = text.replace('<main', block + '<main', 1)
    task2_report_html.write_text(text, encoding='utf-8')
print(json.dumps(summary, ensure_ascii=False, indent=2))


# Preserve the reviewed reading layout after analytical regeneration.
import runpy
runpy.run_path(str(Path(__file__).with_name("publish_pressure_reading.py")))
