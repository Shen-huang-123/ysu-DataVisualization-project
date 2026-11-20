from pathlib import Path
from bs4 import BeautifulSoup
import os,copy
root=Path(__file__).resolve().parents[2]
p=root/'交付文件/任务四_开放创作/09_预测风暴实验室/index.html'
source=root/'交付文件/任务四_开放创作/index.html'
s=BeautifulSoup(p.read_text(encoding='utf8'),'html.parser');ref=BeautifulSoup(source.read_text(encoding='utf8'),'html.parser')
old=s.select_one('header.top')
if old:old.decompose()
for ident in ['xz-nav','xz-menu','xz-progress','xz-top','unified-topbar-style','unified-topbar-script']:
 old=s.find(id=ident)
 if old:old.decompose()
 item=copy.deepcopy(ref.find(id=ident))
 if not item:continue
 for a in item.select('a[href]'):
  href=a['href']
  if not href.startswith(('http','#','mailto:')):a['href']=os.path.relpath(source.parent/href,p.parent).replace('\\','/')
 if item.name=='style':s.head.append(item)
 elif item.name=='script':s.body.append(item)
 else:s.body.insert(0,item)
for name in ['integrated-nav.css?v=9']:
 if not s.find('link',href='../../共享组件/'+name):s.head.append(s.new_tag('link',rel='stylesheet',href='../../共享组件/'+name))
if not s.find('script',src='../../共享组件/integrated-nav.js?v=5'):s.body.append(s.new_tag('script',src='../../共享组件/integrated-nav.js?v=5'))
st=s.select_one('#storm-nav-spacing')
if not st:st=s.new_tag('style',id='storm-nav-spacing');s.head.append(st)
st.string="html body{padding-top:0!important;margin-top:0!important}html body>.wrap{padding-top:0!important;margin-top:0!important}html body .wrap>.hero{margin-top:0!important;min-height:100svh!important;padding-top:130px!important}html body #xz-nav{background:transparent!important}html body #xz-menu a{color:#edf3f2!important}html body #xz-menu{background:#182128!important}"
s.body['class']=list(dict.fromkeys(s.body.get('class',[])+['xz-dark']))
p.write_text(str(s),encoding='utf8')
