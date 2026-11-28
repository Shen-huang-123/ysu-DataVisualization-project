from pathlib import Path
import csv
import json
import re

root = Path(__file__).resolve().parents[2] / "交付文件" / "任务二_百年全景"
overview = root / "05_交互总览"
page = overview / "index.html"

def rows(relative):
    with (root / relative).open(encoding="utf-8-sig", newline="") as source:
        return list(csv.DictReader(source))

metrics = {
    row["Year"]: [int(row["medal_nocs"]), float(row["top5_share"]), float(row["effective_nocs"])]
    for row in rows("07_结论压力测试/逐届集中度三口径.csv")
    if row["unit"] == "运动员获奖行"
}
contributions = [
    [row["运动大类中文"], float(row["合计贡献_百分点"])]
    for row in rows("08_女性结构分解/2024女性占比分解逐项目.csv")
]
data = json.dumps([metrics, contributions], ensure_ascii=False)
block = f'''<!-- panorama-lead:start -->
<link rel="stylesheet" href="panorama-lead.css">
<section id="panorama-lead" aria-labelledby="panorama-lead-title">
  <h2 id="panorama-lead-title">2016 至 2024：获奖队伍更多，分布却更集中</h2>
  <p>2016 → 2024 年，获奖代表团从 <strong>86 增至 92</strong>，前五代表团的获奖记录份额从 <strong>39.3% 升至 41.8%</strong>。</p>
  <label>查看届次 <select id="lead-year"></select></label><div class="lead-shortcuts"><button type="button" data-lead-year="2016">2016 年</button><button type="button" data-lead-year="2024">2024 年</button></div>
  <div class="lead-metrics" aria-live="polite">
    <div>获奖代表团数<strong id="lead-count"></strong></div>
    <div>前五代表团份额<strong id="lead-share"></strong></div>
    <div>有效获奖代表团数<strong id="lead-effective"></strong></div>
  </div>
  <div class="lead-drilldown">
    <div><label>查看代表团 <select id="lead-team"></select></label>
    <div id="lead-teams" class="lead-bars" aria-label="当届前五代表团"></div></div>
    <div><h3 id="lead-sport-title">运动构成</h3><div id="lead-sports" class="lead-bars" aria-live="polite"></div></div>
  </div>
  <p class="lead-note">按运动员获奖记录行统计，排除 1906，历史代表团代码分别保留。有效获奖代表团数为各队份额平方和的倒数。<a href="../07_结论压力测试/结论压力测试.html">复核集中度</a></p>
  <section id="panorama-gender" aria-labelledby="panorama-gender-title">
    <h3 id="panorama-gender-title">接近半数，哪些运动的差异被抵消了？</h3>
    <p>巴黎 2024 女性参赛记录占 49.1%，女性获奖记录占 50.3%。两者相差约 <strong>1.18 个百分点</strong>，其中项目内部结构贡献 +1.294 个百分点，运动权重差贡献 −0.109 个百分点。</p>
    <div id="lead-gender-bars" class="lead-bars" aria-label="正负贡献最大的各三个运动家族"></div>
    <p class="lead-note">显示正负贡献各前三项，单位为百分点。参赛和获奖均按运动员记录行。<a href="../08_女性结构分解/女性结构分解.html">查看分解与口径</a> · <a href="../08_女性结构分解/2024女性占比分解逐项目.csv">下载逐运动结果</a></p>
  </section>
</section>
<script id="panorama-lead-data" type="application/json">{data}</script>
<script defer src="panorama-lead.js"></script>
<!-- panorama-lead:end -->'''
html = page.read_text(encoding="utf-8")
html = re.sub(r"<!-- panorama-lead:start -->.*?<!-- panorama-lead:end -->\n?", "", html, flags=re.S)
marker = '<section class="narrative-chapter" data-story-label="一届切面" id="explore-panorama-2">'
assert html.count(marker) == 1
page.write_text(html.replace(marker, block + "\n" + marker, 1), encoding="utf-8", newline="\n")
