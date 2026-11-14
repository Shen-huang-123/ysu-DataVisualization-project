from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parents[1]; O=R/'outputs'; F=O/'figures'
plt.rcParams.update({'font.family':'Microsoft YaHei','axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'#faf9f6','axes.facecolor':'#faf9f6','savefig.dpi':170})
d=pd.read_csv(O/'olympics_flagged.csv.gz'); d=d[d.include_main]; years=sorted(d.Year.unique()); m=d[d.is_medal]
def save(fig,name,extra=''):
 fig.subplots_adjust(bottom=.17)
 fig.text(.05,.025,'来源：赛题CSV；排除1906；保留重复候选；参赛及奖牌均按记录行计。\n'+extra,fontsize=9,color='#555')
 fig.savefig(F/(name+'.png'),bbox_inches='tight'); plt.close(fig)
ed=d.groupby('Year').agg(records=('Sex','size'),delegations=('NOC','nunique'))
ed['medal_rows']=m.groupby('Year').size(); ed.to_csv(O/'panorama_scale.csv')
fig,axes=plt.subplots(1,3,figsize=(14,5))
for ax,col,label in zip(axes,['records','medal_rows','delegations'],['参赛记录数','奖牌记录数','代表团数']):
 ax.plot(ed.index,ed[col],color='#246477',lw=2); ax.set_title(label); ax.grid(axis='y',alpha=.15)
fig.suptitle('规模扩张改变了奖牌竞争的背景',fontsize=17);save(fig,'A_edition_scale')
selected=['USA','URS','GER','FRG','GDR','CHN','JPN','KOR','AUS','GBR']
grid=pd.MultiIndex.from_product([years,selected],names=['Year','NOC']).to_frame(index=False)
g=d.groupby(['Year','NOC']).size().rename('participation_rows').reset_index()
b=grid.merge(g,how='left').merge(m.groupby(['Year','NOC']).size().rename('medal_rows').reset_index(),how='left')
b['present']=b.participation_rows.notna(); b.loc[b.present,'medal_rows']=b.loc[b.present,'medal_rows'].fillna(0)
b['medal_share']=b.medal_rows/b.Year.map(m.groupby('Year').size())*100
b.to_csv(O/'country_trends_with_absence.csv',index=False)
fig,axes=plt.subplots(2,5,figsize=(16,7),sharex=True,sharey=True)
for ax,noc in zip(axes.flat,selected):
 s=b[b.NOC.eq(noc)];ax.plot(s.Year,s.medal_share,marker='.',color='#246477');ax.set_title(noc);ax.grid(axis='y',alpha=.15)
fig.suptitle('十个历史代表团的奖牌记录份额',fontsize=17);save(fig,'B_country_trends','同一纵轴；空缺表示数据中无参赛记录，折线不跨越缺席届次；历史NOC分别保留。')
c=d[d.Year.eq(2024)].groupby('NOC').agg(records=('Sex','size'),female_records=('Sex',lambda s:s.eq('F').sum()))
c['female_participation_share']=c.female_records/c.records
cm=m[m.Year.eq(2024)].groupby('NOC').agg(medal_rows=('Sex','size'),female_medal_rows=('Sex',lambda s:s.eq('F').sum()))
c=c.join(cm);c['female_medal_share']=c.female_medal_rows/c.medal_rows;c.to_csv(O/'female_country_2024.csv')
s=c.nlargest(15,'records').sort_values('female_participation_share')
fig,ax=plt.subplots(figsize=(11,7)); y=np.arange(len(s))
ax.hlines(y,s.female_participation_share*100,s.female_medal_share*100,color='#aaa')
ax.scatter(s.female_participation_share*100,y,color='#246477',label='女性占参赛记录比例')
ax.scatter(s.female_medal_share*100,y,color='#a23d52',label='女性占奖牌记录比例')
ax.set_yticks(y,s.index);ax.set_xlim(0,100);ax.set_xlabel('%');ax.axvline(50,ls='--',color='#ccc');ax.legend(loc='lower right');ax.set_title('2024：女性参赛与获奖的结构并不总是一致')
save(fig,'C_country_female_structure','选取参赛记录最多的15个代表团；奖牌占比不是个人获奖概率，混合项目按成员性别计入。')
chosen=['Tug-Of-War','Art Competitions','Polo','Figure Skating','Ice Hockey','Taekwondo','Rugby','Skateboarding','Surfing','Breaking','Sport Climbing']
presence=d[d.sport_family.isin(chosen)].groupby(['sport_family','Year']).size().unstack().reindex(index=chosen,columns=years)
presence.to_csv(O/'sport_presence_selected.csv')
fig,ax=plt.subplots(figsize=(14,6)); ax.imshow(presence.notna().values,aspect='auto',cmap=matplotlib.colors.ListedColormap(['#ebe8e1','#246477']),interpolation='nearest')
ax.set_yticks(range(len(chosen)),chosen);ax.set_xticks(range(len(years)),years,rotation=90);ax.set_title('项目的进入与离场：夏奥数据里的历史切片')
save(fig,'D_sport_presence','深色表示该家族在数据中有记录；Rugby家族包含传统橄榄球与七人制；不代表正式项目认定或完整项目清单。')
print(ed.iloc[[0,-1]].to_string());print(c.loc[['CHN','USA','JPN','NED'],['female_participation_share','female_medal_share']].to_string())
