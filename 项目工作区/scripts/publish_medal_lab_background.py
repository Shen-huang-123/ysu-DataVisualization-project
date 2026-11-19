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
/* This lab has a permanent dark canvas and no shared xz-dark theme class. */
html body .native-evidence{--ne-ink:#edf3f2;--ne-muted:#c0d0d4;--ne-line:#94b0ba88;--ne-a:#8bc7db;--ne-b:#e5a0ae;color:var(--ne-ink)!important}
html body .native-evidence h3{color:#edf3f2!important;font-size:26px!important}
html body .native-evidence svg text{fill:#edf3f2!important}
html body .native-evidence svg .ne-muted{fill:#c0d0d4!important;font-size:13px!important}
html body .native-evidence svg .ne-on{fill:#10212a!important;font-weight:700!important}
html body .native-evidence .ne-grid{stroke:#94b0ba88!important;stroke-width:1.3}
html body .native-evidence figcaption{color:#c0d0d4!important;font-size:14px!important}

html body .wrap{max-width:none!important;width:100%!important;padding-inline:4vw!important}
html body main.grid{display:flex!important;flex-direction:column!important;gap:32px!important;min-width:0!important}
html body main.grid>.panel{width:100%!important;max-width:none!important;background:transparent!important;background-image:none!important;border:0!important;border-radius:0!important;box-shadow:none!important;padding:26px 0!important;border-top:1px solid var(--line)!important}
html body main.grid>.ex-route{order:-1;width:100%!important;margin:0!important;min-height:0!important;align-self:stretch!important}
html body main.grid>.case{min-height:0!important}
html body #rank-chart{width:100%!important;background:transparent!important;border:0!important;box-shadow:none!important;border-radius:0!important}
@media(max-width:650px){html body .wrap{padding-inline:24px!important}html body main.grid{gap:24px!important}}
"""
p.write_text(str(s),encoding='utf-8')
