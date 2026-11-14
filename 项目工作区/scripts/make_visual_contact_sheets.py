from pathlib import Path
from PIL import Image,ImageDraw,ImageFont

root=Path(__file__).resolve().parents[2]/'项目工作区/视觉验收'
names=['总入口','任务一','任务二','任务三','任务四','S1','S2','S3','S4','S5','S6','S7','S8','S9','S10']
font=ImageFont.truetype(r'C:\Windows\Fonts\msyh.ttc',18)
for width in (1440,390):
 for mode in ('light','dark'):
  for screen in (0,1):
   cellw=330 if width==1440 else 210
   cellh=260 if width==1440 else 470
   cols=5
   sheet=Image.new('RGB',(cols*cellw,3*cellh),'#e8e8e8')
   draw=ImageDraw.Draw(sheet)
   for i,name in enumerate(names):
    file=root/f'{name}_{width}_{mode}_{screen}.png'
    if not file.exists():continue
    im=Image.open(file).convert('RGB')
    im.thumbnail((cellw-16,cellh-38))
    x=(i%cols)*cellw+(cellw-im.width)//2;y=(i//cols)*cellh+31
    sheet.paste(im,(x,y))
    draw.text(((i%cols)*cellw+8,(i//cols)*cellh+5),name,font=font,fill='#162f38')
   sheet.save(root/f'总览_{width}_{mode}_{screen}.jpg',quality=85)
