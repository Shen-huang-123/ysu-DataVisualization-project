from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[2]
p=root/'交付文件/任务三_专题深挖/S4_小代表团的大突破/index.html'
s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
s.body['class']=list(dict.fromkeys(s.body.get('class',[])+['small-team-topic']))
link=s.select_one('#small-team-topic-style')
if not link:
 link=s.new_tag('link',id='small-team-topic-style',rel='stylesheet');s.head.append(link)
link['href']='../../共享组件/small-team-topic.css?v=1'
shared=s.select_one('#unified-selects')
if not shared:
 shared=s.new_tag('link',id='unified-selects',rel='stylesheet');s.head.append(shared)
shared['href']='../../共享组件/unified-selects.css?v=5'
p.write_text(str(s),encoding='utf-8')
