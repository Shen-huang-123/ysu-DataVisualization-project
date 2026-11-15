from pathlib import Path
from bs4 import BeautifulSoup
import os
root=Path.cwd();shared=root/'交付文件/共享组件'
config=[('任务一_数据体检/index.html',1,'同一个名字，未必是同一件事。','字段归一之后，回到每一条处理决定。','lens.jpg'),('任务二_百年全景/05_交互总览/index.html',0,'把时间拉近，才能看见具体的人。','从百年的轮廓，走进一届奥运的切面。','growth.jpg'),('任务三_专题深挖/统一中文入口/index.html',1,'榜单之外，故事仍在继续。','把视线交给人，也交给历史留下的空白。','women.jpg'),('任务四_开放创作/index.html',1,'未来没有唯一的剧本。','沿着假设的变化，观察答案如何移动。','host.jpg')]
media=root/'交付文件/任务三_专题深挖/媒体'
print([p.name for p in media.glob('*.jpg')])
for filename,index,title,deck,img in config:
 p=root/'交付文件'/filename;s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 if s.select_one('.narrative-cinema'):continue
 imagepath=media/img
 if not imagepath.exists():imagepath=media/'host.jpg'
 src=os.path.relpath(imagepath,p.parent).replace('\\','/')
 f=s.new_tag('figure',attrs={'class':'narrative-cinema'})
 photo=s.new_tag('img',attrs={'src':src,'alt':'','loading':'lazy','decoding':'async','class':'narrative-cinema-photo'})
 caption=s.new_tag('figcaption');h=s.new_tag('p',attrs={'class':'narrative-cinema-title'});h.string=title;caption.append(h);d=s.new_tag('p');d.string=deck;caption.append(d)
 f.extend([photo,caption]);s.select('.narrative-chapter')[index].insert_after(f)
 for name in ['gsap/gsap.min.js','gsap/ScrollTrigger.min.js','narrative-cinema.js?v=1']:
  rel=os.path.relpath(shared/name.split('?')[0],p.parent).replace('\\','/')+('?' +name.split('?')[1] if '?' in name else '')
  if not any(name.split('?')[0] in t.get('src','') for t in s.select('script[src]')):s.body.append(s.new_tag('script',attrs={'src':rel,'defer':''}))
 css=os.path.relpath(shared/'narrative-cinema.css',p.parent).replace('\\','/')+'?v=1';s.head.append(s.new_tag('link',attrs={'rel':'stylesheet','href':css}))
 p.write_text(str(s),encoding='utf-8')
