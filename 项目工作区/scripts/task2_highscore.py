from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

ROOT=Path(__file__).resolve().parents[2]
TASK=ROOT/'交付文件'/'任务二_百年全景'
REPORT=TASK/'01_报告与说明'; TABLES=TASK/'02_数据表'; CODE=TASK/'03_复现代码'; FIG=TASK/'04_核心图表'
for folder in [REPORT,TABLES,CODE,FIG]: folder.mkdir(parents=True,exist_ok=True)
DATA=ROOT/'交付文件'/'任务一_数据体检'/'02_交付数据'/'归一数据_保留原始字段.csv.gz'
EVENTS_2024=ROOT/'交付文件'/'任务一_数据体检'/'02_交付数据'/'2024官方329小项奖牌表.csv'
d=pd.read_csv(DATA); d=d[d.include_main.astype(bool)].copy(); medal=d[d.is_medal.astype(bool)].copy()
years=sorted(d.Year.unique()); palette={'navy':'#153B4A','teal':'#247487','red':'#A64155','gold':'#C4903D','paper':'#FAF9F6','grid':'#D7DDDF','grey':'#7A878C'}
plt.rcParams.update({'font.family':'Microsoft YaHei','axes.spines.top':False,'axes.spines.right':False,
 'figure.facecolor':palette['paper'],'axes.facecolor':palette['paper'],'savefig.facecolor':palette['paper'],
 'axes.titleweight':'bold','axes.labelcolor':'#263238','xtick.color':'#34454B','ytick.color':'#34454B','savefig.dpi':220})

def finish(fig,name,note):
 fig.text(.055,.018,note,fontsize=8.5,color='#59686D',va='bottom')
 fig.savefig(FIG/f'{name}.png',bbox_inches='tight',dpi=220); plt.close(fig)

# A. Scale, inflation and concentration
ed=d.groupby('Year').agg(participation_records=('source_row','size'),delegations=('NOC','nunique'),sport_families=('sport_family','nunique'))
ed['medal_records']=medal.groupby('Year').size()
noc_medals=medal.groupby(['Year','NOC']).size().rename('medal_records').reset_index()
totals=noc_medals.groupby('Year').medal_records.sum()
ed['top5_share']=noc_medals.groupby('Year').apply(lambda x:x.nlargest(5,'medal_records').medal_records.sum(),include_groups=False)/totals
ed['hhi']=noc_medals.assign(s=lambda x:x.medal_records/x.Year.map(totals)).groupby('Year').s.apply(lambda s:(s*s).sum())
ed.to_csv(TABLES/'A_逐届规模与集中度.csv',encoding='utf-8-sig')
fig,axes=plt.subplots(2,2,figsize=(14,8.3)); ax=axes.flat
ax[0].plot(ed.index,ed.participation_records,color=palette['teal'],lw=2.6); ax[0].fill_between(ed.index,ed.participation_records,color=palette['teal'],alpha=.09); ax[0].set_title('参赛活动扩大近40倍'); ax[0].set_ylabel('运动员参赛记录数')
ax[1].plot(ed.index,ed.medal_records,color=palette['gold'],lw=2.6); ax[1].set_title('奖牌记录随项目和团体规模膨胀'); ax[1].set_ylabel('运动员奖牌记录数')
ax[2].plot(ed.index,ed.delegations,color=palette['navy'],lw=2.6); ax[2].set_title('代表团覆盖扩展到206个'); ax[2].set_ylabel('有参赛记录的NOC数')
ax[3].plot(ed.index,ed.top5_share*100,color=palette['red'],lw=2.6); ax[3].set_title('头部集中度长期下降'); ax[3].set_ylabel('前5代表团奖牌记录份额 (%)'); ax[3].axhline(50,color=palette['grid'],lw=1)
for a in ax: a.grid(axis='y',color=palette['grid'],lw=.7,alpha=.7); a.set_xlabel('届次年份')
for y,label in [(1916,'一战停办'),(1940,'二战停办'),(1944,'二战停办')]: ax[0].axvline(y,color=palette['grid'],lw=.8,ls='--')
fig.suptitle('A 规模扩张没有带来同等程度的奖牌垄断',fontsize=19,x=.055,ha='left')
finish(fig,'A_规模扩张与奖牌集中度','口径：运动员记录；排除1906；历史NOC分立；奖牌记录含团体成员。前5份额用于同届比较，不等于官方奖牌份额。')

total_rank=medal.groupby('NOC').size().sort_values(ascending=False).head(15).sort_values()
fig,ax=plt.subplots(figsize=(11,7)); bars=ax.barh(total_rank.index,total_rank.values,color=palette['teal'])
for bar,value in zip(bars,total_rank.values):
 ax.text(value+35,bar.get_y()+bar.get_height()/2,f'{value:,.0f}',va='center',fontsize=9,color='#263238')
ax.set_xlim(0,total_rank.max()*1.13); ax.set_xlabel('累计运动员奖牌记录数'); ax.set_title('A 历史累计榜同时奖励实力、参赛届次与团体项目规模',fontsize=16,loc='left'); ax.grid(axis='x',color=palette['grid'],alpha=.55)
finish(fig,'A_历史累计奖牌记录榜','口径：运动员奖牌记录；排除1906；原始重复候选保留。历史政体分别统计，不能与官方小项奖牌榜混用。')

# B. Rise and fall of 12 historical delegations
selected=['USA','GBR','URS','GDR','FRG','GER','CHN','JPN','KOR','AUS','FRA','NED']
grid=pd.MultiIndex.from_product([years,selected],names=['Year','NOC']).to_frame(index=False)
part=d.groupby(['Year','NOC']).size().rename('participation_records').reset_index()
b=grid.merge(part,how='left').merge(noc_medals,how='left')
b['present']=b.participation_records.notna(); b.loc[b.present,'medal_records']=b.loc[b.present,'medal_records'].fillna(0)
b['medal_share']=b.medal_records/b.Year.map(totals)
b.to_csv(TABLES/'B_十二代表团逐届份额.csv',index=False,encoding='utf-8-sig')
fig,axes=plt.subplots(3,4,figsize=(15,9),sharex=True,sharey=True)
for axis,noc in zip(axes.flat,selected):
 s=b[b.NOC.eq(noc)].copy(); segments=[]; current=[]
 for _,row in s.iterrows():
  if row.present: current.append((row.Year,row.medal_share*100))
  elif current: segments.append(current); current=[]
 if current: segments.append(current)
 for seg in segments:
  xs,ys=zip(*seg); axis.plot(xs,ys,color=palette['teal'],lw=2,marker='o',ms=2.7)
 outliers=s[s.medal_share.gt(.35) & s.present]
 if len(outliers):
  for _,point in outliers.iterrows():
   axis.scatter(point.Year,34.2,marker='^',s=38,color=palette['red'],zorder=5)
   axis.text(point.Year,31.2,f'{point.medal_share:.0%}',ha='center',va='top',fontsize=7.5,color=palette['red'])
 axis.set_title(noc,fontsize=12); axis.grid(axis='y',color=palette['grid'],alpha=.55); axis.set_ylim(0,35)
 axis.axvspan(1979,1985,color=palette['gold'],alpha=.06)
for axis in axes[-1,:]: axis.set_xlabel('届次年份')
for axis in axes[:,0]: axis.set_ylabel('同届奖牌记录份额 (%)')
fig.suptitle('B 强国不是一条连续曲线：战争、抵制与政体变迁留下断点',fontsize=19,x=.055,ha='left')
finish(fig,'B_十二代表团兴衰曲线','口径：同届运动员奖牌记录份额；排除1906；无参赛记录留空且不跨缺席连线；URS、GDR、FRG、GER分别保留。纵轴上限35%，三角标出超过上限的早期异常值；淡黄色提示1980/1984抵制潮。')

pivot=b.pivot(index='NOC',columns='Year',values='medal_share').reindex(selected)
fig,ax=plt.subplots(figsize=(15,6.3)); cmap=LinearSegmentedColormap.from_list('olympic',[palette['paper'],'#B9D1D5',palette['teal'],palette['navy']]); cmap.set_bad('#E8E6E0')
im=ax.imshow(pivot.values*100,aspect='auto',cmap=cmap,vmin=0,vmax=35)
ax.set_yticks(range(len(selected)),selected); ax.set_xticks(range(len(years)),years,rotation=90); ax.set_title('B 奖牌份额的时代接力',fontsize=17,loc='left'); cbar=fig.colorbar(im,ax=ax,pad=.015); cbar.set_label('同届奖牌记录份额 (%)')
finish(fig,'B_强国时代热力图','灰色为无参赛记录，不按零处理；颜色上限35%，极端早期届次会饱和。口径同B曲线。')

# C. Women: participation, medals and events
female=pd.DataFrame(index=years)
female['participation_share']=d.groupby('Year').Sex.apply(lambda s:s.eq('F').mean())
female['medal_share']=medal.groupby('Year').Sex.apply(lambda s:s.eq('F').mean())
event_rows=[]
for year,group in d[d.Year.le(2016)].groupby('Year'):
 units=group.groupby(['sport_family','Event']).Sex.agg(lambda s:set(s))
 event_rows.append({'Year':year,'event_units':len(units),'women_only_event_units':sum(v=={'F'} for v in units),'event_source':'赛题Event字段'})
ev=pd.DataFrame(event_rows).set_index('Year'); female=female.join(ev)
official=pd.read_csv(EVENTS_2024)
female.loc[2024,'event_units']=len(official); female.loc[2024,'women_only_event_units']=official.gender.eq('W').sum(); female.loc[2024,'event_source']='官方结构补充层'
female['women_only_event_share']=female.women_only_event_units/female.event_units
female.to_csv(TABLES/'C_女性参与获奖与小项.csv',encoding='utf-8-sig')
fig,ax=plt.subplots(figsize=(13,7)); ax.plot(female.index,female.participation_share*100,color=palette['teal'],lw=2.7,label='女性参赛记录占比'); ax.plot(female.index,female.medal_share*100,color=palette['red'],lw=2.4,label='女性奖牌记录占比')
mask=female.women_only_event_share.notna(); ax.plot(female.index[mask],female.loc[mask,'women_only_event_share']*100,color=palette['gold'],lw=2,marker='o',ms=3,label='女子小项占比')
ax.axhline(50,color=palette['grid'],ls='--'); ax.set_ylim(0,55); ax.set_ylabel('%'); ax.set_xlabel('届次年份'); ax.grid(axis='y',color=palette['grid'],alpha=.65); ax.legend(frameon=False,ncol=3,loc='upper left'); ax.set_title('C 接近参赛人数平权，不等于项目与奖牌结构完全平权',fontsize=17,loc='left')
ax.annotate(f"2024 参赛记录 {female.loc[2024,'participation_share']:.1%}\n女子小项 {female.loc[2024,'women_only_event_share']:.1%}",xy=(2024,female.loc[2024,'participation_share']*100),xytext=(1988,51),arrowprops={'arrowstyle':'->','color':palette['grey']},fontsize=10)
finish(fig,'C_女性三层平权曲线','参赛/奖牌按运动员记录；女子小项按仅女性参赛的事件单元。1896-2016取赛题Event，2024取329小项补充层；2020因Event泛化不绘小项点。排除1906。')

c=d[d.Year.eq(2024)].groupby('NOC').agg(records=('Sex','size'),female_records=('Sex',lambda s:s.eq('F').sum()))
cm=medal[medal.Year.eq(2024)].groupby('NOC').agg(medal_records=('Sex','size'),female_medal_records=('Sex',lambda s:s.eq('F').sum()))
c=c.join(cm); c['female_participation_share']=c.female_records/c.records; c['female_medal_share']=c.female_medal_records/c.medal_records; c['gap_pp']=(c.female_medal_share-c.female_participation_share)*100
c.to_csv(TABLES/'C_2024代表团女性结构.csv',encoding='utf-8-sig')
s=c.nlargest(15,'records').sort_values('gap_pp'); fig,ax=plt.subplots(figsize=(11,7)); y=np.arange(len(s)); ax.hlines(y,s.female_participation_share*100,s.female_medal_share*100,color='#AEB7BA',lw=2); ax.scatter(s.female_participation_share*100,y,color=palette['teal'],s=42,label='女性参赛记录占比'); ax.scatter(s.female_medal_share*100,y,color=palette['red'],s=42,label='女性奖牌记录占比'); ax.set_yticks(y,s.index); ax.axvline(50,color=palette['grid'],ls='--'); ax.set_xlim(0,100); ax.set_xlabel('%'); ax.legend(frameon=False,ncol=2,loc='lower right'); ax.set_title('C 2024主要代表团的女性参赛结构与奖牌结构并不同步',fontsize=16,loc='left'); ax.grid(axis='x',color=palette['grid'],alpha=.5)
finish(fig,'C_2024代表团女性结构差','选取参赛记录最多的15个NOC；差值反映项目与团体构成，不能解释为个人获奖概率或因果效应。')

# D. Event growth and sport lifecycle
event_count=d[d.Year.le(2016)].groupby('Year').Event.nunique().rename('event_units').to_frame(); event_count['source']='赛题Event字段'; event_count.loc[2024]=[329,'2024官方结构补充层']; event_count.to_csv(TABLES/'D_逐届小项数量.csv',encoding='utf-8-sig')
chosen=['Tug-Of-War','Croquet','Art Competitions','Polo','Figure Skating','Ice Hockey','Taekwondo','Triathlon','Rugby','Skateboarding','Surfing','Sport Climbing','Breaking']
presence=d[d.sport_family.isin(chosen)].groupby(['sport_family','Year']).size().unstack().reindex(index=chosen,columns=years)
presence.notna().astype(int).to_csv(TABLES/'D_代表项目出现矩阵.csv',encoding='utf-8-sig')
fig=plt.figure(figsize=(15,9)); gs=fig.add_gridspec(2,1,height_ratios=[1,2.2],hspace=.28); ax1=fig.add_subplot(gs[0]); ax2=fig.add_subplot(gs[1])
ax1.plot(event_count.index,event_count.event_units,color=palette['gold'],lw=2.7,marker='o',ms=3); ax1.set_ylabel('小项/事件单元数'); ax1.set_title('小项数量增长',loc='left'); ax1.grid(axis='y',color=palette['grid'],alpha=.6); ax1.annotate('2024：329',xy=(2024,329),xytext=(1990,345),arrowprops={'arrowstyle':'->','color':palette['grey']})
matrix=presence.notna().values; ax2.imshow(matrix,aspect='auto',cmap=matplotlib.colors.ListedColormap(['#ECE9E2',palette['teal']]),interpolation='nearest'); ax2.set_yticks(range(len(chosen)),chosen); ax2.set_xticks(range(len(years)),years,rotation=90); ax2.set_title('代表性运动家族的进入、退出与回归',loc='left')
fig.suptitle('D 奥运项目表不是只增不减，而是在扩张中持续换血',fontsize=19,x=.055,ha='left')
finish(fig,'D_小项增长与项目更替','1896-2016小项数取赛题Event去重；2024使用329小项补充层；2020因Event泛化留空。项目矩阵按归一运动家族，有记录即着色，不替代IOC正式项目认定。')

summary={
 'records_1896':int(ed.loc[1896,'participation_records']),'records_2024':int(ed.loc[2024,'participation_records']),
 'delegations_1896':int(ed.loc[1896,'delegations']),'delegations_2024':int(ed.loc[2024,'delegations']),
 'medal_records_1896':int(ed.loc[1896,'medal_records']),'medal_records_2024':int(ed.loc[2024,'medal_records']),
 'top5_share_1896':float(ed.loc[1896,'top5_share']),'top5_share_2024':float(ed.loc[2024,'top5_share']),
 'female_participation_2024':float(female.loc[2024,'participation_share']),'female_medal_2024':float(female.loc[2024,'medal_share']),
 'women_events_2024':int(female.loc[2024,'women_only_event_units']),'events_2024':329,
 'top_total_noc':total_rank.index[-1],'top_total_medal_records':int(total_rank.iloc[-1]),
}
(TABLES/'任务二关键指标.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False,indent=2))
