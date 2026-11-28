"""Rebuild the offline task-one rule lab from delivered audit data."""
from pathlib import Path
import json
import re

import pandas as pd
from task1_localization import SPORT_DISPLAY
from task2_localization import NOC_ZH

TASK = Path(__file__).resolve().parents[2] / '交付文件/任务一_数据体检'
DATA = TASK / '02_交付数据'
RESULTS = TASK / '04_质量检查结果'


EVENT_TERMS = {
    'All-Around': '全能', 'Individual': '个人', 'Team': '团体', 'Singles': '单打', 'Doubles': '双打',
    'Greek Style': '希腊式', 'Freestyle': '自由式', 'Hurdles': '栏', 'Walk': '竞走',
    'Discus Throw': '掷铁饼', 'High Jump': '跳高', 'Javelin Throw': '掷标枪', 'Long Jump': '跳远',
    'Marathon': '马拉松', 'Pentathlon (Ancient)': '古式五项', 'Pole Vault': '撑杆跳高',
    'Shot Put': '推铅球', 'Standing': '站姿', 'Stone Throw': '掷石', 'Triple Jump': '三级跳远',
    'Time Trial': '计时赛', 'Road Race': '公路赛', 'Tandem Sprint': '双人自行车争先赛', 'Sprint': '争先赛',
    'Platform': '跳台', 'Foil': '花剑', 'Sabre': '佩剑', 'epee': '重剑', 'Three Hits': '三剑制',
    'Masters': '大师组', 'Swedish System': '瑞典式', '5 Events': '五项', 'Rope Climbing': '爬绳',
    'Naval Rowing Boats': '海军划艇', '17-Man': '17人', '6-Man': '6人', 'Coxed Fours': '四人单桨有舵手',
    'Coxed Pairs': '双人单桨有舵手', 'Single Sculls': '单人双桨', 'Au Commandement': '听令射击',
    'Au Vise': '瞄准射击', 'Dueling Pistol': '决斗手枪', 'Free Pistol': '自由手枪', 'Free Rifle': '自由步枪',
    'Military Revolver': '军用左轮手枪', 'Military Rifle': '军用步枪', 'Gras Model': '格拉斯型',
    'Any Position': '任意姿势', 'Three Positions': '三种姿势', 'Kneeling Or Standing': '跪姿或站姿',
    'Small-Bore Rifle': '小口径步枪', 'Disappearing Target': '隐现靶', 'Prone': '卧姿',
    'Trap': '多向飞碟', 'Double Shot': '双发', 'Single Shot': '单发', 'Relay': '接力',
    'Unlimited': '不限体重', 'One Hand': '单手', 'Two Hands': '双手', 'Greco-Roman': '古典式',
    'Heavyweight': '重量级', 'Lightweight': '轻量级', 'Middleweight': '中量级',
    'Relay Only Athlete': '仅参加接力的运动员', 'Men': '男子', 'Women': '女子', 'Mixed': '混合',
    "Men's": '男子', "Women's": '女子', 'kilometres': '公里', 'metres': '米', 'One Mile': '1英里',
    'mile': '英里', 'yards': '码', 'Ton': '吨', 'and': '和',
}


def display_events(values):
    terms = {**SPORT_DISPLAY, **EVENT_TERMS}
    pattern = re.compile(r"(?<![A-Za-z])(?:" + "|".join(map(re.escape, sorted(terms, key=len, reverse=True))) + r")(?![A-Za-z])")
    result = {value: pattern.sub(lambda match: terms[match[0]], value).replace(' x ', '×').replace(', ', '，')
              for value in values}
    assert not [value for value, translation in result.items() if re.search('[A-Za-z]', translation)]
    return result


def build_payload(data_path, results):
    data = pd.read_csv(data_path, keep_default_na=False)
    keys = [column for column in data.columns[1:12] if column != 'player_id']
    candidates = data.loc[data.duplicate_candidate].copy()
    candidates['kept'] = candidates.groupby(keys, dropna=False).source_row.transform('min')
    removed = candidates[candidates.include_main & candidates.duplicate_excess & candidates.is_medal]
    output = {}
    for key, file in [('main', 'main'), ('dedup', 'exclude_duplicate_excess'), ('inclusive', 'include_1906')]:
        output[key] = pd.read_csv(results / f'edition_{file}.csv')[['Year','medal_rows']].values.tolist()
    output['excess'] = {str(year): group[['source_row','kept','NOC','Event','Medal']].values.tolist()
                        for year, group in removed.groupby('Year')}
    raw = data.set_index('source_row')
    pairs = {}
    for row in removed[removed.Year.eq(1900)].itertuples():
        kept = raw.loc[row.kept]
        dropped = raw.loc[row.source_row]
        assert kept[keys].equals(dropped[keys])
        pairs[str(row.source_row)] = [str(kept.player_id), str(dropped.player_id),
                                      *[[key, str(kept[key])] for key in keys]]
    output['pairs1900'] = pairs
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
    output['names'] = NOC_ZH
    output['sports'] = SPORT_DISPLAY
    output['eventLabels'] = display_events(
        {row[3] for rows in output['excess'].values() for row in rows}
        | {row[2] for row in output['medals1906']}
        | {row[2] for result in output['events'].values() for row in result['examples']}
    )
    return output


def publish():
    output = build_payload(DATA / '归一数据_保留原始字段.csv.gz', RESULTS)
    (TASK / '规则实验台数据.js').write_text('window.auditLabData = '+json.dumps(output,ensure_ascii=False)+';\n',encoding='utf8')
    page = TASK / 'index.html'
    html = page.read_bytes()
    html = re.sub(rb'<!-- AUDIT_LAB_(?:ENTRY|VIEW) -->.*?<!-- /AUDIT_LAB -->',b'',html,flags=re.S)
    entry = '<!-- AUDIT_LAB_ENTRY --><p><a href="#audit-lab">打开数据规则实验台 ↓</a> · <a href="?review=1900#audit-rows">一键复核 1900 年 ↓</a></p><!-- /AUDIT_LAB -->'
    view = ('<!-- AUDIT_LAB_VIEW --><section id="audit-lab" aria-label="数据规则实验台"></section>'
            '<link rel="stylesheet" href="规则实验台.css"><script defer src="规则实验台数据.js"></script>'
            '<script defer src="规则实验台.js"></script><!-- /AUDIT_LAB -->')
    html = html.replace(b'<main class="xz-container">', b'<main class="xz-container">'+entry.encode(),1)
    page.write_bytes(html.replace(b'</main>',view.encode()+b'</main>',1))


if __name__ == '__main__':
    publish()
