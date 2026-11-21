"""Place the audited forecast and historical readouts beside the main evidence."""
from pathlib import Path
import re

import pandas as pd

ROOT = Path(__file__).resolve().parents[2] / '交付文件'
TASK4 = ROOT / '任务四_开放创作'
UPGRADE = TASK4 / '05_满分升级'
HISTORY = ROOT / '最终提交材料/证据等级与历史反例'
EVIDENCE = '任务三_专题深挖/S2_口径的魔力/08_逐项外部核验/IOC现行结果补证进度_20261121'
AUDIT = ROOT / EVIDENCE
MODELS = ['历史加权基线', '55基线45项目']

def replace_block(path, label, content, placement):
    text = path.read_text(encoding='utf-8')
    start, end = f'<!-- {label}_START -->', f'<!-- {label}_END -->'
    text = re.sub(re.escape(start)+r'.*?'+re.escape(end), '', text, flags=re.S)
    point = placement(text)
    block = start+content+end
    path.write_text(text[:point]+block+text[point:], encoding='utf-8')

metrics = pd.read_csv(UPGRADE/'15_原项目模型时序核验/原模型五方案评分.csv')
rows = metrics[(metrics.Year == 2024) & (metrics['来源'] == '小项二次来源')
               & (metrics['选择规则'] == '仅此前届次')].set_index('模型')
baseline, scenario = [rows.loc[model,'MAE'] for model in MODELS]
coverage = pd.read_csv(UPGRADE/'16_预测区间时序核验/逐届覆盖与宽度.csv')
row = coverage.loc[(coverage['评估届次'] == 2024) & (coverage['校准届次'] == '2012+2016+2020')
                   & coverage['模型'].eq(MODELS[0]) & coverage['评估分组'].eq('全体')
                   & coverage['区间方法'].eq('统一半宽')].iloc[0]
assert baseline < scenario and row['覆盖率'] < .8
pool = round(pd.read_csv(UPGRADE/'15_原项目模型时序核验/2028同口径重训情景榜.csv')[MODELS[0]].sum())
forecast = f"""
<aside aria-label="预测榜复核" style="border-block:1px solid currentColor;margin:1.2rem 0;padding:1rem 0">
<h3>主榜为什么用中性基准？</h3>
<ul>
<li><strong>{baseline:.3f} 对 {scenario:.3f} 槽/队。</strong> 巴黎 2024 小项二次来源留出，全体平均绝对误差。中性基准在这次对照中低于 55/45 情景。两列 2028 点估计使用同一个 {pool} 槽比较总池。</li>
<li><strong>{row['覆盖率']:.1%} 对名义 80%。</strong> 使用 2012、2016、2020 留出误差估计区间后，巴黎实测覆盖 {row['覆盖队数']}/{row['评分队数']} 队。2028 主榜发布点估计。<a href="../05_满分升级/16_预测区间时序核验/index.html">查逐届覆盖与逐队误差 ↗</a></li>
<li><strong>资格按小项核对。</strong> 已公布资格、主办席和待定席见<a href="../05_满分升级/18_LA28资格核验/index.html">十小项资格台账 ↗</a>。完整配方的历史类比覆盖里约七人制橄榄球和东京棒球。</li>
</ul></aside>
"""
place_forecast = lambda html: html.index('<details', html.index('id="project-reading-policy"'))
replace_block(TASK4/'02_2028洛杉矶预测/index.html','FORECAST_REVIEW',forecast,place_forecast)

cases = pd.read_csv(AUDIT/'优先分歧逐项复核.csv')
fin = cases.loc[(cases.Year == 2008) & cases['案例'].eq('女子飞碟多向')].iloc[0]
lon = cases.loc[(cases.Year == 2012) & cases['案例'].eq('男子单人划艇 200 米')].iloc[0]
ranks = pd.read_csv(AUDIT/'优先分歧名次复算.csv')
fin_rank = ranks.loc[(ranks.Year == 2008) & ranks.NOC.eq('FIN') & ranks['案例'].eq(fin['案例'])].iloc[0]
assert lon['名次变化数']==0
fin_text = f"北京 2008 女子飞碟多向。旧存档金牌空缺，ISSF 确认为芬兰金牌。固定其他小项，芬兰从第 {int(fin_rank['原排名'])} 升到第 {int(fin_rank['更新排名'])}，全榜有 {fin['名次变化数']} 队名次变化。"
lon_text = "伦敦 2012 男子单人划艇 200 米。旧存档银牌空缺、铜牌为俄罗斯，IOC 决定补正为俄罗斯银牌、西班牙铜牌。在同一旧存档起点下，奖牌数改变，按金银铜重排后名次不变。"
prefix = '../../'+EVIDENCE+'/'
boundary = '59 项有国际单项协会一手交叉证据。555 项优先清单内的 7 项旧存档与 Olympedia 分歧已逐项复核。910 项现行 IOC 全量核验仍待完成。'
history = f"""
<section aria-label="历史修订对名次的影响" style="border-block:1px solid currentColor;margin:1.4rem 0;padding:1rem 0">
<h3>补齐奖牌后，代表团名次变了吗？</h3>
<ul><li>{fin_text} <a href="{fin['来源']}">ISSF 结果</a></li>
<li>{lon_text} <a href="{lon['来源']}">IOC 递补决定</a></li></ul>
<p>{boundary}</p>
<p><a href="{prefix}优先分歧复核与复算.html">逐项原值、核对值与名次复算 ↗</a> · <a href="{prefix}优先分歧名次复算.csv" download>下载逐队结果 ↓</a></p>
</section>
"""
replace_block(HISTORY/'index.html','HISTORY_REVIEW',history,lambda html: html.index('<div aria-label="筛选差异类型"'))
md = f"""
## 旧存档分歧对名次的影响

- {fin_text} [ISSF 结果]({fin['来源']})
- {lon_text} [IOC 递补决定]({lon['来源']})

{boundary}

[逐项核对与复算]({prefix}优先分歧复核与复算.html) · [下载逐队结果]({prefix}优先分歧名次复算.csv)

以下旧实验采用历史代理榜作起点。两次排名复算起点不同，结果需分别阅读。男子举重 69 公斤级铜牌已另由 IOC 决定核实，见上方逐项明细。

"""
notes=HISTORY/'使用与复算说明.md'
replace_block(notes,'HISTORY_REVIEW',md,lambda html: html.index('## 局部排名敏感性'))
data = notes.read_text(encoding='utf-8')
data = data.replace('1项为原铜牌撤销而继任授牌未从IOC逐项决定确认','1项为原铜牌撤销后递补，IOC 已确认铜牌授予朝鲜')
data = data.replace('2012男子举重69公斤级只确认旧铜牌撤销，未把未经IOC逐项决定确认的新铜牌纳入确定性转授','这组旧实验只纳入2012男子举重69公斤级的旧铜牌撤销')
notes.write_text(data,encoding='utf-8')
