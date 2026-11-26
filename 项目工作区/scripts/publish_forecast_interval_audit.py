"""Validate nominal 80% residual intervals on later Olympic editions."""
import math
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
</style></head><body><main>
<nav aria-label="本页导航"><a href="../../02_2028洛杉矶预测/index.html">← 返回预测页</a><a href="#coverage">历史覆盖率 ↓</a><a href="#formula">完整公式验证 ↓</a><a href="预测区间核验说明.md" download>下载核验说明</a></nav>"""
(OUT / 'index.html').write_text(add_audit_navigation(page + body + '</main></body></html>', TASK.parent, OUT), encoding='utf-8')
for section in ['02_2028洛杉矶预测', '03_数据新闻']:
    file = TASK / section / 'index.html'
    html = file.read_text(encoding='utf-8')
    html = re.sub(r'<!-- FORECAST_INTERVAL_START -->.*?<!-- FORECAST_INTERVAL_END -->', '', html, flags=re.S)
    anchor = re.search(r'<a\b[^>]*href="../05_满分升级/15_原项目模型时序核验/index.html"[^>]*>.*?</a>', html, flags=re.S)
    assert anchor, file
    link = '<!-- FORECAST_INTERVAL_START --> · <a href="../05_满分升级/16_预测区间时序核验/index.html">查历史区间覆盖与完整公式回放</a><!-- FORECAST_INTERVAL_END -->'
    file.write_text(html[:anchor.end()] + link + html[anchor.end():], encoding='utf-8')
print(scores.to_string(index=False))
