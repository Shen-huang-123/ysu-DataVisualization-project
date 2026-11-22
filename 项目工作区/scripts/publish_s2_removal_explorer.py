"""Embed existing leave-one-sport-out results in the offline medal lab."""
from pathlib import Path
from html import escape
import csv
import json
import re

from task2_localization import SPORT_ZH

ROOT = Path(__file__).resolve().parents[2]
TASK = ROOT / '交付文件/任务三_专题深挖/S2_口径的魔力'
TABLE = TASK / '02_数据表/S2_2024代表团剔除敏感性.csv'
PAGE = TASK / '09_奖牌口径实验室/index.html'

def publish():
    scenarios = {}
    with TABLE.open(encoding='utf-8-sig', newline='') as file:
        for row in csv.DictReader(file):
            family = row['removed_family']
            shifts = scenarios.setdefault(family, {})
            assert row['NOC'] not in shifts
            shifts[row['NOC']] = int(row['rank_shift_rows_minus_official'])
    assert len(scenarios) == 36
    assert scenarios['none']['ESP'] == -10 and scenarios['Football']['ESP'] == -3
    families = sorted(set(scenarios) - {'none'})
    options = ''.join(f'<option value="{escape(key)}">{escape(SPORT_ZH.get(key, key))}</option>' for key in families)
    data = json.dumps(scenarios, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c')
    section = f"""
<!-- S2_REMOVAL_START -->
<section id="sport-removal" aria-labelledby="sport-removal-title" style="border-top:1px solid currentColor;padding-top:1rem;margin-top:1rem">
<h3 id="sport-removal-title">剔除一项运动，名次差还在吗？</h3>
<p>在两张榜同时移除同一运动，再比较官方小项榜与运动员行榜。上方仍显示完整榜。</p>
<div id="sport-removal-controls" hidden>
<label for="removed-sport">剔除的运动</label>
<select id="removed-sport" style="width:100%;margin-block:.4rem;min-height:44px"><option value="none">不剔除运动</option>{options}</select>
</div>
<p id="sport-removal-result" role="status" aria-live="polite" aria-atomic="true">西班牙完整样本上升 10 位，剔除足球后仍上升 3 位。</p>
<details id="sport-removal-audit" hidden>
<summary>比较全部单项剔除</summary>
<p id="sport-removal-summary"></p>
<div style="overflow:auto;max-height:24rem">
<table style="width:100%">
<thead><tr><th scope="col">剔除的运动</th><th scope="col">运动员行榜相对小项榜</th><th scope="col">相对完整样本</th></tr></thead>
<tbody id="sport-removal-comparison"></tbody>
</table>
</div>
</details>
<p>剔除试验使用共同匹配样本。名次差来自全榜重排，多个剔除结果不能相加。</p>
<p><a href="../02_数据表/{TABLE.name}" download>下载逐运动剔除结果</a> · <a href="../西班牙双口径案例.html">查看西班牙运动构成与原始数据</a></p>
<script type="application/json" id="sport-removal-data">{data}</script>
<script>
(() => {{
  const entry = document.getElementById('sport-removal');
  const choice = entry.querySelector('#removed-sport');
  const result = entry.querySelector('#sport-removal-result');
  const audit = entry.querySelector('#sport-removal-audit');
  const summary = entry.querySelector('#sport-removal-summary');
  const comparison = entry.querySelector('#sport-removal-comparison');
  const sports = Array.from(choice.options).slice(1);
  const focus = document.getElementById('case-select');
  const name = document.getElementById('case-name');
  const scenarios = JSON.parse(entry.querySelector('#sport-removal-data').textContent);
  const url = new URL(location.href);
  if (Object.hasOwn(scenarios, url.searchParams.get('exclude'))) {{
    choice.value = url.searchParams.get('exclude');
  }}
  function describe(shift) {{
    if (shift === 0) return '名次相同';
    return (shift < 0 ? '上升 ' : '下降 ') + Math.abs(shift) + ' 位';
  }}
  function relativeToBaseline(shift, baseline) {{
    const change = baseline - shift;
    return change === 0 ? '持平' : '相对名次' + (change > 0 ? '提高 ' : '降低 ') + Math.abs(change) + ' 位';
  }}
  function renderComparison(noc, baseline) {{
    const comparable = sports
      .map(option => ({{option, shift: scenarios[option.value][noc]}}))
      .filter(item => item.shift !== undefined)
      .sort((left, right) => Math.abs(right.shift - baseline) - Math.abs(left.shift - baseline));
    audit.hidden = comparable.length === 0;
    const count = comparable.filter(item => Math.sign(item.shift) === Math.sign(baseline)).length;
    summary.textContent = '可比较 ' + comparable.length + ' / ' + sports.length +
      ' 项，其中 ' + count + ' 项与完整样本的升降方向相同（含持平）。按名次差变化幅度排列。';
    const rows = comparable.map(({{option, shift}}) => {{
      const row = document.createElement('tr');
      const label = document.createElement('th');
      label.scope = 'row';
      label.textContent = option.textContent + (option.value === choice.value ? '（当前）' : '');
      row.append(label);
      for (const value of [describe(shift), relativeToBaseline(shift, baseline)]) {{
        row.insertCell().textContent = value;
      }}
      return row;
    }});
    comparison.replaceChildren(...rows);
  }}
  function render() {{
    const noc = focus.value;
    if (!noc) return;
    const label = focus.selectedOptions[0].textContent;
    const baseline = scenarios.none[noc];
    const shift = scenarios[choice.value][noc];
    if (baseline === undefined) {{
      audit.hidden = true;
      comparison.replaceChildren();
      result.textContent = label + '未列入逐运动剔除复核表。';
      return;
    }}
    const scenario = choice.value === 'none' ? '完整样本' : '剔除' + choice.selectedOptions[0].textContent + '后';
    const reading = shift === undefined ? '该情景无可比记录' : describe(shift);
    result.textContent = label + ' · ' + scenario + '：' + reading + '。完整样本：' + describe(baseline) + '。';
    renderComparison(noc, baseline);
  }}
  choice.addEventListener('change', () => {{
    const target = new URL(location.href);
    if (choice.value === 'none') target.searchParams.delete('exclude');
    else target.searchParams.set('exclude', choice.value);
    history.replaceState(history.state, '', target);
    render();
  }});
  focus.addEventListener('change', render);
  new MutationObserver(render).observe(name, {{childList: true, subtree: true}});
  entry.querySelector('#sport-removal-controls').hidden = false;
  render();
}})();
</script>
<!-- S2_REMOVAL_END -->
"""
    html = PAGE.read_text(encoding='utf-8')
    html = re.sub(r'\s*<!-- S2_REMOVAL_START -->.*?<!-- S2_REMOVAL_END -->\n?', '', html, flags=re.S)
    marker = '<p id="robust-note"></p>'
    assert html.count(marker) == 1
    PAGE.write_text(html.replace(marker, marker + section), encoding='utf-8')

if __name__ == '__main__':
    publish()
