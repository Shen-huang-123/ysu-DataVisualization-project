from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[2]
p=root/'交付文件/任务四_开放创作/06_赛后验收单/index.html'
s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
s.body['class']=list(dict.fromkeys(s.body.get('class',[])+['score-audit']))
if not s.select_one('#score-audit-style'):s.head.append(s.new_tag('link',id='score-audit-style',rel='stylesheet',href='../../共享组件/score-audit.css?v=4'))
s.select_one('#score-audit-style')['href']='../../共享组件/score-audit.css?v=4'
s.select_one('#status')['role']='status'
s.select_one('#status')['aria-live']='polite'
for link in s.select('link[href]'):
 if 'exploration-design.css' in link['href']:link['href']=link['href'].split('?')[0]+'?v=20261118-route'
s.select_one('#demo')['aria-pressed']='false'
if not s.select_one('#score-audit-state'):s.head.append(s.new_tag('script',id='score-audit-state',src='../../共享组件/score-audit-state.js?v=1',defer=''))
table=s.select_one('#rows').find_parent('table')
table['id']='score-errors'
for th in table.select('thead th'):th['scope']='col'
wrap=table.parent
wrap['class']=list(dict.fromkeys(wrap.get('class',[])+['score-error-table']))
wrap['tabindex']='0'
wrap['role']='region'
wrap['aria-label']='逐代表团误差表，窄屏可横向查看'
if not wrap.select_one('.score-empty'):
 empty=s.new_tag('div',attrs={'class':'score-empty'})
 empty.append(BeautifulSoup('<strong>尚无比较结果</strong>上传实际结果或运行历史演示后，这里将显示逐代表团误差。','html.parser'))
 wrap.append(empty)
p.write_text(str(s),encoding='utf-8')
