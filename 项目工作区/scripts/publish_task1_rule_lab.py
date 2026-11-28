"""Rebuild the offline task-one rule lab from delivered audit data."""
from pathlib import Path
import json
import re

import pandas as pd

TASK = Path(__file__).resolve().parents[2] / '交付文件/任务一_数据体检'
DATA = TASK / '02_交付数据'
RESULTS = TASK / '04_质量检查结果'


def publish():
    data = pd.read_csv(DATA / '归一数据_保留原始字段.csv.gz', keep_default_na=False)
    keys = [column for column in data.columns[1:12] if column != 'player_id']
    candidates = data.loc[data.duplicate_candidate].copy()
    candidates['kept'] = candidates.groupby(keys, dropna=False).source_row.transform('min')
    removed = candidates[candidates.include_main & candidates.duplicate_excess & candidates.is_medal]
    output = {}
    for key, file in [('main', 'main'), ('dedup', 'exclude_duplicate_excess'), ('inclusive', 'include_1906')]:
        output[key] = pd.read_csv(RESULTS / f'edition_{file}.csv')[['Year','medal_rows']].values.tolist()
    output['excess'] = {str(year): group[['source_row','kept','NOC','Event','Medal']].values.tolist()
                        for year, group in removed.groupby('Year')}
    dedup = dict(output['dedup'])
    assert all(count-dedup[year] == len(output['excess'].get(str(year), []))
               for year,count in output['main'])
    output['medals1906'] = data.loc[data.Year.eq(1906) & data.is_medal, ['source_row','NOC','Event','Medal']].values.tolist()
    assert len(output['medals1906']) == dict(output['inclusive'])[1906]
    output['events'] = {}
    for year in (2020,2024):
        affected = data[data.Year.eq(year) & data.event_status.eq('generic_or_context_required')]
        examples = affected.drop_duplicates(['Sport','Event']).head(16)
        output['events'][year] = {'count':len(affected), 'examples':examples[['source_row','Sport','Event','Sex','sport_family']].values.tolist()}
    output['official'] = len(pd.read_csv(DATA / '2024官方329小项奖牌表.csv'))
    (TASK / '规则实验台数据.js').write_text('window.auditLabData = '+json.dumps(output,ensure_ascii=False)+';\n',encoding='utf8')
    page = TASK / 'index.html'
    html = page.read_bytes()
    html = re.sub(rb'<!-- AUDIT_LAB_(?:ENTRY|VIEW) -->.*?<!-- /AUDIT_LAB -->',b'',html,flags=re.S)
    entry = '<!-- AUDIT_LAB_ENTRY --><p><a href="#audit-lab">打开数据规则实验台 ↓</a></p><!-- /AUDIT_LAB -->'
    view = ('<!-- AUDIT_LAB_VIEW --><section id="audit-lab" aria-label="数据规则实验台"></section>'
            '<link rel="stylesheet" href="规则实验台.css"><script defer src="规则实验台数据.js"></script>'
            '<script defer src="规则实验台.js"></script><!-- /AUDIT_LAB -->')
    html = html.replace(b'<main class="xz-container">', b'<main class="xz-container">'+entry.encode(),1)
    page.write_bytes(html.replace(b'</main>',view.encode()+b'</main>',1))


if __name__ == '__main__':
    publish()
