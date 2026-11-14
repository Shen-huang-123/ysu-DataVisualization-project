from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth

ROOT=Path(__file__).resolve().parents[2]; TASK=ROOT/'交付文件'/'任务三_专题深挖'/'S2_口径的魔力'; FIG=TASK/'04_核心图表'; OUT=TASK/'01_报告与说明'/'S2_口径的魔力_正式报告.pdf'
pdfmetrics.registerFont(TTFont('CN',r'C:\Windows\Fonts\simhei.ttf')); pdfmetrics.registerFont(TTFont('CNB',r'C:\Windows\Fonts\simhei.ttf'))
P={'paper':HexColor('#F7F3EB'),'ink':HexColor('#172A30'),'teal':HexColor('#247487'),'red':HexColor('#A64155'),'gold':HexColor('#C4903D'),'grey':HexColor('#68777D'),'line':HexColor('#D9DEDC')}
def bg(c,w,h): c.setFillColor(P['paper']); c.rect(0,0,w,h,fill=1,stroke=0)
def wrap(c,text,x,y,maxw,size=10,leading=16,color=None,font='CN'):
    c.setFont(font,size); c.setFillColor(color or P['ink']); line=''; lines=[]
    for ch in text:
        if stringWidth(line+ch,font,size)>maxw and line: lines.append(line); line=ch
        else: line+=ch
    if line: lines.append(line)
    for ln in lines: c.drawString(x,y,ln); y-=leading
    return y
def header(c,w,h,kicker,title,page):
    c.setFillColor(P['gold']); c.setFont('CNB',9); c.drawString(40,h-34,kicker)
    size=22
    while stringWidth(title,'CNB',size)>w-80 and size>15:size-=1
    c.setFillColor(P['ink']); c.setFont('CNB',size); c.drawString(40,h-65,title); c.setStrokeColor(P['line']); c.line(40,h-80,w-40,h-80)
    c.setFont('CN',8); c.setFillColor(P['grey']); c.drawRightString(w-40,24,f'{page:02d}  /  S2 口径的魔力')
def image_fit(c,path,x,y,w,h):
    im=ImageReader(str(path)); iw,ih=im.getSize(); s=min(w/iw,h/ih); nw,nh=iw*s,ih*s; c.drawImage(im,x+(w-nw)/2,y+(h-nh)/2,nw,nh,mask='auto')
def note(c,w,text): c.setStrokeColor(P['line']); c.line(40,48,w-40,48); wrap(c,text,40,37,w-80,7.2,9,P['grey'])

w,h=portrait(A4); c=canvas.Canvas(str(OUT),pagesize=(w,h),pageCompression=1); c.setTitle('S2 口径的魔力'); c.setAuthor('晓组织｜燕山大学')
# Cover
bg(c,w,h); c.setFillColor(P['gold']); c.setFont('CNB',12); c.drawString(40,h-45,'任务三 · 专题深挖')
c.setFillColor(P['ink']); c.setFont('CNB',34); c.drawString(40,h-105,'口径的魔力')
c.setFillColor(P['teal']); c.setFont('CNB',18); c.drawString(40,h-138,'奖牌榜究竟在奖励什么？')
image_fit(c,FIG/'00_S2专题英雄图.png',35,215,w-70,440)
wrap(c,'同一组比赛结果，在竞赛单元与获奖者两种统计单位下，会形成两套不同但各自合理的秩序。',40,170,w-80,13,21,P['ink'],'CNB')
wrap(c,'晓组织｜燕山大学｜张子涵60%｜陈旭40%',40,85,w-80,9.5,15,P['grey']); c.showPage()
# Abstract
bg(c,w,h); header(c,w,h,'摘要','摘要与研究设计',2); y=h-115
y=wrap(c,'摘要',40,y,w-80,16,23,P['teal'],'CNB'); y=wrap(c,'2024巴黎奥运官方小项口径与运动员行口径产生显著不同的奖牌榜。荷兰由官方第6升至行口径第3，西班牙由第15升至第5，日本由第3降至第9。两种计数对多人获奖组赋予不同权重；仅用2024官方329小项做35次逐运动大类剔除，关键代表团重排方向均未反转。',40,y-6,w-80,10.5,17)
y-=20; y=wrap(c,'数据与口径',40,y,w-80,16,23,P['teal'],'CNB')
for b in ['官方口径：任务一整理的2024官方329小项获奖结果。','运动员行口径：2024年2,281条运动员奖牌记录。','两种榜单均按金、银、铜依次排序，并列取最小名次，排除AIN。','多人获奖组：同NOC–Event–Medal下记录数大于1。']:
    y=wrap(c,'• '+b,48,y-3,w-96,9.7,16)
note(c,w,'官方结果包含329个金牌单元、330个银牌单元和385个铜牌单元；银铜增加来自并列与双铜牌制度。'); c.showPage()
pages=[
('排名重排','只换统计单位，奖牌榜就会重排','S2_双口径排名重排.png','美国、中国在两种口径中仍居前两位，但荷兰从官方第6升至行口径第3，西班牙从第15升至第5；日本从第3降至第9，乌兹别克斯坦从第13降至第19。行口径系统性提高多人项目冠军的权重。','官方与行口径均按金银铜排序，排除AIN；右侧保留左侧官方前15名的实际行口径名次。'),
('作用机制','多人获奖结构改变计数权重','S2_多人项目与金牌行膨胀.png','西班牙5枚官方金牌对应40条金牌记录，荷兰15枚对应67条，美国40枚对应131条，中国40枚对应71条。多人组贡献占比与金牌行膨胀倍数相关0.973，两指标共用金牌行数，故这是结构描述，不作独立机制验证。','倍率称为每枚官方金牌对应的运动员金牌记录数，不是平均队伍人数；独立敏感性见最后一页。'),
('两个问题','两套口径回答两个不同问题','S2_金牌数量与获奖者规模.png','官方口径回答“赢下多少小项”，运动员行口径回答“产生多少获奖者记录”。没有脱离问题的唯一公平榜：评价竞技项目结果应使用官方口径，评价奖牌覆盖到多少运动员可以使用行口径。','官方金牌数来自329小项表；金牌记录来自归一数据。相同颜色名称不代表相同统计单位。'),
('项目结构','相同金牌数背后，是不同的获奖者结构','S2_代表团金牌记录项目结构.png','荷兰的曲棍球和赛艇、西班牙的足球和水球、法国的柔道与团队球类、美国的田径游泳与篮球，共同解释了行口径中的放大。行口径偏爱的不是某个国家，而是多人夺冠结构。','数字为体育大类运动员金牌记录数，不是官方金牌数。1906不涉及本专题。')]
p=3
for kicker,title,img,body,foot in pages:
    bg(c,w,h); header(c,w,h,kicker,title,p); image_fit(c,FIG/img,40,270,w-80,430); wrap(c,body,40,230,w-80,10.2,17); note(c,w,foot); c.showPage(); p+=1
bg(c,w,h); header(c,w,h,'三种口径','从二选一到三种可解释口径',p)
image_fit(c,FIG/'S2_三口径排名路径.png',40,275,w-80,425)
wrap(c,'官方小项口径让每个竞赛单元计1枚；团队内均分口径把同一NOC–Event–Medal组的1枚奖牌平均分给该组运动员；运动员行口径让每名获奖者各计1次。均分口径既保留运动员贡献，也避免团队人数机械放大奖牌。',40,230,w-80,10.2,17)
note(c,w,'三套口径各有用途：官方口径评价竞赛结果，均分口径评价团队内份额，行口径评价获奖者覆盖规模。'); c.showPage(); p+=1
bg(c,w,h); header(c,w,h,'稳健性验证','只用2024官方小项的35次剔除检验',p)
image_fit(c,FIG/'S2_2024逐大类剔除稳健性.png',40,275,w-80,425)
wrap(c,'只用2024官方329小项及同届运动员记录，每次剔除一个运动大类，重算两套榜单。完整数据Kendall τ为0.931；35次剔除后为0.908—0.938。西班牙、荷兰始终因行口径上升，日本、乌兹别克斯坦始终后移。核心结论无需依赖尚未逐项核实的2008—2016历史奖牌。',40,230,w-80,10.2,17)
note(c,w,'历史三届仍含555项未获现行一手逐项核验，仅作内部口径探索，不承担2024正式结论的证据责任。'); c.showPage(); p+=1
c.save(); print(OUT)
