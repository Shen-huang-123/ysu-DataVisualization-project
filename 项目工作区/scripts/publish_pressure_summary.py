"""Publish the JSON audit summary as an offline readable page; retain raw download."""
from pathlib import Path
from bs4 import BeautifulSoup
import json,html
ROOT=Path(__file__).resolve().parents[2]
folder=ROOT/'交付文件/任务二_百年全景/07_结论压力测试'
data=json.loads((folder/'结论压力测试摘要.json').read_text('utf-8-sig'))
labels={
'1896_top5_rows':'1896年前五代表团份额（运动员行）',
'2024_top5_rows':'2024年前五代表团份额（运动员行）',
'1904_top5_rows':'1904年前五代表团份额（运动员行）',
'2016_top5_rows':'2016年前五代表团份额（运动员行）',
'2016_top5_proxy':'2016年前五代表团份额（历史奖牌组代理）',
'2016_effective_nocs_rows':'2016年有效获奖代表团数（1/HHI）',
'2024_effective_nocs_rows':'2024年有效获奖代表团数（1/HHI）',
'2024_top5_no_duplicate_excess':'2024年删除重复余量后前五份额',
'modern_rows_spearman':'近期届次与前五份额的Spearman相关（运动员行）',
'modern_proxy_spearman':'近期届次与前五份额的Spearman相关（历史代理）',
'proxy_early_median':'1896—1936年前五份额中位数（历史代理）',
'proxy_modern_median':'1992—2016年前五份额中位数（历史代理）',
'rows_early_median':'1896—1936年前五份额中位数（运动员行）',
'rows_modern_median':'1992—2024年前五份额中位数（运动员行）'}
assert set(data)==set(labels)
rows=[]
for key,value in data.items():
 display=f'{value*100:.2f}%' if ('top5' in key or 'median' in key) else f'{value:.3f}'
 rows.append(f'<tr><th scope="row">{labels[key]}<br><code>{key}</code></th><td>{display}</td></tr>')
s=BeautifulSoup((folder/'结论压力测试_完整方法.html').read_text('utf-8'),'html.parser')
s.title.string='结论压力测试｜复算摘要'
content='<article class="method-reading"><nav class="method-actions" aria-label="摘要材料"><a href="结论压力测试.html">← 返回结论压力测试</a><a href="结论压力测试_完整方法.html">阅读完整方法 ↗</a><a href="结论压力测试摘要.json" download>下载原始 JSON ↓</a></nav><h1>奖牌更分散了吗？<br>复算摘要</h1><p>长期下降与近期回升可以同时存在。下列指标直接读取同目录复算摘要，不改变原始数据。</p><h2>先看三个检验</h2><p><strong>长期方向：</strong>运动员行口径的早期前五份额中位数为64.8%，1992—2024年为40.4%；历史奖牌组代理也呈长期下降。</p><p><strong>近期反例：</strong>2016至2024年前五份额由39.3%回升至41.8%，有效获奖代表团数由21.1降至18.9。两届波动不能直接推断为长期逆转。</p><p><strong>清洗敏感性：</strong>删除重复余量后，2024年前五份额仅变化约0.018个百分点。</p><h2>全部复算指标</h2><p>份额换算为百分比展示；原始精度保留在JSON下载中。相关系数为描述性指标，不代表因果或显著性结论。</p><div class="supp-table"><table><thead><tr><th scope="col">指标与原始字段</th><th scope="col">复算值</th></tr></thead><tbody>'+''.join(rows)+'</tbody></table></div><h2>证据边界</h2><p>历史奖牌组代理不是IOC官方小项奖牌表。2020年起Event字段泛化，代理序列停于2016年，不能与2024年运动员行硬接。有效获奖代表团数是1/HHI，与实际获奖代表团数量不同。这里描述分布变化，不识别单一因果机制。</p><p><a href="逐届集中度三口径.csv" download>下载逐届数据 CSV ↓</a></p></article>'
s.main.clear();s.main.append(BeautifulSoup(content,'html.parser'))
s.body['class']=list(dict.fromkeys(s.body.get('class',[])+['pressure-summary']))
h=s.main.h1;h.string='奖牌更分散了吗？'
eyebrow=s.new_tag('p',attrs={'class':'summary-kicker'});eyebrow.string='百年全景 / 结论压力测试 · 复算摘要';h.insert_before(eyebrow)
first=s.main.find('h2');checks=s.new_tag('section',attrs={'class':'summary-checks','aria-label':'三个检验'})
for para in list(first.find_next_siblings('p',limit=3)):
 checks.append(para.extract())
first.insert_after(checks)
if not s.select_one('#pressure-summary-css'):s.head.append(s.new_tag('link',id='pressure-summary-css',rel='stylesheet',href='../../共享组件/pressure-summary.css'))
(folder/'结论压力测试摘要.html').write_text(str(s),'utf-8')
for page in (ROOT/'交付文件').rglob('*.html'):
 text=page.read_text('utf-8');doc=BeautifulSoup(text,'html.parser');changed=False
 for a in doc.select('a[href]'):
  href=a['href']
  if not a.has_attr('download') and href.endswith('结论压力测试摘要.json') and (page.parent/href).resolve()==(folder/'结论压力测试摘要.json').resolve():
   a['href']=href[:-5]+'.html';changed=True
 if changed:page.write_text(str(doc),'utf-8')
print('Pressure summary reading page ready')
