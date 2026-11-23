"""Publish a readable edition table from the fixed-cohort results."""
import csv
import json
from collections import Counter
from html import escape
from pathlib import Path
import re

from task2_localization import NOC_ZH

ROOT = Path(__file__).resolve().parents[2]
FOLDER = ROOT / '交付文件/任务三_专题深挖/S3_冠军的保质期/09_固定小项队列检验'
TABLE = '固定队列逐届卫冕率.csv'


def edition_table(folder):
    with (folder / TABLE).open(encoding='utf-8-sig', newline='') as file:
        editions = list(csv.DictReader(file))
    rows = []
    for edition in editions:
        year = int(edition['to_year'])
        size = int(edition['size'])
        rate = float(edition['mean'])
        period = '早段' if year <= 1976 else '后段' if year >= 1996 else '主比较排除'
        rows.append(f'<tr><th scope="row">{year}</th><td>{period}</td><td>{size}</td><td>{rate:.1%}</td></tr>')
    return f'''<!-- DYNASTY_EDITION_TABLE_START -->
<details class="dynasty-edition-table">
<summary>查看逐届卫冕率</summary>
<p>1980—1992 年保留在趋势图与下表中，主比较使用早段和后段。</p>
<div class="dynasty-table-scroll" role="region" aria-label="固定小项逐届卫冕率" tabindex="0">
<table><thead><tr><th scope="col">目标届次</th><th scope="col">比较时间窗</th><th scope="col">可比小项</th><th scope="col">卫冕率</th></tr></thead><tbody>{''.join(rows)}</tbody></table>
</div>
<p><a href="{escape(TABLE)}" download>下载逐届卫冕率 CSV ↓</a></p>
</details>
<!-- DYNASTY_EDITION_TABLE_END -->'''


def championship_flow(folder):
    editions = {}
    with (folder / '固定小项逐届控制权转移.csv').open(encoding='utf-8-sig', newline='') as file:
        for row in csv.DictReader(file):
            edition = (row['from_year'], row['to_year'])
            key = (row['previous'], row['current'], row['defended'].lower() == 'true')
            editions.setdefault(edition, Counter())[key] += 1
    codes = {code for flows in editions.values() for source, target, _ in flows for code in (source, target)}
    names = {code: '／'.join(NOC_ZH[part] for part in code.split('|')) for code in sorted(codes)}
    data = json.dumps({
        'names': names,
        'editions': [[start, end, [[*key, count] for key, count in flows.items()]]
                     for (start, end), flows in sorted(editions.items())],
    }, ensure_ascii=False)
    return f'''<section class="dynasty-flow" aria-labelledby="dynasty-flow-title">
<h2 id="dynasty-flow-title">谁接过了冠军？</h2>
<p>连线从上届金牌代表团指向本届金牌代表团，线宽表示小项数。数据为固定队列的历史 Event 代理。</p>
<div class="dynasty-flow-controls">
<div id="dynasty-flow-edition" role="group" aria-label="选择相邻届次"></div>
<div id="dynasty-flow-kind" role="group" aria-label="转移类型">
<button type="button" data-kind="all" aria-pressed="true">全部</button><button type="button" data-kind="defended" aria-pressed="false">卫冕</button><button type="button" data-kind="changed" aria-pressed="false">易主</button>
</div>
<button type="button" id="dynasty-flow-play">播放历届</button>
</div>
<p class="dynasty-flow-key"><span>暖金 · 卫冕</span><span>蓝青 · 易主</span></p>
<p id="dynasty-flow-status" role="status"></p>
<div class="dynasty-flow-stage"><svg id="dynasty-flow-chart" role="img" aria-label="左侧为上届代表团，右侧为本届代表团"></svg></div>
<details><summary>查看代表团转移明细</summary><ul id="dynasty-flow-list"></ul></details>
<script type="application/json" id="dynasty-flow-data">{data}</script>
<script src="../../../共享组件/dynasty-championship-flow.js?v=2" defer></script>
</section>'''


def publish_edition_table(folder=FOLDER):
    page = folder / 'index.html'
    html = page.read_text(encoding='utf-8')
    html = re.sub(r'\n?<!-- DYNASTY_EDITION_TABLE_START -->.*?<!-- DYNASTY_EDITION_TABLE_END -->', '', html, flags=re.S)
    html, count = re.subn(r'<img\b[^>]*\bdynasty-fixed-trend\b[^>]*>', lambda match: match[0] + '\n' + edition_table(folder).replace('<!-- DYNASTY_EDITION_TABLE_END -->', championship_flow(folder) + '\n<!-- DYNASTY_EDITION_TABLE_END -->'), html)
    if count != 1:
        raise ValueError('Expected exactly one fixed-cohort trend image')
    page.write_text(html, encoding='utf-8')


if __name__ == '__main__':
    publish_edition_table()
