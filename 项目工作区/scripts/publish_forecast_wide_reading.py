from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[2]
p=root/'交付文件/任务四_开放创作/index.html'
s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
link=s.select_one('#forecast-wide-reading')
if not link:link=s.new_tag('link',id='forecast-wide-reading',rel='stylesheet');s.head.append(link)
link['href']='../共享组件/forecast-wide-reading.css?v=2'
notice=s.select_one('.source-gate-notice')
note=s.select_one('.xz-note')
if note:note['id']='forecast-scenario-boundary'
if notice:
 notice['id']='forecast-source-notice'
 if note:notice.insert_before(note.extract())
p.write_text(str(s),encoding='utf-8')
