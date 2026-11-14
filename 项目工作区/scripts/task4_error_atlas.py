"""Explain where the historical forecast blend wins and fails, without causal overclaim."""
from pathlib import Path
import pandas as pd
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'交付文件'/'任务四_开放创作'/'05_满分升级'
d=pd.read_csv(OUT/'滚动留出逐队同口径结果.csv')
d['baseline_abs_error']=(d.actual-d.baseline).abs()
d['blend_abs_error']=(d.actual-d.blend).abs()
d['gain_from_blend']=d.baseline_abs_error-d.blend_abs_error
d['project_minus_baseline']=d.project-d.baseline
d['error_direction']=np.where(d.blend>d.actual,'高估',np.where(d.blend<d.actual,'低估','吻合'))

# 2024 year-specific row-to-event multiplier, a descriptive structural diagnostic.
raw=pd.read_csv(ROOT/'项目工作区'/'outputs'/'olympics_flagged.csv.gz',low_memory=False)
rows24=raw[raw.Year.eq(2024)&raw.is_medal.eq(True)].groupby('NOC').size().rename('athlete_medal_rows')
d['athlete_medal_rows_2024']=np.where(d.Year.eq(2024),d.NOC.map(rows24),np.nan)
d['rows_per_event_2024']=np.where(d.Year.eq(2024)&d.actual.gt(0),d.athlete_medal_rows_2024/d.actual,np.nan)
d['identity_regime_flag']=d.NOC.isin(['RUS','ROC','BLR','AIN'])&d.Year.eq(2024)
d.to_csv(OUT/'回测误差逐队机制线索.csv',index=False,encoding='utf-8-sig')

summary=d.groupby('Year').apply(lambda z:pd.Series({
    'representatives':len(z),'blend_better':int((z.gain_from_blend>.1).sum()),
    'blend_worse':int((z.gain_from_blend<-.1).sum()),
    'close':int((z.gain_from_blend.abs()<=.1).sum()),
    'baseline_mae':z.baseline_abs_error.mean(),'blend_mae':z.blend_abs_error.mean()}),include_groups=False).reset_index()
summary.to_csv(OUT/'回测误差分布摘要.csv',index=False,encoding='utf-8-sig')
z=d[d.Year.eq(2024)]
clean=z[~z.identity_regime_flag]
clean_base=float(clean.baseline_abs_error.mean());clean_blend=float(clean.blend_abs_error.mean())

def table(frame):
    return ''.join(f'<tr><td>{r.NOC}</td><td>{r.actual:.0f}</td><td>{r.baseline:.1f}</td><td>{r.blend:.1f}</td><td>{r.gain_from_blend:+.1f}</td></tr>' for r in frame.itertuples())
worst=z.nsmallest(8,'gain_from_blend');best=z.nlargest(8,'gain_from_blend')
md=f'''# 预测误差图谱：模型何时帮忙，何时添乱

误差改善定义为 `|实际−透明基线| − |实际−混合预测|`；正数表示混合模型更接近实际。评估单位统一为代表团小项奖牌总量：2012/2016 为历史 Event 代理，2024 为官方小项结果。

| 届次 | 混合更准 | 混合更差 | 近似不变 | 基线 MAE | 混合 MAE |
|---|---:|---:|---:|---:|---:|
'''
for r in summary.itertuples():md+=f'| {r.Year} | {int(r.blend_better)} | {int(r.blend_worse)} | {int(r.close)} | {r.baseline_mae:.2f} | {r.blend_mae:.2f} |\n'
md+=f'''
## 2024 身份边界压力测试

RUS 的透明基线预测约 68.0 枚、混合预测 43.1 枚；ROC 的基线为 0、混合预测 18.6 枚；官方 2024 的 AIN 获得 5 枚。三种代码不能自动视为同一国家队。排除 RUS、ROC、BLR、AIN 四个身份制度敏感代码后，其余代表团的 MAE 为基线 **{clean_base:.2f}**、混合 **{clean_blend:.2f}** 枚；混合模型的小幅优势仍在，但比全样本差异更有限。此处排除法只用于敏感度分析，不用于正式预测评分。

## 2024 团队人数线索

西班牙官方小项奖牌为 18 枚，源表有 83 条获奖运动员行（4.61 行/枚）；混合模型预测约 24.4 枚，高于实际。荷兰为 34 枚、118 行（3.47 行/枚）。行数与小项数的转换差异可造成项目级模型与官方榜之间的错位；**不能仅凭这个比值证明某个具体残差由团队规模导致**。

## 下一轮模型决定

正式展示保留透明基线和混合预测双列；对于身份资格未决代表团，展示情景而非单个确定名次。新增项目排名与主场调整没有可同构回放的历史信号，不把此误差图谱称为完整 2028 模型的因果诊断。逐队表：`回测误差逐队机制线索.csv`。
'''
(OUT/'预测误差机制分析.md').write_text(md,encoding='utf-8')
html=f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>预测误差图谱｜百年圣火</title><style>*{{box-sizing:border-box}}body{{margin:0;background:#eee9df;color:#162b42;font-family:"Microsoft YaHei",sans-serif}}main{{max-width:1120px;margin:auto;padding:64px 24px 100px}}small{{color:#ad563f;letter-spacing:.18em}}h1{{font-size:clamp(42px,7vw,80px);line-height:1.13;margin:18px 0 26px}}h2{{font-size:27px}}p{{line-height:1.8}}.lead{{font-size:19px;max-width:850px}}.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:32px 0}}.card{{background:#fffaf2;padding:22px;border-radius:22px;border:1px solid #ded4c4}}.card b{{display:block;font:700 45px Georgia;color:#154675}}table{{width:100%;border-collapse:collapse;background:#fffaf2;border-radius:18px;overflow:hidden}}td,th{{padding:12px;text-align:left;border-bottom:1px solid #ddd1c0}}.pair{{display:grid;grid-template-columns:1fr 1fr;gap:24px}}.dark{{background:#173954;color:#fff;padding:28px;border-radius:22px;margin:28px 0}}.dark p{{color:#e6e9e9}}a{{color:#2266a5}}@media(max-width:800px){{.grid,.pair{{grid-template-columns:1fr}}}}@media(max-width:500px){{table{{font-size:12px}}td,th{{padding:7px}}}}</style></head><body><main><small>2028 预测 / 历史误差</small><h1>模型什么时候<br>帮忙，什么时候添乱？</h1><p class="lead">复杂模型并不总赢。逐队误差使“平均更准”背后的受益者、受损者和身份边界都能看见。</p><div class="grid">{''.join(f'<div class="card"><small>{int(r.Year)} 留出届次</small><b>{int(r.blend_better)} / {int(r.blend_worse)}</b><p>代表团混合模型更准 / 更差；平均误差 {r.baseline_mae:.2f} → {r.blend_mae:.2f} 枚。</p></div>' for r in summary.itertuples())}</div><div class="pair"><section><h2>2024：混合模型更差的代表团</h2><table><tr><th>代码</th><th>实际</th><th>基线</th><th>混合</th><th>改善</th></tr>{table(worst)}</table></section><section><h2>2024：混合模型更准的代表团</h2><table><tr><th>代码</th><th>实际</th><th>基线</th><th>混合</th><th>改善</th></tr>{table(best)}</table></section></div><div class="dark"><h2>最大问题之一：代表团身份变了</h2><p>2024 年 RUS 基线约 68.0 枚、混合约 43.1 枚，ROC 混合约 18.6 枚；实际 AIN 获 5 枚。代码无法自动拼接。排除四个身份敏感代码后，其余代表团 MAE 为基线 {clean_base:.2f}、混合 {clean_blend:.2f} 枚。排除法仅检验敏感度，正式评分仍纳入全部代表团。</p></div><p>团队人数也是线索：2024 西班牙 18 枚官方小项奖牌对应 83 条获奖运动员行。这个结构可能影响行模型转成官方奖牌的过程，但单个残差的成因不能由一个比值证明。</p><p><a href="回测误差逐队机制线索.csv">下载逐队误差和结构线索</a>　<a href="滚动留出验证.html">返回滚动回放</a></p></main></body></html>'''
(OUT/'预测误差图谱.html').write_text(html,encoding='utf-8')
method=ROOT/'交付文件'/'任务四_开放创作'/'02_2028洛杉矶预测'/'预测方法与验证方案.md'
if method.exists():
    text=method.read_text(encoding='utf-8').split('\n\n### 逐队误差图谱')[0]
    text+='\n\n### 逐队误差图谱\n\n[查看2012／2016／2024逐队误差与机制线索](../05_满分升级/预测误差图谱.html)。2024年排除RUS、ROC、BLR、AIN四个身份制度敏感代码后，透明基线与混合模型MAE分别为2.30与2.18枚；该排除仅作敏感度分析，正式评分仍包含全部代表团。运动员行与官方小项奖牌的倍率差是潜在误差机制，不能单凭倍率证明个别代表团残差的因果来源。\n'
    method.write_text(text,encoding='utf-8')
print(summary.to_string(index=False));print('2024_excluding_identity',round(clean_base,3),round(clean_blend,3))
