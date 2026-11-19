from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[2]
p=root/'交付文件/任务三_专题深挖/S2_口径的魔力/06_滚动叙事专题/index.html'
s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
s.body['class']=list(dict.fromkeys(s.body.get('class',[])+['medal-lens-topic']))
hero=s.select_one('header.hero')
hero['id']='medal-lens-hero'
if not hero.select_one('.medal-lens-photo'):
 photo=s.new_tag('img',attrs={'class':'medal-lens-photo','src':'../../媒体/lens.jpg','alt':'奥运场景照片，作为统计口径专题的场景配图','fetchpriority':'high'})
 hero.insert(0,photo)
link=s.select_one('#medal-lens-topic-style')
if not link:link=s.new_tag('link',id='medal-lens-topic-style',rel='stylesheet');s.head.append(link)
link['href']='../../../共享组件/medal-lens-topic.css?v=4'
for script in s.select('script[src]'):
 if 'exploration-design.js' in script['src']:script['src']='../../../共享组件/exploration-design.js?v=20261119-route'
p.write_text(str(s),encoding='utf-8')


