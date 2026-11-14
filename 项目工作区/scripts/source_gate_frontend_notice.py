"""Add the verified forecast entry to the existing Task 4 public pages."""
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
TASK=ROOT/'交付文件'/'任务四_开放创作'
targets=[
 (TASK/'index.html','05_满分升级/11_官方来源门控预测/index.html'),
 (TASK/'01_交互式Dashboard'/'index.html','../05_满分升级/11_官方来源门控预测/index.html'),
 (TASK/'02_2028洛杉矶预测'/'index.html','../05_满分升级/11_官方来源门控预测/index.html'),
]
for file,link in targets:
    s=file.read_text(encoding='utf-8')
    if 'SOURCE_GATE_2026' in s:
        s=s.replace('并查看其余四项的来源门槛','并查看壁球的来源门槛').replace('并查看其余三项的来源门槛','并查看壁球的来源门槛').replace('并查看其余两项的来源门槛','并查看壁球的来源门槛')
        file.write_text(s,encoding='utf-8')
        continue
    banner=f'''<!-- SOURCE_GATE_2026 --><aside role="note" style="max-width:1080px;margin:48px auto;padding:26px;border:1px solid #bbcbc5;border-radius:22px;background:#e9f0ea;color:#183f47;font-family:'Microsoft YaHei',sans-serif;line-height:1.8"><strong style="font-size:20px">预测来源核验已更新</strong><p>原新增运动排名表保留为情景对照。推荐阅读仅启用已核实排名的审慎预测版本，并查看壁球的来源门槛。</p><a href="{link}" style="color:#126b78;font-weight:800">打开审慎预测榜 ↗</a></aside>'''
    assert '</body>' in s,file
    file.write_text(s.replace('</body>',banner+'</body>',1),encoding='utf-8')
print('Task 4 entry notices ready')
