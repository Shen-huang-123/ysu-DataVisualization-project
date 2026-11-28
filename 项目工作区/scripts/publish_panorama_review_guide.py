from pathlib import Path
import re

root = Path(__file__).resolve().parents[2] / '交付文件' / '任务二_百年全景'
page = root / '05_交互总览/index.html'
text = page.read_text(encoding='utf-8')

def insert(tag, marker, block, start=0):
    global text
    text = re.sub(rf'<!-- {tag}:start -->.*?<!-- {tag}:end -->\n?', '', text, flags=re.S)
    i = text.index(marker, start)
    text = text[:i]+f'<!-- {tag}:start -->\n{block}\n<!-- {tag}:end -->\n'+text[i:]

# Set the final cover layout before deferred controls are installed.
legacy_cover = '<header class="photo-editorial-hero">'
photo = '../../任务三_专题深挖/媒体/sports.jpg'
stable_cover = (
    '<header class="photo-editorial-hero image-stage" style="--image-stage-position:center 48%">'
    f'<img class="image-stage-photo" src="{photo}" alt="" aria-hidden="true" data-no-zoom="" fetchpriority="high">'
)
text = text.replace(legacy_cover, stable_cover, 1)
assert text.count(stable_cover) == 1
text = text.replace('href="../../任务三_专题深挖/媒体/la.jpg" rel="preload"', f'href="{photo}" rel="preload"')
for version in ('20261115-narrative', '20261115-atmosphere'):
    text = text.replace(f'exploration-design.js?v={version}', 'exploration-design.js?v=20261128-cover')

insert('review-guide', '<div aria-label="探索历史的观察角度"', '''
<nav id="panorama-review-guide" aria-labelledby="review-guide-title">
<h3 id="review-guide-title">四个分析场景</h3>
<ul><li><a href="#panorama-lead"><b aria-hidden="true">A</b>选届次，看奖牌分布</a></li>
<li><a href="#team-share-case"><b aria-hidden="true">B</b>选代表团，比记录与份额</a></li>
<li><a href="#panorama-gender"><b aria-hidden="true">C</b>追查女性占比的运动来源</a></li>
<li><a href="../10_百年项目星系/index.html#turnover-preset"><b aria-hidden="true">D</b>看相邻届次更替</a></li></ul>
</nav>
''')
insert('review-a', '<div class="lead-drilldown">', '''

<div class="analysis-actions" data-analysis="a"><button type="button" data-copy>复制当前分析链接</button><button type="button" data-export>导出当前对照 CSV</button><span role="status"></span></div>
<label>固定基准届 <select id="lead-baseline"></select></label><div id="lead-comparison" aria-live="polite"></div>
<div class="panorama-plots">
<section><h4>获奖代表团数</h4><div class="panorama-plot" id="lead-trend-0" role="img" aria-label="逐届获奖代表团数"></div></section>
<section><h4>前五代表团份额</h4><div class="panorama-plot" id="lead-trend-1" role="img" aria-label="逐届前五代表团获奖份额"></div></section>
<section><h4>有效获奖代表团数</h4><div class="panorama-plot" id="lead-trend-2" role="img" aria-label="逐届有效获奖代表团数"></div></section>
</div><p class="lead-note">点击任一图中的届次，或使用上方下拉框，同步更新三个指标、当届前五和所选代表团的运动构成。</p>
''')
insert('review-b', '</section>', '''
<h4>换一个代表团，查看两条曲线</h4>
<label>代表团 <select id="history-team"></select></label>
<div class="analysis-actions" data-analysis="b"><button type="button" data-copy>复制当前分析链接</button><button type="button" data-export>导出当前对照 CSV</button><span role="status"></span></div>

<div class="panorama-plots">
<section><h4>获奖运动员记录（条）</h4><div class="panorama-plot" id="history-count-plot" role="img" aria-label="代表团逐届获奖记录数"></div></section>
<section><h4>占当届全部获奖记录的份额（%）</h4><div class="panorama-plot" id="history-share-plot" role="img" aria-label="代表团逐届获奖份额"></div></section>
</div>
<p>圆点标出两个指标反向变化的后一届。缺席留空，参赛零获奖保留为 0，历史代表团代码分别统计。</p>
<p id="history-opposite" aria-live="polite"></p>
''', text.index('id="team-share-case"'))
insert('review-c', '</section>', '''
<h4>代表团差值从哪些运动来？</h4>
<div id="women-examples" aria-label="代表团案例"></div>
<div class="analysis-actions" data-analysis="c"><button type="button" data-copy>复制当前分析链接</button><button type="button" data-export>导出当前对照 CSV</button><span role="status"></span></div>

<label>巴黎 2024 代表团 <select id="women-team"></select></label>
<label>对照代表团 <select id="women-compare"></select></label>
<div id="women-denominators" class="women-comparison" aria-live="polite"></div>
<div class="women-sport-table"><table>
<thead><tr><th scope="col">运动</th><th scope="col" id="women-primary-title">主选队</th><th scope="col" id="women-compare-title">对照队</th></tr></thead>
<tbody id="women-sport-rows"></tbody></table></div>
<p class="lead-note">各运动贡献＝该运动女性获奖行 ÷ 本队全部获奖行 − 该运动女性参赛行 ÷ 本队全部参赛行。各项贡献可相加为本队占比差，运动按两队绝对贡献的最大值排序。两队使用同一比例尺，小分母会放大比例波动。</p>
''', text.index('id="panorama-gender"'))
insert('review-assets', '</head>', '''
<link rel="stylesheet" href="panorama-guide.css?v=3">
<style id="panorama-stable-entry">
@view-transition { navigation: none; }
</style>
<script defer src="../../任务四_开放创作/07_ECharts大屏/vendor/echarts.min.js"></script>
''')
insert('review-script', '</body>', '<script defer src="panorama-guide.js?v=2"></script>')
page.write_text(text, encoding='utf-8', newline='\n')
