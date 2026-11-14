"""Build a review PDF, A2 poster, and presentation script from computed outputs."""
from pathlib import Path
import textwrap
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from PIL import Image
R=Path(__file__).resolve().parents[1]; O=R/'outputs'; D=R/'deliverables';D.mkdir(exist_ok=True)
plt.rcParams['font.family']='Microsoft YaHei'
sections=[('数据质量与统计口径',R/'docs/数据质量与口径方案.md'),('百年全景',R/'docs/全景分析正文草稿.md'),('统计尺度如何改变排名',R/'docs/S2双口径初步发现.md'),('主办与表现',R/'docs/S1东道主分析.md')]
figures=['A_medal_rows','A_edition_scale','B_country_trends','C_female_records','C_country_female_structure','D_sport_presence','S2_2024_comparison','S2_same_rule_ranks','S1_host_windows']
with PdfPages(D/'百年圣火_评审稿.pdf') as pdf:
 fig=plt.figure(figsize=(8.27,11.69),facecolor='#faf9f6')
 fig.text(.10,.84,'百年圣火\n谁被看见',fontsize=36,weight='bold',color='#246477',linespacing=1.5)
 fig.text(.10,.59,'1896—2024 夏季奥运可视分析',fontsize=17)
 abstract='奥运会的扩张、女性参与和奖牌竞争并非彼此孤立。本作品首先审计原始记录，保留历史代表团与数据质量标记，再比较运动员行与小项奖牌尺度。2024年案例表明，即使统一排名规则，统计单位仍显著改变名次。九个主办案例同时呈现增长与反例，提示主场提升及其持续性不能一概而论。所有结论区分记录数、人数和官方奖牌数，明确外部来源与未解决的信息缺口。'
 fig.text(.10,.47,'摘要\n'+ '\n'.join(textwrap.wrap(abstract,34)),fontsize=12,va='top',linespacing=1.7)
 fig.text(.10,.12,'历史排版稿 · 请优先阅读图文评审稿\n2024官方小项与团队信息见各任务最新交付\n视频成片及提交渠道仍待确认',fontsize=11,color='#666');pdf.savefig(fig);plt.close(fig)
 page=1
 for title,path in sections:
  lines=[]
  for line in path.read_text(encoding='utf-8').splitlines():
   if line.startswith('|') or line.startswith('核心图') or line.startswith('产物：'):continue
   if not line.strip(): lines.append('');continue
   lines.extend(textwrap.wrap(line.lstrip('# '),42,break_long_words=True,break_on_hyphens=False))
  for start in range(0,len(lines),42):
   page+=1;fig=plt.figure(figsize=(8.27,11.69),facecolor='#faf9f6');fig.text(.08,.94,title,fontsize=20,weight='bold',color='#246477')
   fig.text(.08,.88,'\n'.join(lines[start:start+42]),fontsize=10,va='top',linespacing=1.65)
   fig.text(.88,.035,str(page),fontsize=9);pdf.savefig(fig);plt.close(fig)
 for name in figures:
  page+=1;fig=plt.figure(figsize=(8.27,11.69),facecolor='#faf9f6');ax=fig.add_axes([.03,.10,.94,.82]);ax.imshow(Image.open(O/'figures'/f'{name}.png'));ax.axis('off');fig.text(.08,.93,'分析图表',fontsize=18,color='#246477');fig.text(.88,.035,str(page),fontsize=9);pdf.savefig(fig);plt.close(fig)
assert page<=20,page
fig=plt.figure(figsize=(16.54,23.39),facecolor='#faf9f6')
fig.text(.07,.95,'百年圣火，谁被看见？',fontsize=39,weight='bold',color='#246477')
fig.text(.07,.914,'128年奥运史中的扩张、女性参与与统计尺度',fontsize=20)
for rect,name in [([.06,.65,.88,.23],'C_female_records'),([.06,.32,.88,.30],'S2_same_rule_ranks')]:
 ax=fig.add_axes(rect);ax.imshow(Image.open(O/'figures'/f'{name}.png'));ax.axis('off')
fig.text(.08,.27,'一个排名，取决于你在数什么',fontsize=26,weight='bold',color='#a23d52')
fig.text(.08,.23,'相同金牌排名规则下：西班牙15→5，荷兰6→3，日本3→9。\n团体成员各占一行，因此奖牌记录数不能冒充官方奖牌数。',fontsize=18,linespacing=1.6)
fig.text(.08,.13,'边界与来源',fontsize=19,weight='bold')
fig.text(.08,.09,'原始数据：Kaggle Summer Olympics Medals (1896–2024)及其上游。\n主分析排除1906；参赛占比按记录行；2024小项结果见任务一外部结果层。\n衍生数据许可：CC BY-NC-SA 4.0。',fontsize=12,linespacing=1.7)
fig.savefig(D/'百年圣火_A2海报_评审稿.pdf');fig.savefig(D/'百年圣火_A2海报_预览.png',dpi=90);plt.close(fig)
(D/'视频讲解脚本.md').write_text('''# 展示视频脚本 约四分钟

0:00—0:30 展示海报。提出问题：同一届奥运，为什么换一种数法，强国排名就变了？

0:30—1:10 展示数据审计。解释一行是一名运动员参加一个小项，团体成员各占一行；说明ID冲突、项目改名、1906排除和重复候选保留。

1:10—2:00 展示全景。介绍参赛记录和代表团扩张、女性记录占比达到49.10%，强调不是独立人数；国家曲线缺席断开、历史NOC不合并。

2:00—3:00 展示同规则排名图。解释西班牙15到5、荷兰6到3、日本3到9；两侧均只按金牌数排名。展示荷兰曲棍球及赛艇记录构成。2024年已接入329个小项的外部结果层；原CSV的泛化Event仍不能逆推出小项。

3:00—3:40 展示主办前后曲线。中国提升，巴西反例，英国后届继续增长。明确九个选择案例与描述性比较的边界。

3:40—4:00 展示复现入口与局限。核心统计由CSV重现，外部表保留来源快照。结束于结论：先声明在数什么，再解释谁领先。
''',encoding='utf-8')
print(f'Report pages: {page}; A2 PDF and video script generated')
