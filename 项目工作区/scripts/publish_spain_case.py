from pathlib import Path
import pandas as pd
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[2] / '交付文件'
TASK = ROOT / '任务三_专题深挖/S2_口径的魔力'
DATA = ROOT / '任务一_数据体检/02_交付数据'
OUT = TASK / '02_数据表'

official = pd.read_csv(DATA / '2024官方329小项奖牌表.csv')
assert len(official) == 329 and official.event_id.is_unique
gold = official[official.gold_country_code.fillna('').str.split('|').map(lambda codes: 'ESP' in codes)]
raw = pd.read_csv(DATA / '归一数据_保留原始字段.csv.gz', usecols=['Year','NOC','Medal','sport_family','include_main'])
rows = raw.query("Year == 2024 and NOC == 'ESP' and Medal == 'Gold' and include_main")
labels = {'Football':'足球', 'Water Polo':'水球', 'Athletics':'田径', 'Sailing':'帆船'}
result = pd.DataFrame({'小项金牌':gold.groupby('discipline').size(), '金牌记录':rows.groupby('sport_family').size()})
assert set(result.index) == set(labels) and result.notna().all().all()
rank = pd.read_csv(OUT / 'S2_2024双口径完整排名.csv').set_index('NOC').loc['ESP']
assert list(result.sum()) == [rank.Gold_official, rank.Gold_rows]
result = result.rename(index=labels).sort_values('金牌记录', ascending=False)
result.index.name = '运动'
result['增加记录'] = result['金牌记录'] - result['小项金牌']
result.to_csv(OUT / 'S2_西班牙金牌构成.csv', encoding='utf-8-sig')
team = result.loc[['足球','水球']].sum()
rows_html = ''.join(f'<tr><th scope="row">{name}</th><td>{official_count}</td><td>{athlete_count}</td><td>+{extra}</td></tr>' for name,(official_count,athlete_count,extra) in result.iterrows())
scale = int(result['金牌记录'].max())
bars = []
for name, row in result.iterrows():
    pair = []
    for column in ('小项金牌', '金牌记录'):
        count = int(row[column])
        pair.append(f'<div class="measure"><span>{column}</span><i style="--size:{count / scale:.6%}" aria-hidden="true"></i><strong>{count}</strong></div>')
    bars.append(f'<li><h3>{name}</h3>{"".join(pair)}</li>')
page = f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>巴黎2024西班牙的两种金牌榜</title><style>
:root{{color-scheme:light dark;--paper:#f5f3ed;--ink:#1b363e;--accent:#785525;--context:#42747c;--line:#738f9360}}
html[data-supp-theme="dark"]{{--paper:#15222b;--ink:#edf2ef;--accent:#e3c795;--context:#86bbc4;--line:#a3bdbe45}}
*{{box-sizing:border-box}}body{{font:16px/1.75 system-ui,"Microsoft YaHei",sans-serif;margin:0;color:var(--ink);background:radial-gradient(ellipse at top left,#6a99a32b,transparent 75%) top/100% 26rem no-repeat,var(--paper)}}
main{{padding:clamp(24px,5vw,76px) clamp(20px,6vw,100px)}}main>p{{max-width:78ch;overflow-wrap:anywhere}}.spain-table{{overflow:auto}}
.ranks{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;border-block:1px solid var(--line);padding-block:12px}}
.ranks dd{{margin:0;font-size:clamp(24px,4vw,48px);font-weight:650;color:var(--accent)}}
.sport-chart{{margin:26px 0}}.sport-chart h2{{margin:0}}
.sport-chart ul{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px 32px;padding:0;list-style:none}}
.sport-chart li{{border-top:1px solid var(--line)}}.sport-chart h3{{margin:8px 0}}
.measure{{display:grid;grid-template-columns:5em minmax(0,1fr) 2ch;align-items:center;gap:8px;font-size:.9rem}}
.measure i{{height:10px;width:var(--size);background:var(--context);border-radius:2px}}
.measure:last-child i{{background:var(--accent)}}
@media(max-width:650px){{.sport-chart ul{{grid-template-columns:minmax(0,1fr)}}}}
a{{color:var(--accent)}}a:focus-visible{{outline:2px solid currentColor;outline-offset:3px}}
h1{{font-size:clamp(28px,4vw,50px);line-height:1.2}}table{{width:100%;border-collapse:collapse}}td,th{{padding:10px 6px;border-bottom:1px solid #85928d66}}th:first-child{{text-align:left}}td,thead th:not(:first-child){{text-align:right;font-variant-numeric:tabular-nums}}a{{text-underline-offset:4px}}
html body.spain-case.supplement-reading:not(.supp-existing-nav)>main{{padding-top:clamp(12px,1.5vw,24px)!important}}
</style></head><body><main><a href="../../最终提交材料/00_先看这里.html">← 返回提交材料</a>
<h1>西班牙为什么从第{rank.official_rank:.0f}升到第{rank.row_rank:.0f}？</h1>
<dl class="ranks"><div><dt>官方小项口径</dt><dd>第 {rank.official_rank:.0f} 名</dd></div><div><dt>运动员获奖行口径</dt><dd>第 {rank.row_rank:.0f} 名</dd></div></dl>
<p>巴黎2024按金、银、铜依次比较。西班牙有{rank.Gold_official:.0f}枚小项金牌，对应{rank.Gold_rows:.0f}条运动员金牌记录。足球和水球两枚小项金牌对应{team['金牌记录']}条记录，占全部金牌记录的{team['金牌记录']/rank.Gold_rows:.1%}。</p>
<section class="sport-chart" aria-labelledby="sport-chart-title"><h2 id="sport-chart-title">足球和水球贡献了多少金牌记录？</h2>
<p>所有条形从零开始，使用相同的计数刻度。青色表示小项金牌，金色表示运动员金牌记录。</p>
<ul>{''.join(bars)}</ul></section>
<div class="spain-table" tabindex="0" role="region" aria-label="金牌明细"><table><caption>西班牙金牌按运动拆解</caption><thead><tr><th scope="col">运动</th><th scope="col">小项金牌</th><th scope="col">金牌记录</th><th scope="col">增加记录</th></tr></thead><tbody>{rows_html}</tbody></table></div>
<p>表中分解的是西班牙的金牌记录差额。第{rank.official_rank:.0f}到第{rank.row_rank:.0f}来自全部代表团重新排序，无法把十个名次按运动直接相加。</p>
<p>逐一移除35个运动大类中的任意一个，西班牙在运动员行口径下仍相对上升。该检验每次从两张榜同时移除同一大类并重新排序。</p>
<p><a href="02_数据表/S2_西班牙金牌构成.csv" download>下载构成表</a> · <a href="02_数据表/S2_2024双口径完整排名.csv" download>下载完整双口径排名</a> · <a href="02_数据表/S2_2024代表团剔除敏感性.csv" download>下载剔除检验</a></p>
<p><a href="../../任务一_数据体检/02_交付数据/2024官方329小项奖牌表.csv" download>329项结果</a> · <a href="../../任务一_数据体检/02_交付数据/归一数据_保留原始字段.csv.gz" download>归一运动员记录</a></p></main></body></html>'''
# The evidence-chain page shares this page's directory depth and active task.
template = TASK.parent / '12_反例与证据链/index.html'
shell = BeautifulSoup(template.read_text(encoding='utf-8'), 'html.parser')
document = BeautifulSoup(page, 'html.parser')
for selector in ('link[href*="supplement-reading.css"]', 'link[href*="integrated-nav.css"]',
                 '#supplement-theme-preload', 'script[src*="supplement-reading.js"]',
                 'script[src*="integrated-nav.js"]'):
    document.head.append(shell.select_one(selector))
for selector in ('#xz-nav', '#xz-menu'):
    document.main.insert_before(shell.select_one(selector))
document.body['class'] = ['supplement-reading', 'spain-case']
(TASK / '西班牙双口径案例.html').write_text(str(document), encoding='utf-8')
entry = ROOT / '最终提交材料/00_先看这里.html'
text = entry.read_text(encoding='utf-8')
link = '<p><a href="../任务三_专题深挖/S2_口径的魔力/西班牙双口径案例.html">看西班牙第15到第5的运动拆解与复算 ↗</a></p>'
text = text.replace(link, '')
marker = '</main>'
assert marker in text
entry.write_text(text.replace(marker, link + marker, 1), encoding='utf-8')
