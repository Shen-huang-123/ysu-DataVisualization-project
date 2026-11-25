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
def render_replay(html, reviewed, beijing, london):
    table = '<div class="table" role="region" aria-label="逐项分歧" tabindex="0"><table>'
    content = html.replace('<table>', table).replace('</table>', '</table></div>')
    summary = f"""<dl class="summary">
<div><dt>优先复核分歧</dt><dd>{reviewed} 项</dd></div>
<div><dt>北京 · 名次变化</dt><dd>{beijing} 队</dd></div>
<div><dt>伦敦 · 名次变化</dt><dd>{london} 队</dd></div>
</dl><h2>逐项证据与名次复算</h2>"""
    content = content.replace('<div class="table"', summary + '<div class="table"', 1)
    return """<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>优先分歧复核与奖牌榜影响</title>
<style>
:root{color-scheme:light dark;--paper:#f5f3ed;--ink:#19363c;--muted:#52686b;--accent:#785525;--line:#758b8b55}
@media(prefers-color-scheme:dark){:root{--paper:#15222b;--ink:#eef2ee;--muted:#b0c0bf;--accent:#ddc393;--line:#b6c9c540}}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.7 system-ui,"Microsoft YaHei",sans-serif}
main{padding:clamp(24px,5vw,80px) clamp(20px,6vw,100px)}
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
</style></head><body><main><nav aria-label="补证记录"><a href="index.html">← 返回补证记录</a></nav>""" + content + '</main></body></html>'


(OUT/'优先分歧复核与复算.html').write_text(
    render_replay(html, len(ledger), changes.get(2008, 0), changes.get(2012, 0)),
    encoding='utf-8',
)
index=OUT/'index.html'
page=re.sub(r'<!-- PRIORITY_REPLAY_START -->.*?<!-- PRIORITY_REPLAY_END -->','',index.read_text(encoding='utf-8'),flags=re.S)
marker='<h2>取证清单</h2>'
assert page.count(marker)==1
index.write_text(page.replace(marker,'<!-- PRIORITY_REPLAY_START --><p><a href="优先分歧复核与复算.html">查 7 项奖牌分歧与名次复算</a></p><!-- PRIORITY_REPLAY_END -->'+marker),encoding='utf-8')
print(ledger[['Year','案例','直接名次变化','名次变化数']].to_string(index=False))
print(changes.to_dict())
