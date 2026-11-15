"""Rebuild the judge-facing evidence figure and a narrow historical sensitivity check."""
from __future__ import annotations

import csv
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / '交付文件/任务三_专题深挖/S2_口径的魔力'
SOURCE = BASE / '08_逐项外部核验/Olympedia独立交叉核验/历史555项独立交叉对照.csv'
RANKS = BASE / '02_数据表/S2_跨届双口径排名.csv'
PARIS = ROOT / '交付文件/任务一_数据体检/02_交付数据/2024官方329小项奖牌表.csv'
PARIS_RANKS = BASE / '02_数据表/S2_2024三口径完整排名.csv'
OUT = ROOT / '交付文件/最终提交材料/证据等级与历史反例'
OUT.mkdir(parents=True, exist_ok=True)

with SOURCE.open(encoding='utf-8-sig', newline='') as handle:
    checks = list(csv.DictReader(handle))
assert len(checks) == 555
different = [r for r in checks if r['archive_three_match'].strip().lower() != 'true']
assert len(different) == 7
assert sum(r['archive_three_match'].strip().lower() == 'true' for r in checks) == 548
assert {int(r['Year']) for r in checks} == {2008, 2012, 2016}
with PARIS.open(encoding='utf-8-sig', newline='') as handle:
    assert sum(1 for _ in csv.DictReader(handle)) == 329
with PARIS_RANKS.open(encoding='utf-8-sig', newline='') as handle:
    spanish = {r['lens']: int(r['rank']) for r in csv.DictReader(handle) if r['NOC'] == 'ESP'}
assert spanish['official'] == 15 and spanish['rows'] == 5

frame = pd.read_csv(RANKS)

def ranks(rows: pd.DataFrame) -> pd.Series:
    ordered = rows.sort_values(['Gold_event', 'Silver_event', 'Bronze_event'], ascending=False)
    triples = list(zip(ordered.Gold_event, ordered.Silver_event, ordered.Bronze_event))
    first = {}
    for index, triple in enumerate(triples, 1):
        first.setdefault(triple, index)
    return pd.Series([first[t] for t in triples], index=ordered.NOC, dtype=int)

results = []
for year in (2008, 2012):
    original = frame[frame.Year == year].copy().set_index('NOC')
    assert ranks(original.reset_index()).reindex(original.index).equals(original.event_rank.astype(int))
    changed = original.copy()
    if year == 2008:
        # Women's modern pentathlon: the later medal presentation moved bronze.
        changed.loc['UKR', 'Bronze_event'] -= 1
        changed.loc['BLR', 'Bronze_event'] += 1
    else:
        # IOC London 2012 C1 200 m reallocation: LTU silver -> RUS; RUS bronze -> ESP.
        changed.loc['LTU', 'Silver_event'] -= 1
        changed.loc['RUS', 'Silver_event'] += 1
        changed.loc['RUS', 'Bronze_event'] -= 1
        changed.loc['ESP', 'Bronze_event'] += 1
    assert (changed[['Gold_event', 'Silver_event', 'Bronze_event']] >= 0).all().all()
    new_rank = ranks(changed.reset_index()).reindex(original.index)
    altered = original.event_rank.astype(int) != new_rank
    results.append({
        'year': year,
        'scenario': '女子现代五项铜牌转授' if year == 2008 else '男子 C1 200 米银铜重分配',
        'changed_delegations': int(altered.sum()),
        'changed_rank_rows': [
            {'NOC': noc, 'before': int(original.loc[noc, 'event_rank']), 'after': int(new_rank.loc[noc])}
            for noc in original.index[altered]
        ],
        'mean_absolute_rank_shift_before': round(float((original.event_rank - original.row_rank).abs().mean()), 4),
        'mean_absolute_rank_shift_after': round(float((new_rank - original.row_rank).abs().mean()), 4),
        'top_ten_set_unchanged': set(original.nsmallest(10, 'event_rank').index) == set(new_rank.nsmallest(10).index),
    })
assert results[0]['changed_delegations'] == 0
assert results[1]['changed_rank_rows'] == [
    {'NOC': 'LTU', 'before': 34, 'after': 35},
    {'NOC': 'NOR', 'before': 35, 'after': 34},
]

summary = {
    'historic_compared': 555, 'three_color_agreement': 548, 'differences': 7,
    'difference_types': {'archive_missing_one_color': 4, 'documented_later_change': 2, 'revoked_bronze_successor_unconfirmed': 1},
    'rank_sensitivity': results,
    'scope_note': 'Only two documented later-change events were perturbed; this is not an all-910-item current IOC re-ranking.',
}
(OUT / '证据等级与历史反例_复算结果.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
ink, muted, teal, blue, amber, red = '#17333a', '#5b6c70', '#176f77', '#345f9b', '#bb7738', '#a8424f'
paper, line = '#f7f5ef', '#d8ded9'
fig = plt.figure(figsize=(14, 8), facecolor=paper)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 1400); ax.set_ylim(0, 800); ax.axis('off')

def text(x, y, value, size=14, color=ink, weight='normal', va='top'):
    ax.text(x, y, value, fontsize=size, color=color, fontweight=weight, va=va, ha='left')

def box(x, y, w, h, fill='#ffffff', stroke=line, radius=18):
    ax.add_patch(FancyBboxPatch((x,y), w,h, boxstyle=f'round,pad=0,rounding_size={radius}', linewidth=1.2, edgecolor=stroke, facecolor=fill))

text(64, 744, '证据等级决定结论能说到哪里', 29, ink, 'bold')
text(65, 696, '主判断立于巴黎 2024；历史三届用于检验机制与寻找反例。', 15, muted)
ax.plot([64, 1336], [664, 664], color=line, lw=1.4)

box(64, 396, 382, 235, '#e8f1ef', '#b8d1cb')
text(88, 608, '主证据  /  巴黎 2024', 15, teal, 'bold')
text(86, 567, '329', 52, ink, 'bold')
text(225, 545, '个逐项结果', 17, ink)
text(88, 493, '西班牙金牌榜：15 → 5', 21, ink, 'bold')
text(88, 452, '统计单位变了；排序规则未变。', 14, muted)
text(88, 418, '外部逐项表＋IOC总数核对；3条构造链接已标记。', 10.8, muted)

box(468, 396, 410, 235, '#f9faf8', line)
text(491, 608, '交叉验证  /  2008 · 2012 · 2016', 15, blue, 'bold')
text(490, 567, '555', 52, ink, 'bold')
text(626, 545, '项独立二次对照', 17, ink)
text(491, 493, '548项三色一致  ·  7项有差异', 18, ink, 'bold')
text(491, 450, '原数据小项代理与 Olympedia 公开表', 14, muted)
text(491, 418, '一致不等于现行IOC逐项授牌认证。', 12, red, 'bold')

box(900, 396, 436, 235, '#fbf1e9', '#e2cbb7')
text(923, 608, '差异裁定  /  7 项逐条追溯', 15, amber, 'bold')
for y, num, label, color in [(548, '4', '旧存档缺失一色；赛时册补证', teal), (500, '2', '事后奖牌变化；保留两版', amber), (452, '1', '旧铜撤销；继任授牌待证', red)]:
    text(925, y, num, 28, color, 'bold')
    text(972, y-2, label, 14, ink)

text(66, 348, '已知后续变动会推翻“跨届口径重排”吗？', 20, ink, 'bold')
ax.add_patch(Rectangle((66, 247), 1268, 75, facecolor='#e7e9e6', edgecolor='none'))
ax.add_patch(Rectangle((66, 247), 960, 75, facecolor='#d7e8e5', edgecolor='none'))
text(86, 302, '2008 现代五项', 14, muted, 'bold')
text(86, 273, '0 个代表团名次变化', 18, teal, 'bold')
text(484, 302, '2012 皮划艇 C1 200米', 14, muted, 'bold')
text(484, 273, '2 个代表团各变 1 位', 18, teal, 'bold')
text(1045, 300, '两届前十集合', 14, muted, 'bold')
text(1045, 273, '均不变', 18, ink, 'bold')

text(67, 207, '解释边界', 14, red, 'bold')
text(67, 177, '上述敏感性只改动两项有后续变化证据的奖牌；未把其余 908 项改写成“现行 IOC 榜”。', 13, ink)
text(67, 148, '2012 举重69公斤级仅确认原铜撤销，继任铜牌未见 IOC 逐项决定，故不纳入确定性转授。', 13, ink)
ax.plot([64, 1336], [106, 106], color=line, lw=1.2)
text(65, 82, '来源：2024逐项结果层；赛题运动员记录；Olympedia 97份逐运动表；2008赛时册、IOC与单项协会后续裁决。', 10.5, muted)
text(65, 59, '统计单位：小项 / 运动员行；历史555项为代理交叉验证。详见本图复算结果与逐项差异报告。', 10.5, muted)

fig.savefig(OUT / '证据等级图.png', dpi=200, facecolor=paper, bbox_inches='tight', pad_inches=0)
fig.savefig(OUT / '证据等级图.svg', facecolor=paper, bbox_inches='tight', pad_inches=0)
plt.close(fig)
print(OUT)
