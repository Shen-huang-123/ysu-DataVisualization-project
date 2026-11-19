from pathlib import Path
from bs4 import BeautifulSoup
import json,re
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'交付文件/任务三_专题深挖/S9_消失的赛场/index.html'
s=BeautifulSoup(p.read_text(encoding='utf-8-sig'),'html.parser')
s.body['class']=list(dict.fromkeys(s.body.get('class',[])+['vanished-topic']))
if not s.find('link',id='vanished-topic-style'):s.head.append(s.new_tag('link',id='vanished-topic-style',rel='stylesheet',href='../../共享组件/vanished-topic.css'))
header=s.body.find('header',recursive=False);photo=s.select_one('figure.photo-stage')
if photo and not header.select_one('.vanished-photo'):
 img=photo.img.extract();img['class']=['vanished-photo'];header.insert(0,img)
 caption=photo.figcaption.extract();caption['class']=['vanished-credit'];header.append(caption);photo.decompose()
for x in s.select('.art-figure'):x.decompose()
for script in s.find_all('script'):
 match=re.search(r'const rows=(\[.*?\]);',script.text)
 if match:
  rows=json.loads(match[1])
  for button,row in zip(s.select('main .bar'),rows):
   if not button.select_one('.vanished-years'):
    span=s.new_tag('span',attrs={'class':'vanished-years'});span.string=row['detail'].replace(' 年','');button.append(span)
   button['aria-pressed']='true' if button.get('data-i')=='0' else 'false'
  break
if not s.find('script',id='vanished-selection'):
 x=s.new_tag('script',id='vanished-selection');x.string="document.querySelectorAll('main .bar').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('main .bar').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));}));";s.body.append(x)
proof=s.select_one('a.research-proof-link');footer=s.body.find('footer',recursive=False)
if proof and footer:footer.insert_before(proof.extract())
p.write_text(str(s),encoding='utf-8')
