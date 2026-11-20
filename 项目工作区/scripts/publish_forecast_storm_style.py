from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[2]
p=root/'交付文件/任务四_开放创作/09_预测风暴实验室/index.html'
s=BeautifulSoup(p.read_text(encoding='utf8'),'html.parser')
st=s.select_one('#storm-refined-style')
if not st:st=s.new_tag('style',id='storm-refined-style');s.head.append(st)
st.string="""
html body .hero{position:relative;isolation:isolate;min-height:580px!important;width:calc(100% / .88)!important;margin-left:calc(-6% / .88)!important;padding:90px 6vw 80px!important;background:linear-gradient(0deg,#182128,transparent 35%),linear-gradient(90deg,#101e27ed 0%,#101e27bd 48%,#101e2744 100%),url('../../任务三_专题深挖/媒体/la.jpg') center 48%/cover no-repeat!important;border:0!important}
html body .hero:before,html body .hero:after{content:none!important;display:none!important}
html body .hero aside{color:#e2e9e8!important;border-left:1px solid #ddc393!important}
html body .hero h1{color:#fff!important}
html body .hero .storm-photo-credit{position:absolute;bottom:20px;right:6vw;font-size:12px!important;color:#cbd7d8!important;max-width:none!important;margin:0!important}
@media(max-width:800px){html body .hero{width:calc(100% + 48px)!important;margin-left:-24px!important;padding:64px 24px 70px!important;min-height:580px!important}html body .hero .storm-photo-credit{right:24px;left:24px;font-size:11px!important}}

html body{background:#182128!important;background-image:none!important;color:#edf3f2!important;--muted:#bdcdd0;--line:#94b0ba40;font-family:'Microsoft YaHei',sans-serif!important}
html body:before,html body:after{background:none!important}
html body .oa-world,html body .immersive-float-layer{display:none!important}
html body .wrap{width:88%!important;max-width:none!important;margin-inline:auto!important}
html body .hero{padding:64px 0 40px!important;border-bottom:1px solid var(--line)}
html body .hero h1{font-size:clamp(42px,5.5vw,84px)!important;font-weight:500!important;line-height:1.22!important;letter-spacing:-.04em!important}
html body .hero p{font-size:17px!important;line-height:1.9!important}
html body .hero aside{font-size:14px!important;max-width:340px!important}
html body #project-reading-policy,html body #legacy-scenarios{width:100%!important;max-width:none!important;margin:32px 0!important;padding:28px 0!important;background:transparent!important;border-radius:0!important;box-shadow:none!important}
html body #project-reading-policy h2{font-size:clamp(26px,3vw,40px)!important;font-weight:500!important}
html body #project-reading-policy p{line-height:1.95!important;color:#bdcdd0!important}
html body :is(.panel,.kpi,.backtest,.backtest-grid>*,.summary,.detail){background:transparent!important;background-image:none!important;border-radius:0!important;box-shadow:none!important}
html body .panel{border:0!important;border-top:1px solid var(--line)!important;padding:24px 0!important}
html body .grid{grid-template-columns:minmax(250px,.32fr) minmax(0,1fr)!important;gap:40px!important}
html body table,html body table :is(thead,tbody,tr,th,td){background:transparent!important;border-radius:0!important;box-shadow:none!important;color:#edf3f2!important}
html body table :is(th,td){font:400 14px/1.8 'Microsoft YaHei',sans-serif!important;padding:15px 16px!important;border-bottom:1px solid var(--line)!important;text-align:left!important}
html body table thead th{color:#bdcdd0!important;border-bottom-color:#cbb783!important}
html body select,html body button.reset{background:transparent!important;color:#edf3f2!important;border:1px solid var(--line)!important;border-radius:0!important;min-height:44px}
html body select option{background:#182128;color:#edf3f2}
html body .control p,html body .note{font-size:14px!important;line-height:1.9!important;color:#bdcdd0!important}
html body input[type=range]{accent-color:#8bc7db}
html body .chart{background:transparent!important;border-radius:0!important;box-shadow:none!important}
@media(max-width:800px){html body .wrap{width:calc(100% - 48px)!important}html body .hero{display:block!important}html body .hero aside{max-width:none!important;margin-top:24px}html body .grid{grid-template-columns:1fr!important}html body .results{min-width:0}html body table{font-size:13px!important}}
"""
st.string += "\nhtml body :is(h2,h3,strong,b,label,summary,caption){color:#edf3f2!important}\nhtml body :is(p,small,.control p,.interval-label,.bt span,.forecast-archive-note){color:#c4d2d6!important;opacity:1!important}\nhtml body .hero p,html body .hero .eyebrow{color:#edf3f2!important}\nhtml body .hero{overflow:hidden!important;background:none!important;position:relative!important;isolation:isolate}\nhtml body .hero>.storm-motion-photo{position:absolute;inset:-4%;z-index:-2;background:url('../../任务三_专题深挖/媒体/la.jpg') center/cover no-repeat;animation:storm-photo-drift 28s ease-in-out infinite alternate;pointer-events:none}\nhtml body .hero>.storm-motion-shade{position:absolute;inset:0;z-index:-1;background:linear-gradient(0deg,#182128,transparent 32%),linear-gradient(90deg,#101e27f5,#101e27d9 58%,#101e2770);pointer-events:none}\n@keyframes storm-photo-drift{from{transform:scale(1.02) translateX(-1%)}to{transform:scale(1.08) translateX(1%)}}\nhtml body .hero.storm-paused .storm-motion-photo{animation-play-state:paused}\nhtml body .storm-motion-toggle{position:absolute;right:6vw;top:20px;background:#182128b3!important;color:#edf3f2!important;border:1px solid #b1c6cc77!important;border-radius:0!important;padding:8px 12px;min-height:40px;cursor:pointer}\n@media(prefers-reduced-motion:reduce){html body .hero>.storm-motion-photo{animation:none!important}html body .storm-motion-toggle{display:none!important}}\n"
st.string += "\nhtml body #project-reading-policy table{width:100%!important;table-layout:fixed!important;border-collapse:collapse!important;background:transparent!important}\nhtml body #project-reading-policy table :is(thead,tbody,tr,th,td),html body #project-reading-policy table tbody tr:nth-child(n)>:is(th,td){background:transparent!important;background-image:none!important;color:#edf3f2!important;box-shadow:none!important;border-radius:0!important}\nhtml body #project-reading-policy table :is(th,td){padding:16px 16px!important;font:400 14px/1.8 'Microsoft YaHei',sans-serif!important;border:0!important;border-bottom:1px solid #94b0ba40!important}\nhtml body #project-reading-policy table thead th:nth-child(n){background:transparent!important;color:#c4d2d6!important;font-size:13px!important;font-weight:500!important;border-bottom:1px solid #cbb783!important}\nhtml body #project-reading-policy table tbody th:nth-child(n){color:#edf3f2!important;font-weight:400!important;text-decoration:none!important}\nhtml body #project-reading-policy table :is(th,td):nth-child(1){width:10%!important;text-align:left!important}\nhtml body #project-reading-policy table :is(th,td):nth-child(2){width:34%!important;text-align:left!important}\nhtml body #project-reading-policy table :is(th,td):nth-child(n+3){width:28%!important;text-align:right!important;font-variant-numeric:tabular-nums!important}\nhtml body #project-reading-policy table caption{font-size:14px!important;color:#c4d2d6!important;text-align:left!important;padding:16px 0!important;font-weight:400!important;line-height:1.8!important}\nhtml body #project-reading-policy a{color:#e3c48a!important;text-decoration:underline!important;text-underline-offset:5px}\n@media(max-width:650px){html body #project-reading-policy table :is(th,td){padding:12px 8px!important;font-size:13px!important}}\n"
st.string += '\nhtml body .wrap>.hero{box-sizing:border-box!important;width:calc(100vw - 17px)!important;margin-left:calc((88vw - (100vw - 17px)) / 2)!important;padding:90px max(6vw,24px) 100px!important;display:grid!important;grid-template-columns:minmax(0,1fr) minmax(230px,320px)!important;gap:48px!important;align-items:center!important;justify-content:initial!important}\nhtml body .hero>.storm-motion-photo,html body .hero>.storm-motion-shade{position:absolute!important;pointer-events:none!important;margin:0!important;padding:0!important}\nhtml body .hero>.storm-motion-photo{inset:-4%!important}\nhtml body .hero>.storm-motion-shade{inset:0!important}\nhtml body .hero>div:not(.storm-motion-photo):not(.storm-motion-shade){min-width:0!important;margin:0!important;transform:none!important;position:relative!important;left:auto!important;max-width:100%!important}\nhtml body .hero h1{max-width:100%!important;font-size:clamp(40px,5vw,78px)!important;overflow-wrap:anywhere!important}\nhtml body .hero aside{width:auto!important;min-width:0!important;margin:0!important;padding-left:20px!important;position:relative!important}\nhtml body .hero .storm-photo-credit{position:absolute!important;left:6vw!important;right:6vw!important;bottom:24px!important;text-align:right!important}\n@media(max-width:800px){html body .wrap>.hero{width:calc(100% + 48px)!important;margin-left:-24px!important;padding:70px 24px 100px!important;grid-template-columns:minmax(0,1fr)!important;gap:24px!important}html body .hero aside{max-width:60ch!important}html body .hero .storm-photo-credit{left:24px!important;right:24px!important}}\n'
st.string += '\nhtml body .wrap>.hero{width:calc(100% / .88)!important;margin-left:calc(-6% / .88)!important;grid-template-columns:minmax(0,1fr)!important;gap:24px!important;padding-bottom:100px!important}\nhtml body .hero>div:not(.storm-motion-photo):not(.storm-motion-shade){max-width:900px!important}\nhtml body .hero aside{max-width:760px!important;border-left:0!important;border-top:1px solid #b1c6cc55!important;padding:16px 0 0!important;font-size:14px!important;line-height:1.85!important;justify-self:start!important}\nhtml body .hero .storm-motion-toggle{position:absolute!important;top:auto!important;bottom:22px!important;left:6vw!important;right:auto!important;background:transparent!important;border:0!important;border-bottom:1px solid #b1c6cc77!important;padding:8px 0!important;font-weight:400!important;font-size:13px!important}\nhtml body .hero .storm-photo-credit{left:auto!important;right:6vw!important;bottom:28px!important;max-width:65%!important}\n@media(max-width:800px){html body .wrap>.hero{width:calc(100% + 48px)!important;margin-left:-24px!important;padding-bottom:120px!important}html body .hero .storm-motion-toggle{left:24px!important;bottom:62px!important}html body .hero .storm-photo-credit{left:24px!important;right:24px!important;bottom:20px!important;max-width:none!important;text-align:left!important}}\n'
hero=s.select_one('.hero')
if hero and not hero.select_one('.storm-photo-credit'):
 credit=s.new_tag('p',attrs={'class':'storm-photo-credit'})
 credit.string='1984年洛杉矶历史影像 · 场景配图'
 link=s.new_tag('a',href='../../任务三_专题深挖/媒体/图片来源与许可.html');link.string=' · 图片来源与许可 ↗';credit.append(link);hero.append(credit)
if hero and not hero.select_one('.storm-motion-photo'):
 for cls in ['storm-motion-photo','storm-motion-shade']:
  layer=s.new_tag('div',attrs={'class':cls,'aria-hidden':'true'});hero.insert(0,layer)
 button=s.new_tag('button',attrs={'class':'storm-motion-toggle','type':'button','aria-pressed':'false'});button.string='暂停背景';hero.append(button)
if not s.select_one('#storm-motion-control'):
 script=s.new_tag('script',id='storm-motion-control')
 script.string="(()=>{const h=document.querySelector('.hero'),b=document.querySelector('.storm-motion-toggle');if(b)b.onclick=()=>{const paused=h.classList.toggle('storm-paused');b.textContent=paused?'播放背景':'暂停背景';b.setAttribute('aria-pressed',String(paused))}})();"
 s.body.append(script)
p.write_text(str(s),encoding='utf8')

import runpy
runpy.run_path(str(root/'项目工作区/scripts/publish_storm_navigation.py'))
