"""Event-by-event comparison against an archived scrape of Olympics.com results.

The archive is a 2023 third-party capture of the IOC site, not a current IOC export.
Never relabel unmatched or disputed events as verified current official results.
"""
from pathlib import Path
import hashlib,json,re,urllib.request
import numpy as np
import pandas as pd
import pyreadr
from scipy.optimize import linear_sum_assignment
from rapidfuzz import fuzz

ROOT=Path(__file__).resolve().parents[2]
ARCH=ROOT/'资料文件'/'外部核验'/'olympicscom_抓取存档'
OUT=ROOT/'交付文件'/'任务三_专题深挖'/'S2_口径的魔力'/'08_逐项外部核验'
OUT.mkdir(parents=True,exist_ok=True);ARCH.mkdir(parents=True,exist_ok=True)
URL='https://raw.githubusercontent.com/numbats/olympics/ab2d03770c8b435fa7e452a5a1ddfc933433299c/data/summer_games.rda'
file=ARCH/'summer_games.rda'
if not file.exists():file.write_bytes(urllib.request.urlopen(URL,timeout=40).read())
sha=hashlib.sha256(file.read_bytes()).hexdigest()
assert sha=='d31351e057198744b40754e63e9189a86487424c55766751f2a09f0ee3f8b3eb'
archive=pyreadr.read_r(str(file))['summer_games']
game={2008:'beijing-2008',2012:'london-2012',2016:'rio-2016'}
sport_map={'marathon-swimming':'Swimming','gymnastics-artistic':'Gymnastics','gymnastics-rhythmic':'Rhythmic Gymnastics','trampoline':'Trampolining','beach-volleyball':'Beach Volleyball','rugby':'Rugby Sevens'}
country_to_noc=dict(zip(
    ['United States of America','Germany','Great Britain','Australia',"People's Republic of China",'France','Russian Federation','Japan','Netherlands','Italy','Canada','Republic of Korea','Spain','Brazil','Denmark','Jamaica','New Zealand','Hungary','Serbia','Romania','Poland','Argentina','Sweden','Ukraine','Belarus','Croatia','Switzerland','Norway','Nigeria','Bahamas','Trinidad and Tobago','South Africa','Belgium','Slovakia','Czech Republic','Singapore','Greece','Fiji','Estonia','Bulgaria','Chinese Taipei','Finland','Montenegro','Mexico','Saudi Arabia','Ireland','Iceland','Cuba'],
    ['USA','GER','GBR','AUS','CHN','FRA','RUS','JPN','NED','ITA','CAN','KOR','ESP','BRA','DEN','JAM','NZL','HUN','SRB','ROU','POL','ARG','SWE','UKR','BLR','CRO','SUI','NOR','NGR','BAH','TTO','RSA','BEL','SVK','CZE','SGP','GRE','FIJ','EST','BUL','TPE','FIN','MNE','MEX','KSA','IRL','ISL','CUB']))
def sport_name(s):
    if s in sport_map:return sport_map[s]
    if s.startswith('equestrian-'):return 'Equestrianism'
    if s.startswith('cycling-'):return 'Cycling'
    if s.startswith('canoe-'):return 'Canoeing'
    return s.replace('-',' ').title()

def codes(x):
    if pd.isna(x):return set()
    return {v.strip().upper() for v in str(x).replace(',','|').split('|') if v.strip() and v.strip().lower()!='nan'}

def norm(x):
    s=str(x).lower().replace("women's",'women').replace("men's",'men')
    s=re.sub(r'\bmetres\b|\bmeters\b','m',s)
    s=re.sub(r'\bkilometres\b|\bkilometers\b','km',s)
    s=s.replace('synchronised','synchronized').replace('individual','individual')
    return re.sub(r'[^a-z0-9]+',' ',s).strip()

def sex(x):
    s=norm(x).split()
    if 'women' in s:return 'women'
    if 'men' in s:return 'men'
    return 'mixed'

proxy_dir=ROOT/'交付文件'/'任务三_专题深挖'/'S2_口径的魔力'/'02_数据表'
all_rows=[];unmatched=[]
for year,slug in game.items():
    proxy=pd.read_csv(proxy_dir/f'S2_{year}历史小项代理表.csv').fillna('')
    z=archive[archive.game.eq(slug)&archive['rank'].isin(['G','S','B'])].copy()
    z['Sport']=z.sport.map(sport_name)
    z['team']=z.team.map(lambda x:country_to_noc.get(x,x))
    z['source_url']='https://www.olympics.com/en/olympic-games/'+slug+'/results/'+z.sport+'/'+z.event
    source=z.groupby(['Sport','sport','event','source_url'],as_index=False).apply(lambda g:pd.Series({k:'|'.join(sorted(set(g[g['rank'].eq(v)].team.dropna().astype(str)))) for k,v in [('Gold','G'),('Silver','S'),('Bronze','B')]}),include_groups=False).reset_index(drop=True)
    assert not source.duplicated(['sport','event']).any()
    for sp,p in proxy.groupby('Sport'):
        s=source[source.Sport.eq(sp)]
        if s.empty:
            for _,r in p.iterrows():unmatched.append({'Year':year,'Sport':sp,'Event':r.Event,'reason':'外部存档无此运动'})
            continue
        pp=p.reset_index(drop=True);ss=s.reset_index(drop=True)
        scores=np.zeros((len(pp),len(ss)))
        for i,a in pp.iterrows():
            for j,b in ss.iterrows():
                same=[codes(a[m])==codes(b[m]) for m in ['Gold','Silver','Bronze']]
                overlap=sum(len(codes(a[m])&codes(b[m])) for m in ['Gold','Silver','Bronze'])
                medal=28*same[0]+13*same[1]+9*same[2]+2*overlap
                left=norm(a.Event).replace(norm(sp),'').strip()
                right=norm(b.event)
                name=90*fuzz.token_set_ratio(left,right)/100
                if sex(a.Event)!=sex(b.event):name-=100
                scores[i,j]=medal+name
        ri,ci=linear_sum_assignment(-scores)
        assigned=set(ri)
        for i,j in zip(ri,ci):
            a=pp.iloc[i];b=ss.iloc[j]
            checks={m:codes(a[m])==codes(b[m]) for m in ['Gold','Silver','Bronze']}
            status='三色一致' if all(checks.values()) else ('仅金牌一致' if checks['Gold'] else '金牌不一致')
            if scores[i,j]<55:status='匹配待人工复核'
            all_rows.append({'Year':year,'Sport':sp,'Event_proxy':a.Event,'Sport_olympics':b.sport,'Event_olympics':b.event,
                             'Gold_proxy':a.Gold,'Silver_proxy':a.Silver,'Bronze_proxy':a.Bronze,
                             'Gold_archive':b.Gold,'Silver_archive':b.Silver,'Bronze_archive':b.Bronze,
                             'gold_match':checks['Gold'],'silver_match':checks['Silver'],'bronze_match':checks['Bronze'],
                             'match_score':scores[i,j],'status':status,'olympics_event_url':b.source_url,
                             'source_capture':'Olympics.com经第三方抓取，仓库存档更新于2023-02-25'})
        for i,a in pp.iterrows():
            if i not in assigned:unmatched.append({'Year':year,'Sport':sp,'Event':a.Event,'reason':'外部存档缺项'})

result=pd.DataFrame(all_rows).sort_values(['Year','Sport','Event_proxy'])
result.to_csv(OUT/'逐小项三色对照.csv',index=False,encoding='utf-8-sig')
issues=result[(result.status!='三色一致')].copy()
issues['复核队列']=issues.apply(lambda r: '优先复核配对' if r.status=='匹配待人工复核' else
                             ('存档奖牌字段缺失' if any(not str(r[f'{m}_archive']).strip() for m in ['Gold','Silver','Bronze']) else
                              ('金牌冲突_查重分配' if not r.gold_match else '银铜冲突_查重分配')),axis=1)
issues[['Year','Sport','Event_proxy','Event_olympics','Gold_proxy','Gold_archive','Silver_proxy','Silver_archive','Bronze_proxy','Bronze_archive','复核队列','olympics_event_url']].to_csv(OUT/'待复核差异清单.csv',index=False,encoding='utf-8-sig')
missing=pd.DataFrame(unmatched).sort_values(['Year','Sport','Event'])
missing.to_csv(OUT/'未匹配小项.csv',index=False,encoding='utf-8-sig')
summary=[]
for year,g in result.groupby('Year'):
    summary.append({'Year':year,'proxy_events':len(pd.read_csv(proxy_dir/f'S2_{year}历史小项代理表.csv')),
                    'archived_events':len(g),'unmatched':len(missing[missing.Year.eq(year)]),
                    'three_medal_match':int(g.status.eq('三色一致').sum()),
                    'gold_match':int(g.gold_match.sum()),'gold_mismatch':int((~g.gold_match).sum()),
                    'manual_review':int(g.status.eq('匹配待人工复核').sum())})
summ=pd.DataFrame(summary);summ.to_csv(OUT/'逐届核验覆盖.csv',index=False,encoding='utf-8-sig')
meta={'source_url':URL,'source_project':'https://github.com/numbats/olympics','source_method':'https://numbats.github.io/olympics/reference/scrape.html','commit':'ab2d03770c8b435fa7e452a5a1ddfc933433299c','archive_last_commit_utc':'2023-02-25T02:06:34Z','sha256':sha,'scope':'Olympics.com 2023 third-party scrape, not 2026 live official results','matching':'sport-specific one-to-one assignment by medal-country sets, name similarity and gender; nonmatches not forced to verified'}
(OUT/'来源与方法.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8')
md='# 2008、2012、2016逐小项外部核验\n\n'
md+='本次把原主数据的逐小项代理，与 `numbats/olympics` 研究项目从 Olympics.com 抓取的结果存档逐项对照。存档文件的最后更新为2023-02-25；它是**Olympics.com 来源的第三方历史快照**，不是IOC在2026年导出的当前官方表。奖牌后续重分配可能使当前官网与快照不同。\n\n'
md+='| 届次 | 代理小项 | 存档覆盖 | 三色一致 | 金牌一致 | 金牌不一致 | 未覆盖 |\n|---|---:|---:|---:|---:|---:|---:|\n'
for r in summ.itertuples():md+=f'| {r.Year} | {r.proxy_events} | {r.archived_events} | {r.three_medal_match} | {r.gold_match} | {r.gold_mismatch} | {r.unmatched} |\n'
md+='\n匹配先按运动限定，再用奖牌代表团集合、项目名称和性别做一对一分配。每项的原值、存档值、比分和官方项目URL见 `逐小项三色对照.csv`。不一致和低分配对不能自动替换：可能来自主数据错误、存档漏项、赛事名称映射或IOC后续重分配。`未匹配小项.csv` 明确保留缺口。\n\n'
md+='因此本次完成**独立逐项对照**，并没有完成对2026年现行IOC页面全部910项的实时核验。作品不能再只写“总量核对”，但也不应把存档直接改名为当前官方真值。复算：`python 项目工作区/scripts/historical_ioc_event_audit.py`，需 `pyreadr` 和 `rapidfuzz`。\n'
md+='\n**差异复核优先级**：`待复核差异清单.csv` 把低分配对、存档奖牌字段缺失、金牌冲突和银铜冲突分开。比如2008男子100米的存档金牌字段为空，不能由此推断原数据的牙买加金牌错误。奖牌重分配需用IOC决议或现行赛事页逐案确认，不能仅凭第三方快照作自动修正。原有文件名“历史小项代理表”沿用旧流程，来源等级实际是**主数据去重代理**；本说明及结果列覆盖其命名含义。\n'
(OUT/'核验说明.md').write_text(md,encoding='utf-8')
print(summ.to_string(index=False))

