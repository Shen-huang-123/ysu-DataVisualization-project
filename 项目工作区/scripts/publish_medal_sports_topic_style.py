from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[2]
p=root/'交付文件/任务三_专题深挖/S10_奖牌藏在哪些项目/index.html'
s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
s.body['class']=list(dict.fromkeys(s.body.get('class',[])+['medal-sports-topic']))
h=s.select_one('header');h['id']='medal-sports-hero'
if not h.select_one('.sports-photo'):
 img=s.new_tag('img',attrs={'class':'sports-photo','src':'../媒体/sports.jpg','alt':'2024年巴黎奥运会游泳比赛场馆，场景配图','fetchpriority':'high'});h.insert(0,img)
link=s.select_one('#medal-sports-style')
if not link:link=s.new_tag('link',id='medal-sports-style',rel='stylesheet');s.head.append(link)
link['href']='../../共享组件/medal-sports-topic.css?v=2'
for decoration in s.select('.art-figure'):
 decoration.decompose()
bridge=s.select_one('.task3-depth-bridge')
if bridge:
 metrics=bridge.select_one('h2 + div')
 if metrics:metrics['class']=['sports-metrics']
proof=s.select_one('a.research-proof-link');footer=s.select_one('footer')
if proof and footer:footer.insert_before(proof.extract())
p.write_text(str(s),encoding='utf-8')
