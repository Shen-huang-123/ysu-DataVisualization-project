from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parents[2] / "交付文件" / "任务二_百年全景"

def read(name):
    with (ROOT / "02_数据表" / name).open(encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))

years = ("2016", "2020")
teams = {r["Year"]: r for r in read("B_十二代表团逐届份额.csv") if r["NOC"] == "USA"}
totals = {r["Year"]: int(r["medal_records"]) for r in read("A_逐届规模与集中度.csv")}
counts = [int(float(teams[y]["medal_records"])) for y in years]
all_counts = [totals[y] for y in years]
shares = [100 * float(teams[y]["medal_share"]) for y in years]
assert all(abs(100 * n / d - s) < 1e-9 for n, d, s in zip(counts, all_counts, shares))
assert counts[1] > counts[0] and shares[1] < shares[0]
count_growth = 100 * (counts[1] / counts[0] - 1)
total_growth = 100 * (all_counts[1] / all_counts[0] - 1)
explanation = (
    f"美国获奖运动员记录增长 {count_growth:.1f}%，但当届全部代表团的获奖记录从 "
    f"{all_counts[0]:,} 条增至 {all_counts[1]:,} 条，增幅为 {total_growth:.1f}%。"
    f"分母增长更快，因此美国的同届份额下降 {shares[0]-shares[1]:.2f} 个百分点。"
)
scope = "按运动员获奖记录行统计，排除 1906。东京按届次记为 2020 年。"
names = ("里约 2016", "东京 2020")

def panel(title, values, limit, unit):
    items = "".join(
        f'<li><span>{name}</span><meter min="0" max="{limit}" value="{value:.8g}" aria-label="{name}{title}"></meter>'
        f'<strong>{value:.{2 if unit == "%" else 0}f}{unit}</strong></li>'
        for name, value in zip(names, values)
    )
    return f'<div><p>{title}</p><ul>{items}</ul></div>'

block = f"""<!-- team-share-case:start -->
<style>
#team-share-case{{margin-block:1.4rem 2rem;padding-block:1rem;border-block:1px solid color-mix(in srgb,currentColor 22%,transparent)}}
#team-share-case h3{{font-size:clamp(1.25rem,2vw,1.8rem);margin-block:0 .65rem}}
.team-case-charts{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1rem 2rem}}
.team-case-charts p{{margin-block:.4rem;font-weight:700}}
.team-case-charts ul{{padding:0;margin:.4rem 0;list-style:none}}
.team-case-charts li{{display:grid;grid-template-columns:6em minmax(0,1fr) 5em;align-items:center;gap:.55rem;padding-block:.2rem}}
.team-case-charts meter{{width:100%;height:.65rem}}
.team-case-charts meter::-webkit-meter-bar{{background:color-mix(in srgb,currentColor 12%,transparent);border:0}}
.team-case-charts meter::-webkit-meter-optimum-value{{background:#57948f}}
.team-case-charts > div+div meter::-webkit-meter-optimum-value{{background:#b39152}}
.team-case-charts strong{{text-align:end;font-variant-numeric:tabular-nums}}
@media(max-width:680px){{.team-case-charts{{grid-template-columns:1fr}}}}
</style>
<section id="team-share-case" aria-labelledby="team-share-case-title">
<h3 id="team-share-case-title">美国获奖记录增加，同届份额却下降</h3>
<div class="team-case-charts">{panel("美国获奖记录", counts, 320, " 条")}{panel("美国占当届获奖记录的份额", shares, 15, "%")}</div>
<p>{explanation}</p>
<p><small>{scope} <a href="../02_数据表/B_十二代表团逐届份额.csv">下载代表团逐届数据</a> · <a href="../02_数据表/A_逐届规模与集中度.csv">下载全场总量</a></small></p>
</section>
<!-- team-share-case:end -->"""
for relative, marker in [
    ("05_交互总览/index.html", '<div class="t2-table-wrap">'),
    ("01_报告与说明/01_百年奥运全景分析_高分版.html", "</h2>"),
]:
    file = ROOT / relative
    content = file.read_text(encoding="utf-8")
    content = re.sub(r"<!-- team-share-case:start -->.*?<!-- team-share-case:end -->\n?", "", content, flags=re.S)
    anchor = 'id="explore-panorama-3"' if relative.startswith("05") else 'id="teams"'
    position = content.index(marker, content.index(anchor))
    if marker == "</h2>":
        position += len(marker)
    file.write_text(content[:position] + block + "\n" + content[position:], encoding="utf-8", newline="\n")

note = (
    f"**案例｜美国获奖记录增加，同届份额却下降。** 里约 2016 到东京 2020 年，美国从 {counts[0]} 条增至 "
    f"{counts[1]} 条，同届份额从 {shares[0]:.2f}% 降至 {shares[1]:.2f}%。{explanation}{scope}"
)
path = ROOT / "11_四视角独立交付/B_国家兴衰.md"
content = path.read_text(encoding="utf-8")
content = re.sub(r"\*\*案例｜美国获奖记录增加，同届份额却下降。\*\*[^\n]*\n\n", "", content)
path.write_text(content.replace("![时代热力图]", note + "\n\n![时代热力图]", 1), encoding="utf-8", newline="\n")
