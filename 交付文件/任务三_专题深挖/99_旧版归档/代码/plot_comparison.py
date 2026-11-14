from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'outputs'
c=pd.read_csv(OUT/'paris2024_scale_comparison.csv')
plt.rcParams.update({'font.family':'Microsoft YaHei','axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'#faf9f6','axes.facecolor':'#faf9f6'})
fig,axes=plt.subplots(1,2,figsize=(13,7))
s=c.sort_values('published_rank')
y=range(len(s))
axes[0].barh(y,s.gold,color='#246477',label='公布的小项金牌数')
axes[0].barh(y,s.gold_rows,left=s.gold,alpha=0) # keep axis independent of right panel
axes[0].set_yticks(y,s.NOC); axes[0].invert_yaxis(); axes[0].set_xlim(0,45)
for i,v in enumerate(s.gold): axes[0].text(v+.4,i,str(v),va='center',fontsize=9)
axes[0].set_title('外部公布的小项金牌数');axes[0].set_xlabel('枚；按金银铜排序列出前15代表团')
axes[1].barh(y,s.gold_rows,color='#a23d52');axes[1].set_yticks(y,s.NOC);axes[1].invert_yaxis();axes[1].set_xlim(0,145)
for i,v in enumerate(s.gold_rows): axes[1].text(v+1,i,str(v),va='center',fontsize=9)
axes[1].set_title('赛题数据的金牌记录数');axes[1].set_xlabel('行；团体成员每人各占一行')
fig.suptitle('同一届奥运，统计尺度改变了谁被看见',fontsize=18,fontweight='bold')
fig.subplots_adjust(bottom=.18,wspace=.25)
fig.text(.06,.04,'2024巴黎；左：维基百科奖牌表快照（二手来源，待一手核验）；右：赛题CSV。\n两侧横轴尺度不同；代表团顺序一致。金牌行排名仅按金牌行数，并列使用最小名次。',fontsize=10,color='#555')
fig.savefig(OUT/'figures/S2_2024_comparison.png',dpi=180,bbox_inches='tight')
