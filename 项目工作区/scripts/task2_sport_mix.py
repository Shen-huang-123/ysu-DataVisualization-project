from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
TASK = ROOT / '交付文件' / '任务二_百年全景'
OUT = TASK / '12_固定运动构成'
YEARS = (2016, 2020, 2024)

def calculate():
    raw = pd.read_csv(ROOT/'交付文件/任务一_数据体检/02_交付数据/归一数据_保留原始字段.csv.gz',
                      usecols=['Year','NOC','sport_family','include_main','is_medal'])
    selected = raw[raw.Year.isin(YEARS) & raw.include_main & raw.is_medal]
    if selected[['NOC','sport_family']].isna().any().any():
        raise ValueError('获奖记录含空代表团或运动家族')
    edition = {
        year: df.groupby(['sport_family','NOC']).size().unstack(fill_value=0)
        for year, df in selected.groupby('Year')
    }
    common = sorted(set.intersection(*(set(frame.index) for frame in edition.values())))
    counts = {year: edition[year].loc[common].sum(axis=1) for year in YEARS}
    probabilities = {year: edition[year].loc[common].div(counts[year],axis=0) for year in YEARS}
    weights = {year: counts[year]/counts[year].sum() for year in YEARS}
    pooled = sum(counts.values())
    fixed_weights = pooled/pooled.sum()
    summaries, teams = [], []

    def combine(weight, shares):
        return shares.mul(weight,axis=0).sum(axis=0)

    def statistics(shares):
        shares = shares[shares>0].sort_index()
        shares = shares.loc[shares.round(12).sort_values(ascending=False,kind='stable').index]
        assert abs(shares.sum()-1)<1e-9
        return shares,shares.head(5).sum(),1/shares.pow(2).sum()

    for year in YEARS:
        population = edition[year].sum(axis=0)
        for name,shares in (
            ('全场实际',population/population.sum()),
            ('共同运动实际',combine(weights[year],probabilities[year])),
            ('共同运动固定权重',combine(fixed_weights,probabilities[year])),
        ):
            ranked,top,effective=statistics(shares)
            summaries.append([year,name,len(common),int(population.sum()),int(counts[year].sum()),
                              len(ranked),top,effective,'、'.join(ranked.index[:5]),
                              '、'.join(ranked.index[(ranked-ranked.iloc[4]).abs()<1e-12])])
            teams.extend((year,name,noc,share) for noc,share in ranked.items())
    start,end = YEARS[0],YEARS[-1]
    baseline_top = statistics(combine(fixed_weights,probabilities[start]))[0].head(5).index
    change = probabilities[end].reindex(columns=baseline_top,fill_value=0).sum(axis=1) - probabilities[start].reindex(columns=baseline_top,fill_value=0).sum(axis=1)
    contribution = 100*fixed_weights*change
    old = combine(fixed_weights,probabilities[start]).reindex(baseline_top,fill_value=0).sum()
    new = combine(fixed_weights,probabilities[end]).reindex(baseline_top,fill_value=0).sum()
    assert abs(contribution.sum()-100*(new-old))<1e-9
    # Average two substitution paths to account for the interaction of weights and shares.
    counterfactual = {
        (w,p): statistics(combine(weights[w],probabilities[p]))[1:]
        for w in (start,end) for p in (start,end)
    }
    split = []
    for i,metric in enumerate(('前五份额_百分点','有效获奖代表团数')):
        a,b,c,d = (counterfactual[pair][i] for pair in ((start,start),(start,end),(end,start),(end,end)))
        unit = 100 if i==0 else 1
        split.append((metric,unit*(d-a),unit*((b-a)+(d-c))/2,unit*((c-a)+(d-b))/2))
    sensitivity = []
    for name,weight in (('三届合并权重',fixed_weights),('2016共同运动权重',weights[start]),
                        ('2024共同运动权重',weights[end]),('运动等权',fixed_weights*0+1/len(common))):
        for year in YEARS:
            _,top,effective = statistics(combine(weight,probabilities[year]))
            sensitivity.append((name,year,top,effective))
    russian_start = float(combine(fixed_weights,probabilities[start]).get('RUS',0))
    russian_end = float(combine(fixed_weights,probabilities[end]).get('RUS',0))
    return summaries,teams,counts,fixed_weights,contribution,baseline_top,old,new,split,sensitivity,russian_start,russian_end

def publish_reading(report):
    import re
    from markdown import markdown

    reference = (TASK/'08_女性结构分解/女性结构分解.html').read_text(encoding='utf-8')
    nav = re.search(r'<nav aria-label="作品导航" id="xz-nav".*?</aside>', reference)[0]
    assets = '\n'.join(re.search(pattern,reference)[0] for pattern in (
        r'<link[^>]+id="supplement-assets"[^>]*>',
        r'<script id="supplement-theme-preload">.*?</script>',
        r'<script[^>]*src="[^"]*supplement-reading.js[^"]*"[^>]*></script>',
        r'<link[^>]+id="supp-task-nav-assets"[^>]*>',
        r'<script[^>]*src="[^"]*integrated-nav.js[^"]*"[^>]*></script>',
        r'<link[^>]+id="chart-surface-theme"[^>]*>',
    ))
    title,body = report.split('\n',1)
    content = markdown(body)
    content = re.sub(r'<p>(<img [^>]+?)/></p>',r'<figure>\1 class="chart-surface" /></figure>',content,count=1)
    title = title.removeprefix('# ')
    html = f'''<!doctype html>
<html lang="zh-CN">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}｜百年全景</title>
{assets}
</head>
<body class="supplement-reading">
{nav}
<main class="supp-content">
<p><a href="../11_四视角独立交付/四视角核心图复核.html#view-A">← 返回奖牌格局图表</a></p>
<h1>{title}</h1>
{content}
<p><a href="固定运动构成复核.md" download>下载 Markdown 原件</a></p>
</main>
</body></html>
'''
    (OUT/'固定运动构成复核.html').write_text(html,encoding='utf-8')


def publish():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from task2_localization import SPORT_ZH

    OUT.mkdir(exist_ok=True)
    summaries,teams,counts,weights,contributions,baseline,old,new,split,sensitivity,rus_old,rus_new = calculate()
    summary = pd.DataFrame(summaries,columns=['届次','口径','共同运动数','全场获奖行','共同运动获奖行',
                                             '获奖代表团数','前五份额','有效获奖代表团数','前五代表团','第五名同份额队'])
    summary.to_csv(OUT/'三口径集中度.csv',index=False,encoding='utf-8-sig')
    pd.DataFrame(teams,columns=['届次','口径','代表团','份额']).to_csv(OUT/'逐队份额.csv',index=False,encoding='utf-8-sig')
    pd.DataFrame(counts).assign(固定权重=weights,固定五队贡献_百分点=contributions).rename_axis('运动大类').to_csv(
        OUT/'逐运动权重与固定五队贡献.csv',encoding='utf-8-sig')
    pd.DataFrame(split,columns=['指标','共同运动实际变化','运动内部份额效应','运动权重效应']).to_csv(
        OUT/'共同运动变化分解.csv',index=False,encoding='utf-8-sig')
    alternatives = pd.DataFrame(sensitivity,columns=['固定权重方案','届次','前五份额','有效获奖代表团数'])
    alternatives.to_csv(OUT/'固定权重敏感性.csv',index=False,encoding='utf-8-sig')
    limits = alternatives.pivot(index='固定权重方案',columns='届次',values='前五份额')
    deltas = 100*(limits[2024]-limits[2016])
    assert (deltas>0).all()
    for _,total,within,mix in split:
        assert abs(total-within-mix)<1e-10
    starts=summary.loc[summary['届次']==2016].set_index('口径')
    ends=summary.loc[summary['届次']==2024].set_index('口径')
    changes=(ends['前五份额']-starts['前五份额'])*100
    fixed='共同运动固定权重'
    assert changes[fixed]>0 and new<old
    lead = f"2016 到 2024，前五份额实际增加 {changes['全场实际']:.2f} 个百分点；固定 {len(weights)} 类共同运动权重后仍增加 {changes[fixed]:.2f} 个百分点。"
    cohort = '、'.join(baseline)
    group = f"固定 2016 年标准化榜前五队（{cohort}）时，同一组队伍的合计份额从 {old:.2%} 降至 {new:.2%}。"
    note = '采用夏奥运动员获奖记录行，排除 1906。历史代表团代码分开；同份额按代表团代码排序取五，前五阈值并列名单见表。'
    report = f"""# 固定运动构成后，前五份额仍回升吗？

![三种口径下的集中度对照](固定运动构成与奖牌集中度.png)

{lead} 东京 2020 在三种口径下都处于这三届的低位。固定权重后，有效获奖代表团数从 {starts.loc[fixed,'有效获奖代表团数']:.2f} 降至 {ends.loc[fixed,'有效获奖代表团数']:.2f}。

## 运动内份额与运动权重

三届均有获奖行的 {len(weights)} 类运动进入共同集合。共同运动实际值沿用各届自己的记录权重。固定权重取三届共同运动合并后的记录构成，再乘各届各运动内每个代表团的份额并加总。每种口径按份额重新排前五。有效获奖代表团数为各队份额平方和的倒数。

在共同运动实际口径下，前五份额增加 {split[0][1]:.2f} 个百分点。将 2016 与 2024 的运动权重和运动内份额逐一替换，并平均两种替换顺序，运动内份额贡献 {split[0][2]:+.2f} 个百分点，运动权重贡献 {split[0][3]:+.2f} 个百分点。每个替换情景都重新排名；这两个贡献严格加总为共同运动实际变化。

改用 2016 运动权重、2024 运动权重或运动等权，连同三届合并权重，2016 到 2024 的前五份额变化落在 {deltas.min():+.2f} 至 {deltas.max():+.2f} 个百分点之间。四种固定权重方案下方向一致。

## 同一组队伍怎样变化

{group} 这组固定队伍的正贡献主要来自田径（{contributions['Athletics']:+.2f} 个百分点），负贡献主要来自击剑（{contributions['Fencing']:+.2f}）、体操（{contributions['Gymnastics']:+.2f}）。逐运动贡献使用统一运动权重，合计等于固定五队的份额变化。此处的固定队伍结果与每届重新选出的前五回答两个问题。2024 固定权重重新排名的前五为 {ends.loc[fixed,'前五代表团']}。

## 口径与复算

{note} RUS、ROC 等历史代码分别计量，固定五队的降幅包含 RUS 的标准化份额从 {rus_old:.2%} 至 {rus_new:.2%} 的变化；若仅比较同组另外四队，其合计份额变化为 {100*((new-rus_new)-(old-rus_old)):+.2f} 个百分点。结论只适用于这三届和所定义的共同运动；标准化是描述性比较，无法识别因果效应。

复算入口为 `项目工作区/scripts/task2_sport_mix.py`，输入是任务一交付的归一数据（保留原始字段）。

[三口径集中度](三口径集中度.csv) · [逐队份额](逐队份额.csv) · [运动权重与贡献](逐运动权重与固定五队贡献.csv) · [变化分解](共同运动变化分解.csv) · [固定权重敏感性](固定权重敏感性.csv)
"""
    (OUT/'固定运动构成复核.md').write_text(report,encoding='utf-8')
    publish_reading(report)
    review=TASK/'11_四视角独立交付/四视角核心图复核.html'
    import re
    from html import escape
    html=review.read_text(encoding='utf-8')
    html=re.sub(r'<!-- sport-mix:start -->.*?<!-- sport-mix:end -->\n?','',html,flags=re.S)
    position=html.index('</section>',html.index('id="view-A"'))
    prefix='../12_固定运动构成/'
    fragment=(
        f'<!-- sport-mix:start -->\n<h3>固定运动构成后，前五份额仍回升</h3>'
        f'<figure class="additional-core-chart"><a href="{prefix}固定运动构成与奖牌集中度.png">'
        f'<img src="{prefix}固定运动构成与奖牌集中度.png" alt="固定运动构成前后的集中度和运动贡献" loading="lazy"></a>'
        f'<figcaption>{escape(note)}</figcaption></figure><p>{escape(lead)}</p><p>{escape(group)}</p>'
        f'<p><a href="{prefix}固定运动构成复核.html">查看方法和复算入口</a> · '
        f'<a href="{prefix}三口径集中度.csv">下载三口径结果</a> · '
        f'<a href="{prefix}逐运动权重与固定五队贡献.csv">下载运动权重与贡献</a></p>\n<!-- sport-mix:end -->\n'
    )
    review.write_text(html[:position]+fragment+html[position:],encoding='utf-8',newline='\n')
    a=review.with_name('A_奖牌格局.md')
    content=a.read_text(encoding='utf-8')
    content=re.sub(r'<!-- sport-mix:start -->.*?<!-- sport-mix:end -->\n?','',content,flags=re.S)
    a.write_text(content.rstrip()+f'\n\n<!-- sport-mix:start -->\n{lead} {group} '
                 f'[查看图表和复算表]({prefix}固定运动构成复核.html)。\n<!-- sport-mix:end -->\n',
                 encoding='utf-8',newline='\n')
    plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':12,'axes.spines.top':False,
                         'axes.spines.right':False,'axes.unicode_minus':False,'figure.facecolor':'#fbfaf6','axes.facecolor':'#fbfaf6'})
    fig,axes=plt.subplots(1,3,figsize=(14,5.8),gridspec_kw={'width_ratios':[1,1,1.15]})
    fig.subplots_adjust(left=.07,right=.97,bottom=.2,top=.73,wspace=.53)
    labels=['全场实际','共同运动实际',fixed]
    for axis,metric,scale,title in zip(axes[:2],['前五份额','有效获奖代表团数'],[100,1],
                                       ['前五份额（%）','有效获奖代表团数']):
        for label,color,style,mark in zip(labels,['#49737d','#966825','#963d54'],['-','--','-'],['o','s','D']):
            values=summary[summary['口径']==label][metric]*scale
            axis.plot(range(3),values,ls=style,marker=mark,label=label,color=color,linewidth=1.8)
        axis.set_title(title,fontsize=13)
        axis.set_xticks(range(3),YEARS)
        axis.grid(axis='y',color='#d8dfdf')
    axes[0].legend(loc='upper center',bbox_to_anchor=(1.25,-.17),ncol=3,frameon=False,fontsize=10)
    selected=pd.concat([contributions.nsmallest(3),contributions.nlargest(3)]).sort_values()
    axis=axes[2]
    axis.barh([SPORT_ZH.get(s,s) for s in selected.index],selected,
              color=['#963d54' if value<0 else '#49737d' for value in selected])
    axis.axvline(0,color='#697b7e',linewidth=.8)
    axis.set_title('固定 2016 年前五队',fontsize=13)
    axis.set_xlabel('份额变化贡献（百分点）')
    axis.set_xlim(-1.85,1.65)
    for i,value in enumerate(selected):
        axis.text(value+(.06 if value>0 else -.06),i,f'{value:+.2f}',va='center',
                  ha='left' if value>0 else 'right',fontsize=10)
    fig.text(.07,.93,'固定运动构成后，前五份额仍回升',fontsize=23,weight='bold',color='#193039')
    fig.text(.07,.84,lead+' 右图列固定五队贡献正负各前三项。',fontsize=12,color='#36555c')
    fig.text(.07,.035,note,fontsize=9.5,color='#36555c')
    fig.savefig(OUT/'固定运动构成与奖牌集中度.png',dpi=220)
    plt.close(fig)

if __name__ == '__main__':
    publish()