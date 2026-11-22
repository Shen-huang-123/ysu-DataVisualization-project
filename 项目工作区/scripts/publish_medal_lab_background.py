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

/* Keep the chart and the selected delegation on the same reading line. */
html body .wrap{max-width:1680px!important;width:100%!important;padding-inline:clamp(20px,4vw,68px)!important}
html body .hero{padding-block:clamp(32px,5vw,72px) clamp(24px,3.5vw,46px);gap:clamp(24px,5vw,72px);align-items:center}
html body .hero h1{font-size:clamp(38px,5.1vw,76px);line-height:1.12;letter-spacing:-.045em;margin:12px 0 18px}
html body .hero-aside{font-size:15px;line-height:1.8}
html body .hero-aside strong{font-size:clamp(19px,2vw,26px);margin-bottom:8px}
html body .controls{gap:12px;padding:14px 0}
html body .lens-switch{border-radius:9px;background:#111c24}
html body .lens-switch button{min-height:44px;border-radius:6px;padding:8px 12px;white-space:nowrap}
html body .lens-switch button[aria-pressed="true"]{background:#ebce91!important;color:#17212a!important}
html body main.grid{display:grid!important;grid-template-columns:minmax(0,1.65fr) minmax(320px,1fr);align-items:start;gap:clamp(24px,3vw,48px)!important;min-width:0!important}
html body main.grid>.panel{width:100%!important;max-width:none!important;background:transparent!important;border:0!important;border-radius:0!important;box-shadow:none!important;padding:20px 0!important;border-top:2px solid #6a8a96!important}
html body main.grid>.ex-route{grid-column:1/-1;order:-1;width:100%!important;margin:0!important;min-height:0!important}
html body main.grid>.case{min-height:0!important;border-top-color:#ebce91!important}
html body .case .shift strong{color:#ebce91;font-variant-numeric:tabular-nums}
html body .metric-row{gap:0;border-block:1px solid #526771}
html body .metric{min-width:0;border:0;border-radius:0;background:transparent;padding:10px 9px}
html body .metric+.metric{border-inline-start:1px solid #526771}
html body #rank-chart{width:100%!important;background:transparent!important;border:0!important;box-shadow:none!important;border-radius:0!important}
html body #sport-removal-result{background:#24343d;border-inline-start:3px solid #ebce91;padding:12px 14px;line-height:1.65}
html body #sport-removal-audit summary{cursor:pointer;padding-block:10px;color:#ebce91}
html body #sport-removal-audit table{border-collapse:collapse;font-size:.82rem;line-height:1.5}
html body #sport-removal-audit :is(th,td){padding:8px 6px;text-align:start;border-bottom:1px solid #526771}
html body #sport-removal a{color:#ebce91;text-decoration:underline;text-underline-offset:3px}
@media(max-width:900px){
 html body main.grid{grid-template-columns:minmax(0,1fr);gap:24px!important}
 html body .hero{grid-template-columns:minmax(0,1fr)}
}
@media(max-width:480px){
 html body .controls .spacer{display:none}
 html body .lens-switch{width:100%;justify-content:space-between;gap:2px}
 html body .lens-switch button{font-size:.82rem;padding-inline:8px}
}
"""
eyebrow=s.select_one('.hero .eyebrow')
if eyebrow:eyebrow.string='巴黎 2024 · 奖牌口径实验室'
title=s.select_one('.hero h1')
if title:
 title.clear()
 title.append('换一种计数，')
 title.append(s.new_tag('br'))
 title.append('奖牌榜如何重排？')
label=s.select_one('section.more .eyebrow')
if label:label.string='证据与方法'
p.write_text(str(s),encoding='utf-8')

# Preserve conclusion-adjacent evidence notes after regeneration.
from publish_evidence_closure import main as publish_closure_notes
publish_closure_notes()
