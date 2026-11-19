from pathlib import Path
from bs4 import BeautifulSoup
import json,re
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'交付文件/任务三_专题深挖/S6_王者与传奇/index.html'
s=BeautifulSoup(p.read_text(encoding='utf-8-sig'),'html.parser')
s.body['class']=list(dict.fromkeys(s.body.get('class',[])+['legends-topic']))
if not s.find('link',id='legends-topic-style'):s.head.append(s.new_tag('link',id='legends-topic-style',rel='stylesheet',href='../../共享组件/legends-topic.css'))
header=s.body.find('header',recursive=False);photo=s.select_one('figure.photo-stage')
if photo and not header.select_one('.legends-photo'):
 img=photo.img.extract();img['class']=['legends-photo'];header.insert(0,img)
 caption=photo.figcaption.extract();caption['class']=['legends-credit'];header.append(caption);photo.decompose()
for e in s.select('.art-figure'):e.decompose()
for x in s.find_all('script'):
 m=re.search(r'const rows=(\[.*?\]);',x.text)
 if m:
  rows=json.loads(m[1]);break
for button,row in zip(s.select('main .bar'),rows):
 button['data-search']=row['label']+' '+row['raw_name'];button['aria-pressed']='true' if button['data-i']=='0' else 'false'
 if not button.select_one('.legends-years'):
  date=s.new_tag('span',attrs={'class':'legends-years'});date.string=row['detail'].split('；')[0];button.append(date)
if not s.find(id='legends-search'):
 tools=s.new_tag('div',attrs={'class':'legends-tools'});label=s.new_tag('label',attrs={'for':'legends-search'});label.string='检索核验候选';field=s.new_tag('input',id='legends-search',type='search',placeholder='输入姓名或记录标签',autocomplete='off');output=s.new_tag('output',id='legends-count',attrs={'aria-live':'polite'});output.string='12 条候选';tools.extend([label,field,output]);s.select_one('main .chart').insert_before(tools)
if not s.find(id='legends-selection'):
 script=s.new_tag('script',id='legends-selection');script.string="""(()=>{const bars=[...document.querySelectorAll('main .bar')];document.querySelector('#legends-search').addEventListener('input',e=>{const q=e.target.value.trim().toLocaleLowerCase();bars.forEach(b=>b.hidden=!b.dataset.search.toLocaleLowerCase().includes(q));document.querySelector('#legends-count').textContent=bars.filter(b=>!b.hidden).length+' 条候选';});bars.forEach(b=>b.addEventListener('click',()=>bars.forEach(x=>x.setAttribute('aria-pressed',String(x===b)))));})();""";s.body.append(script)
footer=s.body.find('footer',recursive=False)
if footer:
 for a in s.body.find_all('a',recursive=False):
  if a.find('strong'):footer.insert_before(a.extract())
s.select_one('.viz h2').string='姓名对应的金牌行 · 核验候选'
s.select_one('.viz aside small').string='点击记录查看详情'
p.write_text(str(s),encoding='utf-8')
