from evidence_guard import presentation_html
from pathlib import Path
from bs4 import BeautifulSoup
from html import escape
import os,re
ROOT=Path(__file__).resolve().parents[2];delivery=ROOT/'交付文件'
folder=delivery/'任务三_专题深挖/S2_口径的魔力/08_逐项外部核验/未决证据三方案敏感性';source=folder/'未决证据影响报告.md';out=source.with_suffix('.html')
template=delivery/'任务二_百年全景/07_结论压力测试/结论压力测试_完整方法.html'
s=BeautifulSoup(template.read_text('utf8'),'html.parser');s.main.clear();s.title.string='未决证据影响报告｜三方案敏感性'
for n in s.select('[href],[src]'):
 for attr in ['href','src']:
  value=n.get(attr,'')
  if not value or value.startswith(('#','http','data:')):continue
  file,sep,query=value.partition('?');n[attr]=Path(os.path.relpath(template.parent/file,folder)).as_posix()+(sep+query if sep else '')
def inline(t):
 t=escape(t)
 t=re.sub(r'`([^`]+)`',r'<code>\1</code>',t)
 t=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',t)
 return re.sub(r'\[([^]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',t)
lines=source.read_text('utf-8-sig').splitlines();blocks=[];i=0
while i<len(lines):
 line=lines[i]
 if not line.strip() or line.startswith('<!--'):i+=1;continue
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
content='<article class="method-reading"><nav class="method-actions"><a href="../../../三篇旗舰专题_研究闭环.html">← 返回研究闭环</a><a href="未决证据影响报告.md" download>下载 Markdown 原文 ↓</a></nav><p class="flagship-kicker">口径的魔力 / 历史证据 · 三方案敏感性</p>'+''.join(blocks)+'</article>'
s.main.append(BeautifulSoup(content,'html.parser'))
for cell in s.main.select('th,td'):
 if cell.get_text(strip=True)=='Year':cell.string='年份'
 elif cell.get_text(strip=True)=='True':cell.string='是'
 elif cell.get_text(strip=True)=='False':cell.string='否'
for table in s.main.select('.supp-table'):
 table['aria-label']='三方案敏感性复算数据表'
s.body['class']=s.body.get('class',[])+['flagship-reading','uncertainty-reading']
s.head.append(s.new_tag('link',rel='stylesheet',href='../../../../共享组件/flagship-reading.css?v=uncertainty-background-1'))
for a in s.select('#xz-nav .xz-links a'):
 a.attrs.pop('aria-current',None)
 if '任务三_专题深挖/统一中文入口/index.html' in a.get('href',''):a['aria-current']='page'
downloads=s.new_tag('nav',attrs={'class':'method-actions','aria-label':'复算文件下载'})
for filename in ['三方案逐代表团奖牌与名次.csv','替代来源差异逐奖牌清单.csv','输入哈希与检查.json']:
 a=s.new_tag('a',href=filename,attrs={'download':''});a.string='下载 '+filename;downloads.append(a)
s.main.article.append(downloads)
out.write_text(str(s),'utf8')
for p in presentation_html(delivery):
 if p==out:continue
 text=p.read_text('utf8')
 if '未决证据影响报告.md' not in text:continue
 doc=BeautifulSoup(text,'html.parser');changed=False
 for a in doc.select('a[href]'):
  if not a.has_attr('download') and a['href'].endswith('未决证据影响报告.md'):
   a['href']=a['href'][:-3]+'.html';changed=True
 if changed:p.write_text(str(doc),'utf8')
