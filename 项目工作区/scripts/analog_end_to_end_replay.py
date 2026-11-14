"""Full-formula ex-ante *analogue* replay for rugby's 2016 Olympic debut."""
from pathlib import Path
import numpy as np
import pandas as pd

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'交付文件'/'任务四_开放创作'/'05_满分升级'
OUT=BASE/'12_新增运动端到端类比回放'
OUT.mkdir(parents=True,exist_ok=True)
pool_info=pd.read_csv(BASE/'09_赛前条件回放'/'赛前条件与奖牌池.csv')
pool_row=pool_info[pool_info.Year.eq(2016)].iloc[0]
pool=float(pool_row['赛前估计奖牌池']);host_rate=float(pool_row['主场率_赛前估计'])
z=pd.read_csv(BASE/'09_赛前条件回放'/'赛前条件逐队回放.csv')
z=z[z.Year.eq(2016)]
actual=z[z.情景.eq('透明基线_赛前奖牌池')].set_index('NOC')['实际小项奖牌']
def vector(s):return z[z.情景.eq(s)].set_index('NOC')['预测小项奖牌'].reindex(actual.index).fillna(0)
b=vector('透明基线_赛前奖牌池')
core=vector('混合核心_赛前奖牌池')
# Reconstruct the held-out project prediction from the recorded .55/.45 core.
p=(core-.55*b)/.45
assert np.all(p>=-1e-8)
ranking=pd.read_csv(BASE/'10_新增运动历史快照回测'/'赛前排名快照与逐队结果.csv')
ranking=ranking[ranking['奥运届次'].eq(2016)].copy()
name={'Fiji':'FIJ','South Africa':'RSA','New Zealand':'NZL','Australia':'AUS','Canada':'CAN'}
ranking['NOC']=ranking['代表队'].map(name)
assert ranking.NOC.notna().all()
ranking['score']=1/ranking['赛前排名']
bonus=ranking.groupby('NOC')['score'].sum()
# Rugby brought two medal events in Rio. The LA28 model's 24-unit programme
# bonus is scaled to two event units, with the same 45/45/10 formula.
bonus=bonus/bonus.sum()*2
bonus=bonus.reindex(actual.index).fillna(0)
def predict(enable_rank):
    raw=.45*b+.45*p+.10*(b+(bonus if enable_rank else 0))
    if 'BRA' in raw.index:raw.loc['BRA']*=1+host_rate*.55
    return raw/raw.sum()*pool
off=predict(False);on=predict(True)
assert np.isclose(off.sum(),pool) and np.isclose(on.sum(),pool)
detail=pd.DataFrame({'NOC':actual.index,'实际奖牌':actual.values,'关闭赛前排名':off.values,
                     '加入赛前排名':on.values,'赛前排名奖励':bonus.values})
detail['关闭绝对误差']=(detail['关闭赛前排名']-detail['实际奖牌']).abs()
detail['加入绝对误差']=(detail['加入赛前排名']-detail['实际奖牌']).abs()
detail.to_csv(OUT/'2016逐队完整公式回放.csv',index=False,encoding='utf-8-sig')
def metric(v):
    a=actual.reindex(v.index)
    return {'全体MAE':float((v-a).abs().mean()),'实际至少5枚MAE':float((v[a.ge(5)]-a[a.ge(5)]).abs().mean()),
            'RMSE':float(np.sqrt(np.mean((v-a)**2))),
            '前十重合':len(set(v.nlargest(10).index)&set(a.nlargest(10).index))}
summary=pd.DataFrame([{'情景':'关闭排名',**metric(off)},{'情景':'加入赛前排名',**metric(on)}])
summary.to_csv(OUT/'2016端到端类比评分.csv',index=False,encoding='utf-8-sig')
delta=summary.iloc[1]['全体MAE']-summary.iloc[0]['全体MAE']
md=f'''# 2016新增运动：完整公式的赛前条件类比回放\n\n以七人制橄榄球2016首次入奥作为2028新增运动的**类比案例**。透明基线和项目模型来自此前已保存的2016滚动留出结果；奖牌池979.5枚由2004、2008、2012的走势外推；主场率只用此前主办案例，巴西身份赛前已知。新增运动排名只用2015–16赛季结束、里约开赛前已公布的 World Rugby 男、女世界系列赛前三名。为避免英格兰和英国奥运队的错误合并，仅使用可以直接映射的国家。\n\n2016新增七人制橄榄球有男、女两个奖牌小项，所以按2028公式把24单位新增项目奖励池缩至2单位，再执行**45%透明基线＋45%项目模型＋10%基线及新增排名奖励**；主场调整和总奖牌归一化与2028公式相同。\n\n| 情景 | 全体MAE | 实际至少5枚MAE | RMSE | 前十重合 |\n|---|---:|---:|---:|---:|\n'''
for r in summary.itertuples(index=False):md+=f'| {r.情景} | {r.全体MAE:.4f} | {r.实际至少5枚MAE:.4f} | {r.RMSE:.4f} | {r.前十重合}/10 |\n'
md+=f'''\n加入排名后的全体MAE变化 **{delta:+.4f}枚/队**。这检验了完整计算链在一个真实新增运动案例中能否按赛前奖牌池与排名运行；无论改善或变差，都如实报告。\n\n**不能外推的边界**：一届、两小项的七人制橄榄球无法代表2028五项不同运动；2016项目预测的训练数据仍以运动员行为输入，小项评价是代表团总量；赛前排名只有前三名可比，资格结构与2028不同。它是完整公式的历史类比回放，不是原样2028赛事的可识别历史反事实。复算：`python 项目工作区/scripts/analog_end_to_end_replay.py`。\n'''
(OUT/'方法与评分.md').write_text(md,encoding='utf-8')
tr=''.join(f'<tr><td>{r.情景}</td><td>{r.全体MAE:.4f}</td><td>{r.实际至少5枚MAE:.4f}</td><td>{r.RMSE:.4f}</td><td>{r.前十重合}/10</td></tr>' for r in summary.itertuples(index=False))
page=f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>2016新增运动类比回放</title><style>body{{margin:0;background:#f4f0e8;color:#173a44;font-family:"Microsoft YaHei",sans-serif}}main{{max-width:1050px;margin:auto;padding:6vw 24px 100px}}h1{{font-size:clamp(38px,6vw,76px);line-height:1.1;margin:20px 0}}p{{line-height:1.85;max-width:760px}}.lead{{font-size:20px}}.note{{background:#153e46;color:white;padding:26px;border-radius:22px;margin:28px 0}}.scroll{{overflow-x:auto}}table{{width:100%;border-collapse:collapse;background:white}}th,td{{padding:14px;text-align:left;border-bottom:1px solid #d9e1df}}a{{color:#126b78}}@media(max-width:600px){{th,td{{padding:9px;font-size:12px}}}}</style></head><body><main><small>百年圣火 / 赛前条件回放</small><h1>把时间拨回<br>里约开赛前。</h1><p class="lead">使用此前三届走势估计奖牌池，只用此前主办案例估计主场率，再加入World Rugby赛前排名，执行完整45/45/10计算链。</p><div class="scroll"><table><tr><th>情景</th><th>全体MAE</th><th>至少5枚MAE</th><th>RMSE</th><th>前十重合</th></tr>{tr}</table></div><div class="note">排名使全体MAE变化 {delta:+.4f} 枚/队，改善很小。这是一个真实新增运动的历史类比；2028五项运动没有同构的历史赛事。</div><p><a href="2016逐队完整公式回放.csv">逐队结果</a>　<a href="方法与评分.md">完整方法</a>　<a href="../11_官方来源门控预测/index.html">返回审慎预测</a></p></main></body></html>'''
(OUT/'index.html').write_text(page,encoding='utf-8')
print(summary.to_string(index=False))
