"""Build seven additional, offline Task 3 stories from the audited rows."""
from pathlib import Path
from html import escape
import json
import pandas as pd
from task2_localization import NOC_ZH, SPORT_ZH

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / '交付文件' / '任务三_专题深挖'
DATA = ROOT / '项目工作区' / 'outputs' / 'olympics_flagged.csv.gz'
d = pd.read_csv(DATA, low_memory=False)
d = d[d.include_main.eq(True)].copy()
d['Year'] = pd.to_numeric(d.Year, errors='coerce').astype(int)
med = d[d.is_medal.eq(True)].copy()
gold = d[d.Medal.eq('Gold')].copy()

def series(frame, group, value='source_row', n=12):
    x = frame.groupby(group)[value].count().sort_values(ascending=False).head(n)
    return [{'label':str(k),'value':int(v)} for k,v in x.items()]

def noc_label(code):
    return NOC_ZH.get(code,code)

def sport_label(name):
    return SPORT_ZH.get(name,name)

topics = []
def add(code, slug, title, kicker, intro, insight, rows, method, caveat, colors, layout, unit):
    topics.append(dict(code=code,slug=slug,title=title,kicker=kicker,intro=intro,
      insight=insight,rows=rows,method=method,caveat=caveat,colors=colors,layout=layout,unit=unit))

# S3: describe the 1980/1984 boycott trace and changing historical NOCs.
participation = d.groupby('Year').NOC.nunique()
geo = [{'label':str(y),'value':int(participation.get(y,0))} for y in [1972,1976,1980,1984,1988,1992,2000,2020,2024]]
add('S3','S3_地缘政治的投影','缺席的代表团','冷战档案',
    '1980 与 1984 两届的参赛规模突然变化。图中展示的是数据集里实际出现的代表团数量，而不是政治事件的完整名单。',
    '抵制潮留下了可见的参赛缺口，但仅凭总量无法判断单个国家为什么缺席。苏联、独联体联队、俄罗斯、俄罗斯奥委会代表队和个人中立运动员也不能直接合并成同一支队伍。',
    geo,'按届次去重代表团代码；对 1980、1984 及前后届做描述性比较。历史代表团身份保留原码。',
    '代表团数量是数据集覆盖值；抵制原因和代表团身份须结合外部史料确认。1906 排除，1956 双城按一届统计。',
    ('#171f38','#d8b671','#eef0f7'),'archive','代表团')
lineage = d[d.NOC.isin(['URS','EUN','RUS','ROC','AIN','GDR','FRG','GER'])].groupby('NOC').agg(first=('Year','min'),last=('Year','max'),rows=('source_row','count'))
topics[-1]['evidence'] = [('1980 / 1984', f"{int(participation.get(1980,0))} / {int(participation.get(1984,0))} 个代表团出现在数据中；对照前后届，先确认规模变化，再查事件背景。"),
 ('历史身份', ' / '.join(f'{noc_label(k)} {int(v.first)}—{int(v.last)}' for k,v in lineage.iterrows())+'。原始数据仍保留代表团代码，不宜直接加总成一个“国家”。')]

# S4: small delegation breakthroughs, separating medal rows and entrants.
small = d[d.NOC.isin(['HKG','TPE','SGP','FIJ','BER','JOR','KOS'])]
sm = small.groupby('NOC').agg(records=('source_row','count'))
sm['medal_rows'] = med[med.NOC.isin(sm.index)].groupby('NOC').size().reindex(sm.index).fillna(0).astype(int)
small_rows = [{'label':noc_label(k),'code':k,'value':int(v)} for k,v in sm.medal_rows.sort_values(ascending=False).items()]
add('S4','S4_小代表团的大突破','小队伍的大突破','海岛与新星',
    '把镜头从奖牌总榜移开，看看部分规模较小或历史较短的代表团。条形图先展示整段历史的获奖运动员记录。',
    '小代表团的突破更适合结合参赛人数、年份和优势项目看，不能仅用累计奖牌行数判定“效率”。点击条形可查看该代表团的参赛记录数。',
    [{**r,'detail':f"原始代码 {r['code']} · {int(sm.loc[r['code'],'records'])} 条参赛行"} for r in small_rows],
    '选取 HKG、TPE、SGP、FIJ、BER、JOR、KOS；分子为奖牌运动员行，分母提示为全部参赛行。',
    '样本是分析案例而非全部小代表团；团体项目放大奖牌行数，不能当作官方奖牌数。',
    ('#143c3a','#ffb769','#e8f5ef'),'islands','获奖行')
small_sport = med[med.NOC.isin(sm.index)].groupby(['NOC','sport_family']).size().sort_values(ascending=False)
topics[-1]['evidence'] = [('突破年份', '；'.join(f'{noc_label(noc)}：{int(g.groupby("Year").size().idxmax())} 年有 {int(g.groupby("Year").size().max())} 条获奖行' for noc,g in med[med.NOC.isin(['HKG','TPE','SGP'])].groupby('NOC'))),
 ('优势项目', '；'.join(f'{noc_label(noc)}：{sport_label(fam)}（{int(v)} 行）' for (noc,fam),v in small_sport.groupby(level=0).head(1).items()))]

# S5: expansion is partly a change of opportunity, not just national strength.
year_rows = d.groupby('Year').agg(athlete_rows=('source_row','count'),nocs=('NOC','nunique'))
year_medals = med.groupby('Year').size()
growth = [{'label':str(y),'value':int(year_medals.get(y,0)),
           'detail':f"{int(year_rows.loc[y,'athlete_rows'])} 参赛行 · {int(year_rows.loc[y,'nocs'])} 个 NOC"}
          for y in year_rows.index if y != 1906]
add('S5','S5_奖牌的通货膨胀','奖牌变多了，机会也变了','百年刻度',
    '百年间奖牌运动员行显著增加。若只看累计数，早期和现代的代表团并不站在同一条起跑线上。',
    '奖牌行扩张既受小项数量影响，也受团体人数、参赛规模和数据记录方式影响。点击年份可同时查看参赛行与 NOC 数。',
    growth,'按届次统计获奖运动员行，并附参赛运动员行和唯一 NOC 数；展示完整时间序列。',
    '图中不是官方小项奖牌数。2020/2024 源数据字段变动，跨时代比较须回看任务一口径说明；1906 排除。',
    ('#3b2436','#f1a060','#fff4e8'),'timeline','获奖行')
topics[-1]['evidence'] = [('首尾对照', f"1896 年 {int(year_medals.get(1896,0))} 条获奖行、{int(participation.get(1896,0))} 个 NOC；2024 年 {int(year_medals.get(2024,0))} 条获奖行、{int(participation.get(2024,0))} 个 NOC。"),
 ('可比性', '奖牌运动员行同时受小项数、团体成员数和源数据覆盖影响。跨届比较最好增加每届项目机会与参赛规模作分母。')]

# S6: name-quality-aware evidence instead of a false all-time individual ranking.
name_gold = gold.groupby('Name').agg(rows=('source_row','count'),years=('Year','nunique'),first=('Year','min'),last=('Year','max')).sort_values('rows',ascending=False)
name_zh = {
 'Michael Ii':'姓名截断记录一','Charles Jr.':'疑似同名混合记录一',
 'Paavo Nurmi':'帕沃·努尔米','Larysa (diriy-)':'姓名残缺记录二',
 'Mark Spitz':'马克·施皮茨','John Jr.':'疑似同名混合记录二',
 'Caeleb Dressel':'凯莱布·德雷塞尔','Frederick Lewis':'弗雷德里克·刘易斯',
 'Matthew Biondi':'马特·比昂迪','Raymond Ewry':'雷·尤里',
 'Usain Bolt':'尤塞恩·博尔特','Sawao Kato':'加藤泽男',
}
legend_rows = [{'label':name_zh.get(str(k),'待核验姓名记录'), 'raw_name':str(k),
                'value':int(v.rows),'detail':f"{int(v.first)}—{int(v.last)} · {int(v.years)} 届；原始姓名见分析数据，身份待核验"}
               for k,v in name_gold.head(12).iterrows()]
add('S6','S6_王者与传奇','名字背后的传奇','人物鉴证室',
    '原始表里有传奇运动员的姓名被截断，运动员编号也不能稳定表示同一人。先看“姓名对应的金牌行”候选，再决定哪些人物值得人工核验。',
    '同名记录高，并不必然等于同一人的金牌多。一个跨越异常长年代的名字可能合并了不同运动员；真正的个人榜需要外部权威身份核验。',
    legend_rows,'按原始姓名字段聚合金牌运动员行，附首次与末次年份、涉及届次；仅作为核验候选。',
    '这不是个人历史金牌榜。原始姓名和运动员编号均存在实体识别问题；团体项目同一人的多小项记录可重复。',
    ('#2e1e28','#d4a447','#f7efe7'),'portrait','金牌行')
suspect = name_gold.loc['Michael Ii'] if 'Michael Ii' in name_gold.index else None
topics[-1]['evidence'] = [('姓名截断案例', f"原始数据中有一条明显截断的姓名，对应 {int(suspect.rows)} 条金牌行、跨 {int(suspect.years)} 届；原文保留在分析数据中，身份仍需与权威运动员表核对。" if suspect is not None else '原始姓名存在截断，不能直接发布个人排名。'),
 ('反向错误', '同一名字也可能混入不同的人。仅用姓名分组会同时产生“同人拆开”和“异人合并”两类误差，player_id 也不稳定。')]

# S8: distinct from task-two growth curve: changing women's medal participation.
female = med.groupby(['Year','Sex']).size().unstack(fill_value=0)
frows = [{'label':str(y),'value':round(100*int(r.get('F',0))/int(r.sum()),1) if r.sum() else 0,
          'detail':int(r.get('F',0))} for y,r in female.iterrows() if y != 1906]
add('S8','S8_她们登上领奖台','领奖台上的她们','紫色档案',
    '女性参赛比例是一条重要曲线；另一个问题是她们在获奖记录中占多少。这里把焦点移到每届奖牌运动员行的性别构成。',
    '占比上升说明可见度在变化，但它同时受女子小项数量和团体人数影响，不能直接解释为男女夺牌机会已经完全相同。',
    frows,'每届女性获奖运动员行 ÷ 全部获奖运动员行；图中数值为百分比。',
    'Sex 只有 M/F 两值；该指标不是官方女子小项占比，也不是女性参赛人数占比。1906 排除。',
    ('#33234e','#e58bb8','#faf0f8'),'editorial','%')
topics[-1]['evidence'] = [('起点与终点', f"1896 年女性获奖行占比 {frows[0]['value']}%；2024 年为 {frows[-1]['value']}%。"),
 ('另一种分母', '若改看女性参赛行占比，讲的是参与机会；若看女子小项数量，讲的是赛程设置。三者相关，却不能互相替代。')]

# S9: sport turnover without relying on broken 2020 Event labels.
sport_year = d.groupby('sport_family').Year.agg(['min','max','nunique'])
ended = sport_year[(sport_year['max']<=2016)&(sport_year['nunique']>=1)].sort_values(['max','min'])
turnover = [{'label':sport_label(str(k)),'raw_sport':str(k),'value':int(v['nunique']),'detail':f"{int(v['min'])}—{int(v['max'])} 年"}
            for k,v in ended.tail(14).iterrows()]
add('S9','S9_消失的赛场','消失的赛场','项目博物馆',
    '并非每项运动都会永久留在奥运。按归一后的体育大类观察，有些项目最后一次出现在数据中的时间已经很久。',
    '“最后出现年份”是数据现象，不等于该运动永久退出奥运；项目可能改名、拆分或在以后重返。图中条长表示它在多少届出现。',
    turnover,'按任务一 sport_family 归一字段，计算各大类最早、最后出现年份和出现届数。',
    '2020/2024 名称漂移可能造成假退出；此图是待核验线索，不作 IOC 正式项目沿革结论。1906 排除。',
    ('#2e3432','#bad77a','#f4f2df'),'museum','届')
topics[-1]['evidence'] = [('历史样本', '艺术竞赛、拔河、马球、槌球等项目提供了不同的退场故事；花样滑冰和冰球也曾出现在夏季奥运记录中。'),
 ('名称核验', '体操、场地自行车等在 2020 年后有拆分或改名。凡是“消失”结论，都需要先对照归一映射和官方赛程。')]

# S10: concentration of medal rows by sport, a fourth research question.
sport_med = [{**r,'raw_sport':r['label'],'label':sport_label(r['label']),'detail':'获奖运动员记录'} for r in series(med,'sport_family',n=15)]
add('S10','S10_奖牌藏在哪些项目','奖牌藏在哪些项目','运动地图',
    '如果一个代表团长期在少数项目积累奖牌，它的总量可能很高，却也更依赖这些项目的赛制和名额。先看全数据的获奖记录集中在哪些体育大类。',
    '排名靠前的运动往往同时拥有更多小项、更多届次或更多团体成员。它提示“机会结构”，不等于运动难度或国家实力。',
    sport_med,'按归一体育大类统计 1896—2024 的获奖运动员行，显示前 15 类。',
    '团体项目和历史年数影响记录总量；不能将条形长度读作官方奖牌数。1906 排除。',
    ('#102e46','#75c9d0','#e8f7f7'),'atlas','获奖行')
total_med = len(med)
top3 = sum(r['value'] for r in sport_med[:3])
topics[-1]['evidence'] = [('集中程度', f"图中前三类体育大类合计 {top3:,} 条获奖行，占全表 {top3/total_med:.1%}。这是记录分布，不是官方奖牌分配。"),
 ('研究下一步', '若要比较代表团的优势项目，应改算“该代表团在某项目的获奖行 ÷ 该项目全部获奖行”，并按时代分层。')]

def page(t):
    rows = json.dumps(t['rows'], ensure_ascii=False)
    bg, accent, pale = t['colors']
    top = max((r['value'] for r in t['rows']), default=1) or 1
    bars = ''.join(f'<button class="bar" data-i="{i}" aria-label="{escape(r["label"])}：{r["value"]}"><span class="label">{escape(r["label"])}</span><span class="track"><i style="width:{max(1,100*r["value"]/top):.1f}%"></i></span><strong>{r["value"]}{t["unit"] if t["unit"]=="%" else ""}</strong></button>' for i,r in enumerate(t['rows']))
    return f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{t['code']} {escape(t['title'])}｜百年圣火</title>
<style>:root{{--bg:{bg};--a:{accent};--p:{pale}}}*{{box-sizing:border-box}}body{{margin:0;background:var(--p);color:var(--bg);font-family:"Microsoft YaHei",system-ui,sans-serif}}a{{color:inherit}}nav{{padding:18px 5vw;display:flex;justify-content:space-between;gap:15px;background:var(--bg);color:var(--p)}}nav a{{text-decoration:none}}nav a:hover{{text-decoration:underline}}header{{min-height:58vh;background:var(--bg);color:var(--p);padding:8vh 7vw;display:flex;flex-direction:column;justify-content:end;position:relative;overflow:hidden}}header:after{{content:"{t['code']}";position:absolute;right:-1vw;top:-8vw;font-size:35vw;font-weight:900;opacity:.08;pointer-events:none}}.tag{{color:var(--a);font-weight:900;letter-spacing:.23em}}h1{{font-size:clamp(52px,8vw,120px);line-height:1.03;margin:.25em 0;max-width:1000px}}.lead{{font-size:clamp(18px,2vw,26px);line-height:1.7;max-width:860px}}main{{max-width:1400px;margin:auto;padding:7vw}}.insight{{font-size:clamp(22px,3vw,38px);line-height:1.5;max-width:1050px;margin:0 0 60px}}.viz{{display:grid;grid-template-columns: minmax(0,2fr) minmax(260px,1fr);gap:42px}}h2{{font-size:32px;margin:0 0 22px}}.chart{{display:grid;gap:9px}}.bar{{font:inherit;background:transparent;border:0;border-bottom:1px solid #80909666;color:var(--bg);display:grid;grid-template-columns:155px 1fr 85px;gap:15px;align-items:center;padding:8px;text-align:left;cursor:pointer}}.bar:hover,.bar:focus-visible{{background:#ffffff88;outline:2px solid var(--a)}}.track{{height:14px;background:#7f8c8b3b;border-radius:10px;overflow:hidden}}.track i{{display:block;height:100%;background:var(--a);border-radius:10px}}.bar strong{{text-align:right}}aside{{background:white;padding:30px;align-self:start;border-top:8px solid var(--a);box-shadow:0 20px 60px #0001}}aside b{{font-size:clamp(38px,5vw,70px);display:block;color:var(--bg)}}aside p{{line-height:1.8}}.method{{display:grid;grid-template-columns:1fr 1fr;gap:35px;margin-top:80px;border-top:2px solid var(--bg);padding-top:35px}}.method p{{line-height:1.9}}footer{{padding:32px 7vw;background:var(--bg);color:var(--p);display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap}}.archive header{{background-image:repeating-linear-gradient(0deg,transparent 0 37px,#ffffff12 38px 39px)}}.archive .bar{{grid-template-columns:90px 1fr 90px;border-bottom:1px dashed #67748c}}.archive .track{{height:4px;border-radius:0}}.islands header{{border-bottom:18px solid var(--a);border-radius:0 0 100px 0}}.islands .bar{{border-radius:30px;background:#ffffff77;border:0;padding:12px 18px}}.timeline header{{clip-path:polygon(0 0,100% 0,100% 87%,0 100%);padding-bottom:15vh}}.timeline .viz{{grid-template-columns:1fr}}.timeline .chart{{grid-template-columns:repeat(3,1fr);gap:8px 18px}}.timeline .bar{{grid-template-columns:60px 1fr 65px;font-size:13px}}.timeline aside{{display:flex;gap:30px;align-items:center}}.portrait header{{text-align:center;align-items:center}}.portrait header:after{{right:35%;top:5%;font-size:20vw}}.portrait .viz{{grid-template-columns:1fr 1.5fr}}.portrait .viz>div{{order:2}}.portrait aside{{order:1;position:sticky;top:20px;background:var(--bg);color:var(--p)}}.portrait aside b{{color:var(--a)}}.editorial h1{{font-family:Georgia,"SimSun",serif;font-weight:400}}.editorial .bar{{grid-template-columns:65px 1fr 65px;border-left:5px solid var(--a);padding-left:16px}}.museum header{{background-image:radial-gradient(circle at 80% 50%,#ffffff25 0 13%,transparent 13.2%)}}.museum .chart{{grid-template-columns:repeat(2,1fr)}}.museum .bar{{display:block;background:white;border:1px solid #b8c0a6;padding:15px;min-height:100px}}.museum .bar .label{{display:block;font-weight:700}}.museum .track{{display:block;margin:12px 0 6px}}.atlas header{{background-image:linear-gradient(115deg,transparent 55%,#ffffff16 55% 56%,transparent 56%)}}.atlas .bar{{grid-template-columns:170px 1fr 90px}}.atlas .bar:nth-child(3n) .track i{{background:#347b9e}}@media(max-width:800px){{.viz,.method,.timeline .viz,.portrait .viz{{grid-template-columns:1fr}}.timeline .chart,.museum .chart{{grid-template-columns:1fr}}.timeline aside{{display:block}}.portrait .viz>div,.portrait aside{{order:initial;position:static}}.bar,.archive .bar,.editorial .bar,.atlas .bar{{grid-template-columns:85px 1fr 70px;gap:7px;font-size:13px}}main{{padding:40px 5vw}}}}</style></head><body class="{t['layout']}"><nav><a href="../统一中文入口/index.html">← 十专题总览</a><span>百年圣火 · {t['code']}</span></nav><header><div class="tag">{escape(t['kicker'])} / {t['code']}</div><h1>{escape(t['title'])}</h1><p class="lead">{escape(t['intro'])}</p></header><main><p class="insight">{escape(t['insight'])}</p><section class="viz"><div><h2>从数据里看</h2><div class="chart">{bars}</div></div><aside aria-live="polite"><small>点击任意条形查看</small><b id="pick">{escape(t['rows'][0]['label']) if t['rows'] else ''}</b><p id="detail">{t['rows'][0]['value'] if t['rows'] else 0} {escape(t['unit'])}　{escape(str(t['rows'][0].get('detail',''))) if t['rows'] else ''}</p><p>图中所有条形均可点击。页面可离线阅读，数据由本项目归一数据重新计算。</p></aside></section><section class="method"><div><h2>怎么算</h2><p>{escape(t['method'])}</p></div><div><h2>读图边界</h2><p>{escape(t['caveat'])}</p></div></section></main><footer><span>数据：赛题归一表 · CC BY-NC-SA 4.0</span><span>本页面为专题分析，不替代官方奖牌榜</span></footer><script>const rows={rows};document.querySelectorAll('.bar').forEach(b=>b.onclick=()=>{{const r=rows[+b.dataset.i];document.querySelector('#pick').textContent=r.label;document.querySelector('#detail').textContent=r.value+' {t['unit']}　'+(r.detail??'');}})</script></body></html>'''

for t in topics:
    folder = BASE / t['slug']
    folder.mkdir(parents=True, exist_ok=True)
    evidence = ''.join(f'<article><span>{escape(k)}</span><p>{escape(v)}</p></article>' for k,v in t.get('evidence',[]))
    html = page(t).replace('</style>', 'aside b{overflow-wrap:anywhere;line-height:1.06}.evidence{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:70px}.evidence article{padding:28px;background:#fff;border-left:6px solid var(--a)}.evidence span{font-weight:900;color:var(--bg)}.evidence p{line-height:1.8}@media(max-width:800px){.evidence{grid-template-columns:1fr}}</style>', 1)
    html = html.replace('<section class="method">', '<section class="evidence">'+evidence+'</section><section class="method">',1)
    (folder/'index.html').write_text(html,encoding='utf-8')
    (folder/'分析数据.json').write_text(json.dumps(t['rows'],ensure_ascii=False,indent=2),encoding='utf-8')
    evidence_text='\n'.join(f'- **{k}**：{v}' for k,v in t.get('evidence',[]))
    (folder/'研究说明.md').write_text(f"# {t['code']} {t['title']}\n\n{t['intro']}\n\n## 发现\n\n{t['insight']}\n\n{evidence_text}\n\n## 方法\n\n{t['method']}\n\n## 局限\n\n{t['caveat']}\n\n数据由 `项目工作区/outputs/olympics_flagged.csv.gz` 生成。运行 `项目工作区/scripts/task3_ten_topics.py` 可复现本页。\n",encoding='utf-8')
print('Built',len(topics),'additional topics')

# Restore S8 task-page presentation after generating content.
import runpy
runpy.run_path(str(Path(__file__).with_name("publish_women_topic_style.py")))

# Restore S9 topic layout after general topic generation.
import runpy
runpy.run_path(str(Path(__file__).with_name('publish_vanished_topic_style.py')))
runpy.run_path(str(Path(__file__).with_name('publish_geopolitics_topic_style.py')))
