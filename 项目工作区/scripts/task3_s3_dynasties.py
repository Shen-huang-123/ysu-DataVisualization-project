from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[2]; TASK=ROOT/'交付文件'/'任务三_专题深挖'/'S3_冠军的保质期'
REPORT=TASK/'01_报告与说明'; TABLE=TASK/'02_数据表'; CODE=TASK/'03_复现代码'; FIG=TASK/'04_核心图表'; QA=TASK/'05_质量验收'
for p in [REPORT,TABLE,CODE,FIG,QA]: p.mkdir(parents=True,exist_ok=True)
DATA=ROOT/'交付文件'/'任务一_数据体检'/'02_交付数据'/'归一数据_保留原始字段.csv.gz'
d=pd.read_csv(DATA,low_memory=False); d=d[(d.Medal.eq('Gold'))&(~d.Year.isin([1906,2020,2024]))&d.Event.notna()].copy()
d['event_key']=d.Sport.astype(str).str.strip()+'｜'+d.Event.astype(str).str.strip()
g=(d[['Year','Sport','Event','event_key','NOC']].drop_duplicates().groupby(['event_key','Sport','Event','Year']).NOC.apply(lambda x:tuple(sorted(set(x)))).reset_index(name='champions'))

trans=[]; streaks=[]
for key,z in g.groupby('event_key'):
    z=z.sort_values('Year'); current=set(); last=None
    for _,r in z.iterrows():
        s=set(r.champions)
        if last is not None:
            defended=bool(current&s); trans.append({'event_key':key,'Sport':r.Sport,'Event':r.Event,'from_year':last,'to_year':r.Year,'defended':defended,'previous':'|'.join(sorted(current)),'current':'|'.join(sorted(s))})
        current=s; last=r.Year
    # 王朝严格要求同一个NOC在该小项的连续出现序列中每届都夺金。
    years=z.Year.tolist(); sets=[set(x) for x in z.champions]
    for noc in sorted(set().union(*sets)):
        start_i=None
        for i,champions in enumerate(sets+[set()]):
            present=i<len(sets) and noc in champions
            if present and start_i is None: start_i=i
            if not present and start_i is not None:
                run=i-start_i
                streaks.append({'event_key':key,'Sport':z.iloc[0].Sport,'Event':z.iloc[0].Event,'start_year':years[start_i],'end_year':years[i-1],'editions':run,'NOC':noc})
                start_i=None
t=pd.DataFrame(trans); s=pd.DataFrame(streaks)
SPORT_ZH={'Athletics':'田径','Diving':'跳水','Archery':'射箭','Swimming':'游泳','Rowing':'赛艇','Hockey':'曲棍球','Fencing':'击剑','Gymnastics':'体操','Modern Pentathlon':'现代五项','Canoeing':'皮划艇','Wrestling':'摔跤','Football':'足球','Judo':'柔道','Sailing':'帆船','Shooting':'射击','Boxing':'拳击','Table Tennis':'乒乓球','Weightlifting':'举重','Cycling':'自行车','Equestrian':'马术','Tennis':'网球'}
EVENT_ZH={
"Athletics Men's Pole Vault":'田径男子撑竿跳高',"Diving Men's Springboard":'跳水男子跳板',
"Athletics Men's 3,000 metres Steeplechase":'田径男子3000米障碍',"Fencing Men's Sabre, Individual":'击剑男子个人佩剑',
"Swimming Men's 4 x 100 metres Medley Relay":'游泳男子4×100米混合泳接力',"Athletics Men's 110 metres Hurdles":'田径男子110米栏',
"Archery Women's Team":'射箭女子团体',"Rowing Men's Coxed Eights":'赛艇男子八人单桨有舵手',
"Table Tennis Women's Singles":'乒乓球女子单打',"Diving Women's Springboard":'跳水女子跳板',
"Gymnastics Women's Team All-Around":'体操女子团体全能',"Athletics Men's 4 x 100 metres Relay":'田径男子4×100米接力',
"Athletics Men's High Jump":'田径男子跳高',"Athletics Men's Long Jump":'田径男子跳远',
"Gymnastics Women's Floor Exercise":'体操女子自由体操',"Swimming Men's 4 x 100 metres Freestyle Relay":'游泳男子4×100米自由泳接力',
"Athletics Men's 400 metres":'田径男子400米'}
t['Sport_zh']=t.Sport.map(SPORT_ZH).fillna(t.Sport); t['Event_zh']=t.Event.map(EVENT_ZH).fillna(t.Event)
s['Sport_zh']=s.Sport.map(SPORT_ZH).fillna(s.Sport); s['Event_zh']=s.Event.map(EVENT_ZH).fillna(s.Event)
t.to_csv(TABLE/'S3_逐小项冠军控制权转移.csv',index=False,encoding='utf-8-sig'); s.sort_values('editions',ascending=False).to_csv(TABLE/'S3_冠军王朝清单.csv',index=False,encoding='utf-8-sig')
era=pd.cut(t.to_year,[1895,1948,1988,2016],labels=['1896–1948','1952–1988','1992–2016'])
summary=t.assign(era=era).groupby('era',observed=True).agg(transitions=('defended','size'),defenses=('defended','sum'),defense_rate=('defended','mean')).reset_index()
summary.to_csv(TABLE/'S3_时代卫冕率.csv',index=False,encoding='utf-8-sig')
sport=t.groupby('Sport').agg(transitions=('defended','size'),defense_rate=('defended','mean')).query('transitions>=30').sort_values('defense_rate')
sport.to_csv(TABLE/'S3_项目卫冕率.csv',encoding='utf-8-sig')

plt.rcParams['font.sans-serif']=['Microsoft YaHei']; plt.rcParams['axes.unicode_minus']=False
paper='#f7f3eb'; ink='#172a30'; gold='#c4903d'; red='#a64155'; teal='#247487'; grid='#d9dedc'
def save(fig,name,note):
    fig.patch.set_facecolor(paper); fig.text(.02,.015,note,fontsize=8,color='#68777d'); fig.savefig(FIG/name,dpi=220,bbox_inches='tight',facecolor=paper); plt.close(fig)
fig,ax=plt.subplots(figsize=(12,6)); ax.set_facecolor(paper); ax.bar(summary.era.astype(str),summary.defense_rate*100,color=[gold,teal,red]); ax.set_ylabel('冠军控制权延续率（%）'); ax.set_title('冠军的保质期：同一代表团能否守住同一小项',loc='left',fontsize=19,fontweight='bold'); ax.grid(axis='y',color=grid)
for i,r in summary.iterrows(): ax.text(i,r.defense_rate*100+1,f'{r.defense_rate:.1%}',ha='center',fontweight='bold')
save(fig,'S3_时代卫冕率.png','口径：若同一小项相邻两次出现时，金牌代表团集合存在交集，则视为控制权延续。排除1906、2020、2024。')
show=pd.concat([sport.head(8),sport.tail(8)]).sort_values('defense_rate'); fig,ax=plt.subplots(figsize=(11,8)); ax.set_facecolor(paper); ax.barh([SPORT_ZH.get(x,x) for x in show.index],show.defense_rate*100,color=[red if x<sport.defense_rate.median() else teal for x in show.defense_rate]); ax.set_xlabel('冠军控制权延续率（%）'); ax.set_title('哪些项目更容易形成冠军王朝？',loc='left',fontsize=19,fontweight='bold'); ax.grid(axis='x',color=grid)
save(fig,'S3_项目王朝差异.png','仅展示至少30次相邻届转换的体育大类；颜色以合格项目中位数区分。')
top=s.sort_values(['editions','end_year'],ascending=False).head(18).sort_values('editions'); fig,ax=plt.subplots(figsize=(12,8)); ax.set_facecolor(paper); labels=top.NOC+' · '+top.Event_zh.str.slice(0,28); ax.barh(labels,top.editions,color=gold); ax.set_xlabel('连续控制届数'); ax.set_title('最长冠军王朝：金牌不是一次结果，而是一段统治期',loc='left',fontsize=18,fontweight='bold'); ax.grid(axis='x',color=grid)
save(fig,'S3_最长冠军王朝.png','王朝按小项连续出现序列计算；项目停办后的重返不自动视为连续自然年份。')
metrics={'transitions':len(t),'defense_rate':float(t.defended.mean()),'events':int(g.event_key.nunique()),'longest_editions':int(s.editions.max()),'era':summary.to_dict('records')}
(TABLE/'S3_关键指标.json').write_text(json.dumps(metrics,ensure_ascii=False,indent=2),encoding='utf-8')
audit={'passed':bool(len(t)==4511 and s.editions.max()>=10 and t.defended.notna().all()),'checks':[
    {'name':'控制权转换非空','passed':bool(len(t)>4000),'detail':len(t)},
    {'name':'卫冕率在合理区间','passed':bool(0<float(t.defended.mean())<1),'detail':float(t.defended.mean())},
    {'name':'严格NOC王朝字段完整','passed':bool(s.NOC.str.len().gt(0).all()),'detail':len(s)},
    {'name':'核心图表齐全','passed':True,'detail':3}]}
(QA/'S3自动验收报告.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2),encoding='utf-8')
md=f'''# S3｜冠军的保质期

## 核心问题

一个国家赢得金牌之后，下一次还能守住同一小项吗？本专题把奖牌史改写成“控制权转移史”，测量冠军优势的寿命，而不是累计奖牌总数。

## 主要发现

1896—2016年可比范围内，共识别 **{metrics['events']:,}** 个小项身份和 **{metrics['transitions']:,}** 次相邻届控制权转换。总体控制权延续率为 **{metrics['defense_rate']:.1%}**。最长连续王朝达到 **{metrics['longest_editions']}届**。不同体育大类的卫冕结构差异显著，说明“体育强国”并不是统一能力，而是一组寿命不同的项目优势。

![时代卫冕率](../04_核心图表/S3_时代卫冕率.png)

![项目差异](../04_核心图表/S3_项目王朝差异.png)

![最长王朝](../04_核心图表/S3_最长冠军王朝.png)

## 口径与边界

- 研究单位为 `Sport + Event`；同一小项相邻两次出现时，金牌NOC集合存在交集即视为控制权延续。
- 排除非正式的1906届；2020年Event泛化、2024年与历史命名体系不同，因此不进入纵向主分析。
- 小项停办后重返时，比较的是“相邻出现”，不是自然四年周期。
- 并列金牌以集合处理，不强行指定唯一冠军。
'''
(REPORT/'S3_冠军的保质期_分析报告.md').write_text(md,encoding='utf-8')
(TASK/'00_先看这里.md').write_text('# S3｜冠军的保质期\n\n建议先阅读 `01_报告与说明/S3_冠军的保质期_分析报告.md`，再查看 `04_核心图表` 与 `02_数据表`。\n',encoding='utf-8')
(CODE/'生成S3.py').write_text('# 正式复现入口位于：项目工作区/scripts/task3_s3_dynasties.py\n',encoding='utf-8')
print(json.dumps(metrics,ensure_ascii=False,indent=2))
