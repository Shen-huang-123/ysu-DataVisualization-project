from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'outputs'
FIG=OUT/'figures'; FIG.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'Microsoft YaHei','axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'#faf9f6','axes.facecolor':'#faf9f6','axes.titleweight':'bold','savefig.dpi':160})
d=pd.read_csv(OUT/'olympics_flagged.csv.gz'); d=d[d.include_main]
e=pd.read_csv(OUT/'edition_main.csv')
note='口径：运动员参赛记录；排除1906；原始重复候选保留。来源：赛题CSV。'
def save(fig,name):
 fig.text(.06,.025,note,fontsize=9,color='#555555'); fig.savefig(FIG/f'{name}.png',bbox_inches='tight'); plt.close(fig)

fig,ax=plt.subplots(figsize=(11,6)); a=d[d.is_medal].groupby('NOC').size().nlargest(15).sort_values()
ax.barh(a.index,a.values,color='#246477'); ax.set(title='A  历史奖牌记录集中于哪些代表团',xlabel='奖牌记录数（团体成员各计一行）'); fig.subplots_adjust(bottom=.15); save(fig,'A_medal_rows')
selected=['USA','URS','GER','GDR','CHN','JPN','KOR','AUS','GBR']
fig,axes=plt.subplots(3,3,figsize=(12,9),sharex=True)
tot=d[d.is_medal].groupby('Year').size()
for ax,noc in zip(axes.flat,selected):
 present=d[d.NOC.eq(noc)].groupby('Year').size().index
 medals=d[d.NOC.eq(noc)&d.is_medal].groupby('Year').size().reindex(present,fill_value=0)
 share=medals/tot.reindex(present)*100
 ax.plot(share.index,share.values,color='#246477',marker='.',lw=1.6); ax.set_title(noc); ax.set_ylabel('奖牌记录份额 %'); ax.grid(axis='y',alpha=.15)
fig.suptitle('B  九个代表团的奖牌记录份额',fontsize=17); fig.subplots_adjust(bottom=.1,hspace=.5); save(fig,'B_country_shares')
fig,ax=plt.subplots(figsize=(11,6)); ax.plot(e.Year,e.female_record_share*100,color='#a23d52',lw=2.5); ax.axhline(50,color='#999',ls='--',lw=1); ax.set(title='C  女性参赛记录占比接近一半',ylabel='女性记录 / 全部参赛记录 %',xlabel='届次年份',ylim=(0,55)); ax.annotate('2024：49.10%',(2024,49.1002),xytext=(1990,35),arrowprops={'arrowstyle':'->'}); fig.subplots_adjust(bottom=.15); save(fig,'C_female_records')
fig,ax=plt.subplots(figsize=(11,6)); ax.plot(e.Year,e.sport_families,color='#246477',marker='o'); ax.set(title='D  统一运动家族的覆盖变化',ylabel='数据中出现的运动家族数',xlabel='届次年份'); ax.text(.02,.95,'家族层级为本项目定义；不等于IOC大项数或小项数',transform=ax.transAxes,va='top',fontsize=10); fig.subplots_adjust(bottom=.15); save(fig,'D_sport_families')
print('Created four exploratory figures')
