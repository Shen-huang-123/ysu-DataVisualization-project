from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, A2, portrait
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth

ROOT=Path(__file__).resolve().parents[2]
TASK=ROOT/'交付文件'/'任务二_百年全景'
FIG=TASK/'04_核心图表'
OUT=TASK/'01_报告与说明'
OUT.mkdir(parents=True,exist_ok=True)
REPORT=OUT/'任务二_百年奥运全景_正式报告.pdf'
POSTER=OUT/'任务二_百年奥运全景_A2海报.pdf'

pdfmetrics.registerFont(TTFont('CN',r'C:\Windows\Fonts\simhei.ttf'))
pdfmetrics.registerFont(TTFont('CNB',r'C:\Windows\Fonts\simhei.ttf'))
P={'paper':HexColor('#F7F3EB'),'ink':HexColor('#172A30'),'teal':HexColor('#247487'),'red':HexColor('#A64155'),'gold':HexColor('#C4903D'),'grey':HexColor('#68777D'),'line':HexColor('#D9DEDC')}

def bg(c,w,h): c.setFillColor(P['paper']); c.rect(0,0,w,h,fill=1,stroke=0)
def header(c,w,h,kicker,title,page=None):
    c.setFillColor(P['gold']); c.setFont('CNB',10); c.drawString(40,h-36,kicker)
    title_size=22
    while stringWidth(title,'CNB',title_size)>w-80 and title_size>15: title_size-=1
    c.setFillColor(P['ink']); c.setFont('CNB',title_size); c.drawString(40,h-67,title)
    c.setStrokeColor(P['line']); c.line(40,h-82,w-40,h-82)
    if page is not None:
        c.setFont('CN',8); c.setFillColor(P['grey']); c.drawRightString(w-40,24,f'{page:02d}  /  百年圣火')

def wrap(c,text,x,y,maxw,size=10,leading=16,color=None,font='CN'):
    c.setFont(font,size); c.setFillColor(color or P['ink']); line=''; lines=[]
    for ch in text:
        test=line+ch
        if stringWidth(test,font,size)>maxw and line: lines.append(line); line=ch
        else: line=test
    if line: lines.append(line)
    for ln in lines: c.drawString(x,y,ln); y-=leading
    return y

def image_fit(c,path,x,y,w,h):
    im=ImageReader(str(path)); iw,ih=im.getSize(); scale=min(w/iw,h/ih); nw,nh=iw*scale,ih*scale
    c.drawImage(im,x+(w-nw)/2,y+(h-nh)/2,nw,nh,mask='auto')

def footer_note(c,w,text):
    c.setStrokeColor(P['line']); c.line(40,47,w-40,47); wrap(c,text,40,36,w-80,7.5,10,P['grey'])

def make_report():
    w,h=portrait(A4); c=canvas.Canvas(str(REPORT),pagesize=(w,h),pageCompression=1)
    c.setTitle('任务二 百年奥运全景'); c.setAuthor('晓组织｜燕山大学')
    # 1 cover
    bg(c,w,h); image_fit(c,FIG/'00_封面总览英雄图.png',28,210,w-56,510)
    c.setFillColor(P['ink']); c.setFont('CNB',30); c.drawString(40,155,'百年圣火')
    c.setFont('CNB',15); c.setFillColor(P['teal']); c.drawString(40,125,'扩张、权力转移与结构性平权')
    wrap(c,'晓组织｜燕山大学｜张子涵 60%｜陈旭 40%',40,85,w-80,10,15,P['grey']); c.showPage()
    # 2 abstract
    bg(c,w,h); header(c,w,h,'EXECUTIVE SUMMARY','摘要与研究设计',2)
    y=h-120
    y=wrap(c,'摘要',40,y,w-80,16,24,P['teal'],'CNB')
    y=wrap(c,'1896至2024年，夏季奥运会由少数国家参与的精英赛事发展为覆盖206个代表团、329个小项的全球制度。参赛记录扩大39.2倍，但前五代表团的同届奖牌记录份额由83.9%降至41.8%，显示规模扩张伴随去集中化。2024年女性参赛记录占49.1%、女性奖牌记录占50.3%，而女子专属小项占45.9%，说明人数平权尚未完全转化为项目机会平权。九个现代主办案例中八个主办届份额上升，但项目贡献分解显示增益路径因国而异，不能把主办身份直接解释为因果。',40,y-8,w-80,10.3,17)
    y-=22; y=wrap(c,'统一口径',40,y,w-80,16,24,P['teal'],'CNB')
    bullets=['主分析使用运动员记录口径；团体项目每名获奖成员均形成记录。','排除1906；URS、GDR、FRG、GER等历史政体分别统计。','2020年Event字段泛化，不计算小项数；2024年采用官方329小项补充表。','无参赛记录留空，不自动视为零；描述性比较不冒充因果估计。']
    for b in bullets: y=wrap(c,'• '+b,48,y-4,w-96,9.5,16)
    c.showPage()
    pages=[
      ('A 规模与集中度','规模扩张没有带来同等程度的奖牌垄断','A_规模扩张与奖牌集中度.png','1896年只有380条参赛记录、12个代表团和143条运动员奖牌记录；到2024年分别达到14,892条、206个和2,281条。与此同时，前五代表团奖牌记录份额由83.9%下降到41.8%。绝对奖牌记录随项目与团体规模膨胀，但相对统治力长期下降。','运动员记录口径；前五份额用于同届比较，不等于官方小项奖牌份额。'),
      ('B 强国兴衰','历史不是连续曲线，而是战争、抵制与政体变迁留下的断点','B_十二代表团兴衰曲线.png','USA在1904年达到81%的异常高位，战后多数届次约为12%至16%；URS在1952年登场后迅速进入高位；CHN自1984年形成连续轨迹，2008年约9.0%，2024年约7.4%。将历史政体强行拼接，会把制度断点误写成平滑增长。','同届奖牌记录份额；缺席留空；纵轴35%，超限值用三角标注。'),
      ('B 准实验检验','匹配DID显示主办届存在稳定的相对提升','B_主场效应准实验检验.png','九个现代主办案例逐一匹配五个前届奖牌份额接近的非主办代表团。主办国前后变化减去匹配组同期变化后，平均DID为+2.70个百分点；案例自助法95%区间为[1.84, 3.59]。五万次组内随机指派未产生同等极端均值，前趋势平均差为0.24个百分点。证据比简单前后比较更强，但主办权并非随机，不能无条件外推为因果。','匹配变量为前届奖牌记录份额；九个案例、小样本、未控制体育投入与资格扩张。结论定位为准实验关联证据。'),
      ('B 扩展合成对照','扩展样本与严格敏感性检验仍支持正向关联','B_20届合成对照与稳健性.png','1948至2024年整理20个候选主办届，其中17届具备三个主办前届次的连续信息，14届达到严格的前拟合质量阈值。每届使用前三届奖牌份额与参赛份额拟合非负合成权重，并排除事件窗口内成为东道主的供体。高拟合样本的平均主办届差为+2.24个百分点，案例自助法95%区间为[1.30, 3.28]；剔除1956双城及1980、1984抵制届后仍为+2.52个百分点。','合成对照提高反事实可比性；后续路径使用完整平衡窗口。主办权仍非随机，不作自然实验或随机试验解释。'),
      ('C 女性平权','人数接近平权，不等于项目机会结构完全对称','C_女性三层平权曲线.png','2024年女性参赛记录占49.1%，女性奖牌记录占50.3%，但官方329个小项中女子专属小项为151个，占45.9%。混合小项、团体人数与项目设置使参赛、获奖和小项三种比例出现差异；三层指标共同展示进展，也保留结构性问题。','参与与获奖按主表Sex字段；2024小项性别属性来自官方补充表。'),
      ('D 项目演化','奥运项目表在扩容，也在持续退出与重返','D_项目新增退出重返流向.png','项目体系并非机械累加。早期更替频繁，随着制度成熟，连续保留成为主流；但近年仍可观察到新增、退出与重返。艺术比赛等历史项目消失，城市文化与青年项目进入。项目表是传统、全球普及度、性别平衡和青年吸引力之间的动态配置。','按归一体育大类识别首次出现、上届缺席后的重返及下届缺席。'),
      ('D 小项数量','从43到329：扩容主线中的口径控制','D_小项增长与项目更替.png','可比口径下，小项数从1896年的约43个增至1920年的158个、1984年的221个、2000年的300个，2024年达到官方329个。2020年留空是主动控制：原始Event已泛化，直接计数会制造虚假断崖。宁可披露不可比，也不把错误精确包装成趋势。','1896至2016按清洗后Event唯一值；2020不计；2024采用官方329项表。')]
    p=3
    for kicker,title,img,body,note in pages:
        bg(c,w,h); header(c,w,h,kicker,title,p); image_fit(c,FIG/img,40,260,w-80,450)
        wrap(c,body,40,225,w-80,10,16); footer_note(c,w,note); c.showPage(); p+=1
    # final
    bg(c,w,h); header(c,w,h,'结论','结论：扩张中的去集中化',p)
    image_fit(c,FIG/'00_封面总览英雄图.png',40,345,w-80,345)
    y=315
    y=wrap(c,'奥运百年发展的核心，不只是“更多”，而是覆盖更广、权力更分散、平权更接近，同时仍保留结构差异。规模扩张带来绝对奖牌记录通胀，却没有制造同等程度的强国垄断；强国格局在历史断点中重组；女性人数平权接近实现，但项目机会仍未完全对称；项目表则通过持续增删回应时代。',40,y,w-80,11,18)
    y=wrap(c,'交互版本：任务二_百年全景/05_交互总览/index.html（离线打开）',40,y-15,w-80,9.5,15,P['teal'],'CNB')
    footer_note(c,w,'数据与代码：任务一归一数据、2024官方329小项补充表、任务二复现脚本。全部结论均受所声明统计口径约束。')
    c.save()

def make_poster():
    w,h=portrait(A2); c=canvas.Canvas(str(POSTER),pagesize=(w,h),pageCompression=1); bg(c,w,h)
    c.setFillColor(P['gold']); c.setFont('CNB',20); c.drawString(56,h-54,'晓组织 · 燕山大学 · 数据可视化挑战赛')
    c.setFillColor(P['ink']); c.setFont('CNB',48); c.drawString(56,h-118,'百年圣火')
    c.setFont('CNB',23); c.setFillColor(P['teal']); c.drawString(56,h-156,'扩张、权力转移与结构性平权')
    image_fit(c,FIG/'00_封面总览英雄图.png',48,h-650,w-96,450)
    c.setFillColor(P['ink']); c.setFont('CNB',22); c.drawString(56,h-690,'三个结论，把“更多”变成“更懂”')
    col=(w-128)/2
    image_fit(c,FIG/'B_主场效应与项目贡献.png',48,h-1095,col,350)
    image_fit(c,FIG/'C_女性三层平权曲线.png',72+col,h-1095,col,350)
    image_fit(c,FIG/'D_项目新增退出重返流向.png',48,h-1475,w-96,320)
    y=170
    c.setFillColor(P['red']); c.setFont('CNB',19); c.drawString(56,y,'扩张 ≠ 垄断')
    wrap(c,'参赛记录扩大39.2倍，前五强份额却从83.9%降至41.8%。',56,y-28,230,11,17)
    c.setFillColor(P['teal']); c.setFont('CNB',19); c.drawString(330,y,'参与平权 ≠ 机会完全平权')
    wrap(c,'2024女性参赛占49.1%，女子专属小项占45.9%。',330,y-28,250,11,17)
    c.setFillColor(P['gold']); c.setFont('CNB',19); c.drawString(630,y,'主场身份 ≠ 必然增长')
    wrap(c,'九个现代案例八升一降，增益来自不同优势项目组合。',630,y-28,250,11,17)
    c.setStrokeColor(P['line']); c.line(56,75,w-56,75); c.setFillColor(P['grey']); c.setFont('CN',9)
    c.drawString(56,50,'1896—2024｜运动员记录口径｜排除1906｜2024小项采用官方329项表｜张子涵60% · 陈旭40%')
    c.save()

make_report(); make_poster(); print(REPORT); print(POSTER)
