from pathlib import Path
import csv,re
ROOT=Path(__file__).resolve().parents[2]
data=ROOT/'交付文件/任务三_专题深挖/S1_东道主效应/01_来源与口径敏感性/三方案共同案例摘要.csv'
rows=list(csv.DictReader(data.open(encoding='utf-8-sig')))
css='''<style id="host-interval-style">#host-source-sensitivity .host-interval{margin:28px 0 36px;padding:24px 0;border-block:1px solid #829a9b55;color:inherit;background:transparent;font-family:"Microsoft YaHei",sans-serif}#host-source-sensitivity .host-interval figcaption{font-size:18px;font-weight:600;margin-bottom:8px}#host-source-sensitivity .hi-note{font-size:13px;opacity:.72;margin-bottom:24px}.hi-row,.hi-axis{display:grid;grid-template-columns:180px minmax(0,1fr) 220px;gap:24px;align-items:center}.hi-row{min-height:100px;border-bottom:1px solid #829a9b30}.hi-label{font-size:15px}.hi-value{font-size:22px;font-variant-numeric:tabular-nums}.hi-value small{display:block;font-size:12px;opacity:.7}.hi-plot svg{display:block;width:100%;height:64px;overflow:visible}.hi-axis{font-size:12px;opacity:.7;margin-top:12px}.hi-ticks{display:flex;justify-content:space-between}.hi-value,.hi-label{color:inherit}.hi-row{--hi-color:#78aabb}.hi-row:last-of-type{--hi-color:#c68e9d}@media(max-width:650px){.hi-row,.hi-axis{grid-template-columns:1fr;gap:6px}.hi-row{padding:18px 0}.hi-value{font-size:20px;display:flex;align-items:baseline;gap:14px}.hi-axis>span{display:none}.hi-plot svg{height:48px}.hi-row{min-height:0}}</style>'''
parts=[]
for i,r in enumerate(rows):
 x,lo,hi=[float(r[k]) for k in ['平均差值','区间下限','区间上限']]
 grid=''.join(f'<line x1="{v*100}" x2="{v*100}" y1="0" y2="64" stroke="currentColor" opacity=".12"/>' for v in range(7))
 plot=f'<svg viewBox="0 0 600 64" preserveAspectRatio="none" aria-hidden="true">{grid}<line x1="0" x2="0" y1="0" y2="64" stroke="currentColor" opacity=".5" stroke-dasharray="3 4"/><path d="M{lo*100} 24v16 M{lo*100} 32H{hi*100} M{hi*100} 24v16" fill="none" stroke="var(--hi-color)" stroke-width="3" vector-effect="non-scaling-stroke"/><circle cx="{x*100}" cy="32" r="5" fill="var(--hi-color)"/></svg>'
 name=['小项原代理','二次来源替换','排除未决同名系列'][i]
 parts.append(f'<div class="hi-row"><div class="hi-label">{name}</div><div class="hi-plot">{plot}</div><div class="hi-value">{x:+.2f}<small>95%区间 [{lo:+.2f}, {hi:+.2f}]</small></div></div>')
figure='<figure class="host-interval" aria-label="同15个主办案例，三方案平均差值及案例成组95%区间"><figcaption>三种来源方案，平均关联均为正</figcaption><div class="hi-note">同15个主办案例 · 圆点为平均差值，横线为案例成组95%区间；不代表每届都受益</div>'+''.join(parts)+'<div class="hi-axis"><span>主办届 − 合成对照</span><div class="hi-ticks">'+''.join(f'<span>{i}</span>' for i in range(7))+'</div><span>单位：百分点</span></div></figure>'
for p in (ROOT/'交付文件').rglob('*.html'):
 text=p.read_text(encoding='utf-8-sig')
 if 'id="host-source-sensitivity"' not in text:continue
 text=re.sub(r'<style id="host-interval-style">.*?</style>','',text,flags=re.S)
 text=re.sub(r'<figure class="host-interval".*?</figure>',figure,text,flags=re.S) if 'class="host-interval"' in text else re.sub(r'<img\b[^>]*主场来源敏感性\.png[^>]*>',figure,text)
 text=text.replace('<section id="host-source-sensitivity">',css+'<section id="host-source-sensitivity">')
 p.write_text(text,encoding='utf-8')
