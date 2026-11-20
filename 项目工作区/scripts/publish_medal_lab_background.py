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
html body section.more{background:transparent!important;background-image:none!important;border:0!important;border-top:1px solid #94b0ba55!important;padding:40px 0!important;margin:0!important;min-height:0!important}
html body section.more h2{font-size:clamp(26px,3vw,40px)!important;line-height:1.5!important;font-weight:500!important;letter-spacing:-.025em!important;margin:10px 0 28px!important}
html body section.more .eyebrow{font-size:12px!important;font-weight:500!important;letter-spacing:.08em!important}
html body section.more .more-grid{display:grid!important;grid-template-columns:repeat(3,minmax(0,1fr))!important;gap:32px!important}
html body section.more .more-grid>article{display:flex!important;flex-direction:column!important;gap:0!important;padding:24px 0 0!important;margin:0!important;background:transparent!important;background-image:none!important;border:0!important;border-top:1px solid #94b0ba55!important;border-radius:0!important;box-shadow:none!important;min-width:0!important}
html body section.more article>strong{font-size:22px!important;line-height:1.5!important;font-weight:500!important;color:#edf3f2!important}
html body section.more article p{font-size:15px!important;line-height:1.95!important;color:#c0d0d4!important;margin:14px 0 20px!important}
html body section.more article a{align-self:flex-start!important;margin-top:auto!important;padding:8px 0!important;font-size:15px!important;color:#e3c48a!important}
@media(max-width:800px){html body section.more .more-grid{grid-template-columns:1fr!important;gap:24px!important}html body section.more{padding:28px 0!important}}

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
label=s.select_one('section.more .eyebrow')
if label:label.string='证据与方法'
p.write_text(str(s),encoding='utf-8')

# Preserve conclusion-adjacent evidence notes after regeneration.
from publish_evidence_closure import main as publish_closure_notes
publish_closure_notes()
