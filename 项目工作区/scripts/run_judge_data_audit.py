'''Run the raw audit in isolation and reconcile the published evidence.'''
import argparse
import hashlib
from html import escape
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

from bs4 import BeautifulSoup
import pandas as pd
import pymupdf

ROOT = Path(__file__).resolve().parents[2]
DELIVERY = ROOT/'交付文件'
TASK1 = DELIVERY/'任务一_数据体检'
TASK2 = DELIVERY/'任务二_百年全景'
TASK3 = DELIVERY/'任务三_专题深挖/S2_口径的魔力'
VERIFY = TASK3/'08_逐项外部核验'
EVIDENCE = VERIFY/'IOC现行结果补证进度_20261121'
FINAL = DELIVERY/'最终提交材料'

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--csv',type=Path,default=ROOT/'资料文件/原始资料/olympics_dataset.csv')
parser.add_argument('--out',type=Path,default=TASK1/'04_质量检查结果/评审复跑验收')
args=parser.parse_args()
source=args.csv.resolve(strict=True)
out=args.out.resolve()
out.mkdir(parents=True,exist_ok=True)
raw=pd.read_csv(source)
with tempfile.TemporaryDirectory() as scratch:
    work=Path(scratch)
    code=work/'03_复现代码'
    code.mkdir()
    env=dict(os.environ,OLYMPICS_CSV=str(source))
    for script in ['audit.py','prepare.py']:
        shutil.copyfile(TASK1/'03_复现代码'/script,code/script)
        subprocess.run([sys.executable,str(code/script)],cwd=work,env=env,check=True)
    audit=json.loads((work/'04_质量检查结果/audit.json').read_text(encoding='utf-8'))
    flags=pd.read_csv(work/'99_运行生成/olympics_flagged.csv.gz')
    names=['sport_mapping.csv','event_quality_by_year.csv','edition_main.csv','edition_include_1906.csv','duplicate_by_year.csv']
    for name in names:
        shutil.copyfile(work/'99_运行生成'/name,out/name)
    shutil.copyfile(work/'04_质量检查结果/audit.json',out/'audit.json')
assert flags[raw.columns].equals(raw) and len(raw)==252565
assert audit['sha256']==hashlib.sha256(source.read_bytes()).hexdigest()
main=flags[flags.include_main]
medals=flags[flags.is_medal]
group=medals.groupby(['Year','Event','Medal']).size()
one_color=medals.groupby(['Year','Event']).Medal.nunique().eq(1)
cross=flags[flags.Year.eq(2024)&flags.Sport.str.contains(',')]
assert len(cross)==89 and not flags.sport_family.eq('Cross-sport unresolved').any()
assert len(medals)==38818 and len(main[main.is_medal])==38360 and audit['medal_rows_1906']==458
assert int(group.gt(1).sum())==5080 and int(one_color.sum())==34
assert not main.Year.eq(1906).any()
assert len(audit['cities_1956'])==2 and audit['id_multiple_names']==12883
assert audit['names_spanning_over_40_years']==670
counts=[]
for year in [2020,2024]:
    part=raw[raw.Year.eq(year)]
    count=part.Event.str.fullmatch(r'Men|Women|Men Team|Women Team|Relay Only Athlete',case=False,na=False).sum()
    assert count=={2020:2862,2024:3210}[year]
    counts.append(f'{year}：{count:,}/{len(part):,} 行')
teams=raw.groupby('Year').NOC.nunique()
assert (teams[1980],teams[1984])==(80,140)
sections=[
 ('Q1','Year / NOC / Medal',f'原表 {len(medals):,} 获奖行，主分析 {int(main.is_medal.sum()):,} 行','双口径分列，官方小项另接逐项表','edition_main.csv','双口径榜、西班牙名次重排'),
 ('Q2','Sport / Event',f'{len(cross)} 条巴黎多标签记录已映射，跨大类待解析为 0','按运动家族映射，跨大类由 Event 判别','sport_mapping.csv','运动大类趋势及项目贡献'),
 ('Q3','Year / Event','；'.join(counts),'严格五词表单列，2020 小项趋势空缺，2024 补官方结构','event_quality_by_year.csv','小项增长与女子专属项目占比'),
 ('Q4','player_id / Name',f'{audit["id_multiple_names"]:,} 个 ID 对应多个姓名；{audit["names_spanning_over_40_years"]:,} 个同名跨度超过40年','保留原始身份字段，避免把姓名和 ID 直接当作跨届人物键','audit.json','个人榜与运动员生涯结论'),
 ('Q5','Year / City / NOC',f'1906 有 458 获奖行；1956 有 {len(audit["cities_1956"])} 个城市；1980/1984 代表团 {teams[1980]}/{teams[1984]}','主分析排除 1906；双城留档，政体按原 NOC 分列，缺席留空','edition_include_1906.csv','百年趋势、代表团兴衰'),
 ('Q6','Year / Event / Medal',f'{group.gt(1).sum():,} 组同色多行，{one_color.sum()} 项只见一种奖牌；重复候选超额 {int(flags.duplicate_excess.sum()):,} 行','保留多行与并列，重复仅作候选和敏感性处理，缺色单独核对','duplicate_by_year.csv','官方小项榜、运动员行榜与历史复算'),
]
checks=pd.DataFrame(sections,columns=['赛题','原字段','触发读数','处理规则','输出','受影响结论'])
checks.to_csv(out/'Q1至Q6验收.csv',index=False,encoding='utf-8-sig')
official=pd.read_csv(TASK1/'02_交付数据/2024官方329小项奖牌表.csv')
assert len(official)==329 and official.event_id.is_unique
paris=main[main.Year.eq(2024)]
winners=paris[paris.is_medal]
ratios=[(int(paris.Sex.eq('F').sum()),len(paris)),(int(winners.Sex.eq('F').sum()),len(winners)),
        (int(official.gender.eq('W').sum()),len(official))]
assert ratios==[(7312,14892),(1147,2281),(151,329)]
c=pd.read_csv(TASK2/'02_数据表/C_女性参与获奖与小项.csv',index_col=0)
assert all(abs(x/y-rate)<1e-12 for (x,y),rate in zip(ratios,c.loc[2024,['participation_share','medal_share','women_only_event_share']]))
d=pd.read_csv(TASK2/'02_数据表/D_逐届小项数量.csv',index_col=0)
assert 2020 not in d.index and d.loc[2024,'event_units']==329
r=pd.read_csv(TASK3/'02_数据表/S2_2024双口径完整排名.csv').set_index('NOC').loc['ESP']
assert (r.official_rank,r.row_rank,r.Gold_official,r.Gold_rows)==(15,5,5,40)
podium = pd.DataFrame({
    color: official[color.lower()+'_country_code'].fillna('').str.split('|').explode().str.strip().value_counts()
    for color in ['Gold','Silver','Bronze']
}).drop(index='',errors='ignore').fillna(0)
athletes = winners.groupby(['NOC','Medal']).size().unstack(fill_value=0).reindex(columns=['Gold','Silver','Bronze'],fill_value=0)
for counts,expected_gold,expected_rank in [(podium,5,15),(athletes,40,5)]:
    spanish=tuple(counts.loc['ESP'])
    assert spanish[0]==expected_gold
    assert 1+sum(other>spanish for other in counts.itertuples(index=False,name=None))==expected_rank

def compact(text):
    return re.sub(r'\s+','',text)

# Verify public HTML by text, and record named PDF pages without exporting student data.
def html_text(path):
    return compact(BeautifulSoup(path.read_text(encoding='utf-8'),'html.parser').get_text())
views=TASK2/'11_四视角独立交付/四视角核心图复核.html'
spain=TASK3/'西班牙双口径案例.html'
assert all(t in html_text(views) for t in ['7,312/14,892','1,147/2,281','151/329','49.1%','50.3%','45.9%','2020','2024'])
assert '从第15升到第5' in html_text(spain)
with pymupdf.open(FINAL/'数说奥运_晓组织_正式答卷.pdf') as pdf:
    assert len(pdf)==20
    pages=[compact(p.get_text()) for p in pdf]
    assert all(t in pages[5] for t in ['329','49.1%','50.3%','45.9%'])
    assert '2020留空' in pages[7] and '329' in pages[7]
    assert any('西班牙' in p and re.search(r'第15.{0,55}第5',p) for p in pages)
crosswalk=[
 ('巴黎官方小项','329 项','2024官方329小项奖牌表.csv','答卷第 6、8 页；四视角复核页 C/D'),
 ('女性三个分母','；'.join(f'{x:,}/{y:,} = {x/y:.1%}' for x,y in ratios),'C_女性参与获奖与小项.csv','答卷第 6 页核对比例；四视角复核页 C 核对比例和分子分母'),
 ('西班牙双口径','第 15 → 第 5；5 枚 → 40 行','S2_2024双口径完整排名.csv','答卷逐文核对名次；西班牙案例页'),
 ('2020 事件结构','小项曲线留空','D_逐届小项数量.csv','答卷第 8 页；四视角复核页 D'),
]
pd.DataFrame(crosswalk,columns=['关键读数','复算值','下载表','交付核对']).to_csv(out/'关键数字跨交付核对.csv',index=False,encoding='utf-8-sig')

# Weight-class regression uses the already reviewed two mappings and hashes.
subprocess.run([sys.executable,str(ROOT/'项目工作区/scripts/qa_weightlifting_evidence.py')],check=True)
fix=VERIFY/'后续补证_20261121'
weight=pd.read_csv(fix/'两项配对更正记录.csv').set_index('weight_kg')
assert weight.loc[63,'corrected_gold']=='CAN' and weight.loc[75,'corrected_gold']=='ESP'
impact=pd.read_csv(fix/'四组复算差异核验.csv')
assert impact['numeric_conclusion_unchanged'].all()
# Isolate the Finnish correction from all other medal changes.
f=pd.read_csv(TASK3/'02_数据表/S2_2008历史小项代理表.csv',keep_default_na=False).set_index('Event')
cases=pd.read_csv(EVIDENCE/'优先分歧逐项复核.csv',keep_default_na=False)
colors=['Gold','Silver','Bronze']
for case in cases[cases.Year.eq(2008)].itertuples(index=False):
    values=case.原金银铜.split('/')
    f.loc[case.Event,colors]=['' if x=='空' else x for x in values]
def ranks(frame):
    counts=pd.DataFrame({color:frame[color].str.split('|',regex=False).explode().str.strip().value_counts() for color in colors}).drop(index='',errors='ignore').fillna(0)
    keys=list(counts[colors].itertuples(index=False,name=None))
    return {noc:1+sum(better>key for better in keys) for noc,key in zip(counts.index,keys)}
before=ranks(f)
f.loc["Shooting Women's Trap",'Gold']='FIN'
after=ranks(f)
affected=sum(before.get(n)!=after.get(n) for n in before.keys()|after.keys())
assert (before['FIN'],after['FIN'],affected)==(60,44,20)
samples=[
    ('伦敦女子举重 63kg／75kg','两个小项互配','63kg 加拿大金；75kg 西班牙金','性别和公斤级硬约束；原件哈希及四组差异表','四组既有隔离复算的数值结论均保持'),
    ('北京女子飞碟多向','旧存档金牌空缺','芬兰金牌','ISSF 赛果；其他小项固定',f'芬兰 {before["FIN"]}→{after["FIN"]}，{affected} 队名次变化'),
]
pd.DataFrame(samples,columns=['案例','旧值','核对值','验收依据','复算影响']).to_csv(out/'两项修订验收.csv',index=False,encoding='utf-8-sig')
federations=len(pd.read_csv(EVIDENCE/'协会一手逐项交叉核验.csv'))
scope=len(pd.read_csv(VERIFY/'历史910项来源覆盖总表.csv'))
assert (federations,len(cases),scope)==(59,7,910)
res={'Q1至Q6':'通过','原始CSV_sha256':audit['sha256'],'行数':len(raw),'协会一手交叉核验':federations,'来源分歧已补证':len(cases),'现行IOC全量任务':scope,'现行IOC全量状态':'待完成'}
(out/'验收结果.json').write_text(json.dumps(res,ensure_ascii=False,indent=2),encoding='utf-8')
def table(frame):
    def cells(values,tag):
        return ''.join(f'<{tag}>{escape(str(value))}</{tag}>' for value in values)
    head=cells(frame.columns,'th')
    rows=''.join('<tr>'+cells(row,'td')+'</tr>' for row in frame.itertuples(index=False,name=None))
    return f'<div class="table" tabindex="0"><table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>'

shortcut='../../../'
refs=[
 ('63／75 公斤配对及隔离复算','任务三_专题深挖/S2_口径的魔力/08_逐项外部核验/后续补证_20261121/index.html'),
 ('芬兰补录的逐队名次','任务三_专题深挖/S2_口径的魔力/08_逐项外部核验/IOC现行结果补证进度_20261121/优先分歧复核与复算.html'),
 ('59 项协会交叉核验','任务三_专题深挖/S2_口径的魔力/08_逐项外部核验/IOC现行结果补证进度_20261121/协会一手逐项交叉核验.html'),
 ('910 项现行 IOC 核验进度','任务三_专题深挖/S2_口径的魔力/08_逐项外部核验/IOC现行结果补证进度_20261121/index.html'),
]
published=TASK1/'04_质量检查结果/评审复跑验收'
links=' · '.join(f'<a href="{shortcut+uri}">{label}</a>' for label,uri in refs) if out==published else ''
content=f"""<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>赛题数据复跑验收</title><style>:root{{color-scheme:light dark}}main{{max-width:78rem;margin:auto;padding:clamp(16px,4vw,56px);font:16px/1.7 system-ui}}.table{{overflow:auto}}table{{border-collapse:collapse;width:100%;min-width:42rem}}td,th{{padding:.65rem;text-align:left;border-bottom:1px solid #81949288}}code{{overflow-wrap:anywhere}}a{{text-underline-offset:4px}}</style>
<main><h1>赛题数据复跑验收</h1>
<p>以赛题原始 CSV 的 {len(raw):,} 条记录运行原审计和归一脚本。六项验收全部通过。原始字段与复跑记录逐行一致。原件 SHA-256 见下载 JSON。</p>
<p>安装 pandas、beautifulsoup4、PyMuPDF 后，从仓库根目录运行 <code>py 项目工作区/scripts/run_judge_data_audit.py --csv 路径/olympics_dataset.csv</code>。使用默认路径时可省略参数。</p>
<h2>Q1–Q6 原字段与处理</h2>{table(checks)}
<p>输出列里的诊断文件由复跑生成。严格五词检测用于复核泛化规模，归一脚本同时保留范围更宽的上下文风险标记。</p>
<h2>关键数字跨交付核对</h2>{table(pd.DataFrame(crosswalk,columns=['关键读数','复算值','下载表','交付核对']))}
<h2>两项修订验收</h2>{table(pd.DataFrame(samples,columns=['案例','旧值','核对值','验收依据','复算影响']))}<p>{links}</p>
<p>59 项是单项协会的一手交叉证据。7 项是 555 项优先清单里旧存档与 Olympedia 的全部分歧。910 项是历史全量逐项核验范围，现行 IOC 核验待完成。这三个数字描述不同证据范围。</p>
<p><a href="Q1至Q6验收.csv" download>下载 Q1–Q6 CSV</a> · <a href="关键数字跨交付核对.csv" download>下载关键数字核对</a> · <a href="两项修订验收.csv" download>下载案例验收</a> · <a href="验收结果.json" download>下载机器可读验收记录</a></p>
</main></html>"""
(out/'index.html').write_text(content,encoding='utf-8')
print('Q1–Q6, cross-delivery figures and two revision checks passed.')
