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
hero=s.select_one('.hero')
if hero and not hero.select_one('.storm-photo-credit'):
 credit=s.new_tag('p',attrs={'class':'storm-photo-credit'})
 credit.string='1984年洛杉矶历史影像 · 场景配图'
 link=s.new_tag('a',href='../../任务三_专题深挖/媒体/图片来源与许可.html');link.string=' · 图片来源与许可 ↗';credit.append(link);hero.append(credit)
p.write_text(str(s),encoding='utf8')
