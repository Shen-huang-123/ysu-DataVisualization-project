"""Compare gold-only competition ranks with an identical ranking rule."""
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]; O=ROOT/'outputs'
c=pd.read_csv(O/'paris2024_scale_comparison.csv')
ext=pd.read_csv(O/'paris2024_published_medals_secondary.csv')
ext=ext[ext.delegation.ne('Individual Neutral Athletes')].copy()
ext['gold_only_rank']=ext.gold.rank(method='min',ascending=False).astype(int)
c=c.merge(ext[['delegation','gold_only_rank']],on='delegation',validate='one_to_one')
d=pd.read_csv(O/'olympics_flagged.csv.gz'); d=d[d.Year.eq(2024)&d.NOC.ne('AIN')]
def ranks(frame):
 return frame[frame.Medal.eq('Gold')].groupby('NOC').size().rank(method='min',ascending=False)
c['gold_row_rank']=c.NOC.map(ranks(d)).astype(int)
c['dedup_gold_row_rank']=c.NOC.map(ranks(d[~d.duplicate_excess])).astype(int)
c['ranking_rule_change']=c.gold_only_rank-c.published_rank
c['unit_change_same_rule']=c.gold_row_rank-c.gold_only_rank
assert (c.gold_row_rank-c.published_rank == c.ranking_rule_change+c.unit_change_same_rule).all()
c.to_csv(O/'paris2024_rank_sensitivity.csv',index=False)
plt.rcParams.update({'font.family':'Microsoft YaHei','axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'#faf9f6','axes.facecolor':'#faf9f6'})
fig,ax=plt.subplots(figsize=(10,8))
colors={'ESP':'#a23d52','NED':'#a23d52','JPN':'#246477'}
for _,r in c.iterrows():
 color=colors.get(r.NOC,'#a0a7aa')
 ax.plot([0,1],[r.gold_only_rank,r.gold_row_rank],marker='o',color=color,alpha=.85)
for column,x,ha in [('gold_only_rank',-.04,'right'),('gold_row_rank',1.04,'left')]:
 for rank,g in c.groupby(column):
  ax.text(x,rank,f'{rank} '+ '/'.join(g.NOC),ha=ha,va='center',fontsize=9)
ax.set(xlim=(-.3,1.3),ylim=(20,0),xticks=[0,1],xticklabels=['公布金牌数排名','金牌记录数排名'],ylabel='名次（越小越靠前）',title='相同排名规则下，统计单位仍改变名次')
ax.set_yticks(range(1,20,2));ax.grid(axis='y',alpha=.12)
fig.subplots_adjust(bottom=.18)
fig.text(.07,.04,'2024；两端均仅按金牌计数、并列取最小名次；均排除AIN。\n展示已明确映射的15个代表团，名次在各自完整榜中计算；斜线连接并列代表团名称。\n外部计数：维基百科快照，待一手核验；记录计数：赛题CSV。',fontsize=9)
fig.savefig(O/'figures/S2_same_rule_ranks.png',dpi=170,bbox_inches='tight')
print(c[['NOC','published_rank','gold_only_rank','gold_row_rank','dedup_gold_row_rank','unit_change_same_rule']].to_string(index=False))
