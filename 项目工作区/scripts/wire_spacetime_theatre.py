"""Idempotently connect the spatial presentation to existing site navigation."""
from pathlib import Path

root=Path(__file__).resolve().parents[2]
task=root/'交付文件/任务四_开放创作/index.html'
s=task.read_text(encoding='utf-8')
link='<a href="08_奥运时空剧场/index.html" data-no="06"><small>空间叙事</small><h3>沿着举办地走过百年</h3><p>拖动三维地球，选择届次、代表团与运动，观察历史如何发生。</p><strong>进入奥运时空剧场 ↗</strong></a>'
if link not in s:
    start=s.index('data-no="05"')
    end=s.index('</a>',start)+4
    s=s[:end]+link+s[end:]
    s=s.replace('五种进入方式','六种进入方式',1)
    task.write_text(s,encoding='utf-8')

home=root/'index.html'
s=home.read_text(encoding='utf-8')
old='href="交付文件/任务四_开放创作/07_ECharts大屏/index.html"'
new='href="交付文件/任务四_开放创作/08_奥运时空剧场/index.html"'
if old in s and new not in s:
    s=s.replace(old,new,1).replace('打开奥运数据大屏','进入奥运时空剧场',1)
    home.write_text(s,encoding='utf-8')

screen=root/'交付文件/任务四_开放创作/07_ECharts大屏/screen.template.html'
s=screen.read_text(encoding='utf-8')
link='<a href="../08_奥运时空剧场/index.html">时空剧场 ↗</a>'
if link not in s:
    s=s.replace('<a href="../index.html">返回任务四 ↗</a>',link+'<a href="../index.html">返回任务四 ↗</a>',1)
    screen.write_text(s,encoding='utf-8')
