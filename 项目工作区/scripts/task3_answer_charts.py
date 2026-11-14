from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / '交付文件/任务三_专题深挖'
OUT = ROOT / '交付文件/最终提交材料/答卷附图'
OUT.mkdir(parents=True, exist_ok=True)
font = next((x for x in ['Microsoft YaHei','SimHei','Noto Sans CJK SC'] if x in {f.name for f in font_manager.fontManager.ttflist}), 'DejaVu Sans')
plt.rcParams.update({'font.family':font,'axes.unicode_minus':False,'font.size':11,'axes.edgecolor':'#aebfbe','text.color':'#163b43','axes.labelcolor':'#163b43','xtick.color':'#53696d','ytick.color':'#53696d','figure.facecolor':'#f8f7f2','axes.facecolor':'#f8f7f2'})

specs = [
 ('S3_地缘政治的投影','S3_代表团覆盖变化','1980与1984：参赛代表团覆盖的变化','bar'),
 ('S4_小代表团的大突破','S4_小代表团获奖记录','小代表团：总量背后有不同项目路径','barh'),
 ('S5_奖牌的通货膨胀','S5_逐届获奖记录','绝对奖牌记录持续扩张','line'),
 ('S6_王者与传奇','S6_姓名候选记录','原始姓名候选：先核验，再谈个人排名','barh'),
 ('S8_她们登上领奖台','S8_女性获奖记录占比','女性获奖记录的百年弧线','line'),
 ('S9_消失的赛场','S9_历史项目出现届数','曾经的赛场：出现届数不同','barh'),
 ('S10_奖牌藏在哪些项目','S10_体育大类获奖记录','哪些运动家族积累了更多获奖记录','barh'),
]

for folder,name,title,kind in specs:
    rows=json.loads((SRC/folder/'分析数据.json').read_text(encoding='utf-8'))
    if kind=='line':
        x=[int(r['label']) for r in rows]; y=[float(r['value']) for r in rows]
        fig,ax=plt.subplots(figsize=(9.5,4.3));ax.plot(x,y,color='#168a91',lw=2.6,marker='o',ms=3)
        ax.fill_between(x,y,alpha=.13,color='#168a91')
        ax.set_xlim(min(x),max(x));ax.grid(axis='y',color='#d6e1dc')
        ax.set_ylabel('获奖运动员记录占比（%）' if 'S8' in name else '获奖运动员记录（条）')
        for xx,yy in [(x[0],y[0]),(x[-1],y[-1])]:ax.annotate(f'{yy:.1f}%' if 'S8' in name else f'{yy:,.0f}',(xx,yy),xytext=(0,9),textcoords='offset points',ha='center',fontweight='bold')
    elif kind=='bar':
        x=[str(r['label']) for r in rows];y=[float(r['value']) for r in rows]
        fig,ax=plt.subplots(figsize=(9.5,4.3));bars=ax.bar(x,y,color=['#c89b59' if z in ('1980','1984') else '#168a91' for z in x],width=.68)
        ax.grid(axis='y',color='#d6e1dc');ax.set_axisbelow(True);ax.bar_label(bars,padding=3,fontsize=9)
        ax.set_ylabel('有记录的代表团（个）')
    else:
        rows=rows[:12]
        labels=[str(r['label']) for r in rows][::-1]; vals=[float(r['value']) for r in rows][::-1]
        fig,ax=plt.subplots(figsize=(9.5,max(4.3,len(rows)*.38)))
        bars=ax.barh(labels,vals,color=['#c89b59' if i>=len(rows)-3 else '#168a91' for i in range(len(rows))],height=.65)
        ax.grid(axis='x',color='#d6e1dc');ax.set_axisbelow(True);ax.bar_label(bars,padding=4,fontsize=9)
        ax.set_xlabel('运动员获奖记录（条）' if 'S4' in name or 'S10' in name or 'S6' in name else '出现届数')
        ax.spines[['top','right']].set_visible(False)
    ax.set_title(title,loc='left',fontsize=17,fontweight='bold',pad=18)
    ax.spines[['top','right']].set_visible(False)
    fig.tight_layout(pad=1.4)
    fig.savefig(OUT/(name+'.png'),dpi=180,bbox_inches='tight')
    plt.close(fig)
    print(name)
