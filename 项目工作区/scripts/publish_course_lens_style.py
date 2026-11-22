from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[2]
p=root/'交付文件/任务二_百年全景/09_课程方法可视分析/index.html'
s=BeautifulSoup(p.read_text('utf8'),'html.parser');s.body['class']=list(dict.fromkeys(s.body.get('class',[])+['course-lens']))
link=s.select_one('#course-lens-style')
if not link:
 link=s.new_tag('link',id='course-lens-style',rel='stylesheet')
 s.head.append(link)
link['href']='../../共享组件/course-lens.css?v=2'
if not s.select_one('.course-track-art'):
 art=BeautifulSoup('<svg class="course-track-art" viewBox="0 0 640 210" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg"><g fill="none" stroke-width="1.2"><path d="M60 210 C220 210 210 25 380 25 H640" stroke="#83b6c8"/><path d="M90 210 C250 210 240 45 400 45 H640" stroke="#d6bd82"/><path d="M120 210 C280 210 270 65 420 65 H640" stroke="#bac9ca"/><path d="M150 210 C310 210 300 85 440 85 H640" stroke="#82ad99"/><path d="M180 210 C340 210 330 105 460 105 H640" stroke="#c894a1"/></g></svg>','html.parser')
 s.select_one('header.hero').insert(0,art)
p.write_text(str(s),'utf8')

import runpy
runpy.run_path(str(Path(__file__).with_name('publish_interval_reading.py')))
