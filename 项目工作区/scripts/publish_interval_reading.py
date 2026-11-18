from pathlib import Path
from bs4 import BeautifulSoup
from html import escape
import json,os
root=Path(__file__).resolve().parents[2];folder=root/'交付文件/任务二_百年全景/09_课程方法可视分析';source=folder/'2024代表团性别结构_区间数据.json';out=source.with_suffix('.html');rows=json.loads(source.read_text('utf8'))
template=root/'交付文件/任务一_数据体检/05_数据问题影响账本/数据问题影响账本.html';s=BeautifulSoup(template.read_text('utf8'),'html.parser');s.main.clear();s.body['class']=['supplement-reading','interval-data'];s.title.string='2024代表团性别结构｜区间数据'
for n in s.select('[href],[src]'):
 for attr in ['href','src']:
  v=n.get(attr,'')
  if not v or v.startswith(('http','#','data:')):continue
  file,sep,q=v.partition('?');n[attr]=Path(os.path.relpath(template.parent/file,folder)).as_posix()+(sep+q if sep else '')
for n in s.select('link[href*="impact-ledger.css"]'):n.decompose()
for a in s.select('#xz-nav .xz-links a'):
 a.attrs.pop('aria-current',None)
 if '任务二_百年全景/05_交互总览' in a.get('href',''):a['aria-current']='page'
fields=[('name','代表团'),('noc','代码'),('participants','参赛记录行'),('medals','获奖运动员行'),('female_medals','女性获奖行'),('participation','女性参赛占比（%）'),('award','女性获奖占比（%）'),('gap','份额差（百分点）'),('low','差距区间下限'),('high','差距区间上限')]
body='<article class="interval-reading"><nav class="method-actions"><a href="index.html">← 返回可视分析</a><a href="'+source.name+'" download>下载原始 JSON 数据</a></nav><p class="interval-kicker">2024 巴黎 / 运动员行口径</p><h1>参与与获奖，差距有多大？</h1><p>完整列出92个代表团的参与结构、获奖结构及差距区间。份额差＝女性获奖运动员行占比－女性参赛记录占比；区间上下限为获奖份额的 Wilson 95% 区间平移到差距轴，单位为百分点。</p><p>获奖行并非独立观测，同队多人获奖会产生相关性；区间仅作粗略阅读提示，不是严格推断或因果证据。记录行不等于独立运动员人数，也不是官方小项奖牌数。</p><label class="interval-search">查找代表团 <input id="interval-search" type="search" placeholder="输入中文名称或代码"><span id="interval-count" aria-live="polite">92 个代表团</span></label><div class="supp-table" role="region" tabindex="0" aria-label="完整区间数据，可横向查看"><table><thead><tr>'+''.join('<th>'+label+'</th>' for _,label in fields)+'</tr></thead><tbody>'
for r in rows:
 body+='<tr>'+''.join('<td>'+escape(str(r[key]))+'</td>' for key,_ in fields)+'</tr>'
body+='</tbody></table></div></article>'
s.main.append(BeautifulSoup(body,'html.parser'))
style=s.new_tag('style');style.string='.interval-reading h1{font-family:SimSun,serif!important;font-weight:400!important;font-size:clamp(32px,4vw,58px)!important;line-height:1.4!important}.interval-reading p{max-width:110ch}.interval-kicker{font-size:12px;color:var(--sr-accent)!important}.interval-search{display:flex;align-items:center;gap:16px;flex-wrap:wrap;margin:32px 0;font-size:14px}.interval-search input{background:transparent;color:var(--sr-ink);border:1px solid var(--sr-line);border-radius:10px;padding:12px;font:inherit;max-width:100%}.interval-reading table{min-width:1320px}.interval-reading td,.interval-reading th{white-space:nowrap;text-align:right!important;font-variant-numeric:tabular-nums}.interval-reading td:first-child,.interval-reading th:first-child{text-align:left!important}';s.head.append(style)
s.head.append(s.new_tag('link',rel='stylesheet',href='../../共享组件/interval-data.css'))
article=s.select_one('.interval-reading')
hero=s.new_tag('header',attrs={'class':'interval-task-hero'})
hero.append(BeautifulSoup('<p class="task-kicker">百年全景 · 2024 代表团性别结构</p><h1>参与之后，<br>谁留下成绩？</h1><p>在同一份记录中，比较参与份额、获奖份额与差距区间。</p><a href="../../任务三_专题深挖/媒体/图片来源与许可.html" class="interval-credit">奥运历史影像 · 来源与许可 ↗</a>','html.parser'))
s.main.insert_before(hero)
article.h1.string='代表团之间，差距有多大？'
article.select_one('.interval-kicker').decompose()

for tr in s.select('tbody tr'):
 tr['class']=['gap-positive' if float(tr.find_all('td')[7].text)>=0 else 'gap-negative']
script=s.new_tag('script');script.string="document.querySelector('#interval-search').addEventListener('input',e=>{const q=e.target.value.trim().toLowerCase();let count=0;document.querySelectorAll('tbody tr').forEach(r=>{r.hidden=![r.cells[0].textContent,r.cells[1].textContent].some(v=>v.toLowerCase().includes(q));if(!r.hidden)count++});document.querySelector('#interval-count').textContent=count+' 个代表团'})";s.body.append(script);out.write_text(str(s),'utf8')
p=folder/'index.html';doc=BeautifulSoup(p.read_text('utf8'),'html.parser')
for a in doc.select('a[href]'):
 if a.get('href')==source.name and not a.has_attr('download'):a['href']=out.name
p.write_text(str(doc),'utf8')
