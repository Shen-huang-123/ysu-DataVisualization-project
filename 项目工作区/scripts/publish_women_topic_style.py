from pathlib import Path
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'交付文件/任务三_专题深挖/S8_她们登上领奖台/index.html'
s=BeautifulSoup(p.read_text('utf8'),'html.parser')
s.body['class']=list(dict.fromkeys(s.body.get('class',[])+['women-topic']))
if not s.select_one('#women-topic-style'):s.head.append(s.new_tag('link',id='women-topic-style',rel='stylesheet',href='../../共享组件/women-topic.css?v=2'))
hero=s.body.find('header',recursive=False)
if hero:
 tag=hero.select_one('.tag')
 if tag:tag.string='专题深挖 / S8 · 女性获奖记录'
 figure=s.select_one('.photo-stage')
 if figure and not hero.select_one('.women-credit'):
  credit=s.new_tag('div',attrs={'class':'women-credit'})
  credit.append(figure.figcaption.extract());hero.append(credit)
aside=s.select_one('.viz>aside')
if aside:
 for node in aside.find_all(string=True):
  if '点击任意条形查看' in node:node.replace_with('选择届次，查看精确读数')
if hero and not hero.select_one('.women-hero-photo'):
 photo=s.new_tag('img',attrs={'class':'women-hero-photo','src':'../媒体/women.jpg','alt':'1900年巴黎奥运会女子网球比赛完整历史照片','loading':'eager'})
 hero.append(photo)
chart=s.select_one('.chart')
if chart and not s.select_one('.women-axis'):
 axis=BeautifulSoup('<div class="women-axis" aria-hidden="true"><span>女性获奖行占比</span><span>0%</span><span>50%</span><span>100%</span></div>','html.parser')
 chart.insert_before(axis)
for bar in s.select('.bar'):
 value=float(bar.strong.get_text().rstrip('%'))
 bar.select_one('i')['style']=f'width:{value}%'
 bar['aria-pressed']='false'
if s.select_one('#women-topic-interaction'):s.select_one('#women-topic-interaction').decompose()
if True:
 js=s.new_tag('script',id='women-topic-interaction')
 js.string="""(()=>{const bars=[...document.querySelectorAll('.bar')];bars.forEach(b=>b.addEventListener('click',()=>{bars.forEach(x=>x.setAttribute('aria-pressed',String(x===b)));const i=+b.dataset.i;const r=rows[i];document.querySelector('#detail').textContent=r.value.toFixed(1)+'% · 女性获奖记录 '+r.detail+' 行';}));window.addEventListener('load',()=>{const range=document.querySelector('.ex-stage input[type=range]');if(range){range.value=range.max;range.dispatchEvent(new Event('input',{bubbles:true}));}else bars.at(-1)?.click();});})();"""
 s.body.append(js)
# S8 uses a licensed medal-ceremony photograph, displayed uncropped.
photo=hero.select_one('.women-hero-photo')
photo['src']='../媒体/women-wide-2016.jpg'
photo['alt']='2016年里约奥运会女子体操团体获奖队伍合影'
credit=hero.select_one('.women-credit')
credit.clear()
credit.append(BeautifulSoup('<figcaption><strong>里约2016 · 女子体操颁奖仪式 <small>· 场景配图，不作为统计证据</small></strong><a href="https://commons.wikimedia.org/wiki/File:EUA_levam_ouro_na_gin%C3%A1stica_art%C3%ADstica_feminina;_Brasil_fica_em_8%C2%BA_lugar_(28264937223).jpg" target="_blank" rel="noopener">Agência Brasil Fotografias · CC BY 2.0</a></figcaption>','html.parser'))
proof=s.body.find('a',href='../11_结论稳定性地图/index.html#S8',recursive=False)
if proof:
 proof['class']=['women-proof-link']
 proof.attrs.pop('style',None)
 for child in proof.select('[style]'):child.attrs.pop('style',None)
 s.body.find('footer',recursive=False).insert_before(proof.extract())
p.write_text(str(s),'utf8')
