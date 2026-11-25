from pathlib import Path
from bs4 import BeautifulSoup
from html import escape
import csv
from collections import Counter
ROOT=Path(__file__).resolve().parents[2]
folder=ROOT/'交付文件/任务三_专题深挖/11_结论稳定性地图'
with (folder/'十专题结论稳定性矩阵.csv').open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f))
p=folder/'index.html';s=BeautifulSoup(p.read_text('utf-8'),'html.parser')
target=s.select_one('.stability-list') or s.select_one('.hero img');assert target
counts = Counter(row['状态'] for row in rows)
filters = [('all', '全部', len(rows)), ('sensitive', '口径敏感', counts['口径敏感']),
           ('uncertain', '证据不足', counts['证据不足'])]
missing = {'S1': '主场净收益的因果效应尚未识别。',
           'S6': '缺少逐人身份核验，个人历史榜暂不可验证。',
           'S7': '尚未识别卫冕率变化背后的运动员个人机制。'}
parts = ['<section class="stability-list" aria-labelledby="matrix-title"><h2 id="matrix-title">十个直觉，核验后还能说什么？</h2>'
         '<p>按证据状态筛选，展开专题可查看反例、核验方法和推断边界。状态针对原判断。</p>'
         '<fieldset class="matrix-filters"><legend>证据状态</legend>']
for key, label, count in filters:
 checked = ' checked' if key == 'all' else ''
 parts.append(f'<input type="radio" name="matrix-status" id="matrix-{key}"{checked}/>'
              f'<label for="matrix-{key}">{label} <span>{count}</span></label>')
parts.append('</fieldset><div class="matrix-head" aria-hidden="true"><span>专题</span><span>原判断</span>'
             '<span>核验结果</span><span>证据状态</span><span></span></div><div class="stability-rows">')
for r in rows:
 status = r['状态']
 tone = {'口径敏感': 'sensitive', '证据不足': 'uncertain'}[status]
 topic = escape(r['专题'])
 entry = escape(r['证据入口'], quote=True)
 gap = f'<p><b>待核验</b> {escape(missing[topic])}</p>' if topic in missing else ''
 parts.append(f"""<details class="matrix-row {tone}">
<summary><span class="matrix-topic">{topic}</span><span class="matrix-origin">{escape(r['未经检验的直觉'])}</span>
<strong class="matrix-result">{escape(r['修正后结论'])}</strong><span class="matrix-status">{escape(status)}</span></summary>
<div class="matrix-evidence"><p><b>反例与交叉证据</b> {escape(r['最关键的交叉证据'])}</p>
<p><b>核验口径</b> {escape(r['替代口径或核验'])}</p>
<p><b>推断边界</b> {escape(r['推断边界'])}</p>{gap}
<a href="../{entry}">查看专题反例与依据 ↗</a></div></details>""")
parts.append('</div><p class="stability-download"><a href="十专题结论稳定性矩阵.csv" download>下载核验矩阵 CSV ↓</a> · <a href="结论稳定性地图.png" id="matrix-preview-open">预览原始地图 ↗</a> · <a href="结论稳定性地图.png" download>下载 PNG ↓</a></p>')
parts.append("""
<dialog id="matrix-preview" aria-label="原始结论稳定性地图预览">
<form method="dialog"><button autofocus>关闭预览</button></form>
<img alt="十个专题的原判断及证据状态" data-src="结论稳定性地图.png"/>
</dialog>
<script>
(() => {
  const dialog = document.getElementById('matrix-preview');
  const link = document.getElementById('matrix-preview-open');
  link.addEventListener('click', (event) => {
    if (!dialog.showModal || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    const image = dialog.querySelector('img');
    if (!image.hasAttribute('src')) image.src = image.dataset.src;
    dialog.showModal();
  });
  dialog.addEventListener('click', (event) => {
    if (event.target === dialog) dialog.close();
  });
})();
</script>
</section>
""")
target.replace_with(BeautifulSoup(''.join(parts),'html.parser'))
s.body['class']=list(dict.fromkeys(s.body.get('class',[])+['stability-map-motion']))
link=s.select_one('#stability-map-motion-style')
if link is None:
 link=s.new_tag('link',id='stability-map-motion-style',rel='stylesheet')
 s.head.append(link)
link['href']='../../共享组件/stability-map-motion.css?v=6'
p.write_text(str(s),'utf-8')

from publish_stability_case_map import publish as publish_case_map
publish_case_map()
