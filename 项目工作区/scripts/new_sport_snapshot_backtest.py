"""Pre-Games ranking snapshot test for an Olympic entrant sport: rugby sevens.

This tests the ranking feature itself, not the full LA28 ensemble. World Rugby
season standings were known before each Games; medal outcomes are held out.
"""
from pathlib import Path
import pyreadr
import pandas as pd

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'交付文件'/'任务四_开放创作'/'05_满分升级'/'10_新增运动历史快照回测'
OUT.mkdir(parents=True,exist_ok=True)
ARCH=ROOT/'资料文件'/'外部核验'/'olympicscom_抓取存档'/'summer_games.rda'
results=pyreadr.read_r(str(ARCH))['summer_games']

# The order below is stated in the linked federation reports/articles. GBR is
# deliberately NOT substituted for England: the series-to-Olympics entity
# mapping is not one-to-one and is excluded from the scored top three.
snapshots=[
 (2016,'男子','2015-16', ['Fiji','South Africa','New Zealand'],
  'https://resources.world.rugby/worldrugby/document/2016/12/06/9c27dfbd-5ae8-4e85-b0a4-4d4f6fedfbb3/2015-16-World-Rugby-HSBC-Sevens-Series-Game-Analysis-Report.pdf'),
 (2016,'女子','2015-16', ['Australia','New Zealand','Canada'],
  'https://resources.world.rugby/worldrugby/document/2016/12/06/f479edd1-451f-4031-8e70-69f24183f6fe/2015-16-World-Rugby-HSBC-Women-s-Sevens-Series-Game-Analysis-Report.pdf'),
 (2020,'男子','2018-19', ['Fiji','United States of America','New Zealand'],
  'https://www.world.rugby/news/427722/fiji-clinch-hsbc-world-rugby-sevens-series-title-in-paris'),
 (2020,'女子','2018-19', ['New Zealand','United States of America','Canada'],
  'https://www.world.rugby/news/431049/awards-night-brings-record-breaking-womens-series-to-an-end?lang=en'),
]
rows=[];scores=[]
for year,sex,season,top,source in snapshots:
    game='rio-2016' if year==2016 else 'tokyo-2020'
    sport='rugby' if year==2016 else 'rugby-sevens'
    event=('rugby-7-' if year==2016 else '')+('men' if sex=='男子' else 'women')
    actual=results[(results.game==game)&(results.sport==sport)&(results.event==event)&results['rank'].isin(['G','S','B'])]
    medalists=set(actual.team)
    assert len(actual)==3, (year,sex)
    for rank,team in enumerate(top,1):
        rows.append({'奥运届次':year,'性别':sex,'赛前赛季':season,'赛前排名':rank,'代表队':team,
                     '是否获牌':team in medalists,'实际奖牌':next(iter(actual.loc[actual.team.eq(team),'rank']),''),
                     '赛前排名一手来源':source,
                     '结果存档':'https://www.olympics.com/en/olympic-games/'+game+'/results/'+sport+'/'+event})
    scores.append({'奥运届次':year,'性别':sex,'赛前前3名获牌数':len(set(top)&medalists),
                   '赛前第1名获金':top[0] in set(actual.loc[actual['rank'].eq('G'),'team']),
                   '实际奖牌队':'; '.join(actual.team),'赛前前3名':'; '.join(top)})
detail=pd.DataFrame(rows);summary=pd.DataFrame(scores)
detail.to_csv(OUT/'赛前排名快照与逐队结果.csv',index=False,encoding='utf-8-sig')
summary.to_csv(OUT/'四场比赛排名信号评分.csv',index=False,encoding='utf-8-sig')
hit=int(summary['赛前前3名获牌数'].sum());champ=int(summary['赛前第1名获金'].sum())
md=f'''# 新增运动信号：赛前排名快照的历史类比回测

选择2016年进入奥运的七人制橄榄球，使用国际单项组织 World Rugby 在赛前已完成的2015–16赛季排名，对照里约2016的男、女奖牌；再以2018–19赛季排名对照东京2020（实际2021举行）的男、女奖牌。排名材料来自 World Rugby，实际成绩来自 Olympics.com 的2023年第三方抓取存档；来源链接逐行保留在CSV中。东京案例受到疫情和赛季间隔影响，是压力测试，不是正常四年周期的直接复制。

四场比赛中，赛前前三名合计命中 **{hit}/12** 个实际获牌席位；赛前第一名赢得金牌 **{champ}/4** 次。分别看：

| 届次 | 性别 | 前三名命中 | 第一名获金 | 赛前前三名 | 实际获牌队 |
|---|---|---:|---|---|---|
'''
for r in summary.itertuples(index=False):
    md+=f'| {r.奥运届次} | {r.性别} | {r.赛前前3名获牌数}/3 | {"是" if r.赛前第1名获金 else "否"} | {r.赛前前3名} | {r.实际奖牌队} |\n'
md+='''
## 可迁移与不可迁移之处

这项实验验证的是**赛前国际排名作为新增运动竞争力信号是否有方向性**。2016年男子世界系列赛中的英格兰与奥运英国队、以及部分项目的国家与奥运代表团身份不一一对应，故只使用来源中清晰可比的前三名；未把英格兰直接当英国。2020实际在2021举办，2019排名距比赛有更长间隔。四场比赛样本很小，不能据此估计2028五项新增运动的统一转化系数。

**2028最终集成的端到端历史回测依然无法原样完成**：板球T20、棒垒球、腰旗橄榄球、长曲棍球六人制和壁球在历史奥运缺少相同的参赛结构、官方小项口径与赛前排名快照。这里提供了可复算的新增运动信号类比检验，但没有把它冒充五项运动整体回测。复算：`python 项目工作区/scripts/new_sport_snapshot_backtest.py`。

另须注意，当前交付包里的 `新增项目权威排名特征.csv` 尚无逐条可点开的官方排名归档URL和抓取哈希，其中的数值只能作为**情景输入**，不能称为已证实的“权威快照”。正式对外引用前需逐运动补齐带日期的原始榜单、奥运参赛资格映射与版本哈希；未补齐时应对10%排名分量做关闭敏感性情景。
'''
(OUT/'方法与结果.md').write_text(md,encoding='utf-8')
print(summary.to_string(index=False));print('top3 medal hits',hit,'/12; rank1 gold',champ,'/4')
