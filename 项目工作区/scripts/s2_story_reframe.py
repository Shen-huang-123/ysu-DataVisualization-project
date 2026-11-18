"""Place verified-2024 sensitivity before historical proxy cards in S2 story."""
from pathlib import Path
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力/06_滚动叙事专题/index.html'
s=BeautifulSoup(P.read_text(encoding='utf-8'),'html.parser')
history=s.find('section',id='history')
assert history
history.find(class_='kicker').string='03 · 历史代理探索'
history.find('h2').string='历史三届只用于内部口径探索'
history.find('p',class_='lede').string='2008、2012、2016的小项由运动员行按代表团—小项—奖牌类型去重生成，仍有555项缺现行一手逐项核验。下方三届数值展示数据内部结构，不证明现行官方奖牌榜跨届稳定。'
if not s.find('section',id='robustness2024'):
 block=BeautifulSoup('''<section id="robustness2024" style="padding:clamp(50px,8vw,110px) clamp(22px,5vw,72px);background:#f7f3eb;color:#172a30"><div class="kicker">02 · 官方2024稳健性</div><h2 class="title">剔除任一运动大类，关键重排仍在</h2><p class="lede">仅用2024官方329小项和同届运动员记录，逐次剔除35个运动大类。完整两榜 Kendall τ 为0.931；剔除后为0.908—0.938。西班牙、荷兰始终因行口径上升，日本、乌兹别克斯坦始终后移。</p><figure style="margin:2rem 0 0"><img src="../04_核心图表/S2_2024逐大类剔除稳健性.png" alt="2024官方小项与运动员行两口径的逐大类剔除敏感性" style="display:block;width:100%;height:auto;border-radius:20px"><figcaption style="margin-top:.8rem;font-size:.83rem;opacity:.7">35次试验只改变纳入的运动大类；历史代理数据不参与。</figcaption></figure></section>''','html.parser').section
 history.insert_before(block)
P.write_text(str(s),encoding='utf-8')
print(P)

import runpy
runpy.run_path(str(Path(__file__).with_name("publish_s2_robustness_chart.py")))
