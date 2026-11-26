"""Validate nominal 80% residual intervals on later Olympic editions."""
import math
from html import escape
import re
from pathlib import Path

import markdown
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
TASK = ROOT / '交付文件/任务四_开放创作'
BASE = TASK / '05_满分升级'
MODEL = BASE / '15_原项目模型时序核验'
OUT = BASE / '16_预测区间时序核验'
OUT.mkdir(exist_ok=True)
MODELS = ['历史加权基线', '55基线45项目']
TOKYO = BASE / '17_东京补充回放'
YEAR = [2012, 2016, 2020, 2024]
residuals = pd.concat([pd.read_csv(MODEL / '原模型逐队误差.csv'),
                       pd.read_csv(TOKYO / '东京核心逐队误差.csv')], ignore_index=True)
data = residuals[
    residuals['来源'].eq('小项二次来源')
    & residuals['选择规则'].eq('仅此前届次')
    & residuals['模型'].isin(MODELS)
].copy()
assert sorted(data.Year.unique()) == YEAR
assert not data.duplicated(['Year', '模型', 'NOC']).any()
assert (data[['实际', '预测']] >= 0).all().all()

outputs = []
summary = []
for model in MODELS:
    series = data[data['模型'].eq(model)]
    # Keep the original Paris experiment alongside the Tokyo-augmented calibration.
    for target, calibration_years in [(2016,[2012]), (2020,[2012,2016]),
                                      (2024,[2012,2016]), (2024,[2012,2016,2020])]:
        past = series[series.Year.isin(calibration_years)]
        assert max(calibration_years) < target
        current = series[series.Year.eq(target)].copy()
        assert len(past) > 0 and len(current) > 0
        for method in ['统一半宽', '按预测量分组']:
            result = current.copy()
            result['半宽'] = 0.0
            groups = [(past, current)]
            if method == '按预测量分组':
                groups = [(past[past['预测'].lt(5)], current[current['预测'].lt(5)]),
                          (past[past['预测'].ge(5)], current[current['预测'].ge(5)])]
            for prior, evaluation in groups:
                calibration = (prior['实际'] - prior['预测']).abs().sort_values()
                assert len(prior) >= 4
                radius = calibration.iloc[math.ceil((len(prior) + 1) * .8) - 1]
                result.loc[evaluation.index, '半宽'] = radius
            result['区间方法'] = method
            result['校准届次'] = '+'.join(map(str, sorted(past.Year.unique())))
            result['下限'] = (result['预测'] - result['半宽']).clip(lower=0)
            result['上限'] = result['预测'] + result['半宽']
            result['覆盖'] = result['实际'].between(result['下限'], result['上限'])
            result['宽度'] = result['上限'] - result['下限']
            outputs.append(result)
            for label, sample in [('全体', result), ('预测至少5槽', result[result['预测'].ge(5)])]:
                summary.append({
                    '区间方法': method, '评估届次': target, '模型': model, '评估分组': label,
                    '校准届次': result['校准届次'].iat[0], '校准记录数': len(past),
                    '评分队数': len(sample), '覆盖队数': int(sample['覆盖'].sum()),
                    '覆盖率': sample['覆盖'].mean(), '平均宽度': sample['宽度'].mean(),
                    '平均绝对误差': (sample['实际'] - sample['预测']).abs().mean(),
                })
detail = pd.concat(outputs, ignore_index=True)
detail.to_csv(OUT / '逐队区间与覆盖.csv', index=False, encoding='utf-8-sig')
scores = pd.DataFrame(summary)
scores.to_csv(OUT / '逐届覆盖与宽度.csv', index=False, encoding='utf-8-sig')
lines = []
for r in summary:
    lines.append(f"| {r['区间方法']} | {r['评估届次']} | {r['模型']} | {r['评估分组']} | {r['校准届次']} | {r['覆盖队数']}/{r['评分队数']} | {r['覆盖率']:.1%} | {r['平均宽度']:.2f} |")
baseline_2024 = scores[
    scores['评估届次'].eq(2024) & scores['模型'].eq(MODELS[0])
    & scores['校准届次'].eq('2012+2016')
].set_index(['区间方法', '评估分组'])
fixed_all = baseline_2024.loc[('统一半宽', '全体'), '覆盖率']
fixed_high = baseline_2024.loc[('统一半宽', '预测至少5槽')]
group_high = baseline_2024.loc[('按预测量分组', '预测至少5槽')]
updated = scores[
    scores['评估届次'].eq(2024) & scores['模型'].eq(MODELS[0])
    & scores['校准届次'].eq('2012+2016+2020') & scores['评估分组'].eq('全体')
].set_index('区间方法')
tokyo = pd.read_csv(TOKYO / '东京完整配方评分.csv').set_index('情景')
tokyo_off = tokyo.loc['关闭排名', '全体MAE']
tokyo_on = tokyo.loc['加入棒球赛前信号', '全体MAE']
analog = pd.read_csv(BASE / '12_新增运动端到端类比回放/2016端到端类比评分.csv').set_index('情景')
off = analog.loc['关闭排名', '全体MAE']
on = analog.loc['加入赛前排名', '全体MAE']
md = f"""# 预测验证与区间覆盖

2024 留出评估中，中性基准的统一半宽区间覆盖 {fixed_all:.1%} 的评分代表团。预测至少 5 槽组的覆盖从 {fixed_high['覆盖率']:.1%} 提升到 {group_high['覆盖率']:.1%}，平均宽度从 {fixed_high['平均宽度']:.2f} 增至 {group_high['平均宽度']:.2f} 槽。分组改善了高预测量覆盖，仍未达到 80%。加入东京留出误差后，保持巴黎点预测固定，统一半宽和分组区间全体覆盖分别为 {updated.loc["统一半宽","覆盖率"]:.1%} 和 {updated.loc["按预测量分组","覆盖率"]:.1%}。

## 区间用过去的误差校准，再由未来届次评分

使用小项二次来源下的严格滚动留出逐队结果，分别检验历史加权基线和 55/45 核心情景。2016 只用 2012 误差，东京 2020 只用 2012、2016 误差。巴黎 2024 分别比较校准池有无东京留出误差，两种方案均保留。区间半宽为校准集绝对残差从小到大第 ⌈0.8(n+1)⌉ 个值，下限截在零。目标届实际结果只用来测覆盖及误差。评估含评分池内全部代表团，另按赛前预测至少 5 槽切片，以免全体读数掩盖高预测量代表团表现。

| 区间方法 | 评估届次 | 模型 | 分组 | 校准届次 | 覆盖队数 | 实测覆盖率 | 平均宽度（槽） |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
{chr(10).join(lines)}

统一半宽在 2024 全体样本中低于 80% 覆盖，高预测量组覆盖更低。另以赛前预测量是否达到 5 槽分组，仅从同组早期残差估半宽，检查覆盖改善与区间变宽的代价。分组是探索性对照，表中保留两种方法，未用结果选择或发布 2028 区间。

2012 缺少更早的同协议留出误差，因此只作校准输入。逐队误差受同届总池与代表团结构约束，校准误差跨届也可能变动。80% 是设定目标，覆盖率是各留出届次的实际观察。后验整理的历史数据存在修订，原巴黎点预测仍沿用原有 2016 最近小项训练届，新增东京误差只进入区间校准对照。此实验评估核心模型的逐队区间，2028 主榜仍只发布点估计。

## 完整集成公式的历史验证到哪里

| 验证层 | 历史证据 | 证据适用范围 |
| --- | --- | --- |
| 核心模型 | 2012、2016、2020、2024 严格时序回测，对比基线、RF、GB、RF/GB 和 55/45 | 小项代理下的总量预测 |
| 奖牌池、主场、资格 | 三届赛前条件和资格情景回放 | 奖牌池只用早期历史估计，资格采用条件情景 |
| 新增运动与完整配方 | 2016 七人制橄榄球赛前排名类比，45/45/10 加主场和总池归一 | 增加东京棒球一个小项的回归类比，仍无法覆盖 LA28 五项运动和真实资格 |
| 旧集成预测区间 | 2028 历史情景保留旧区间 | 缺少同协议跨届完整公式残差，无法给出经历史检验的 2028 完整集成覆盖率 |

2016 类比中，关闭排名与加入赛前排名的全体 MAE 分别为 {off:.4f} 与 {on:.4f} 枚/队，变化 {on-off:+.4f}。两种条件下前十均重合 9 队。这个对照说明完整公式能在已有赛前快照的历史案例中运行，排名分量的误差改善很小。

东京回放使用第三方抓取存档中的 339 个小项、1080 个奖牌槽评分。赛前池按 2008、2012、2016 历史估得 981 槽。主场使用既有 18% 上限情景并收缩，棒球信号取 2019 WBSC Premier12 四支已取得东京参赛资格的前四队，以名次倒数分配 1 个情景单位。参赛资格仅约束棒球分量，其他运动资格维持候选池。关闭与加入信号的全体 MAE 为 {tokyo_off:.5f} 与 {tokyo_on:.5f}，前十均重合 8 队。东京只覆盖棒球，软球和其他新增运动没有加入这一排名分量。

[东京完整配方评分](../17_东京补充回放/东京完整配方评分.csv) · [东京逐队对照](../17_东京补充回放/东京完整配方逐队对照.csv) · [东京核心评分](../17_东京补充回放/东京核心模型评分.csv) · [东京历史输入及来源](../17_东京补充回放/东京输入清单.json) · [IOC 东京项目规模](https://www.olympics.com/ioc/tokyo-2020-facts-and-figures) · [WBSC 2019 排名](https://static.wbsc.org/uploads/federations/278/cms/documents/8d9568c2-596e-53fe-f532-d1c35832aaaa.pdf)

[逐届覆盖与宽度 CSV](逐届覆盖与宽度.csv) · [逐队区间与覆盖 CSV](逐队区间与覆盖.csv) · [核心模型逐队误差](../15_原项目模型时序核验/原模型逐队误差.csv) · [赛前条件回放](../09_赛前条件回放/index.html) · [2016 完整公式类比](../12_新增运动端到端类比回放/index.html)

先运行 `项目工作区/scripts/tokyo_forecast_replay.py`，再运行 `项目工作区/scripts/publish_forecast_interval_audit.py`。
"""
(OUT / '预测区间核验说明.md').write_text(md, encoding='utf-8')
body = markdown.markdown(md, extensions=['tables'])
body = body.replace('<table>', '<div class="scroll" role="region" aria-label="核验数据表" tabindex="0"><table>').replace('</table>', '</table></div>')
body = body.replace('<p>2024 留出', '<p class="coverage-lead">2024 留出', 1)
body = body.replace('<h2>区间用过去', '<h2 id="coverage">区间用过去', 1)
body = body.replace('<h2>完整集成公式', '<h2 id="formula">完整集成公式', 1)
def coverage_tradeoff(rows):
    methods = ('统一半宽', '按预测量分组')
    selected = {
        row['区间方法']: (index, row) for index, row in enumerate(rows)
        if int(row['评估届次']) == 2024 and row['模型'] == '历史加权基线'
        and row['评估分组'] == '预测至少5槽' and row['校准届次'] == '2012+2016'
    }
    points, labels = [], []
    for number, method in enumerate(methods, 1):
        index, row = selected[method]
        width = float(row['平均宽度'])
        rate = float(row['覆盖率'])
        point_label = f'{method}，{width:.2f} 槽，覆盖 {rate:.1%}'
        points.append(f'<a href="#coverage-row-{index}" style="--x:{width / 16:.6%};--y:{rate:.6%}" '
                      f'aria-label="{point_label}，查看核验记录">{number}</a>')
        labels.append(f'<li>{method} · <strong>{width:.2f} 槽 · {rate:.1%}</strong></li>')
    return f"""<figure class="coverage-tradeoff" aria-labelledby="tradeoff-title">
<figcaption id="tradeoff-title">覆盖率与区间宽度</figcaption>
<p>巴黎 2024 留出评估 · 历史加权基线 · 预测至少 5 槽组 · 校准届次 2012、2016。点击圆点查看核验记录。</p>
<div class="tradeoff-grid">
<div class="tradeoff-y" aria-hidden="true"><span>100%</span><span>80%</span><span>0%</span></div>
<div class="tradeoff-plot"><span class="tradeoff-target">80% 目标</span>{''.join(points)}</div>
<div class="tradeoff-x" aria-hidden="true"><span>0</span><span>4</span><span>8</span><span>12</span><span>16</span></div>
</div>
<p class="tradeoff-axis-title">平均区间宽度（槽）</p>
<ol>{''.join(labels)}</ol>
<p>纵轴为实测覆盖率。分组提高了这一组的历史覆盖率，区间也随之变宽。2028 主榜仅发布点估计。</p>
</figure>"""


DELEGATION_NAMES = {
    'AUS': '澳大利亚',
    'AZE': '阿塞拜疆',
    'BLR': '白俄罗斯',
    'BRA': '巴西',
    'CAN': '加拿大',
    'CHN': '中国',
    'COL': '哥伦比亚',
    'CRO': '克罗地亚',
    'CUB': '古巴',
    'CZE': '捷克',
    'DEN': '丹麦',
    'ESP': '西班牙',
    'ETH': '埃塞俄比亚',
    'FRA': '法国',
    'GBR': '英国',
    'GEO': '格鲁吉亚',
    'GER': '德国',
    'GRE': '希腊',
    'HUN': '匈牙利',
    'IRI': '伊朗',
    'ITA': '意大利',
    'JAM': '牙买加',
    'JPN': '日本',
    'KAZ': '哈萨克斯坦',
    'KEN': '肯尼亚',
    'KOR': '韩国',
    'MEX': '墨西哥',
    'NED': '荷兰',
    'NOR': '挪威',
    'NZL': '新西兰',
    'POL': '波兰',
    'PRK': '朝鲜',
    'ROU': '罗马尼亚',
    'RSA': '南非',
    'RUS': '俄罗斯',
    'SRB': '塞尔维亚',
    'SUI': '瑞士',
    'SWE': '瑞典',
    'THA': '泰国',
    'TUR': '土耳其',
    'UKR': '乌克兰',
    'USA': '美国',
    'UZB': '乌兹别克斯坦',
}


def delegation_intervals(rows):
    selected = [row for row in rows if int(row['Year']) == 2024
                and row['模型'] == '历史加权基线' and row['校准届次'] == '2012+2016'
                and float(row['预测']) >= 5]
    maximum = max(max(float(row[key]) for key in ('上限', '实际')) for row in selected)
    ceiling = math.ceil(maximum / 10) * 10
    panels = []
    for index, method in enumerate(('统一半宽', '按预测量分组')):
        series = sorted((row for row in selected if row['区间方法'] == method),
                        key=lambda row: -float(row['预测']))
        marks = []
        misses = 0
        for row in series:
            low, high, prediction, actual = (float(row[key]) for key in ('下限', '上限', '预测', '实际'))
            side = '低于下限' if actual < low else '高于上限' if actual > high else '区间内'
            state = 'covered' if side == '区间内' else 'miss'
            misses += state == 'miss'
            code = str(row['NOC'])
            name = escape(DELEGATION_NAMES.get(code, code))
            coords = ';'.join(f'--{key}:{value / ceiling:.6%}' for key, value in
                              zip(('low', 'high', 'prediction', 'actual'), (low, high, prediction, actual)))
            marks.append(f"""<details class="delegation-row {state}">
<summary><strong>{name}</strong><span class="delegation-track" style="{coords}" aria-hidden="true"><i></i><b></b><em></em></span><span>{side}</span></summary>
<p>点预测 {prediction:.2f} 槽 · 实际 {actual:.2f} 槽 · 区间 {low:.2f}–{high:.2f} 槽。实际值{side if state == 'miss' else '落在区间内'}。</p>
</details>""")
        panels.append(f'<section class="delegation-method method-{index}" aria-label="{method}">'
                      f'<p>{len(series)} 队中有 {misses} 队未覆盖。</p>'
                      f'<div class="delegation-axis" aria-hidden="true"><span>0</span><span>{ceiling / 2:g}</span><span>{ceiling} 槽</span></div>'
                      + ''.join(marks) + '</section>')
    return f"""<details class="delegation-intervals"><summary>查看逐队预测区间</summary>
<p>巴黎 2024 留出评估 · 历史加权基线 · 预测至少 5 槽 · 用 2012、2016 校准。点击代表团查看数值和偏离方向。</p>
<p>— 预测区间　● 点预测　◆ 实际结果</p>
<fieldset><legend>区间方法</legend>
<label><input type="radio" name="delegation-method" id="delegation-uniform" checked> 统一半宽</label>
<label><input type="radio" name="delegation-method" id="delegation-grouped"> 按预测量分组</label>
</fieldset>
<label><input type="checkbox" id="delegation-misses"> 仅看未覆盖</label>
{''.join(panels)}
</details>"""


def calibration_track(rows):
    reference = {
        (int(row['评估届次']), row['校准届次']): index
        for index, row in enumerate(rows)
        if row['模型'] == '历史加权基线' and row['区间方法'] == '统一半宽'
        and row['评估分组'] == '全体'
    }
    stages = ['<li data-year="2012"><strong>2012</strong><span>校准起点</span></li>']
    styles = []
    for year, pools in ((2016, ('2012',)), (2020, ('2012+2016',)),
                        (2024, ('2012+2016', '2012+2016+2020'))):
        links = []
        for pool in pools:
            row_id = f'coverage-row-{reference[year, pool]}'
            links.append(f'<a href="#{row_id}">用 {pool.replace("+", "、")} 校准</a>')
            scope = f'body:has(#{row_id}:target) .calibration-track'
            years = ','.join(f'{scope} [data-year="{item}"]' for item in pool.split('+'))
            styles.append(f'{years}{{border-top-color:var(--accent);background:color-mix(in srgb,var(--accent) 9%,transparent)}}')
            styles.append(f'{scope} a[href="#{row_id}"]{{font-weight:700;text-decoration-thickness:2px}}')
        stages.append(f'<li data-year="{year}"><strong>{year}</strong><span>留出评估</span>{"".join(links)}</li>')
    return f"""<nav class="calibration-track" aria-labelledby="calibration-title">
<style>{''.join(styles)}</style>
<h3 id="calibration-title">校准与评估赛道</h3>
<p>选择校准方案，金色站点标出纳入的校准届次。入口定位至历史加权基线、统一半宽、全体代表团的核验表行。</p>
<ol>{''.join(stages)}</ol>
</nav>"""


def add_coverage_plot(body, rows):
    selected = []
    for index, row in enumerate(rows):
        year = int(row['评估届次'])
        if (row['模型'] == '历史加权基线' and row['区间方法'] == '统一半宽'
                and (year != 2024 or row['校准届次'] == '2012+2016')):
            selected.append((index, year, row))
    panels = []
    for group in ('全体', '预测至少5槽'):
        points = [item for item in selected if item[2]['评估分组'] == group]
        points.sort(key=lambda item: item[1])
        _, furthest_year, furthest = max(points, key=lambda item: abs(float(item[2]['覆盖率']) - .8))
        gap = abs(float(furthest['覆盖率']) * 100 - 80)
        marks = []
        for index, year, row in points:
            rate = float(row['覆盖率']) * 100
            count = int(row['评分队数'])
            marks.append(f"""<div class="coverage-point-row">
<span>{year}</span><div class="coverage-track"><a href="#coverage-row-{index}"
 style="--rate:{rate:.5f}%" aria-label="{year} 年，覆盖率 {rate:.1f}%，评分 {count} 队，查看核验表"></a></div>
<span><strong>{rate:.1f}%</strong> · {count} 队</span></div>""")
        panels.append(f"""<section><h3>{group}</h3>
<div class="coverage-axis" aria-hidden="true"><span>0%</span><span>80% 目标</span><span>100%</span></div>
{''.join(marks)}<p>偏离最大：{furthest_year} 年，距目标 {gap:.1f} 个百分点。</p></section>""")
    chart = f"""<figure class="coverage-plot" aria-labelledby="coverage-plot-title">
<figcaption id="coverage-plot-title">历史验证覆盖率</figcaption>
<p>历史加权基线 · 统一半宽。巴黎 2024 使用 2012 和 2016 的误差校准。点击圆点查看覆盖队数及区间宽度。</p>
<div class="coverage-panels">{''.join(panels)}</div>
<p>2012 只用于校准。80% 是历史核验的设定目标，2028 主榜只发布点估计。</p></figure>
"""
    first, tail = body.split('</tbody>', 1)
    assert first.count('<tr>') == len(rows) + 1
    ids = iter(f'<tr id="coverage-row-{index}" tabindex="-1">' for index in range(len(rows)))
    head, records = first.split('<tbody>', 1)
    records = re.sub(r'<tr>', lambda _: next(ids), records)
    result = head + '<tbody>' + records + '</tbody>' + tail
    return re.sub(r'<div\b[^>]*class="scroll"[^>]*>', lambda match: calibration_track(rows) + chart + coverage_tradeoff(rows) + delegation_intervals(detail.to_dict('records')) + match[0], result, count=1)


body = add_coverage_plot(body, summary)


def add_audit_navigation(page, delivery, destination):
    from os.path import relpath
    from bs4 import BeautifulSoup

    template = delivery / '任务三_专题深挖/12_反例与证据链/index.html'
    shell = BeautifulSoup(template.read_text(encoding='utf-8'), 'html.parser')
    result = BeautifulSoup(page, 'html.parser')
    assets = (
        'link[href*="supplement-reading.css"]', 'link[href*="integrated-nav.css"]',
        '#supplement-theme-preload',
        'script[src*="supplement-reading.js"]', 'script[src*="integrated-nav.js"]',
    )
    for selector in (*assets, '#xz-nav', '#xz-menu'):
        element = shell.select_one(selector)
        for node in (element, *element.select('[href],[src]')):
            for attr in ('href', 'src'):
                if node.has_attr(attr):
                    path, sep, query = node[attr].partition('?')
                    relative = Path(relpath(template.parent / path, destination)).as_posix()
                    node[attr] = relative + sep + query
        if selector in assets:
            result.head.append(element)
        else:
            result.main.insert_before(element)
    for link in result.select('#xz-nav .xz-links a'):
        link.attrs.pop('aria-current', None)
        if '任务四_开放创作' in link['href']:
            link['aria-current'] = 'page'
    result.body['class'] = ['supplement-reading', 'interval-reading']
    return '<!doctype html>' + str(result.html)


page = """<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>预测验证与区间覆盖</title>
<style>
:root{color-scheme:light dark;--paper:#f5f3ed;--ink:#19363c;--muted:#52686b;--accent:#785525;--line:#758b8b55}
@media(prefers-color-scheme:dark){:root{--paper:#15222b;--ink:#eef2ee;--muted:#b0c0bf;--accent:#ddc393;--line:#b6c9c540}}
*{box-sizing:border-box}body{margin:0;background:radial-gradient(ellipse at top left,#648a962b,transparent 72%) top/100% 29rem no-repeat,var(--paper);color:var(--ink);font:16px/1.75 system-ui,"Microsoft YaHei",sans-serif}
main{padding:clamp(24px,4vw,64px) clamp(20px,6vw,100px)}
nav{display:flex;flex-wrap:wrap;gap:8px 22px}nav a{display:inline-flex;align-items:center;min-height:44px}
h1{font-size:clamp(2rem,4vw,3.8rem);line-height:1.2;margin:20px 0}
h2{font-size:clamp(1.35rem,2.4vw,2rem);margin:36px 0 14px;border-top:1px solid var(--line);padding-top:20px}
p{max-width:86ch;color:var(--muted);overflow-wrap:anywhere}
.coverage-lead{border-inline-start:2px solid var(--accent);padding-inline-start:16px;color:var(--ink)}
.scroll{overflow:auto;border:1px solid var(--line)}
table{width:100%;min-width:44rem;border-collapse:collapse}
th,td{padding:.55rem .75rem;text-align:left;border-bottom:1px solid var(--line);font-variant-numeric:tabular-nums}
thead{background:color-mix(in srgb,var(--ink) 8%,var(--paper))}
tbody tr:nth-child(even){background:color-mix(in srgb,var(--ink) 3%,var(--paper))}
a{color:var(--accent);text-underline-offset:4px}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.scroll:focus-visible{outline-offset:-2px}

@media screen {
  body.interval-reading {isolation:isolate}
  body.interval-reading::after {
    content:"";position:absolute;inset:0 0 auto;height:29rem;z-index:-1;pointer-events:none;
    background:radial-gradient(ellipse at top left,#648a9638,transparent 72%);
    transform-origin:top left;
  }
}
@media screen and (prefers-reduced-motion:no-preference) {
  body.interval-reading::after {animation:interval-light 20s ease-in-out infinite alternate}
}
@keyframes interval-light {
  from {transform:scale(.82,.93);opacity:.65}
  to {transform:scale(1);opacity:1}
}
html body.interval-reading.supplement-reading:not(.supp-existing-nav)>main{padding-top:clamp(12px,1.5vw,24px)!important}
.interval-reading main h2[id]{scroll-margin-top:90px}

.interval-reading main tbody tr:hover,
.interval-reading main tbody tr:focus-within {
  background:color-mix(in srgb,var(--accent) 10%,var(--paper));
}
@media (prefers-reduced-motion:no-preference) {
  .interval-reading main tbody tr {transition:background-color 160ms ease}
}

.coverage-plot{margin:24px 0;border-block:1px solid var(--line);padding-block:18px}
.coverage-plot figcaption{font-size:1.35rem;font-weight:650}
.coverage-plot p{font-size:.9rem;margin:10px 0}
.coverage-panels{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px 40px}
.coverage-panels h3{margin:8px 0}
.coverage-axis,.coverage-point-row{display:grid;grid-template-columns:4ch minmax(0,1fr) 8.5em;gap:10px;align-items:center;font-variant-numeric:tabular-nums}
.coverage-axis{position:relative;display:flex;justify-content:space-between;margin-inline:calc(4ch + 10px) calc(8.5em + 10px);color:var(--muted);white-space:nowrap}
.coverage-axis span:nth-child(2){position:absolute;left:80%;transform:translateX(-77%);color:var(--accent)}
.coverage-track{position:relative;height:44px;background:linear-gradient(var(--line),var(--line)) center/100% 1px no-repeat}
.coverage-track::before{content:"";position:absolute;inset:0 auto 0 80%;border-left:1px dashed var(--accent)}
.coverage-track a{position:absolute;left:var(--rate);top:50%;transform:translate(-50%,-50%);width:44px;height:44px;display:grid;place-items:center}
.coverage-track a::after{content:"";width:12px;height:12px;border-radius:50%;background:var(--accent)}
.coverage-track a:hover::after,.coverage-track a:focus-visible::after{outline:2px solid var(--accent);outline-offset:3px}
.interval-reading tr[id]{scroll-margin-top:90px}
.interval-reading tr:target{background:color-mix(in srgb,var(--accent) 16%,var(--paper))}
@media(max-width:850px){.coverage-panels{grid-template-columns:minmax(0,1fr)}}

.coverage-tradeoff{margin:24px 0;border-bottom:1px solid var(--line);padding-bottom:16px}
.coverage-tradeoff figcaption{font-size:1.35rem;font-weight:650}
.tradeoff-grid{display:grid;grid-template-columns:3.5rem minmax(0,1fr);column-gap:8px;margin:16px 0 0}
.tradeoff-y{position:relative;color:var(--muted);font-size:.8rem;text-align:right}
.tradeoff-y span{position:absolute;right:0;top:0;transform:translateY(-50%)}
.tradeoff-y span:nth-child(2){top:20%}
.tradeoff-y span:last-child{top:100%}
.tradeoff-plot{position:relative;height:clamp(170px,25vw,250px);border-left:1px solid var(--line);border-bottom:1px solid var(--line)}
.tradeoff-target{position:absolute;top:20%;width:100%;border-top:1px dashed var(--accent);color:var(--accent);font-size:.78rem}
.tradeoff-plot a{position:absolute;left:var(--x);bottom:var(--y);translate:-50% 50%;width:44px;height:44px;display:grid;place-items:center;text-decoration:none;font-weight:700;isolation:isolate;color:var(--paper)}
.tradeoff-plot a::before{content:"";position:absolute;z-index:-1;width:23px;height:23px;border-radius:50%;background:var(--accent)}
.tradeoff-x{grid-column:2;display:flex;justify-content:space-between;color:var(--muted);font-size:.8rem}
.coverage-tradeoff .tradeoff-axis-title{max-width:none;padding-inline-start:calc(3.5rem + 8px);text-align:center;font-size:.85rem;margin:3px 0}
.coverage-tradeoff li{padding-inline-start:.25em}

.delegation-intervals{margin:20px 0 28px;border-block:1px solid var(--line);padding-block:12px}
.delegation-intervals summary{cursor:pointer}
.delegation-intervals>summary{font-weight:650;color:var(--sr-accent,var(--accent));min-height:44px;width:100%}
.delegation-intervals fieldset{border:0;margin:0 0 8px;padding:0}
.delegation-intervals fieldset label{display:inline-block;margin-inline-end:12px}
.delegation-intervals:has(#delegation-uniform:checked) .method-1,
.delegation-intervals:has(#delegation-grouped:checked) .method-0,
.delegation-intervals:has(#delegation-misses:checked) .covered{display:none}
.delegation-method{--name-width:clamp(5em,10vw,8em);font-size:.85rem}
.delegation-axis{display:flex;justify-content:space-between;margin-inline:calc(var(--name-width) + 12px) calc(5em + 12px);font-size:.85rem}
.delegation-row summary{display:grid;grid-template-columns:var(--name-width) minmax(0,1fr) 5em;gap:12px;align-items:center;min-height:44px;border-bottom:1px solid var(--line)}
.delegation-row summary:hover{background:color-mix(in srgb,var(--accent) 8%,transparent)}
.delegation-row.miss summary>span:last-child{color:var(--accent);font-weight:600}
.delegation-track{position:relative;height:23px}
.delegation-track i{position:absolute;left:var(--low);right:calc(100% - var(--high));top:50%;border-top:2px solid var(--muted)}
.delegation-track :is(b,em){position:absolute;top:50%;width:9px;height:9px;translate:-50% -50%}
.delegation-track b{left:var(--prediction);border-radius:50%;background:var(--ink)}
.delegation-track em{left:var(--actual);rotate:45deg;background:var(--accent);outline:1px solid var(--paper)}

.calibration-track{display:block;margin:22px 0;scroll-margin-top:90px}
.calibration-track h3{margin-bottom:4px}
.calibration-track p{margin:4px 0 12px;font-size:.9rem}
.calibration-track ol{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:6px;list-style:none;margin:0;padding:0}
.calibration-track li{min-width:0;border-top:3px solid var(--line);padding:8px}
.calibration-track li strong,.calibration-track li span{display:block}
.calibration-track li strong{font-size:1.25rem;font-variant-numeric:tabular-nums}
.calibration-track li span{color:var(--muted);font-size:.84rem}
.calibration-track li a{display:flex;font-size:.85rem;min-height:44px}
@media(max-width:700px){.calibration-track ol{grid-template-columns:repeat(2,minmax(0,1fr))}}
</style></head><body><main>
<nav aria-label="本页导航"><a href="../../02_2028洛杉矶预测/index.html">← 返回预测页</a><a href="#coverage">历史覆盖率 ↓</a><a href="#formula">完整公式验证 ↓</a><a href="预测区间核验说明.md" download>下载核验说明</a></nav>"""
motion = """<script>
(() => {
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  if (!('IntersectionObserver' in window) || !Element.prototype.animate || reduced.matches) return;
  const observer = new IntersectionObserver(entries => {
    for (const {target, isIntersecting} of entries) {
      if (!isIntersecting) continue;
      observer.unobserve(target);
      if (reduced.matches || target.contains(document.activeElement)) continue;
      target.animate(
        [{opacity:.8, translate:'0 6px'}, {opacity:1, translate:'0 0'}],
        {duration:360, easing:'cubic-bezier(.22,1,.36,1)'}
      );
    }
  });
  document.querySelectorAll('main :is(.coverage-lead, h2[id], .scroll)').forEach(element => observer.observe(element));
})();
</script>"""
(OUT / 'index.html').write_text(add_audit_navigation(page + body + '</main>' + motion + '</body></html>', TASK.parent, OUT), encoding='utf-8')
for section in ['02_2028洛杉矶预测', '03_数据新闻']:
    file = TASK / section / 'index.html'
    html = file.read_text(encoding='utf-8')
    html = re.sub(r'<!-- FORECAST_INTERVAL_START -->.*?<!-- FORECAST_INTERVAL_END -->', '', html, flags=re.S)
    anchor = re.search(r'<a\b[^>]*href="../05_满分升级/15_原项目模型时序核验/index.html"[^>]*>.*?</a>', html, flags=re.S)
    assert anchor, file
    link = '<!-- FORECAST_INTERVAL_START --> · <a href="../05_满分升级/16_预测区间时序核验/index.html">查历史区间覆盖与完整公式回放</a><!-- FORECAST_INTERVAL_END -->'
    file.write_text(html[:anchor.end()] + link + html[anchor.end():], encoding='utf-8')
print(scores.to_string(index=False))
