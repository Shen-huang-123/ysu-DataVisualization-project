from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[2]
p=root/'交付文件/任务三_专题深挖/S2_口径的魔力/09_奖牌口径实验室/index.html'
s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
style=s.select_one('#medal-lab-background')
if not style:
 style=s.new_tag('style',id='medal-lab-background');s.head.append(style)
style.string="""/* Local reading surface: no decorative water ribbons behind evidence. */
html body{background:#182128!important;background-image:none!important}
html body .oa-world,html body .immersive-float-layer{display:none!important}
html body::before,html body::after{background:none!important;background-image:none!important;box-shadow:none!important}
html body.xz-dark{background:#182128!important}
"""
p.write_text(str(s),encoding='utf-8')
