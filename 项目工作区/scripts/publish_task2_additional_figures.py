from pathlib import Path
import csv
from html import escape
import re

TASK = Path(__file__).resolve().parents[2] / '交付文件/任务二_百年全景'
FIG = TASK / '04_核心图表'
PAPER, INK, GRID = '#fbfaf6', '#193039', '#d8dfdf'
TEAL, GOLD, RED = '#247487', '#966825', '#A64155'

# Code, title, figure name, scope, observation, reading, evidence limit.
CASES = (
    ('A','获奖队伍更多，奖牌记录却更集中','A_两届获奖覆盖与集中度.png',
     '仅 2016、2024，排除 1906。奖牌按获奖运动员记录行；有效队数为各队份额平方和的倒数。',
     '里约到巴黎，获奖代表团由 86 个增至 92 个，但前五代表团的记录份额也由 39.3% 升至 41.8%。同一时期，有效获奖代表团数从 21.1 降至 18.9。',
     '三组对照使用各自单位，读数应在同一组内比较。获奖队数每队计一次，前五份额关注头部，有效队数则以全场份额分布为基础，对大份额代表团更敏感。',
     '三项合读能区分获奖覆盖和分布均匀度。这个反例只对应里约与巴黎，不能用两个端点判定百年趋势已经逆转。团体奖牌在运动员行口径下仍可能对应多条记录。'),
    ('B','美国的记录增长与份额变化有时反向','B_美国逐届变化象限.png',
     '1992—2024 相邻夏奥届次，排除 1906。横轴为获奖运动员行变化，纵轴为同届份额变化。',
     '每个点代表美国从上一届到所标届次的变化。多数点落在两个同向象限，说明记录数与份额常常一起升降；里约到东京落在右下，表示获奖记录增加而份额减少。',
     '右下角案例增加 34 条获奖记录，份额却下降约 0.88 个百分点。同期全场总量从 2,023 行增至 2,449 行，增长比美国更快。横轴看绝对规模，纵轴看相对位置。',
     '这张图只观察美国及给定的现代时间窗口。其他代表团的缺席和零获奖应分开处理；本图中的记录数也不能直接读成官方小项奖牌数。'),
    ('C','头部正负运动贡献如何抵消','C_巴黎女性运动贡献对照.png',
     '仅巴黎 2024，1906 不在图示范围。以运动员参赛和获奖记录行为单位，贡献单位为百分点。',
     '巴黎 2024 女性获奖记录占比比参赛记录占比高约 1.185 个百分点。图中分开列出正、负贡献各前三项，再把其他运动合并，使所有条形仍能加回整体差值。',
     '赛艇、足球和篮球提供较大的正贡献，田径、体操和射击提供较大的负贡献。单个运动的绝对贡献可以超过总差值，因为全场指标由各运动正负项相加。',
     '这些贡献反映运动组合及队伍记录结构。团体人数会影响记录层面的分母，不能由此估计个人获奖概率或制度公平性。各运动的精确数值和结构分解可下载复算。'),
    ('D','净减两类背后有十四类更替','D_1900至1904运动更替瀑布.png',
     '仅 1900 与 1904 两届，排除 1906。单位为在赛题数据中有参赛记录的归一运动大类。',
     '1900 到 1904 年，运动大类总数从 20 降至 18。把两届名单逐一对照，可以看见总量背后有 4 类首次出现、2 类重返，以及 8 类在后一届没有记录。',
     '瀑布图以 20 类为起点，先加上首次出现与重返，随后扣掉后一届无记录的运动。14 类更替是三项变动的绝对数量之和，净变化则只有 -2 类。',
     '未再出现以这对相邻已收录届次为限。运动大类是清洗后记录的分类单位，不能等同于官方小项，也不能把一期缺席解释为永久取消。'),
)

def rows(relative):
    with (TASK / relative).open(encoding='utf-8-sig',newline='') as file:
        return list(csv.DictReader(file))

def draw():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.ticker import FuncFormatter

    plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':12,'axes.unicode_minus':False,
                         'axes.spines.top':False,'axes.spines.right':False,
                         'figure.facecolor':PAPER,'axes.facecolor':PAPER,'text.color':INK,
                         'axes.labelcolor':INK,'xtick.color':INK,'ytick.color':INK})

    def save(fig,index):
        code,title,name,scope,*_ = CASES[index]
        fig.text(.065,.94,title,fontsize=20,weight='bold')
        fig.text(.065,.045,scope,fontsize=10)
        fig.savefig(FIG/name,dpi=220)
        plt.close(fig)

    source = {r['Year']:r for r in rows('07_结论压力测试/逐届集中度三口径.csv') if r['unit']=='运动员获奖行'}
    fig, axes = plt.subplots(1,3,figsize=(10,4.9))
    fig.subplots_adjust(left=.07,right=.96,bottom=.21,top=.76,wspace=.24)
    for ax,(label,key,factor,unit,fmt,color) in zip(axes,(
        ('获奖代表团数','medal_nocs',1,'','.0f',TEAL),
        ('前五代表团份额','top5_share',100,'%','.1f',GOLD),
        ('有效获奖代表团数','effective_nocs',1,'','.1f',RED),
    )):
        values=[float(source[year][key])*factor for year in ('2016','2024')]
        ax.bar([0,1],values,width=.55,color=['#8ca2a4',color])
        ax.set_title(label,fontsize=13)
        ax.set_xticks([0,1],['2016','2024'])
        ax.set_ylim(0,max(values)*1.21)
        ax.set_yticks([])
        ax.spines['left'].set_visible(False)
        for x,value in enumerate(values):
            ax.text(x,value+max(values)*.035,f'{value:{fmt}}{unit}',ha='center',weight='bold')
    save(fig,0)

    team = {int(r['Year']):r for r in rows('02_数据表/B_十二代表团逐届份额.csv') if r['NOC']=='USA' and int(r['Year'])>=1992}
    editions = sorted(team)
    changes=[(year,int(float(team[year]['medal_records'])-float(team[prior]['medal_records'])),
              100*(float(team[year]['medal_share'])-float(team[prior]['medal_share']))) for prior,year in zip(editions,editions[1:])]
    fig,ax=plt.subplots(figsize=(10,5.6))
    fig.subplots_adjust(left=.16,right=.93,bottom=.23,top=.82)
    ax.axhline(0,color=GRID); ax.axvline(0,color=GRID)
    for year,x,y in changes:
        color=RED if x*y<0 else TEAL
        ax.scatter(x,y,color=color,s=48,zorder=3)
        offset=(-7,-11) if year in (2000,2008) else (7,5)
        ax.annotate(str(year),(x,y),xytext=offset,textcoords='offset points',fontsize=10,color=color)
    ax.margins(x=.18,y=.21)
    ax.set_xlabel('相对上一届的美国获奖记录变化（条）')
    ax.set_ylabel('同届份额变化（百分点）')
    save(fig,1)

    source=rows('08_女性结构分解/2024女性占比分解逐项目.csv')
    values=sorted([(r['运动大类中文'],float(r['合计贡献_百分点'])) for r in source],key=lambda v:v[1],reverse=True)
    show=values[:3]+[('其余运动合计',sum(v for _,v in values[3:-3]))]+values[-3:]
    assert abs(sum(v for _,v in show)-sum(v for _,v in values))<1e-10
    fig,ax=plt.subplots(figsize=(10,5.6))
    fig.subplots_adjust(left=.22,right=.94,bottom=.23,top=.81)
    ax.axvline(0,color=GRID)
    for i,(label,value) in enumerate(show):
        color=TEAL if value>=0 else RED
        ax.barh(i,value,color=color,height=.58)
        ax.text(value+(.09 if value>=0 else -.09),i,f'{value:+.2f}',va='center',ha='left' if value>=0 else 'right',color=color)
    ax.set_yticks(range(len(show)),[label for label,_ in show]); ax.invert_yaxis()
    ax.set_xlim(min(v for _,v in show)-.55,max(v for _,v in show)+.55)
    ax.set_xlabel(f"对总体差值的贡献（百分点）｜未四舍五入的各项合计 {sum(v for _,v in show):+.3f}")
    save(fig,2)

    life={r['Year']:r for r in rows('02_数据表/D_项目新增退出重返.csv')}
    old,new=life['1900'],life['1904']
    start=sum(int(old[key]) for key in ('新增','重返','连续保留'))
    steps=[int(new['新增']),int(new['重返']),-int(old['本届后退出'])]
    end=sum(int(new[key]) for key in ('新增','重返','连续保留'))
    assert start+sum(steps)==end
    fig,ax=plt.subplots(figsize=(10,5.2))
    fig.subplots_adjust(left=.13,right=.94,bottom=.2,top=.77)
    running=start
    ax.bar(0,start,color=TEAL,width=.62)
    ax.text(0,start+.35,str(start),ha='center',weight='bold')
    for i,n in enumerate(steps,1):
        following=running+n
        ax.plot([i-1+.31,i-.31],[running,running],color='#91a3a5',linestyle='--')
        ax.bar(i,abs(n),bottom=min(running,following),color=GOLD if n>0 else RED,width=.62)
        ax.text(i,max(running,following)+.35,f'{n:+d}',ha='center',weight='bold')
        running=following
    ax.plot([3.31,3.69],[end,end],color='#91a3a5',linestyle='--')
    ax.bar(4,end,color=TEAL,width=.62)
    ax.text(4,end+.35,str(end),ha='center',weight='bold')
    ax.set_xticks(range(5),['1900','首次出现','重返','未再出现','1904'])
    ax.set_ylabel('运动大类（类）')
    ax.set_ylim(0,30)
    save(fig,3)

def update_reading():
    folder = TASK / '11_四视角独立交付'
    web = folder / '四视角核心图复核.html'
    html = web.read_text(encoding='utf-8')
    for code,title,name,scope,observation,reading,limit in CASES:
        path, = folder.glob(f'{code}_*.md')
        url = f'../04_核心图表/{name}'
        start,end = f'<!-- core-case-{code}:start -->',f'<!-- core-case-{code}:end -->'
        pattern = re.escape(start)+r'.*?'+re.escape(end)+r'\n?'
        prose = '\n\n'.join((observation,reading,limit))
        assert len(re.findall(r'[一-龥]',prose)) >= 100
        text = re.sub(pattern,'',path.read_text(encoding='utf-8'),flags=re.S).rstrip()
        text += f'\n\n{start}\n## {title}\n\n![{title}]({url})\n\n{prose}\n\n**口径。** {scope}\n{end}\n'
        path.write_text(text,encoding='utf-8',newline='\n')
        html = re.sub(pattern,'',html,flags=re.S)
        position = html.index('</section>',html.index(f'id="view-{code}"'))
        fragment = (
            f'{start}\n<h3>{escape(title)}</h3>\n<figure class="additional-core-chart">'
            f'<a href="{url}"><img src="{url}" alt="{escape(title)}" loading="lazy"></a>'
            f'<figcaption>{escape(scope)}</figcaption></figure>\n'
            + ''.join(f'<p>{escape(part)}</p>\n' for part in (observation,reading,limit))
            + end+'\n'
        )
        html = html[:position]+fragment+html[position:]
    web.write_text(html,encoding='utf-8',newline='\n')


if __name__ == '__main__':
    draw()
    update_reading()
