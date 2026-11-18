"""Canonical final styling pass for authored research pages, excluding source archives and immersive scenes."""
from pathlib import Path
from bs4 import BeautifulSoup
import os,json
root=Path(__file__).resolve().parents[2];delivery=root/'交付文件';selected=[]
exclusions=['原始页面','99_旧版归档','媒体','screen.template','文档阅读入口.html','07_ECharts大屏','08_奥运时空剧场','10_百年项目星系','09_预测风暴实验室','09_奖牌口径实验室']
for p in delivery.rglob('*.html'):
 if any(x in str(p) for x in exclusions):continue
 s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 if not s.body or not s.head or s.select_one('#xz-nav') or s.find('meta',attrs={'http-equiv':lambda v:v and v.lower()=='refresh'}):continue
 classes=s.body.get('class',[])
 if 'supplement-reading' not in classes:classes.append('supplement-reading')
 s.body['class']=classes
 rel=Path(os.path.relpath(delivery/'共享组件',p.parent)).as_posix()
 if not s.select_one('#supplement-assets'):
  link=s.new_tag('link',id='supplement-assets',rel='stylesheet',href=rel+'/supplement-reading.css?v=1');s.head.append(link)
  preload=s.new_tag('script',id='supplement-theme-preload');preload.string="try{if(localStorage.getItem('xz-theme')==='dark'){document.write('<style>body.supplement-reading{background:#10212a!important;color:#eef2ee!important}</style>')}}catch(e){}";s.head.append(preload)
  script=s.new_tag('script',src=rel+'/supplement-reading.js?v=1',defer='');s.head.append(script)
 preload=s.select_one('#supplement-theme-preload')
 if preload:preload.string="try{document.documentElement.dataset.suppTheme=localStorage.getItem('xz-theme')==='dark'?'dark':'light'}catch(e){}"
 if not s.select_one('.supp-nav'):
  nav=s.new_tag('nav',attrs={'class':'supp-nav','aria-label':'作品导航'})
  a=s.new_tag('a',href=Path(os.path.relpath(delivery/'作品总入口/index.html',p.parent)).as_posix());a.string='晓 · 奥运数据观察';nav.append(a)
  links=s.new_tag('div')
  for file,label in [('任务一_数据体检/index.html','数据体检'),('任务二_百年全景/05_交互总览/index.html','百年全景'),('任务三_专题深挖/统一中文入口/index.html','专题深挖'),('任务四_开放创作/index.html','洛杉矶2028')]:
   a=s.new_tag('a',href=Path(os.path.relpath(delivery/file,p.parent)).as_posix());a.string=label;links.append(a)
  button=s.new_tag('button',type='button',attrs={'data-supp-theme':'','aria-pressed':'false'});button.string='深色模式';links.append(button);nav.append(links)
  if not s.main and not s.select_one('body>.wrap,body>.container'):
   content=s.new_tag('main',attrs={'class':'supp-content'})
   for n in list(s.body.contents):
    if getattr(n,'name',None) not in ['script','style']:content.append(n.extract())
   s.body.insert(0,content)
  s.body.insert(0,nav)
 for table in s.select('table'):
  if table.find_parent(class_='supp-table'):continue
  wrap=s.new_tag('div',attrs={'class':'supp-table','role':'region','aria-label':'数据表，可横向查看','tabindex':'0'});table.wrap(wrap)
 p.write_text(str(s),encoding='utf-8');selected.append(str(p.relative_to(delivery)).replace('\\','/'))
(delivery/'最终提交材料/附页风格统一清单.json').write_text(json.dumps(selected,ensure_ascii=False,indent=2),encoding='utf-8')
print('Unified',len(selected),'authored supplementary pages')
