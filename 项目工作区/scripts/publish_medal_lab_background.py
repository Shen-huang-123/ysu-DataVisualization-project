from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[2]
p=root/'交付文件/任务三_专题深挖/S2_口径的魔力/09_奖牌口径实验室/index.html'
s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
style=s.select_one('#medal-lab-background')
if not style:
 style=s.new_tag('style',id='medal-lab-background');s.head.append(style)
style.string="""/* Local reading surface: no decorative water ribbons behind evidence. */
html body{background:#182128!important;background-image:none!important}
html body .oa-world,html body .immersive-float-layer{display:none!important}
html body::before,html body::after{background:none!important;background-image:none!important;box-shadow:none!important}
html body.xz-dark{background:#182128!important}
html body .wrap{max-width:none!important;width:100%!important;padding-inline:4vw!important}
html body main.grid{display:flex!important;flex-direction:column!important;gap:32px!important;min-width:0!important}
html body main.grid>.panel{width:100%!important;max-width:none!important;background:transparent!important;background-image:none!important;border:0!important;border-radius:0!important;box-shadow:none!important;padding:26px 0!important;border-top:1px solid var(--line)!important}
html body main.grid>.ex-route{order:-1;width:100%!important;margin:0!important;min-height:0!important;align-self:stretch!important}
html body main.grid>.case{min-height:0!important}
html body #rank-chart{width:100%!important;background:transparent!important;border:0!important;box-shadow:none!important;border-radius:0!important}
@media(max-width:650px){html body .wrap{padding-inline:24px!important}html body main.grid{gap:24px!important}}
"""
p.write_text(str(s),encoding='utf-8')
