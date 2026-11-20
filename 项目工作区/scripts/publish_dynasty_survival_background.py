from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[2]
p=root/'交付文件/任务三_专题深挖/S3_冠军的保质期/07_王朝生存图/index.html'
s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
st=s.select_one('#dynasty-survival-background')
if not st:st=s.new_tag('style',id='dynasty-survival-background');s.head.append(st)
st.string="""
html body.ip-dynasty main .scroll{background:transparent!important;border:0!important;border-radius:0!important;box-shadow:none!important;overflow-x:auto!important}
html body.ip-dynasty main .scroll table{table-layout:fixed!important;min-width:740px!important;background:transparent!important}
html body.ip-dynasty main .scroll table :is(thead,tbody,tr,th,td){background:transparent!important;background-image:none!important;border-radius:0!important;box-shadow:none!important;color:var(--ink)!important}
html body.ip-dynasty main .scroll table :is(th,td){padding:17px 16px!important;border:0!important;border-bottom:1px solid var(--line)!important;font-size:15px!important;font-weight:400!important;line-height:1.7!important;font-variant-numeric:tabular-nums!important}
html body.ip-dynasty main .scroll table th{font-size:13px!important;color:var(--muted)!important;border-top:1px solid var(--line)!important;font-weight:500!important}
html body.ip-dynasty main .scroll table :is(th,td):nth-child(1){width:12%!important}
html body.ip-dynasty main .scroll table :is(th,td):nth-child(2){width:40%!important;overflow-wrap:anywhere}
html body.ip-dynasty main .scroll table :is(th,td):nth-child(3){width:15%!important}
html body.ip-dynasty main .scroll table :is(th,td):nth-child(4){width:20%!important;white-space:nowrap}
html body.ip-dynasty main .scroll table :is(th,td):nth-child(5){width:13%!important;text-align:right!important}
html body.ip-dynasty main .scroll table tbody tr:hover td{background:#8aaeb014!important}
/* Match the task pages' shared table typography and theme tokens. */
html body.ip-dynasty main .scroll table :is(th,td){padding:18px 16px!important;font-size:14px!important;line-height:1.8!important;color:var(--ut-ink)!important;border-bottom:1px solid var(--ut-line)!important;text-align:left!important}
html body.ip-dynasty main .scroll table thead th:nth-child(n){background:var(--ut-head)!important;color:var(--ut-muted)!important;font-size:13px!important;font-weight:600!important;border-top:0!important;border-bottom:1px solid var(--ut-gold)!important;text-align:left!important}
html body.ip-dynasty main .scroll table tbody tr:hover td{background:transparent!important}
html body.ip-dynasty main .scroll table :is(th,td):nth-child(5){text-align:left!important}
@media(max-width:650px){html body.ip-dynasty main .scroll table :is(th,td){padding:13px 12px!important;font-size:13px!important}}
html body.ip-dynasty #dynasty-table-note{font-size:14px!important;color:var(--muted)!important;line-height:1.9!important;margin:16px 0 0!important}

html body.ip-dynasty main.wrap,html body.ip-dynasty footer.wrap{width:100%!important;max-width:none!important;padding-inline:6vw!important;box-sizing:border-box!important}
html body.ip-dynasty main>section{padding:40px 0!important;margin:0!important;border-bottom:1px solid var(--line)!important}
html body.ip-dynasty main h2{font-family:inherit!important;font-weight:500!important;font-size:clamp(26px,3vw,42px)!important;line-height:1.5!important;letter-spacing:-.025em!important;color:var(--ink)!important}
html body.ip-dynasty main .ip-eyebrow{font:500 13px/1.8 'Microsoft YaHei',sans-serif!important;color:var(--muted)!important}
html body.ip-dynasty main .controls{display:flex!important;flex-wrap:wrap!important;gap:20px!important;background:transparent!important;border:0!important;border-radius:0!important;box-shadow:none!important;padding:20px 0!important}
html body.ip-dynasty main .controls label{display:grid;gap:8px;min-width:min(240px,100%);font-size:14px!important;color:var(--ink)!important}
html body.ip-dynasty main .grid{display:grid!important;grid-template-columns:repeat(3,minmax(0,1fr))!important;gap:32px!important}
html body.ip-dynasty main .grid>.card{background:transparent!important;background-image:none!important;border:0!important;border-top:1px solid var(--line)!important;border-radius:0!important;box-shadow:none!important;padding:20px 0!important;transform:none!important;color:var(--ink)!important}
html body.ip-dynasty main .metric{font-size:clamp(32px,4vw,52px)!important;color:var(--ink)!important;font-weight:500!important}
html body.ip-dynasty main .chart{background:transparent!important;border:0!important;border-radius:0!important;box-shadow:none!important;padding:18px 0!important;overflow-x:auto!important}
html body.ip-dynasty #curve{display:block;width:100%!important;min-width:620px;height:auto!important}
html body.ip-dynasty main .note,html body.ip-dynasty main .muted{color:var(--muted)!important;font-size:15px!important;line-height:1.95!important}
html body.ip-dynasty main table{width:100%!important;border-radius:0!important;box-shadow:none!important}
@media(max-width:650px){html body.ip-dynasty main.wrap,html body.ip-dynasty footer.wrap{padding-inline:24px!important}html body.ip-dynasty main .grid{grid-template-columns:1fr!important;gap:8px!important}html body.ip-dynasty main>section{padding:28px 0!important}}

html body.ip-dynasty{--ds-bg:#f2f3ee;background:var(--ds-bg)!important;background-image:none!important}
html body.ip-dynasty.xz-dark{--ds-bg:#182128;--ink:#edf3f2;--muted:#c0d0d4;background:var(--ds-bg)!important}
html body.ip-dynasty .oa-world{display:none!important}
html body.ip-dynasty::before,html body.ip-dynasty::after{background:none!important;box-shadow:none!important}
html body.ip-dynasty header.photo-editorial-hero.image-stage::before{background:linear-gradient(0deg,var(--ds-bg),transparent 28%),linear-gradient(90deg,#07191fd9, #07191f55 58%,transparent)!important}
html body.ip-dynasty header.photo-editorial-hero:not(.image-stage){background-image:linear-gradient(0deg,var(--ds-bg),transparent 28%),linear-gradient(90deg,#07191fd9,#07191f33),url('../../媒体/dynasty.jpg')!important}
html body.ip-dynasty.xz-dark main :is(h2,h3){color:#edf3f2!important}
html body.ip-dynasty.xz-dark main .ip-eyebrow{color:#d8be89!important}
html body.ip-dynasty .photo-editorial-credit{display:block!important;width:auto!important;max-width:none!important;margin:14px 6vw 0!important;padding:8px 0!important;border:0!important;border-radius:0!important;box-shadow:none!important;background:transparent!important;color:var(--ink)!important;text-align:right;font-size:12px!important}
"""
table=s.select_one('main .scroll table')
if table:
 table['aria-describedby']='dynasty-table-note'
 note=s.select_one('#dynasty-table-note')
 if not note:
  note=s.new_tag('p',id='dynasty-table-note');table.parent.insert_after(note)
 note.string='* 表示截至2016年仍在延续，按右删失处理；连续届数为已观察到的长度。'
p.write_text(str(s),encoding='utf-8')

import runpy
runpy.run_path(str(root/'项目工作区/scripts/publish_survival_interval_svg.py'))
