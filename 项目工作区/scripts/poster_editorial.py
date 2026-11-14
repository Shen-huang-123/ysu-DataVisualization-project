"""A2 editorial data poster, rebuilt from submitted tables."""
from pathlib import Path
import csv
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A2
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import shutil
import subprocess
from PIL import Image, ImageOps
from reportlab.lib.utils import ImageReader

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'交付文件/最终提交材料/海报'
OUT.mkdir(parents=True,exist_ok=True)
PDF=OUT/'百年圣火_A2海报_正式版.pdf'
PNG=OUT/'百年圣火_A2海报_正式版_预览.png'
pdfmetrics.registerFont(TTFont('CN',r'C:\Windows\Fonts\msyh.ttc',subfontIndex=0))
pdfmetrics.registerFont(TTFont('CNBold',r'C:\Windows\Fonts\msyhbd.ttc',subfontIndex=0))
pdfmetrics.registerFont(TTFont('Number',r'C:\Windows\Fonts\arial.ttf'))
W,H=A2
NAVY=HexColor('#102b3d'); INK=HexColor('#163243'); MUTE=HexColor('#506574')
PAPER=HexColor('#f5f4ef'); WHITE=HexColor('#ffffff'); GOLD=HexColor('#e2a53c')
TEAL=HexColor('#087f84'); CORAL=HexColor('#c5574b'); GRID=HexColor('#d6dedc')

def text(c,s,x,y,size=14,color=INK,bold=False,font=None):
 c.setFillColor(color);c.setFont(font or ('CNBold' if bold else 'CN'),size);c.drawString(x,y,str(s))
def line(c,x1,y1,x2,y2,color=GRID,width=1):
 c.setStrokeColor(color);c.setLineWidth(width);c.line(x1,y1,x2,y2)
def circle(c,x,y,r,fill):
 c.setFillColor(fill);c.circle(x,y,r,stroke=0,fill=1)
def section(c,n,eyebrow,title,y):
 text(c,f'{n:02d}',70,y,16,GOLD,True,font='Number')
 text(c,eyebrow,115,y,13,TEAL,True)
 text(c,title,70,y-43,27,INK,True)

rows={r['NOC']:r for r in csv.DictReader(open(ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力/02_数据表/S2_2024双口径完整排名.csv',encoding='utf-8-sig'))}
c=canvas.Canvas(str(PDF),pagesize=A2,pageCompression=1)
c.setTitle('百年圣火｜谁被看见：A2数据分析海报')
c.setAuthor('晓组织 · 燕山大学')
c.setFillColor(PAPER);c.rect(0,0,W,H,fill=1,stroke=0)

# Title band: a diagonal editorial collision between type and the actual venue.
c.setFillColor(NAVY);c.rect(0,H-386,W,386,fill=1,stroke=0)
photo=ROOT/'交付文件/任务三_专题深挖/媒体/sports.jpg'
with Image.open(photo) as source:
 cropped=ImageOps.fit(source.convert('RGB'),(1280,772),method=Image.Resampling.LANCZOS,centering=(.53,.53))
 c.saveState()
 mask=c.beginPath();mask.moveTo(682,H-386);mask.lineTo(832,H);mask.lineTo(W,H);mask.lineTo(W,H-386);mask.close()
 c.clipPath(mask,stroke=0,fill=0)
 c.drawImage(ImageReader(cropped),628,H-386,width=W-628,height=386,mask='auto')
 c.restoreState()
line(c,682,H-386,832,H,GOLD,4)
text(c,'百年圣火 / 数说奥运',70,H-61,12,GOLD,True)
text(c,'1896—2024  ·  夏季奥运数据观察',70,H-92,13,WHITE)
text(c,'谁被看见，',68,H-197,58,WHITE,True)
text(c,'取决于我们在数什么。',68,H-273,58,WHITE,True)
text(c,'换一种计数，奖牌榜就换一种答案。',72,H-327,16,HexColor('#c8d9db'))
line(c,70,H-366,W-70,H-366,HexColor('#587080'),1)
text(c,'晓组织  /  燕山大学',71,H-376,10,HexColor('#b9cace'))

# Measurement strip.
for i,(big,label) in enumerate([('252,565','原始参赛记录'),('329','巴黎2024奖牌小项'),('4,511','跨届冠军转移')]):
 x=72+i*365
 text(c,big,x,H-451,35,INK,True,font='Number')
 text(c,label,x,H-478,12,MUTE)
 if i<2:line(c,x+325,H-474,x+325,H-413,GRID)

# Section 1: exact rank slope chart.
section(c,1,'口径实验 / 2024','同一届奖牌榜，换一种计数就换了一种排名',H-550)
text(c,'官方小项口径：每个获胜小项计一枚金牌。运动员行口径：每名获奖成员各计一行。',72,H-617,13,MUTE)
left,right=340,825
text(c,'官方小项金牌排名',left-84,H-672,15,INK,True)
text(c,'运动员金牌行排名',right-85,H-672,15,INK,True)
circle(c,1030,H-666,5,TEAL);text(c,'名次上升',1040,H-670,10,MUTE)
circle(c,1030,H-683,5,CORAL);text(c,'名次下降',1040,H-687,10,MUTE)
line(c,left,H-690,left,H-980,GRID,2);line(c,right,H-690,right,H-980,GRID,2)
text(c,'+10',69,H-895,97,HexColor('#e5e1d7'),True,font='Number')
selected=[('日本','JPN'),('荷兰','NED'),('西班牙','ESP')]
for name,noc in selected:
 r=rows[noc];a=int(r['official_rank']);b=int(r['row_rank'])
 y1=H-704-(a-1)*17.5;y2=H-704-(b-1)*17.5
 color=CORAL if b>a else (TEAL if b<a else HexColor('#7f9295'))
 line(c,left,y1,right,y2,color,3)
 circle(c,left,y1,7,color);circle(c,right,y2,7,color)
 text(c,f'{name}  #{a}',left-142,y1-5,14,color,True)
 text(c,f'#{b}  {name}',right+21,y2-5,14,color,True)
text(c,'西班牙：官方第15 → 运动员行第5',72,H-1011,17,TEAL,True)
text(c,'多人项目放大了获奖成员数。40行金牌记录只对应5枚官方小项金牌。',72,H-1038,12,MUTE)

# Section 2: three denominators, no deceptive common horizontal scale.
line(c,70,H-1074,W-70,H-1074,GRID)
section(c,2,'结构差 / 2024','人数接近平衡，项目机会仍有缺口',H-1120)
text(c,'三条比例采用不同分母，因此比较的是结构位置，不能直接相减为“个人机会差”。',72,H-1184,13,MUTE)
barx=423;barw=580
for i,(lab,pct,detail,col) in enumerate([
 ('女性参赛记录',49.1,'参赛记录中的女性占比',TEAL),
 ('女性奖牌记录',50.3,'奖牌记录中的女性占比',TEAL),
 ('女子专属小项',45.9,'329项中女子专属小项占比',CORAL),
]):
 y=H-1240-i*67
 text(c,lab,74,y+4,17,INK,True)
 text(c,detail,74,y-18,10,MUTE)
 c.setFillColor(GRID);c.roundRect(barx,y-2,barw,20,10,fill=1,stroke=0)
 c.setFillColor(col);c.roundRect(barx,y-2,barw*pct/60,20,10,fill=1,stroke=0)
 line(c,barx+barw*50/60,y-10,barx+barw*50/60,y+27,NAVY,.9)
 text(c,f'{pct:.1f}%',barx+barw+20,y,19,col,True,font='Number')
text(c,'50% 参照线',barx+barw*50/60-47,H-1436,10,MUTE)

# Section 3: distribution rather than a single decorative headline number.
line(c,70,H-1458,W-70,H-1458,GRID)
text(c,'03',70,H-1483,16,GOLD,True,font='Number')
text(c,'跨届验证 / 1896—2024',115,H-1483,13,TEAL,True)
text(c,'冠军王朝，少数人的长跑',70,H-1515,24,INK,True)
text(c,'3,833段连续占有期，仅20.8%跨越至少两届；基础是4,511次可比较转移。',72,H-1541,12,MUTE)
for i in range(100):
 x=72+i*(1044/100)
 c.setFillColor(GOLD if i<21 else GRID)
 c.roundRect(x,H-1579,7,18,3,fill=1,stroke=0)
text(c,'20.8% 跨届延续',72,H-1593,11,INK,True)
text(c,'79.2% 仅一届',950,H-1593,11,MUTE,True)

# Print footer, source and scope.
c.setFillColor(NAVY);c.rect(0,0,W,80,fill=1,stroke=0)
text(c,'口径与来源',70,53,13,GOLD,True)
text(c,'Kaggle Summer Olympics Medals (1896—2024)；巴黎2024官方329小项结果；主分析排除1906。',70,33,10,WHITE)
text(c,'完整核验与代码见任务一；王朝为连续届次代理。封面摄影：DarDarCH / Wikimedia Commons / CC0。',70,17,9,HexColor('#c8d9db'))
text(c,'张子涵 60%  /  陈旭 40%',926,52,10,WHITE)
c.showPage();c.save()

try:
 import fitz
 doc=fitz.open(PDF); pix=doc[0].get_pixmap(matrix=fitz.Matrix(1.1,1.1),alpha=False)
 pix.save(PNG)
except ImportError:
 poppler=shutil.which('pdftoppm') or r'C:\Users\z8596\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe'
 if Path(poppler).is_file():
  subprocess.run([poppler,'-f','1','-singlefile','-png','-r','90',str(PDF),str(PNG.with_suffix(''))],check=True)
print(PDF)
print(PNG)
