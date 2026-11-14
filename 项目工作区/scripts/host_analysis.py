"""Descriptive host comparisons, not causal estimates."""
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parents[1];O=R/'outputs'
d=pd.read_csv(O/'olympics_flagged.csv.gz');d=d[d.include_main]
years=sorted(d.Year.unique());total=d[d.is_medal].groupby('Year').size()
# Deliberate modern case study sample, not all historical host editions.
cases=[(1964,'JPN','Tokyo'),(1988,'KOR','Seoul'),(1992,'ESP','Barcelona'),(2000,'AUS','Sydney'),(2008,'CHN','Beijing'),(2012,'GBR','London'),(2016,'BRA','Rio de Janeiro'),(2020,'JPN','Tokyo'),(2024,'FRA','Paris')]
rows=[]; controls=[]
for year,noc,city in cases:
 assert city in set(d.loc[d.Year.eq(year),'City'])
 i=years.index(year); window=years[max(0,i-1):min(len(years),i+2)]
 for y in window:
  part=d[d.Year.eq(y)&d.NOC.eq(noc)]
  count=int(part.is_medal.sum()) if len(part) else np.nan
  rows.append(dict(host_year=year,NOC=noc,City=city,Year=y,relative_edition=years.index(y)-i,participation_rows=len(part),medal_rows=count,medal_share=count/total[y]*100))
 pre=years[i-1]
 a=d[d.Year.eq(pre)].groupby('NOC').agg(records=('Sex','size'),medal_rows=('is_medal','sum'))
 b=d[d.Year.eq(year)].groupby('NOC').agg(records=('Sex','size'),medal_rows=('is_medal','sum'))
 pool=a.join(b,lsuffix='_pre',rsuffix='_host',how='inner').drop(index=[noc],errors='ignore')
 pool=pool[(pool.medal_rows_pre>0)&(pool.medal_rows_host>0)].copy()
 host_pre=a.loc[noc,'medal_rows']/total[pre]*100
 pool['pre_share']=pool.medal_rows_pre/total[pre]*100
 pool['host_share']=pool.medal_rows_host/total[year]*100
 pool['distance']=(pool.pre_share-host_pre).abs()
 # Five closest previous-edition shares, with deterministic NOC tie break.
 pool=pool.reset_index().sort_values(['distance','NOC']).head(5)
 pool['host_year']=year;pool['host_NOC']=noc
 pool['change_pp']=pool.host_share-pool.pre_share
 controls.extend(pool.to_dict('records'))
w=pd.DataFrame(rows);w.to_csv(O/'host_windows.csv',index=False)
ctrl=pd.DataFrame(controls);ctrl.to_csv(O/'host_comparison_groups.csv',index=False)
res=[]
for (year,noc),g in w.groupby(['host_year','NOC']):
 s=g.set_index('relative_edition');change=s.loc[0,'medal_share']-s.loc[-1,'medal_share']
 control=ctrl[ctrl.host_year.eq(year)].change_pp.mean()
 res.append(dict(Year=year,NOC=noc,pre_rows=s.loc[-1,'medal_rows'],host_rows=s.loc[0,'medal_rows'],pre_share=s.loc[-1,'medal_share'],host_share=s.loc[0,'medal_share'],change_pp=change,comparison_mean_pp=control,descriptive_gap_pp=change-control,post_share=s.loc[1,'medal_share'] if 1 in s.index else np.nan))
out=pd.DataFrame(res);out.to_csv(O/'host_summary.csv',index=False)
plt.rcParams.update({'font.family':'Microsoft YaHei','axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'#faf9f6','axes.facecolor':'#faf9f6'})
fig,axes=plt.subplots(3,3,figsize=(12,10),sharex=True,sharey=True)
for ax,((year,noc),g) in zip(axes.flat,w.groupby(['host_year','NOC'])):
 ax.plot(g.relative_edition,g.medal_share,marker='o',color='#246477');ax.axvline(0,ls='--',color='#bbb');ax.set_title(f'{noc} {year}');ax.set_xticks([-1,0,1],['前届','主办届','后届']);ax.set_ylabel('奖牌记录份额 %');ax.grid(axis='y',alpha=.15)
fig.suptitle('主办届的提升，离开主场后还剩多少？',fontsize=17)
fig.subplots_adjust(bottom=.14,hspace=.4)
fig.text(.06,.025,'赛题CSV；运动员奖牌记录口径；排除1906；保留重复候选；九个现代案例，非全部东道主。\n2020保留官方届次年份；2024无后届观测；同一纵轴。描述性关联，不代表主办的因果效应。',fontsize=9)
fig.savefig(O/'figures/S1_host_windows.png',dpi=170,bbox_inches='tight')
print(out.round(3).to_string(index=False))
