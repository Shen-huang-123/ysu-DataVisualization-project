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
        # Unwrap at the antimeridian and let the viewport clip repeated copies.
        unwrapped = [ring[0]]
        for lon, lat in ring[1:]:
            previous = unwrapped[-1][0]
            lon += 360 * round((previous - lon) / 360)
            unwrapped.append((lon, lat))
        for offset in (-360, 0, 360):
            if max(lon for lon, _ in unwrapped) + offset < -180 or min(lon for lon, _ in unwrapped) + offset > 180:
                continue
            coords = ' '.join(f'{x:.1f},{y:.1f}' for x, y in
                              (point(lon + offset, lat) for lon, lat in unwrapped))
            land.append(f'<polygon points="{coords}"/>')
    pins, cards, links = [], [], []
    for i, ((city, lon, lat), years) in enumerate(cities.items(), 1):
        label = escape(city)
        target = f'host-map-case-{i}'
        links.append(f'<a href="#{target}">{i} · {label}</a>')
        x, y = point(lon, lat)
        dx, dy = {'伦敦': (-42, -20), '巴黎': (38, -13), '巴塞罗那': (-23, 28)}.get(city, (0, 0))
        leader = (f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x+dx:.1f}" y2="{y+dy:.1f}"/>'
                  f'<circle class="host-location" cx="{x:.1f}" cy="{y:.1f}" r="2"/>' if dx or dy else '')
        pins.append(f'<a href="#{target}" aria-label="{label}"><title>{label}</title>{leader}'
                    f'<circle class="host-pin" cx="{x+dx:.1f}" cy="{y+dy:.1f}" r="10"/>'
                    f'<text x="{x+dx:.1f}" y="{y+dy:.1f}">{i}</text></a>')
        detail = []
        for year in years:
            before, host = shares[year, -1], shares[year, 0]
            detail.append(f'<li><span>{year} 年</span><strong>{host-before:+.2f} 个百分点</strong>'
                          f'<small>{before:.2f}% → {host:.2f}%</small></li>')
        cards.append(f'<article id="{target}" tabindex="-1"><h4>{i} · {label}</h4><ul>{"".join(detail)}</ul>'
                     '</article>')

    section = f'''<section id="stability-case-map" aria-labelledby="stability-case-map-title">
<style>
#stability-case-map{{margin:30px 0 40px;padding-block:22px;border-block:1px solid color-mix(in srgb,currentColor 22%,transparent);scroll-margin-top:100px}}
#stability-case-map h2,#stability-case-map h4{{margin:0 0 10px}}
#stability-case-map svg{{display:block;width:100%;height:auto;background:#132a35;border-radius:10px}}
#stability-case-map polygon{{fill:#44636d;stroke:#587782;stroke-width:.4}}
#stability-case-map circle{{fill:#f1cc89}}
#stability-case-map .host-pin{{stroke:#182e39;stroke-width:2}}
#stability-case-map line{{stroke:#f1cc89;stroke-width:1;pointer-events:none}}
#stability-case-map text{{fill:#142630;text-anchor:middle;dominant-baseline:central;font:bold 10px system-ui;pointer-events:none}}
#stability-case-map svg a:is(:hover,:focus) circle{{fill:white;stroke:#121e25;stroke-width:3}}
#stability-case-map .host-map-layout{{display:grid;grid-template-columns:minmax(0,1fr) minmax(224px,24%);gap:clamp(16px,2vw,32px);align-items:start}}
#stability-case-map .host-map-links{{display:flex;flex-wrap:wrap;gap:6px;margin-top:12px}}
#stability-case-map .host-map-links a{{padding:5px 10px;border:1px solid color-mix(in srgb,currentColor 30%,transparent);border-radius:4px}}
#stability-case-map aside{{padding:18px;border:1px solid color-mix(in srgb,currentColor 24%,transparent);border-radius:10px}}
#stability-case-map article{{display:none;scroll-margin-top:100px}}
#stability-case-map aside:not(:has(article:target)) article:first-of-type,#stability-case-map article:target{{display:block}}
#stability-case-map article ul{{list-style:none;margin:0 0 14px;padding:0}}
#stability-case-map article li{{display:grid;gap:2px;padding:10px 0;border-bottom:1px solid color-mix(in srgb,currentColor 20%,transparent)}}
#stability-case-map article strong{{font-size:1.15em}}
#stability-case-map aside > a{{text-decoration:underline}}
@media (max-width:720px){{#stability-case-map .host-map-layout{{grid-template-columns:minmax(0,1fr)}}}}
</style>
<h2 id="stability-case-map-title">主场效应案例地图</h2>
<p>选择地图标记或城市名称，查看获奖记录份额变化。{sum(map(len,cities.values()))} 届案例按举办地定位，东京两届共用一处标记。</p>
<div class="host-map-layout"><div><svg viewBox="0 0 900 365" aria-label="主场效应案例世界地图">
<g aria-hidden="true">{''.join(land)}</g>{''.join(pins)}</svg>
<nav class="host-map-links" aria-label="主办城市">{''.join(links)}</nav></div>
<aside aria-label="城市案例">{''.join(cards)}<a href="../S1_东道主效应/index.html">查看主场效应核验 ↗</a></aside></div>
<p>数值为前一届到主办届的获奖记录份额变化，单位为百分比与百分点。地图仅定位案例，差值不能单独证明主场的因果作用。底图使用项目既有 Natural Earth 110m 数据。</p>
</section>'''
    soup = BeautifulSoup(PAGE.read_text(encoding='utf-8'), 'html.parser')
    prior = soup.select_one('#stability-case-map')
    if prior:
        prior.decompose()
    soup.select_one('.stability-list').insert_before(BeautifulSoup(section, 'html.parser'))
    PAGE.write_text(str(soup), encoding='utf-8')


if __name__ == '__main__':
    publish()
