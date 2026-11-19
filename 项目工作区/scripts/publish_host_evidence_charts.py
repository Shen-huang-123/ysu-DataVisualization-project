from pathlib import Path
import json,io,re
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[2];tab=root/'交付文件/任务二_百年全景/02_数据表';host=root/'交付文件/任务三_专题深挖/S1_东道主效应'
h=pd.read_csv(tab/'B_匹配DID逐案例.csv');prof=pd.read_csv(tab/'B_主场事件窗口.csv');summary=json.loads((tab/'B_主场准实验摘要.json').read_text(encoding='utf-8'))
plt.rcParams.update({'font.family':'Microsoft YaHei','svg.fonttype':'none','font.size':11,'axes.spines.top':False,'axes.spines.right':False,'axes.labelcolor':'#849b9e','xtick.color':'#849b9e','ytick.color':'#849b9e','text.color':'#849b9e','axes.edgecolor':'#849b9e','figure.facecolor':'none','axes.facecolor':'none','savefig.transparent':True})
names={'CHN':'中国','ESP':'西班牙','KOR':'韩国','GBR':'英国','FRA':'法国','JPN':'日本','AUS':'澳大利亚','BRA':'巴西'}
figures=[]
def finish(fig,title,note):
 fig.tight_layout(pad=1.6);buf=io.StringIO();fig.savefig(buf,format='svg',transparent=True);plt.close(fig);svg=buf.getvalue();svg=svg[svg.index('<svg'):];svg=re.sub(r'width="[^"]+" height="[^"]+"','width="100%" height="auto"',svg,count=1);figures.append(f'<figure class="host-proof-chart"><h3>{title}</h3>{svg}<figcaption>{note}</figcaption></figure>')
f,a=plt.subplots(figsize=(6.2,4.6));v=h.sort_values('did_pp');a.barh(range(len(v)),v.did_pp,facecolor='none',edgecolor='#b59b68',linewidth=1.1,height=.55);a.set_yticks(range(len(v)),[f'{names.get(r.NOC,r.NOC)} {int(r.Year)}' for _,r in v.iterrows()]);a.set_xlim(0,6.4);a.set_xlabel('主办国变化 − 匹配组变化（百分点）');a.grid(axis='x',alpha=.12);a.set_axisbelow(True)
for i,x in enumerate(v.did_pp):a.text(x+.1,i,f'+{x:.2f}',va='center',fontsize=10)
finish(f,'九个案例：相对变化均为正','原五队匹配、运动员获奖记录口径；不等同于官方小项奖牌。')
f,a=plt.subplots(figsize=(6.2,4.6));avg=prof.groupby('k')[['host_share','control_share']].mean();base=avg.loc[-1]
for field,color,label in [('host_share','#c5a66c','主办国'),('control_share','#78aabb','匹配组')]:a.plot(avg.index,avg[field]-base[field],marker='o',lw=2,color=color,label=label)
a.axvline(0,color='#b59b68',ls='--',lw=1);a.axhline(0,color='#849b9e',alpha=.35,lw=1);a.set_xticks(avg.index,['前两届','前一届','主办届','后一届','后两届']);a.set_ylabel('相对前一届变化（百分点）');a.legend(frameon=False);a.grid(axis='y',alpha=.12)
finish(f,'事件窗口：主办届出现分化','各相对届次按可用案例求均值，覆盖案例会变化；不代表已验证平行趋势。')
g=pd.read_csv(host/'host_comparison_groups.csv');rng=np.random.default_rng(20261107)
for _ in range(50000):rng.choice(h.did_pp.to_numpy(),len(h),replace=True).mean()
sets=[np.array([r.change_pp]+g[(g.host_year.eq(r.Year))&(g.host_NOC.eq(r.NOC))].change_pp.tolist()) for _,r in h.iterrows()];placebo=[]
for _ in range(50000):
 eff=[]
 for arr in sets:
  j=rng.integers(len(arr));eff.append(arr[j]-np.delete(arr,j).mean())
 placebo.append(np.mean(eff))
f,a=plt.subplots(figsize=(6.2,4.6));a.hist(placebo,bins=45,color='#78aabb',alpha=.55);a.axvline(summary['matched_did_mean_pp'],color='#c5a66c',lw=2,label='观测均值 +2.70');a.axvline(-summary['matched_did_mean_pp'],color='#c5a66c',ls=':',lw=1);a.set_xlabel('随机指派下的平均差值（百分点）');a.set_ylabel('模拟次数');a.legend(frameon=False);a.grid(axis='y',alpha=.12)
finish(f,'随机化检验：'+summary['randomization_p_label'],'50,000次组内随机指派；检验反映给定匹配设计，不能消除主办权选择偏差。')
p=host/'index.html';s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser');old=s.select_one('#host-proof-charts');img=s.select_one('img.s1-figure');markup=BeautifulSoup('<div id="host-proof-charts">'+''.join(figures)+'</div>','html.parser')
if old:old.replace_with(markup)
elif img:img.replace_with(markup)
p.write_text(str(s),encoding='utf-8')
print('Published three evidence charts')
