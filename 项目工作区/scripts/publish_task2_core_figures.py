"""Regenerate eight Task 2 figures from the published data tables."""
from pathlib import Path
from html import escape
import re

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, ListedColormap
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import numpy as np
import pandas as pd

from task2_localization import NOC_ZH, SPORT_ZH

ROOT = Path(__file__).resolve().parents[2] / '交付文件'
TASK = ROOT / '任务二_百年全景'
TABLE = TASK / '02_数据表'
FIG = TASK / '04_核心图表'
PAPER, INK, GRID = '#fbfaf6', '#193039', '#d8dfdf'
BLUE, RED, GOLD = '#196478', '#9f3953', '#8a5c18'
YEARS = [1896,1920,1948,1972,2000,2024]
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':11,
    'figure.facecolor':PAPER,'axes.facecolor':PAPER,'text.color':INK,
    'axes.labelcolor':INK,'xtick.color':INK,'ytick.color':INK,
    'axes.spines.top':False,'axes.spines.right':False,'axes.unicode_minus':False})

def csv(name,index=False):
    return pd.read_csv(TABLE/name,index_col=0 if index else None)

def figure(title,note,height=5.4,left=.14,right=.94,bottom=.16,top=.82,grid=(1,1),sharex=False,sharey=False):
    fig,ax=plt.subplots(*grid,figsize=(10,height),sharex=sharex,sharey=sharey)
    fig.subplots_adjust(left=left,right=right,bottom=bottom,top=top,hspace=.46,wspace=.20)
    fig.text(.065,.96,title,ha='left',va='top',fontsize=21,weight='bold')
    fig.text(.065,.038,note,ha='left',va='bottom',fontsize=10)
    return fig,ax

def save(fig,name):
    fig.savefig(FIG/f'{name}.png',dpi=220,facecolor=PAPER)
    plt.close(fig)

def grid(ax,axis='y'):
    ax.set_axisbelow(True)
    ax.grid(axis=axis,color=GRID,lw=.7)

def timeline(ax):
    ax.set_xlim(1894,2028)
    ax.set_xticks(YEARS)
    ax.set_xlabel('奥运届次年份')

a=csv('A_逐届规模与集中度.csv',True)
fig,(total,share)=figure('奖牌记录增加，前五代表团份额下降',
    f"参赛记录：{a.loc[1896,'participation_records']:,} → {a.loc[2024,'participation_records']:,} 行。排除 1906；团体获奖成员各计一行。",6.7,grid=(2,1),sharex=True)
total.plot(a.index,a.medal_records,color=BLUE,lw=2.4)
total.set_ylabel('获奖记录数（行）')
total.annotate(f"{a.loc[2024,'medal_records']:,.0f} 行",(2024,a.loc[2024,'medal_records']),xytext=(-12,17),textcoords='offset points',ha='right',weight='bold',arrowprops={'arrowstyle':'-','color':BLUE})
share.plot(a.index,a.top5_share*100,color=RED,lw=2.4)
share.set_ylabel('前五代表团份额（%）')
share.set_ylim(30,100)
for year,offset,align in [(1896,(5,8),'left'),(2024,(-4,-17),'right')]:
    share.annotate(f'{a.loc[year,"top5_share"]:.1%}',(year,a.loc[year,'top5_share']*100),
                   xytext=offset,textcoords='offset points',ha=align,color=RED,weight='bold')
for ax in (total,share): grid(ax)
timeline(share)
save(fig,'A_规模扩张与奖牌集中度')

raw=ROOT/'任务一_数据体检/02_交付数据/归一数据_保留原始字段.csv.gz'
medals=pd.read_csv(raw,usecols=['include_main','is_medal','NOC'])
cumulative=medals.loc[medals.include_main & medals.is_medal,'NOC'].value_counts().head(15).sort_values()
fig,ax=figure('历届累计获奖记录最多的 15 个代表团',
    '数据：任务一归一记录，排除 1906。历史代表团代码独立统计。',6.6,left=.21)
bars=ax.barh([NOC_ZH.get(n,n) for n in cumulative.index],cumulative,color=BLUE)
ax.bar_label(bars,labels=[f'{n:,}' for n in cumulative],padding=5,fontsize=10)
ax.set_xlim(0,cumulative.max()*1.22); ax.set_xlabel('累计获奖运动员记录（行）')
grid(ax,'x')
save(fig,'A_历史累计奖牌记录榜')

b=csv('B_十二代表团逐届份额.csv')
assert b.loc[~b.present,'medal_share'].isna().all()
order=b.NOC.unique().tolist()
bmatrix=b.pivot(index='NOC',columns='Year',values='medal_share').reindex(order)*100
fig,axes=figure('缺席与历史身份变化会让份额曲线断开',
    '缺席留空；参赛零获奖用空心圆标于零线。三角表示超出 35%，数字为实际值。',8,left=.10,right=.95,bottom=.12,top=.80,grid=(4,3),sharex=True,sharey=True)
fig.text(.065,.865,'同届获奖记录份额（%）   ｜   浅金区域：1980、1984 抵制届次',fontsize=11)
for axis,(noc,row) in zip(axes.flat,bmatrix.iterrows()):
    axis.axvspan(1979,1985,color='#efdfb4',zorder=0)
    axis.plot(row.index,row,color=BLUE,lw=1.6,marker='.',ms=4)
    zero=row[row.eq(0)]
    axis.scatter(zero.index,zero,s=15,facecolors=PAPER,edgecolors=INK,zorder=4,clip_on=False)
    for year,value in row[row.gt(35)].items():
        axis.scatter(year,34,marker='^',s=22,color=RED,zorder=5)
        axis.annotate(f'{value:.0f}%',(year,34),xytext=(3,-4),textcoords='offset points',ha='left',va='top',fontsize=9,color=RED)
    axis.set_title(f'{NOC_ZH.get(noc,noc)} · {noc}',loc='left',fontsize=11)
    axis.set_ylim(0,36); axis.set_yticks([0,15,30]); axis.set_xlim(1894,2028)
    axis.set_xticks([1896,1948,1984,2024])
    grid(axis)
save(fig,'B_十二代表团兴衰曲线')

fig,ax=figure('奖牌记录份额在不同代表团之间接续',
    '浅金边框：1980、1984；独立保留 URS、GDR、FRG、GER。超过 35% 的色阶饱和。',5.9,left=.22,right=.90,bottom=.20)
cmap=LinearSegmentedColormap.from_list('share',['#ffffff','#82b8c1',BLUE,'#162f45'])
cmap.set_bad('#d0d5d8')
im=ax.imshow(bmatrix,aspect='auto',interpolation='nearest',cmap=cmap,vmin=0,vmax=35)
for index,year in enumerate(bmatrix.columns):
    if year in (1980,1984):
        ax.axvspan(index-.5,index+.5,fill=False,edgecolor=GOLD,lw=1.4)
ax.set_yticks(range(len(order)),[f'{NOC_ZH.get(n,n)} {n}' for n in order])
ix=[i for i,y in enumerate(bmatrix.columns) if y in YEARS or y in (1980,1984)]
ax.set_xticks(ix,[bmatrix.columns[i] for i in ix],rotation=55,ha='right')
fig.colorbar(im,ax=ax,pad=.025,label='同届获奖记录份额（%）')
ax.legend(handles=[Patch(facecolor='#d0d5d8',label='缺席'),Patch(facecolor='white',edgecolor=GRID,label='参赛但零获奖')],
          frameon=False,ncol=2,loc='lower left',bbox_to_anchor=(0,1))
save(fig,'B_强国时代热力图')

f=csv('C_女性参与获奖与小项.csv',True)
metrics=[('participation_share','女性参赛记录',BLUE,'-','o',a.loc[2024,'participation_records']),
         ('medal_share','女性获奖记录',RED,'--','s',a.loc[2024,'medal_records']),
         ('women_only_event_share','女子专属小项',GOLD,':','D',f.loc[2024,'event_units'])]
fig,ax=figure('巴黎 2024：三个分母，三种女性占比',
    '记录按运动员行；历史小项为 Event 代理。2020 小项缺值；2024 来自官方结构表。',6.2,right=.68,top=.79)
for i,(column,label,color,ls,marker,total) in enumerate(metrics):
    values=f[column]*100
    ax.plot(values.index,values,color=color,ls=ls,lw=2.3)
    value=f.loc[2024,column]
    ax.scatter(2024,value*100,color=color,marker=marker,s=49,zorder=4)
    count=round(value*total)
    assert np.isclose(count/total,value)
    y=.71-i*.18
    fig.text(.72,y,label,fontsize=11,color=color,weight='bold')
    fig.text(.72,y-.060,f'{value:.1%}',fontsize=20,color=color,weight='bold')
    fig.text(.72,y-.102,f'{count:,} / {int(total):,}',fontsize=11)
ax.legend(handles=[Line2D([0],[0],color=c,ls=ls,marker=m,label=l) for _,l,c,ls,m,_ in metrics],
          frameon=False,ncol=2,loc='upper left')
ax.set_ylabel('占比（%）'); ax.set_ylim(0,65)
ax.axhline(50,color=GRID,lw=.9)
grid(ax); timeline(ax)
save(fig,'C_女性三层平权曲线')

c=csv('C_2024代表团女性结构.csv',True).nlargest(15,'records').sort_values('gap_pp')
fig,ax=figure('同一代表团的女性参赛与获奖占比可以相差很大',
    '巴黎 2024 参赛行最多的 15 队。差值为获奖占比减参赛占比，单位为百分点。',6.65,left=.20,right=.86)
y=np.arange(len(c))
x=c.female_participation_share*100; z=c.female_medal_share*100
ax.hlines(y,x,z,color='#a2adb1',lw=2)
ax.scatter(x,y,c=BLUE,s=42,marker='o',label='女性参赛行占比')
ax.scatter(z,y,c=RED,s=43,marker='s',label='女性获奖行占比')
extremes=set(c.gap_pp.abs().nlargest(3).index)
for index,(noc,value) in enumerate(c.gap_pp.items()):
    if noc in extremes:
        ax.text(103,index,f'{value:+.1f}',va='center',fontsize=11,weight='bold',color=RED if value<0 else BLUE)
ax.axvline(50,color=GRID,ls='--')
ax.set_yticks(y,[NOC_ZH.get(n,n) for n in c.index])
ax.set_xlim(0,100); ax.set_xlabel('占本代表团同类记录的比例（%）')
ax.legend(frameon=False,ncol=2,loc='lower left',bbox_to_anchor=(0,1))
grid(ax,'x')
save(fig,'C_2024代表团女性结构差')

d=csv('D_逐届小项数量.csv',True)
presence=csv('D_代表项目出现矩阵.csv',True)
fig,(ax,matrix)=figure('小项持续扩容，运动大类仍有进出',
    '历史小项按 Event 去重；2020 字段泛化。下图按运动大类，有参赛记录即着色。',7.5,left=.23,right=.95,bottom=.17,grid=(2,1))
ax.plot(d.loc[:2016].index,d.loc[:2016,'event_units'],color=BLUE,lw=2.3)
ax.scatter(2024,d.loc[2024,'event_units'],marker='D',color=RED,s=55,zorder=4)
ax.axvline(2020,color=GOLD,ls=':',lw=1.2)
ax.set_ylim(0,410); ax.set_xlim(1896,2030); ax.set_xticks([1896,1948,1984,2016,2024])
ax.annotate('2020\n小项留空',xy=(2020,145),xytext=(1997,130),arrowprops={'arrowstyle':'-','color':GOLD},color=GOLD,ha='center')
ax.annotate(f"2024 官方 {d.loc[2024,'event_units']:.0f} 项",xy=(2024,d.loc[2024,'event_units']),xytext=(-9,12),textcoords='offset points',ha='right',color=RED)
ax.set_ylabel('小项数'); grid(ax)
matrix.imshow(presence,aspect='auto',interpolation='nearest',cmap=ListedColormap(['#e9eceb',BLUE]),vmin=0,vmax=1)
matrix.set_yticks(range(len(presence)),[SPORT_ZH.get(k,k) for k in presence.index],fontsize=8.5)
t=[i for i,k in enumerate(presence.columns) if int(k) in YEARS]
matrix.set_xticks(t,[presence.columns[i] for i in t]); matrix.set_xlabel('奥运届次年份')
matrix.legend(handles=[Patch(color=BLUE,label='观察到'),Patch(color='#e9eceb',label='未观察到')],frameon=False,ncol=2,loc='lower left',bbox_to_anchor=(0,1))
save(fig,'D_小项增长与项目更替')

life=csv('D_项目新增退出重返.csv',True)
fig,(mix,exit_ax)=figure('运动大类既有新增，也有退出和重返',
    '退出指下一届未观察到。2024 是资料末届，退出状态留空。2020 沿用 Sport 大类。',6.8,grid=(2,1),sharex=True)
mix.stackplot(life.index,life['连续保留'],life['新增'],life['重返'],labels=['连续保留','首次出现','重返'],colors=[BLUE,'#d6a04e','#97718e'])
mix.legend(frameon=False,ncol=3,loc='upper left')
mix.set_ylabel('当届运动大类数')
exit_ax.bar(life.index[:-1],life['本届后退出'].iloc[:-1],width=2.6,color=RED)
exit_ax.annotate('资料末届\n退出待观察',(2024,0),xytext=(-3,24),textcoords='offset points',ha='right',color=GOLD)
exit_ax.set_ylabel('本届后退出的运动大类数')
for ax in (mix,exit_ax): grid(ax)
timeline(exit_ax)
save(fig,'D_项目新增退出重返流向')


# Keep direct access to native resolution on narrow screens and in offline review.
review=TASK/'11_四视角独立交付/四视角核心图复核.html'
html=review.read_text(encoding='utf-8')
html=re.sub(r'<a class="core-chart-zoom"[^>]*>(<img [^>]+/>)</a>',r'\1',html)
def enlarge(match):
    src,alt=re.search(r'src="([^"]+)"',match[1])[1],re.search(r'alt="([^"]+)"',match[1])[1]
    return f'<figure><a class="core-chart-zoom" aria-label="打开原图：{escape(alt)}" href="{src}">{match[1]}</a>'
html,count=re.subn(r'<figure>(<img [^>]+/>)',enlarge,html)
assert count==8
review.write_text(html,encoding='utf-8')
