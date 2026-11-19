from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[2]
p=root/'交付文件/任务三_专题深挖/S5_奖牌的通货膨胀/index.html'
s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
s.body['class']=list(dict.fromkeys(s.body.get('class',[])+['medal-growth-topic']))
h=s.select_one('header');h['id']='medal-growth-hero'
if not h.select_one('.growth-photo'):
 img=s.new_tag('img',attrs={'class':'growth-photo','src':'../媒体/growth.jpg','alt':'1896年雅典奥运会体育场历史照片，场景配图','fetchpriority':'high'});h.insert(0,img)
link=s.select_one('#medal-growth-style')
if not link:link=s.new_tag('link',id='medal-growth-style',rel='stylesheet');s.head.append(link)
link['href']='../../共享组件/medal-growth-topic.css?v=2'
p.write_text(str(s),encoding='utf-8')

