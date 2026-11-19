from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[2]
p=root/'交付文件/任务三_专题深挖/统一中文入口/index.html'
s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
s.body['class']=list(dict.fromkeys(s.body.get('class',[])+['topic-portal-refined']))
footer=s.select_one('footer')
for child in list(s.body.children):
 if getattr(child,'name',None) in ('a','section') and child is not footer and footer in list(child.previous_siblings):
  footer.insert_before(child.extract())
  if child.name=='a':child['class']=list(dict.fromkeys(child.get('class',[])+['portal-research-entry']))
link=s.select_one('#topic-portal-refined-style')
if not link:link=s.new_tag('link',id='topic-portal-refined-style',rel='stylesheet');s.head.append(link)
link['href']='../../共享组件/topic-portal-refined.css?v=1'
p.write_text(str(s),encoding='utf-8')
