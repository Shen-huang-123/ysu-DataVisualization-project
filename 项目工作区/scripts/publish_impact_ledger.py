from evidence_guard import presentation_html
from pathlib import Path
from bs4 import BeautifulSoup
from html import escape
import os,re
ROOT=Path(__file__).resolve().parents[2];delivery=ROOT/'交付文件'
folder=delivery/'任务一_数据体检/05_数据问题影响账本';source=folder/'数据问题影响账本.md';out=source.with_suffix('.html')
template=delivery/'任务二_百年全景/07_结论压力测试/结论压力测试_完整方法.html'
s=BeautifulSoup(template.read_text('utf8'),'html.parser');s.main.clear();s.title.string='数据问题影响账本｜完整方法与边界'
for n in s.select('[href],[src]'):
 for attr in ['href','src']:
  value=n.get(attr,'')
  if not value or value.startswith(('#','http','data:')):continue
  file,sep,query=value.partition('?');n[attr]=Path(os.path.relpath(template.parent/file,folder)).as_posix()+(sep+query if sep else '')
def inline(t):
 return re.sub(r'`([^`]+)`',r'<code>\1</code>',escape(t))
lines=source.read_text('utf-8-sig').splitlines();blocks=[];i=0
while i<len(lines):
 line=lines[i]
 if not line.strip():i+=1;continue
 if line.startswith('|'):
  table=[]
  while i<len(lines) and lines[i].startswith('|'):
   cells=[c.strip() for c in lines[i].strip('|').split('|')];i+=1
   if all(re.fullmatch(r':?-+:?',c) for c in cells):continue
   table.append(cells)
  blocks.append('<div class="supp-table" role="region" tabindex="0" aria-label="清洗决定影响数据表"><table><thead><tr>'+''.join('<th>'+inline(c)+'</th>' for c in table[0])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+inline(c)+'</td>' for c in row)+'</tr>' for row in table[1:])+'</tbody></table></div>');continue
 if line.startswith('- '):
  items=[]
  while i<len(lines) and lines[i].startswith('- '):items.append('<li>'+inline(lines[i][2:])+'</li>');i+=1
  blocks.append('<ul>'+''.join(items)+'</ul>');continue
 m=re.match(r'^(#{1,6}) (.*)',line)
 blocks.append(f'<h{len(m[1])}>{inline(m[2])}</h{len(m[1])}>' if m else '<p>'+inline(line)+'</p>');i+=1
content='<article class="method-reading"><nav class="method-actions"><a href="../index.html#research-closure">← 返回数据体检</a><a href="数据问题影响账本.md" download>下载 Markdown 原文</a><a href="问题影响实测.csv" download>下载影响实测 CSV</a></nav>'+''.join(blocks)+'</article>'
s.main.append(BeautifulSoup(content,'html.parser'))
s.body['class']=s.body.get('class',[])+['impact-ledger']
h=s.main.h1;h.string='清洗决定，究竟改变了什么？'
eyebrow=s.new_tag('p',attrs={'class':'ledger-eyebrow'});eyebrow.string='数据体检 / 数据问题影响账本';h.insert_before(eyebrow)
s.head.append(s.new_tag('link',rel='stylesheet',href='../../共享组件/impact-ledger.css?v=drifting-light'))

for a in s.select('#xz-nav .xz-links a'):
 a.attrs.pop('aria-current',None)
 if '任务一_数据体检/index.html' in a.get('href',''):a['aria-current']='page'
out.write_text(str(s),'utf8')
for p in presentation_html(delivery):
 if p==out:continue
 text=p.read_text('utf8')
 if '数据问题影响账本.md' not in text:continue
 doc=BeautifulSoup(text,'html.parser');changed=False
 for a in doc.select('a[href]'):
  if not a.has_attr('download') and a['href'].endswith('数据问题影响账本.md'):
   a['href']=a['href'][:-3]+'.html';changed=True
 if changed:p.write_text(str(doc),'utf8')
