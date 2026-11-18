from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[2]
p=root/'交付文件/任务二_百年全景/09_课程方法可视分析/index.html'
s=BeautifulSoup(p.read_text('utf8'),'html.parser');s.body['class']=list(dict.fromkeys(s.body.get('class',[])+['course-lens']))
if not s.select_one('#course-lens-style'):s.head.append(s.new_tag('link',id='course-lens-style',rel='stylesheet',href='../../共享组件/course-lens.css'))
p.write_text(str(s),'utf8')

import runpy
runpy.run_path(str(Path(__file__).with_name('publish_interval_reading.py')))
