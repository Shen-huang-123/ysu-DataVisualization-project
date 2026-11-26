"""Reconcile the seven archive/Olympedia differences and isolate ranking effects."""
from collections import Counter
from pathlib import Path
import re

import markdown
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
TASK = ROOT / '交付文件/任务三_专题深挖/S2_口径的魔力'
BASE = TASK / '08_逐项外部核验'
OUT = BASE / 'IOC现行结果补证进度_20261121'
compare = pd.read_csv(BASE / 'Olympedia独立交叉核验/历史555项独立交叉对照.csv', keep_default_na=False)
disputed = compare.loc[~compare.archive_three_match].set_index(['Year', 'Event'])
colors = ['Gold', 'Silver', 'Bronze']
# The priority is the changed medal color. Preserve the distinction between a
# historical result, a medal action and a complete current IOC event record.
cases = [
    (2008, "Fencing Men's Sabre, Individual", '男子佩剑个人', 'CHN FRA ROU', 'FIE 证实金牌，击剑历史档案核对银铜',
     'https://static.fie.org/uploads/5/26350-ZHONG%20Man.pdf',
     'https://www.usfencingresults.org/history/Olympics/Olympic%20Reports/Individual%20Competitions/Individual%20Competitions%20%20-%20All%20years.pdf'),
    (2008, "Shooting Women's Trap", '女子飞碟多向', 'FIN SVK USA', 'ISSF 逐项结果表',
     'https://www.issf-sports.org/competitions/results?compId=447&ctId=4&view=comp', ''),
    (2008, "Canoeing Men's Kayak Singles, 1,000 metres", '男子单人皮艇 1000 米', 'GBR NOR AUS', 'ICF 历届领奖结果',
     'https://www.canoeicf.com/sites/default/files/icf_canoe_sprint_tokyo_2020_olympic_games_media_guide.pdf', ''),
    (2008, "Modern Pentathlon Women's Individual", '女子现代五项个人', 'GER GBR BLR', 'UIPM 手册证实银牌；IOC 后续颁牌记录优先用于铜牌',
     'https://www.uipmworld.org/sites/default/files/media_guide_digital.pdf',
     'https://www.olympics.com/ioc/news/olympic-highlights-1257'),
    (2008, "Triathlon Men's Olympic Distance", '男子铁人三项', 'GER CAN NZL', 'World Triathlon 赛果',
     'https://triathlon.org/news/frodeno-crowned-olympic-champ', ''),
    (2012, "Canoeing Men's Canadian Singles, 200 metres", '男子单人划艇 200 米', 'UKR RUS ESP', 'IOC 与 ICF 确认银铜递补；金牌沿用一致结果',
     'https://www.olympics.com/cio/news/reattribution-de-medailles-et-de-diplomes-dans-cinq-epreuves-des-jeux-olympiques-de-londres-2012',
     'https://www.canoeicf.com/news/olympian-stripped-medal-after-positive-drug-test'),
    (2012, "Weightlifting Men's Lightweight", '男子举重 69 公斤级', 'CHN INA PRK', 'IOC 确认铜牌递补；金银由 IWF 赛时报道核对',
     'https://www.olympics.com/ioc/news/ioc-executive-board-approves-medal-reallocations-from-olympic-games-london-2012-and-pyeongchang-2018',
     'https://iwf.sport/2012/08/01/lin-lifts-his-way-to-title/'),
]
assert {(year,event) for year,event,*_ in cases} == set(disputed.index)

def medals(text):
    return [item.strip() for item in text.split('|') if item.strip()]

def rank(frame):
    totals = Counter((noc,color) for color in colors for value in frame[color] for noc in medals(value))
    teams = {noc for noc,_ in totals}
    scores = {noc:tuple(totals[noc,color] for color in colors) for noc in teams}
    ordered = sorted(scores.values(),reverse=True)
    ranks = {}
    for index,value in enumerate(ordered,1):
        ranks.setdefault(value,index)
    return {noc:(scores[noc],ranks[scores[noc]]) for noc in teams}

def effects(year, case, before, after):
    old,new=rank(before),rank(after)
    for noc in sorted(old.keys() | new.keys()):
        counts0,r0=old.get(noc,((0,0,0),None))
        counts1,r1=new.get(noc,((0,0,0),None))
        if (counts0,r0)!=(counts1,r1):
            yield dict(Year=year,案例=case,NOC=noc,原金银铜='/'.join(map(str,counts0)),
                       更新金银铜='/'.join(map(str,counts1)),原排名=r0,更新排名=r1,
                       变化色='、'.join(c for c,x,y in zip('金银铜',counts0,counts1) if x!=y))

ledger,ranks=[],[]
for year in sorted({row[0] for row in cases}):
    base=pd.read_csv(TASK/'02_数据表'/f'S2_{year}历史小项代理表.csv',keep_default_na=False).set_index('Event')
    assert len(base)==302 and base.index.is_unique
    selected=[row for row in cases if row[0]==year]
    for _,event,*_ in selected:
        base.loc[event,colors]=disputed.loc[(year,event),[f'{c}_archive' for c in colors]].tolist()
    combined=base.copy()
    for _,event,label,value,scope,source,secondary in selected:
        old=disputed.loc[(year,event)]
        confirmed=value.split()
        assert confirmed==old[[f'{c}_olympedia' for c in colors]].tolist()
        one=base.copy()
        one.loc[event,colors]=confirmed
        combined.loc[event,colors]=confirmed
        change=list(effects(year,label,base,one))
        ranks.extend(change)
        direct=[r for r in change if r['变化色']]
        ledger.append(dict(Year=year,Event=event,案例=label,
                           原金银铜='/'.join(old[f'{c}_archive'] or '空' for c in colors),
                           核对金银铜='/'.join(confirmed),证据范围=scope,来源=source,补充来源=secondary,
                           奖牌变动代表团='、'.join(r['NOC'] for r in direct),
                           名次变化数=sum(r['原排名']!=r['更新排名'] for r in change),
                           直接名次变化='、'.join(f"{r['NOC']} {r['原排名'] or '未上榜'}→{r['更新排名'] or '未上榜'}" for r in direct)))
    ranks.extend(effects(year,'同届全部分歧同时更正',base,combined))
ledger=pd.DataFrame(ledger)
result=pd.DataFrame(ranks)
ledger.to_csv(OUT/'优先分歧逐项复核.csv',index=False,encoding='utf-8-sig')
result.to_csv(OUT/'优先分歧名次复算.csv',index=False,encoding='utf-8-sig')
table=[]
for _,r in ledger.sort_values(['Year','Event']).iterrows():
    links=f"[来源]({r['来源']})"
    if r['补充来源']:
        links+=f" · [补充]({r['补充来源']})"
    table.append(f"| {r.Year} {r['案例']} | {r['原金银铜']} | {r['核对金银铜']} | {r['直接名次变化']} | {r['名次变化数']} | {links} |")
totals=result[result['案例'].eq('同届全部分歧同时更正')]
changes=totals[totals['原排名'].ne(totals['更新排名'])].groupby('Year').size()
body=f"""# 优先分歧复核与奖牌榜影响

555 项中，旧存档与 Olympedia 有 7 项三色不一致。两个金牌空缺分别补为中国和芬兰，另外 5 项涉及银牌空缺、旧铜牌空缺或后续递补。逐项读到的证据范围见下载表。现代五项的白俄罗斯铜牌采用晚于 UIPM 手册的 IOC 颁牌记录。

| 届次和小项 | 旧金/银/铜 | 核对后金/银/铜 | 奖牌变化队名次 | 全榜名次变化队数 | 来源 |
| --- | --- | --- | --- | ---: | --- |
{chr(10).join(table)}

每届从 302 项项目代理表出发，将本批分歧项置为旧存档结果，其他小项固定。依次单独替换每项，再同时替换同届全部分歧项。按金、银、铜排序，完全相同的奖牌数并列。上表的名次来自项目敏感性计算。同届一起替换后，北京有 **{changes.get(2008,0)}** 队、伦敦有 **{changes.get(2012,0)}** 队名次变化，各项位移不能相加。主数据、模型输入与既有榜单保留原版本。

这 7 项的已核对证据包括单项协会结果、历史出版物及 IOC 某色重分配公告。全量 910 项的现行 IOC 逐项核验仍待完成。

[下载逐项证据表](优先分歧逐项复核.csv) · [下载每队名次复算](优先分歧名次复算.csv) · [返回补证记录](index.html)
"""
(OUT/'优先分歧复核与复算.md').write_text(body,encoding='utf-8')
html=markdown.markdown(body,extensions=['tables'])
def add_replay_navigation(page, delivery, destination):
    from os.path import relpath
    from bs4 import BeautifulSoup

    template = delivery / '任务三_专题深挖/12_反例与证据链/index.html'
    shell = BeautifulSoup(template.read_text(encoding='utf-8'), 'html.parser')
    result = BeautifulSoup(page, 'html.parser')
    assets = (
        'link[href*="supplement-reading.css"]', 'link[href*="integrated-nav.css"]',
        '#supplement-theme-preload',
        'script[src*="supplement-reading.js"]', 'script[src*="integrated-nav.js"]',
    )
    for selector in (*assets, '#xz-nav', '#xz-menu'):
        element = shell.select_one(selector)
        for node in (element, *element.select('[href],[src]')):
            for attr in ('href', 'src'):
                if node.has_attr(attr):
                    path, sep, query = node[attr].partition('?')
                    relative = Path(relpath(template.parent / path, destination)).as_posix()
                    node[attr] = relative + sep + query
        if selector in assets:
            result.head.append(element)
        else:
            result.main.insert_before(element)
    result.body['class'] = ['supplement-reading', 'replay-reading']
    return '<!doctype html>' + str(result.html)


RANK_NAMES = {'AUT': '奥地利', 'BEL': '比利时', 'BRA': '巴西', 'CMR': '喀麦隆', 'CRO': '克罗地亚', 'DOM': '多米尼加共和国', 'EST': '爱沙尼亚', 'FIN': '芬兰', 'GRE': '希腊', 'IND': '印度', 'IRI': '伊朗', 'IRL': '爱尔兰', 'LAT': '拉脱维亚', 'LTU': '立陶宛', 'NGR': '尼日利亚', 'NOR': '挪威', 'PAN': '巴拿马', 'POR': '葡萄牙', 'SRB': '塞尔维亚', 'SWE': '瑞典', 'TTO': '特立尼达和多巴哥', 'TUN': '突尼斯'}


def rank_slope(rows):
    from html import escape

    combined = [row for row in rows if row['案例'] == '同届全部分歧同时更正']
    changed = [row for row in combined if int(row['原排名']) != int(row['更新排名'])]
    beijing = sorted((row for row in changed if int(row['Year']) == 2008),
                     key=lambda row: (int(row['原排名']), row['NOC']))
    london = sum(int(row['Year']) == 2012 for row in changed)
    if not beijing:
        return '<p>北京同届合并复算没有名次变化。</p>'
    ranks = [int(row[key]) for row in beijing for key in ('原排名', '更新排名')]
    lo, hi = min(ranks), max(ranks)
    guides = []
    for rank in range((lo + 9) // 10 * 10, hi + 1, 10):
        y = 18 + 228 * (rank - lo) / (hi - lo)
        guides.append(f'<path d="M76 {y:.2f}H484"/><text x="65" y="{y:.2f}">{rank}</text>')
    lines, cards, links = [], [], []
    for row in beijing:
        code = escape(row['NOC'])
        name = escape(RANK_NAMES.get(row['NOC'], row['NOC']))
        before, after = (int(row[key]) for key in ('原排名', '更新排名'))
        y1, y2 = (18 + 228 * (rank - lo) / (hi - lo) for rank in (before, after))
        change = f'上升 {before-after} 位' if before > after else f'下降 {after-before} 位'
        target = f'rank-{code}'
        label = f'{name}，第 {before} → {after} 名，{change}'
        annotation = (f'<text class="rank-annotation" x="494" y="{y2:.2f}">{name} +{before-after}</text>'
                      if before > after else '')
        lines.append(f"""<a href="#{target}" aria-label="{label}" class="{'up' if before > after else 'down'}">
<title>{label}</title><path d="M76 {y1:.2f}L484 {y2:.2f}"/><circle cx="76" cy="{y1:.2f}" r="3"/><circle cx="484" cy="{y2:.2f}" r="3"/>{annotation}</a>""")
        links.append(f'<a href="#{target}">{name} <small>{before} → {after}</small></a>')
        medal_cells = []
        for medal, old, new in zip(('金牌', '银牌', '铜牌'),
                                  row['原金银铜'].split('/'), row['更新金银铜'].split('/')):
            delta = int(new) - int(old)
            state = f'{delta:+d} 枚' if delta else '无变化'
            style = ' class="medal-changed"' if delta else ''
            medal_cells.append(f'<div{style}><dt>{medal}</dt><dd>{old} → {new}<small>{state}</small></dd></div>')
        cards.append(f"""<article id="{target}" tabindex="-1"><h3>{name} <small>{code}</small></h3>
<p>第 {before} 名 → 第 {after} 名 · {change}</p>
<dl class="rank-medals" aria-label="金银铜复算前后对照">{''.join(medal_cells)}</dl></article>""")
    return f"""<section class="rank-slope" aria-labelledby="rank-slope-title">
<h2 id="rank-slope-title">北京 2008 · 合并复算后的名次变化</h2>
<p>北京 {len(beijing)} 队、伦敦 {london} 队名次变化。图中显示北京名次有变化的代表团，并列名次位于同一高度。点击连线或队名可核对逐队结果。</p>
<div class="rank-layout"><div class="rank-chart"><div class="rank-labels"><span>旧存档名次</span><span>同届合并复算名次</span></div>
<svg viewBox="0 0 590 264" aria-label="北京名次坡度图">
<g class="rank-guides" aria-hidden="true"><path d="M76 18V246 M484 18V246"/>{''.join(guides)}</g>
{''.join(sorted(lines, key=lambda line: 'class="up"' in line))}
</svg>
<div class="rank-labels"><span>图示范围：第 {lo}–{hi} 名</span><span>金色上升 · 青色下降</span></div></div>
<div class="rank-roster"><div class="rank-details">{''.join(cards)}</div>
<h3>名次变化的代表团</h3><div class="rank-links">{''.join(links)}</div></div></div>
<p><a href="优先分歧名次复算.csv" download>下载完整逐队复算 CSV ↓</a></p>
</section>"""


def render_replay(html, reviewed, beijing, london, rows):
    table = '<div class="table" role="region" aria-label="逐项分歧" tabindex="0"><table>'
    content = html.replace('<table>', table).replace('</table>', '</table></div>')
    summary = f"""<dl class="summary">
<div><dt>优先复核分歧</dt><dd>{reviewed} 项</dd></div>
<div><dt>北京 · 名次变化</dt><dd>{beijing} 队</dd></div>
<div><dt>伦敦 · 名次变化</dt><dd>{london} 队</dd></div>
</dl>"""
    content = content.replace('<div class="table"', summary + rank_slope(rows) + '<h2>逐项证据与名次复算</h2><div class="table"', 1)
    return """<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>优先分歧复核与奖牌榜影响</title>
<style>
:root{color-scheme:light dark;--paper:#f5f3ed;--ink:#19363c;--muted:#52686b;--accent:#785525;--line:#758b8b55}
html[data-supp-theme="dark"]{--paper:#15222b;--ink:#eef2ee;--muted:#b0c0bf;--accent:#ddc393;--line:#b6c9c540}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.7 system-ui,"Microsoft YaHei",sans-serif}
@media screen {
body.replay-reading { isolation: isolate; }
body.replay-reading::after {
  content: ""; position: absolute; inset: 0 0 auto; height: clamp(18rem,38vw,34rem);
  z-index: -1; pointer-events: none;
  background:
    radial-gradient(ellipse at 10% 0%, #638e9d30, transparent 74%),
    radial-gradient(ellipse at 94% 0%, #b0915924, transparent 72%);
}
body.replay-reading tbody tr:is(:hover,:focus-within) td {
  background-color: color-mix(in srgb,var(--sr-accent) 9%,var(--sr-paper)) !important;
}
}
@media screen and (prefers-reduced-motion:no-preference) {
  body.replay-reading::after { animation: replay-glow 16s ease-in-out infinite alternate; }
  .replay-reading .summary > div { animation: replay-summary 420ms cubic-bezier(.22,1,.36,1) both; }
  .replay-reading .summary > div:nth-child(2) { animation-delay: 55ms; }
  .replay-reading .summary > div:nth-child(3) { animation-delay: 110ms; }
  .replay-reading tbody td { transition: background-color 160ms ease; }
}
@keyframes replay-glow { from { opacity: .62; } to { opacity: 1; } }
@keyframes replay-summary { from { opacity: .72; translate: 0 7px; } to { opacity: 1; translate: 0 0; } }
html body.replay-reading.supplement-reading:not(.supp-existing-nav)>main{padding-top:clamp(12px,1.5vw,24px)!important}
h1{font-size:clamp(30px,4vw,58px);line-height:1.2;margin:24px 0 16px}h2{font-size:clamp(22px,2.6vw,34px);line-height:1.3}
p{max-width:78ch;color:var(--muted)}a{color:var(--accent);text-underline-offset:4px}
a:focus-visible,.table:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
.summary{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:4px 12px;border-block:1px solid var(--line);padding-block:16px;margin:24px 0}
.summary dt{color:var(--muted);font-size:.85rem}.summary dd{margin:0;font-size:clamp(22px,3vw,38px);font-weight:650;color:var(--accent)}
.table{overflow:auto;border:1px solid var(--line);margin-bottom:22px}
table{width:100%;min-width:48rem;border-collapse:collapse;font-variant-numeric:tabular-nums}
td,th{padding:.75rem;text-align:left;border-bottom:1px solid var(--line)}
th{background:color-mix(in srgb,var(--paper) 90%,var(--ink));font-size:.9rem}
td:nth-child(3),td:nth-child(5){color:var(--accent);font-weight:600}
tbody tr:last-child td{border-bottom:0}

.rank-slope{margin-block:28px;border-bottom:1px solid var(--line);padding-bottom:14px}
.rank-layout{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr);gap:clamp(20px,4vw,60px);align-items:start}
.rank-slope svg{display:block;width:100%;height:auto}
.rank-labels{display:flex;justify-content:space-between;gap:8px;color:var(--muted);font-size:.88rem}
.rank-slope svg path{fill:none;stroke:currentColor;stroke-width:1.5}
body.replay-reading .rank-slope svg a.down{color:#397c86;opacity:.55}
html[data-supp-theme="dark"] body.replay-reading .rank-slope svg a.down{color:#83c6ce}
body.replay-reading .rank-slope svg a.up{color:var(--accent)}
.rank-slope svg a.up path{stroke-width:3}
body.replay-reading .rank-slope svg a:is(:hover,:focus-visible){opacity:1}
.rank-slope svg a:is(:hover,:focus-visible) path{stroke-width:5}
.rank-slope svg circle{fill:currentColor}
.rank-guides{color:var(--line)}
.rank-guides text{fill:var(--muted);font:12px system-ui;text-anchor:end;dominant-baseline:middle}
.rank-roster h3{margin:0 0 8px;font-size:1rem}
.rank-links{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0 14px}
.rank-links a{display:flex;align-items:center;justify-content:space-between;gap:6px;min-height:44px;border-bottom:1px solid var(--line);font-size:.88rem;text-decoration:none}
.rank-links a:hover{text-decoration:underline}
.rank-links small{white-space:nowrap;color:var(--muted);font-variant-numeric:tabular-nums}
@media(max-width:850px){.rank-layout{grid-template-columns:minmax(0,1fr)}}
.rank-details article{display:none;scroll-margin-top:95px}
.rank-details article:target{display:block;border-inline-start:2px solid var(--accent);padding-inline-start:12px}

.rank-annotation{fill:currentColor;font:600 15px system-ui;dominant-baseline:middle}
.rank-chart{min-width:0;padding-block:8px}
.rank-details article:target{margin-bottom:16px;padding-block:8px}
.rank-details article h3,.rank-details article p{margin:0 0 4px}
.rank-links a:focus-visible{background:color-mix(in srgb,var(--accent) 12%,transparent)}

.rank-medals{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin:12px 0 0}
.rank-medals>div{border-top:1px solid var(--line);padding-top:6px}
.rank-medals dt,.rank-medals small{color:var(--muted);font-size:.8rem}
.rank-medals dd{margin:0;font-variant-numeric:tabular-nums;font-weight:650}
.rank-medals small{display:block;font-weight:400}
.rank-medals .medal-changed{border-color:var(--accent)}
.rank-medals .medal-changed :is(dt,dd,small){color:var(--accent)}
</style></head><body><main><nav aria-label="补证记录"><a href="index.html">← 返回补证记录</a></nav>""" + content + '</main></body></html>'


(OUT/'优先分歧复核与复算.html').write_text(
    add_replay_navigation(
        render_replay(html, len(ledger), changes.get(2008, 0), changes.get(2012, 0), totals.to_dict('records')),
        OUT.parents[3], OUT,
    ),
    encoding='utf-8',
)
index=OUT/'index.html'
page=re.sub(r'<!-- PRIORITY_REPLAY_START -->.*?<!-- PRIORITY_REPLAY_END -->','',index.read_text(encoding='utf-8'),flags=re.S)
marker='<h2>取证清单</h2>'
assert page.count(marker)==1
index.write_text(page.replace(marker,'<!-- PRIORITY_REPLAY_START --><p><a href="优先分歧复核与复算.html">查 7 项奖牌分歧与名次复算</a></p><!-- PRIORITY_REPLAY_END -->'+marker),encoding='utf-8')
print(ledger[['Year','案例','直接名次变化','名次变化数']].to_string(index=False))
print(changes.to_dict())
