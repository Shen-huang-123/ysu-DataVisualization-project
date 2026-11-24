"""Reproducible small-delegation cohort and IOC-source audit for topic three."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / '交付文件' / '任务三_专题深挖'
OUT = BASE / 'S4_小代表团的大突破' / '02_客观样本'
OUT.mkdir(parents=True, exist_ok=True)

d = pd.read_csv(ROOT / '项目工作区' / 'outputs' / 'olympics_flagged.csv.gz', low_memory=False)
d = d[d.Year.between(2000, 2024) & d.include_main.eq(True)].copy()
edition = d.groupby(['NOC', 'Year'], as_index=False).agg(
    participation_rows=('NOC', 'size'), medal_rows=('is_medal', 'sum'))
cohort = edition.groupby('NOC').agg(
    editions=('Year', 'size'), median_participation_rows=('participation_rows', 'median'),
    medal_editions=('medal_rows', lambda x: int((x > 0).sum())), medal_rows=('medal_rows', 'sum')).reset_index()
eligible = cohort[cohort.editions.ge(3)].copy()
threshold = float(eligible.median_participation_rows.quantile(.25))
eligible['bottom_quartile'] = eligible.median_participation_rows.le(threshold)
eligible['selected'] = eligible.bottom_quartile & eligible.medal_editions.ge(1) & ~eligible.NOC.isin(['AIN', 'EOR', 'IOA'])
eligible['selection_reason'] = eligible.apply(
    lambda r: '非国家奥委会中立/难民/独立身份' if r.NOC in ['AIN','EOR','IOA'] else
    ('至少三届、规模处于下四分位且至少一届获奖' if r.selected else
     ('未获奖' if r.medal_editions == 0 else '规模高于下四分位门槛')), axis=1)
eligible.sort_values(['selected','median_participation_rows','NOC'], ascending=[False,True,True]).to_csv(
    OUT / '2000_2024全部候选及纳入判定.csv', index=False, encoding='utf-8-sig')
chosen = eligible[eligible.selected].sort_values(['medal_rows','NOC'], ascending=[False,True])
chosen.to_csv(OUT / '客观小代表团清单.csv', index=False, encoding='utf-8-sig')
edition[edition.NOC.isin(chosen.NOC)].to_csv(OUT / '入选代表团逐届记录.csv', index=False, encoding='utf-8-sig')

old = ['HKG','TPE','SGP','FIJ','BER','JOR','KOS']
old_status = eligible[eligible.NOC.isin(old)][['NOC','editions','median_participation_rows','medal_editions','selected']]
old_status.to_csv(OUT / '原七案例与客观门槛对照.csv', index=False, encoding='utf-8-sig')
names = '、'.join(chosen.NOC.tolist())
md = f'''# 小代表团：预先定义的可复现样本

## 纳入规则

研究窗为 2000—2024 七届夏奥会。先按 `NOC×Year` 计算参赛运动员行，至少出现三届的代表团形成比较总体（{len(eligible)} 个）。用各代表团逐届参赛行的中位数衡量典型规模；总体的第 25 百分位为 **{threshold:g} 行**。预先规定“中位数不高于该门槛，且至少一届有获奖行”为小代表团突破候选。AIN、EOR、IOA 等非国家奥委会身份单列，不进入国家代表团比较。最终 **{len(chosen)} 个**：{names}。

此规则在查看获奖多寡前确定规模门槛；“至少一届获奖”只定义本专题的突破样本，不作为成功率的分母。完整候选和排除理由见 `2000_2024全部候选及纳入判定.csv`，逐届记录见 `入选代表团逐届记录.csv`。

## 反例与稳健性

原专题的 HKG、TPE、SGP、FIJ、BER、JOR、KOS 是叙事案例，其中多数不属于最小规模四分位。它们仍可作为有代表性的突破故事，但不能被称为客观筛出的“小代表团全体”。本规则下的样本以低参赛人数为特征，奖牌行极少，单届一枚奖牌即可造成巨大比例波动；不计算“奖牌行/参赛行”来声称效率或培养质量。若门槛改成 100 行，会得到完全不同的更宽泛群体，应作为另一个预先定义的问题。

## 计算方式

`python 项目工作区/scripts/task3_evidence_upgrade.py`。源数据为任务一审计后的 `olympics_flagged.csv.gz`。运动员行口径会受团体项目人数影响；本清单不等于按官方小项奖牌定义的最小代表团榜。
'''
(OUT / '样本定义与反例.md').write_text(md, encoding='utf-8')
rows = ''.join(f'<tr><td>{r.NOC}</td><td>{r.editions}</td><td>{r.median_participation_rows:g}</td><td>{r.medal_editions}</td><td>{r.medal_rows}</td></tr>' for r in chosen.itertuples())
html = f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>小代表团客观样本</title><style>body{{margin:0;background:#eee9df;color:#172c43;font-family:"Microsoft YaHei",sans-serif}}main{{max-width:980px;margin:auto;padding:60px 24px}}h1{{font-size:clamp(36px,6vw,66px)}}p{{line-height:1.8}}table{{width:100%;border-collapse:collapse;background:#fffaf2;border-radius:18px;overflow:hidden}}td,th{{padding:13px;text-align:left;border-bottom:1px solid #ddd2c3}}.note{{background:#153653;color:#fff;padding:26px;border-radius:22px;margin:28px 0}}a{{color:#216299}}.note a{{color:#b8dcff}}</style></head><body><main><small>任务三 / 小代表团</small><h1>先定门槛，<br>再讲突破。</h1><p>2000—2024 年至少参加三届的 {len(eligible)} 个代表团中，参赛行中位数的下四分位门槛是 <strong>{threshold:g} 行</strong>。再要求至少一届获奖，并单列中立、难民和独立身份，得到 {len(chosen)} 个代表团。</p><table><thead><tr><th>代表团代码</th><th>参赛届数</th><th>典型参赛行</th><th>获奖届数</th><th>获奖行</th></tr></thead><tbody>{rows}</tbody></table><div class="note"><h2>这个结果挑战了原专题的选例</h2><p>原七个故事案例大多不在最小规模四分位内。它们可以继续讲述，但不能代替按统一门槛筛出的总体。小样本的比例极不稳定，也不能把运动员获奖行当作官方奖牌数或运动员培养效率。</p><a href="原七案例与客观门槛对照.csv">查看原七案例对照</a></div><p><a href="2000_2024全部候选及纳入判定.csv">下载全部候选与排除理由</a>　<a href="入选代表团逐届记录.csv">下载逐届数据</a></p></main></body></html>'''
(OUT / 'index.html').write_text(html, encoding='utf-8')
source = BASE / 'S4_小代表团的大突破' / '研究说明.md'
txt = source.read_text(encoding='utf-8')
txt = txt.split('\n\n## 客观样本复核')[0]
txt += f'\n\n## 客观样本复核\n\n原七个案例为叙事选例；[客观样本与反例](02_客观样本/index.html)按 2000—2024 年至少三届、参赛规模下四分位（≤{threshold:g} 行）、至少一届获奖的预设门槛筛出 {len(chosen)} 个代表团。结论不等同于官方小项奖牌效率。\n'
source.write_text(txt, encoding='utf-8')

# S3 的事实只引用 IOC 页面；数据本身只提供缺席与身份代码的观察。
s3 = BASE / 'S3_地缘政治的投影'
sources = [
    ('1980 / 1984 抵制背景', 'IOC 回顾 1980 与 1984 年接连的抵制', 'https://www.olympics.com/ioc/news/ioc-president-thomas-bach-reflects-on-the-boycott-of-the-olympic-games-moscow-1980-40-years-later', '支持两届抵制事件的存在；不支持由数据直接判定每个缺席代表团的动机'),
    ('1992 独联体联队', 'IOC 巴塞罗那 1992 回顾', 'https://www.olympics.com/ioc/news/barcelona-1992-a-city-turning-towards-the-sea-and-winning-the-hearts-of-the-world', '支持十二个前苏联共和国以联队参赛；不应与单一现存国家直接拼接'),
    ('1992 独立身份', 'IOC 奥林匹克休战历史', 'https://www.olympics.com/ioc/news/the-history-of-the-olympic-truce', '支持前南斯拉夫运动员以奥林匹克旗帜参赛；身份与独联体联队不同'),
    ('2024 中立运动员', 'IOC AIN 资格条件决定', 'https://www.olympics.com/ioc/news/strict-eligibility-conditions-in-place-as-ioc-eb-approves-individual-neutral-athletes-ains-for-the-olympic-games-paris-2024', 'AIN 为个人资格安排，不等同于俄罗斯国家奥委会代表队'),
    ('2024 难民代表队', 'IOC 参赛国家与运动员 FAQ', 'https://www.olympics.com/ioc/faq/sports-programme-and-results/how-many-athletes-and-countries-take-part-in-the-olympic-games', '将国家奥委会、AIN 与 EOR 分列'),
]
ledger = pd.DataFrame(sources, columns=['核验事项','IOC一手文献','网址','允许支持的结论'])
ledger.to_csv(s3 / 'IOC一手来源核验.csv', index=False, encoding='utf-8-sig')
s3_note = '# S3 地缘政治专题：一手来源与推断边界\n\n'
for topic, title, url, implication in sources:
    s3_note += f'- **{topic}**：[ {title} ]({url})。{implication}。\n'
s3_note += '\n## 结论层级\n\n数据直接支持各届出现的代表团代码、参赛行和奖牌行。IOC 文献支持特定历史事件和身份制度。两类证据合读，才能解释部分结构断点；不得从未出现的代码反推个别代表团的唯一缺席动机。1980 / 1984 年的参赛总量与 IOC 官方国家奥委会数量可能口径不同，本专题标为数据集覆盖值。\n'
(s3 / 'IOC一手来源核验.md').write_text(s3_note, encoding='utf-8')
items = ''.join(
    f'<li><span class="ioc-year">{year}</span><strong>{name}</strong><p>{implication}。</p><a href="{url}">{title}</a></li>'
    for topic, title, url, implication in sources
    for year, name in [topic.rsplit(' ', 1)]
)
(s3 / 'IOC一手来源核验.html').write_text(f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>S3 IOC一手来源核验</title><style>body{{margin:0;background:#eee9df;color:#172c43;font-family:"Microsoft YaHei",sans-serif}}main{{max-width:900px;margin:auto;padding:60px 24px}}h1{{font-size:clamp(36px,6vw,60px)}}li{{background:#fffaf2;margin:14px 0;padding:20px;border-radius:18px;line-height:1.7}}a{{color:#196298}}.note{{padding:25px;border-radius:20px;background:#173754;color:#fff;line-height:1.8}}</style><style id="ioc-source-contrast">
html:has(#ioc-source-contrast) body main>ol{{--ioc-rule:#8caaa859;list-style:none;padding:0;margin:28px 0;border-top:1px solid var(--ioc-rule)}}
html:has(#ioc-source-contrast) body main>ol>li{{display:grid;grid-template-columns:8rem minmax(0,1fr);column-gap:24px;margin:0!important;padding:20px 4px!important;border:0;border-bottom:1px solid var(--ioc-rule);border-radius:0!important;background:transparent!important;color:#20343c!important}}
html:has(#ioc-source-contrast) body .ioc-year{{grid-row:1/4;color:#52646c;font-variant-numeric:tabular-nums;align-self:start;padding-top:.2em}}
html:has(#ioc-source-contrast) body main>ol>li strong{{color:inherit!important;font-size:1.14em}}
html:has(#ioc-source-contrast) body main>ol>li p{{color:#40555f!important;margin:4px 0 7px!important;max-width:78ch}}
html:has(#ioc-source-contrast) body main>ol>li a{{color:#175b70!important;justify-self:start;text-underline-offset:.22em;overflow-wrap:anywhere}}
html:has(#ioc-source-contrast) body.xz-dark main>ol>li,html:has(#ioc-source-contrast)[data-supp-theme=dark] body main>ol>li{{color:#f1f5f4!important}}
html:has(#ioc-source-contrast) body.xz-dark main>ol>li :is(p,.ioc-year),html:has(#ioc-source-contrast)[data-supp-theme=dark] body main>ol>li :is(p,.ioc-year){{color:#c5d4d9!important}}
html:has(#ioc-source-contrast) body.xz-dark main>ol>li a,html:has(#ioc-source-contrast)[data-supp-theme=dark] body main>ol>li a{{color:#a9dce9!important}}
@media(max-width:650px){{
html:has(#ioc-source-contrast) body main>ol>li{{grid-template-columns:minmax(0,1fr);padding-block:16px!important}}
html:has(#ioc-source-contrast) body .ioc-year{{grid-row:auto;margin-bottom:4px}}
}}
</style></head><body><main><small>任务三 / 地缘政治的投影</small><h1>数据记录缺席，<br>史料解释背景。</h1><ol>{items}</ol><div class="note">数据直接支持代表团代码、参赛行和奖牌行。IOC 文献支持特定事件与身份制度。不得从某代表团在数据中缺席，反推它的唯一政治动机。</div></main></body></html>''', encoding='utf-8')
s3_research = s3 / '研究说明.md'
s3_text = s3_research.read_text(encoding='utf-8').split('\n\n## IOC 一手来源核验')[0]
s3_text += '\n\n## IOC 一手来源核验\n\n[打开逐条 IOC 来源与推断边界](IOC一手来源核验.html)。1980 / 1984 抵制背景、1992 联队与独立身份、2024 AIN/EOR 均有对应 IOC 文献；数据集中的“未出现”仍不能解释个别代表团的唯一缺席原因。\n'
s3_research.write_text(s3_text, encoding='utf-8')
for folder, href, heading, copy in [
    (s3, 'IOC一手来源核验.html', '历史解释逐条核验', '1980／1984抵制、1992联队与2024中立身份均链接到IOC一手文献。'),
    (BASE/'S4_小代表团的大突破', '02_客观样本/index.html', '小代表团客观样本', '先用统一门槛筛选208个代表团，再看9个真正处于最小规模四分位的突破案例。')]:
    page=folder/'index.html'
    if page.exists():
        body=page.read_text(encoding='utf-8')
        marker='<!-- evidence-upgrade -->'
        if marker not in body:
            card=f'''{marker}<a href="{href}" style="display:block;max-width:1050px;margin:32px auto;padding:24px 28px;border-radius:20px;background:#173956;color:#fff;text-decoration:none;font-family:'Microsoft YaHei',sans-serif"><small style="color:#a7d1f1">证据升级 / 点击查看</small><h2 style="margin:8px 0;font-size:25px;color:#fff">{heading} ↗</h2><p style="margin:0;color:#dce9ef;line-height:1.7">{copy}</p></a>'''
            page.write_text(body.replace('</body>',card+'</body>',1),encoding='utf-8')
print(f'eligible={len(eligible)}, threshold={threshold:g}, selected={len(chosen)}: {names}')
