from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[2]
p=root/'交付文件/任务三_专题深挖/S2_口径的魔力/06_滚动叙事专题/index.html'
s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
s.body['class']=list(dict.fromkeys(s.body.get('class',[])+['medal-lens-topic']))
link=s.select_one('#medal-lens-topic-style')
if not link:link=s.new_tag('link',id='medal-lens-topic-style',rel='stylesheet');s.head.append(link)
link['href']='../../../共享组件/medal-lens-topic.css?v=1'
p.write_text(str(s),encoding='utf-8')
