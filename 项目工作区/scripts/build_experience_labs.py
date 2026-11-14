"""Build two offline exhibits from the existing audited competition tables."""
from pathlib import Path
from collections import defaultdict
import csv, gzip, json
from task2_localization import NOC_ZH, SPORT_ZH

ROOT = Path(__file__).resolve().parents[2]
DELIVERY = ROOT / '交付文件'
TWO = DELIVERY / '任务二_百年全景'
FOUR = DELIVERY / '任务四_开放创作'

def read(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

def write(folder, payload):
    folder.mkdir(parents=True, exist_ok=True)
    raw = json.dumps(payload, ensure_ascii=False, separators=(',', ':'))
    (folder / 'data.json').write_text(raw, encoding='utf-8')
    template = (folder / 'screen.template.html').read_text(encoding='utf-8')
    (folder / 'index.html').write_text(template.replace('__DATA__', raw), encoding='utf-8')

years = [int(x['Year']) for x in read(TWO/'02_数据表/A_逐届规模与集中度.csv')]
assert len(years) == 30 and years[0] == 1896 and years[-1] == 2024
counts = defaultdict(lambda: defaultdict(int))
with gzip.open(DELIVERY/'任务一_数据体检/02_交付数据/归一数据_保留原始字段.csv.gz', 'rt', encoding='utf-8-sig', newline='') as f:
    for row in csv.DictReader(f):
        year = int(row['Year']) if row['Year'].isdigit() else 0
        sport = row['sport_family'].strip()
        if year in years and sport:
            counts[sport][year] += 1
sports = []
for sport, by_year in counts.items():
    presence = [by_year[y] > 0 for y in years]
    if not any(presence):
        continue
    sports.append({'key': sport, 'name': SPORT_ZH.get(sport, sport),
                   'counts': [by_year[y] for y in years], 'presence': presence})
sports.sort(key=lambda s: (-sum(s['presence']), s['name']))
write(TWO/'10_百年项目星系', {'years': years, 'sports': sports,
      'scope': '赛题归一数据的夏奥届次；出现按 sport_family 有参赛记录判定，数量为运动员记录行，不是官方小项数。'})

base = read(FOUR/'05_满分升级/11_官方来源门控预测/LA2028审慎来源门控预测榜.csv')
ablation = read(FOUR/'05_满分升级/07_模型消融与资格情景/逐代表团消融情景.csv')
by_noc = defaultdict(dict)
for row in ablation:
    by_noc[row['NOC']][row['情景']] = float(row['预测奖牌'])
teams = []
for row in base:
    noc = row['NOC']
    scenarios = by_noc[noc]
    if not scenarios:
        continue
    teams.append({'noc': noc, 'name': NOC_ZH.get(noc, noc),
                  'point': float(row['审慎集成预测']),
                  'full': scenarios['完整集成'],
                  'noHost': scenarios['关闭主场调整'],
                  'noNew': scenarios['关闭新增运动排名'],
                  'limited': scenarios['资格受限：RUS/AIN不参赛'],
                  'lowerRef': float(row['lower80']),
                  'upperRef': float(row['upper80']),
                  'rank': int(row['审慎集成名次'])})
backtest = read(FOUR/'05_满分升级/滚动留出同口径比较.csv')
write(FOUR/'09_预测风暴实验室', {'teams': teams,
      'backtest': [{'year': int(r['Year']), 'model': r['model'],
                    'mae': float(r['MAE_all']), 'rmse': float(r['RMSE_all']),
                    'top10': int(r['top10_overlap'])} for r in backtest],
      'scope': '情景变化按已保存的逐队消融结果做线性插值；不是重新训练、资格模拟或校准后的联合概率模型。原 lower80/upper80 来自另一统计基线，只能作为宽度参照。'})
print(f'Built {len(sports)} sports across {len(years)} editions; {len(teams)} forecast delegations.')
