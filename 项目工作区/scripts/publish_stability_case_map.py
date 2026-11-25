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
        links.append(f'<a href="#{target}"><span>{i:02}</span>{label}</a>')
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
            detail.append(f'<li><span>{year} 年</span><strong>{host-before:+.2f} <span>个百分点</span></strong>'
                          f'<small>{before:.2f}% → {host:.2f}%</small></li>')
        cards.append(f'<article id="{target}" tabindex="-1"><h3>{label}</h3><ul>{"".join(detail)}</ul>'
                     '</article>')

    grid = ''.join(f'M{x} 0V365' for x in range(75, 900, 75))
    grid += ''.join(f'M0 {y}H900' for y in range(62, 365, 75))
    active = ',\n'.join(
        f'#stability-case-map:has(#host-map-case-{i}:target) [href="#host-map-case-{i}"]'
        for i in range(1, len(cities) + 1)
    )

    section = f'''<section id="stability-case-map" aria-labelledby="stability-case-map-title">
<style>
#stability-case-map{{margin:38px 0 48px;padding-block:24px;scroll-margin-top:100px}}
#stability-case-map .host-map-heading{{margin-bottom:20px}}
#stability-case-map h2,#stability-case-map h3{{margin:0}}
#stability-case-map .host-map-heading p{{margin:6px 0 0}}
#stability-case-map .host-map-layout{{color:var(--sr-ink);display:grid;column-gap:clamp(18px,3vw,48px);grid-template-columns:minmax(0,1fr) minmax(225px,24%);align-items:start}}
#stability-case-map .host-map-main{{min-width:0}}
#stability-case-map svg{{display:block;width:100%;height:auto;background:transparent}}
#stability-case-map .host-map-geography{{mask-image:linear-gradient(to right,transparent,#000 7%,#000 93%,transparent)}}
#stability-case-map .host-graticule{{fill:none;stroke:var(--sr-muted);stroke-opacity:.15;stroke-width:.65}}
#stability-case-map polygon{{fill:color-mix(in srgb,var(--sr-muted) 22%,transparent);stroke:color-mix(in srgb,var(--sr-muted) 55%,transparent);stroke-width:.55}}
#stability-case-map circle{{fill:#e9c98f}}
#stability-case-map .host-pin{{fill:#142733;stroke:#e9c98f;stroke-width:1.4}}
#stability-case-map line{{stroke:#e9c98f;stroke-width:1;pointer-events:none}}
#stability-case-map text{{fill:#fff0d4;text-anchor:middle;dominant-baseline:central;font:700 11px system-ui;pointer-events:none}}
#stability-case-map .host-map-links{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));padding:8px clamp(8px,1.6vw,24px);gap:0 10px;border-top:1px solid var(--sr-line)}}
#stability-case-map .host-map-links a{{display:flex;align-items:center;gap:7px;min-height:44px;padding:4px 5px;color:var(--sr-ink);border-bottom:1px solid transparent;text-decoration:none;font-size:.88rem}}
#stability-case-map .host-map-links a span{{font-size:.68rem;color:var(--sr-muted);font-variant-numeric:tabular-nums}}
#stability-case-map .host-map-links a:is(:hover,:focus-visible){{background:var(--sr-line)}}
#stability-case-map aside{{padding:12px 0 10px clamp(16px,2vw,28px);border-left:1px solid var(--sr-line)}}
#stability-case-map aside > p{{margin:0 0 5px;color:var(--sr-muted);font-size:.8rem;letter-spacing:.08em}}
#stability-case-map article{{display:none;scroll-margin-top:110px}}
#stability-case-map aside:not(:has(article:target)) article:first-of-type,#stability-case-map article:target{{display:block}}
#stability-case-map article h3{{font-size:clamp(1.45rem,2.6vw,2rem)}}
#stability-case-map article ul{{list-style:none;margin:8px 0 16px;padding:0}}
#stability-case-map article li{{display:grid;gap:2px;padding:12px 0;border-bottom:1px solid var(--sr-line);font-variant-numeric:tabular-nums}}
#stability-case-map article strong{{color:var(--sr-accent);font-size:clamp(1.4rem,2vw,2rem);line-height:1.15}}
#stability-case-map article strong span{{font-size:.72rem;font-weight:500}}
#stability-case-map article small,#stability-case-map article li > span{{color:var(--sr-muted)}}
#stability-case-map aside > a{{color:var(--sr-accent);text-decoration:underline;text-underline-offset:4px}}
{active},
#stability-case-map:not(:has(article:target)) [href="#host-map-case-1"]{{color:var(--sr-accent);border-bottom-color:var(--sr-accent)}}
:is({active}, #stability-case-map:not(:has(article:target)) [href="#host-map-case-1"], #stability-case-map svg a:is(:hover,:focus-visible)) .host-pin{{fill:#e9c98f}}
:is({active}, #stability-case-map:not(:has(article:target)) [href="#host-map-case-1"], #stability-case-map svg a:is(:hover,:focus-visible)) text{{fill:#142733}}
#stability-case-map .host-map-note{{margin:12px 0 0;font-size:.84rem}}
@media (max-width:820px){{
  #stability-case-map .host-map-layout{{grid-template-columns:minmax(0,1fr)}}
  #stability-case-map aside{{border-left:0;border-top:1px solid var(--sr-line);padding-inline:0;margin-top:12px}}
}}
@media (max-width:560px){{#stability-case-map .host-map-links{{grid-template-columns:repeat(2,minmax(0,1fr))}}}}
</style>
<div class="host-map-heading"><h2 id="stability-case-map-title">主场效应案例地图</h2>
<p>选择城市，比较主办届与前一届的获奖记录份额。{len(cities)} 座城市，{sum(map(len,cities.values()))} 届案例。</p></div>
<div class="host-map-layout"><div class="host-map-main"><svg viewBox="0 0 900 365" aria-label="主场效应案例世界地图">
<g class="host-map-geography" aria-hidden="true"><path class="host-graticule" d="{grid}"/>{''.join(land)}</g>{''.join(pins)}</svg>
<nav class="host-map-links" aria-label="主办城市">{''.join(links)}</nav></div>
<aside aria-label="城市案例"><p>前一届 → 主办届</p>{''.join(cards)}<a href="../S1_东道主效应/index.html">查看主场效应核验 ↗</a></aside></div>
<p class="host-map-note">差值用于描述两届变化，不能单独证明主场的因果作用。底图来自项目内的 Natural Earth 110m 数据。</p>
</section>'''
    soup = BeautifulSoup(PAGE.read_text(encoding='utf-8'), 'html.parser')
    prior = soup.select_one('#stability-case-map')
    if prior:
        prior.decompose()
    soup.select_one('.stability-list').insert_before(BeautifulSoup(section, 'html.parser'))
    PAGE.write_text(str(soup), encoding='utf-8')


if __name__ == '__main__':
    publish()
