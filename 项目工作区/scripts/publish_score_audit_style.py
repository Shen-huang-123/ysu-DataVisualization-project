from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[2]
p=root/'交付文件/任务四_开放创作/06_赛后验收单/index.html'
s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
s.body['class']=list(dict.fromkeys(s.body.get('class',[])+['score-audit']))
if not s.select_one('#score-audit-style'):s.head.append(s.new_tag('link',id='score-audit-style',rel='stylesheet',href='../../共享组件/score-audit.css?v=2'))
s.select_one('#score-audit-style')['href']='../../共享组件/score-audit.css?v=2'
s.select_one('#status')['role']='status'
s.select_one('#status')['aria-live']='polite'
p.write_text(str(s),encoding='utf-8')
