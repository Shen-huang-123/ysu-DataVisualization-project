"""任务一提交版 PDF：将审计数据组织成可阅读的视觉报告。"""
from pathlib import Path
from html import escape
import csv

from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

ROOT=Path(__file__).resolve().parents[2]
TASK=ROOT/'交付文件'/'任务一_数据体检'
OUT=TASK/'01_报告与说明'/'任务一_数据质量与口径说明书.pdf'
W,H=A4
FONT='SourceHan'
BOLD='YaHeiBold'
pdfmetrics.registerFont(TTFont(FONT,r'C:\Windows\Fonts\SourceHanSansCN-Normal.ttf'))
pdfmetrics.registerFont(TTFont(BOLD,r'C:\Windows\Fonts\msyhbd.ttf'))

NAVY=HexColor('#102F38'); INK=HexColor('#19343D'); TEAL=HexColor('#187E88')
MINT=HexColor('#A3D8CC'); GOLD=HexColor('#CA9251'); RED=HexColor('#B85D64')
PAPER=HexColor('#F5F3EC'); WHITE=HexColor('#FFFFFF'); LINE=HexColor('#D9E2DF')
MUTED=HexColor('#5A7277'); PALE=HexColor('#E7F0EB')
M=42; CW=W-2*M

def box(c,x,top,w,h,fill,stroke=None,r=14):
    c.setFillColor(fill);c.setStrokeColor(stroke or fill)
    c.roundRect(x,H-top-h,w,h,r,fill=1,stroke=bool(stroke))

def text(c,s,x,top,size=11,color=INK,font=FONT):
    c.setFillColor(color);c.setFont(font,size);c.drawString(x,H-top-size,s)

def para(c,s,x,top,width,size=10.5,leading=17,color=INK,font=FONT):
    style=ParagraphStyle('p',fontName=font,fontSize=size,leading=leading,textColor=color,wordWrap='CJK')
    p=Paragraph(escape(str(s)),style)
    _,height=p.wrap(width,1000)
    p.drawOn(c,x,H-top-height)
    return top+height

def rule(c,top):
    c.setStrokeColor(LINE);c.setLineWidth(.75);c.line(M,H-top,W-M,H-top)

def page(c,n,section,title,subtitle=''):
    c.setFillColor(PAPER);c.rect(0,0,W,H,fill=1,stroke=0)
    box(c,M,42,66,25,NAVY,r=12)
    text(c,f'{n:02d} / 10',M+11,46,10,WHITE,BOLD)
    text(c,section,M+82,47,9.5,TEAL,BOLD)
    text(c,title,M,88,30,NAVY,BOLD)
    if subtitle:para(c,subtitle,M,135,CW,10.5,17,MUTED)
    rule(c,176)
    footer(c,n)

def footer(c,n):
    rule(c,796)
    text(c,'燕山大学 · 晓组织  /  数据体检与口径定义',M,806,8,MUTED)
    c.setFillColor(MUTED);c.setFont(BOLD,8);c.drawRightString(W-M,H-814,f'{n:02d} / 10')

def pill(c,s,x,top,w,fill=PALE,color=TEAL):
    box(c,x,top,w,23,fill,r=11)
    text(c,s,x+10,top+4,8.7,color,BOLD)

def metric(c,x,top,w,value,label,accent=TEAL):
    box(c,x,top,w,94,WHITE,LINE)
    text(c,value,x+16,top+15,31,accent,BOLD)
    para(c,label,x+16,top+58,w-32,9,14,MUTED)

def get_rows(path):
    with path.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))

def cover(c):
    c.setFillColor(NAVY);c.rect(0,0,W,H,fill=1,stroke=0)
    c.setStrokeColor(Color(.6,.87,.82,alpha=.20))
    for radius in (90,140,190):c.circle(W-66,H-170,radius,stroke=1,fill=0)
    text(c,'YANSHAN UNIVERSITY  /  晓组织',M,59,10,MINT,BOLD)
    box(c,M,102,127,28,Color(.35,.77,.72,alpha=.17),r=13)
    text(c,'任务一 · 数据基础',M+13,108,10,MINT,BOLD)
    text(c,'先把数据',M,174,57,WHITE,BOLD)
    text(c,'说清楚',M,245,57,MINT,BOLD)
    para(c,'奥运数据质量与统计口径说明书',M,345,CW,20,29,WHITE,BOLD)
    para(c,'1896—2024 夏季奥运 · 记录行、官方小项与特殊历史边界',M,383,CW,11.5,19,HexColor('#C8DDDA'))
    c.setStrokeColor(Color(.65,.85,.8,alpha=.4));c.line(M,H-451,W-M,H-451)
    cover_metrics=[('252,565','原始记录'),('38,360','主分析奖牌行'),('329','2024官方小项')]
    col=(CW-20)/3
    for i,(v,l) in enumerate(cover_metrics):
        x=M+i*(col+10);box(c,x,482,col,94,HexColor('#1E4952'))
        text(c,v,x+15,497,26,WHITE,BOLD);text(c,l,x+15,538,9,MINT)
    box(c,M,618,CW,105,HexColor('#1A4550'),r=18)
    text(c,'核心判断',M+20,638,12,GOLD,BOLD)
    para(c,'原始数据适合记录层面的历史分析。运动员获奖行不等于官方奖牌枚数；信息缺失的小项名称须标记风险，不能靠字符串去重补出官方结果。',M+20,664,CW-40,12,20,WHITE)
    text(c,'张子涵 60%  ·  陈旭 40%  ·  2026 年 11 月',M,777,9,MINT)
    c.showPage()

def quick_index(c):
    page(c,2,'评审抽查 / Q1–Q6','六类问题，从规则查到结果','代码及结果位于任务一目录。复算范围与边界见各条处理说明。')
    entries = [
        ('Q1 · 双口径', '巴黎美国：40 枚官方小项金牌对应 131 条金牌记录。百年趋势用获奖行，官方榜用小项。',
         '代码：同步2024官方小项.py、运行任务一.py｜结果：2024双口径敏感性.csv'),
        ('Q2 · 运动名称', '89 条逗号拼接 Sport 按运动家族与 Event 规则消解；按运动比较统一使用 sport_family。',
         '代码：prepare.py｜结果：体育大类归一映射表.csv'),
        ('Q3 · 小项泛化', '如 Men Team 无法单凭标签还原小项。历史相关届次降到大类或大类×性别；巴黎另接官方表。',
         '代码：prepare.py｜结果：event_quality_by_year.csv'),
        ('Q4 · 身份风险', '12,883 个 ID 对应多个姓名；670 个姓名跨逾 40 年。个体榜只展示待核候选。',
         '代码：audit.py｜结果：audit.json（id_multiple_names 等）'),
        ('Q5 · 历史特殊记录', '1906 届 458 条获奖行排除于主分析；1956 双城合并为一届。政体代码、ROC、AIN、EOR 分列。',
         '代码：audit.py、prepare.py｜结果：audit.json、preparation_summary.json'),
        ('Q6 · 多行、并列与缺色', '复跑得多行组 5,080、仅一色组 34；1908 男子 400 米仅有金。多行不能直接判为并列或团体；不补缺色。',
         '代码：抽查Q6.py｜结果：Q6抽查结果.json；巴黎小项口径按官方归属计数。'),
    ]
    for i,(title,decision,source) in enumerate(entries):
        top=176+i*96
        box(c,M,top,CW,88,WHITE,LINE)
        text(c,title,M+14,top+9,12,NAVY,BOLD)
        para(c,decision,M+14,top+29,CW-28,10,14,INK)
        para(c,source,M+14,top+62,CW-28,8.4,12,MUTED)
    footer(c,2)
    c.showPage()


def risks(c):
    page(c,3,'质量风险 / 一页总览','五个风险，五项处理决定','先看哪些字段会改变结论，再看我们如何限制推断。')
    rows=[
        ('01','小项粒度丢失','8,515 条需结合上下文；2024 官方共 329 项','外接官方小项结果层；禁止用泛化标签去重','高'),
        ('02','身份标识不可当人数','12,883 个 ID 对应多个姓名','只称参赛记录；独立运动员人数结论降级','高'),
        ('03','重复候选影响早期史','1,466 条去 ID 重复余量','主版保留；排除版只作敏感性检验','中'),
        ('04','历史边界不统一','1906、1956 双城、政体变迁','明确纳入标记；保留当届代表团身份','中'),
        ('05','运动名称漂移','76 个原值，89 条逗号拼接','完整映射；跨大类结合小项判断','中'),
    ]
    top=204
    for num,title,evidence,action,level in rows:
        box(c,M,top,CW,100,WHITE,LINE)
        box(c,M+15,top+17,40,34,NAVY,r=9);text(c,num,M+24,top+24,13,WHITE,BOLD)
        text(c,title,M+69,top+15,15,NAVY,BOLD)
        pill(c,level,W-M-47,top+16,33,HexColor('#FBE7E5') if level=='高' else HexColor('#F5EBDA'),RED if level=='高' else GOLD)
        para(c,'证据：'+evidence,M+69,top+43,CW-90,9.5,15,MUTED)
        para(c,'处理：'+action,M+69,top+65,CW-90,9.5,15,TEAL)
        top+=109
    c.showPage()

def medal(c):
    page(c,4,'统计口径 / 奖牌是什么','同一届奥运，两种排名','先定义统计单位，才谈榜单。运动员行与官方小项回答的是不同问题。')
    box(c,M,202,246,153,WHITE,LINE);box(c,M+260,202,246,153,WHITE,LINE)
    text(c,'运动员行口径',M+20,220,17,NAVY,BOLD)
    para(c,'一行是一名运动员在一届某小项的记录。获奖行代表获奖成员记录的广度；一支18人的冠军队可能产生18条金牌行。',M+20,256,206,10.5,17,INK)
    text(c,'官方小项口径',M+280,220,17,NAVY,BOLD)
    para(c,'一个代表团在一个比赛小项获一枚对应奖牌。2024年按329个官方小项核对；不能将团队成员行直接相加。',M+280,256,206,10.5,17,INK)
    box(c,M,375,CW,94,HexColor('#E3EFEB'))
    text(c,'2024 年最醒目的名次变化',M+19,391,11,TEAL,BOLD)
    text(c,'西班牙  15 → 5',M+19,419,28,NAVY,BOLD)
    para(c,'左：公布金牌名次；右：按运动员金牌行重排。差异与多人获奖结构有关，不应全归因于队伍规模。',M+285,403,205,10,16,MUTED)
    rows=[('美国','1','1'),('中国','2','2'),('荷兰','6','3'),('日本','3','9'),('西班牙','15','5')]
    text(c,'代表团',M+14,494,10,MUTED,BOLD);text(c,'官方金牌名次',M+203,494,10,MUTED,BOLD);text(c,'运动员行名次',M+363,494,10,MUTED,BOLD)
    rule(c,520)
    y=531
    for i,(name,official,athlete) in enumerate(rows):
        if i%2==0:box(c,M,y-4,CW,39,WHITE,r=5)
        text(c,name,M+14,y+4,11,INK,BOLD)
        text(c,official,M+230,y+4,11,INK,BOLD)
        text(c,athlete,M+400,y+4,11,TEAL,BOLD)
        y+=43
    para(c,'排名仅在同一金牌数降序规则下比较；同名次并列取最小名次。完整代表团表、官方小项来源和奖牌归一数据随交付文件提供。',M,764,CW,8.5,13,MUTED)
    c.showPage()

def normalization(c):
    page(c,5,'字段归一 / 信息边界','能映射的统一，丢失的标记','Sport 名称漂移和 2020 年起小项标签泛化，是两种不同的数据质量问题。')
    text(c,'运动大类：76 / 76 已映射',M,205,18,NAVY,BOLD)
    examples=[('Artistic Gymnastics','体操'),('Cycling Road / Track / BMX','自行车'),('Canoe Sprint / Slalom','皮划艇'),('Cycling Road, Triathlon','按具体小项判定')]
    y=246
    for src,dst in examples:
        box(c,M,y,CW,52,WHITE,LINE,r=9)
        para(c,src,M+15,y+17,230,9.5,14,MUTED)
        text(c,'→',M+268,y+13,15,GOLD,BOLD)
        para(c,dst,M+310,y+15,180,10.5,16,TEAL,BOLD)
        y+=60
    text(c,'小项名称：2020 起不再强行“还原”',M,516,18,NAVY,BOLD)
    para(c,'例如“男子”“女子”“团体”等标签必须结合运动项目和上下文解释。已将 8,515 条记录标为“泛化或需上下文”；其余较具体名称仅标为“尚未逐项核验”。',M,550,CW,11,18,INK)
    box(c,M,626,CW,112,HexColor('#E7F0EB'))
    text(c,'处理策略',M+18,643,11,TEAL,BOLD)
    para(c,'2020 年后的小项演化退回到运动大类×性别层级。逐小项获奖者使用单独接入的 2024 官方结果表；主分析不猜测丢失的赛制和项目名称。',M+18,668,CW-36,11,18,INK)
    c.showPage()

def special(c):
    page(c,6,'特殊记录 / 历史不被抹平','边界规则写在数据里','历史变化不是清洗错误。每个例外都保留原始值，并提供明确的分析规则。')
    rows=[
        ('1906 届间奥运会','原始记录保留；主分析排除；另提供纳入版本检验敏感性。'),
        ('1956 双城','墨尔本与斯德哥尔摩保留城市差异，按同一届次年份汇总。'),
        ('政体变迁','苏联、独联体、俄罗斯及德国不同历史政体分别统计，不默认接续。'),
        ('特殊身份','俄罗斯奥委会、个人中立运动员和难民代表队独立保留。'),
        ('东京 2020','使用官方届次年份 2020；举办时间与届次标识分开解释。'),
        ('缺席与零奖牌','没有参赛记录，与参赛但零奖牌，严格区分。'),
    ]
    top=207
    for i,(title,desc) in enumerate(rows):
        box(c,M,top,CW,82,WHITE,LINE)
        box(c,M+14,top+16,6,49,TEAL if i%2==0 else GOLD,r=3)
        text(c,title,M+34,top+16,14,NAVY,BOLD)
        para(c,desc,M+34,top+43,CW-53,10,16,MUTED)
        top+=91
    c.showPage()

def quality(c,items,n):
    page(c,n,'可复现检查 / 审计证据',f'12 项质量检查 · {"上" if n==7 else "下"}半场','每项都保留检查代码位置、实测结果和处理决定。')
    top=199
    for row in items:
        title=row['检查内容'].replace('Sport','运动').replace('Event','小项').replace('ID','标识符')
        result=row['实测结果'].replace('Melbourne','墨尔本').replace('Stockholm','斯德哥尔摩').replace('Sport','运动')
        action=row['处理决定'].replace('player_id','运动员标识符').replace('Event','小项')
        box(c,M,top,CW,91,WHITE,LINE)
        text(c,row['编号'],M+14,top+13,10,TEAL,BOLD)
        text(c,title,M+66,top+10,13,NAVY,BOLD)
        c.setFillColor(MUTED);c.setFont(FONT,8)
        c.drawRightString(W-M-14,H-top-23,row['代码位置'])
        para(c,'实测：'+result,M+66,top+35,CW-83,9.5,15,MUTED)
        para(c,'决定：'+action,M+66,top+58,CW-83,9.5,15,INK)
        top+=98
    c.showPage()

def impact_matrix(c):
    page(c,9,'口径敏感性 / 图表对照','换一条规则，图表会怎样变？',
         '每行只比较所列规则；没有可比小项数的届次明确留空。')
    folder = TASK / '04_质量检查结果'
    main = {int(row['Year']): row for row in get_rows(folder/'edition_main.csv')}
    inclusive = {int(row['Year']): row for row in get_rows(folder/'edition_include_1906.csv')}
    dedup = {int(row['Year']): row for row in get_rows(folder/'edition_exclude_duplicate_excess.csv')}
    spain = next(row for row in get_rows(folder/'2024双口径敏感性.csv') if row['NOC']=='ESP')
    historical = inclusive[1906]
    rows = [
        ('奖牌计数单位', '任务一 · 双口径金牌排名对照',
         f"两榜均只按金牌计数排名，并列取最小名次。西班牙从小项金牌第 {spain['gold_only_rank']} 到运动员金牌记录第 {spain['gold_row_rank']}。",
         '2024双口径敏感性.csv'),
        ('是否纳入 1906', '任务二 A1 · 参赛与获奖规模',
         f"纳入后，时间轴多一届，增加 {historical['medal_rows']} 条获奖行；1896 与 2024 两端数值仍为 {main[1896]['medal_rows']} 和 {main[2024]['medal_rows']}。",
         'edition_main.csv / edition_include_1906.csv'),
        ('是否扣除重复候选余量', '任务二 A1 · 逐届获奖记录',
         f"1900 年 {main[1900]['medal_rows']} → {dedup[1900]['medal_rows']} 条；2024 年 {main[2024]['medal_rows']} → {dedup[2024]['medal_rows']} 条。两届间增长方向保留。",
         'edition_main.csv / edition_exclude_duplicate_excess.csv'),
        ('是否能还原原始小项', '任务二 D1 · 逐届小项数量',
         '东京 2020 因 Event 泛化留空；巴黎 2024 使用 329 个官方小项。运动大类分析仍可进行。',
         'event_quality_by_year.csv / 2024官方329小项奖牌表.csv'),
    ]
    for i, (rule_name, chart, result, source) in enumerate(rows):
        top = 180 + i*136
        box(c,M,top,CW,124,WHITE,LINE)
        text(c,rule_name,M+16,top+10,13,NAVY,BOLD)
        text(c,chart,M+16,top+34,10,TEAL,BOLD)
        para(c,result,M+16,top+55,CW-32,10.5,16,INK)
        para(c,'复核：'+source,M+16,top+94,CW-32,8.6,12,MUTED)
    para(c,'离线复查：打开任务一首页的「数据规则实验台」，可切换方案和届次，并追查原始记录行。',M,739,CW,9,14,MUTED)
    c.showPage()


def reproduce(c):
    page(c,10,'复现路径 / 从原始行到结论','交付能独立重跑','评委可从原始 CSV 一键生成质量检查、归一数据和后续分析基础。')
    stages=[('01','输入','赛题原始 CSV；保留文件校验值'),('02','审计','规模、缺失、重复、身份和历史边界'),('03','归一','运动大类、小项状态、主分析标记'),('04','对照','双口径、1906 与重复候选敏感性'),('05','输出','说明书、数据表、代码与检查日志')]
    top=206
    for num,title,desc in stages:
        box(c,M,top,CW,64,WHITE,LINE)
        box(c,M+12,top+13,37,37,NAVY,r=8);text(c,num,M+19,top+21,11,WHITE,BOLD)
        text(c,title,M+64,top+13,13,NAVY,BOLD)
        para(c,desc,M+145,top+14,CW-165,10,16,MUTED)
        top+=72
    box(c,M,594,CW,138,HexColor('#E4EFEB'))
    text(c,'复现入口',M+19,609,12,TEAL,BOLD)
    para(c,'双击「一键运行任务一.cmd」。脚本自动定位原始 CSV，并运行规模、映射完整性和主分析奖牌行断言；失败时停止。更细的字段字典、12 项检查代码与结果均在同目录交付。',M+19,636,CW-38,11,18,INK)
    para(c,'来源：赛题 Summer Olympics Medals (1896—2024) 数据；2024 官方小项结果另接一手来源。原始 CSV 不随提交包分发，文件校验值保存在审计结果中。',M,750,CW,8.4,13,MUTED)
    c.showPage()

def main():
    OUT.parent.mkdir(parents=True,exist_ok=True)
    c=canvas.Canvas(str(OUT),pagesize=A4,pageCompression=1)
    labels = ['封面', 'Q1–Q6 抽查索引', '质量风险总览', '统计口径', '字段归一', '特殊记录', '质量检查（一）', '质量检查（二）', '口径规则与图表影响', '复现路径']
    c.setAuthor("晓组织 · 燕山大学")
    c.setSubject("数据质量审计与统计口径")
    show_page = c.showPage
    def bookmarked_page():
        number = c.getPageNumber()
        key = f"audit-{number}"
        c.bookmarkPage(key)
        c.addOutlineEntry(labels[number-1], key)
        show_page()
    c.showPage = bookmarked_page
    c.setTitle('任务一｜奥运数据质量与口径说明书')
    cover(c);quick_index(c);risks(c);medal(c);normalization(c);special(c)
    checks=get_rows(TASK/'01_报告与说明'/'03_质量检查登记表.csv')
    assert len(checks)==12
    quality(c,checks[:6],7);quality(c,checks[6:],8);impact_matrix(c);reproduce(c)
    c.save();print(OUT)

if __name__=='__main__':main()
