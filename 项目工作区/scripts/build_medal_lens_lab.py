"""Build an offline 2024 medal-accounting lab from existing audited tables."""
from pathlib import Path
from collections import Counter, defaultdict
import csv, gzip, json
from task2_localization import NOC_ZH, SPORT_ZH

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力'
OUT=BASE/'09_奖牌口径实验室'
OUT.mkdir(exist_ok=True)

def read(path):
    with path.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))

rank=read(BASE/'02_数据表/S2_2024三口径完整排名.csv')
assert len(rank)==273 and {r['lens'] for r in rank}=={'official','fractional','rows'}
records=defaultdict(dict)
for r in rank:
    noc=r['NOC'];records[noc]['noc']=noc;records[noc]['name']=NOC_ZH.get(noc,noc)
    records[noc][r['lens']]={k:float(r[k]) for k in ('Gold','Silver','Bronze')}|{'rank':int(r['rank'])}

gold_rows=defaultdict(Counter)
data=ROOT/'交付文件/任务一_数据体检/02_交付数据/归一数据_保留原始字段.csv.gz'
with gzip.open(data,'rt',encoding='utf-8-sig',newline='') as f:
    for r in csv.DictReader(f):
        if r['Year']=='2024' and r['Medal']=='Gold' and r['NOC'] in records:
            gold_rows[r['NOC']][r['sport_family']]+=1
assert sum(sum(c.values()) for c in gold_rows.values())>700

official=read(ROOT/'交付文件/任务一_数据体检/02_交付数据/2024官方329小项奖牌表.csv')
assert len(official)==329
gold_events=defaultdict(Counter)
for r in official:
    for noc in (r['gold_country_code'] or '').split(' | '):
        if noc in records:gold_events[noc][r['discipline']]+=1

robust=read(BASE/'02_数据表/S2_2024代表团剔除敏感性.csv')
robust_by=defaultdict(list)
for r in robust:
    if r['removed_family']!='none':robust_by[r['NOC']].append(int(r['rank_shift_rows_minus_official']))

cases=[]
for noc,d in records.items():
    sports=[{'name':SPORT_ZH.get(k,k),'rows':v,'key':k} for k,v in gold_rows[noc].most_common()]
    events=[{'name':SPORT_ZH.get(k,k),'events':v,'key':k} for k,v in gold_events[noc].most_common()]
    shifts=robust_by[noc]
    cases.append(d|{'sports':sports,'officialSports':events,'robust':{'min':min(shifts),'max':max(shifts),'n':len(shifts)} if shifts else None})
assert len(cases)==91
payload={'cases':sorted(cases,key=lambda x:x['official']['rank']),'meta':{'year':2024,'officialEvents':329,'athleteMedalRows':2281,'sportRemovalTrials':35,'sourceNote':'官方小项来自2024年329项公开结果整理表；运动员行与组内均分来自赛题归一数据。逐运动剔除结果为35次独立重算。'}}
(OUT/'data.json').write_text(json.dumps(payload,ensure_ascii=False,separators=(',',':')),encoding='utf-8')
template=(OUT/'screen.template.html').read_text(encoding='utf-8')
(OUT/'index.html').write_text(template.replace('__EMBEDDED_DATA__',json.dumps(payload,ensure_ascii=False,separators=(',',':'))),encoding='utf-8')
print(f'Built {len(cases)} delegations; {len(official)} official events; {sum(sum(c.values()) for c in gold_rows.values())} athlete gold rows')
