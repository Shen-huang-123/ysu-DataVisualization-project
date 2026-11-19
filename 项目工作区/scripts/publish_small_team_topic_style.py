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
p.write_text(str(s),encoding='utf-8')
