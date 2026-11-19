from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[2]
p=root/'交付文件/任务三_专题深挖/媒体/图片来源与许可.html'
s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
source=BeautifulSoup((root/'交付文件/任务三_专题深挖/统一中文入口/index.html').read_text(encoding='utf-8'),'html.parser')
s.body['class']=list(dict.fromkeys(s.body.get('class',[])+['photo-credits-page']))
old=s.select_one('.top')
if old:old.decompose()
for ident in ['unified-theme-preload','unified-topbar-style']:
 if not s.select_one('#'+ident):s.head.append(source.select_one('#'+ident).extract())
for ident in ['xz-nav','xz-progress','xz-menu','xz-top']:
 if not s.select_one('#'+ident):
  node=source.select_one('#'+ident)
  if node:s.body.insert(0,node.extract())
nav=s.select_one('#xz-nav')
for a in nav.select('a[aria-current]'):a['href']='../统一中文入口/index.html'
menu=s.select_one('#xz-menu')
if menu:
 for a in menu.select('a[href]'):
  if a['href']=='index.html':a['href']='../统一中文入口/index.html'
if not s.select_one('#unified-topbar-script'):s.body.append(source.select_one('#unified-topbar-script').extract())
s.select_one('.hero small').string='摄影档案 / 图片来源与许可'
link=s.select_one('#photo-credits-style')
if not link:link=s.new_tag('link',id='photo-credits-style',rel='stylesheet');s.head.append(link)
link['href']='../../共享组件/photo-credits.css?v=1'
p.write_text(str(s),encoding='utf-8')
