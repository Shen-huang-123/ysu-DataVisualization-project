from pathlib import Path
from bs4 import BeautifulSoup, Tag
import os
root=Path.cwd();shared=root/'交付文件/共享组件'
files=[('任务一_数据体检/index.html','audit'),('任务二_百年全景/05_交互总览/index.html','panorama'),('任务三_专题深挖/统一中文入口/index.html','stories'),('任务四_开放创作/index.html','future')]
copy={
'audit':('一条记录，怎样成为可信的证据？','从一个模糊的小项名称出发，沿着原始字段、处理规则和排名差异，追问每一个数字的含义。',['标签的裂缝','名字的归处','决定的依据','历史的边界','榜单的变化']),
'panorama':('把一个世纪，收进同一个视野。','时间拉远，结构浮现；视线停在一届，差异才有了具体的名字。',['百年尺度','一届切面','代表团之间']),
'stories':('同一份数据，问题可以走多远？','一张榜单引出统计单位，一次反常引出解释机制，最后回到被记录的人与没有被记录的历史。',['数字的含义','解释的分寸','被看见的人','结论的反面']),
'future':('预测的终点，是接受现实检验。','历史提供起点，假设改变方向；读完一张榜单，还要回头看它如何形成、又可能在哪里失准。',['历史的起点','假设的风向','未来的区间','现实的检验'])}

def fragment(s):return BeautifulSoup(s,'html.parser')
def make(soup,tag,cls=None,text=None):
 e=soup.new_tag(tag)
 if cls:e['class']=cls
 if text:e.string=text
 return e
for filename,key in files:
 p=root/'交付文件'/filename;soup=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser');main=soup.find('main')
 if main.select_one('.narrative-layout'):continue
 soup.body['class']=soup.body.get('class',[])+['narrative-module','narrative-'+key]
 soup.body['data-narrative']=key
 title,lead,labels=copy[key]
 intro=make(soup,'div','narrative-opening');intro.append(make(soup,'h2',None,title));intro.append(make(soup,'p',None,lead))
 groups=[]
 if key=='audit':
  audit=main.select_one('.xz-section');year=main.find(id='年份');mapping=main.find(id='映射');ranks=main.find(id='口径');boundary=main.select_one('.xz-note')
  groups=[[year],[mapping],[audit],[boundary],[ranks]]
  # The same controls and underlying data, now ordered as an evidence chain.
  for i,sec in enumerate([year,mapping,audit,boundary,ranks]):
   top=sec.select_one('.xz-section-top > span')
   if top:top.string=['字段观察','名称归一','可复现审计','样本边界','口径对照'][i]
  year.select_one('h2').string='看似完整的小项名称，在哪里失去细节？'
  mapping.select_one('h2').string='名字变了，还是运动变了？'
  audit.select_one('h2').string='一次处理，能不能找到它的依据？'
  boundary.select_one('h2').string='同一个世纪，并非同一种身份。'
  ranks.select_one('h2').string='处理规则落定，榜单仍只有一种读法吗？'
  ranks.select_one('.xz-toolbar').insert_before(fragment('<div class="narrative-choices" role="group" aria-label="突出显示奖牌统计口径"><button type="button" data-rank-lens="official" aria-pressed="true">看小项名次</button><button type="button" data-rank-lens="athlete" aria-pressed="false">看运动员行名次</button></div>'))
 elif key=='panorama':
  elements=[e for e in main.children if isinstance(e,Tag)]
  cards=main.select_one('section.cards');filters=main.select_one('section.filters');heads=main.select('.t2-section-head')
  groups=[[heads[0],filters,cards],[heads[1],main.select_one('.actions'),main.select_one('.t2-chart-panel')],[heads[2],main.select_one('.t2-table-wrap')]]
  heads[0].select_one('h2').string='改变尺度，同一份数据会怎样回应？'
  filters.insert_before(fragment('<div class="narrative-choices" role="group" aria-label="探索历史的观察角度"><button type="button" data-panorama="century" aria-pressed="true">百年参与</button><button type="button" data-panorama="edition" aria-pressed="false">停在2024</button><button type="button" data-panorama="women" aria-pressed="false">女性参赛轨迹</button></div>'))
  # The newly inserted choices belong in the same chapter as the original filters.
  groups[0].insert(1,main.select_one('.narrative-choices'))
  heads[1].select_one('h2').string='把视线停在一届，趋势变成谁的名字？'
  heads[2].select_one('h2').string='总量相近，参与结构也一样吗？'
 elif key=='stories':
  cards=list(main.select('.grid .story'));grid=main.select_one('.grid');filters=main.select_one('.filters')
  order=[[1,4,9],[0,3,6],[2,5,7,8]]
  names=['先问：这个数字到底在数什么？','再问：看见差异，就能解释原因吗？','继续追问：谁留下记录，谁没有被看见？']
  descriptions=['把名次、规模与项目份额放在一起，统计单位的影响不再只是脚注。','主场、小队伍与王朝，需要共同面对趋势、样本选择和反例。','代表团、人物、女性与项目档案，留下不同类型的历史缺口。']
  for i,indices in enumerate(order):
   sec=make(soup,'section','narrative-topic-group');sec.append(make(soup,'h2',None,names[i]));sec.append(make(soup,'p','narrative-deck',descriptions[i]))
   if i==0:sec.append(filters.extract())
   g=make(soup,'div','grid');g['aria-label']=labels[i]+'的专题'
   for j in indices:g.append(cards[j].extract())
   sec.append(g);groups.append([sec])
  groups.append([main.select_one('.inline-evidence')])
 elif key=='future':
  cards=list(main.select('.xz-path > a'));note=main.select_one('.xz-note')
  order=[[2,5,4],[6,3],[0,1],[7]]
  names=['历史能提供怎样的起点？','如果风向变了，答案会怎样？','看见名次，也看见不确定性。','把解释权，交回未来的实际结果。']
  descriptions=['回到历史趋势、举办地与结构变化，确认预测借用了哪些经验。','改变主场、新增运动与资格条件；同时保留方法、回测及误差作为参照。','从完整故事进入预测看板，分清点估计、区间与条件。','预测可以被检验；赛后把真实结果放进同一套评价规则。']
  for i,indices in enumerate(order):
   sec=make(soup,'section','narrative-future-group');sec.append(make(soup,'h2',None,names[i]));sec.append(make(soup,'p','narrative-deck',descriptions[i]));g=make(soup,'div','xz-path')
   for j in indices:
    card=cards[j].extract();card.attrs.pop('data-no',None);g.append(card)
   sec.append(g)
   if i==3:sec.append(note.extract())
   groups.append([sec])
 layout=make(soup,'div','narrative-layout');aside=make(soup,'aside','narrative-companion');aside['aria-label']='本模块的阅读线索'
 aside.append(make(soup,'p','narrative-companion-title','沿着问题，走向证据'))
 route=make(soup,'nav','narrative-route');route['aria-label']='探索章节'
 aside.append(route)
 context=make(soup,'div','narrative-context');context.append(make(soup,'small',None,'当前观察'));context.append(make(soup,'p','narrative-context-text',''));aside.append(context)
 flow=make(soup,'div','narrative-flow')
 for i,items in enumerate(groups):
  chapter=make(soup,'section','narrative-chapter');chapter['id']=f'explore-{key}-{i+1}';chapter['data-story-label']=labels[i]
  link=make(soup,'a',None,labels[i]);link['href']='#'+chapter['id'];route.append(link)
  for el in items:
   if el:chapter.append(el.extract())
  if i+1<len(groups):
   foot=make(soup,'div','narrative-bridge');a=make(soup,'a',None,labels[i+1]+'  →');a['href']=f'#explore-{key}-{i+2}';a['aria-label']='继续探索：'+labels[i+1];foot.append(a);chapter.append(foot)
  flow.append(chapter)
 layout.extend([aside,flow])
 main.clear();main.extend([intro,layout])
 # A question carries the reader into the next module, rather than another card grid.
 dest={'audit':('../任务二_百年全景/05_交互总览/index.html','口径清楚了，百年变化会呈现什么形状？','进入百年全景'),'panorama':('../../任务三_专题深挖/统一中文入口/index.html','看见变化之后，我们能解释多少？','进入专题深挖'),'stories':('../../任务四_开放创作/index.html','这些历史经验，能带我们走向哪里？','进入洛杉矶2028'),'future':('../最终提交材料/00_先看这里.html','带着问题离开，也带走完整证据。','查看正式材料')}[key]
 end=make(soup,'section','narrative-handoff');end.append(make(soup,'p',None,dest[1]));a=make(soup,'a',None,dest[2]+' ↗');a['href']=dest[0];end.append(a);main.append(end)
 hero=soup.select_one('header.photo-editorial-hero, header.hero, header.xz-hero')
 if hero:
  action=hero.select_one('.xz-hero-actions a,.hero-actions a')
  if action:action['href']='#explore-'+key+'-1';action.string={'audit':'看一条记录的变化 ↘','panorama':'把时间拉远 ↘','stories':'从一个数字开始 ↘','future':'回到历史的起点 ↘'}[key]
 rel=os.path.relpath(shared,p.parent).replace('\\','/')
 css=soup.new_tag('link',rel='stylesheet',href=rel+'/narrative-modules.css?v=1');soup.head.append(css)
 script=soup.new_tag('script',src=rel+'/narrative-modules.js?v=1',defer='');soup.body.append(script)
 p.write_text(str(soup),encoding='utf-8')
 print('Narrative layout:',filename)
p=shared/'exploration-design.js';s=p.read_text(encoding='utf-8').replace('if(headings.length>1){',"if(headings.length>1&&!document.body.classList.contains('narrative-module')){");p.write_text(s,encoding='utf-8')
