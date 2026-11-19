from pathlib import Path
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'交付文件/任务三_专题深挖/S3_地缘政治的投影/index.html'
s=BeautifulSoup(p.read_text(encoding='utf-8-sig'),'html.parser')
s.body['class']=list(dict.fromkeys(s.body.get('class',[])+['geopolitics-topic']))
if not s.find('link',id='geopolitics-topic-style'):s.head.append(s.new_tag('link',id='geopolitics-topic-style',rel='stylesheet',href='../../共享组件/geopolitics-topic.css'))
header=s.body.find('header',recursive=False);photo=s.select_one('figure.photo-stage')
if photo and not header.select_one('.geopolitics-photo'):
 img=photo.img.extract();img['class']=['geopolitics-photo'];header.insert(0,img)
 caption=photo.figcaption.extract();caption['class']=['geopolitics-credit'];header.append(caption);photo.decompose()
for x in s.select('.art-figure'):x.decompose()
identity=s.select_one('.evidence article:nth-child(2)')
if identity and not identity.select_one('.identity-list'):
 paragraph=identity.p;original=paragraph.get_text(' ',strip=True);items,tail=original.split('。',1)
 listing=s.new_tag('ul',attrs={'class':'identity-list'})
 for text in items.split(' / '):
  li=s.new_tag('li');li.string=text.strip();listing.append(li)
 paragraph.string=tail;paragraph.insert_before(listing)
footer=s.body.find('footer',recursive=False)
if footer:
 for a in s.body.find_all('a',recursive=False):
  if a.find(['strong','h2']):
   if a.h2:a.h2.name='strong'
   if a.p:a.p.name='span'
   a['class']=list(dict.fromkeys(a.get('class',[])+['research-proof-link']));footer.insert_before(a.extract())
if not s.find('link',id='research-proof-links'):s.head.append(s.new_tag('link',id='research-proof-links',rel='stylesheet',href='../../共享组件/research-proof-links.css'))
s.select_one('.viz h2').string='参赛规模的变化'
p.write_text(str(s),encoding='utf-8')

