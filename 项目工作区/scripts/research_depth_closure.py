"""Recompute issue impacts and paired forecast ablations without changing source data."""
from pathlib import Path
import hashlib
import json
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / '交付文件'
T1 = D / '任务一_数据体检'
T3 = D / '任务三_专题深挖'
T4 = D / '任务四_开放创作'
inputs = []

def read(path):
    inputs.append(path)
    return pd.read_csv(path, low_memory=False)

def save(frame, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(path, index=False, encoding='utf-8-sig')

def mdtable(frame):
    def fmt(x):
        return f'{x:.4f}' if isinstance(x, (float, np.floating)) else str(x)
    return '| ' + ' | '.join(frame.columns) + ' |\n|' + '|'.join(['---'] * len(frame.columns)) + '|\n' + '\n'.join('| ' + ' | '.join(fmt(x) for x in row) + ' |' for row in frame.itertuples(index=False, name=None))

raw = read(T1 / '02_交付数据/归一数据_保留原始字段.csv.gz')
assert {'include_main', 'duplicate_excess', 'sport_family', 'event_status'} <= set(raw)
main = raw[raw.Year.ne(1906)].copy()
medals = ['Gold', 'Silver', 'Bronze']

def metrics(frame):
    m = frame[frame.Medal.isin(medals)]
    return {'参赛记录行': len(frame), '获奖记录行': len(m), '女性参赛行占比%': frame.Sex.eq('F').mean()*100,
            '女性获奖行占比%': m.Sex.eq('F').mean()*100}

rows = []
for name, before, after in [('排除1906', raw, main), ('疑似重复超额行剔除敏感性', main, main[~main.duplicate_excess.astype(str).str.lower().eq('true')])]:
    a, b = metrics(before), metrics(after)
    for key in a:
        rows.append({'问题': name, '指标': key, '处理前': a[key], '处理后': b[key], '变化_后减前': b[key]-a[key]})
impact = pd.DataFrame(rows)
out1 = T1 / '05_数据问题影响账本'
save(impact, out1/'问题影响实测.csv')
dedup = main[~main.duplicate_excess.astype(str).str.lower().eq('true')]
editions = []
for year, a in main.groupby('Year'):
    b = dedup[dedup.Year.eq(year)]
    ra = a[a.Medal.eq('Gold')].groupby('NOC').size()
    rb = b[b.Medal.eq('Gold')].groupby('NOC').size().reindex(ra.index, fill_value=0)
    shifts = (ra.rank(method='min', ascending=False)-rb.rank(method='min', ascending=False)).abs()
    editions.append({'Year':year,'剔除行数':len(a)-len(b),'金牌行榜名次变化代表团数':int(shifts.gt(0).sum()),'最大名次变化':float(shifts.max())})
save(pd.DataFrame(editions), out1/'重复敏感性逐届名次.csv')
sport_before, sport_after = main.Sport.nunique(), main.sport_family.nunique()
generic = int(main.event_status.eq('generic_or_context_required').sum())
text = '# 数据问题影响账本：清洗决定究竟改变了什么？\n\n'
text += '复算直接读取保留原始字段的归一表；不覆盖原表。数量为记录行，占比变化为百分点。疑似重复不是已证实错误，剔除仅为敏感性情景。\n\n'+mdtable(impact)+'\n\n'
text += f'## 哪些改变统计值，哪些改变可回答的问题？\n\n- 项目归一：主分析原始 Sport 有 {sport_before} 个标签，归一为 {sport_after} 个家族；不删除任何记录。分类合并改变项目归属和组内份额，不能解释成项目数量真实减少。\n- Event 泛化：主分析 {generic} 行需要上下文。将它们删掉会改变研究总体，因此保留记录，停止从这些标签推导正式小项数；2024正式小项采用独立官方表。\n- 身份警报：编号多姓名不等于全部错人；不强行修复身份，不发布未经核验的独立运动员历史榜。\n- 1956双城：合并为同一届但保留城市字段；全表行数不变，避免把一届重复计入时间轴。\n- 历史代表团：保持代码身份，缺席不补成已观察的零成绩；不能把身份变化当作连续同一国家。\n\n'
text += '## 可以与不可以据此宣称什么\n\n问题影响实测表回答总量及女性份额是否变动；逐届表另外检查疑似重复剔除对金牌行榜的名次影响。它们不验证主场因果结论，也不把行榜转成官方榜。项目归一与身份问题尚未形成全套替代映射的结论重算，不能宣称全部下游结论均已通过。\n\n复算：`py 项目工作区/scripts/research_depth_closure.py`。\n'
(out1/'数据问题影响账本.md').write_text(text, encoding='utf-8')

# Pair every scenario on exactly the same NOCs within each held-out edition.
source = read(T4/'05_满分升级/09_赛前条件回放/赛前条件逐队回放.csv')
scenarios = ['透明基线_赛前奖牌池','混合核心_赛前奖牌池','混合核心_加主场','混合核心_资格受限']
scores, paired = [], []
for year, g in source.groupby('Year'):
    assert not g.duplicated(['NOC','情景']).any()
    sets = [set(g[g.情景.eq(s)].NOC) for s in scenarios]
    assert all(x == sets[0] for x in sets)
    actuals = g.pivot(index='NOC', columns='情景', values='实际小项奖牌')
    assert actuals.nunique(axis=1).eq(1).all()
    actual = actuals.iloc[:,0]
    pred = g.pivot(index='NOC', columns='情景', values='预测小项奖牌')
    assert np.allclose(pred.sum().values, pred.sum().iloc[0])
    baseline_error = (pred[scenarios[0]]-actual).abs()
    previous = None
    for s in scenarios:
        error = (pred[s]-actual).abs()
        scores.append({'Year':year,'阶段':s,'代表团数':len(actual),'MAE':error.mean(),'至少5枚MAE':error[actual.ge(5)].mean(),
                       'RMSE':np.sqrt(((pred[s]-actual)**2).mean()),'相对基线MAE变化':error.mean()-baseline_error.mean(),
                       '相对上阶段MAE变化':0.0 if previous is None else error.mean()-previous.mean(),
                       '较基线改善队数':int((error < baseline_error-1e-9).sum()),'较基线恶化队数':int((error > baseline_error+1e-9).sum())})
        for noc in actual.index:
            paired.append({'Year':year,'NOC':noc,'阶段':s,'实际':actual.loc[noc],'预测':pred.loc[noc,s],
                           '绝对误差':error.loc[noc],'相对基线误差变化':error.loc[noc]-baseline_error.loc[noc]})
        previous = error
out4 = T4/'05_满分升级/13_统一条件消融总表'
scores = pd.DataFrame(scores)
save(scores, out4/'统一条件消融评分.csv')
save(pd.DataFrame(paired), out4/'逐队配对误差.csv')
report = '# 模型增加复杂度，究竟换来了多少预测收益？\n\n'
report += '本表从既有赛前条件逐队回放重新评分，不重新训练模型，不选择更有利的参数。每届四阶段使用完全相同代表团集合、实际值和赛前估计奖牌池；误差越低越好，负的MAE变化表示改善。2012、2016实际为历史小项代理，2024为官方小项奖牌。不同届次保留各自证据等级，不合成一个掩盖差异的总分。\n\n'
report += mdtable(scores)+'\n\n'
report += '## 如何读这张消融表\n\n1. 基线→混合核心：检验以45%项目模型替换对应基线后的增量。\n2. 混合核心→加主场：检验收缩主场情景后的增量。\n3. 加主场→资格受限：仅是排除预设身份代码的压力情景；不是当年已知资格策略，不能把它的改善当成可部署预测能力。\n4. 新增排名：三届表缺统一可比赛前快照，不能填0分冒充检验；独立2016橄榄球类比回放的MAE为2.1698→2.1691，增益仅0.0007枚/队，不并入三届主表。\n\n'
report += '## 对预测主张的约束\n\n只有逐届对照支持的阶段才可称在该届改善；不能宣称集成必然优于基线。2028的45/45/10权重和收缩系数仍是设定，未由此表证明最优。主场率三届均触及18%上限，检验的主要是固定上限情景。上游模型输出分布来自既有滚动留出；本次只保证重新评分配对与奖牌池条件一致，没有新增训练泄漏全链审计。历史残差区间也不能转称最终集成已校准区间。\n\n'
report += '建议展示透明基线和来源门控审慎榜并列，以敏感性和误差解释支撑预测，暂不以“算法更复杂所以更准确”为卖点。\n\n复算：`py 项目工作区/scripts/research_depth_closure.py`。\n'
(out4/'统一条件消融结论.md').write_text(report, encoding='utf-8')

manifest = {'inputs': [{'path':str(p.relative_to(ROOT)), 'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in inputs],
            'checks':['同届同代表团集合','同届实际值一致','同届奖牌池一致','无逐队重复','归一数据字段存在'],
            'forecast_rows':len(paired),'issue_metrics':len(impact)}
(out4/'复算输入与检查.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
print(impact.to_string(index=False))
print(scores.to_string(index=False))

# Publish the ledger as a themed UTF-8 reading page after data generation.
import runpy
runpy.run_path(str(Path(__file__).with_name("publish_impact_ledger.py")))
