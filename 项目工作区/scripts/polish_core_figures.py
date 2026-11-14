from pathlib import Path
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[2]
folder=ROOT/'交付文件/任务四_开放创作/02_2028洛杉矶预测'
rows=list(csv.DictReader((folder/'LA2028奖牌预测完整榜.csv').open(encoding='utf-8-sig',newline='')))
names={'USA':'美国','CHN':'中国','GBR':'英国','FRA':'法国','AUS':'澳大利亚','JPN':'日本','GER':'德国','ITA':'意大利','KOR':'韩国','NED':'荷兰','CAN':'加拿大','RUS':'俄罗斯','NZL':'新西兰','HUN':'匈牙利','UZB':'乌兹别克斯坦'}
rows=sorted(rows[:15],key=lambda r:-float(r['forecast_total_programme']))
plt.rcParams['font.family']='Microsoft YaHei'
fig,ax=plt.subplots(figsize=(11.5,8.4))
fig.patch.set_facecolor('#F4F1EA'); ax.set_facecolor('#F4F1EA')
for i,r in enumerate(rows):
    y=len(rows)-1-i; p=float(r['forecast_total_programme']); lo=float(r['lower80']); hi=float(r['upper80'])
    ax.plot([lo,hi],[y,y],color='#A95D62',lw=5,solid_capstyle='round',alpha=.72,zorder=2)
    ax.plot(p,y,'o',color='#176A7C',markersize=9,zorder=3)
    ax.text(hi+2,y,f'{p:.0f}  [{lo:.0f}, {hi:.0f}]',va='center',fontsize=9.2,color='#18333A')
ax.set_yticks(range(len(rows)),[names.get(r['NOC'],r['NOC']) for r in rows[::-1]],fontsize=11)
ax.set_xlim(0,205);ax.set_xticks(range(0,201,25));ax.set_xlabel('预测奖牌数（枚；官方小项口径的模型估计）',fontsize=11,labelpad=12)
ax.grid(axis='x',color='#D4D9D5',lw=.8);ax.set_axisbelow(True)
for spine in ax.spines.values():spine.set_visible(False)
ax.tick_params(axis='both',length=0,pad=8)
ax.set_title('透明基线：美中区间分离，中游名次仍不确定',loc='left',fontsize=19,fontweight='bold',pad=23,color='#18333A')
fig.text(.12,.155,'● 点估计     ━ 历史回测残差分位数构造的 80% 参考区间',fontsize=10,color='#315A64')
fig.text(.12,.105,'来源：LA2028奖牌预测完整榜.csv；历史 2012、2016、2024 回测残差。区间仅对应透明基线情景，',fontsize=8.8,color='#536A6E')
fig.text(.12,.084,'并非项目级集成模型的独立校准区间；仅 3 届回测，赛后覆盖率待检。俄罗斯资格另设情景。',fontsize=8.8,color='#536A6E')
fig.text(.12,.063,'预测不是已发生的奥运结果；点估计和区间不表示 IOC 授牌。',fontsize=8.8,color='#536A6E')
fig.subplots_adjust(left=.12,right=.9,top=.85,bottom=.24)
fig.savefig(folder/'核心图表/LA2028预测总览.png',dpi=210,facecolor=fig.get_facecolor())
plt.close(fig)
print('updated',folder/'核心图表/LA2028预测总览.png')

# Cover figure: the same annual table, with an explicit thesis and provenance.
cover_folder=ROOT/'交付文件/任务二_百年全景'
annual=list(csv.DictReader((cover_folder/'02_数据表/A_逐届规模与集中度.csv').open(encoding='utf-8-sig',newline='')))
annual=[r for r in annual if int(r['Year'])!=1906]
years=[int(r['Year']) for r in annual];records=[int(r['participation_records']) for r in annual]
fig=plt.figure(figsize=(15.5,8.3),facecolor='#F4F1EA')
ax=fig.add_axes([.07,.27,.58,.53],facecolor='#F4F1EA')
ax.fill_between(years,records,color='#227487',alpha=.12)
ax.plot(years,records,color='#227487',lw=3.2)
ax.set_xlim(1893,2028);ax.set_ylim(0,16500)
ax.set_ylabel('参赛记录（行）');ax.set_xlabel('夏季奥运届次年份')
ax.grid(axis='y',color='#D3DAD7');ax.set_axisbelow(True)
for spine in ax.spines.values():spine.set_visible(False)
ax.tick_params(length=0,pad=7)
ax.text(1897,records[0]+200,'380',fontsize=12,color='#A34057',fontweight='bold')
ax.text(2024,records[-1]+250,'14,892',fontsize=12,color='#227487',fontweight='bold',ha='right')
fig.text(.07,.91,'百年圣火 / 全景总览',fontsize=13,color='#9A6939',fontweight='bold')
fig.text(.07,.85,'参赛记录增 39 倍，前五强份额却近乎减半',fontsize=22,color='#172E35',fontweight='bold')
for i,(value,label,sub,color) in enumerate([
    ('×39.2','参赛规模','380 → 14,892','#227487'),
    ('206','2024代表团','1896年仅12个','#AA7938'),
    ('41.8%','2024前五强份额','1896年为83.9%','#A34057'),
    ('49.1%','女性参赛行占比','女性获奖行占50.3%','#173B49')]):
    y=.71-i*.14
    fig.text(.69,y,value,fontsize=27,fontweight='bold',color=color)
    fig.text(.84,y+.013,label,fontsize=10.5,fontweight='bold',color='#172E35')
    fig.text(.84,y-.023,sub,fontsize=9,color='#4D6166')
fig.text(.07,.15,'规模扩张与份额分散同步出现；性别结构接近，不足以证明项目机会平等。',fontsize=15,color='#17333B',fontweight='bold')
fig.text(.07,.106,'口径：1896—2024夏奥运动员记录行；前五份额按获奖行计算；1906排除。',fontsize=9.5,color='#445B60')
fig.text(.07,.077,'来源：任务一归一数据、任务二 A_逐届规模与集中度.csv。2024小项数量另据官方329项表；本图不以行数称官方奖牌。',fontsize=9.5,color='#445B60')
fig.savefig(cover_folder/'04_核心图表/00_封面总览英雄图.png',dpi=210,facecolor=fig.get_facecolor())
plt.close(fig)
print('updated',cover_folder/'04_核心图表/00_封面总览英雄图.png')
