from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / '项目工作区'
TASK = ROOT / '交付文件' / '任务一_数据体检'
SOURCE = WORK / 'outputs' / 'paris2024_medallists_official_open_data.csv'
DATA_OUT = TASK / '02_交付数据'
CHECK_OUT = TASK / '04_质量检查结果'
DATA_OUT.mkdir(parents=True, exist_ok=True)
CHECK_OUT.mkdir(parents=True, exist_ok=True)

source_url = (
    'https://data.smartidf.services/api/explore/v2.1/catalog/datasets/'
    'paris-2024-resultats-des-medailles-pour-chaque-discipline-olympique/exports/csv'
    '?lang=fr&timezone=Europe%2FParis&use_labels=true&delimiter=%3B'
)
raw = pd.read_csv(SOURCE, sep=';', encoding='utf-8-sig')
required = {'Medal_type','Medal_code','Name','Gender','Discipline','Code_Discipline','Event','url_event','Country_code','Country'}
assert required.issubset(raw.columns), sorted(required - set(raw.columns))
event_key = ['Code_Discipline', 'Event']
assert raw[event_key].drop_duplicates().shape[0] == 329
assert raw.loc[raw.Medal_code.eq(1), event_key].drop_duplicates().shape[0] == 329
assert raw.duplicated().sum() == 0

def joined(frame, column):
    return ' | '.join(dict.fromkeys(frame[column].astype(str)))

canonical_fallbacks = {
 ('ATH', "Women's Heptathlon"):'https://olympics.com/en/paris-2024/results/athletics/women-s-heptathlon',
 ('GRY', 'Group All-Around'):'https://olympics.com/en/paris-2024/results/rhythmic-gymnastics/group-all-around',
 ('GRY', 'Individual All-Around'):'https://olympics.com/en/paris-2024/results/rhythmic-gymnastics/individual-all-around',
}

records = []
for (code, event), group in raw.groupby(event_key, sort=True):
    row = {'event_id':f'{code}::{event}','discipline_code':code,'discipline':group.Discipline.iloc[0],
           'event':event,'gender':joined(group,'Gender')}
    for medal_code, prefix in [(1,'gold'),(2,'silver'),(3,'bronze')]:
        medal = group[group.Medal_code.eq(medal_code)]
        row[f'{prefix}_name'] = joined(medal,'Name')
        row[f'{prefix}_country_code'] = joined(medal,'Country_code')
        row[f'{prefix}_country'] = joined(medal,'Country')
    urls = group.url_event.dropna().astype(str)
    row['official_result_url'] = urls.iloc[0] if len(urls) else canonical_fallbacks.get((code,event),'')
    row['url_resolution'] = 'upstream record' if len(urls) else 'constructed from Olympics.com canonical event path'
    row['source_tier'] = '政府开放数据；事件链接指向Olympics.com官方结果页'
    records.append(row)

events = pd.DataFrame(records)
assert len(events) == 329
events.to_csv(DATA_OUT/'2024官方329小项奖牌表.csv',index=False,encoding='utf-8-sig')
raw.to_csv(DATA_OUT/'2024逐项获奖开放数据_原始快照.csv.gz',index=False,compression='gzip',encoding='utf-8-sig')
unit_counts=(raw.groupby(['Country_code','Medal_code']).size().unstack(fill_value=0)
             .rename(columns={1:'gold',2:'silver',3:'bronze'}).reset_index())
published=pd.read_csv(CHECK_OUT/'2024双口径敏感性.csv')
comparison=published[['NOC','gold','silver','bronze']].merge(unit_counts,left_on='NOC',right_on='Country_code',suffixes=('_published','_event'))
mismatch=0
for medal in ['gold','silver','bronze']:
    mismatch += int(comparison[f'{medal}_published'].ne(comparison[f'{medal}_event']).sum())
assert len(comparison)==len(published) and mismatch==0
summary = {
 'retrieved_at_utc':datetime.now(timezone.utc).isoformat(),'source_url':source_url,
 'publisher':'Île-de-France Smart Services（法兰西岛大区开放数据平台）',
 'ioc_structure_source':'https://www.olympics.com/ioc/news/paris-2024-record-breaking-olympic-games-on-and-off-the-field',
 'raw_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'raw_rows':int(len(raw)),
 'distinct_events':int(len(events)),'gold_units':int(raw.Medal_code.eq(1).sum()),
 'silver_units':int(raw.Medal_code.eq(2).sum()),'bronze_units':int(raw.Medal_code.eq(3).sum()),
 'distinct_medal_countries':int(raw.Country_code.nunique()),
 'missing_official_result_url_rows':int(raw.url_event.isna().sum()),
 'event_rows_with_official_url':int(events.official_result_url.ne('').sum()),
 'constructed_canonical_event_urls':int(events.url_resolution.str.startswith('constructed').sum()),
 'published_top15_crosscheck_rows':int(len(comparison)),'published_top15_crosscheck_mismatches':mismatch,
 'checks':{'329_event_keys':True,'329_gold_units':True,'no_exact_duplicates':True,'top15_medal_totals_match':True}}
(CHECK_OUT/'2024官方小项接入审计.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False,indent=2))
