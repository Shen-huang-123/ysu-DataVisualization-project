from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
ROOT=Path(__file__).resolve().parents[2]; TASK=ROOT/'交付文件'/'任务三_专题深挖'/'S3_冠军的保质期'; FIG=TASK/'04_核心图表'; OUT=TASK/'01_报告与说明'/'S3_冠军的保质期_正式报告.pdf'
pdfmetrics.registerFont(TTFont('中',r'C:\Windows\Fonts\simhei.ttf')); pdfmetrics.registerFont(TTFont('中粗',r'C:\Windows\Fonts\simhei.ttf'))
纸=HexColor('#F7F3EB'); 墨=HexColor('#172A30'); 金=HexColor('#C4903D'); 红=HexColor('#A64155'); 青=HexColor('#247487'); 灰=HexColor('#68777D'); 线=HexColor('#D9DEDC')
def 背景(c,w,h): c.setFillColor(纸); c.rect(0,0,w,h,fill=1,stroke=0)
def 换行(c,txt,x,y,w,size=10,lead=16,color=墨,font='中'):
    c.setFont(font,size); c.setFillColor(color); line=''
    for ch in txt:
        if stringWidth(line+ch,font,size)>w and line: c.drawString(x,y,line); y-=lead; line=ch
        else: line+=ch
    if line:c.drawString(x,y,line); y-=lead
    return y
def 图(c,path,x,y,w,h):
    im=ImageReader(str(path)); iw,ih=im.getSize(); s=min(w/iw,h/ih); c.drawImage(im,x+(w-iw*s)/2,y+(h-ih*s)/2,iw*s,ih*s,mask='auto')
def 页眉(c,w,h,序,题,页):
    c.setFillColor(金); c.setFont('中粗',9); c.drawString(40,h-34,序); c.setFillColor(墨); c.setFont('中粗',22); c.drawString(40,h-65,题); c.setStrokeColor(线); c.line(40,h-80,w-40,h-80); c.setFont('中',8); c.setFillColor(灰); c.drawRightString(w-40,24,f'{页:02d}  /  冠军的保质期')
w,h=A4; c=canvas.Canvas(str(OUT),pagesize=A4,pageCompression=1); c.setTitle('冠军的保质期'); c.setAuthor('晓组织｜燕山大学')
背景(c,w,h); c.setFillColor(金); c.setFont('中粗',11); c.drawString(42,h-48,'任务三 · 创新专题'); c.setFillColor(墨); c.setFont('中粗',34); c.drawString(42,h-112,'冠军的保质期'); c.setFillColor(青); c.setFont('中粗',18); c.drawString(42,h-148,'一个国家能守住同一小项多久？'); 图(c,FIG/'S3_最长冠军王朝.png',35,220,w-70,420); 换行(c,'把金牌史改写成控制权转移史：研究卫冕、王朝与优势衰退。',42,170,w-84,13,21,墨,'中粗'); 换行(c,'晓组织｜燕山大学｜张子涵60%｜陈旭40%',42,88,w-84,9,14,灰); c.showPage()
背景(c,w,h); 页眉(c,w,h,'研究问题','从奖牌数量转向优势寿命',2); y=h-118; y=换行(c,'核心发现',40,y,w-80,17,24,青,'中粗'); y=换行(c,'1896—2016年可比范围内，共识别615个小项身份和4,511次相邻届冠军控制权转换。总体只有29.5%的冠军成功延续控制权。现代阶段的延续率为27.7%，低于早期的35.6%。',40,y-8,w-80,11,19); y=换行(c,'方法定义',40,y-16,w-80,17,24,青,'中粗');
for t in ['研究单位：体育大类与具体小项的组合。','控制权延续：相邻两次出现时，金牌NOC集合存在交集。','冠军王朝：必须是同一个NOC连续夺得该小项金牌。','排除1906；2020小项字段泛化，2024命名体系不同，不进入纵向主分析。']: y=换行(c,'• '+t,48,y-4,w-96,10,17)
c.showPage()
pages=[('时代变化','冠军越来越难长期守住','S3_时代卫冕率.png','控制权延续率从早期的35.6%下降到现代阶段的27.7%。这不是“竞技水平下降”，而是更多国家进入竞争、训练知识扩散与项目专业化共同形成的更高流动性。'),('项目差异','有些项目天然容易形成王朝','S3_项目王朝差异.png','跳水、射箭、田径和游泳更容易形成连续优势；拳击、射击和帆船的冠军更替更频繁。体育强国不是一种统一能力，而是一组寿命不同的项目优势。'),('王朝档案','最长统治期跨越数十年','S3_最长冠军王朝.png','美国男子撑竿跳高连续控制16届，是样本中的最长王朝。美国跳水、肯尼亚男子3000米障碍、匈牙利男子个人佩剑等也形成跨世代优势。')]
for i,(序,题,图片,正文) in enumerate(pages,3): 背景(c,w,h); 页眉(c,w,h,序,题,i); 图(c,FIG/图片,40,270,w-80,420); 换行(c,正文,40,225,w-80,10.5,18); c.showPage()
背景(c,w,h); 页眉(c,w,h,'结论','金牌是瞬间，王朝是结构',6); y=h-125; y=换行(c,'冠军王朝并不只是连续出现的名字。它往往意味着训练体系、人才管线、技术知识和国内竞争共同维持了跨世代优势。与此同时，七成以上的冠军控制权会在下一次比较时更换，奥运格局的常态不是垄断，而是流动。',40,y,w-80,12,21); y=换行(c,'交互延伸',40,y-22,w-80,17,24,青,'中粗'); y=换行(c,'配套“冠军王朝时间轴”支持按代表团、体育项目和连续届数筛选。评委可以从总体结论进入具体王朝，核对每一条故事线。',40,y,w-80,11,19); y=换行(c,'边界提醒',40,y-20,w-80,17,24,青,'中粗'); 换行(c,'项目命名变化可能切断真实连续性，因此本专题采取保守识别：宁可少认一段王朝，也不把不同项目错误拼接。并列金牌按集合处理，但王朝严格要求同一NOC连续出现。',40,y,w-80,10.5,18); c.showPage(); c.save(); print(OUT)
