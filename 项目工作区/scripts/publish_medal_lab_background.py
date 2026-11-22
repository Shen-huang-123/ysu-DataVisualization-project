from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[2]
p=root/'交付文件/任务三_专题深挖/S2_口径的魔力/09_奖牌口径实验室/index.html'
s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
s.select_one('main.grid')['data-medal-route']=''
style=s.select_one('#medal-lab-background')
if not style:
 style=s.new_tag('style',id='medal-lab-background');s.head.append(style)
backdrop = s.select_one('.medal-lab-backdrop')
if not backdrop:
 backdrop = s.new_tag('div', attrs={'class':'medal-lab-backdrop','aria-hidden':'true'})
 s.body.insert(0, backdrop)
style.string="""/* Keep the moving light behind the reading surface. */
html body{isolation:isolate}
html body .medal-lab-backdrop{
 position:fixed;inset:0;z-index:-1;overflow:hidden;pointer-events:none;
}
.medal-lab-backdrop::before,.medal-lab-backdrop::after{
 content:"";position:absolute;width:min(75vw,1100px);height:78vh;
}
.medal-lab-backdrop::before{
 top:-26vh;right:-15vw;
 background:radial-gradient(ellipse at center,rgba(66,144,172,.36),transparent 70%);
 animation:medal-lab-drift 24s ease-in-out infinite alternate;
}
.medal-lab-backdrop::after{
 bottom:-39vh;left:-20vw;
 background:radial-gradient(ellipse at center,rgba(196,151,82,.24),transparent 72%);
 animation:medal-lab-drift 32s ease-in-out -12s infinite alternate-reverse;
}
@keyframes medal-lab-drift{
 from{transform:translate3d(0,0,0)}
 to{transform:translate3d(-8vw,17vh,0)}
}
@media(prefers-reduced-motion:reduce){
 .medal-lab-backdrop::before,.medal-lab-backdrop::after{animation:none}
}
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
html body .hero{display:block;padding-block:clamp(30px,4vw,54px) 24px}
html body .hero .eyebrow{font-size:.78rem;letter-spacing:.06em}
html body .hero h1{font-size:clamp(32px,4.3vw,64px);line-height:1.16;letter-spacing:-.04em;margin:10px 0 12px}
html body .hero p{max-width:58ch;line-height:1.65}
html body .medal-method{margin-top:12px;color:#c0d0d4;font-size:.85rem;line-height:1.65;max-width:72ch}
html body .medal-method summary{cursor:pointer;color:#ebce91;width:fit-content}
html body .medal-method p{margin:6px 0 0}
html body .controls{gap:12px;padding:10px 0}
html body .lens-switch{border:0;border-radius:0;background:transparent;padding:0}
html body .lens-switch button{min-height:44px;border-radius:0;padding:8px 12px;white-space:nowrap;border-bottom:2px solid transparent}
html body .lens-switch button[aria-pressed="true"]{background:transparent!important;color:#ebce91!important;border-bottom-color:#ebce91}
html body #rank-discovery{margin:18px 0 0;padding:14px 0 0;border:0;border-top:1px solid #526771;border-radius:0;background:transparent;box-shadow:none}
html body #rank-discovery h2{font-size:1.05rem;margin:0 0 8px}
html body main.grid{display:grid!important;grid-template-columns:minmax(0,1.65fr) minmax(320px,1fr);align-items:start;gap:clamp(24px,3vw,48px)!important;min-width:0!important}
html body main.grid>.panel{width:100%!important;max-width:none!important;background:transparent!important;border:0!important;border-radius:0!important;box-shadow:none!important;padding:20px 0!important;border-top:2px solid #6a8a96!important}
html body main.grid>.ex-route{grid-column:1/-1;order:1;width:100%!important;margin:0!important;min-height:0!important}
html body main.grid>.medal-route{
 --route-ink:#f3f5f2;--route-muted:#c5d1d5;--route-line:#607782;--route-accent:#ebce91;
 background:transparent!important;border:0;border-top:1px solid var(--route-line);
 border-radius:0;padding:14px 0 0!important;
}
html body main.grid>.medal-route h2{font-size:.9rem;margin:0;color:var(--route-muted)}
html body main.grid>.medal-route>nav{
 grid-template-columns:repeat(3,minmax(0,1fr))!important;
 gap:6px 24px!important;margin:8px 0 10px!important;
}
html body main.grid>.medal-route>nav>a{
 border:0!important;padding:8px 0!important;font-size:1rem;text-decoration:underline;
 text-decoration-color:#607782;text-underline-offset:5px;
}
html body main.grid>.medal-route .ex-tools{margin-bottom:0!important}
@media(max-width:540px){
 html body main.grid>.medal-route>nav{grid-template-columns:1fr!important;gap:0!important}
}
html body main.grid>.case{min-height:0!important;border-top-color:#ebce91!important}
html body .case .shift strong{color:#ebce91;font-variant-numeric:tabular-nums}
html body #medal-rank-comparison{margin:0 0 18px;padding:12px 0;border-block:1px solid #526771}
html body #medal-rank-heading{font-size:1rem;margin:0 0 12px}
.medal-rank-axis{display:flex;justify-content:space-between;margin-inline:6em 4.6em;color:#c0d0d4;font-size:.75rem}
#medal-rank-comparison dl{margin:4px 0 0}
#medal-rank-comparison dl>div{display:grid;grid-template-columns:5em minmax(0,1fr);gap:10px;align-items:center;padding:6px 0;font-size:.82rem}
#medal-rank-comparison dd{display:grid;grid-template-columns:minmax(0,1fr) 4em;gap:10px;align-items:center;margin:0}
#medal-rank-comparison b{text-align:end;font-variant-numeric:tabular-nums;white-space:nowrap}
.medal-rank-track{position:relative;display:block;height:2px;background:#647b84}
.medal-rank-track::after{content:"";position:absolute;top:50%;left:var(--position);width:9px;height:9px;border-radius:50%;background:#8bc7db;transform:translate(-50%,-50%)}
#medal-rank-comparison .is-active{color:#ebce91;font-weight:700}
#medal-rank-comparison .is-active .medal-rank-track::after{background:#ebce91}
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
if title:title.string='换一种计数，奖牌榜如何重排？'
intro=s.select_one('.hero > div > p')
if intro:intro.string='切换巴黎 2024 的三种奖牌口径，比较 91 个代表团的名次与金牌构成。'
aside=s.select_one('.hero-aside')
if aside:
 method=s.new_tag('details',attrs={'class':'medal-method'})
 summary=s.new_tag('summary')
 summary.string='这三种口径怎么数？'
 method.append(summary)
 paragraph=s.new_tag('p')
 paragraph.string=aside.get_text().removeprefix('同一组比赛结果，三种回答。')
 method.append(paragraph)
 aside.replace_with(method)
feedback=s.select_one('#rank-discovery')
chart=s.select_one('#rank-chart')
if feedback and chart:chart.insert_after(feedback.extract())
label=s.select_one('section.more .eyebrow')
if label:label.string='证据与方法'
comparison = s.select_one('#medal-rank-comparison')
if not comparison:
 comparison = BeautifulSoup("""<section id="medal-rank-comparison" aria-labelledby="medal-rank-heading" hidden>
 <h3 id="medal-rank-heading">三种口径的名次</h3>
 <div class="medal-rank-axis" aria-hidden="true"><span>第 1 名</span><span id="medal-rank-end"></span></div>
 <dl>
 <div data-rank-lens="official"><dt>官方小项</dt><dd><span class="medal-rank-track" aria-hidden="true"></span><b></b></dd></div>
 <div data-rank-lens="fractional"><dt>团队内均分</dt><dd><span class="medal-rank-track" aria-hidden="true"></span><b></b></dd></div>
 <div data-rank-lens="rows"><dt>运动员行</dt><dd><span class="medal-rank-track" aria-hidden="true"></span><b></b></dd></div>
 </dl>
 </section>""", 'html.parser').section
 s.select_one('.case .shift').insert_after(comparison)
behavior = s.select_one('#medal-rank-comparison-script')
if not behavior:
 behavior = s.new_tag('script', id='medal-rank-comparison-script')
 s.body.append(behavior)
behavior.string = """
(() => {
  const panel = document.getElementById('medal-rank-comparison');
  const chooser = document.getElementById('case-select');
  const {cases} = JSON.parse(document.getElementById('lab-data').textContent);
  const byNoc = new Map(cases.map(item => [item.noc, item]));
  const lenses = [...panel.querySelectorAll('[data-rank-lens]')];
  const lastRank = Math.max(...cases.flatMap(item => lenses.map(row => item[row.dataset.rankLens].rank)));
  document.getElementById('medal-rank-end').textContent = '第 ' + lastRank + ' 名';
  function renderRanks() {
    const item = byNoc.get(chooser.value);
    if (!item) return;
    for (const row of lenses) {
      const lens = row.dataset.rankLens;
      const rank = item[lens].rank;
      const active = document.querySelector('[data-lens="' + lens + '"]').getAttribute('aria-pressed') === 'true';
      row.classList.toggle('is-active', active);
      row.querySelector('.medal-rank-track').style.setProperty('--position', (rank - 1) * 100 / Math.max(1, lastRank - 1) + '%');
      row.querySelector('b').textContent = '第 ' + rank + ' 名';
    }
    panel.hidden = false;
  }
  chooser.addEventListener('change', renderRanks);
  new MutationObserver(renderRanks).observe(document.getElementById('case-shift'), {childList:true, subtree:true});
  renderRanks();
})();
"""
p.write_text(str(s),encoding='utf-8')

# Preserve conclusion-adjacent evidence notes after regeneration.
from publish_evidence_closure import main as publish_closure_notes
publish_closure_notes()
