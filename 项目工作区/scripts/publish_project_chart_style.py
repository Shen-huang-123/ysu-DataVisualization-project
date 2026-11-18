"""Theme-aware web chart; publication PNG/PDF and underlying scores stay unchanged."""
from pathlib import Path
from bs4 import BeautifulSoup
import pandas as pd
root=Path(__file__).resolve().parents[2];t4=root/'交付文件/任务四_开放创作';out=t4/'05_满分升级/15_原项目模型时序核验'
df=pd.read_csv(out/'原模型五方案评分.csv');df=df[(df.选择规则=='仅此前届次')&(df.来源=='小项二次来源')]
models=['历史加权基线','RF60_GB40','55基线45项目']
svg=['<svg viewBox="0 0 960 390" role="img" aria-label="二次来源情景三折全体MAE比较，越低越好；RF/GB及混合在2024小项口径略差于基线">']
for tick in [0,1,2,3]:
 y=320-tick*84
 svg.append(f'<line x1="50" y1="{y}" x2="945" y2="{y}" class="fc-grid"/><text x="30" y="{y+5}" text-anchor="end">{tick}</text>')
for j,year in enumerate([2012,2016,2024]):
 for k,model in enumerate(models):
  v=float(df[(df.Year==year)&(df.模型==model)].MAE.iloc[0]);x=90+j*295+k*68;y=320-v*84
  svg.append(f'<rect class="fc-bar fc-model-{k}" x="{x}" y="{y:.3f}" width="52" height="{v*84:.3f}" rx="3"/><text x="{x+26}" y="{y-12:.3f}" text-anchor="middle">{v:.3f}</text>')
 svg.append(f'<text x="{184+j*295}" y="352" text-anchor="middle">{year}</text>')
svg.append('<text x="774" y="380" text-anchor="middle" class="fc-muted">最近奖牌特征为2016</text></svg>')
style="""#project-model-audit{--fc-ink:#1a343b;--fc-muted:#526a70;--fc-line:#758b8b30;--fc-a:#347789;--fc-b:#b35d70;--fc-c:#ac863f;color:var(--fc-ink);max-width:none!important;margin:48px clamp(24px,6vw,100px)!important;padding:32px 0!important;border-color:var(--fc-line)!important}body.xz-dark #project-model-audit,html.xz-dark-preload #project-model-audit{--fc-ink:#e8efec;--fc-muted:#adbfbe;--fc-line:#bbceca26;--fc-a:#71b5c4;--fc-b:#d38c9b;--fc-c:#ddbd79}#project-model-audit h2{font-family:inherit!important;font-weight:500;letter-spacing:-.025em}#project-model-audit p{font-size:15px;font-weight:400;line-height:1.95;color:var(--fc-muted)}#project-model-audit .fc-figure{margin:36px 0;background:transparent;border:0;box-shadow:none}#project-model-audit .fc-figure h3{font-family:inherit;font-size:22px;font-weight:500;color:var(--fc-ink);margin:0 0 10px}#project-model-audit .fc-legend{display:flex;flex-wrap:wrap;gap:12px 28px;font-size:13px;margin:20px 0;color:var(--fc-muted)}#project-model-audit .fc-legend span:before{content:'';display:inline-block;width:9px;height:9px;margin-right:8px;border-radius:50%;background:var(--dot)}#project-model-audit .fc-scroll{overflow-x:auto}#project-model-audit svg{display:block;width:100%;min-width:600px;height:auto}#project-model-audit svg text{fill:var(--fc-ink);font-family:inherit;font-size:15px;font-weight:400}#project-model-audit svg .fc-muted{fill:var(--fc-muted);font-size:12px}#project-model-audit .fc-grid{stroke:var(--fc-line);stroke-width:1}#project-model-audit .fc-model-0{fill:var(--fc-a)}#project-model-audit .fc-model-1{fill:var(--fc-b)}#project-model-audit .fc-model-2{fill:var(--fc-c)}#project-model-audit figcaption{font-size:12px;line-height:1.8;color:var(--fc-muted);margin-top:12px}html body #project-model-audit table,html body #project-model-audit :is(thead,tbody,tr,th,td){background:transparent!important;box-shadow:none!important;border-radius:0!important;color:var(--fc-ink)!important;font-family:inherit!important}html body #project-model-audit table{border:0!important;border-collapse:collapse;width:100%;font-size:14px}html body #project-model-audit :is(th,td){padding:16px 12px!important;border:0!important;border-bottom:1px solid var(--fc-line)!important;font-weight:400!important;text-align:right}html body #project-model-audit :is(th,td):first-child{text-align:left}html body #project-model-audit thead th{color:var(--fc-muted)!important;font-size:12px!important;font-weight:500!important}#project-model-audit caption{font-size:13px;color:var(--fc-muted);padding-bottom:12px;text-align:left}#project-model-audit details{border-block:1px solid var(--fc-line);padding:20px 0;margin-block:24px}#project-model-audit a{color:var(--fc-a);text-underline-offset:5px}@media(max-width:600px){#project-model-audit{margin-inline:24px!important}#project-model-audit .fc-figure h3{font-size:20px}html body #project-model-audit :is(th,td){padding:12px 6px!important;font-size:12px!important}}"""
paths=[t4/'index.html',t4/'02_2028洛杉矶预测/index.html',t4/'03_数据新闻/index.html',t4/'05_满分升级/09_赛前条件回放/index.html',t4/'05_满分升级/11_官方来源门控预测/index.html',t4/'09_预测风暴实验室/index.html',out/'index.html']
for p in paths:
 s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser');section=s.select_one('#project-model-audit');assert section,p
 old=s.select_one('#project-chart-theme');
 if old:old.decompose()
 tag=s.new_tag('style',id='project-chart-theme');tag.string=style;s.head.append(tag)
 img=section.find('img')
 if img:
  markup='<figure class="fc-figure"><h3>混合有时改善，2024仍略差</h3><p>小项二次来源 · 全体 MAE，越低越好</p><div class="fc-legend"><span style="--dot:var(--fc-a)">历史加权基线</span><span style="--dot:var(--fc-b)">RF60 / GB40</span><span style="--dot:var(--fc-c)">固定55/45混合</span></div><div class="fc-scroll">'+''.join(svg)+'</div><figcaption>同单位内比较：2012和2016混合优于基线，2024仍略差。2024最近小项特征为2016，间隔八年；不能据此确认45%权重稳定有效。窄屏可横向查看图表，精确数值见下表。</figcaption></figure>'
  img.replace_with(BeautifulSoup(markup,'html.parser'))
 p.write_text(str(s),encoding='utf-8')
print('Styled seven original RF/GB audit blocks from unchanged CSV')

# The supplementary-page theme is the final presentation pass.
import runpy
runpy.run_path(str(Path(__file__).with_name("publish_supplement_reading.py")))
