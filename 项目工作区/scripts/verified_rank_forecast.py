"""Conservative LA28 forecast: include only directly checked sport rankings.

Unverified sport signals receive zero incremental bonus and are not pooled into
verified sports. The historical baseline/ML/host terms stay identical.
"""
from pathlib import Path
import hashlib
import numpy as np
import pandas as pd
from task2_localization import NOC_ZH

ROOT=Path(__file__).resolve().parents[2]
PRED=ROOT/'交付文件'/'任务四_开放创作'/'02_2028洛杉矶预测'
OUT=ROOT/'交付文件'/'任务四_开放创作'/'05_满分升级'/'11_官方来源门控预测'
OUT.mkdir(parents=True,exist_ok=True)
old=pd.read_csv(PRED/'LA2028机器学习集成预测榜.csv').set_index('NOC')
assert old.index.is_unique
source='https://worldlacrosse.sport/world-rankings/'
# Current World Lacrosse Sixes tables, verified 2026-11-12. Haudenosaunee is
# excluded because it is not a currently confirmed Olympic NOC entry.
men={'CAN':1,'USA':2,'JPN':3,'GBR':4,'AUS':6,'GER':7,'ISR':8}
women={'USA':1,'CAN':2,'AUS':3,'JPN':4,'GBR':5,'CZE':6,'IRL':7,'CHN':8}
rows=[]
for noc in sorted(set(men)|set(women)):
    m=men.get(noc);w=women.get(noc)
    signal=(1/(m or 40)+1/(w or 40))/2
    rows.append({'新增运动':'长曲棍球六人制','NOC':noc,'男子排名':m,'女子排名':w,
                 '排名信号':signal,'一手来源':source,'核验日期':'2026-11-12',
                 '代表团映射':'直接同名国家队' if noc!='GBR' else '页面直接使用Great Britain',
                 '适用限制':'排名不等于奥运资格；资格须另行核对'})
verified=pd.DataFrame(rows)
verified.to_csv(OUT/'已核验六人制排名.csv',index=False,encoding='utf-8-sig')
flag_source='https://www.americanfootball.sport/ifaf-world-rankings/'
# IFAF 2025 flag-football tables, checked 2026-11-12. Both sexes use the same
# sport and national federation; these are ranking signals, not entry lists.
flag_men={'USA':1,'AUT':2,'MEX':3,'ITA':4,'FRA':5,'SUI':6,'JPN':7,'AUS':8,'ISR':9,'CAN':10,'GER':11,'GBR':12,'PAN':13,'DEN':14,'NZL':15,'ESP':16}
flag_women={'MEX':1,'USA':2,'GBR':3,'CAN':4,'JPN':5,'AUT':6,'ESP':7,'ITA':8,'GER':9,'AUS':10,'FRA':11,'PAN':12,'NZL':13,'SUI':14,'BRA':15,'CZE':16}
flag_rows=[]
for noc in sorted(set(flag_men)|set(flag_women)):
    m=flag_men.get(noc);w=flag_women.get(noc)
    flag_rows.append({'新增运动':'腰旗橄榄球','NOC':noc,'男子排名':m,'女子排名':w,
        '排名信号':(1/(m or 40)+1/(w or 40))/2,'一手来源':flag_source,
        '榜单年度':2025,'核验日期':'2026-11-12',
        '代表团映射':'IFAF Great Britain 对应英国奥运代表团' if noc=='GBR' else '直接同名国家队',
        '适用限制':'2025年度排名；2026世锦赛结果须单独解释；排名不等于参赛资格'})
flag_verified=pd.DataFrame(flag_rows)
flag_verified.to_csv(OUT/'已核验腰旗橄榄球排名.csv',index=False,encoding='utf-8-sig')
cricket_source='https://www.icc-cricket.com/media-releases/india-and-australia-retain-top-positions-in-men-s-and-women-s-t20i-team-rankings-after-annual-update'
# Synchronized official ICC annual-update snapshot, 2026-05-05. Exclude West
# Indies (not an Olympic NOC); England maps to GBR. Scotland is separate in ICC
# and is not merged into England's rating. Ranking is not qualification.
cricket_men={'IND':1,'GBR':2,'AUS':3,'NZL':4,'RSA':5,'PAK':6,'BAN':8,'SRI':9,'AFG':10,'ZIM':11,'IRL':12,'USA':13,'NED':14,'NAM':16}
cricket_women={'AUS':1,'GBR':2,'IND':3,'NZL':4,'RSA':5,'SRI':7,'PAK':8,'IRL':9,'BAN':10,'THA':12,'NED':14,'ZIM':16,'USA':20}
cricket_rows=[]
for noc in sorted(set(cricket_men)|set(cricket_women)):
    m=cricket_men.get(noc);w=cricket_women.get(noc)
    cricket_rows.append({'新增运动':'板球T20','NOC':noc,'男子排名':m,'女子排名':w,
       '排名信号':(1/(m or 40)+1/(w or 40))/2,'一手来源':cricket_source,
       '榜单日期':'2026-05-05','核验日期':'2026-11-12',
       '代表团映射':'ICC England→GBR；Scotland不合并；West Indies排除' if noc=='GBR' else '直接同名国家队',
       '适用限制':'5月同步快照不是12月资格截点；未列球队记为40位保守背景值'})
cricket_verified=pd.DataFrame(cricket_rows)
cricket_verified.to_csv(OUT/'已核验板球T20同步排名.csv',index=False,encoding='utf-8-sig')
wbsc_men_source='https://sports.yahoo.co.jp/official/detail/2026100900003-spnaviow'
wbsc_women_source='https://sports.yahoo.co.jp/official/detail/2026102200002-spnaviow'
# WBSC-authored official-account releases syndicated through SportsNavi.
# Baseball men 2026-10-08; softball women 2026-10-21. Only explicitly listed
# places are captured. Baseball5, women's baseball and men's softball excluded.
baseball_men={'JPN':1,'TPE':2,'USA':3,'KOR':4,'VEN':5,'MEX':6,'PUR':7,'DOM':8,'PAN':9,'AUS':10,'CAN':18}
softball_women={'JPN':1,'USA':2,'PUR':3,'CAN':4,'TPE':5,'MEX':6,'NED':7,'CHN':8,'CZE':9,'ITA':10,'AUS':11,'VEN':12,'GBR':13,'PHI':14,'CUB':15}
wbsc_rows=[]
for noc in sorted(set(baseball_men)|set(softball_women)):
    m=baseball_men.get(noc);w=softball_women.get(noc)
    wbsc_rows.append({'新增运动':'棒球/垒球','NOC':noc,'男子棒球排名':m,'女子垒球排名':w,
        '排名信号':(1/(m or 40)+1/(w or 40))/2,
        '男子一手发布':wbsc_men_source,'女子一手发布':wbsc_women_source,
        '男子榜单日期':'2026-10-08','女子榜单日期':'2026-10-21','核验日期':'2026-11-12',
        '代表团映射':'WBSC代表队与同名奥运NOC对应',
        '适用限制':'WBSC官方机构在SportsNavi官方信息频道署名发布；排名含青少年赛成绩；未列球队以40位为背景值；不代表资格'})
wbsc_verified=pd.DataFrame(wbsc_rows)
wbsc_verified.to_csv(OUT/'已核验棒球垒球分项排名.csv',index=False,encoding='utf-8-sig')
wsf_source='https://wsfworldteams.com/en/pages/final-standings'
# 2024 WSF team championship standings are a national-depth proxy for Olympic
# individual singles, NOT PSA individual rankings. Keep out of the main gate.
wsf_men={'EGY':1,'GBR':2,'FRA':3.5,'SUI':3.5,'IND':5,'HKG':6,'GER':7,'COL':8,'MAS':9,'CAN':11,'ESP':12,'PAK':13,'USA':14,'CZE':15}
wsf_women={'EGY':1,'USA':2,'BEL':3.5,'MAS':3.5,'GBR':5,'HKG':6,'IND':7,'FRA':8,'JPN':9,'CAN':10,'AUS':11,'ESP':13,'GER':14,'IRL':15}
wsf_rows=[]
for noc in sorted(set(wsf_men)|set(wsf_women)):
    m=wsf_men.get(noc);w=wsf_women.get(noc)
    wsf_rows.append({'NOC':noc,'男子团体名次':m,'女子团体名次':w,
       '团队实力代理':(1/(m or 40)+1/(w or 40))/2,'一手来源':wsf_source,
       '赛事年份':2024,'核验日期':'2026-11-12',
       '适用限制':'团体赛每队三人；奥运为个人单打；英格兰成绩映射英国，苏格兰不合并；并列3/4取3.5；仅做敏感性情景'})
wsf_proxy=pd.DataFrame(wsf_rows)
wsf_proxy.to_csv(OUT/'壁球WSF团体赛替代代理.csv',index=False,encoding='utf-8-sig')
status=[
 ('板球T20','ICC 2026-05-05男女T20I同步年度榜',cricket_source,'已逐队录入同日男女榜；英格兰→英国、西印度群岛排除；排名不是2026-12-31资格榜','通过排名核验'),
 ('棒球/垒球','WBSC男子棒球2026-10-08、女子垒球2026-10-21榜',wbsc_men_source+' | '+wbsc_women_source,'由WBSC官方账号署名发布；两小项各取原榜，仅明确列出名次入表；不使用棒球5或女子棒球','通过排名核验'),
 ('腰旗橄榄球','IFAF男子与女子2025年旗橄榜',flag_source,'男女逐队名次、榜单年度与代表团映射已记录；资格与2026世锦赛结果不由排名替代','通过排名核验'),
 ('长曲棍球六人制','World Lacrosse男/女Sixes榜',source,'网页可逐队对照；未确认奥运资格','通过排名核验'),
 ('壁球','PSA男女个人榜','https://www.psasquashtour.com/rankings/','PSA原榜无法在本环境读取；已取得WSF 2024男女团体最终名次，单列敏感性情景，不冒充个人榜','未通过个人榜；有一手团队代理'),
]
pd.DataFrame(status,columns=['新增运动','应使用的官方指标','入口','未通过原因或限制','核验状态']).to_csv(OUT/'五项运动来源门控清单.csv',index=False,encoding='utf-8-sig')

# The old model distributed a 24-medal-unit bonus across all five sports.
# Four sports have sex-/discipline-specific first-party published ranks.
# Allocate one fifth of the original pool to each; do not reallocate the rest.
bonus_budget=24/5
def sport_bonus(frame,column='排名信号'):
    z=frame.set_index('NOC')[column].reindex(old.index).fillna(0)
    assert z.sum()>0
    return z/z.sum()*bonus_budget
bonus=sum((sport_bonus(frame) for frame in [verified,flag_verified,cricket_verified,wbsc_verified]),
          start=pd.Series(0.0,index=old.index))
neutral=old.forecast_total_neutral
ml=old.ml_project_forecast
host=float(old.synthetic_control_host_rate.iloc[0])
pool=old.forecast_total_programme.sum()
raw=.45*neutral+.45*ml+.10*(neutral+bonus)
raw.loc['USA']*=1+host*.55
forecast=raw/raw.sum()*pool
out=old.copy()
out['已核验排名奖励']=bonus
out['审慎集成预测']=forecast
out['审慎集成名次']=forecast.rank(method='min',ascending=False).astype(int)
out['相对旧情景变化']=forecast-old.ensemble_total
out['相对旧情景名次变化']=out['审慎集成名次']-old.ensemble_rank
out.reset_index().sort_values('审慎集成名次').to_csv(OUT/'LA2028审慎来源门控预测榜.csv',index=False,encoding='utf-8-sig')
wsf_bonus=sport_bonus(wsf_proxy,'团队实力代理')
raw_wsf=.45*neutral+.45*ml+.10*(neutral+bonus+wsf_bonus)
raw_wsf.loc['USA']*=1+host*.55
forecast_wsf=raw_wsf/raw_wsf.sum()*pool
wsf_out=pd.DataFrame({'NOC':old.index,'审慎榜':forecast.to_numpy(),
    '加入壁球团队代理后':forecast_wsf.to_numpy(),
    '差值':(forecast_wsf-forecast).to_numpy()})
wsf_out.sort_values('加入壁球团队代理后',ascending=False).to_csv(OUT/'壁球团队代理敏感性榜.csv',index=False,encoding='utf-8-sig')
maxdelta=float(out['相对旧情景变化'].abs().max());maxrank=int(out['相对旧情景名次变化'].abs().max())
md=f'''# 2028新增运动：官方来源门控的审慎预测\n\n五项新增运动原排名输入逐项审计见 `五项运动来源门控清单.csv`。截至2026-11-12，World Lacrosse 男女 **Sixes** 榜、IFAF 男女 **2025年腰旗橄榄球** 榜、[ICC 2026-05-05男女T20I同步年度榜]({cricket_source})可按同项目男女逐队核对。棒垒球和壁球尚未满足同口径输入门槛，旧数值不并入正式审慎预测。\n\n通过门控的三项各分配原24单位奖励池的1/5，剩余2/5不转嫁；原45/45/10权重、主场率与总奖牌池不变。审慎榜相对旧情景单队最多变化 **{maxdelta:.2f}枚**、名次最多变化 **{maxrank}位**。\n\n[World Lacrosse 官方Sixes榜]({source})和[IFAF男女2025年旗橄榜]({flag_source})分别提供逐队排名。IFAF榜不是2026世锦赛赛果；意大利男队和加拿大女队已获得LA28资格，须参照[IFAF官方资格报道](https://www.americanfootball.sport/2026/08/15/italy-and-canada-punch-golden-tickets-to-la28-at-ifaf-world-flag-26)单独解读。\n\n板球[ICC资格规则](https://www.icc-cricket.com/tournaments/womens-t20-worldcup-2026/news/qualifying-pathway-confirmed-for-cricket-s-olympic-games-return)明确，英格兰女队对应英国代表团，西印度群岛不是单一奥运NOC；现已确定澳大利亚、英国、印度、南非女队资格。本模型用5月同日男女榜作竞技信号，不把它冒充2026-12-31最终资格榜；苏格兰也不与英格兰分数合并。\n\n**后续更新门槛**：棒垒球与壁球需取得带日期、逐队数值、URL或PDF哈希的原榜，并写清资格和代表团映射。复算：`python 项目工作区/scripts/verified_rank_forecast.py`。\n'''
md=md.replace('棒垒球和壁球尚未满足同口径输入门槛，旧数值不并入正式审慎预测。',
              'WBSC官方机构于SportsNavi官方信息频道署名发布的男子棒球和女子垒球2026年10月分项榜亦已逐项核对；壁球尚未满足一手来源门槛。')
md=md.replace('可按同项目男女逐队核对。','可按同项目男女逐队核对。')
md=md.replace('通过门控的三项各分配原24单位奖励池的1/5，剩余2/5不转嫁',
              '通过门控的四项各分配原24单位奖励池的1/5，剩余1/5不转嫁')
md=md.replace('棒垒球与壁球需取得带日期、逐队数值、URL或PDF哈希的原榜，并写清资格和代表团映射。',
              '壁球需取得PSA一手个人榜并预先定义个人到代表团的聚合规则；WBSC榜中的未列名次均按保守背景值处理。')
md+='\n[WBSC男子棒球官方署名发布]('+wbsc_men_source+')与[WBSC女子垒球官方署名发布]('+wbsc_women_source+')在SportsNavi官方信息频道刊载；两榜不同日更新，分别对应奥运男子棒球和女子垒球。WBSC排名计入青年赛事，并非成年国家队奥运夺牌概率。\n'
md+='\n壁球另有[WSF官方2024男女团体世锦赛名次]('+wsf_source+')，已制成`壁球WSF团体赛替代代理.csv`和`壁球团队代理敏感性榜.csv`。这不是PSA个人榜，因此只作敏感性情景；加入后单队相对审慎榜的最大变化为 **'+f'{(forecast_wsf-forecast).abs().max():.2f}'+'枚**。\n'
(OUT/'模型说明.md').write_text(md,encoding='utf-8')
top=out.reset_index().sort_values('审慎集成名次').head(15)
assert set(top.NOC).issubset(NOC_ZH), '预测榜有未翻译的代表团代码'
tr=''.join(f'<tr><td title="{r.NOC}">{NOC_ZH[r.NOC]}</td><td>{r.审慎集成预测:.1f}</td><td>{r.审慎集成名次}</td><td>{r.相对旧情景变化:+.2f}</td></tr>' for r in top.itertuples())
page=f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>2028审慎预测｜来源门控</title><style>body{{margin:0;background:#f4f0e8;color:#173a44;font-family:"Microsoft YaHei",sans-serif}}main{{max-width:1050px;margin:auto;padding:6vw 24px 100px}}h1{{font-size:clamp(38px,6vw,76px);line-height:1.1;margin:20px 0}}p{{line-height:1.85;max-width:760px}}.lead{{font-size:20px}}.note{{background:#153e46;color:white;padding:26px;border-radius:22px;margin:28px 0}}.scroll{{overflow-x:auto}}table{{width:100%;border-collapse:collapse;background:white;border-radius:18px;overflow:hidden}}th,td{{padding:14px;text-align:left;border-bottom:1px solid #d9e1df}}a{{color:#126b78}}.links a{{margin-right:20px}}@media(max-width:600px){{th,td{{padding:9px;font-size:12px}}}}</style></head><body><main><small>百年圣火 / 2028预测证据升级</small><h1>先核来源，<br>再谈排名。</h1><p class="lead">审慎榜使用长曲棍球六人制、腰旗橄榄球与T20板球的官方男女排名。棒垒球和壁球的旧奖励保留为情景，不进入正式榜。</p><div class="note">全榜与旧情景相比，单队最多变化 {maxdelta:.2f} 枚，名次最多变化 {maxrank} 位。排名本身不代表奥运参赛资格。</div><h2>审慎预测 · 前15代表团</h2><div class="scroll"><table><tr><th>代表团代码</th><th>预测奖牌</th><th>名次</th><th>较旧情景</th></tr>{tr}</table></div><p class="links"><a href="五项运动来源门控清单.csv">五项来源核验</a><a href="已核验六人制排名.csv">六人制排名</a><a href="已核验腰旗橄榄球排名.csv">旗橄排名</a><a href="已核验板球T20同步排名.csv">板球排名</a><a href="LA2028审慎来源门控预测榜.csv">完整预测榜</a><a href="模型说明.md">模型说明</a></p><p><a href="../12_新增运动端到端类比回放/index.html">继续看历史类比回放 →</a></p></main></body></html>'''
page=page.replace('棒垒球和壁球的旧奖励保留为情景，不进入正式榜。','壁球的旧奖励保留为情景，不进入正式榜；棒垒球使用WBSC分项榜。')
page=page.replace('<th>代表团代码</th>','<th>代表团</th>')
page=page.replace('<a href="LA2028审慎来源门控预测榜.csv">','<a href="已核验棒球垒球分项排名.csv">棒垒球排名</a><a href="LA2028审慎来源门控预测榜.csv">')
(OUT/'index.html').write_text(page,encoding='utf-8')
print('verified sports: 4/5; max medal delta',round(maxdelta,3),'max rank delta',maxrank)
