"""Map manually read IOC decisions to historical events without certifying whole events.

The input statements are reading notes, not downloaded original IOC webpages.
Run from any directory; no network or changes to the primary results.
"""
from pathlib import Path
import hashlib
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / '交付文件/任务三_专题深挖/S2_口径的魔力/08_逐项外部核验'
OUT = BASE / 'IOC决议补证_20261117'
OUT.mkdir(exist_ok=True)
prefix = 'https://www.olympics.com/ioc/news/'
jun21 = prefix + 'ioc-executive-board-approves-medal-reallocations-from-olympic-games-london-2012-and-pyeongchang-2018'
nov21 = prefix + 'five-london-2012-events-to-have-medals-diplomas-reallocated'
ceremony = prefix + 'ten-olympians-from-three-editions-of-the-olympic-games-awarded-their-olympic-medals-during-reallocation-ceremony-at-paris-2024'
notes = []
def add(year, event, medal, noc, athlete, url, scope, locator):
    notes.append(dict(Year=year, Event=event, Medal=medal, NOC=noc, athlete=athlete,
                      source_url=url, evidence_scope=scope, locator=locator,
                      read_date='2026-11-17', capture='浏览工具正文阅读的结构化记录；不是原网页存档'))

add(2012, "Weightlifting Men's Lightweight", 'Bronze', 'PRK', 'Myong Hyok Kim', jun21, 'IOC明确批准铜牌递补', '正文男子69kg段')
add(2012, "Weightlifting Women's Light-Heavyweight", 'Bronze', 'COL', 'Ubaldina Valoyes Cuesta', jun21, 'IOC明确批准铜牌递补；该文另述银牌当时暂缓，不外推现行银牌', '正文女子69kg段')
add(2008, "Weightlifting Women's Light-Heavyweight", 'Silver', 'COL', 'Leidy Solis', prefix+'olympic-highlights-121', 'IOC官网记载银牌已补颁', 'National Olympic Committees / Colombian NOC')
add(2008, "Weightlifting Women's Heavyweight", 'Silver', 'ESP', 'Lydia Valentin', prefix+'olympic-highlights-124', 'IOC官网记载银牌已补颁', 'National Olympic Committees / Spanish NOC')
add(2012, "Weightlifting Men's Light-Heavyweight", 'Bronze', 'EGY', 'Tarek Yehia Fouad Abdelazim', ceremony, 'IOC官网2024补颁仪式确认', 'London 2012 / Weightlifting / 85kg')
add(2012, "Weightlifting Men's Super-Heavyweight", 'Bronze', 'KOR', 'Sangguen Jeon', ceremony, 'IOC官网2024补颁仪式确认', 'London 2012 / Weightlifting / +105kg')
event = "Wrestling Men's Super-Heavyweight, Freestyle"
add(2012, event, 'Gold', 'IRI', 'Komeil Ghasemi', nov21, 'IOC公告列并列第1；仅记录该次决定', '第5小项排名1')
add(2012, event, 'Gold', 'RUS', 'Bilyal Makhov', nov21, '公告列并列第1但附当时禁赛暂不颁发条件；2024后状态仍待追查', '第5小项排名1及星号脚注')
add(2012, event, 'Bronze', 'KAZ', 'Daulet Shabanbay', nov21, 'IOC公告列并列第3', '第5小项排名3')
add(2012, event, 'Bronze', 'USA', 'Tervel Dlagnev', nov21, 'IOC公告列并列第3', '第5小项排名3')
event = "Canoeing Men's Canadian Singles, 200 metres"
add(2012, event, 'Silver', 'RUS', 'Ivan Shtyl', nov21, 'IOC明确批准银牌递补；未在本公告重列金牌', '第4小项排名2')
add(2012, event, 'Bronze', 'ESP', 'Alfonso Benavidez', nov21, 'IOC明确批准铜牌递补', '第4小项排名3')

reference_path = BASE / 'Olympedia独立交叉核验/历史555项独立交叉对照.csv'
reference = pd.read_csv(reference_path).fillna('')
coverage = pd.read_csv(BASE / '历史910项来源覆盖总表.csv').fillna('')
for row in notes:
    key = (coverage.Year.eq(row['Year']) & coverage.Event.eq(row['Event']))
    assert key.sum() == 1, row
    match = reference[reference.Year.eq(row['Year']) & reference.Event.eq(row['Event'])]
    row['in_555_queue'] = len(match) == 1
    if len(match):
        value = str(match.iloc[0][row['Medal']+'_olympedia'])
        row['Olympedia_value'] = value
        row['NOC_present_in_secondary_value'] = row['NOC'] in value
    else:
        row['Olympedia_value'] = ''
        row['NOC_present_in_secondary_value'] = ''
    row['whole_event_current_IOC_verified'] = False
df = pd.DataFrame(notes)
assert len(df)==12 and not df.duplicated(['Year','Event','Medal','NOC']).any()
df.to_csv(OUT/'IOC逐奖牌动作与现有记录对照.csv',index=False,encoding='utf-8-sig')
summary = dict(read_records=len(df), events=len(df[['Year','Event']].drop_duplicates()),
               source_pages=df.source_url.nunique(),
               events_in_555=len(df[df.in_555_queue][['Year','Event']].drop_duplicates()),
               newly_certified_complete_current_IOC_events=0,
               reference_sha256=hashlib.sha256(reference_path.read_bytes()).hexdigest(),
               note='逐奖牌决议证据补充，保留条件和历史时点；不覆盖主表，不减555全项待核验数。')
(OUT/'检查摘要.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False,indent=2))
