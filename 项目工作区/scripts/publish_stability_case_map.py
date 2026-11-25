"""Add the geographic index using the existing theatre geography and host data."""
import csv
from collections import defaultdict
from html import escape
import json
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[2]
DELIVERY = ROOT / '交付文件'
PAGE = DELIVERY / '任务三_专题深挖/11_结论稳定性地图/index.html'


def publish():
    theatre = DELIVERY / '任务四_开放创作/08_奥运时空剧场/src/data.json'
    data = json.loads(theatre.read_text(encoding='utf-8'))
    source = DELIVERY / '任务二_百年全景/02_数据表/B_主场事件窗口.csv'
    with source.open(encoding='utf-8-sig', newline='') as file:
        shares = {(int(r['host_year']), int(r['k'])): float(r['host_share'])
                  for r in csv.DictReader(file) if r['host_share']}
    cities = defaultdict(list)
    for edition in data['editions']:
        year = edition['year']
        if (year, 0) in shares:
            cities[edition['city'], edition['lon'], edition['lat']].append(year)

    def point(lon, lat):
        return (lon + 180) * 2.5, (85 - lat) * 2.5

    land = []
    for ring in data['geography']:
        if max(p[1] for p in ring) < -60:
            continue
        coords = ' '.join(f'{x:.1f},{y:.1f}' for x, y in (point(*p) for p in ring))
        land.append(f'<polygon points="{coords}"/>')
    pins, cards = [], []
    for i, ((city, lon, lat), years) in enumerate(cities.items(), 1):
        label = escape(city)
        target = f'host-map-case-{i}'
        x, y = point(lon, lat)
        pins.append(f'<a href="#{target}" aria-label="{label}"><title>{label}</title>'
                    f'<circle cx="{x:.1f}" cy="{y:.1f}" r="10"/>'
                    f'<text x="{x:.1f}" y="{y:.1f}">{i}</text></a>')
        detail = []
        for year in years:
            before, host = shares[year, -1], shares[year, 0]
            detail.append(f'<li>{year} 年：{before:.2f}% → {host:.2f}%（{host-before:+.2f} 个百分点）</li>')
        cards.append(f'<article id="{target}" tabindex="-1"><h4>{i} · {label}</h4><ul>{"".join(detail)}</ul>'
                     '<a href="../S1_东道主效应/index.html">查看主场效应核验 ↗</a></article>')

    section = f'''<section id="stability-case-map" aria-labelledby="stability-case-map-title">
<style>
#stability-case-map{{margin:30px 0 40px;padding-block:22px;border-block:1px solid currentColor}}
#stability-case-map h2,#stability-case-map h4{{margin:0 0 10px}}
#stability-case-map svg{{display:block;width:100%;height:auto;background:#132a35;border-radius:10px}}
#stability-case-map polygon{{fill:#44636d;stroke:#587782;stroke-width:.4}}
#stability-case-map circle{{fill:#f1cc89;stroke:#182e39;stroke-width:2}}
#stability-case-map text{{fill:#142630;text-anchor:middle;dominant-baseline:central;font:bold 10px system-ui;pointer-events:none}}
#stability-case-map svg a:is(:hover,:focus) circle{{fill:white;stroke:#121e25;stroke-width:3}}
#stability-case-map .host-map-cases{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,230px),1fr));gap:12px;margin-top:16px}}
#stability-case-map article{{padding:12px;border-top:1px solid currentColor;scroll-margin-top:95px}}
#stability-case-map article:target{{outline:2px solid #c69b56;outline-offset:-2px}}
#stability-case-map article ul{{margin:0 0 6px;padding-left:1.1em}}
#stability-case-map article a{{text-decoration:underline}}
</style>
<h2 id="stability-case-map-title">主场效应案例地图</h2>
<p>点击编号查看对应主办城市。{sum(map(len,cities.values()))} 届案例按举办地定位，东京两届共用一处标记。</p>
<svg viewBox="0 0 900 365" aria-label="主场效应案例世界地图">
<g aria-hidden="true">{''.join(land)}</g>{''.join(pins)}</svg>
<p>数值为前一届到主办届的获奖记录份额变化，单位为百分比与百分点。地图仅定位案例，差值不能单独证明主场的因果作用。底图使用项目既有 Natural Earth 110m 数据。</p>
<div class="host-map-cases">{''.join(cards)}</div></section>'''
    soup = BeautifulSoup(PAGE.read_text(encoding='utf-8'), 'html.parser')
    prior = soup.select_one('#stability-case-map')
    if prior:
        prior.decompose()
    soup.select_one('.stability-list').insert_before(BeautifulSoup(section, 'html.parser'))
    PAGE.write_text(str(soup), encoding='utf-8')


if __name__ == '__main__':
    publish()
