"""A 2024-only sensitivity test requiring no unverified historical medal outcomes."""
from pathlib import Path
import pandas as pd
from s2_sport_family import family
from scipy.stats import kendalltau

ROOT=Path(__file__).resolve().parents[2]
TASK=ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力'
OFF=ROOT/'交付文件/任务一_数据体检/02_交付数据/2024官方329小项奖牌表.csv'
DATA=ROOT/'交付文件/任务一_数据体检/02_交付数据/归一数据_保留原始字段.csv.gz'
OUT=TASK/'02_数据表'
o=pd.read_csv(OFF)
d=pd.read_csv(DATA)
d=d[(d.Year==2024)&d.include_main.astype(bool)&d.is_medal.astype(bool)&d.NOC.ne('AIN')]

official=[]
for r in o.itertuples(index=False):
 for color,col in [('Gold','gold_country_code'),('Silver','silver_country_code'),('Bronze','bronze_country_code')]:
  codes=getattr(r,col)
  if pd.isna(codes):continue
  for noc in str(codes).split('|'):
   noc=noc.strip()
   if noc and noc!='AIN':official.append((r.event_id,family(r.discipline),noc,color))
off=pd.DataFrame(official,columns=['event_id','family','NOC','Medal'])
rows=d[['source_row','sport_family','NOC','Medal']].rename(columns={'sport_family':'family'})
assert set(off.family)==set(rows.family),(set(off.family)-set(rows.family),set(rows.family)-set(off.family))
assert off.event_id.nunique()==329

def ranking(frame):
 z=frame.groupby(['NOC','Medal']).size().unstack(fill_value=0).reindex(columns=['Gold','Silver','Bronze'],fill_value=0)
 z=z.sort_values(['Gold','Silver','Bronze'],ascending=False)
 ranks={};out={}
 for pos,(noc,r) in enumerate(z.iterrows(),1):
  key=(r.Gold,r.Silver,r.Bronze)
  ranks.setdefault(key,pos)
  out[noc]=ranks[key]
 return out

base_o=ranking(off);base_r=ranking(rows)
top=[noc for noc,_ in sorted(base_o.items(),key=lambda x:x[1]) if base_o[noc]<=20]
def measure(drop=None):
 a=off if drop is None else off[off.family.ne(drop)]
 b=rows if drop is None else rows[rows.family.ne(drop)]
 x=ranking(a);y=ranking(b);alln=sorted(set(x)|set(y))
 # Place delegations with no medals in a lens one place below that lens's last rank.
 xo=[x.get(n,len(alln)+1) for n in alln];yo=[y.get(n,len(alln)+1) for n in alln]
 shifts={n:y.get(n,len(alln)+1)-x.get(n,len(alln)+1) for n in top}
 return {'removed_family':drop or 'none','official_events':a.event_id.nunique(),
         'athlete_medal_rows':len(b),'kendall_tau':kendalltau(xo,yo).statistic,
         'top20_mean_abs_rank_shift':sum(abs(v) for v in shifts.values())/len(shifts),
         'top20_shifted_nocs':sum(v!=0 for v in shifts.values())},shifts

summary=[];shifts=[]
for drop in [None]+sorted(off.family.unique()):
 s,part=measure(drop);summary.append(s)
 shifts.extend({'removed_family':s['removed_family'],'NOC':n,'rank_shift_rows_minus_official':v} for n,v in part.items())
S=pd.DataFrame(summary);T=pd.DataFrame(shifts)
S.to_csv(OUT/'S2_2024逐大类剔除敏感性.csv',index=False,encoding='utf-8-sig')
T.to_csv(OUT/'S2_2024代表团剔除敏感性.csv',index=False,encoding='utf-8-sig')
print('families',len(S)-1,'baseline',S.iloc[0].to_dict())
print('tau range',S.iloc[1:].kendall_tau.min(),S.iloc[1:].kendall_tau.max())
print('top20 shift range',S.iloc[1:].top20_mean_abs_rank_shift.min(),S.iloc[1:].top20_mean_abs_rank_shift.max())

# A compact figure showing the result survives deleting any one sport family.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Microsoft YaHei'
fig,(ax,ax2)=plt.subplots(1,2,figsize=(13.4,6.0),gridspec_kw={'width_ratios':[1.1,1.3]})
fig.patch.set_facecolor('#F7F3EB')
for a in (ax,ax2):
 a.set_facecolor('#F7F3EB');a.spines[['top','right']].set_visible(False);a.grid(axis='x',color='#D9DEDC',alpha=.8);a.set_axisbelow(True)
sub=S[S.removed_family.ne('none')].sort_values('kendall_tau')
ax.scatter(sub.kendall_tau,range(len(sub)),s=28,color='#247487',alpha=.75)
ax.axvline(S.iloc[0].kendall_tau,color='#A64155',lw=2,label='未剔除：35类')
ax.set_yticks([0,len(sub)//2,len(sub)-1],['最低','35次单类剔除','最高'])
ax.set_xlim(.88,.95);ax.set_xlabel('两口径榜单 Kendall τ');ax.set_title('剔除任一运动大类，\n榜单差异仍在',loc='left',fontweight='bold')
ax.legend(frameon=False,loc='lower right')
focus=['ESP','NED','JPN','UZB']
for pos,noc in enumerate(focus):
 vals=T[(T.NOC.eq(noc))&(T.removed_family.ne('none'))].rank_shift_rows_minus_official
 base=T[(T.NOC.eq(noc))&(T.removed_family.eq('none'))].rank_shift_rows_minus_official.iloc[0]
 ax2.plot([vals.min(),vals.max()],[pos,pos],lw=7,color='#A64155' if base<0 else '#247487',alpha=.6,solid_capstyle='round')
 ax2.scatter([base],[pos],s=90,color='#172A30',zorder=3)
 ax2.text(vals.max()+.35,pos,f'{int(vals.min()):+d}～{int(vals.max()):+d}',va='center',fontsize=10)
ax2.axvline(0,color='#172A30',lw=1)
ax2.set_yticks(range(4),['西班牙','荷兰','日本','乌兹别克斯坦']);ax2.invert_yaxis()
ax2.set_xlim(-16,11);ax2.set_xlabel('行口径名次 − 官方口径名次（负值表示上升）')
ax2.set_title('关键代表团的方向\n经35次剔除均未反转',loc='left',fontweight='bold')
fig.text(.04,.075,'口径：官方329小项榜 vs 赛题运动员获奖行榜；名次差单位：位。',fontsize=9,color='#344f56')
fig.text(.04,.050,'来源：任务一2024官方小项表、赛题运动员记录。',fontsize=9,color='#344f56')
fig.text(.04,.025,'限制：35次单类剔除是同届扰动检验；只证明所列代表团方向在这35种排除下未反转。',fontsize=9,color='#344f56')
fig.tight_layout(rect=(0,.13,1,1),w_pad=2.5)
fig.savefig(TASK/'04_核心图表/S2_2024逐大类剔除稳健性.png',dpi=220,bbox_inches='tight')
plt.close(fig)
