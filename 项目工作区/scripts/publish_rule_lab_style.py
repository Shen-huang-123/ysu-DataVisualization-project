from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[2]
p=root/'交付文件/任务三_专题深挖/S2_口径的魔力/07_口径实验室/index.html'
s=BeautifulSoup(p.read_text(encoding='utf8'),'html.parser')
st=s.select_one('#rule-lab-refined')
if not st:st=s.new_tag('style',id='rule-lab-refined');s.head.append(st)
st.string="""
html body.ip-lab main .scroll table{table-layout:fixed!important}
html body.ip-lab main .scroll table :is(thead,tbody,tr,th,td),html body.ip-lab main .scroll table tbody#board tr:nth-child(n),html body.ip-lab main .scroll table tbody#board tr:nth-child(n)>td:nth-child(n){background:transparent!important;background-color:transparent!important;background-image:none!important;box-shadow:none!important;border-radius:0!important}
html body.ip-lab main .scroll table :is(th,td){padding:16px!important;line-height:1.8!important;font-size:14px!important;border-bottom:1px solid var(--line)!important;color:var(--ink)!important;font-weight:400!important;font-variant-numeric:tabular-nums}
html body.ip-lab main .scroll table :is(th,td):nth-child(1){width:10%!important;text-align:left!important}
html body.ip-lab main .scroll table :is(th,td):nth-child(2){width:30%!important;text-align:left!important}
html body.ip-lab main .scroll table :is(th,td):nth-child(n+3){width:20%!important;text-align:right!important}
html body.ip-lab main .scroll table thead th:nth-child(n){color:var(--muted)!important;font-size:13px!important;border-bottom:1px solid #a28c5e!important}
html body.ip-lab main .scroll table tbody#board tr[style]>td:nth-child(2){text-decoration:underline;text-decoration-color:var(--teal);text-underline-offset:6px;text-decoration-thickness:2px}
html body.ip-lab main .scroll table tbody#board tr[style]>td{border-bottom-color:var(--teal)!important}
@media(max-width:650px){html body.ip-lab main .scroll table :is(th,td){padding:12px!important;font-size:13px!important}}

html body.ip-lab main.wrap{padding-top:0!important;margin-top:0!important}
html body.ip-lab main.wrap>section:first-child{padding-top:24px!important}
html body.ip-lab .photo-editorial-credit{margin:0 6vw!important;padding:12px 0!important;min-height:0!important;line-height:1.6!important;display:block!important;max-width:none!important}

html body.ip-lab main .controls:is(.controls,#rule-controls){display:grid!important;grid-template-columns:minmax(240px,1fr) 64px minmax(220px,.6fr)!important;align-items:end!important;gap:24px!important;padding:24px 0!important;background:transparent!important;background-color:transparent!important;background-image:none!important;border:0!important;border-top:1px solid var(--line)!important;border-radius:0!important;box-shadow:none!important}
html body.ip-lab main .controls label{display:grid!important;gap:14px!important;min-width:0!important;font-size:14px!important;line-height:1.8!important}
html body.ip-lab main .controls #alpha{display:block!important;width:100%!important;min-width:0!important;margin:0!important;height:46px!important;background:transparent!important;border:0!important;box-shadow:none!important}
html body.ip-lab main .controls #weight{align-self:end!important;display:flex!important;align-items:center!important;height:46px!important;padding:0!important;background:transparent!important;border:0!important;box-shadow:none!important;font-size:20px!important;color:var(--ink)!important}
html body.ip-lab main .controls #noc{width:100%!important;min-height:46px!important;background:transparent!important;border:0!important;border-bottom:1px solid var(--line)!important;border-radius:0!important;box-shadow:none!important;color:var(--ink)!important;font-weight:400!important}
html body.ip-lab main .controls #noc option{background:var(--bg)!important;color:var(--ink)!important}
@media(max-width:650px){html body.ip-lab main .controls:is(.controls,#rule-controls){grid-template-columns:minmax(0,1fr) 54px!important;gap:16px!important}html body.ip-lab main .controls label:last-child{grid-column:1/-1!important}}

html body.ip-lab{padding-top:0!important;margin-top:0!important}
html body.ip-lab>header.photo-editorial-hero.image-stage,html body.ip-lab>header.photo-editorial-hero{margin-top:0!important;min-height:100svh!important;width:100%!important;box-sizing:border-box!important;padding:130px 6vw 100px!important}
html body.ip-lab>header.photo-editorial-hero>.wrap{width:100%!important;max-width:none!important;padding:0!important;margin:0!important}
html body.ip-lab #xz-nav{background:transparent!important;border:0!important;box-shadow:none!important}
@media(max-width:650px){html body.ip-lab>header.photo-editorial-hero.image-stage,html body.ip-lab>header.photo-editorial-hero{padding:110px 24px 90px!important}}

html body.ip-lab{background:#f2f3ee!important;background-image:none!important}
html body.ip-lab.xz-dark{background:#182128!important;--ink:#edf3f2;--muted:#c0d0d4;--line:#94b0ba40}
html body.ip-lab .oa-world{display:none!important}
html body.ip-lab::before{background:none!important}
html body.ip-lab main.wrap,html body.ip-lab footer.wrap{width:100%!important;max-width:none!important;padding-inline:6vw!important;box-sizing:border-box!important}
html body.ip-lab main>section{margin:0!important;padding:40px 0!important;border-bottom:1px solid var(--line)!important}
html body.ip-lab main h2{font:500 clamp(26px,3vw,42px)/1.5 'Microsoft YaHei',sans-serif!important;color:var(--ink)!important}
html body.ip-lab main :is(.muted,.note,small){color:var(--muted)!important;line-height:1.9!important;font-size:14px!important}
html body.ip-lab main .controls{display:flex!important;flex-wrap:wrap!important;gap:24px!important;background:transparent!important;border:0!important;border-radius:0!important;box-shadow:none!important;padding:24px 0!important}
html body.ip-lab main .controls label{color:var(--ink)!important;font-weight:400!important;min-width:min(240px,100%)}
html body.ip-lab main .controls input[type=range]{accent-color:var(--teal);min-width:200px}
html body.ip-lab main .grid{display:grid!important;grid-template-columns:repeat(3,minmax(0,1fr))!important;gap:32px!important}
html body.ip-lab main .grid>.card:nth-child(n){background:transparent!important;background-image:none!important;border:0!important;border-top:1px solid var(--line)!important;border-radius:0!important;box-shadow:none!important;padding:20px 0!important;transform:none!important;color:var(--ink)!important}
html body.ip-lab main .metric{font:500 clamp(30px,4vw,52px)/1.4 'Microsoft YaHei',sans-serif!important;color:var(--ink)!important}
html body.ip-lab main :is(.scroll,.pill,.cards2>*){background:transparent!important;background-image:none!important;border-radius:0!important;box-shadow:none!important}
html body.ip-lab main .scroll{overflow-x:auto!important;border:0!important}
html body.ip-lab main table{width:100%!important;min-width:660px!important;border-collapse:collapse!important;box-shadow:none!important;border-radius:0!important;background:transparent!important}
html body.ip-lab main table :is(thead,tbody,tr,th,td),html body.ip-lab main table tbody#board tr:nth-child(n)>*{background:transparent!important;background-image:none!important;color:var(--ink)!important;box-shadow:none!important}
html body.ip-lab main table :is(th,td){font:400 14px/1.8 'Microsoft YaHei',sans-serif!important;padding:16px!important;border:0!important;border-bottom:1px solid var(--line)!important;text-align:left!important;font-variant-numeric:tabular-nums}
html body.ip-lab main table thead th{color:var(--muted)!important;font-size:13px!important;border-bottom-color:#a28c5e!important}
html body.ip-lab main .cards2>*{border:0!important;border-top:1px solid var(--line)!important;padding:20px 0!important;color:var(--ink)!important}
html body.ip-lab .photo-editorial-credit{background:transparent!important;border:0!important;border-radius:0!important;color:var(--ink)!important}
@media(max-width:650px){html body.ip-lab main.wrap,html body.ip-lab footer.wrap{padding-inline:24px!important}html body.ip-lab main .grid{grid-template-columns:1fr!important;gap:8px!important}html body.ip-lab main>section{padding:28px 0!important}}
"""
st.string += '\nhtml body.ip-lab main .scroll table :is(th,td):nth-child(n){text-align:left!important;padding:18px 16px!important;font-size:14px!important;line-height:1.8!important;color:var(--ut-ink,var(--ink))!important;font-weight:400!important;border-bottom:1px solid var(--ut-line,var(--line))!important}\nhtml body.ip-lab main .scroll table thead th:nth-child(n){color:var(--ut-muted,var(--muted))!important;font-size:13px!important;font-weight:600!important;border-bottom:1px solid var(--ut-gold,#a28c5e)!important;background:transparent!important}\nhtml body.ip-lab main .scroll table tbody#board tr[style]>td{border-bottom-color:var(--ut-line,var(--line))!important}\nhtml body.ip-lab main .scroll table tbody#board tr[style]>td:nth-child(2){text-decoration-color:var(--ut-gold,#a28c5e)!important;text-decoration-thickness:1px!important}\n@media(max-width:650px){html body.ip-lab main .scroll table :is(th,td):nth-child(n){padding:13px 12px!important;font-size:13px!important}}\n'
p.write_text(str(s),encoding='utf8')
