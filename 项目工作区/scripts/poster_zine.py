"""A2 Olympic data zine: tactile collage with vector, auditable charts."""
from pathlib import Path
import csv, math, random, shutil, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageOps, ImageEnhance
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A2
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'交付文件/最终提交材料/海报'
OUT.mkdir(parents=True,exist_ok=True)
PDF=OUT/'百年圣火_A2海报_正式版.pdf'
PNG=OUT/'百年圣火_A2海报_正式版_预览.png'
W,H=A2; SCALE=2.15
PAPER='#eee7d8'; BLACK=HexColor('#24211e'); BLUE=HexColor('#a83d24')
RED=HexColor('#d17131'); MUTED=HexColor('#5f5a51'); RULE=HexColor('#b6ad9e')
pdfmetrics.registerFont(TTFont('Song',r'C:\Windows\Fonts\FZSTK.TTF'))
pdfmetrics.registerFont(TTFont('Hei',r'C:\Windows\Fonts\msyh.ttc',subfontIndex=0))
pdfmetrics.registerFont(TTFont('HeiBold',r'C:\Windows\Fonts\msyhbd.ttc',subfontIndex=0))
pdfmetrics.registerFont(TTFont('Type',r'C:\Windows\Fonts\cour.ttf'))

def bg_image():
 w,h=round(W*SCALE),round(H*SCALE)
 rng=np.random.default_rng(20241109)
 grain=rng.normal(0,3.7,(h,w,1))
 cloud=Image.fromarray(np.uint8(np.clip(rng.normal(127,22,(105,78)),0,255)),'L')
 cloud=cloud.resize((w,h),Image.Resampling.BICUBIC).filter(ImageFilter.GaussianBlur(13))
 cloud=(np.asarray(cloud,dtype=np.float32).reshape(h,w,1)-127)*.075
 base=np.array([238,231,216],dtype=np.float32).reshape(1,1,3)
 arr=np.uint8(np.clip(base+grain+cloud,0,255))
 im=Image.fromarray(arr,'RGB')
 d=ImageDraw.Draw(im,'RGBA')
 for _ in range(1600):
  x=int(rng.integers(0,w));y=int(rng.integers(0,h))
  if rng.random()<.6:
   r=int(rng.integers(1,3));d.ellipse((x,y,x+r,y+r),fill=(78,67,50,int(rng.integers(9,35))))
 for _ in range(1700):
  x=int(rng.integers(0,w));y=int(rng.integers(0,h))
  length=int(rng.integers(2,12))
  d.line((x,y,x+length,y+int(rng.integers(-2,3))),fill=(87,72,55,int(rng.integers(5,16))),width=1)
 # Irregular opening: original sport photograph remains truthful inside it.
 mask=Image.new('L',(w,h),0);md=ImageDraw.Draw(mask)
 rr=random.Random(2397)
 def wave(v,phase):return 9*math.sin(v/39+phase)+4*math.sin(v/13+phase*2)+rr.uniform(-2.2,2.2)
 top=[(x,round((410-.055*(x-600)+wave(x,1))*SCALE)) for x in range(48,1150,6)]
 right=[(round((1140+wave(y,2))*SCALE),round(y*SCALE)) for y in range(390,1212,6)]
 bottom=[(x,round((1235-.055*(x-600)+wave(x,3))*SCALE)) for x in range(1138,47,-6)]
 left=[(round((57+wave(y,4))*SCALE),round(y*SCALE)) for y in range(1265,445,-6)]
 md.polygon(top+right+bottom+left,fill=255)
 mask=mask.filter(ImageFilter.GaussianBlur(1.2*SCALE))
 outer=mask.filter(ImageFilter.MaxFilter(35))
 shadow=outer.filter(ImageFilter.GaussianBlur(18))
 im.paste(Image.new('RGB',(w,h),(171,157,137)),(0,0),Image.eval(shadow,lambda v:int(v*.30)))
 torn=Image.new('RGB',(w,h),(251,246,235))
 im.paste(torn,(0,0),Image.eval(outer,lambda v:max(0,v-100)))
 photo=Image.open(ROOT/'交付文件/任务三_专题深挖/媒体/lens.jpg').convert('RGB')
 # Warm print grading makes the photograph and paper read as one visual surface.
 toned=ImageOps.colorize(ImageOps.grayscale(photo),black='#211d1a',white='#e9d6b8')
 photo=Image.blend(toned,photo,.12)
 photo=ImageEnhance.Contrast(photo).enhance(1.11)
 region=ImageOps.fit(photo,(round(1115*SCALE),round(965*SCALE)),Image.Resampling.LANCZOS,centering=(.50,.50))
 layer=Image.new('RGB',(w,h));layer.paste(region,(round(42*SCALE),round(345*SCALE)))
 im.paste(layer,(0,0),mask)
 # Fibres on the torn edge; they follow the contour, never the data region.
 ed=ImageDraw.Draw(im,'RGBA')
 # Sparse warm paper flecks keep the cut edge readable at print size.
 for p in top[::2]+left[::3]+right[::4]+bottom[::3]:
  x,y=p;ed.ellipse((x-3,y-3,x+3,y+3),fill=(250,245,233,155))
 return im

def t(c,s,x,y,size=12,font='Hei',color=BLACK):
 c.setFont(font,size);c.setFillColor(color);c.drawString(x,y,s)
def ln(c,x1,y1,x2,y2,color=RULE,width=1):
 c.setStrokeColor(color);c.setLineWidth(width);c.line(x1,y1,x2,y2)

rank={r['NOC']:r for r in csv.DictReader(open(ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力/02_数据表/S2_2024双口径完整排名.csv',encoding='utf-8-sig'))}
esp=rank['ESP']
c=canvas.Canvas(str(PDF),pagesize=A2,pageCompression=1)
c.setTitle('百年圣火｜谁被看见｜A2数据艺术海报')
c.setAuthor('晓组织 · 燕山大学')
c.drawImage(ImageReader(bg_image()),0,0,width=W,height=H,mask='auto')

# Zine cover. Art and evidence have separate reading distances.
t(c,'谁被看见？',57,H-239,124,'Song',BLACK)
t(c,'换一种计数，奖牌榜就换一种答案。',72,H-307,23,'HeiBold',BLACK)
t(c,'奥运一百余年，胜利如何被记录？',75,H-346,17,'Hei',MUTED)
t(c,'一场交锋，两种口径。',74,H-1300,20,'HeiBold',BLACK)
t(c,'西班牙 · 2024 金牌榜排名',78,H-1355,13,'Hei',MUTED)
t(c,str(esp['official_rank']).zfill(2),75,H-1498,145,'Song',BLACK)
t(c,'→',325,H-1479,73,'Song',RED)
t(c,str(esp['row_rank']).zfill(2),505,H-1498,145,'Song',BLUE)
t(c,f"官方小项 {esp['Gold_official']} 金  /  运动员获奖 {esp['Gold_rows']} 行",79,H-1527,12,'Hei',MUTED)

# Exhibition-style colophon: this is a campaign image, with the evidence in the work.
t(c,'1896—2028',75,H-1605,32,'Song',BLACK)
t(c,'百年全景  /  十个专题  /  交互档案  /  洛杉矶2028情景预测',465,H-1601,11,'Hei',MUTED)
t(c,'历史数据截至2024；2028为预测情景。完整方法、图表与来源见作品报告。',76,H-1644,9,'Hei',MUTED)
c.showPage();c.save()
poppler=shutil.which('pdftoppm') or r'C:\Users\z8596\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe'
if Path(poppler).is_file():subprocess.run([poppler,'-f','1','-singlefile','-png','-r','90',str(PDF),str(PNG.with_suffix(''))],check=True)
print(PDF)
