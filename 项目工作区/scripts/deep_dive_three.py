"""Three reproducible follow-up analyses: small teams, forecast errors, dynasties."""
from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from task2_localization import SPORT_ZH
from publish_dynasty_sport_chart import sport_chart

ROOT = Path(__file__).resolve().parents[2]
T3 = ROOT/'交付文件'/'任务三_专题深挖'
T4 = ROOT/'交付文件'/'任务四_开放创作'/'05_满分升级'
S4 = T3/'S4_小代表团的大突破'/'03_突破还是持续'
S7 = T3/'S3_冠军的保质期'/'10_王朝机制与反例'
F = T4/'08_历史误差归因'
for p in (S4,S7,F): p.mkdir(parents=True,exist_ok=True)
plt.rcParams['font.sans-serif']=['Microsoft YaHei','SimHei','DejaVu Sans']
plt.rcParams['axes.unicode_minus']=False

def page(title,lead,body,folder):
    css='''body{margin:0;background:#f2eee5;color:#173447;font-family:"Microsoft YaHei",sans-serif}main{max-width:1080px;margin:auto;padding:56px 24px 90px}h1{font-size:clamp(38px,6vw,70px);line-height:1.15}p{line-height:1.85}img{display:block;width:100%;border-radius:18px;margin:26px 0}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:15px}.card{background:#fffaf2;border-radius:18px;padding:22px}.card b{display:block;font:700 32px Georgia;color:#ad5b40;margin-top:8px}table{width:100%;border-collapse:collapse;background:#fffaf2}th,td{padding:10px;text-align:left;border-bottom:1px solid #ddd6c9}.scroll{overflow-x:auto}.note{background:#173e54;color:#fff;border-radius:20px;padding:25px;margin:26px 0}a{color:#267497}@media(max-width:700px){.grid{grid-template-columns:1fr}table{font-size:13px}}'''
    html=f'<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}｜百年圣火</title><style>{css}</style></head><body><main><small>百年圣火 · 深度检验</small><h1>{title}</h1><p>{lead}</p>{body}</main></body></html>'
    (folder/'index.html').write_text(html,encoding='utf-8')

def small():
    base=T3/'S4_小代表团的大突破'/'02_客观样本'
    d=pd.read_csv(base/'2000_2024全部候选及纳入判定.csv')
    e=pd.read_csv(base/'入选代表团逐届记录.csv')
    # The denominator is every eligible NOC below the size threshold, including no-medal cases.
    q=d[(d.bottom_quartile)&~d.NOC.isin(['AIN','EOR','IOA'])].copy()
    q['outcome']=np.select([q.medal_editions.ge(2),q.medal_editions.eq(1)],['重复获奖','单届突破'],default='尚未获奖')
    q.to_csv(S4/'全部小代表团与结局.csv',index=False,encoding='utf-8-sig')
    counts=q.outcome.value_counts().reindex(['尚未获奖','单届突破','重复获奖'],fill_value=0)
    m=e[e.medal_rows.gt(0)].sort_values(['NOC','Year'])
    first=m.groupby('NOC').Year.min().rename('首次获奖年')
    rel=q.set_index('NOC').join(first).reset_index()
    rel['首次获奖距2024届数']=(2024-rel['首次获奖年'])/4
    rel['has_later_observation']=rel['首次获奖年'].lt(2024)
    rel.to_csv(S4/'首次获奖与随访窗口.csv',index=False,encoding='utf-8-sig')
    fig,ax=plt.subplots(figsize=(10,5.8),facecolor='#f2eee5');ax.set_facecolor('#f2eee5')
    bars=ax.barh(counts.index[::-1],counts.values[::-1],color=['#31758a','#b86342','#cac2b1'])
    for b in bars:ax.text(b.get_width()+.3,b.get_y()+b.get_height()/2,int(b.get_width()),va='center',fontsize=15)
    ax.set_xlim(0,max(counts)+3);ax.spines[:].set_visible(False);ax.tick_params(length=0)
    ax.set_xlabel('代表团数');fig.text(.08,.92,'一次突破，不等于持续崛起',fontsize=23,weight='bold',color='#173447')
    fig.tight_layout(rect=[0,0,1,.85]);fig.savefig(S4/'突破持续分布.png',dpi=180,facecolor=fig.get_facecolor());plt.close(fig)
    summary={'denominator':len(q),'no_medal':int(counts['尚未获奖']),'one_edition':int(counts['单届突破']),'repeat':int(counts['重复获奖']),'first_medal_2024':int(first.eq(2024).sum())}
    (S4/'摘要.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
    md=f'''# 小代表团：突破与持续\n\n2000—2024 七届中，至少出现三届、典型参赛运动员行数不高于原预设下四分位门槛的国家代表团共有 **{len(q)} 个**。这里将未获奖者放回分母：尚未获奖 **{counts['尚未获奖']}**，只在一届获奖 **{counts['单届突破']}**，至少两届获奖 **{counts['重复获奖']}**。获奖样本的重复获奖比例是 {counts['重复获奖']}/{int(q.medal_editions.gt(0).sum())}，不能用作未来成功率估计。\n\n首次获奖若发生于2024，观察窗没有后续奥运会，不能归入“不能延续”。具体首次获奖年及随访机会见 CSV。奖牌仍是运动员行口径，团体项目会放大行数；结果只按“是否有获奖届次”分类。小样本和选定时间窗限制推广性。\n\n原七个叙事案例均不满足最严格的下四分位规模门槛，因此 S4 应写作“突破的不同路径”，并明确客观样本才是小代表团总体分析。复算：`python 项目工作区/scripts/deep_dive_three.py`。\n'''
    (S4/'研究说明.md').write_text(md,encoding='utf-8')
    body=f'<div class="grid"><div class="card">全部小规模代表团<b>{len(q)}</b></div><div class="card">单届突破<b>{counts["单届突破"]}</b></div><div class="card">重复获奖<b>{counts["重复获奖"]}</b></div></div><img src="突破持续分布.png" alt="小代表团突破与持续分布"><div class="note">原七个故事并非严格下四分位样本。获奖一次也不能证明持续崛起；2024首次获奖者尚无下一届可观察。</div><p><a href="全部小代表团与结局.csv">下载全部分母</a>　<a href="首次获奖与随访窗口.csv">核对随访机会</a>　<a href="研究说明.md">研究说明</a></p>'
    page('一次突破，能延续吗？',f'将未获奖者放回分母，在 {len(q)} 个小规模代表团中区分没有奖牌、单届突破与重复获奖。',body,S4)
    return summary

def forecast():
    d=pd.read_csv(T4/'滚动留出逐队同口径结果.csv')
    d['baseline_error']=(d.baseline-d.actual).abs();d['project_error']=(d.project-d.actual).abs()
    d['blend_error']=(d.blend-d.actual).abs();d['blend_gain']=d.baseline_error-d.blend_error
    d['project_gain']=d.baseline_error-d.project_error
    d['size_group']=pd.cut(d.actual,[-.1,.1,1,4,19,1e9],labels=['0枚','1枚','2—4枚','5—19枚','20枚及以上'])
    by=d.groupby(['Year','size_group'],observed=True).agg(n=('NOC','size'),baseline_MAE=('baseline_error','mean'),project_MAE=('project_error','mean'),blend_MAE=('blend_error','mean'),blend_gain=('blend_gain','mean')).reset_index()
    by.to_csv(F/'逐届规模组误差.csv',index=False,encoding='utf-8-sig')
    d.sort_values('blend_gain').to_csv(F/'逐队误差改进与反例.csv',index=False,encoding='utf-8-sig')
    leaders=d.groupby('NOC').agg(appearances=('Year','size'),total_gain=('blend_gain','sum'),mean_gain=('blend_gain','mean')).query('appearances==3').reset_index().sort_values('total_gain')
    leaders.to_csv(F/'三届共同代表团改进.csv',index=False,encoding='utf-8-sig')
    fig,axes=plt.subplots(1,3,figsize=(13,5.5),sharey=True,facecolor='#f2eee5')
    for ax,(year,g) in zip(axes,d.groupby('Year')):
        b=g.groupby('size_group',observed=True).blend_gain.mean().reindex(['0枚','1枚','2—4枚','5—19枚','20枚及以上'])
        ax.barh(b.index,b.values,color=['#1b7487' if x>=0 else '#b65f41' for x in b.values]);ax.axvline(0,color='#173447',lw=1);ax.set_title(str(year));ax.set_facecolor('#f2eee5');ax.spines[:].set_visible(False);ax.tick_params(length=0)
    fig.text(.06,.94,'项目级模型，在哪些代表团帮了忙？',fontsize=22,weight='bold',color='#173447')
    fig.text(.06,.02,'正值：混合模型绝对误差小于透明基线；按实际奖牌数分组，仅为事后诊断。',fontsize=10,color='#536b73')
    fig.tight_layout(rect=[0,.06,1,.88]);fig.savefig(F/'规模组误差归因.png',dpi=180,facecolor=fig.get_facecolor());plt.close(fig)
    summ=d.groupby('Year').agg(n=('NOC','size'),improved=('blend_gain',lambda x:int((x>0).sum())),worsened=('blend_gain',lambda x:int((x<0).sum())),mean_gain=('blend_gain','mean')).reset_index()
    summ.to_csv(F/'逐届改进人数.csv',index=False,encoding='utf-8-sig')
    md='# 历史预测：误差归因与反例\n\n此处使用已发布的 2012、2016、2024 同口径滚动留出逐队结果，直接比较透明基线、项目模型、55/45混合模型。正的“改进”是基线绝对误差减混合模型绝对误差。\n\n'
    md+='| 届次 | 改善代表团 | 变差代表团 | 平均改进（枚） |\n|---|---:|---:|---:|\n'
    for r in summ.itertuples():md+=f'| {r.Year} | {r.improved}/{r.n} | {r.worsened}/{r.n} | {r.mean_gain:+.2f} |\n'
    md+='\n按实际奖牌数分层是**事后误差诊断**，不能在赛前用作选模规则；三届共现代表团的改进与反例见表。历史2012、2016小项使用代理，2024才是官方表。各届奖牌池为事后已知；2028新增运动和主场分量仍未得到同类历史端到端验证。\n\n运动层面：当前滚动结果仅保存代表团总量预测，无法从总量误差反推各运动的贡献。不能把运动员行训练特征与小项奖牌误差直接拼表并称为同口径运动验证；这项需要另建小项级历史真值与赛前项目预测。\n'
    (F/'误差归因说明.md').write_text(md,encoding='utf-8')
    rows=''.join(f'<tr><td>{r.Year}</td><td>{r.improved}/{r.n}</td><td>{r.worsened}/{r.n}</td><td>{r.mean_gain:+.2f}</td></tr>' for r in summ.itertuples())
    body=f'<img src="规模组误差归因.png" alt="逐届分层误差变化"><div class="scroll"><table><tr><th>届次</th><th>改善</th><th>变差</th><th>平均改进</th></tr>{rows}</table></div><div class="note">复杂模型并非对每个代表团都有帮助。按实际奖牌数分组只用于赛后诊断。当前历史回测没有同单位运动级真值和预测，因此不声称已经完成运动级误差归因。</div><p><a href="逐队误差改进与反例.csv">逐队反例</a>　<a href="逐届规模组误差.csv">规模分层</a>　<a href="误差归因说明.md">方法边界</a></p>'
    page('模型到底帮了谁？','把历史预测的平均分拆开：逐届、逐代表团、逐奖牌规模看改善和恶化。',body,F)
    return summ.to_dict('records')

def dynasty():
    src=T3/'S3_冠军的保质期'/'09_固定小项队列检验'/'固定小项逐届控制权转移.csv'
    d=pd.read_csv(src)
    # Event text offers a reproducible sex label; ambiguous/mixed events stay separate.
    e=d.Event.str.lower().fillna('')
    d['sex_group']=np.select([e.str.contains(r"women's|female|girls"),e.str.contains(r"men's|male|boys")],['女子','男子'],default='混合或未标明')
    team_words=r'team|relay|doubles|pairs|eight|four|quad|crew|synchroni|group'
    d['format_proxy']=np.where(e.str.contains(team_words,regex=True),'疑似多人','其余小项')
    d['era']=np.select([d.to_year.between(1964,1976),d.to_year.between(1996,2016)],['早段','后段'],default='转折期')
    part=d[d.era.ne('转折期')]
    g=part.groupby(['Sport','sex_group','format_proxy','era'],observed=True).defended.agg(['sum','size','mean']).reset_index()
    g.to_csv(S7/'运动性别与赛制分层.csv',index=False,encoding='utf-8-sig')
    sport=part.groupby(['Sport','era']).defended.agg(['sum','size','mean']).reset_index().pivot(index='Sport',columns='era',values=['sum','size','mean'])
    sport.columns=['_'.join(x) for x in sport.columns];sport=sport.reset_index()
    sport['late_minus_early_pp']=100*(sport['mean_后段']-sport['mean_早段'])
    sport.sort_values('late_minus_early_pp').to_csv(S7/'逐运动趋势与反例.csv',index=False,encoding='utf-8-sig')
    sex=part.groupby(['sex_group','era']).defended.agg(['sum','size','mean']).reset_index()
    sex.to_csv(S7/'性别分层.csv',index=False,encoding='utf-8-sig')
    fmt=part.groupby(['format_proxy','era']).defended.agg(['sum','size','mean']).reset_index()
    fmt.to_csv(S7/'赛制代理分层.csv',index=False,encoding='utf-8-sig')
    # Event-level trajectories surface counterexamples instead of ranking noisy single outcomes.
    ev=part.groupby(['event_key','Sport','Event','sex_group','format_proxy','era']).defended.mean().reset_index().pivot(index=['event_key','Sport','Event','sex_group','format_proxy'],columns='era',values='defended').reset_index()
    ev['late_minus_early_pp']=100*(ev['后段']-ev['早段'])
    ev.sort_values('late_minus_early_pp',ascending=False).to_csv(S7/'固定小项反例.csv',index=False,encoding='utf-8-sig')
    fig,ax=plt.subplots(figsize=(11,6),facecolor='#f2eee5');ax.set_facecolor('#f2eee5')
    view=sport[sport['size_早段'].ge(8)].sort_values('late_minus_early_pp').tail(12)
    ax.barh(view.Sport.map(lambda x:SPORT_ZH.get(x,{'Equestrianism':'马术'}.get(x,x))),view.late_minus_early_pp,color=['#b65f41' if v<0 else '#1b7487' for v in view.late_minus_early_pp]);ax.axvline(0,color='#173447');ax.spines[:].set_visible(False);ax.tick_params(length=0)
    ax.set_xlabel('后段－早段卫冕率（百分点）');fig.text(.08,.94,'总体下降，不代表每种运动都下降',fontsize=22,weight='bold',color='#173447')
    fig.tight_layout(rect=[0,0,1,.88]);fig.savefig(S7/'逐运动反例.png',dpi=180,facecolor=fig.get_facecolor());plt.close(fig)
    sexrows=''.join(f'<tr><td>{r.sex_group}</td><td>{r.era}</td><td>{r["size"]}</td><td>{r["mean"]:.1%}</td></tr>' for _,r in sex.iterrows())
    md='# 固定小项的机制线索与反例\n\n在已锁定的113个连续小项内，按项目名称提取男子、女子、混合/未标明，并以 Team、Relay、Doubles 等词标记“疑似多人”；该标记只是名称代理，不能等同官方项目规则。早段为1964—1976，后段为1996—2016。\n\n'
    md+='## 性别分层\n\n| 分组 | 时段 | 转移数 | 卫冕率 |\n|---|---|---:|---:|\n'
    for _,r in sex.iterrows():md+=f'| {r.sex_group} | {r.era} | {r["size"]} | {r["mean"]:.1%} |\n'
    md+='\n逐运动和逐小项的正向反例已单列。分层是探索性描述，运动数与小项数很不均衡；不能把性别或赛制差异解释为成因。赛事规则、参赛资格、政体变化仍是未控制混杂；同名 Event 也未核验规则完全稳定。\n\n复算：`python 项目工作区/scripts/deep_dive_three.py`。\n'
    (S7/'机制与反例说明.md').write_text(md,encoding='utf-8')
    body=f'{sport_chart(S7)}<h2>性别分层</h2><div class="scroll"><table><tr><th>分组</th><th>时段</th><th>转移数</th><th>卫冕率</th></tr>{sexrows}</table></div><div class="note">总体下降并不保证每种运动都下降。性别和多人赛制仅按历史小项名称代理，不能视为因果机制；规则变化仍未逐项核验。</div><p><a href="逐运动趋势与反例.csv">逐运动数据</a>　<a href="固定小项反例.csv">查看小项反例</a>　<a href="机制与反例说明.md">方法与边界</a></p>'
    page('王朝为何变短？先看反例。','在113个固定小项中拆开运动、性别和疑似多人赛制，检验总体趋势是否掩盖相反方向。',body,S7)
    return {'sports':len(sport),'counterexample_sports':int((sport.late_minus_early_pp>0).sum())}

def link_file(path,marker,block):
    if not path.exists():return
    s=path.read_text(encoding='utf-8')
    if marker not in s:path.write_text(s.replace('</body>',f'<!-- {marker} -->{block}</body>',1),encoding='utf-8')

if __name__=='__main__':
    out={'small':small(),'forecast':forecast(),'dynasty':dynasty()}
    link_file(T3/'S4_小代表团的大突破'/'index.html','s4-followup','<a href="03_突破还是持续/index.html" style="display:block;max-width:1000px;margin:30px auto;padding:24px;border-radius:20px;background:#173e54;color:white;text-decoration:none">新研究：一次突破，能延续吗？ ↗</a>')
    link_file(T3/'S3_冠军的保质期'/'06_冠军王朝时间轴'/'index.html','s7-mechanism','<a href="../10_王朝机制与反例/index.html" style="display:block;max-width:1000px;margin:30px auto;padding:24px;border-radius:20px;background:#173e54;color:white;text-decoration:none">新研究：逐运动与小项反例 ↗</a>')
    link_file(T4/'滚动留出验证.html','forecast-attribution','<a href="08_历史误差归因/index.html" style="display:block;max-width:980px;margin:30px auto;padding:24px;border-radius:20px;background:#173e54;color:white;text-decoration:none">新研究：模型到底帮了谁？ ↗</a>')
    print(json.dumps(out,ensure_ascii=False,indent=2))
