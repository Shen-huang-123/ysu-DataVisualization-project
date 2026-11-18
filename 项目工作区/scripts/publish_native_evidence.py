"""Publish core evidence as native SVG using unchanged audited CSV values."""
from pathlib import Path
import json,html
import pandas as pd
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[2];d=root/'交付文件';out=d/'最终提交材料/核心证据图'
ranks=pd.read_csv(d/'任务三_专题深挖/S2_口径的魔力/02_数据表/S2_2024双口径完整排名.csv')
cohorts=pd.read_csv(d/'任务三_专题深挖/S3_冠军的保质期/11_历史来源敏感性/固定队列三方案复算.csv')
scores=pd.read_csv(d/'任务四_开放创作/05_满分升级/15_原项目模型时序核验/原模型五方案评分.csv')
def text(x,y,t,cl='',anchor='start'):return f'<text x="{x}" y="{y}" class="{cl}" text-anchor="{anchor}">{html.escape(str(t))}</text>'
def svg(label,marks):return '<svg viewBox="0 0 960 390" role="img" aria-label="'+label+'"><title>'+label+'</title>'+''.join(marks)+'</svg>'
charts={}
a=[]
for x,label in [(310,'官方小项 · 名次'),(750,'运动员行 · 名次')]:a.append(text(x,35,label,'ne-muted','middle'))
for i,(noc,name) in enumerate([('ESP','西班牙'),('NED','荷兰'),('JPN','日本')]):
 r=ranks[ranks.NOC.eq(noc)].iloc[0];y=100+i*110
 a+=[text(30,y+6,name),f'<line x1="338" y1="{y}" x2="722" y2="{y}" class="ne-grid"/>']
 for x,key,cl in [(310,'official_rank','ne-a'),(750,'row_rank','ne-b')]:a+=[f'<circle cx="{x}" cy="{y}" r="26" class="{cl}"/>',text(x,y+6,int(r[key]),'ne-on','middle')]
 a.append(text(530,y+35,f'{int(r.Gold_official)}个金牌小项 / {int(r.Gold_rows)}条金牌记录','ne-muted','middle'))
charts['01_统计单位与名次']=('相同排序，换统计单位会换名次',svg('巴黎2024三个代表团双口径名次',a),'两端采用相同金银铜排序，排除AIN。连接线只配对同一代表团，线长不编码名次差。')
a=[];xx=lambda v:310+(v+18)/22*610
for tick in [-15,-10,-5,0]:a+=[f'<line x1="{xx(tick)}" y1="30" x2="{xx(tick)}" y2="330" class="ne-grid"/>',text(xx(tick),370,tick,'ne-muted','middle')]
for i,(_,r) in enumerate(cohorts.head(3).iterrows()):
 y=80+i*105;v,lo,hi=[float(r[k]) for k in ['后减前百分点','区间下限','区间上限']];color='var(--ne-b)' if i==2 else 'var(--ne-a)'
 a+=[text(12,y,['原代理 · 113项','二次来源 · 同113项','排除未决系列 · 50项'][i]),f'<path d="M {xx(lo)} {y} H {xx(hi)} M {xx(lo)} {y-9} V {y+9} M {xx(hi)} {y-9} V {y+9}" fill="none" stroke="{color}" stroke-width="3"/><circle cx="{xx(v)}" cy="{y}" r="7" fill="{color}"/>',text(310,y+35,f'{v:.2f} [{lo:.2f}, {hi:.2f}]','ne-muted')]
charts['02_固定队列与排除敏感性']=('排除未决系列后，下降区间跨过零',svg('后段减早段卫冕率差值与95%区间，单位百分点',a),'小项成组重抽样10,000次，种子42。子队列变化含样本选择；二次来源及排除子集不等于现行IOC认证，也非因果检验。')
a=[];q=scores[scores.来源.eq('小项二次来源')&scores.选择规则.eq('仅此前届次')]
for tick in range(4):
 y=320-tick*84;a+=[f'<line x1="50" y1="{y}" x2="945" y2="{y}" class="ne-grid"/>',text(30,y+5,tick,'','end')]
for j,year in enumerate([2012,2016,2024]):
 for k,model in enumerate(['历史加权基线','RF60_GB40','55基线45项目']):
  v=float(q[q.Year.eq(year)&q.模型.eq(model)].MAE.iloc[0]);x=90+j*295+k*68;y=320-v*84
  a+=[f'<rect x="{x}" y="{y:.3f}" width="52" height="{v*84:.3f}" rx="3" class="ne-{chr(97+k)}"/>',text(x+26,round(y-12,3),f'{v:.3f}','','middle')]
 a.append(text(184+j*295,352,year,'','middle'))
a.append(text(774,385,'最近奖牌特征为2016','ne-muted','middle'))
charts['03_原模型与同口径基准']=('项目模型有局部收益，但没有稳定胜过基准',svg('小项二次来源全体代表团MAE，越低越好',a),'同单位内比较：2012和2016混合优于基线，2024仍略差。2024最近小项特征为2016，间隔八年；不能据此确认45%权重稳定有效。')
records=[]
for page in d.rglob('*.html'):
 if any(k in str(page) for k in ['原始页面','99_旧']):continue
 s=BeautifulSoup(page.read_text(encoding='utf-8'),'html.parser');changed=False
 for name,(title,graphic,note) in charts.items():
  candidates=s.select(f'img[src*="{name}.png"],figure[data-native-evidence="{name}"]')
  for old in candidates:
   legend='<div class="ne-legend"><span class="ne-key-a">历史加权基准</span><span class="ne-key-b">RF60 / GB40</span><span class="ne-key-c">固定55/45混合</span></div>' if name.startswith('03') else ''
   figure=BeautifulSoup(f'<figure class="native-evidence" data-native-evidence="{name}"><h3>{title}</h3>{legend}<div class="ne-scroll" tabindex="0" aria-label="统计图，窄屏可横向查看">{graphic}</div><figcaption>{note} 原始数据与PDF下载见下方。</figcaption></figure>','html.parser').figure
   old.replace_with(figure);changed=True;records.append({'page':str(page.relative_to(d)),'chart':name})
 if changed:
  for chart in s.select('.native-evidence'):
   parent=chart.parent
   if parent.name=='figure':
    parent['class']=list(dict.fromkeys(parent.get('class',[])+['native-evidence-host']))
    parent.attrs.pop('style',None)
  import os
  if not s.select_one('#native-evidence-theme'):s.head.append(s.new_tag('link',id='native-evidence-theme',rel='stylesheet',href=os.path.relpath(d/'共享组件/native-evidence.css',page.parent).replace('\\','/')))
  page.write_text(str(s),encoding='utf-8')
(d/'最终提交材料/原生证据图发布记录.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
print('Published native CSV evidence:',len(records))
