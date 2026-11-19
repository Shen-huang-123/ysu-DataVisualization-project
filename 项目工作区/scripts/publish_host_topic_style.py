"""Restore the host topic design after generating the research page."""
from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[2]
p=root/'交付文件/任务三_专题深挖/S1_东道主效应/index.html'
s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
s.body['class']=list(dict.fromkeys(s.body.get('class',[])+['host-topic']))
link=s.select_one('#host-topic-style')
if not link:
 link=s.new_tag('link',id='host-topic-style',rel='stylesheet');s.head.append(link)
link['href']='../../共享组件/host-topic.css?v=4'
for preload in s.select('link[rel="preload"][as="image"]'):
 preload['href']='../媒体/host.jpg'
hero=s.select_one('.s1-hero')
if hero and not hero.select_one('.host-entry-photo'):
 photo=s.new_tag('img',attrs={'class':'host-entry-photo','src':'../媒体/host.jpg','alt':'','aria-hidden':'true','fetchpriority':'high','loading':'eager'})
 hero.insert(0,photo)
if not s.select_one('#host-topic-script'):
 script=s.new_tag('script',id='host-topic-script',src='../../共享组件/host-topic.js',defer='');s.body.append(script)
p.write_text(str(s),encoding='utf-8')
import runpy
runpy.run_path(str(Path(__file__).with_name('publish_host_evidence_charts.py')))

