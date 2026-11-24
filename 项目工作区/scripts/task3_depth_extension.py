"""Reproducible cross-checks and deeper reading for all ten Task 3 stories."""
from __future__ import annotations

from html import escape
from pathlib import Path
import json

import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "交付文件" / "任务三_专题深挖"
DATA = ROOT / "项目工作区" / "outputs" / "olympics_flagged.csv.gz"
d = pd.read_csv(DATA, low_memory=False)
d = d[d.include_main.eq(True)].copy()
d.Year = pd.to_numeric(d.Year, errors="coerce").astype(int)
m = d[d.is_medal.eq(True)].copy()
gold = d[d.Medal.eq("Gold")].copy()


def pct(a, b):
    return 100 * a / b if b else 0.0


def metric(label, value, note):
    return {"label": label, "value": str(value), "note": note}


sections = []


def add(code, title, question, metrics, finding, crosscheck, counterexample, boundary, source):
    sections.append(dict(code=code, title=title, question=question, metrics=metrics,
                         finding=finding, crosscheck=crosscheck,
                         counterexample=counterexample, boundary=boundary, source=source))


# S1 — host effect. Shares and contemporaneous comparators answer different questions.
h = pd.read_csv(BASE / "S1_东道主效应" / "host_summary.csv")
positive = int(h.change_pp.gt(0).sum())
median_change = h.change_pp.median()
median_gap = h.descriptive_gap_pp.median()
bra = h[h.NOC.eq("BRA")].iloc[0]
add("S1", "东道主效应", "主办届的奖牌份额增加，是否等于主场带来了净收益？", [
    metric("上升案例", f"{positive}/{len(h)}", "九个选定现代主办案例中，主办届份额高于前届的数量"),
    metric("份额变化中位数", f"{median_change:+.2f} 个百分点", "先计算每个案例，再取中位数，避免大国主导"),
    metric("相对比较组中位数", f"{median_gap:+.2f} 个百分点", "前届份额相近代表团的描述性差值"),
], "份额上升在样本中常见，但案例间差异很大。把每届获奖运动员行除以当届总获奖行，能够减弱赛程扩张的影响，不能消除团体规模和项目结构的差异。",
    "同一案例同时报告原始份额变化与前届份额匹配比较组的差值；两者不完全相同。任务二另有前趋势、匹配 DID 与合成对照，但这些仍依赖不可验证的主办权选择假设。",
    f"巴西 2016 的自身份额变化为 {bra.change_pp:+.2f} 个百分点，而相对比较组为 {bra.descriptive_gap_pp:+.2f} 个百分点。自身下降与相对优势可以同时成立。",
    "九例是选定样本，不能推广为所有主办城市的因果平均效应；2024 法国没有后届观测。", "S1_东道主效应/index.html")


# S2 — official, fractional and row rankings, with historical validation.
s2 = pd.read_csv(BASE / "S2_口径的魔力" / "02_数据表" / "S2_2024三口径完整排名.csv")
rank = s2.pivot_table(index="NOC", columns="lens", values="rank", aggfunc="first")
common = rank.dropna(subset=["official", "rows"])
mean_shift = (common.official - common.rows).abs().mean()
history = pd.read_csv(BASE / "S2_口径的魔力" / "02_数据表" / "S2_跨届稳定性摘要.csv")
esp = rank.loc["ESP"]
ned = rank.loc["NED"]
add("S2", "口径的魔力", "同一批比赛结果为什么能产生不同的金牌榜？", [
    metric("西班牙名次", f"{int(esp.official)} → {int(esp.rows)}", "官方小项 → 运动员获奖行；并非官方名次变更"),
    metric("平均名次移动", f"{mean_shift:.1f} 位", f"2024 年 {len(common)} 个两榜均出现的代表团，取绝对名次差均值"),
    metric("跨届机制相关", f"{history.mechanism_rho.min():.3f}—{history.mechanism_rho.max():.3f}", "2008、2012、2016 三届多人组占比与膨胀倍率的 Spearman 相关"),
], "行口径提高了多人获奖结构的权重。2024 年西班牙由官方第 15 到行口径第 5，荷兰由第 6 到第 3，反向移动的代表团也存在。平均名次移动显示重排不是单个特例。",
    "同时对照2024官方小项、团队内均分、运动员行三套口径；2008、2012、2016仅用NOC–Event–Medal历史代理做数据内部探索，不能称为现行IOC逐项核验或独立机制验证。",
    f"荷兰的团队内均分榜为第 {int(ned.fractional)}，不同于行口径第 {int(ned.rows)}；均分榜的金牌合计也可能因原始运动员匹配缺口与官方数不完全一致。",
    "官方小项榜回答竞赛单元结果；行榜回答获奖者记录规模。两者的数值和名次均不得互称为官方奖牌数。", "S2_口径的魔力/06_滚动叙事专题/index.html")


# S3 — distinguish coverage change from the political event that may explain it.
sets = {y: set(d.loc[d.Year.eq(y), "NOC"].dropna()) for y in [1976, 1980, 1984, 1988]}
counts = {y: len(v) for y, v in sets.items()}
absent80 = len(sets[1976] - sets[1980])
new84 = len(sets[1984] - sets[1980])
add("S3", "地缘政治的投影", "参赛代表团的缺口能否直接解释成抵制名单？", [
    metric("1976 → 1980", f"{counts[1976]} → {counts[1980]}", "数据中出现的唯一 NOC 数"),
    metric("前届有、本届无", f"{absent80} 个", "1976 出现而 1980 未出现的代码，不等于抵制国家数"),
    metric("1980 → 1984", f"{counts[1980]} → {counts[1984]}", "总数反而上升，说明不能只看总量判断抵制强弱"),
], "1980 年的代表团总量下降，与抵制背景相容；1984 年总量上升，却不能据此否认另一轮抵制。总体扩张、首次参赛和身份变化会掩盖单个群体的缺席。",
    f"集合差比单一总数更接近问题：1984 比 1980 新出现 {new84} 个 NOC 代码，但其中既可能有重新参赛者，也可能有首次出现者。下一步应按代码逐个查 IOC 与各国奥委会档案。",
    "苏联、独联体联队、俄罗斯、俄罗斯奥委会代表队及个人中立运动员不是一条可以直接加总的连续国家序列。",
    "本表只识别数据中的参赛覆盖变化，不标注政治动机；1956 双城按一届，1906 排除。", "S3_地缘政治的投影/index.html")


# S4 — alternative denominator changes a small-delegation comparison.
codes = ["HKG", "TPE", "SGP", "FIJ", "BER", "JOR", "KOS"]
small = d[d.NOC.isin(codes)].groupby("NOC").size().rename("rows")
small_m = m[m.NOC.isin(codes)].groupby("NOC").size().rename("medal_rows")
sm = pd.concat([small, small_m], axis=1).fillna(0)
sm["rate"] = 1000 * sm.medal_rows / sm.rows
raw_leader = sm.medal_rows.idxmax()
rate_leader = sm.rate.idxmax()
fiji_sport = m[m.NOC.eq("FIJ")].groupby("sport_family").size().sort_values(ascending=False)
fiji_top_share = pct(int(fiji_sport.iloc[0]), int(sm.loc["FIJ", "medal_rows"])) if len(fiji_sport) else 0
add("S4", "小代表团的大突破", "累计奖牌行多，就代表小队伍更有效率吗？", [
    metric("累计行数第一", raw_leader, f"选定七个案例，{int(sm.loc[raw_leader, 'medal_rows'])} 条获奖行"),
    metric("每千参赛行第一", rate_leader, f"{sm.loc[rate_leader, 'rate']:.1f} 条获奖行 / 千参赛记录行"),
    metric("斐济最大项目占比", f"{fiji_top_share:.1f}%", "该项目在斐济获奖运动员行中所占比重"),
], "原始累计量与按参赛记录行标准化后的排序可能不同。大团队一次夺牌会形成多条获奖运动员行，因此单一团队项目可能主导小代表团的总量。",
    "同时展示累计获奖行、每千参赛行和最大项目占比。分母是数据记录行，不是独立运动员人数；跨年代累加仍受参赛届数不同影响。",
    "本页只挑选七个分析案例，不构成全部小代表团的公平排行榜。把某届团队夺牌的数十条记录读作数十枚官方奖牌会产生严重夸大。",
    "要评估突破概率，应进一步按届次、参赛人数和小项机会分层；本页不作因果解释。", "S4_小代表团的大突破/index.html")


# S5 — opportunity and recording intensity cannot be collapsed into a single count.
year_rows = d.groupby("Year").size()
year_med = m.groupby("Year").size()
year_noc = d.groupby("Year").NOC.nunique()
share_1896 = pct(year_med.get(1896, 0), year_rows.get(1896, 0))
share_2024 = pct(year_med.get(2024, 0), year_rows.get(2024, 0))
growth_factor = year_med.get(2024, 0) / year_med.get(1896, 1)
add("S5", "奖牌的通货膨胀", "奖牌记录变多，是夺牌更容易了吗？", [
    metric("获奖行倍数", f"{growth_factor:.1f} 倍", "2024 / 1896，反映记录规模，不能解释为获奖概率"),
    metric("1896 获奖行占参赛行", f"{share_1896:.1f}%", "早期届次规模小，受项目与记录覆盖影响大"),
    metric("2024 获奖行占参赛行", f"{share_2024:.1f}%", "同一分母定义下重新观察"),
], "绝对获奖行随奥运规模扩张显著增加，但把分母换成参赛记录行之后，问题变成每条参赛记录被标记获奖的频率。两个指标不能互相替代。",
    f"同时核对代表团覆盖数：1896 年 {int(year_noc.get(1896,0))} 个，2024 年 {int(year_noc.get(2024,0))} 个。项目、代表团与团队人数共同变化，单看获奖行曲线会把不同机制混在一起。",
    "2020 起 Event 字段泛化，不能直接用其唯一值数来证明正式小项增加或减少。",
    "这些是运动员记录指标，不是官方小项奖牌数或独立运动员获奖概率。", "S5_奖牌的通货膨胀/index.html")


# S6 — quantify identity risk without claiming that a suspicious span proves an error.
named = gold.dropna(subset=["Name"]).groupby("Name").agg(first=("Year", "min"), last=("Year", "max"), rows=("source_row", "count"))
long_span = named[(named["last"] - named["first"]).gt(60)]
id_names = d.dropna(subset=["player_id", "Name"]).groupby("player_id").Name.nunique()
id_conflict = int(id_names.gt(1).sum())
raw_top = named.rows.idxmax()
add("S6", "王者与传奇", "原表的姓名能直接生成个人历史金牌榜吗？", [
    metric("跨越超 60 年的姓名", f"{len(long_span)} 组", "只标记核验候选，不自动判定为错人"),
    metric("编号对应多个姓名", f"{id_conflict} 个", "按原始 player_id 分组的身份一致性警报"),
    metric("原始姓名首位", str(raw_top), "仅是字符串聚合结果，不是已核验运动员"),
], "姓名既可能截断，也可能同名异人；编号也不能无条件视为稳定人物 ID。按字符串直接排出的金牌榜会同时产生拆人和并人两类风险。",
    "先用姓名时间跨度与编号多姓名映射筛选异常，再把候选人与权威运动员档案逐条核对。核验之前只发布记录级图，不发布个人历史排名。",
    "时间跨度很长也可能是常见姓名被多人使用，不能把每一个长跨度组都宣称为数据错误。",
    "本专题的定量值是数据质量警报数量，非真实身份数量；外部身份核验仍未覆盖全部候选。", "S6_王者与传奇/index.html")


# S7 — reigning rates are edition-level control, not athlete survival.
dyn = json.loads((BASE / "S3_冠军的保质期" / "02_数据表" / "S3_关键指标.json").read_text(encoding="utf-8"))
eras = dyn["era"]
early, recent = eras[0], eras[-1]
add("S7", "冠军的保质期", "王朝变短，是冠军个人变弱了吗？", [
    metric("控制权转移", f"{dyn['transitions']:,} 次", "同一小项相邻届冠军代表团之间的比较"),
    metric("总体卫冕率", f"{100*dyn['defense_rate']:.1f}%", "同一代表团连续保有小项金牌的比例"),
    metric("早期 → 近代", f"{100*early['defense_rate']:.1f}% → {100*recent['defense_rate']:.1f}%", "分时代的代表团卫冕率，受项目结构变化影响"),
], "以代表团对小项的连续控制，而非个人运动员生涯，衡量冠军王朝。分时代卫冕率下降是一条结构线索，尚不能解释其原因。",
    "按小项比较相邻实际举办届次，并在专题时间轴和生存图中筛选年代、体育大类。完整王朝清单允许复查最长连续段。",
    "某些小项改名、拆分、取消后重返；如果把名称变化误作新项目，会缩短王朝长度。",
    "本结果截至 2016 年、使用历史小项代理；2020 起 Event 泛化，不外推到 2024。", "S3_冠军的保质期/06_冠军王朝时间轴/index.html")


# S8 — two denominators and their gap.
def female_share(frame, y):
    x = frame[frame.Year.eq(y)]
    return pct(x.Sex.eq("F").sum(), len(x))

f_1900 = female_share(m, 1900)
f_2024 = female_share(m, 2024)
entry_2024 = female_share(d, 2024)
gap_2024 = f_2024 - entry_2024
add("S8", "领奖台上的她们", "女子获奖行占比上升，是否说明机会已经平等？", [
    metric("1900 女子获奖行占比", f"{f_1900:.1f}%", "女性进入早期奥运记录后的历史起点"),
    metric("2024 女子获奖行占比", f"{f_2024:.1f}%", "女性获奖运动员行 / 全部获奖行"),
    metric("2024 与参赛行差", f"{gap_2024:+.1f} 个百分点", f"同年女子参赛行占比为 {entry_2024:.1f}%"),
], "获奖行占比与参赛行占比回答不同问题。二者的差值比单看获奖曲线多了一层参照，但仍不等于夺牌率的性别差异。",
    "对同一届同时计算女性参赛行占比和女性获奖行占比；再回看女子项目开设、混合项目和团队规模，才能讨论机会结构。",
    "若女子项目和男子项目的小项数不同，即使获奖行占比接近参赛行占比，也不能推出制度机会完全相同。",
    "Sex 字段仅有 M/F 两值；记录行并非独立运动员或官方女子小项。", "S8_她们登上领奖台/index.html")


# S9 — distinguish archival end from permanent exclusion.
sport_years = d.groupby("sport_family").Year.agg(["min", "max", "nunique"])
ended = sport_years[sport_years["max"].le(2016)]
golf_years = sorted(d.loc[d.sport_family.eq("Golf"), "Year"].unique().tolist())
add("S9", "消失的赛场", "数据里最后一次出现，等于永久退出奥运吗？", [
    metric("最后出现 ≤2016", f"{len(ended)} 类", "按项目大类归一后的候选清单"),
    metric("高尔夫出现届次", f"{len(golf_years)} 届", "用于检查中断后重返，而非永久消失"),
    metric("高尔夫首末年份", f"{golf_years[0] if golf_years else '—'}—{golf_years[-1] if golf_years else '—'}", "首末年之间并非每届连续举办"),
], "“消失”至少有三种机制：正式退出、名称重编和中断后重返。只按最后出现年份画图，会把三者压成同一种故事。",
    "以 sport_family 归一映射复查源字段，并把出现年份序列与官方赛程核对。高尔夫提供了‘中断—重返’反例。",
    "花样滑冰和冰球曾存在于夏季奥运历史记录，却不能据此宣称它们今天仍是夏季项目。",
    "2020/2024 Event 泛化和项目命名漂移可能制造假退出；本页提供核验线索，不是 IOC 正式沿革表。", "S9_消失的赛场/index.html")


# S10 — opportunity concentration changes with time and counting unit.
def concentration(frame):
    n = frame.groupby("sport_family").size().sort_values(ascending=False)
    return pct(n.head(3).sum(), n.sum()), len(n)

all_top3, all_sports = concentration(m)
share_2016, fam_2016 = concentration(m[m.Year.eq(2016)])
share_2024, fam_2024 = concentration(m[m.Year.eq(2024)])
add("S10", "奖牌藏在哪些项目", "哪类运动贡献了更多获奖记录，是否等于更容易夺牌？", [
    metric("全史前三类占比", f"{all_top3:.1f}%", f"{all_sports} 个归一体育大类中的运动员获奖行分布"),
    metric("2016 前三类占比", f"{share_2016:.1f}%", f"当届 {fam_2016} 类，以同届为分母"),
    metric("2024 前三类占比", f"{share_2024:.1f}%", f"当届 {fam_2024} 类，以同届为分母"),
], "全史总量叠加了举办年数和项目机会。把统计单位切到单届，可以观察集中度是否只是时间累积造成；两届前三类占比并不必然相同。",
    "同报全史与单届前三类份额，再按代表团和体育大类分层。若研究竞技优势，应进一步除以该类小项机会和参赛规模。",
    "接力、团体与个人项目产生的获奖运动员行不同，行数多可能是团队人数多，而非官方金牌更多。",
    "2020 起 Event 泛化；本页在体育大类层面比较记录，不把行数换算成官方奖牌或夺牌概率。", "S10_奖牌藏在哪些项目/index.html")


assert [s["code"] for s in sections] == [f"S{i}" for i in range(1, 11)]


def md_section(s):
    lines = [f"## {s['code']}｜{s['title']}", "", f"**研究问题：**{s['question']}", "",
             "| 交叉核验指标 | 结果 | 计算说明 |", "| --- | ---: | --- |"]
    lines += [f"| {x['label']} | {x['value']} | {x['note']} |" for x in s["metrics"]]
    for label, key in [("发现与机制", "finding"), ("交叉验证", "crosscheck"),
                       ("反例与替代解释", "counterexample"), ("证据边界", "boundary")]:
        lines += ["", f"**{label}：**{s[key]}"]
    lines += ["", f"[打开交互专题]({s['source']})", ""]
    return "\n".join(lines)


md = "# 任务三｜十专题深度核验\n\n"
md += "本补充报告把每个专题从单一图形扩展为研究问题、替代分母、反例和证据边界。所有新指标由赛题归一数据及既有 S1/S2/S7 分析表复算。默认排除 1906；获奖记录均为运动员行，除 S2 明确标出的官方小项数外，不能作为官方奖牌数。\n\n"
md += "\n".join(md_section(s) for s in sections)
md += "\n## 复现\n\n运行 `项目工作区/scripts/task3_depth_extension.py`；输入为任务一归一数据、S1 主场表、S2 三口径和跨届表、S7 王朝关键指标。对应可机器读取结果见 `十专题深度核验.json`。\n"
(BASE / "十专题深度核验.md").write_text(md, encoding="utf-8")
(BASE / "十专题深度核验.json").write_text(json.dumps(sections, ensure_ascii=False, indent=2), encoding="utf-8")


cards = []
for s in sections:
    metrics = "".join(f"<div class='metric'><span>{escape(x['label'])}</span><strong>{escape(x['value'])}</strong><small>{escape(x['note'])}</small></div>" for x in s["metrics"])
    cards.append(f"<section class='topic' id='{s['code']}'><div class='topic-head'><small>{s['code']} / 深度核验</small><h2>{escape(s['title'])}</h2><p>{escape(s['question'])}</p></div><div class='metrics'>{metrics}</div><div class='read'><article><h3>发现与机制</h3><p>{escape(s['finding'])}</p></article><article><h3>交叉验证</h3><p>{escape(s['crosscheck'])}</p></article><article><h3>反例与替代解释</h3><p>{escape(s['counterexample'])}</p></article><article><h3>证据边界</h3><p>{escape(s['boundary'])}</p></article></div><a class='open' href='{escape(s['source'])}'>进入交互专题 ↗</a></section>")

nav = "".join(f"<a href='#{s['code']}'>{s['code']} {escape(s['title'])}</a>" for s in sections)
html = f"""<!doctype html><html lang='zh-CN'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>任务三｜十专题深度核验</title><style>
*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}body{{margin:0;background:#f0eee8;color:#153039;font-family:'Microsoft YaHei',system-ui,sans-serif}}a{{color:inherit;text-decoration:none}}a:focus-visible{{outline:3px solid #d8a267;outline-offset:4px}}header{{background:#102b34;color:#f4f2e9;padding:75px clamp(22px,6vw,90px) 85px}}header a{{font-size:13px;color:#dfb681}}header h1{{font-family:'STSong','SimSun',serif;font-size:clamp(48px,8vw,105px);font-weight:500;letter-spacing:-.07em;line-height:1.08;margin:35px 0 23px}}header p{{font-size:18px;line-height:1.85;max-width:850px;color:#d1deda}}nav{{position:sticky;top:0;z-index:5;display:flex;gap:9px;padding:12px clamp(16px,4vw,55px);overflow:auto;background:#102b34e8;backdrop-filter:blur(12px);color:#e7eeea;border-top:1px solid #ffffff25}}nav:not(#xz-nav) a{{flex:none;font-size:12px;padding:8px 12px;border:1px solid #ffffff35;border-radius:99px;white-space:nowrap}}nav:not(#xz-nav) a:hover{{background:#e5b87e;color:#102b34}}main{{max-width:1380px;margin:auto;padding:40px clamp(18px,5vw,70px) 110px}}.topic{{scroll-margin-top:80px;border-bottom:1px solid #b8c4be;padding:80px 0 90px}}.topic-head{{display:grid;grid-template-columns:1fr 1.5fr;gap:30px;align-items:end}}.topic-head small{{grid-column:1/-1;color:#ae6f45;font-size:12px;font-weight:800;letter-spacing:.2em}}h2{{font-family:'STSong','SimSun',serif;font-size:clamp(42px,6vw,76px);font-weight:500;letter-spacing:-.06em;line-height:1.1;margin:0}}.topic-head p{{font-size:clamp(18px,2.2vw,25px);line-height:1.55;margin:0}}.metrics{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:42px 0}}.metric{{background:#fffdf8;padding:25px;border-radius:18px;min-height:180px;border-top:3px solid #ca8c5f;display:flex;flex-direction:column}}.metric span{{font-size:13px;color:#677579}}.metric strong{{font-family:Georgia,'Microsoft YaHei',serif;font-weight:500;font-size:clamp(27px,3vw,42px);margin:16px 0 10px;color:#af5838;line-height:1.15}}.metric small{{font-size:12px;line-height:1.65;color:#627276;margin-top:auto}}.read{{display:grid;grid-template-columns:repeat(2,1fr);gap:34px 65px}}.read h3{{font-size:14px;color:#9d613d;margin:0 0 12px}}.read p{{font-size:15px;line-height:1.9;margin:0;color:#39535a}}.open{{display:inline-block;border-bottom:1px solid #153039;margin-top:42px;padding-bottom:9px;font-size:14px;font-weight:800}}.open:hover{{color:#b26139;border-color:#b26139}}footer{{background:#102b34;color:#c7d9d6;padding:32px clamp(22px,6vw,90px);font-size:12px;line-height:1.8}}@media(max-width:760px){{.topic-head,.metrics,.read{{grid-template-columns:1fr}}.topic{{padding:55px 0}}.metrics{{margin:32px 0}}.metric{{min-height:130px}}}}@media(prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}}}
</style><style id="topic-review-layout">
html:has(#topic-review-layout) body>.topic-map-entry{{display:flex;align-items:center;justify-content:space-between;gap:16px;margin:0 6vw 24px;padding:16px 0;border-bottom:1px solid var(--review-line);color:var(--review-accent)!important;font-size:clamp(18px,2vw,26px);font-weight:650}}
html:has(#topic-review-layout) body>.topic-map-entry:hover{{text-decoration:underline;text-underline-offset:.2em}}
html:has(#topic-review-layout) body>.topic-map-entry::after{{content:none!important}}

html:has(#topic-review-layout) body{{
 --review-paper:#f3f5f1;--review-ink:#183640;--review-muted:#445c65;
 --review-line:#b8cac8;--review-accent:#1d6170;
 background:radial-gradient(ellipse 85% 560px at 0 0,#dbeae7,transparent),var(--review-paper)!important;
}}
html:has(#topic-review-layout) body.xz-dark,
html[data-supp-theme="dark"]:has(#topic-review-layout) body{{
 --review-paper:#17242c;--review-ink:#eef4f1;--review-muted:#bacbd0;
 --review-line:#536a73;--review-accent:#add9e1;
 background:radial-gradient(ellipse 85% 560px at 0 0,#243d46,transparent),var(--review-paper)!important;
}}
html:has(#topic-review-layout) body>header:has(h1){{
 background:transparent!important;color:var(--review-ink)!important;
 padding:clamp(26px,5vw,68px) 6vw 24px!important;
}}
html:has(#topic-review-layout) body>header:has(h1) h1{{
 color:var(--review-ink)!important;font-size:clamp(38px,5vw,72px)!important;margin:20px 0 12px!important;line-height:1.18!important;
}}
html:has(#topic-review-layout) body>header:has(h1) p{{color:var(--review-muted)!important;margin-bottom:0}}
html:has(#topic-review-layout) body>header:has(h1) a{{color:var(--review-accent)!important}}
html:has(#topic-review-layout) body>nav:has(a[href="#S10"]){{
 position:relative!important;top:auto!important;display:flex!important;flex-wrap:wrap;gap:8px!important;
 padding:12px 6vw!important;background:var(--review-paper)!important;border-block:1px solid var(--review-line)!important;
}}
html:has(#topic-review-layout) body>nav:has(a[href="#S10"]) a{{
 color:var(--review-accent)!important;border:1px solid var(--review-line)!important;border-radius:4px!important;
}}
html:has(#topic-review-layout) body>nav:has(a[href="#S10"]) a:hover{{background:var(--review-ink)!important;color:var(--review-paper)!important}}
html:has(#topic-review-layout) body main:has(>.topic){{
 max-width:none!important;width:100%!important;padding:0 6vw 48px!important;
}}
html:has(#topic-review-layout) body main>.topic{{
 padding:clamp(28px,4vw,58px) 0!important;scroll-margin-top:92px;border-color:var(--review-line)!important;
}}
html:has(#topic-review-layout) body main>.topic h2{{font-size:clamp(30px,3.4vw,52px)!important;color:var(--review-ink)!important}}
html:has(#topic-review-layout) body .topic :is(.topic-head small,.metric strong,.read h3,.open){{color:var(--review-accent)!important}}
html:has(#topic-review-layout) body .topic .metrics{{margin:22px 0 26px!important;gap:14px 24px}}
html:has(#topic-review-layout) body .topic .metric{{
 min-height:0!important;padding:12px 0!important;border:0!important;border-top:2px solid var(--review-line)!important;border-radius:0!important;background:transparent!important;
}}
html:has(#topic-review-layout) body .topic .metric strong{{margin:6px 0!important}}
html:has(#topic-review-layout) body .topic :is(.metric span,.metric small,.read p,.topic-head p){{color:var(--review-muted)!important}}
html:has(#topic-review-layout) body .topic .read{{gap:20px 44px}}
html:has(#topic-review-layout) body .topic .open{{margin-top:22px!important;border-color:var(--review-line)}}
@media(max-width:760px){{html:has(#topic-review-layout) body .topic :is(.topic-head,.metrics,.read){{grid-template-columns:minmax(0,1fr)!important;gap:14px}}}}
</style></head><body><header><a href='统一中文入口/index.html'>← 返回十专题交互入口</a><h1>十个专题，<br>十次交叉核验。</h1><p>每个结论都要回答：数字怎样算、换一个分母会怎样、哪个反例会推翻直觉、证据到哪里为止。这里是可复算的深度阅读版。</p></header><nav>{nav}</nav><main>{''.join(cards)}</main><footer>数据：赛题归一表及任务三既有分析表。除明确标出的官方小项结果外，获奖统计均为运动员行口径。2028 预测不进入历史核验。</footer></body></html>"""
(BASE / "十专题深度核验.html").write_text(html, encoding="utf-8")


# Short, source-specific bridges from every story page into its deeper cross-check.
paths = {
    "S1": BASE / "S1_东道主效应" / "index.html",
    "S2": BASE / "S2_口径的魔力" / "06_滚动叙事专题" / "index.html",
    "S3": BASE / "S3_地缘政治的投影" / "index.html",
    "S4": BASE / "S4_小代表团的大突破" / "index.html",
    "S5": BASE / "S5_奖牌的通货膨胀" / "index.html",
    "S6": BASE / "S6_王者与传奇" / "index.html",
    "S7": BASE / "S3_冠军的保质期" / "06_冠军王朝时间轴" / "index.html",
    "S8": BASE / "S8_她们登上领奖台" / "index.html",
    "S9": BASE / "S9_消失的赛场" / "index.html",
    "S10": BASE / "S10_奖牌藏在哪些项目" / "index.html",
}
for s in sections:
    path = paths[s["code"]]
    if not path.exists():
        raise FileNotFoundError(path)
    text = path.read_text(encoding="utf-8")
    if s["code"] == "S10":
        text = text.replace("<title>0 奖牌藏在哪些项目｜百年圣火</title>", "<title>专题十｜奖牌藏在哪些项目｜百年圣火</title>")
    start, end = "<!-- DEPTH_EXTENSION_START -->", "<!-- DEPTH_EXTENSION_END -->"
    if start in text and end in text:
        text = text[:text.index(start)] + text[text.index(end) + len(end):]
    href = Path(__import__("os").path.relpath(BASE / "十专题深度核验.html", path.parent)).as_posix() + "#" + s["code"]
    mini = "".join(f"<div><b>{escape(x['value'])}</b><span>{escape(x['label'])}</span></div>" for x in s["metrics"])
    block = f"{start}<section class='task3-depth-bridge' style='background:#102b34;color:#f3f0e8;padding:clamp(35px,5vw,70px);font-family:Microsoft YaHei,system-ui,sans-serif'><div style='max-width:1200px;margin:auto'><small style='color:#dfac72;letter-spacing:.15em'>交叉核验 / {s['code']}</small><h2 style='font-size:clamp(28px,4vw,48px);margin:12px 0 18px;line-height:1.2'>{escape(s['question'])}</h2><div style='display:flex;gap:28px;flex-wrap:wrap;margin:25px 0'>{mini}</div><p style='max-width:900px;line-height:1.8'>{escape(s['counterexample'])}</p><a href='{escape(href)}' style='color:#f0bd81;text-decoration:underline;text-underline-offset:5px;font-weight:700'>阅读证据、替代分母与局限 ↗</a></div></section>{end}"
    if "<footer" in text:
        text = text.replace("<footer", block + "<footer", 1)
    else:
        text = text.replace("</body>", block + "</body>", 1)
    path.write_text(text, encoding="utf-8")

portal = BASE / "统一中文入口" / "index.html"
text = portal.read_text(encoding="utf-8")
start, end = "<!-- DEPTH_PORTAL_START -->", "<!-- DEPTH_PORTAL_END -->"
if start in text and end in text:
    text = text[:text.index(start)] + text[text.index(end) + len(end):]
portal.write_text(text, encoding="utf-8")

print(f"Generated cross-checks for {len(sections)} Task 3 topics")

