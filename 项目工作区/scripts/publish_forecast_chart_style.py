"""Theme-aware web chart; publication PNG/PDF and underlying scores stay unchanged."""
from pathlib import Path
from bs4 import BeautifulSoup
import pandas as pd
root=Path(__file__).resolve().parents[2];t4=root/'交付文件/任务四_开放创作';out=t4/'05_满分升级/14_同口径时序重训'
df=pd.read_csv(out/'三折同口径评分.csv');df=df[(df.训练来源=='B二次来源')&(df.评分来源=='B二次来源')]
models=['上一可用届份额','同口径岭回归','固定55_45混合']
svg=['<svg viewBox="0 0 960 390" role="img" aria-label="二次来源情景三折全体MAE比较，越低越好；历史份额基线三折均优于本轮岭回归与固定混合">']
for tick in [0,1,2,3]:
 y=320-tick*84
 svg.append(f'<line x1="50" y1="{y}" x2="945" y2="{y}" class="fc-grid"/><text x="30" y="{y+5}" text-anchor="end">{tick}</text>')
for j,year in enumerate([2012,2016,2024]):
 for k,model in enumerate(models):
  v=float(df[(df.Year==year)&(df.模型==model)].MAE.iloc[0]);x=90+j*295+k*68;y=320-v*84
  svg.append(f'<rect class="fc-bar fc-model-{k}" x="{x}" y="{y:.3f}" width="52" height="{v*84:.3f}" rx="3"/><text x="{x+26}" y="{y-12:.3f}" text-anchor="middle">{v:.2f}</text>')
 svg.append(f'<text x="{184+j*295}" y="352" text-anchor="middle">{year} · {[207,208,212][j]}队</text>')
svg.append('<text x="774" y="380" text-anchor="middle" class="fc-muted">最近奖牌特征为2016</text></svg>')
style="""#forecast-same-unit{--fc-ink:#1a343b;--fc-muted:#526a70;--fc-line:#758b8b30;--fc-a:#347789;--fc-b:#b35d70;--fc-c:#ac863f;color:var(--fc-ink);max-width:none!important;margin:48px clamp(24px,6vw,100px)!important;padding:32px 0!important;border-color:var(--fc-line)!important}body.xz-dark #forecast-same-unit,html.xz-dark-preload #forecast-same-unit{--fc-ink:#e8efec;--fc-muted:#adbfbe;--fc-line:#bbceca26;--fc-a:#71b5c4;--fc-b:#d38c9b;--fc-c:#ddbd79}#forecast-same-unit h2{font-family:inherit!important;font-weight:500;letter-spacing:-.025em}#forecast-same-unit p{font-size:15px;font-weight:400;line-height:1.95;color:var(--fc-muted)}#forecast-same-unit .fc-figure{margin:36px 0;background:transparent;border:0;box-shadow:none}#forecast-same-unit .fc-figure h3{font-family:inherit;font-size:22px;font-weight:500;color:var(--fc-ink);margin:0 0 10px}#forecast-same-unit .fc-legend{display:flex;flex-wrap:wrap;gap:12px 28px;font-size:13px;margin:20px 0;color:var(--fc-muted)}#forecast-same-unit .fc-legend span:before{content:'';display:inline-block;width:9px;height:9px;margin-right:8px;border-radius:50%;background:var(--dot)}#forecast-same-unit .fc-scroll{overflow-x:auto}#forecast-same-unit svg{display:block;width:100%;min-width:600px;height:auto}#forecast-same-unit svg text{fill:var(--fc-ink);font-family:inherit;font-size:15px;font-weight:400}#forecast-same-unit svg .fc-muted{fill:var(--fc-muted);font-size:12px}#forecast-same-unit .fc-grid{stroke:var(--fc-line);stroke-width:1}#forecast-same-unit .fc-model-0{fill:var(--fc-a)}#forecast-same-unit .fc-model-1{fill:var(--fc-b)}#forecast-same-unit .fc-model-2{fill:var(--fc-c)}#forecast-same-unit figcaption{font-size:12px;line-height:1.8;color:var(--fc-muted);margin-top:12px}html body #forecast-same-unit table,html body #forecast-same-unit :is(thead,tbody,tr,th,td){background:transparent!important;box-shadow:none!important;border-radius:0!important;color:var(--fc-ink)!important;font-family:inherit!important}html body #forecast-same-unit table{border:0!important;border-collapse:collapse;width:100%;font-size:14px}html body #forecast-same-unit :is(th,td){padding:16px 12px!important;border:0!important;border-bottom:1px solid var(--fc-line)!important;font-weight:400!important;text-align:right}html body #forecast-same-unit :is(th,td):first-child{text-align:left}html body #forecast-same-unit thead th{color:var(--fc-muted)!important;font-size:12px!important;font-weight:500!important}#forecast-same-unit caption{font-size:13px;color:var(--fc-muted);padding-bottom:12px;text-align:left}#forecast-same-unit details{border-block:1px solid var(--fc-line);padding:20px 0;margin-block:24px}#forecast-same-unit a{color:var(--fc-a);text-underline-offset:5px}@media(max-width:600px){#forecast-same-unit{margin-inline:24px!important}#forecast-same-unit .fc-figure h3{font-size:20px}html body #forecast-same-unit :is(th,td){padding:12px 6px!important;font-size:12px!important}}"""
paths=[t4/'index.html',t4/'02_2028洛杉矶预测/index.html',t4/'03_数据新闻/index.html',t4/'05_满分升级/09_赛前条件回放/index.html',t4/'05_满分升级/11_官方来源门控预测/index.html',t4/'09_预测风暴实验室/index.html',out/'index.html']
for p in paths:
 s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser');section=s.select_one('#forecast-same-unit');assert section,p
 old=s.select_one('#forecast-chart-theme');
 if old:old.decompose()
 tag=s.new_tag('style',id='forecast-chart-theme');tag.string=style;s.head.append(tag)
 img=section.find('img')
 if img:
  markup='<figure class="fc-figure"><h3>简单基线，三折均胜出</h3><p>全体代表团 MAE · 小项奖牌槽/队，越低越好</p><div class="fc-legend"><span style="--dot:var(--fc-a)">历史份额</span><span style="--dot:var(--fc-b)">同口径岭回归</span><span style="--dot:var(--fc-c)">固定55/45混合</span></div><div class="fc-scroll">'+''.join(svg)+'</div><figcaption>同来源、同候选池、同预测池。2024回放的最近奖牌特征为2016，存在八年间隔；结果仅适用于本独立基准。窄屏可横向查看图表，精确数值见下表。</figcaption></figure>'
  img.replace_with(BeautifulSoup(markup,'html.parser'))
 p.write_text(str(s),encoding='utf-8')
print('Styled seven forecast benchmark blocks from unchanged CSV')
