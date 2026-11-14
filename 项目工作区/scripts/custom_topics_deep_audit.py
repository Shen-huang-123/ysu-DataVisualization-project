"""Reproducible denominator and robustness checks for four self-selected topics."""
from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from task2_localization import NOC_ZH, SPORT_ZH

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'交付文件/任务三_专题深挖'
DATA=ROOT/'交付文件/任务一_数据体检/02_交付数据/归一数据_保留原始字段.csv.gz'
df=pd.read_csv(DATA,low_memory=False)
df=df[df.include_main.eq(True)].copy()
df.Year=pd.to_numeric(df.Year,errors='raise').astype(int)
med=df[df.is_medal.eq(True)].copy()
plt.rcParams.update({'font.family':'Microsoft YaHei','axes.unicode_minus':False,'font.size':10,'figure.facecolor':'#f7f5ef','axes.facecolor':'#f7f5ef','axes.edgecolor':'#aabdb9','text.color':'#173b42','axes.labelcolor':'#173b42','xtick.color':'#5b7072','ytick.color':'#5b7072'})
TEAL='#187f87';GOLD='#c69a57'
def folder(slug):
 p=BASE/slug/'08_深度复核';p.mkdir(parents=True,exist_ok=True);return p
def save(fig,p,name):
 fig.tight_layout(pad=1.5);fig.savefig(p/name,dpi=180,bbox_inches='tight');plt.close(fig)

# S7: empirical streak distribution. Right censoring is disclosed in prose.
p7=folder('S3_冠军的保质期')
base=BASE/'S3_冠军的保质期/02_数据表'
t=pd.read_csv(base/'S3_逐小项冠军控制权转移.csv')
s=pd.read_csv(base/'S3_冠军王朝清单.csv')
streak=pd.DataFrame({'length':[1,2,3,4,5]})
streak['runs_at_least']=streak.length.map(lambda k:int((s.editions>=k).sum()))
streak['runs_at_least_share']=streak.runs_at_least/len(s)
streak.to_csv(p7/'S7_王朝长度分布.csv',index=False,encoding='utf-8-sig')
fig,ax=plt.subplots(figsize=(8.4,4.2));ax.bar(streak.length,streak.runs_at_least_share*100,color=[GOLD]+[TEAL]*4)
ax.set_xticks(streak.length);ax.set_xlabel('至少连续夺金的届数');ax.set_ylabel('占已识别连冠段的比例（%）');ax.set_title('冠军优势的寿命：长王朝是少数',loc='left',weight='bold')
for x,y in zip(streak.length,streak.runs_at_least_share):ax.text(x,y*100+1,f'{y:.1%}',ha='center',fontsize=9)
ax.set_ylim(0,108);ax.spines[['top','right']].set_visible(False);save(fig,p7,'S7_王朝寿命分布.png')

# S8: participant and award records use comparable but distinct denominators.
p8=folder('S8_她们登上领奖台')
part=df.groupby(['Year','Sex']).size().unstack(fill_value=0)
aw=med.groupby(['Year','Sex']).size().unstack(fill_value=0)
sex=pd.DataFrame({'Year':sorted(set(part.index)&set(aw.index))})
sex['female_participation_share']=sex.Year.map(part.F/part.sum(axis=1))
sex['female_award_share']=sex.Year.map(aw.F/aw.sum(axis=1))
sex['gap_pp']=(sex.female_award_share-sex.female_participation_share)*100
sex.to_csv(p8/'S8_逐届参赛与获奖占比差.csv',index=False,encoding='utf-8-sig')
n24=df[df.Year.eq(2024)].groupby(['NOC','Sex']).size().unstack(fill_value=0).rename(columns={'F':'participant_F','M':'participant_M'})
a24=med[med.Year.eq(2024)].groupby(['NOC','Sex']).size().unstack(fill_value=0).rename(columns={'F':'award_F','M':'award_M'})
noc=n24.join(a24,how='left').fillna(0)
noc['participant_rows']=noc.participant_F+noc.participant_M
noc['award_rows']=noc.award_F+noc.award_M
noc['gap_pp']=(noc.award_F/noc.award_rows-noc.participant_F/noc.participant_rows)*100
noc=noc[noc.award_rows>=20].sort_values('gap_pp')
noc.to_csv(p8/'S8_2024代表团结构差_至少20获奖行.csv',encoding='utf-8-sig')
fig,ax=plt.subplots(figsize=(9,4.5));ax.plot(sex.Year,sex.female_participation_share*100,label='女性参赛记录',color=TEAL,lw=2.5)
ax.plot(sex.Year,sex.female_award_share*100,label='女性获奖记录',color=GOLD,lw=2.5)
ax.set_xlabel('奥运届次年份');ax.set_ylabel('女性记录占比（%）');ax.set_title('两种分母下的女性可见度',loc='left',weight='bold');ax.legend(frameon=False);ax.grid(axis='y',alpha=.25);ax.spines[['top','right']].set_visible(False);save(fig,p8,'S8_参赛与获奖双曲线.png')

# S9: reappearance after a gap is separate from current absence.
p9=folder('S9_消失的赛场')
years=sorted(df.Year.unique())
presence=(df.groupby(['sport_family','Year']).size().unstack(fill_value=0)>0).reindex(columns=years,fill_value=False)
life=[]
for fam,row in presence.iterrows():
 vals=row.to_numpy(dtype=bool);first=np.flatnonzero(vals)[0];last=np.flatnonzero(vals)[-1]
 entries=int(sum(vals[i] and not vals[i-1] for i in range(1,len(vals))))
 life.append({'sport_family':fam,'first_year':years[first],'last_year':years[last],'editions_present':int(vals.sum()),'return_after_gap':max(entries-1,0),'absent_in_2024':not bool(vals[-1])})
life=pd.DataFrame(life).sort_values(['return_after_gap','editions_present'],ascending=False)
life.to_csv(p9/'S9_运动家族出现与重返.csv',index=False,encoding='utf-8-sig')
chart=life.sort_values('editions_present',ascending=False).head(15).sort_values('editions_present')
fig,ax=plt.subplots(figsize=(9,5));ax.barh([SPORT_ZH.get(x,x) for x in chart.sport_family],chart.editions_present,color=[GOLD if x else TEAL for x in chart.return_after_gap.gt(0)])
ax.set_xlabel('出现届数');ax.set_title('出现很多届，不等于从未中断',loc='left',weight='bold');ax.legend(handles=[Patch(color=GOLD,label='曾缺席后重返'),Patch(color=TEAL,label='未观察到中断')],frameon=False,loc='lower right');ax.spines[['top','right']].set_visible(False);save(fig,p9,'S9_出现届数与重返.png')

# S10: historical gross count versus same-year, within-sport shares.
p10=folder('S10_奖牌藏在哪些项目')
overall=med.groupby('sport_family').size().sort_values(ascending=False)
top3=overall.head(3)
modern=med[med.Year.eq(2024)]
by=modern.groupby(['sport_family','NOC']).size().rename('award_rows').reset_index()
size=modern.groupby('sport_family').size().rename('sport_total_rows')
by=by.join(size,on='sport_family');by['within_sport_share']=by.award_rows/by.sport_total_rows
fam=by.sort_values(['sport_family','award_rows'],ascending=[True,False]).groupby('sport_family').head(1)
fam=fam[fam.sport_total_rows>=25].sort_values('within_sport_share',ascending=False)
fam.to_csv(p10/'S10_2024大类最大代表团份额.csv',index=False,encoding='utf-8-sig')
totals=pd.DataFrame({'sport_family':overall.index,'award_rows':overall.values});totals['share_all']=totals.award_rows/len(med)
totals.to_csv(p10/'S10_历史获奖记录大类份额.csv',index=False,encoding='utf-8-sig')
fig,ax=plt.subplots(figsize=(9,5));show=fam.head(12).sort_values('within_sport_share')
ax.barh([SPORT_ZH.get(a,a)+' · '+NOC_ZH.get(b,b) for a,b in zip(show.sport_family,show.NOC)],show.within_sport_share*100,color=TEAL)
ax.set_xlabel('该运动2024获奖记录中的最大代表团份额（%）');ax.set_title('换一个分母：看项目内的相对优势',loc='left',weight='bold');ax.spines[['top','right']].set_visible(False);save(fig,p10,'S10_项目内代表团份额.png')

summary={'s7':{'transitions':len(t),'defense_rate':round(float(t.defended.mean()),4),'streaks':len(s),'two_or_more_share':round(float((s.editions>=2).mean()),4)},'s8':{'2024_participation_share':round(float(sex.loc[sex.Year.eq(2024),'female_participation_share'].iloc[0]),4),'2024_award_share':round(float(sex.loc[sex.Year.eq(2024),'female_award_share'].iloc[0]),4),'2024_gap_pp':round(float(sex.loc[sex.Year.eq(2024),'gap_pp'].iloc[0]),3),'noc_min_award_rows':20,'nocs_eligible':len(noc)},'s9':{'families':len(life),'families_returned':int(life.return_after_gap.gt(0).sum()),'families_absent_2024':int(life.absent_in_2024.sum())},'s10':{'top3_rows':int(top3.sum()),'top3_share':round(float(top3.sum()/len(med)),4),'2024_families_with_25_rows':len(fam)}}
(BASE/'自拟专题深度核验摘要.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False,indent=2))
