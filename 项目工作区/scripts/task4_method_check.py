from pathlib import Path
from urllib.parse import unquote,urlparse
import re

ROOT=Path(__file__).resolve().parents[2]
TASK=ROOT/'交付文件'/'任务四_开放创作'
page=TASK/'02_2028洛杉矶预测'/'index.html'
text=page.read_text(encoding='utf-8')
assert 'lang="zh-CN"' in text and 'aria-label="预测方法"' in text
assert '历史基线' in text and '项目级集成' in text
assert '2.74' in text and '0.52' in text
for raw in re.findall(r'(?:href|src)=["\']([^"\']+)["\']',text):
    url=urlparse(raw)
    if url.scheme or raw.startswith(('#','//')):continue
    target=(page.parent/unquote(url.path)).resolve()
    assert target.is_file(),raw
for other in (TASK/'index.html',TASK/'03_数据新闻'/'index.html'):
    other_text=other.read_text(encoding='utf-8')
    assert '预测方法与验证方案.md"' not in other_text
    assert '02_2028洛杉矶预测/index.html' in other_text
assert (ROOT/'项目工作区'/'sites'/'la28-fullscore'/'dist'/'任务四_开放创作'/'02_2028洛杉矶预测'/'index.html').is_file()
print('任务四方法网页、链接和站点副本检查通过')
