from pathlib import Path
from bs4 import BeautifulSoup
import html,re
root=Path(__file__).resolve().parents[2]
p=root/'交付文件/任务二_百年全景/07_结论压力测试/结论压力测试.html'
s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
if not s.select_one('#pressure-reading-style'):
 link=s.new_tag('link',id='pressure-reading-style',rel='stylesheet',href='pressure-reading.css?v=1');s.head.append(link)
if not s.select_one('.pressure-photo-credit'):
 credit=s.new_tag('a',attrs={'class':'pressure-photo-credit','href':'../../任务三_专题深挖/媒体/图片来源与许可.html'})
 credit.string='1896 雅典 · 历史影像 / Public domain'
 s.header.append(credit)
main=s.main
sections=main.find_all('section',recursive=False)
for i,n in enumerate(sections):n['id']='pressure-'+str(i+1)
if not s.select_one('.pressure-route'):
 nav=s.new_tag('nav',attrs={'class':'pressure-route','aria-label':'压力测试阅读路径'})
 for i,label in enumerate(['长期与近期','替换单位','清洗决定','证据边界']):
  a=s.new_tag('a',href='#pressure-'+str(i+1));a.string=label;nav.append(a)
 main.insert(0,nav)
 facts=s.select_one('.facts');facts.extract();nav.insert_after(facts)
 figure=main.figure
 caption=s.new_tag('figcaption');caption.string='阅读提示：先比较长期水平，再检查最近两届的反向波动。运动员行与历史奖牌组代理分别阅读；代理线停于2016年，不与2020后的泛化Event硬接。完整数值见逐届CSV。';figure.append(caption)
 downloads=s.new_tag('nav',attrs={'class':'pressure-downloads','aria-label':'复算材料'})
 for file,label in [('逐届集中度三口径.csv','下载逐届数据'),('结论压力测试摘要.json','查看复算摘要'),('结论压力测试.md','阅读完整方法')]:
  a=s.new_tag('a',href=file);a.string=label;downloads.append(a)
 main.append(downloads)
p.write_text(str(s),encoding='utf-8')
# Render the controlled Markdown source as a browser-readable UTF-8 document.
folder=p.parent
method=folder/'结论压力测试_完整方法.html'
source=(folder/'结论压力测试.md').read_text(encoding='utf-8-sig')
def inline(text):
 text=html.escape(text)
 text=re.sub(r'`([^`]+)`',r'<code>\1</code>',text)
 text=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',text)
 text=re.sub(r'!\[([^]]*)\]\(([^)]+)\)',r'<img alt="\1" src="\2" loading="lazy">',text)
 return re.sub(r'\[([^]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',text)
blocks=[]
for paragraph in re.split(r'\n\s*\n',source.strip()):
 heading=re.match(r'^(#{1,6}) (.*)$',paragraph)
 if heading:
  level=len(heading[1]);blocks.append(f'<h{level}>'+inline(heading[2])+f'</h{level}>')
 else:blocks.append('<p>'+inline(paragraph)+'</p>')
method.write_text('<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>结论压力测试｜完整方法与复现</title><style>.method-reading{width:100%;max-width:none;margin:0;min-width:0;box-sizing:border-box}.method-reading h2{margin-top:48px}.method-reading p{margin-block:20px}.method-reading img{display:block;width:100%;border-radius:10px}.method-reading code{font-size:.9em;overflow-wrap:anywhere}.method-actions{display:flex;gap:24px;flex-wrap:wrap;margin-bottom:36px}.method-actions a{min-height:44px;display:inline-flex;align-items:center}</style></head><body><main><article class="method-reading"><nav class="method-actions" aria-label="方法材料"><a href="结论压力测试.html">← 返回结论压力测试</a><a href="结论压力测试.md" download>下载 Markdown 原文</a></nav>'+''.join(blocks)+'</article></main></body></html>',encoding='utf-8')
# Route authored HTML method links to the reading page; retain explicit downloads.
for page in (root/'交付文件').rglob('*.html'):
 if '原始页面' in str(page) or page==method:continue
 doc=BeautifulSoup(page.read_text(encoding='utf-8'),'html.parser');changed=False
 for a in doc.select('a[href]'):
  href=a['href']
  if a.has_attr('download') or not href.endswith('结论压力测试.md'):continue
  if (page.parent/href).resolve()==(folder/'结论压力测试.md').resolve():
   a['href']=href[:-3]+'_完整方法.html';changed=True
 if changed:page.write_text(str(doc),encoding='utf-8')


# The supplementary-page theme is the final presentation pass.
import runpy
runpy.run_path(str(Path(__file__).with_name("publish_supplement_reading.py")))

runpy.run_path(str(Path(__file__).with_name("publish_pressure_summary.py")))
