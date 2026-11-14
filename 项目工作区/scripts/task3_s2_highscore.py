from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from task2_localization import NOC_ZH

ROOT=Path(__file__).resolve().parents[2]
TASK=ROOT/'交付文件'/'任务三_专题深挖'/'S2_口径的魔力'
REPORT=TASK/'01_报告与说明'; TABLE=TASK/'02_数据表'; CODE=TASK/'03_复现代码'; FIG=TASK/'04_核心图表'
for x in [REPORT,TABLE,CODE,FIG]: x.mkdir(parents=True,exist_ok=True)
DATA=ROOT/'交付文件'/'任务一_数据体检'/'02_交付数据'/'归一数据_保留原始字段.csv.gz'
OFFICIAL=ROOT/'交付文件'/'任务一_数据体检'/'02_交付数据'/'2024官方329小项奖牌表.csv'
d=pd.read_csv(DATA); d=d[d.include_main.astype(bool)].copy(); a=d[(d.Year.eq(2024))&d.is_medal.astype(bool)].copy(); o=pd.read_csv(OFFICIAL)

P={'paper':'#F7F3EB','ink':'#172A30','teal':'#247487','red':'#A64155','gold':'#C4903D','blue':'#65A9B4','grid':'#D9DEDC','grey':'#6C7A80'}
plt.rcParams.update({'font.family':'Microsoft YaHei','axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':P['paper'],'axes.facecolor':P['paper'],'savefig.facecolor':P['paper'],'savefig.dpi':220})
def finish(fig,name,note): fig.text(.045,.012,note,fontsize=8.2,color=P['grey']); fig.savefig(FIG/name,bbox_inches='tight',dpi=220); plt.close(fig)

def split_codes(s):
    if pd.isna(s): return []
    return [x.strip() for x in str(s).split('|') if x.strip()]

official=[]
for medal,col in [('Gold','gold_country_code'),('Silver','silver_country_code'),('Bronze','bronze_country_code')]:
    for event_id,codes in zip(o.event_id,o[col]):
        for noc in split_codes(codes): official.append({'event_id':event_id,'NOC':noc,'Medal':medal})
official=pd.DataFrame(official)
off=official.pivot_table(index='NOC',columns='Medal',values='event_id',aggfunc='count',fill_value=0).reindex(columns=['Gold','Silver','Bronze'],fill_value=0)
rows=a.pivot_table(index='NOC',columns='Medal',values='source_row',aggfunc='count',fill_value=0).reindex(columns=['Gold','Silver','Bronze'],fill_value=0)

def medal_rank(frame):
    f=frame.copy(); f['_key']=list(zip(-f.Gold,-f.Silver,-f.Bronze)); ordered=sorted(f._key.tolist()); rank={}
    for i,key in enumerate(ordered,1): rank.setdefault(key,i)
    return f._key.map(rank)
off['official_rank']=medal_rank(off); rows['row_rank']=medal_rank(rows)
alln=off.join(rows,how='outer',lsuffix='_official',rsuffix='_rows').fillna(0)
alln=alln.drop(index=['AIN'],errors='ignore')
alln['official_total']=alln[['Gold_official','Silver_official','Bronze_official']].sum(axis=1)
alln['row_total']=alln[['Gold_rows','Silver_rows','Bronze_rows']].sum(axis=1)
alln['gold_multiplier']=alln.Gold_rows/alln.Gold_official.replace(0,np.nan)
alln['rank_shift']=alln.official_rank-alln.row_rank

gold=a[a.Medal.eq('Gold')].copy(); gold['award_group_size']=gold.groupby(['NOC','Event','Medal']).source_row.transform('size'); multi=gold[gold.award_group_size.gt(1)].groupby('NOC').size(); total_gold_rows=gold.groupby('NOC').size()
alln['multi_gold_rows']=multi; alln['gold_rows_total_check']=total_gold_rows; alln[['multi_gold_rows','gold_rows_total_check']]=alln[['multi_gold_rows','gold_rows_total_check']].fillna(0)
alln['multi_gold_row_share']=alln.multi_gold_rows/alln.gold_rows_total_check.replace(0,np.nan)
eligible=alln[(alln.Gold_official.gt(0))&alln.gold_multiplier.notna()&alln.multi_gold_row_share.notna()].copy()
rho,p=spearmanr(eligible.gold_multiplier,eligible.multi_gold_row_share)
alln.reset_index().to_csv(TABLE/'S2_2024双口径完整排名.csv',index=False,encoding='utf-8-sig')
official.to_csv(TABLE/'S2_官方小项奖牌长表.csv',index=False,encoding='utf-8-sig')

# Figure 1: rank slope, official top 15.
top=alln.sort_values('official_rank').head(15).copy().sort_values('official_rank')
rank_bottom=max(16,float(top.row_rank.max())+1)
fig,ax=plt.subplots(figsize=(11,9)); ax.set_xlim(-.15,1.15); ax.set_ylim(rank_bottom,.2); ax.axis('off')
ax.text(0,0,'官方小项口径',ha='center',fontsize=15,fontweight='bold',color=P['teal']); ax.text(1,0,'运动员行口径',ha='center',fontsize=15,fontweight='bold',color=P['red'])
for noc,r in top.iterrows():
    y1=r.official_rank; y2=r.row_rank; color=P['red'] if abs(y2-y1)>=4 else P['grey']; ax.plot([0,1],[y1,y2],color=color,alpha=.8,lw=2 if color==P['red'] else 1.2)
    ax.scatter([0,1],[y1,y2],s=45,color=[P['teal'],P['red']],zorder=3); ax.text(-.03,y1,f'{int(y1)}  {noc}',ha='right',va='center',fontsize=10); ax.text(1.03,y2,f'{noc}  {int(y2)}',ha='left',va='center',fontsize=10)
ax.set_title('S2 同一届奥运，只换统计单位，奖牌榜就会重排',fontsize=20,fontweight='bold',loc='left',pad=24)
finish(fig,'S2_双口径排名重排.png','官方口径：2024官方329小项获奖结果，按金银铜排序；行口径：运动员获奖记录，按金银铜排序；均排除AIN，1906不涉及。')

# Figure 2: mechanism scatter.
fig,ax=plt.subplots(figsize=(11,7)); sizes=np.sqrt(eligible.Gold_official)*45
ax.scatter(eligible.multi_gold_row_share*100,eligible.gold_multiplier,s=sizes,color=P['teal'],alpha=.78,edgecolor='white',linewidth=1)
labels=set(eligible.gold_multiplier.nlargest(8).index)|{'USA','CHN','NED','ESP','JPN'}
offsets={'USA':(10,-10),'FRA':(-28,10),'CHN':(8,7),'NED':(7,7),'ESP':(7,7),'JPN':(7,7)}
for noc in labels:
    if noc in eligible.index:
        r=eligible.loc[noc]; ax.annotate(noc,(r.multi_gold_row_share*100,r.gold_multiplier),xytext=offsets.get(noc,(5,5)),textcoords='offset points',fontsize=9,fontweight='bold' if noc in {'USA','CHN','NED','ESP'} else 'normal')
ax.set_xlabel('多人获奖组贡献的金牌记录占比 (%)'); ax.set_ylabel('每枚官方金牌对应的运动员金牌记录数'); ax.grid(color=P['grid'],alpha=.7)
ax.set_title('S2 名次变化不是魔法：多人获奖结构解释金牌行膨胀',fontsize=18,fontweight='bold',loc='left')
ax.text(.99,.04,f'Spearman ρ = {rho:.3f}\np = {p:.2e}',transform=ax.transAxes,ha='right',fontsize=12,color=P['red'],fontweight='bold')
finish(fig,'S2_多人项目与金牌行膨胀.png','样本：2024至少1枚官方金牌且原始表有金牌记录的代表团；多人获奖组定义为同NOC-Event-Medal下记录数>1。相关不等于因果。')

# Figure 3: official gold vs athlete rows and multiplier.
show=alln[alln.Gold_official.gt(0)].sort_values('Gold_official',ascending=False).head(15).sort_values('Gold_official')
fig,axes=plt.subplots(1,2,figsize=(14,8),gridspec_kw={'width_ratios':[1.45,1]})
y=np.arange(len(show)); axes[0].barh(y,show.Gold_rows,color=P['red'],alpha=.84,label='运动员金牌记录'); axes[0].barh(y,show.Gold_official,color=P['gold'],label='官方小项金牌'); axes[0].set_yticks(y,[NOC_ZH.get(x,x) for x in show.index]); axes[0].set_xlabel('金牌计数'); axes[0].legend(frameon=False); axes[0].grid(axis='x',color=P['grid']); axes[0].set_title('同样是“金牌”，数的是竞赛单元还是获奖者',loc='left',fontweight='bold')
mult=alln[alln.Gold_official.gt(0)].gold_multiplier.nlargest(15).sort_values(); axes[1].barh([NOC_ZH.get(x,x) for x in mult.index],mult.values,color=P['teal']); axes[1].axvline(1,color=P['ink'],lw=.8); axes[1].set_xlabel('金牌行 ÷ 官方金牌'); axes[1].grid(axis='x',color=P['grid']); axes[1].set_title('高倍率代表团被行口径放大',loc='left',fontweight='bold')
fig.suptitle('S2 两套口径回答的是两个不同问题',fontsize=20,fontweight='bold',x=.04,ha='left')
finish(fig,'S2_金牌数量与获奖者规模.png','官方口径回答“赢下多少小项”；运动员行口径回答“产生多少获奖者记录”。倍率不是平均队伍人数，也不代表更公平。')

# Figure 4: which sports create gold rows for selected delegations.
selected=['USA','CHN','NED','ESP','FRA','GBR','JPN','AUS']
sp=gold[gold.NOC.isin(selected)].pivot_table(index='NOC',columns='sport_family',values='source_row',aggfunc='count',fill_value=0)
cols=sp.sum().nlargest(12).index; sp=sp.reindex(selected).reindex(columns=cols,fill_value=0)
fig,ax=plt.subplots(figsize=(14,6)); im=ax.imshow(sp.values,aspect='auto',cmap='YlGnBu',vmin=0,vmax=max(12,np.quantile(sp.values,.95)))
ax.set_yticks(range(len(sp.index)),sp.index); ax.set_xticks(range(len(sp.columns)),sp.columns,rotation=45,ha='right')
for i in range(sp.shape[0]):
    for j in range(sp.shape[1]):
        if sp.iat[i,j]: ax.text(j,i,str(int(sp.iat[i,j])),ha='center',va='center',fontsize=8,color='white' if sp.iat[i,j]>8 else P['ink'])
ax.set_title('S2 相同金牌数背后，是完全不同的获奖者结构',fontsize=18,fontweight='bold',loc='left'); cb=fig.colorbar(im,ax=ax,pad=.015); cb.set_label('运动员金牌记录数')
finish(fig,'S2_代表团金牌记录项目结构.png','运动员行口径；2024；数字为各体育大类金牌记录数。团体、接力和多人艇等会产生多条记录，不能解释为官方金牌数。')

metrics={'official_events':int(len(o)),'official_gold_units':int(len(official[official.Medal.eq('Gold')])),'official_silver_units':int(len(official[official.Medal.eq('Silver')])),'official_bronze_units':int(len(official[official.Medal.eq('Bronze')])),'athlete_medal_rows':int(len(a)),'spearman_rho':float(rho),'spearman_p':float(p),'eligible_nocs':int(len(eligible)),'usa_gold_units':int(alln.loc['USA','Gold_official']),'usa_gold_rows':int(alln.loc['USA','Gold_rows']),'chn_gold_units':int(alln.loc['CHN','Gold_official']),'chn_gold_rows':int(alln.loc['CHN','Gold_rows']),'ned_gold_units':int(alln.loc['NED','Gold_official']),'ned_gold_rows':int(alln.loc['NED','Gold_rows']),'esp_gold_units':int(alln.loc['ESP','Gold_official']),'esp_gold_rows':int(alln.loc['ESP','Gold_rows'])}
(TABLE/'S2_关键指标.json').write_text(json.dumps(metrics,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(metrics,ensure_ascii=False,indent=2))
