"""Render the fixed-cohort sport comparison from its published CSV."""
import csv
from html import escape
from pathlib import Path
import re

from task2_localization import SPORT_ZH

ROOT = Path(__file__).resolve().parents[2]
FOLDER = ROOT / '交付文件/任务三_专题深挖/S3_冠军的保质期/10_王朝机制与反例'


def sport_chart(folder):
    with (folder / '逐运动趋势与反例.csv').open(encoding='utf-8-sig', newline='') as source:
        eligible = [(row['Sport'], float(row['late_minus_early_pp']))
                    for row in csv.DictReader(source) if float(row['size_早段']) >= 8]
    shown = sorted(eligible, key=lambda row: row[1])[-12:][::-1]
    limit = max(40, 10 * int(max(abs(value) for _, value in shown) / 10 + 1))
    rows = []
    for sport, value in shown:
        name = escape(SPORT_ZH.get(sport, '马术' if sport == 'Equestrianism' else sport))
        kind = 'up' if value > 0 else 'down' if value < 0 else 'zero'
        number = f'{value:+.1f}'.replace('-', '−') if value else '0.0'
        rows.append(
            f'<div class="dy-sport-row {kind}" role="listitem">'
            f'<span>{name}</span><span class="dy-sport-track" aria-hidden="true">'
            f'<i style="--bar:{abs(value) / (2 * limit):.6%}"></i></span>'
            f'<strong>{number}</strong></div>'
        )
    return f'''<!-- DYNASTY_SPORT_CHART_START -->
<style>
html body main:has(>.dy-sport-chart){{box-sizing:border-box;width:100%;max-width:none!important;padding:clamp(22px,3vh,42px) clamp(16px,4.5vw,112px) 32px!important}}
html body main:has(>.dy-sport-chart)>.scroll table{{width:100%;font-variant-numeric:tabular-nums}}
html body main:has(>.dy-sport-chart)>.scroll :is(th,td){{padding-block:12px!important}}
html body main:has(>.dy-sport-chart)>.scroll :is(th,td):nth-child(n+3){{text-align:right!important}}
html body main:has(>.dy-sport-chart)>.note{{
 background:transparent!important;color:inherit!important;border-radius:0!important;
 border-inline-start:3px solid #ad9464;padding:6px 0 6px 16px!important;margin:18px 0 10px;
}}
html body main:has(>.dy-sport-chart)>.note+p{{margin:10px 0 0}}
html body:has(main>.dy-sport-chart) :is(main>.note+p,#dynasty-source-sensitivity) a{{
 color:#226078!important;text-underline-offset:4px;
}}
html body.xz-dark:has(main>.dy-sport-chart) :is(main>.note+p,#dynasty-source-sensitivity) a{{color:#acd4df!important}}
html body:has(main>.dy-sport-chart) #dynasty-source-sensitivity{{
 width:auto!important;max-width:none!important;box-sizing:border-box;
 margin:0 clamp(16px,4.5vw,112px) 16px!important;padding:20px 0 16px!important;
}}
html body:has(main>.dy-sport-chart) #dynasty-source-sensitivity h2{{margin-top:0}}
html body:has(main>.dy-sport-chart) #dynasty-source-sensitivity img{{
 width:100%;max-width:none!important;aspect-ratio:auto 1600 / 560;
}}
html body main:has(>.dy-sport-chart)>details.ex-route{{margin-block:12px 16px!important}}
html body main:has(>.dy-sport-chart)>details.ex-route>summary{{min-height:44px;padding-block:4px!important}}
.dy-sport-chart{{--up:#17687b;--down:#934a34;--ruler:#718b9666;margin:2rem 0;color:inherit}}
body.xz-dark .dy-sport-chart{{--up:#87c9db;--down:#f0a284;--ruler:#aec3ce52}}
.dy-sport-chart figcaption{{margin-bottom:1rem}}
.dy-sport-chart figcaption h2{{font-size:clamp(21px,2.6vw,34px);margin:0 0 .4rem}}
.dy-sport-chart figcaption p{{margin:0}}
.dy-sport-row{{display:grid;grid-template-columns:5em minmax(0,1fr) 4em;align-items:center;gap:clamp(5px,1.5vw,20px);min-height:32px;border-bottom:1px solid #8097a32e;font-variant-numeric:tabular-nums}}
.dy-sport-row strong{{text-align:right;font-weight:650}}
.dy-sport-track{{position:relative;align-self:stretch;background:linear-gradient(90deg,transparent calc(50% - .5px),var(--ruler) calc(50% - .5px),var(--ruler) calc(50% + .5px),transparent calc(50% + .5px))}}
.dy-sport-track i{{position:absolute;top:50%;height:11px;width:var(--bar);transform:translateY(-50%);background:currentColor}}
.dy-sport-row.up :is(strong,i){{color:var(--up)}}
.dy-sport-row.down :is(strong,i){{color:var(--down)}}
.up .dy-sport-track i{{left:50%;border-radius:0 4px 4px 0}}
.down .dy-sport-track i{{right:50%;border-radius:4px 0 0 4px}}
.zero .dy-sport-track i{{left:50%;width:6px;height:6px;border-radius:50%;transform:translate(-50%,-50%)}}
.dy-sport-axis{{display:flex;justify-content:space-between;grid-column:2;font-size:.82em}}
.dy-sport-chart .dy-sport-note{{font-size:.84em;margin:.7em 0 0}}
@media(max-width:520px){{.dy-sport-row{{grid-template-columns:3.7em minmax(0,1fr) 3.5em;font-size:.85rem}}}}
</style>
<figure class="dy-sport-chart" aria-labelledby="dy-sport-title">
<figcaption><h2 id="dy-sport-title">各运动的卫冕率升降</h2>
<p>后段（1996—2016）减早段（1964—1976），单位为百分点。</p></figcaption>
<div class="dy-sport-row" aria-hidden="true"><span class="dy-sport-axis"><span>−{limit}</span><span>0</span><span>+{limit}</span></span></div>
<div role="list">{''.join(rows)}</div>
<p class="dy-sport-note">仅纳入早段至少有 8 次转移记录的运动，展示差值从高到低的前 {len(shown)} 项。</p>
</figure>
<!-- DYNASTY_SPORT_CHART_END -->'''


if __name__ == '__main__':
    page = FOLDER / 'index.html'
    html = page.read_text(encoding='utf-8')
    target = r'<!-- DYNASTY_SPORT_CHART_START -->.*?<!-- DYNASTY_SPORT_CHART_END -->|<img\b[^>]*src="逐运动反例\.png"[^>]*>'
    html, count = re.subn(target, lambda _: sport_chart(FOLDER), html, flags=re.S)
    if count != 1:
        raise SystemExit(f'Expected one sport chart, found {count}')
    page.write_text(html, encoding='utf-8')
