"""Add the large-screen presentation to the site's existing navigation."""
from pathlib import Path

root = Path(__file__).resolve().parents[2]
task = root / '交付文件/任务四_开放创作/index.html'
text = task.read_text(encoding='utf-8')
link = '<a href="07_ECharts大屏/index.html" data-no="05"><small>现场演示</small><h3>一屏看见百年奥运</h3><p>用 ECharts 串起参赛规模、女性参与、双口径榜与洛杉矶预测区间。</p><strong>打开数据大屏 ↗</strong></a>'
if link not in text:
    start = text.index('data-no="04"')
    end = text.index('</a>', start) + 4
    text = text[:end] + link + text[end:]
    text = text.replace('四种进入方式', '五种进入方式', 1)
    task.write_text(text, encoding='utf-8')

home = root / 'index.html'
text = home.read_text(encoding='utf-8')
href = '交付文件/任务四_开放创作/07_ECharts大屏/index.html'
link = f'<a class="voyage-cta" href="{href}" style="margin-left:12px;background:transparent;border:1px solid currentColor">打开奥运数据大屏<span aria-hidden="true">↗</span></a>'
if href not in text:
    start = text.index('data-scene="5"')
    end = text.index('</a>', text.index('class="voyage-cta"', start)) + 4
    text = text[:end] + link + text[end:]
    home.write_text(text, encoding='utf-8')
