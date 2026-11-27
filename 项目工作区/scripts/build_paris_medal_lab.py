"""Build offline evidence for the Paris medal recalculation lab."""
import json
import re
from pathlib import Path

import pandas as pd

from s2_sport_family import family

ROOT = Path(__file__).resolve().parents[2]
DELIVERY = ROOT / '交付文件'
DATA = DELIVERY / '任务一_数据体检/02_交付数据'
LAB = DELIVERY / '任务三_专题深挖/S2_口径的魔力/09_奖牌口径实验室'
official = pd.read_csv(DATA / '2024官方329小项奖牌表.csv').fillna('')
records = []
for row in official.itertuples(index=False):
    for color, column in enumerate(('gold_country_code', 'silver_country_code', 'bronze_country_code')):
        for code in getattr(row, column).split('|'):
            code = code.strip()
            if code and code != 'AIN':
                records.append([0, code, family(row.discipline), color, row.event, 1, row.official_result_url])
# Group raw labels within the same sport, delegation and medal color.
# Raw Event labels are preserved and do not imply a match to an official event.
raw = pd.read_csv(DATA / '归一数据_保留原始字段.csv.gz',
                  usecols=['Year', 'include_main', 'is_medal', 'NOC', 'sport_family', 'Event', 'Medal'])
raw = raw[raw.Year.eq(2024) & raw.include_main & raw.is_medal & raw.NOC.ne('AIN')]
for (code, sport, event, medal), count in raw.fillna({'Event': '无小项标签'}).groupby(
        ['NOC', 'sport_family', 'Event', 'Medal']).size().items():
    records.append([1, code, sport, ('Gold', 'Silver', 'Bronze').index(medal), event, int(count), ''])
assert {r[2] for r in records if r[0] == 0} == {r[2] for r in records if r[0] == 1}
names = dict(re.findall(r'^([A-Z]{3})=([^\r\n]+)',
                        Path(__file__).with_name('task2_localization.py').read_text(encoding='utf8'), re.M))
payload = json.dumps({'records': records, 'names': names}, ensure_ascii=False, allow_nan=False)
(LAB / 'paris-evidence.js').write_text('window.parisEvidence = ' + payload + ';\n', encoding='utf8')
