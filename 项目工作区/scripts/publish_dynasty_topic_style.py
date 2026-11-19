from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[2]
p=root/'交付文件/任务三_专题深挖/S3_冠军的保质期/06_冠军王朝时间轴/index.html'
s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
s.body['class']=list(dict.fromkeys(s.body.get('class',[])+['dynasty-topic']))
for ident,href in [('dynasty-topic-style','dynasty-topic.css?v=1'),('unified-selects','unified-selects.css?v=5')]:
 link=s.select_one('#'+ident)
 if not link:link=s.new_tag('link',id=ident,rel='stylesheet');s.head.append(link)
 link['href']='../../../共享组件/'+href
p.write_text(str(s),encoding='utf-8')
