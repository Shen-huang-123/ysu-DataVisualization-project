"""Package audited CSV summaries as local JSON for the offline ECharts screen."""
from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / '交付文件/任务四_开放创作/07_ECharts大屏/data.json'

def rows(path):
    with (ROOT / path).open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

scale = rows('交付文件/任务二_百年全景/02_数据表/A_逐届规模与集中度.csv')
female = rows('交付文件/任务二_百年全景/02_数据表/C_女性参与获奖与小项.csv')
flow = rows('交付文件/任务二_百年全景/02_数据表/D_项目新增退出重返.csv')
rank = rows('交付文件/任务三_专题深挖/S2_口径的魔力/99_旧版归档/paris2024_rank_sensitivity.csv')
forecast = rows('交付文件/任务四_开放创作/05_满分升级/11_官方来源门控预测/LA2028审慎来源门控预测榜.csv')

fem = {int(r.get('Year') or r.get('') or 0): r for r in female}
flo = {int(r['Year']): r for r in flow}
history = []
for r in scale:
    y = int(r['Year'])
    fr = fem.get(y, {})
    dr = flo.get(y, {})
    history.append({
        'year': y, 'records': int(r['participation_records']),
        'delegations': int(r['delegations']), 'sports': int(r['sport_families']),
        'top5': round(float(r['top5_share']) * 100, 1),
        'female': round(float(fr.get('participation_share') or 0) * 100, 1),
        'new': int(dr.get('新增') or 0), 'returning': int(dr.get('重返') or 0),
        'retained': int(dr.get('连续保留') or 0),
    })

ranked = []
for r in rank:
    if not r.get('published_rank') or int(r['published_rank']) > 15: continue
    ranked.append({'noc':r['NOC'],'official':int(r['published_rank']),
                   'athlete':int(r['gold_row_rank']), 'gold':int(r['gold']),
                   'athleteGold':int(r['gold_rows'])})

predict = []
for r in forecast:
    if not r.get('rank') or int(r['rank']) > 12: continue
    predict.append({'noc':r['NOC'], 'rank':int(r['rank']),
                    'estimate':round(float(r['forecast_total_programme']),1),
                    'lower':round(float(r['lower80']),1), 'upper':round(float(r['upper80']),1)})

payload = {'history':history,'rank2024':sorted(ranked,key=lambda x:x['official']),
           'forecast2028':sorted(predict,key=lambda x:x['rank']),
           'notes':{'history':'参赛记录为运动员行，非独立人数；女性占比同为运动员行口径。',
                    'rank':'官方小项金牌榜与运动员获金行数排名，统计单位不同。',
                    'forecast':'点与80%区间均来自项目级调整后的统计基线；这是预测区间，不是保证范围。'}}
OUT.write_text(json.dumps(payload,ensure_ascii=False,separators=(',',':')),encoding='utf-8')
template = ROOT / '交付文件/任务四_开放创作/07_ECharts大屏/screen.template.html'
(OUT.parent / 'index.html').write_text(template.read_text(encoding='utf-8').replace('__EMBEDDED_DATA__', json.dumps(payload,ensure_ascii=False,separators=(',',':'))),encoding='utf-8')
print(f'{OUT}: {len(history)} editions, {len(ranked)} rank rows, {len(predict)} forecast rows')
