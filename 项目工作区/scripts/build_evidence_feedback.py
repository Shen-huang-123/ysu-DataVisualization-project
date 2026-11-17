"""Add interaction feedback to three existing evidence pages, without refitting data.

Run after page publishers and polish_evidence_figures.py. Local JSON payloads also
work over file://. Existing static figures/tables remain the no-script fallback.
"""
from pathlib import Path
from html import escape
import csv, hashlib, json, os, re

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'交付文件'
SHARED=BASE/'共享组件'
R=BASE/'任务三_专题深挖/S2_口径的魔力/09_奖牌口径实验室'
I=BASE/'任务三_专题深挖/S3_冠军的保质期/11_历史来源敏感性'
M=BASE/'任务四_开放创作/05_满分升级/15_原项目模型时序核验'
inputs=[R/'data.json',I/'固定队列三方案复算.csv',M/'原模型五方案评分.csv']

def read_csv(p):
    with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))

interval=[]
for x in read_csv(inputs[1])[:3]:
    interval.append(dict(name=x['方案'],n=int(x['小项数']),transitions=int(x['转移数']),delta=float(x['后减前百分点']),low=float(x['区间下限']),high=float(x['区间上限'])))
assert [x['n'] for x in interval]==[113,113,50]
scores=[x for x in read_csv(inputs[2]) if x['选择规则']=='仅此前届次']
baselines={(x['来源'],x['Year']):float(x['MAE']) for x in scores if x['模型']=='历史加权基线'}
models=['RF60_GB40','55基线45项目','RF','GB']
sources=['小项二次来源','小项原代理','运动员行原口径']
rows=[dict(source=x['来源'],year=x['Year'],model=x['模型'],mae=float(x['MAE']),baseline=baselines[x['来源'],x['Year']]) for x in scores if x['模型'] in models]
assert len(rows)==36 and all(x['mae']>=0 for x in rows)

rank='''<section id="rank-discovery" class="evidence-feedback" aria-labelledby="rank-feedback-title" hidden><h2 id="rank-feedback-title">亲手切换：同一组结果，名次如何改变？</h2><div role="status" aria-live="polite" aria-atomic="true"><p id="rank-result" class="ef-main"></p><p id="rank-direction" class="ef-key"></p><p id="rank-unit"></p><p id="rank-meaning" class="ef-note"></p></div></section>'''
choices=''.join(f'<option value="{i}">{escape(x["name"])}</option>' for i,x in enumerate(interval))
cohort=f'''<section id="interval-discovery" class="evidence-feedback" aria-labelledby="interval-feedback-title" hidden><h2 id="interval-feedback-title">排除历史样本后，区间还在零线左侧吗？</h2><p>同113项来源替换，与排除后的50项子队列分开比较。点估计和95%区间均取自既有复算CSV。</p><div class="ef-controls"><label>选择核查情景<select id="interval-choice">{choices}</select></label></div><div role="status" aria-live="polite" aria-atomic="true"><p id="interval-result" class="ef-main"></p><p id="interval-reading"></p><p id="interval-boundary" class="ef-note ef-reading"></p></div><div id="interval-chart"></div><p class="ef-note">圆点：前后差；横线：按小项成组重抽样的95%区间；虚线：零差值。区间跨零不等于已经证明没有变化。<a href="固定队列三方案复算.csv">核对原始读数</a></p></section>'''
options=''.join(f'<option>{x}</option>' for x in sources)
labels=['RF/GB（60/40）','55%基准＋45%项目','随机森林 RF','梯度提升 GB']
modelopts=''.join(f'<option value="{m}">{l}</option>' for m,l in zip(models,labels))
buttons=''.join(f'<button type="button" data-feedback-year="{y}" aria-pressed="{str(y==2024).lower()}">{y}</button>' for y in [2012,2016,2024])
model=f'''<section id="model-discovery" class="evidence-feedback" aria-labelledby="model-feedback-title" hidden><h2 id="model-feedback-title">复杂模型在哪一届未胜过简单基准？</h2><p>先固定统计口径，再比较同一评分池的全体MAE。只采用“仅此前届次”的三折回放，不混入含目标届选择诊断。</p><div class="ef-controls"><label>统计口径<select id="model-source">{options}</select></label><label>比较模型<select id="model-choice">{modelopts}</select></label></div><p id="model-fails"></p><div class="ef-years" role="group" aria-label="选择回测届次">{buttons}</div><div role="status" aria-live="polite" aria-atomic="true"><p id="model-result" class="ef-main"></p><p id="model-reading"></p></div><div id="model-chart"></div><p class="ef-note">横向距离：模型MAE − 同口径基准MAE。零线左侧更小，右侧更大；横向尺度按当前口径全部候选模型固定，不同口径不可横比。</p><p class="ef-note ef-reading">“未胜出”仅指该口径、该届全体MAE大于同口径基准，不表示模型在所有代表团和指标上都失败。三折不是显著性检验；不得事后据此宣称权重最优。小项为历史代理/二次来源奖牌槽，仍非现行IOC全项认证。<a href="原模型五方案评分.csv">核对完整评分</a></p></section>'''

for folder,payload,markup,anchor in [
    (R,dict(kind='rank'),rank,'<main class="grid">'),
    (I,dict(kind='interval',rows=interval),cohort,'<img loading="lazy"'),
    (M,dict(kind='model',rows=rows,sources=sources,models=models,years=['2012','2016','2024']),model,'<img loading="lazy"')]:
    p=folder/'index.html';s=p.read_text(encoding='utf-8')
    s=re.sub(r'<!-- FEEDBACK_(?:UI|ASSETS)_START -->.*?<!-- FEEDBACK_(?:UI|ASSETS)_END -->','',s,flags=re.S)
    assert anchor in s,p
    s=s.replace(anchor,'<!-- FEEDBACK_UI_START -->'+markup+'<!-- FEEDBACK_UI_END -->'+anchor,1)
    rel=Path(os.path.relpath(SHARED,folder)).as_posix()
    assets=f'<!-- FEEDBACK_ASSETS_START --><link rel="stylesheet" href="{rel}/evidence-feedback.css"><script id="evidence-feedback-data" type="application/json">{json.dumps(payload,ensure_ascii=False)}</script><script src="{rel}/evidence-feedback.js"></script><!-- FEEDBACK_ASSETS_END -->'
    s=s.replace('</body>',assets+'</body>');p.write_text(s,encoding='utf-8')

out=BASE/'最终提交材料/关键交互反馈说明.md'
out.write_text('''# 三处关键交互反馈

- 奖牌口径实验室：沿用原控件与榜单数据，同步突出官方名次→当前名次、上升/后移位数及计数单位。焦点不在前N榜中时，仍显示独立案例读数。
- 冠军来源敏感性：切换原113项、同113项二次来源及排除后50项，区间与零线同步更新。明确跨零是证据不确定，不是证明无变化；排除改变样本。
- 原模型核验：切换三种口径、四种候选模型与三个届次，显示MAE相对同口径基准之差及未胜出届次。不混入含目标届筛选的诊断，不比较不同单位的误差。

数据直接取既有JSON/CSV，无重训，无新增结论或官方核验认证。筛选写入当前页URL，刷新恢复；原静态图表保留供无脚本阅读。反馈使用文字、数值和位置，颜色不独立承担结论。

复现：在页面发布脚本之后运行 `项目工作区/scripts/build_evidence_feedback.py`；`polish_evidence_figures.py`末尾已自动调用。此脚本不会改动报告PDF或源数据。
''',encoding='utf-8')
(BASE/'最终提交材料/关键交互反馈来源.json').write_text(json.dumps({'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs},'model_rows':len(rows),'interval_scenarios':len(interval),'refit':False},ensure_ascii=False,indent=2),encoding='utf-8')
print('Published three evidence feedback interactions (3 cohorts, 36 strict model scores).')
