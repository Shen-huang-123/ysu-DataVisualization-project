from pathlib import Path
import re

task = Path(__file__).resolve().parents[2]/'交付文件'/'任务二_百年全景'
page = task/'11_四视角独立交付/四视角核心图复核.html'
text = page.read_text(encoding='utf-8')
if 'id="core-review-layout"' not in text:
    reference = (task/'12_固定运动构成/固定运动构成复核.html').read_text(encoding='utf-8')
    nav = re.search(r'<nav aria-label="作品导航" id="xz-nav".*?</aside>', reference)[0]
    assets = '\n'.join(re.search(pattern,reference)[0] for pattern in (
        r'<link[^>]+id="supplement-assets"[^>]*>',
        r'<script id="supplement-theme-preload">.*?</script>',
        r'<script[^>]*src="[^"]*supplement-reading.js[^"]*"[^>]*></script>',
        r'<link[^>]+id="supp-task-nav-assets"[^>]*>',
        r'<script[^>]*src="[^"]*integrated-nav.js[^"]*"[^>]*></script>',
        r'<link[^>]+id="chart-surface-theme"[^>]*>',
    ))
    head = f"""<!doctype html>
<html lang="zh-CN">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>百年全景四视角图表复核</title>
{assets}
<link id="core-review-layout" rel="stylesheet" href="core-review.css">
</head>
<body class="supplement-reading">
{nav}
"""
    i = text.index('<main>')
    text = head + text[i:]
    text = text.replace('<main><h1>百年全景四项必选视角复核</h1><p><a', '<main class="core-review"><header class="core-review-head"><p><a',1)
    text = text.replace('返回完整报告</a></p><nav aria-label="四视角导航">','返回完整报告</a></p><h1>四视角图表复核</h1></header><nav class="core-view-nav" aria-label="四视角导航">',1)
    text = re.sub(r'独立解读含 \d+ 个汉字，配 \d+ 张图。', '', text)
    text = re.sub(r'<details(?: open(?:="")?)?><summary>两张图与完整解读</summary><h1>(.*?)</h1>',
                  r'<details class="core-baseline" open><summary>基础图表与解读</summary><h3>\1</h3>',text)
    text = re.sub(r'<img (?![^>]*class=)([^>]+?)(\s*/?)>',r'<img class="chart-surface" \1\2>',text)
    if '</body>' not in text:
        text = text.replace('</html>','</body></html>') if '</html>' in text else text+'\n</body></html>\n'
    page.write_text(text,encoding='utf-8',newline='\n')
