"""Publish the authored replay method as UTF-8 HTML; retain Markdown downloads."""
from evidence_guard import presentation_html
from pathlib import Path
import html,re,runpy
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[2]
folder=root/'交付文件/任务四_开放创作/05_满分升级/14_同口径时序重训'
source=folder/'同口径时序重训说明.md'
target=source.with_suffix('.html')
def inline(s):
 s=html.escape(s)
 s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
 s=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',s)
 s=re.sub(r'!\[([^]]*)\]\(([^)]+)\)',r'<img alt="\1" src="\2">',s)
 return re.sub(r'\[([^]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',s)
blocks=[]
for part in re.split(r'\n\s*\n',source.read_text(encoding='utf-8-sig').strip()):
 lines=part.splitlines()
 if lines[0].startswith('|') and len(lines)>1 and re.match(r'^\|[ :|\-]+\|$',lines[1]):
  rows=[[c.strip() for c in line.strip().strip('|').split('|')] for line in lines]
  blocks.append('<div class="method-table" tabindex="0" role="region" aria-label="重训结果表，可横向滚动"><table><thead><tr>'+''.join('<th>'+inline(c)+'</th>' for c in rows[0])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+inline(c)+'</td>' for c in row)+'</tr>' for row in rows[2:])+'</tbody></table></div>')
 else:
  heading=re.match(r'^(#{1,6}) (.*)$',part)
  if heading:
   n=len(heading[1]);blocks.append(f'<h{n}>'+inline(heading[2])+f'</h{n}>')
  else:blocks.append('<p>'+inline(part)+'</p>')
target.write_text('<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>同口径时序重训｜方法与限制</title><style>html body main:has(>article.method-reading){box-sizing:border-box;width:100%!important;max-width:none!important;padding-inline:clamp(16px,6vw,120px)!important}html body article.method-reading{width:100%;max-width:none!important;margin:0}html body article.method-reading > h1{font-size:clamp(28px,3.6vw,56px)!important;line-height:1.18!important;margin:0 0 20px!important;text-wrap:balance}.method-reading h2{margin-top:clamp(28px,4vw,48px)}html body article.method-reading p{max-width:none!important;line-height:1.9}.method-reading .method-table{max-width:100%;overflow-x:auto}.method-reading .method-table table{width:100%!important}.method-reading code{overflow-wrap:anywhere}.method-reading img{max-width:100%}.method-actions{display:flex;gap:24px;flex-wrap:wrap;margin-bottom:36px}.method-reading table{white-space:nowrap}</style></head><body><main><article class="method-reading"><nav class="method-actions"><a href="index.html">← 返回同口径时序重训</a><a href="同口径时序重训说明.md" download>下载 Markdown 原文</a></nav>'+''.join(blocks)+'</article></main></body></html>',encoding='utf-8')
for page in presentation_html(root/'交付文件'):
 if '原始页面' in str(page) or page==target:continue
 text=page.read_text(encoding='utf-8')
 if source.name not in text:continue
 doc=BeautifulSoup(text,'html.parser');changed=False
 for a in doc.select('a[href]'):
  href=a['href']
  if not a.has_attr('download') and href.endswith(source.name) and (page.parent/href).resolve()==source.resolve():
   a['href']=href[:-3]+'.html';changed=True
 if changed:page.write_text(str(doc),encoding='utf-8')
runpy.run_path(str(Path(__file__).with_name('publish_supplement_reading.py')))
