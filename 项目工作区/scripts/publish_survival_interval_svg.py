from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[2]
p=root/'交付文件/任务三_专题深挖/S3_冠军的保质期/07_王朝生存图/index.html'
s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
region=s.select_one('#dynasty-source-sensitivity')
old=region.select_one('.source-interval-figure') or region.select_one('img')
rows=[('原代理 · 固定队列',113,-7.37,-13.20,-1.62),('二次来源替换 · 同队列',113,-7.37,-13.20,-1.62),('排除未决系列',50,-7.33,-16.17,1.50)]
x=lambda v:330+(v+20)/25*560
svg=['<figure class="source-interval-figure"><svg viewBox="0 0 1200 480" role="img" aria-labelledby="interval-title interval-desc"><title id="interval-title">来源替换前后，卫冕率变化与95%区间</title><desc id="interval-desc">固定113项的两种来源结果一致，下降7.37个百分点；排除后50项下降7.33个百分点，但区间跨零。</desc>']
svg+=['<text x="0" y="30" class="iv-heading">卫冕率变化</text><text x="0" y="58" class="iv-muted">后段减早段 · 百分点</text><text x="970" y="30" class="iv-muted">点估计 [95%区间]</text>']
for tick in [-20,-15,-10,-5,0,5]:
 pos=x(tick);svg.append(f'<line x1="{pos}" x2="{pos}" y1="95" y2="380" class="iv-grid {"iv-zero" if tick==0 else ""}"/><text x="{pos}" y="410" text-anchor="middle" class="iv-muted">{tick:+d}</text>')
for i,(name,n,mean,lo,hi) in enumerate(rows):
 y=140+i*100;cls='iv-caution' if i==2 else 'iv-stable'
 svg.append(f'<text x="0" y="{y-5}" class="iv-label">{name}</text><text x="0" y="{y+22}" class="iv-muted">{n} 个连续小项</text><g class="{cls}"><line x1="{x(lo)}" x2="{x(hi)}" y1="{y}" y2="{y}" class="iv-interval"/><line x1="{x(lo)}" x2="{x(lo)}" y1="{y-8}" y2="{y+8}"/><line x1="{x(hi)}" x2="{x(hi)}" y1="{y-8}" y2="{y+8}"/><circle cx="{x(mean)}" cy="{y}" r="7"/></g><text x="970" y="{y+6}" class="iv-value">{mean:.2f} [{lo:.2f}, {hi:.2f}]</text>')
svg.append('<text x="330" y="455" class="iv-muted">← 卫冕率下降</text><text x="890" y="455" text-anchor="end" class="iv-muted">卫冕率上升 →</text></svg><figcaption>圆点表示点估计，横线表示小项成组95%区间；橙色区间跨过零，不能确认下降。</figcaption></figure>')
if old:old.replace_with(BeautifulSoup(''.join(svg),'html.parser'))
style=s.select_one('#survival-interval-style')
if not style:style=s.new_tag('style',id='survival-interval-style');s.head.append(style)
style.string="\nhtml body.ip-dynasty #dynasty-source-sensitivity{max-width:none!important;width:auto!important;margin:32px 6vw!important;padding:32px 0!important;color:var(--ink)!important}\n#dynasty-source-sensitivity .source-interval-figure{margin:28px 0!important;padding:0!important;background:transparent!important;overflow-x:auto}\n#dynasty-source-sensitivity .source-interval-figure svg{display:block;width:100%;min-width:780px;height:auto;background:transparent;color:inherit}\n#dynasty-source-sensitivity .source-interval-figure text{fill:currentColor;font:16px 'Microsoft YaHei',sans-serif}\n#dynasty-source-sensitivity .source-interval-figure .iv-heading{font-size:24px;font-weight:500}\n#dynasty-source-sensitivity .source-interval-figure .iv-muted{font-size:14px;opacity:.8}\n#dynasty-source-sensitivity .iv-grid{stroke:currentColor;opacity:.12}\n#dynasty-source-sensitivity .iv-zero{opacity:.6;stroke-dasharray:5 5}\n#dynasty-source-sensitivity .iv-stable{stroke:#46849a;fill:#46849a;stroke-width:2}\n#dynasty-source-sensitivity .iv-caution{stroke:#ad672f;fill:#ad672f;stroke-width:2}\nbody.xz-dark #dynasty-source-sensitivity .iv-stable{stroke:#8bc7db;fill:#8bc7db}\nbody.xz-dark #dynasty-source-sensitivity .iv-caution{stroke:#edb77d;fill:#edb77d}\n#dynasty-source-sensitivity .iv-interval{stroke-width:3}\n#dynasty-source-sensitivity figcaption{font-size:14px;line-height:1.8;margin-top:14px}\n@media(max-width:650px){html body.ip-dynasty #dynasty-source-sensitivity{margin:24px!important;padding:24px 0!important}}\n"
p.write_text(str(s),encoding='utf-8')
