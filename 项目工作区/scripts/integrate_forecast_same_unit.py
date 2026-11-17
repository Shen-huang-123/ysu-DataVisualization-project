"""Publish the independent chronological forecast benchmark, including failures."""
from pathlib import Path
import os,re,json
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader

ROOT=Path(__file__).resolve().parents[2];T4=ROOT/'交付文件/任务四_开放创作';OUT=T4/'05_满分升级/14_同口径时序重训'
s=pd.read_csv(OUT/'三折同口径评分.csv');a=pd.read_csv(OUT/'逐折数据边界.csv');detail=pd.read_csv(OUT/'三折逐队预测.csv')
z=s[s.训练来源.eq('B二次来源')&s.评分来源.eq('B二次来源')]
models=['上一可用届份额','同口径岭回归','固定55_45混合']
head='独立岭回归基准未胜过历史份额：公开失败结果'
intro='新增独立基准把历史输入、训练目标和输出都统一到小项奖牌槽代理；逐折用更早届次进行内部调参。二次来源情景下，2012、2016、2024三折中，历史份额基线的全体MAE均低于岭回归及固定55/45混合模型。不能据此宣称机器学习提高了预测能力。'
limits='这不是已发布2028最终集成的重训或完整验证。历史小项代理可能合并同NOC同色多枚；二次来源不是现行IOC逐项认证。2024目标使用既有政府开放数据逐项表，其结构与历史代理仍不完全等价。历史资料含事后追溯修订，缺逐届赛前冻结快照；严格时间切分不等于严格真实时点数据。'
gap='2020小项字段泛化，因此不进入奖牌特征；2024回放最近可用奖牌届次为2016，实际是八年间隔，不能当作通常的一届预测。2020参赛身份仍可用于候选代表团筛选。2028新增运动排名、资格、主场加成与最终集成区间覆盖率，均不在本基准验证范围。'
method='候选代表团仅取目标前最近三届的参赛记录；训练与内部验证届次均早于外层留出届次。模型为代表团总量岭回归，输入为前两次可用份额、趋势、近三次均值与波动及年份间隔；正则系数仅在更早届次选择。目标奖牌池由此前三次总量按年度趋势外推，实际池只评分。每折训练来源下的三模型使用相同预测池和评分代表团集合。'
score_note='全体评分包含赛前候选中的零奖牌代表团，并补入当届未见获奖代表团、预测置零；三折分别为207、208、212队。2016、2024各有一个未见获奖身份，保留误差，不用赛后身份映射修补。MAE分母与旧132队回放不同，不能直接横比；同时公开实际至少5枚子集、RMSE与完整逐队误差。'
version_note='分开三步：A预测对A标签；保持A预测不动、改用B标签评分；再用B历史重新调参训练、对B标签评分。这样区分“改评分标签”和“重新训练”的影响。两套来源中的岭回归和固定混合模型均未在全体MAE上胜过各自基线；这只评价本独立基准，不证明原RF/GB模型必然相同。'

plt.rcParams.update({'font.sans-serif':['Microsoft YaHei','SimHei'],'axes.unicode_minus':False})
fig,ax=plt.subplots(figsize=(10,4.5),facecolor='#f7f3eb');ax.set_facecolor('#f7f3eb');x=np.arange(3)
for i,(model,color) in enumerate(zip(models,['#247487','#a64155','#b88c43'])):
    v=z[z.模型.eq(model)].sort_values('Year').MAE.to_numpy();bars=ax.bar(x+(i-1)*.24,v,.22,label=model,color=color)
    for bar,val in zip(bars,v):ax.text(bar.get_x()+bar.get_width()/2,val+.04,f'{val:.2f}',ha='center',fontsize=10)
ax.set_xticks(x,['2012 · 207队','2016 · 208队','2024 · 212队\n最近奖牌特征为2016'])
ax.set_ylabel('每代表团MAE（小项奖牌槽；越低越好）');ax.set_ylim(0,3.25)
ax.set_title('同来源、同候选池、同预测池：简单基线三折均胜出',loc='left',fontsize=14,pad=16)
ax.legend(frameon=False,ncol=3,loc='upper left');ax.spines[['top','right']].set_visible(False);fig.tight_layout();fig.savefig(OUT/'同口径时序回放.png',dpi=160);plt.close(fig)
def table():
    t=z.pivot(index='Year',columns='模型',values='MAE')
    return '<table><caption>二次来源情景 · 全体MAE（枚/队，越低越好）</caption><thead><tr><th>留出届次</th><th>历史份额</th><th>岭回归</th><th>固定混合</th></tr></thead><tbody>'+''.join('<tr><th>'+str(y)+'</th>'+''.join(f'<td>{t.loc[y,m]:.3f}</td>' for m in models)+'</tr>' for y in t.index)+'</tbody></table>'
style='''<style>#forecast-same-unit{font-family:inherit;max-width:1100px;margin:3rem auto;padding:clamp(18px,3vw,36px);box-sizing:border-box;border-block:1px solid #8b969766;line-height:1.85}#forecast-same-unit h2{font-size:clamp(22px,3vw,32px);line-height:1.4}#forecast-same-unit img{display:block;width:100%;height:auto;margin:24px 0}#forecast-same-unit table{width:100%;border-collapse:collapse;font-size:clamp(12px,1.2vw,16px)}#forecast-same-unit th,#forecast-same-unit td{padding:10px 4px;text-align:left;border-bottom:1px solid #8b969766}#forecast-same-unit caption{text-align:left}#forecast-same-unit summary{cursor:pointer;font-weight:600}#forecast-same-unit a{overflow-wrap:anywhere}</style>'''
def block(parent):
    rel=Path(os.path.relpath(OUT,parent)).as_posix()
    return '<!-- FORECAST_SAME_UNIT_START -->'+style+f'<section id="forecast-same-unit"><h2>{head}</h2><p>{intro}</p><p><strong>先看边界：</strong>{limits}</p><img loading="lazy" src="{rel}/同口径时序回放.png" alt="2012、2016、2024三折的简单基线MAE均小于岭回归及固定混合">'+table()+f'<p>{gap}</p><details><summary>展开时间边界、评分分母与来源拆解</summary><p>{method}</p><p>{score_note}</p><p>{version_note}</p></details><p><a href="{rel}/三折同口径评分.csv" download>下载27行评分</a> · <a href="{rel}/三折逐队预测.csv" download>完整逐队误差</a> · <a href="{rel}/同口径时序重训说明.md">方法与限制</a> · <a href="{rel}/同口径时序重训补充报告.pdf">补充PDF</a></p></section><!-- FORECAST_SAME_UNIT_END -->'
paths=[T4/'index.html',T4/'02_2028洛杉矶预测/index.html',T4/'03_数据新闻/index.html',T4/'05_满分升级/09_赛前条件回放/index.html',T4/'05_满分升级/11_官方来源门控预测/index.html',T4/'09_预测风暴实验室/index.html']
for p in paths:
    text=p.read_text(encoding='utf-8');text=re.sub(r'<!-- FORECAST_SAME_UNIT_START -->.*?<!-- FORECAST_SAME_UNIT_END -->','',text,flags=re.S)
    assert '</body>' in text.lower();text=re.sub('</body>',lambda _:block(p.parent)+'\n</body>',text,count=1,flags=re.I);p.write_text(text,encoding='utf-8')
(OUT/'index.html').write_text('<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>同口径时序重训</title></head><body style="margin:0;background:#f7f3eb;color:#172a30;font-family:Microsoft YaHei,sans-serif">'+block(OUT)+'</body></html>',encoding='utf-8')
md='# '+head+'\n\n'+intro+'\n\n## 先读适用范围\n\n'+limits+'\n\n'+gap+'\n\n## 时间切分与评分\n\n'+method+'\n\n'+score_note+'\n\n'+version_note+'\n\n## 完整评分\n\n'+s.to_markdown(index=False)+'\n\n## 每折数据边界\n\n'+a.to_markdown(index=False)+'\n\n复现：`py 项目工作区/scripts/forecast_same_unit_replay.py`，再运行 `py 项目工作区/scripts/integrate_forecast_same_unit.py`。输入哈希、逐折数据边界、内部调参记录、评分与逐队预测均在本目录。未覆盖原预测榜、原模型参数及原始输入。没有拟合或宣称最终模型80%覆盖率。\n'
(OUT/'同口径时序重训说明.md').write_text(md,encoding='utf-8')
append='\n\n<!-- FORECAST_SAME_UNIT_START -->\n## 2026-11-17：独立的同口径时序重训基准\n\n'+intro+'\n\n'+limits+'\n\n'+gap+'\n\n'+score_note+'\n\n详见任务四/05_满分升级/14_同口径时序重训，复现脚本 forecast_same_unit_replay.py。新增的是代表团总量岭回归基准，不是已发布RF/GB最终集成的完整重训，不可将其MAE或结论替换到原模型。\n<!-- FORECAST_SAME_UNIT_END -->\n'
for p in [T4/'02_2028洛杉矶预测/预测方法与验证方案.md',ROOT/'交付文件/证据边界核验进度.md',ROOT/'项目交接_请新AI先读.md']:
    text=p.read_text(encoding='utf-8');text=re.sub(r'\n*<!-- FORECAST_SAME_UNIT_START -->.*?<!-- FORECAST_SAME_UNIT_END -->\n*','',text,flags=re.S);p.write_text(text+append,encoding='utf-8')

pdfmetrics.registerFont(TTFont('ReplayCN',r'C:\Windows\Fonts\simhei.ttf'))
c=canvas.Canvas(str(OUT/'同口径时序重训补充报告.pdf'),pagesize=A4);w,h=A4
def page(title,n):
    c.setFillColorRGB(.969,.953,.922);c.rect(0,0,w,h,fill=1,stroke=0);c.setFillColorRGB(.09,.16,.19);c.setFont('ReplayCN',20);c.drawString(35,h-55,title);c.setFont('ReplayCN',9);c.drawString(35,25,f'2026-11-17 · 独立时序基准 · {n}/2')
def para(text,y):
    line='';c.setFont('ReplayCN',10.5)
    for ch in text:
        if pdfmetrics.stringWidth(line+ch,'ReplayCN',10.5)>w-70:c.drawString(35,y,line);y-=18;line=ch
        else:line+=ch
    if line:c.drawString(35,y,line);y-=18
    return y-12
page('简单基线三折胜出：不隐去失败结果',1);y=para(intro,h-95)
im=ImageReader(str(OUT/'同口径时序回放.png'));iw,ih=im.getSize();hh=(w-70)*ih/iw;c.drawImage(im,35,y-hh,w-70,hh);y-=hh+30
y=para(limits,y);para(gap,y);c.showPage()
page('时间边界与完整评分口径',2);y=para(method,h-95);y=para(score_note,y);y=para(version_note,y)
for yy,g in z.groupby('Year'):
    vals={x.模型:x.MAE for x in g.itertuples()};y=para(f'{yy}：历史份额 {vals[models[0]]:.3f}、岭回归 {vals[models[1]]:.3f}、固定混合 {vals[models[2]]:.3f} 枚/队。',y)
para('模型复杂度不能替代样本外表现。三折及一处八年间隔不足以保证未来泛化；不据此修改已发布2028榜单或其区间。完整CSV、内部调参记录、输入哈希随项目交付。',y);c.showPage();c.save()
p=ROOT/'README.md';text=p.read_text(encoding='utf-8');line='\n- [独立同口径时序重训](交付文件/任务四_开放创作/05_满分升级/14_同口径时序重训/index.html)：三折早于目标届的调参训练；简单份额基线优于本轮复杂模型，保留历史数据版本与八年间隔限制。\n'
if '独立同口径时序重训](' not in text:p.write_text(text+line,encoding='utf-8')
print('Updated six forecast interfaces, report, audit and two-page PDF supplement.')
