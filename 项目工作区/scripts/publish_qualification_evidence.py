"""Publish dated Olympic qualification evidence and historical medal decisions."""
from pathlib import Path
import re
import markdown
import pandas as pd

ROOT=Path(__file__).resolve().parents[2]
T4=ROOT/'交付文件/任务四_开放创作'
OUT=T4/'05_满分升级/18_LA28资格核验'
OUT.mkdir(exist_ok=True)
RULE='https://stillmed.olympics.com/media/Documents/Olympic-Games/LA28'
BASEBALL='https://www.usopc.org/news/2026/march/16/last-call-registration-closes-march-18-for-the-first-la28-ticket-draw-and-locals-presale-'
CRICKET='https://www.icc-cricket.com/news/how-teams-can-qualify-at-the-la28'
FLAG='https://www.americanfootball.sport/2026/08/16/canada-and-united-states-crowned-ifaf-world-flag-2026-champions'
LACROSSE='https://worldlacrosse.sport/wl-confirms-olympic-pathway-from-continental-sixes-championships-to-la28/'
rows=[
 ('棒球','男子',6,'USA DOM VEN','WBSC Premier12 两席，最终资格赛一席','BSB',BASEBALL),
 ('垒球','女子',6,'USA','世界杯决赛一席，三场赛区资格赛各一席，最终资格赛一席','BSB',''),
 ('板球T20','男子',6,'','分洲排名四席，主办席有排名门槛，最终资格赛一席','CRT',CRICKET),
 ('板球T20','女子',6,'AUS GBR IND RSA','洲别世界杯名额已公布，主办席有排名门槛，最终资格赛一席','CRT',CRICKET),
 ('腰旗橄榄球','男子',6,'USA ITA CAN','主办资格以持续参赛和合规为条件，其余名额经后续资格阶段产生','FFB',FLAG),
 ('腰旗橄榄球','女子',6,'USA CAN MEX','主办资格以持续参赛和合规为条件，其余名额经后续资格阶段产生','FFB',FLAG),
 ('六人制长曲棍球','男子',6,'','2027 世锦赛决出五席（含符合资格的东道主），终资格赛一席','LAC',LACROSSE),
 ('六人制长曲棍球','女子',6,'','2027 世锦赛决出五席（含符合资格的东道主），终资格赛一席','LAC',LACROSSE),
 ('壁球单打','男子',16,'','洲际赛事、条件主办席、PSA 榜、普遍性席位和终资格赛','SQU',''),
 ('壁球单打','女子',16,'','洲际赛事、条件主办席、PSA 榜、普遍性席位和终资格赛','SQU',''),
]
detail=[]
for sport,gender,quota,nocs,path,code,source in rows:
    names=nocs.split()
    assert len(names)==len(set(names))<=quota
    detail.append({'小项':sport,'组别':gender,'单位':'运动员' if code=='SQU' else '队',
                   '总名额':quota,'已核实公布代表团':nocs,'已核实名额':len(names),
                   '未纳入已核实数量':quota-len(names),'资格路径':path,
                   'IOC规则':f'{RULE}/{code}-LA28-Qualification-System.pdf',
                   '进度来源':source or f'{RULE}/{code}-LA28-Qualification-System.pdf'})
data=pd.DataFrame(detail)
assert len(data)==10 and data['已核实名额'].sum()==14
data.to_csv(OUT/'十小项资格快照.csv',index=False,encoding='utf-8-sig')
lines=[]
for row in detail:
    lines.append(f"| {row['小项']} {row['组别']} | {row['总名额']}{row['单位']} | {row['已核实公布代表团'] or '本表未录入'} | {row['资格路径']} | [规则]({row['IOC规则']}) · [进度]({row['进度来源']}) |")
md=f"""# LA28 新增运动资格核验

截至 2026-11-21，五项新增运动的 10 个奖牌小项均可查到 IOC 资格制度。本次核实公开名额 14 个，其中包括美国主办名额。腰旗橄榄球美国主办席仍附条件。空白表示本次未录入已核实名额。

| 小项 | 满额规模 | 已核实公布的代表团 | 资格路径与待确认条件 | 一手来源 |
| --- | ---: | --- | --- | --- |
{chr(10).join(lines)}

## 与预测衔接

资格条件按小项和组别解释。已公布参赛资格仅确定可参加对应小项。未公布的席位留空。女子板球的英国席位通过英格兰取得，西印度群岛联合队需按各自奥委会资格路径处理。长曲棍球洲际赛晋级的是 2027 世锦赛。壁球按个人排名和个人资格确认，每个代表团每组最多两人。

历史模型已有里约七人制橄榄球和东京棒球两个完整配方类比。规则与已公布名额提供赛前约束，余下资格赛和 LA28 实际赛果仍决定完整模型能否验证。当前 2028 主榜继续使用中性基准点估计。

[下载十小项资格快照](十小项资格快照.csv) · [历史回放与误差](../16_预测区间时序核验/index.html) · [返回预测页](../../02_2028洛杉矶预测/index.html)
"""
(OUT/'资格核验说明.md').write_text(md,encoding='utf-8')
def write_page(path,title,body):
    html=markdown.markdown(body,extensions=['tables']).replace('<table>','<div class="table" tabindex="0"><table>').replace('</table>','</table></div>')
    path.write_text(f'<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><style>:root{{color-scheme:light dark}}main{{max-width:74rem;margin:auto;padding:clamp(16px,4vw,56px);font:16px/1.75 system-ui}}.table{{overflow:auto}}table{{width:100%;min-width:45rem;border-collapse:collapse}}th,td{{padding:.65rem;text-align:left;border-bottom:1px solid #83928e88}}a{{text-underline-offset:.2em}}</style><main>{html}</main></html>',encoding='utf-8')
write_page(OUT/'index.html','LA28 新增运动资格核验',md)
T3=ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力/08_逐项外部核验'
I=T3/'IOC现行结果补证进度_20261121'
CEREMONY='https://www.olympics.com/ioc/news/ten-olympians-from-three-editions-of-the-olympic-games-awarded-their-olympic-medals-during-reallocation-ceremony-at-paris-2024'
DECISION='https://www.olympics.com/cio/news/reattribution-de-medailles-et-de-diplomes-dans-cinq-epreuves-des-jeux-olympiques-de-londres-2012'
records=[
 (2008,"Athletics Women's Long Jump",'BRA','NGR','JAM','IOC颁发记录确认铜牌；世界田联确认三色',CEREMONY,'the-xxix-olympic-games-6977748/results/women/long-jump'),
 (2012,"Athletics Men's High Jump",'USA','CAN|GBR|QAT','','IOC决定附完整领奖名次：并列第二三席，无铜牌',DECISION,'the-xxx-olympic-games-6999193/results/men/high-jump'),
 (2012,"Athletics Women's High Jump",'RUS','USA','ESP','IOC决定确认铜牌递补，金银见世界田联',DECISION,'the-xxx-olympic-games-6999193/results/women/high-jump'),
]
keys=pd.read_csv(T3/'历史910项来源覆盖总表.csv').set_index(['Year','Event'])
for year,event,gold,silver,bronze,*_ in records:
    prior=keys.loc[(year,event),"status"]
    medals="/".join((gold,silver,bronze or "—"))
    assert f"世界田联现行名次：{medals}；" in prior
supp=pd.DataFrame(records,columns=['Year','Event','Gold','Silver','Bronze','证据范围','IOC来源','世界田联路径'])
supp['世界田联路径']='https://worldathletics.org/competitions/olympic-games/'+supp['世界田联路径']+'/final/result'
supp.to_csv(I/'IOC决定与颁发记录补充.csv',index=False,encoding='utf-8-sig')
ioc_md=f"""# IOC 奖牌修订补证

本轮对照 IOC 决定或颁发记录与世界田联现行决赛表。三项结果与原世界田联核验表一致，本轮补入 IOC 一手依据。伦敦男子跳高由 IOC 决定列出完整领奖名次，另两项由 IOC 确认铜牌。910 项全量仍需带版本的 IOC 逐项结果。

| 小项 | 金 | 银 | 铜 | 证据 |
| --- | --- | --- | --- | --- |
| 北京 2008 女子跳远 | BRA | NGR | JAM | [IOC 颁发记录]({CEREMONY}) · [世界田联决赛]({supp.iloc[0]['世界田联路径']}) |
| 伦敦 2012 男子跳高 | USA | CAN、GBR、QAT | 无 | [IOC 重分配决定]({DECISION}) · [世界田联决赛]({supp.iloc[1]['世界田联路径']}) |
| 伦敦 2012 女子跳高 | RUS | USA | ESP | [IOC 重分配决定]({DECISION}) · [世界田联决赛]({supp.iloc[2]['世界田联路径']}) |

[下载逐项补证表](IOC决定与颁发记录补充.csv) · [返回 910 项补证进度](index.html)
"""
(I/'IOC奖牌修订补证.md').write_text(ioc_md,encoding='utf-8')
write_page(I/'IOC奖牌修订补证.html','IOC 奖牌修订补证',ioc_md)

def insert_link(page,marker,href,label,inline=False):
    html=page.read_text(encoding='utf-8')
    html=re.sub(r'<!-- VERIFIED_QUOTAS_START -->.*?<!-- VERIFIED_QUOTAS_END -->','',html,flags=re.S)
    assert marker in html,page
    anchor=f'<a href="{href}">{label} ↗</a>'
    body=" · "+anchor if inline else "<p>"+anchor+"</p>"
    link=f"<!-- VERIFIED_QUOTAS_START -->{body}<!-- VERIFIED_QUOTAS_END -->"
    page.write_text(html.replace(marker,link+marker,1),encoding='utf-8')
insert_link(I/'index.html','<h2>取证清单</h2>','IOC奖牌修订补证.html','核对三项 IOC 决定与颁发记录')
for section in ['02_2028洛杉矶预测','03_数据新闻']:
    insert_link(T4/section/'index.html','<!-- FORECAST_INTERVAL_START -->',
                '../05_满分升级/18_LA28资格核验/index.html','查看五项新增运动的 IOC 资格和已公布名额',inline=True)
