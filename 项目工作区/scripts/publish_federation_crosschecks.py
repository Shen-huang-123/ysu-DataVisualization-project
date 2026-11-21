"""Cross-check historical podiums against international federation publications."""
from pathlib import Path
import re
import pandas as pd
import markdown

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / '交付文件/任务三_专题深挖/S2_口径的魔力/08_逐项外部核验'
OUT = BASE / 'IOC现行结果补证进度_20261121'
FIBA_M = 'https://www.fiba.basketball/en/history/320-mens-olympic-basketball-tournament/'
FIBA_W = 'https://about.fiba.basketball/es/our-sport/basketball/national-team-competition-systems/olympic-womens-basketball-tournaments'
IHF08 = 'https://archive.ihf.info/en-us/mediacentre/theroadto/olympicgames2012/historyoftheolympicgames/handballtournamentsatthebeijing2008olympicg.aspx'
IHF12 = 'https://archive.ihf.info/files/Uploads/Documents/11044_Medal%20Standings.pdf'
IHF16 = 'https://www.ihf.info/sites/default/files/2020-01/IHF%20Activity%20Report%202013-2017_E.pdf'
FIH = 'https://www.fih.hockey/static-assets/pdf/fih_paris2024_mediakit_hockey.pdf'
data = [
    ('Basketball','FIBA','Men','USA ESP ARG','USA ESP RUS','USA SRB ESP',[FIBA_M]*3),
    ('Basketball','FIBA','Women','USA AUS RUS','USA FRA AUS','USA ESP SRB',[FIBA_W]*3),
    ('Handball','IHF','Men','FRA ISL ESP','FRA SWE CRO','DEN FRA GER',[IHF08,IHF12,IHF16]),
    ('Handball','IHF','Women','NOR RUS KOR','NOR MNE ESP','RUS FRA NOR',[IHF08,IHF12,IHF16]),
    ('Hockey','FIH','Men','GER ESP AUS','GER NED AUS','ARG BEL GER',[FIH]*3),
    ('Hockey','FIH','Women','NED CHN ARG','NED ARG GBR','GBR NED GER',[FIH]*3),
]
rows = []
for sport, fed, gender, *values in data:
    for year, medals, url in zip((2008,2012,2016),values[:3],values[3]):
        g,s,b=medals.split()
        rows.append(dict(Year=year,Event=f"{sport} {gender}'s {sport}",协会=fed,
                         Gold=g,Silver=s,Bronze=b,一手来源=url,复核日期='2026-11-21'))
BWF = 'https://res.cloudinary.com/badminton/images/v1721624876/wordpress_assets_test/Badminton-World-Federation-Paris-2024-Media-Guide/Badminton-World-Federation-Paris-2024-Media-Guide.pdf'
ITF = 'https://www.itftennis.com/media/2451/tokyo-2020-olympic-tennis-event-regulations.pdf'
FIVB = 'https://en.volleyballworld.com/volleyball/competitions/volleyball-olympic-games-paris-2024/competition/previous-winners'
BEACH = 'https://en.volleyballworld.com/beachvolleyball/competitions/olympics-2020/competition/beachvolleyball-at-the-olympics'
additional = [
    ("Badminton Men's Singles", 'BWF', BWF, 'CHN MAS CHN', 'CHN MAS CHN', 'CHN MAS DEN'),
    ("Badminton Women's Singles", 'BWF', BWF, 'CHN CHN INA', 'CHN CHN IND', 'ESP IND JPN'),
    ("Badminton Men's Doubles", 'BWF', BWF, 'INA CHN KOR', 'CHN DEN KOR', 'CHN MAS GBR'),
    ("Badminton Women's Doubles", 'BWF', BWF, 'CHN KOR CHN', 'CHN JPN RUS', 'JPN DEN KOR'),
    ('Badminton Mixed Doubles', 'BWF', BWF, 'KOR INA CHN', 'CHN CHN DEN', 'INA MAS CHN'),
    ("Tennis Men's Singles", 'ITF', ITF, 'ESP CHI SRB', 'GBR SUI ARG', 'GBR ARG JPN'),
    ("Tennis Women's Singles", 'ITF', ITF, 'RUS RUS RUS', 'USA RUS BLR', 'PUR GER CZE'),
    ("Tennis Men's Doubles", 'ITF', ITF, 'SUI SWE USA', 'USA FRA FRA', 'ESP ROU USA'),
    ("Tennis Women's Doubles", 'ITF', ITF, 'USA ESP CHN', 'USA CZE RUS', 'RUS SUI CZE'),
    ('Tennis Mixed Doubles', 'ITF', ITF, None, 'BLR GBR USA', 'USA USA CZE'),
    ("Volleyball Men's Volleyball", 'Volleyball World', FIVB, 'USA BRA RUS', 'RUS BRA ITA', 'BRA ITA USA'),
    ("Volleyball Women's Volleyball", 'Volleyball World', FIVB, 'BRA USA CHN', 'BRA USA JPN', 'CHN SRB USA'),
    ("Beach Volleyball Men's Beach Volleyball", 'Volleyball World', BEACH, 'USA BRA BRA', 'GER BRA LAT', 'BRA ITA NED'),
    ("Beach Volleyball Women's Beach Volleyball", 'Volleyball World', BEACH, 'USA CHN CHN', 'USA USA BRA', 'GER BRA USA'),
]
for event,fed,url,*medal_sets in additional:
    for year,medals in zip((2008,2012,2016),medal_sets):
        if medals is None:
            continue
        gold,silver,bronze=medals.split()
        rows.append(dict(Year=year,Event=event,协会=fed,Gold=gold,Silver=silver,
                         Bronze=bronze,一手来源=url,复核日期='2026-11-21'))
first=pd.DataFrame(rows)
old=pd.read_csv(BASE/'Olympedia独立交叉核验/历史555项独立交叉对照.csv',keep_default_na=False)
queue=pd.read_csv(OUT/'555项优先取证范围.csv')
keys=['Year','Event']
assert len(first.merge(queue,on=keys,validate='one_to_one'))==len(first)==59
cols=['Gold','Silver','Bronze']
comparison=[f'{colour}_{source}' for source in ('archive','olympedia','proxy') for colour in cols]
result=first.merge(old[keys+comparison+['event_url']],on=keys,how='left',validate='one_to_one',indicator=True)
assert result['_merge'].eq('both').all()
result=result.drop(columns='_merge').sort_values(keys)
labels={'archive':'旧存档','olympedia':'Olympedia','proxy':'主数据代理'}
for source,label in labels.items():
    result[label+'差异色']=result.apply(lambda r:'、'.join(name for col,name in zip(cols,['金','银','铜']) if r[col]!=r[f'{col}_{source}']),axis=1)
result.to_csv(OUT/'协会一手逐项交叉核验.csv',index=False,encoding='utf-8-sig')
counts={label:int(result[label+'差异色'].eq('').sum()) for label in labels.values()}
table=[]
for _,r in result.iterrows():
    marks=[r[label+'差异色'] or '一致' for label in labels.values()]
    table.append(f"| {r.Year} | {r.Event} | {r.Gold} / {r.Silver} / {r.Bronze} | {' | '.join(marks)} | [{r['协会']}]({r['一手来源']}) |")
body=f"""# 三届历史奖牌 · 国际单项协会交叉核验

累计核对北京 2008 19 项、伦敦 2012 20 项、里约 2016 20 项，均在 555 项优先取证清单。原有篮球、手球和曲棍球 18 项，本轮新增羽毛球 15 项、网球 14 项、室内排球和沙滩排球各 6 项。按届次和小项逐色与旧存档、Olympedia 和主数据代理比对。双打每对只计一个奖牌槽。

三色一致的项目数分别为 **旧存档 {counts['旧存档']}/59、Olympedia {counts['Olympedia']}/59、主数据代理 {counts['主数据代理']}/59**。协会结果提供各项目的一手交叉证据，现行 IOC 全量核验仍以 IOC 逐项结果为准，现有数据表保留原版本。

| 届次 | 小项 | 协会金 / 银 / 铜 | 旧存档 | Olympedia | 主数据代理 | 一手来源 |
| --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(table)}

[下载核验明细](协会一手逐项交叉核验.csv) · [返回历史 IOC 补证进度](index.html)
"""
(OUT/'协会一手逐项交叉核验.md').write_text(body,encoding='utf-8')
html=markdown.markdown(body,extensions=['tables'])
(OUT/'协会一手逐项交叉核验.html').write_text('<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>国际单项协会交叉核验</title><style>:root{color-scheme:light dark}main{max-width:74rem;margin:auto;padding:clamp(16px,4vw,56px);font:16px/1.7 system-ui}section{overflow:auto}table{border-collapse:collapse;min-width:44rem}td,th{padding:.55rem;border-bottom:1px solid #82978d88;text-align:left}</style><main>'+html.replace('<table>','<section aria-label="逐项核验表" tabindex="0"><table>').replace('</table>','</table></section>')+'</main></html>',encoding='utf-8')
p=OUT/'index.html'
s=re.sub(r'<!-- FEDERATION_CHECK_START -->.*?<!-- FEDERATION_CHECK_END -->','',p.read_text(encoding='utf-8'),flags=re.S)
marker='<h2>取证清单</h2>'
assert s.count(marker)==1
p.write_text(s.replace(marker,'<!-- FEDERATION_CHECK_START --><p><a href="协会一手逐项交叉核验.html">查七项运动的 59 项协会核验结果</a></p><!-- FEDERATION_CHECK_END -->'+marker),encoding='utf-8')
print(counts)
