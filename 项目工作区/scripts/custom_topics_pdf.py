"""Create a concise PDF companion for the data-backed S7–S10 supplement."""
from pathlib import Path
import re
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'交付文件/任务三_专题深挖'
SOURCE=BASE/'自拟专题_深度复核报告.md'
OUT=BASE/'自拟专题_深度复核报告.pdf'
font=Path('C:/Windows/Fonts/msyh.ttc')
if not font.exists():font=Path('C:/Windows/Fonts/simhei.ttf')
pdfmetrics.registerFont(TTFont('CJK',str(font)))
ink=HexColor('#173b42');muted=HexColor('#5a7074');accent=HexColor('#a87336')
styles={
 'title':ParagraphStyle('title',fontName='CJK',fontSize=24,leading=32,textColor=ink,spaceAfter=18),
 'h2':ParagraphStyle('h2',fontName='CJK',fontSize=15,leading=22,textColor=ink,spaceBefore=16,spaceAfter=10),
 'body':ParagraphStyle('body',fontName='CJK',fontSize=10.5,leading=17,textColor=ink,firstLineIndent=21,spaceAfter=8),
 'small':ParagraphStyle('small',fontName='CJK',fontSize=8.5,leading=13,textColor=muted,spaceAfter=9),
}
def clean(s):
 s=escape(s)
 s=re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',s)
 s=re.sub(r'`([^`]+)`',r'\1',s)
 s=re.sub(r'\[([^]]+)\]\(([^)]+)\)',r'\1',s)
 return s
def footer(canv,doc):
 canv.saveState();canv.setStrokeColor(HexColor('#cedbd6'));canv.line(44,42,A4[0]-44,42)
 canv.setFont('CJK',8);canv.setFillColor(muted);canv.drawString(44,28,'晓组织 · 燕山大学  /  自拟专题深度复核')
 canv.drawRightString(A4[0]-44,28,str(doc.page));canv.restoreState()
story=[];buf=[]
def flush():
 if buf:
  story.append(Paragraph(clean(''.join(buf)),styles['body']));buf.clear()
for line in SOURCE.read_text(encoding='utf-8').splitlines():
 line=line.strip()
 if not line:flush();continue
 if line.startswith('# '):flush();story.append(Paragraph(clean(line[2:]),styles['title']));continue
 if line.startswith('## '):flush();story.append(Paragraph(clean(line[3:]),styles['h2']));continue
 if line.startswith('!['):
  flush();m=re.match(r'!\[([^]]+)\]\(([^)]+)\)',line)
  if m:
   p=BASE/m.group(2)
   from PIL import Image as PILImage
   with PILImage.open(p) as im: w,h=im.size
   target=480;story.append(Image(str(p),width=target,height=target*h/w));story.append(Paragraph(m.group(1),styles['small']))
  continue
 buf.append(line)
flush()
doc=SimpleDocTemplate(str(OUT),pagesize=A4,leftMargin=46,rightMargin=46,topMargin=46,bottomMargin=56,title='自拟专题深度复核报告',author='晓组织')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(OUT)
