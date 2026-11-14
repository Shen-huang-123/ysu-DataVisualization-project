"""One-at-a-time counterfactual ablations of the published 2028 point forecast."""
from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from task2_localization import NOC_ZH

ROOT=Path(__file__).resolve().parents[2]
PRED=ROOT/'交付文件'/'任务四_开放创作'/'02_2028洛杉矶预测'
OUT=ROOT/'交付文件'/'任务四_开放创作'/'05_满分升级'/'07_模型消融与资格情景'
OUT.mkdir(parents=True,exist_ok=True)
d=pd.read_csv(PRED/'LA2028机器学习集成预测榜.csv').set_index('NOC')
base=d.forecast_total_neutral.astype(float)
ml=d.ml_project_forecast.astype(float)
bonus=d.new_sport_ranking_bonus.astype(float)
host_rate=float(d.synthetic_control_host_rate.iloc[0])
pool=float(d.ensemble_total.sum())
assert abs(base.sum()-pool)<1e-6 and abs(ml.sum()-pool)<1e-6
assert all(base.ge(0)) and all(ml.ge(0))

def normalize(raw):
    raw=raw.clip(lower=0)
    return raw/raw.sum()*pool
def apply_host(raw):
    out=raw.copy()
    if 'USA' in out.index:out.loc['USA']*=1+host_rate*.55
    return out
core=.55*base+.45*ml+.10*bonus
scenarios={
    '完整集成':normalize(apply_host(core)),
    '关闭项目模型':normalize(apply_host(base+.10*bonus)),
    '关闭新增运动排名':normalize(apply_host(.55*base+.45*ml)),
    '关闭主场调整':normalize(core),
    '仅透明基线':normalize(base),
}
eligibility=apply_host(core)
eligibility.loc[eligibility.index.intersection(['RUS','AIN'])]=0
scenarios['资格受限：RUS/AIN不参赛']=normalize(eligibility)

long=[]
for name,series in scenarios.items():
    rank=series.rank(method='min',ascending=False).astype(int)
    for noc,value in series.items():
        long.append({'NOC':noc,'代表团':NOC_ZH.get(noc,noc),'情景':name,'预测奖牌':float(value),
                     '名次':int(rank.loc[noc]),'相对完整集成变化':float(value-scenarios['完整集成'].loc[noc])})
table=pd.DataFrame(long)
table.to_csv(OUT/'逐代表团消融情景.csv',index=False,encoding='utf-8-sig')
full=scenarios['完整集成']
summary=[]
for name,series in scenarios.items():
    shift=(series-full).abs()
    summary.append({'情景':name,'总奖牌池':series.sum(),'全部代表团绝对变化合计':shift.sum(),
                    '最大单队变化':shift.max(),'最大变化代表团':NOC_ZH.get(shift.idxmax(),shift.idxmax()),
                    '前十重合':len(set(series.nlargest(10).index)&set(full.nlargest(10).index))})
summary=pd.DataFrame(summary)
summary.to_csv(OUT/'消融影响摘要.csv',index=False,encoding='utf-8-sig')
assert np.allclose(full.reindex(d.index).values,d.ensemble_total.values,atol=1e-6), 'Formula drift from published ensemble'

show=summary[~summary.情景.eq('完整集成')].copy()
plt.rcParams['font.sans-serif']=['Microsoft YaHei','SimHei','DejaVu Sans'];plt.rcParams['axes.unicode_minus']=False
fig,ax=plt.subplots(figsize=(10,5.8),facecolor='#f2eee5');ax.set_facecolor('#f2eee5')
ax.spines[['top','right','bottom','left']].set_visible(False)
bars=ax.barh(show.情景,show.全部代表团绝对变化合计,color=['#2c6c80','#aa6347','#bb8852','#577b75','#9d4a4a'])
ax.invert_yaxis();ax.grid(axis='x',color='#d7d6cc');ax.set_axisbelow(True);ax.tick_params(length=0)
ax.set_xlabel('相对完整集成，各代表团预测变化的绝对值之和（枚）')
for b,v in zip(bars,show.全部代表团绝对变化合计):ax.text(v+1,b.get_y()+b.get_height()/2,f'{v:.1f}',va='center')
ax.set_xlim(0,show.全部代表团绝对变化合计.max()*1.14)
fig.text(.09,.95,'2028榜单由哪些假设推着走？',fontsize=22,fontweight='bold',color='#173447')
fig.text(.09,.89,'一次只关闭一个组成部分；每次重新归一到相同奖牌池',fontsize=11,color='#59717a')
fig.text(.09,.025,'绝对变化合计并非新增奖牌数；固定奖牌池使一队上升伴随其他队下降。资格情景是条件模拟，不是参赛决定。',fontsize=9,color='#65777d')
fig.tight_layout(rect=[0,.05,1,.83]);fig.savefig(OUT/'模型组成影响.png',dpi=190,facecolor=fig.get_facecolor());plt.close(fig)

usa=table[table.NOC.eq('USA')][['情景','预测奖牌','相对完整集成变化']]
notop=table[table.情景.eq('完整集成')].nsmallest(10,'名次')
md='# 2028 预测：模型组成消融与资格情景\n\n'
md+='从已发布集成公式重算所有情景，并断言“完整集成”与正式预测榜逐队完全一致。每次只关闭一个组成部分，撤去的权重回到透明基线；每次均归一到相同奖牌池。相对完整模型的变化是**条件敏感度**，不是对未来成绩的因果贡献，各情景差值不能相加。\n\n'
md+='| 情景 | 全部代表团绝对变化合计 | 最大单队变化 | 前十重合 |\n|---|---:|---:|---:|\n'
for r in summary.itertuples():md+=f'| {r.情景} | {r.全部代表团绝对变化合计:.1f} 枚 | {r.最大变化代表团} {r.最大单队变化:.1f} 枚 | {r.前十重合}/10 |\n'
md+='\n## 美国主场情景切换\n\n'
for r in usa.itertuples():md+=f'- {r.情景}：{r.预测奖牌:.1f} 枚（相对完整集成 {r.相对完整集成变化:+.1f}）。\n'
md+='\n## 资格边界\n\n“RUS/AIN 不参赛”只是假设场景，将这两类代码的预测置零后按固定奖牌池重分配；不是对 2028 实际资格的判断。身份变化在2024历史回放中是重大误差来源，应以参赛资格最终决定更新情景。\n\n## 重要修正\n\n检查发现此前名为 `forecast_total_neutral` 的列误含早期美国+12枚主场假设，最终模型又施加合成对照收缩主场系数。现已把中性基线改为真正不含主场调整；旧的+12枚仅保留在可关闭的早期情景列。正式榜、消融表和站点已重建。\n\n公式、逐代表团情景与全表见本目录；运行 `python 项目工作区/scripts/task4_component_ablation.py` 可复算。\n'
(OUT/'消融分析说明.md').write_text(md,encoding='utf-8')
data=json.dumps(table[table.NOC.isin(notop.NOC)].to_dict('records'),ensure_ascii=False)
opts=''.join(f'<option>{x}</option>' for x in scenarios)
html=f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>2028模型消融｜百年圣火</title><style>body{{margin:0;background:#f2eee5;color:#173447;font-family:"Microsoft YaHei",sans-serif}}main{{max-width:1100px;margin:auto;padding:60px 24px 95px}}h1{{font-size:clamp(40px,7vw,78px);line-height:1.14}}p{{line-height:1.8}}img{{width:100%;border-radius:20px}}select{{font:inherit;padding:11px 18px;border-radius:12px;background:#fffaf1;border:1px solid #b9c3bd}}table{{width:100%;border-collapse:collapse;margin:20px 0;background:#fffaf2}}td,th{{padding:11px;border-bottom:1px solid #dad4c7;text-align:left}}.note{{background:#173e54;color:#fff;padding:26px;border-radius:20px}}a{{color:#277099}}@media(max-width:600px){{table{{font-size:13px}}td,th{{padding:7px}}}}</style></head><body><main><small>洛杉矶 2028 / 条件敏感度</small><h1>拿掉一个假设，<br>榜单会怎么变？</h1><p>逐一关闭项目模型、新增运动排名与主场调整，再观察所有代表团的点估计变化。资格限制另作情景，不代表实际参赛决定。</p><img src="模型组成影响.png" alt="各模型组成关闭后的预测变化"><h2>完整集成前十代表团的情景变化</h2><label>选择情景 <select id="scenario">{opts}</select></label><table><thead><tr><th>代表团</th><th>预测奖牌</th><th>名次</th><th>相对完整集成</th></tr></thead><tbody id="rows"></tbody></table><div class="note">所有情景固定总奖牌池；变化不能解释为新增奖牌数，也不能相加。中性基线已修正早期主场加成的重复计入。资格情景只用于检验风险边界。</div><p><a href="逐代表团消融情景.csv">下载完整逐队情景</a>　<a href="消融分析说明.md">方法与修正记录</a></p></main><script>const D={data};const s=document.querySelector('#scenario'),rows=document.querySelector('#rows');function draw(){{const a=D.filter(x=>x['情景']===s.value).sort((a,b)=>a['名次']-b['名次']);rows.innerHTML=a.map(x=>`<tr><td>${{x['代表团']}}</td><td>${{x['预测奖牌'].toFixed(1)}}</td><td>${{x['名次']}}</td><td>${{x['相对完整集成变化'].toFixed(1)}}</td></tr>`).join('')}}s.onchange=draw;draw()</script></body></html>'''
(OUT/'index.html').write_text(html,encoding='utf-8')
method=PRED/'预测方法与验证方案.md'
if method.exists():
    text=method.read_text(encoding='utf-8').split('\n\n### 模型组成消融')[0]
    text+='\n\n### 模型组成消融\n\n[查看逐项关闭项目模型、新增运动排名和主场调整后的榜单变化](../05_满分升级/07_模型消融与资格情景/index.html)。所有情景固定奖牌池，变化为条件敏感度，不是可相加的因果贡献。此前“中性基线”误含美国+12枚早期主场情景，现已修正；最终集成使用真正中性基线，主场调整只施加一次。\n'
    method.write_text(text,encoding='utf-8')
print(summary.to_string(index=False))

