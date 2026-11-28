import csv
from pathlib import Path
from PIL import Image, ImageChops
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
PAPER_RGB = (251, 250, 246)
P={'paper':HexColor('#FBFAF6'),'ink':HexColor('#172A30'),'teal':HexColor('#247487'),'red':HexColor('#A64155'),'gold':HexColor('#C4903D'),'grey':HexColor('#68777D'),'line':HexColor('#D9DEDC')}

def bg(c,w,h): c.setFillColor(P['paper']); c.rect(0,0,w,h,fill=1,stroke=0)
CHAPTER_COLORS = {
    'A': HexColor('#247487'),
    'B': HexColor('#966825'),
    'C': HexColor('#A64155'),
    'D': HexColor('#477765'),
}

def header(c,w,h,kicker,title,page=None):
    chapter = kicker.split()[0]
    accent = CHAPTER_COLORS.get(chapter, P['teal'])
    c.setFillColor(accent)
    c.rect(40,h-40,17,2,fill=1,stroke=0)
    c.setFont('CNB',10)
    c.drawString(65,h-42,kicker)
    title_size=24
    while stringWidth(title,'CNB',title_size)>w-80 and title_size>15: title_size-=1
    c.setFillColor(P['ink']); c.setFont('CNB',title_size); c.drawString(40,h-77,title)
    c.setStrokeColor(P['line']); c.line(40,h-95,w-40,h-95)
    if page is not None:
        c.setFont('CN',8); c.setFillColor(P['grey'])
        c.drawString(40,24,'任务二  /  百年奥运全景')
        c.drawRightString(w-40,24,f'{page:02d}  /  13')


def wrap(c,text,x,y,maxw,size=10,leading=16,color=None,font='CN', *, indent=False):
    c.setFont(font,size); c.setFillColor(color or P['ink']); line=''; lines=[]
    first_indent = 2*size if indent else 0
    for ch in text:
        test=line+ch
        if stringWidth(test,font,size)>maxw-(first_indent if not lines else 0) and line: lines.append(line); line=ch
        else: line=test
    if line: lines.append(line)
    for index, ln in enumerate(lines):
        c.drawString(x+(first_indent if index == 0 else 0),y,ln)
        y-=leading
    return y

def image_fit(c,source,x,y,w,h, *, align_top=False):
    im=ImageReader(str(source) if isinstance(source, Path) else source); iw,ih=im.getSize(); scale=min(w/iw,h/ih); nw,nh=iw*scale,ih*scale
    bottom = y + (h - nh) * (1 if align_top else .5)
    c.drawImage(im, x+(w-nw)/2, bottom, nw, nh, mask='auto')
    return bottom

def footer_note(c,w,text):
    c.setStrokeColor(P['line']); c.line(40,47,w-40,47); wrap(c,text,40,36,w-80,7.5,10,P['grey'])

FIGURE_SCOPE = {
    '00_封面总览英雄图.png': '1896—2024，排除 1906。参赛与获奖按运动员记录行；前五份额以当届全部获奖行为分母；2024 小项据官方补充表。',
    'A_规模扩张与奖牌集中度.png': '1896—2024，排除 1906。参赛与获奖为运动员记录行；前五份额以当届全部获奖行为分母。',
    'A_历史累计奖牌记录榜.png': '1896—2024，排除 1906。按历史代表团累计获奖运动员记录行。',
    'B_十二代表团兴衰曲线.png': '1896—2024，排除 1906。份额为代表团获奖运动员行除以当届全部获奖运动员行。',
    'B_强国时代热力图.png': '1896—2024，排除 1906。色阶为代表团占当届获奖运动员记录的份额。',
    'B_主场效应准实验检验.png': '主办届 1964—2024，共 9 案例，排除 1906。匹配差异按获奖运动员行份额计算，单位为百分点。',
    'B_20届合成对照与稳健性.png': '候选主办届 1948—2024，排除 1906。按获奖运动员行份额对照，差值单位为百分点。',
    'C_女性三层平权曲线.png': '1896—2024，排除 1906。参赛与获奖按运动员行；小项按历史 Event 代理，2020 留空，2024 用官方结构表。',
    'C_2024代表团女性结构差.png': '仅巴黎 2024，1906 不在图示范围。参赛与获奖按运动员行，份额差以百分点计。',
    'D_项目新增退出重返流向.png': '1896—2024，排除 1906。按有参赛记录的归一运动大类计数，并与相邻已收录届次比较。',
    'D_小项增长与项目更替.png': '排除 1906。1896—2016 按 Event 去重估计小项，2020 留空，2024 用官方 329 项；矩阵按归一运动大类。',
}


def figure_on_report_paper(path):
    with Image.open(path) as source:
        image = source.convert('RGB')
    original_paper = image.getpixel((0, 0))
    difference = ImageChops.difference(image, Image.new('RGB', image.size, original_paper))
    bounds = difference.getbbox()
    if bounds:
        left, top, right, bottom = bounds
        margin = round(image.width * .012)
        image = image.crop((max(0,left-margin), max(0,top-margin),
                            min(image.width,right+margin), min(image.height,bottom+margin)))
        difference = difference.crop((max(0,left-margin), max(0,top-margin),
                                      min(difference.width,right+margin), min(difference.height,bottom+margin)))
    if original_paper != PAPER_RGB:
        red, green, blue = difference.split()
        delta = ImageChops.lighter(ImageChops.lighter(red, green), blue)
        # Blend only paper and its antialiased edge pixels. Keep data marks and text colors.
        paper_mask = delta.point(lambda value: max(0, 255-32*value))
        image.paste(PAPER_RGB, (0, 0, image.width, image.height), paper_mask)
    return image


def report_figure(c, name, x, y, width, height, *, align_top=False):
    image = figure_on_report_paper(FIG/name)
    bottom = image_fit(c, image, x, y, width, height, align_top=align_top)
    return wrap(c, '图注｜' + FIGURE_SCOPE[name], x, bottom-12, width, 8.6, 12, P['grey'])


def team_share_case(c, width, y):
    years = ('2016', '2020')
    tables = TASK/'02_数据表'
    with (tables/'B_十二代表团逐届份额.csv').open(encoding='utf-8-sig', newline='') as file:
        team = {r['Year']: int(float(r['medal_records'])) for r in csv.DictReader(file) if r['NOC'] == 'USA' and r['Year'] in years}
    with (tables/'A_逐届规模与集中度.csv').open(encoding='utf-8-sig', newline='') as file:
        total = {r['Year']: int(r['medal_records']) for r in csv.DictReader(file)}
    counts = [team[year] for year in years]
    denominators = [total[year] for year in years]
    shares = [100*n/d for n,d in zip(counts, denominators)]
    c.setStrokeColor(P['line'])
    c.line(40,y+14,width-40,y+14)
    wrap(c, '局部对照｜里约 2016 → 东京 2020', 56, y, width-112, 10, 14, P['teal'], 'CNB')
    column = (width-136)/2
    headings = ('美国获奖运动员记录（条）', '美国占当届获奖记录的份额')
    for i, (heading, values, color) in enumerate(zip(headings, (counts, shares), ('teal', 'gold'))):
        x = 56+i*(column+24)
        wrap(c, heading, x, y-17, column, 8.8, 12, P['grey'])
        left, right = x+32, x+column-32
        low, high = y-51, y-40
        first, last = (low, high) if values[1] > values[0] else (high, low)
        c.setStrokeColor(P[color])
        c.setFillColor(P[color])
        c.setLineWidth(1.15)
        c.line(left, first, right, last)
        c.circle(left, first, 2, stroke=0, fill=1)
        c.circle(right, last, 2, stroke=0, fill=1)
        c.setFont('CNB', 10)
        for px, py, value in ((left, first, values[0]), (right, last, values[1])):
            c.drawCentredString(px, py+5, f'{value:.2f}%' if i else str(value))
        c.setFont('CN', 8)
        c.setFillColor(P['grey'])
        for px, year in ((left, years[0]), (right, years[1])):
            c.drawCentredString(px, y-65, year)
    c.setLineWidth(1)
    wrap(c, '图注｜仅 2016 与 2020 两届，排除 1906；以获奖运动员记录行为单位，东京按届次记为 2020。',
         56, y-82, width-112, 8.6, 12, P['grey'])
    team_growth = 100*(counts[1]/counts[0]-1)
    total_growth = 100*(denominators[1]/denominators[0]-1)
    return (
        f'美国的获奖运动员记录从 {counts[0]} 条增至 {counts[1]} 条，多了 {counts[1]-counts[0]} 条，增幅为 {team_growth:.1f}%。'
        f'同期全场记录从 {denominators[0]:,} 条增至 {denominators[1]:,} 条，增幅为 {total_growth:.1f}%。'
        f'美国的份额以当届全场为分母，分母增长更快，所以份额从 {shares[0]:.2f}% 降至 {shares[1]:.2f}%，'
        f'下降 {shares[0]-shares[1]:.2f} 个百分点。',
        '记录数回答一队有多少获奖运动员记录，份额回答这些记录在当届占多大比重。'
        '团队项目的一枚小项奖牌可对应多条记录，因此本例说明美国在记录分布中的相对份额下降；'
        '判断官方奖牌数或长期竞争力，还需使用小项口径并查看更多届次。',
    )


def panorama_overview(c, w, top):
    tables = TASK/'02_数据表'
    with (tables/'A_逐届规模与集中度.csv').open(encoding='utf-8-sig', newline='') as file:
        editions = [row for row in csv.DictReader(file) if row['Year'] != '1906']
    with (tables/'C_女性参与获奖与小项.csv').open(encoding='utf-8-sig', newline='') as file:
        women = next(row for row in csv.DictReader(file) if row[''] == '2024')
    start, latest = editions[0], editions[-1]
    left, right = 78, w-48
    bottom, plot_top = top-249, top-43

    def point(row):
        year = int(row['Year'])
        x = left + (right-left)*(year-1896)/(2024-1896)
        y = bottom + (plot_top-bottom)*int(row['participation_records'])/16000
        return x,y

    wrap(c,'参赛规模与获奖分布',40,top,w-80,17,22,P['ink'],'CNB')
    wrap(c,'夏奥参赛记录（行）',40,top-20,w-80,9,12,P['grey'])
    c.setFont('CN',8)
    c.setLineWidth(.5)
    for amount in (0,4000,8000,12000,16000):
        y = bottom+(plot_top-bottom)*amount/16000
        c.setStrokeColor(P['line'])
        c.line(left,y,right,y)
        c.setFillColor(P['grey'])
        c.drawRightString(left-8,y-3,f'{amount:,}')
    points = [point(row) for row in editions]
    path = c.beginPath()
    path.moveTo(*points[0])
    for x,y in points[1:]:
        path.lineTo(x,y)
    c.setLineWidth(1.8)
    c.setStrokeColor(P['teal'])
    c.drawPath(path)
    c.setLineWidth(1)
    for label in (1896,1920,1948,1972,2000,2024):
        x = left+(right-left)*(label-1896)/128
        c.setFillColor(P['grey'])
        c.drawCentredString(x,bottom-15,str(label))
    for row, alignment in ((start,'left'),(latest,'right')):
        x,y = point(row)
        c.setFillColor(P['teal'])
        c.circle(x,y,2.5,stroke=0,fill=1)
        c.setFont('CNB',9)
        text = f"{int(row['participation_records']):,}"
        if alignment == 'left':
            c.drawString(x+5,y+7,text)
        else:
            c.drawRightString(x-5,y+7,text)
    metrics = (
        ('A','前五份额',f"{float(start['top5_share']):.1%} → {float(latest['top5_share']):.1%}"),
        ('B','参赛代表团',f"{start['delegations']} → {latest['delegations']}"),
        ('C','2024 女性参赛记录',f"{float(women['participation_share']):.1%}"),
        ('D','2024 官方小项',f"{int(float(women['event_units']))} 项"),
    )
    width = (w-80)/4
    for i,(chapter,label,value) in enumerate(metrics):
        x = 40+i*width
        color = CHAPTER_COLORS[chapter]
        c.setStrokeColor(color)
        c.line(x,bottom-37,x+width-15,bottom-37)
        wrap(c,value,x,bottom-60,width-12,16,21,color,'CNB')
        wrap(c,label,x,bottom-78,width-12,8.5,12,P['grey'])
    return wrap(c,'图注｜'+FIGURE_SCOPE['00_封面总览英雄图.png'],40,bottom-104,w-80,8.6,12,P['grey'])


def report_cover(c,w,h):
    bg(c,w,h)
    colors = ['#427D9D','#26383F','#AE5260','#B6883D','#548873']
    for i, color in enumerate(colors):
        c.setFillColor(HexColor(color))
        c.rect(40+i*(w-80)/5,h-36,(w-80)/5,2,fill=1,stroke=0)
    wrap(c,'任务二 · 1896—2024 夏季奥运',40,h-75,w-80,10,16,P['teal'],'CNB')
    wrap(c,'百年圣火',40,h-141,w-80,54,60,P['ink'],'CNB')
    wrap(c,'扩张、权力转移与结构性平权',40,h-181,w-80,17,22,P['teal'],'CNB')
    wrap(c,'参赛规模扩大之后，奖牌、参与机会和运动项目如何重新分布？',40,h-225,w-80,12,18,P['grey'])
    panorama_overview(c,w,h-269)
    c.setStrokeColor(P['line'])
    c.line(40,151,w-40,151)
    wrap(c,'奖牌格局     代表团兴衰     女性参与     项目演化',40,121,w-80,12,18,P['ink'],'CNB')
    wrap(c,'晓组织｜燕山大学｜张子涵 60%｜陈旭 40%',40,72,w-80,10,15,P['grey'])
    c.showPage()


def add_report_navigation(document):
    chapters = [
        ('摘要与研究设计',2), ('A 奖牌格局',3), ('B 代表团兴衰',5),
        ('C 女性参与',9), ('D 项目演化',11), ('结论',13),
    ]
    if len(document) != 13:
        raise ValueError('任务二报告章节页码与生成结构不符')
    document.set_toc([[1,'封面',1], *[[1,title,page] for title,page in chapters]])
    from pymupdf import LINK_GOTO, Rect
    for index, page in enumerate((3,5,9,11)):
        x = 40 + index*70
        document[0].insert_link({'kind': LINK_GOTO, 'from': Rect(x,702,x+70,728), 'page': page-1})


FIGURE_INTERPRETATION = {
    'A_规模扩张与奖牌集中度.png': (
        '读图时先看规模，再看分布。记录总数随着参赛规模和团体项目人数扩大而增加；前五份额则把每届的全场记录设为共同分母，回答获奖记录集中在哪些队手里。',
        '长期分散也有反向波动。2016 到 2024 年，获奖代表团由 86 增至 92，前五份额却由 39.3% 升至 41.8%，有效获奖代表团数从 21.1 降至 18.9。获奖覆盖与分布均匀度需要同时观察。早期少数代表团参赛的格局也不宜直接代表现代竞争水平。',
    ),
    'A_历史累计奖牌记录榜.png': (
        '横条长度表示 1896—2024 年累加的获奖运动员记录。美国累计 5,597 条。长期参赛的代表团有更多累积机会，同一支获奖团体也会按成员产生多条记录，因此这里反映的是所用数据中获奖记录的历史规模。',
        '若要判断某届的相对表现，应把分母限定在该届，并查看代表团所占份额。政体变迁同样影响累积结果，苏联、东德、西德和统一德国按各自代码保留，避免将不同时期的代表团直接合并后比较。',
    ),
    'B_强国时代热力图.png': (
        '沿一行横读，能看到同一代表团在哪些届次进入或离开较高份额区间；沿一列竖读，则能比较同届代表团的相对位置。灰格表示没有参赛记录，白格表示参赛但没有获奖记录，两者对应不同历史情形。',
        '苏联、东德、西德和统一德国分列，可以把身份变迁和份额变化区分开。1980 和 1984 年附近的颜色跳变适合联系抵制背景阅读；单看色阶无法衡量抵制对某队份额的独立影响。',
    ),
    'B_主场效应准实验检验.png': (
        '读图时，应比较主办队的变化与匹配队同期的变化。这个差值控制了两组共同经历的一部分届次变化，也保留了每个案例的差异。以巴西 2016 为例，主办届份额约从 3.04% 降到 2.47%，但匹配比较的差值仍约为 +0.13 个百分点。',
        '因此平均正值可以与个别主办队的原始份额下降同时存在。匹配条件只覆盖已观测的前届份额，备战投入、东道主资格和项目变化仍可能影响结果。',
    ),
    'B_20届合成对照与稳健性.png': (
        '合成对照用多支代表团的加权组合拟合主办前走势。先看主办前是否贴合，再看主办届两条走势之间的距离。拟合质量筛选将结论限定在具备可比前期走势的案例，减少把既有差距算成主场关联的风险。',
        '剔除双城和抵制届后，估计仍保持正向，说明这些特殊届次并未单独决定方向。不同样本的平均值有差异；区间反映所选案例中的估计波动，无法覆盖所有未观测的主办权选择因素。',
    ),
    'C_女性三层平权曲线.png': (
        '三条线的分母分别是全部参赛记录、全部获奖记录和全部小项。混合小项可以增加女性参赛和获奖记录，但仍归为混合小项；团队项目也会因一项获奖产生多条记录。比较三条线之前，应先确认衡量的是参与、获奖还是赛程。',
        '巴黎的女性获奖与参赛记录占比精确相差约 1.185 个百分点。按运动家族拆解，项目内结构贡献 +1.294，运动权重贡献 −0.109 个百分点。不同运动的正负贡献彼此抵消，总体比例无法直接代表某项运动的个体获奖机会。',
    ),
    'C_2024代表团女性结构差.png': (
        '比较同一队的两个比例时，先看女性在本队参赛记录里占多少，再看她们在本队获奖记录里占多少。正差表示女性在获奖记录中的份额较高，负差表示较低，差值方向能帮助定位值得下钻的代表团。',
        '差异可能来自各队参加的运动组合、团体项目人数和奖牌记录总量。图中样本为参赛记录最多的十五队，方便比较具备较多参赛记录的队伍；要解释某队的差值，应回看分运动构成和获奖记录。',
    ),
    'D_项目新增退出重返流向.png': (
        '净变化是新增和重返减去未再出现，更替量则把三者相加。按归一运动大类，1900 到 1904 年由 20 类降至 18 类，净减 2 类，实际有 4 类首次出现、2 类重返和 8 类未再出现，共 14 类更替。',
        '这说明总数相近的两届也可能拥有很不同的运动构成。未再出现仅指后一届没有赛题记录；正式赛程如何认定运动或小项，需要另查对应届次资料。',
    ),
    'D_小项增长与项目更替.png': (
        '上部数量曲线看扩容幅度，下部出现矩阵看具体运动在哪些届次留下记录。花样滑冰曾出现在 1908、1920 年夏奥，冰球也出现在 1920 年夏奥，说明早期项目分类与今天的夏冬奥分工存在差异。',
        '历史曲线使用清洗后的 Event 唯一值作为估计。2020 年原始标签泛化，因此小项曲线留空；2024 年用官方补充表单独确认 329 项。读者可以沿矩阵核对运动更替，并把两种小项来源的口径差异纳入判断。',
    ),
}


def make_report():
    w,h=portrait(A4); c=canvas.Canvas(str(REPORT),pagesize=(w,h),pageCompression=1)
    c.setTitle('任务二 百年奥运全景'); c.setAuthor('晓组织｜燕山大学')
    report_cover(c,w,h)
    # 2 abstract
    bg(c,w,h); header(c,w,h,'研究导览','摘要与研究设计',2)
    y=h-124
    y=wrap(c,'摘要',40,y,w-80,16,24,P['teal'],'CNB')
    y=wrap(c,'1896至2024年，夏季奥运会由少数国家参与的精英赛事发展为覆盖206个代表团、329个小项的全球制度。参赛记录扩大39.2倍，但前五代表团的同届奖牌记录份额由83.9%降至41.8%，显示规模扩张伴随去集中化。2024年女性参赛记录占49.1%、女性奖牌记录占50.3%，而女子专属小项占45.9%，说明人数平权尚未完全转化为项目机会平权。九个现代主办案例中八个主办届份额上升，但项目贡献分解显示增益路径因国而异，不能把主办身份直接解释为因果。',40,y-8,w-80,12,22,indent=True)
    y-=22; y=wrap(c,'统一口径',40,y,w-80,16,24,P['teal'],'CNB')
    bullets=['主分析使用运动员记录口径；团体项目每名获奖成员均形成记录。','排除1906；URS、GDR、FRG、GER等历史政体分别统计。','2020年Event字段泛化，不计算小项数；2024年采用官方329小项补充表。','无参赛记录留空，不自动视为零；描述性比较不冒充因果估计。']
    for b in bullets: y=wrap(c,'· '+b,48,y-7,w-96,11.5,21)
    y = wrap(c,'四个视角如何一起读',40,y-18,w-80,15,23,P['teal'],'CNB')
    overview = (
        ('A','奖牌格局','看全场参赛规模和获奖记录如何增长，再用同届前五份额衡量集中度。'),
        ('B','代表团兴衰','把同届份额拆到代表团，结合缺席与政体变化辨认断点，再查看主场对照。'),
        ('C','女性参与','分别比较女性参赛记录、获奖记录和女子专属小项，占比相近时追查运动构成。'),
        ('D','项目演化','比较小项总量的长期变化，再用运动大类的新增、重返和未再出现解释届间更替。'),
    )
    for code,title,description in overview:
        y = wrap(c,f'{code}  {title}',40,y-7,78,11,20,CHAPTER_COLORS[code],'CNB')+20
        y = wrap(c,description,133,y,w-173,11,20)
    c.showPage()
    pages=[
      ('A 规模与集中度','规模扩张没有带来同等程度的奖牌垄断','A_规模扩张与奖牌集中度.png','1896年只有380条参赛记录、12个代表团和143条运动员奖牌记录；到2024年分别达到14,892条、206个和2,281条。与此同时，前五代表团奖牌记录份额由83.9%下降到41.8%。绝对奖牌记录随项目与团体规模膨胀，但相对统治力长期下降。','运动员记录口径；前五份额用于同届比较，不等于官方小项奖牌份额。'),
      ('A 累计记录','累计获奖记录前十五','A_历史累计奖牌记录榜.png','累计获奖量同时受参赛历史与团体项目人数影响。美国居首，苏联与德国分别按历史代码记录。','统计单位为获奖运动员记录行。'),
      ('B 强国兴衰','历史不是连续曲线，而是战争、抵制与政体变迁留下的断点','B_十二代表团兴衰曲线.png','USA在1904年达到81%的异常高位，战后多数届次约为12%至16%；URS在1952年起出现连续参赛记录并进入高位；CHN自1984年形成连续轨迹，2008年约9.0%，2024年约7.4%。将历史政体强行拼接，会把制度断点误写成平滑增长。','同届奖牌记录份额；缺席留空；纵轴35%，超限值用三角标注。'),
      ('B 时代接力','同届获奖记录份额的代表团热力图','B_强国时代热力图.png','与趋势图使用相同的代表团顺序和年份范围。灰色表示无参赛记录，白色表示参赛但零获奖，金色框标记1980和1984抵制届次。','色阶上限35%，分母为同届全部获奖记录。'),
      ('B 准实验检验','匹配DID显示主办届存在稳定的相对提升','B_主场效应准实验检验.png','九个现代主办案例逐一匹配五个前届奖牌份额接近的非主办代表团。主办国前后变化减去匹配组同期变化后，平均DID为+2.70个百分点；案例自助法95%区间为[1.84, 3.59]。五万次组内随机指派未产生同等极端均值，前趋势平均差为0.24个百分点。证据比简单前后比较更强，但主办权并非随机，不能无条件外推为因果。','匹配变量为前届奖牌记录份额；九个案例、小样本、未控制体育投入与资格扩张。结论定位为准实验关联证据。'),
      ('B 扩展合成对照','扩展样本与严格敏感性检验仍支持正向关联','B_20届合成对照与稳健性.png','1948至2024年整理20个候选主办届，其中17届具备三个主办前届次的连续信息，14届达到严格的前拟合质量阈值。每届使用前三届奖牌份额与参赛份额拟合非负合成权重，并排除事件窗口内成为东道主的供体。高拟合样本的平均主办届差为+2.24个百分点，案例自助法95%区间为[1.30, 3.28]；剔除1956双城及1980、1984抵制届后仍为+2.52个百分点。','合成对照提高反事实可比性；后续路径使用完整平衡窗口。主办权仍非随机，不作自然实验或随机试验解释。'),
      ('C 女性平权','人数接近平权，不等于项目机会结构完全对称','C_女性三层平权曲线.png','2024年女性参赛记录占49.1%，女性奖牌记录占50.3%，但官方329个小项中女子专属小项为151个，占45.9%。混合小项、团体人数与项目设置使参赛、获奖和小项三种比例出现差异；三层指标共同展示进展，也保留结构性问题。','参与与获奖按主表Sex字段；2024小项性别属性来自官方补充表。'),
      ('C 代表团结构','同队女性参赛和获奖占比的差','C_2024代表团女性结构差.png','选择参赛记录最多的十五队，分别计算各队女性参赛占比与获奖占比。右侧标出差值绝对值最大的三队。','差值单位为百分点，基于记录行。'),
      ('D 项目演化','奥运项目表在扩容，也在持续退出与重返','D_项目新增退出重返流向.png','项目体系并非机械累加。早期更替频繁，随着制度成熟，连续保留成为主流；但近年仍可观察到新增、退出与重返。艺术比赛等历史项目消失，城市文化与青年项目进入。项目表是传统、全球普及度、性别平衡和青年吸引力之间的动态配置。','按归一体育大类识别首次出现、上届缺席后的重返及下届缺席。'),
      ('D 小项数量','从43到329：扩容主线中的口径控制','D_小项增长与项目更替.png','可比口径下，小项数从1896年的约43个增至1920年的158个、1984年的221个、2000年的300个，2024年达到官方329个。2020年留空是主动控制：原始Event已泛化，直接计数会制造虚假断崖。宁可披露不可比，也不把错误精确包装成趋势。','1896至2016按清洗后Event唯一值；2020不计；2024采用官方329项表。')]
    p=3
    for kicker,title,img,body,note in pages:
        bg(c,w,h); header(c,w,h,kicker,title,p)
        if img == 'B_十二代表团兴衰曲线.png':
            report_figure(c,img,40,295,w-80,468)
            result, interpretation = team_share_case(c,w,280)
            y = wrap(c,result,40,169,w-80,9.4,14,indent=True)
            y = wrap(c,interpretation,40,y-4,w-80,9.4,14,indent=True)
            end = wrap(c,body,40,y-4,w-80,9.2,14,indent=True)
            assert end >= 47, 'B 视角正文与页脚重叠'
        else:
            below_figure = report_figure(c,img,40,282,w-80,h-394,align_top=True)
            accent = CHAPTER_COLORS[kicker[0]]
            y = wrap(c,'图表解读',40,below_figure-14,w-80,13,23,accent,'CNB')
            y = wrap(c,body,40,y,w-80,11.5,19,indent=True)
            for heading, paragraph in zip(('如何读图','比较与边界'), FIGURE_INTERPRETATION[img]):
                y = wrap(c,heading,40,y-6,w-80,11,20,accent,'CNB')
                y = wrap(c,paragraph,40,y,w-80,11.5,19,indent=True)
            assert y >= 47, f'图表解读与页脚重叠：{img}'
        footer_note(c,w,note); c.showPage(); p+=1
    # final
    bg(c,w,h); header(c,w,h,'结论','结论：扩张中的去集中化',p)
    y = panorama_overview(c,w,h-121)
    y = wrap(c,'综合解读',40,y-12,w-80,12,20,P['teal'],'CNB')
    y=wrap(c,'奥运百年发展的核心，不只是“更多”，而是覆盖更广、权力更分散、平权更接近，同时仍保留结构差异。规模扩张带来绝对奖牌记录通胀，却没有制造同等程度的强国垄断；强国格局在历史断点中重组；女性人数平权接近实现，但项目机会仍未完全对称；项目表则通过持续增删回应时代。',40,y,w-80,12,22,indent=True)
    y=wrap(c,'这些结果可以互相核对。先用 A 的获奖覆盖与集中度区分规模和分布，再用 B 的美国案例核对绝对数与相对份额。'
           '在 C 中，核对三个分母和运动贡献的抵消；在 D 中，把净变化拆成新增、重返和未再出现。'
           '跨届推断仍受团队记录、历史政体、早期覆盖和小项标签可比性的约束。',40,y-10,w-80,12,22,indent=True)
    y=wrap(c,'交互版本：任务二_百年全景/05_交互总览/index.html（离线打开）',40,y-15,w-80,9.5,15,P['teal'],'CNB')
    footer_note(c,w,'数据与代码：任务一归一数据、2024官方329小项补充表、任务二复现脚本。全部结论均受所声明统计口径约束。')
    c.save()
    import pymupdf
    with pymupdf.open(REPORT) as document:
        add_report_navigation(document)
        document.saveIncr()


def make_poster():
    w,h = portrait(A2)
    c = canvas.Canvas(str(POSTER), pagesize=(w,h), pageCompression=1)
    c.setTitle('百年圣火｜百年奥运全景 A2 海报')
    c.setAuthor('晓组织｜燕山大学')
    bg(c,w,h)
    left, gutter = 55, 36
    column = (w-2*left-gutter)/2
    for i,color in enumerate(CHAPTER_COLORS.values()):
        c.setFillColor(color)
        c.rect(left+i*(w-2*left)/4,h-45,(w-2*left)/4,3,fill=1,stroke=0)
    wrap(c,'任务二 · 百年奥运全景',left,h-87,column,19,25,P['teal'],'CNB')
    c.setFont('CN',16)
    c.setFillColor(P['grey'])
    c.drawRightString(w-left,h-87,'1896—2024  /  夏季奥运会')
    wrap(c,'百年圣火',left,h-177,w-2*left,81,88,P['ink'],'CNB')
    wrap(c,'规模扩张之后，荣誉与机会如何分布？',left,h-228,w-2*left,29,38,P['teal'])
    cards = (
        ('A','奖牌格局','前五份额 83.9% → 41.8%','A_规模扩张与奖牌集中度.png',
         '奖牌记录总量大增，前五份额长期下降。2016 至 2024 年，获奖队伍变多，前五份额却由 39.3% 回升至 41.8%。'),
        ('B','代表团兴衰','美国 264 → 298 条','B_强国时代热力图.png',
         '里约至东京，美国同届份额从 13.05% 降至 12.17%。全场记录增长更快，拉低了美国份额。'),
        ('C','女性参与','巴黎 2024：49.1%','C_女性三层平权曲线.png',
         '女性参赛记录占 49.1%，获奖记录占 50.3%，女子专属小项占 45.9%。三个分母对应参与、获奖和赛程。'),
        ('D','项目演化','净减 2 类，更替 14 类','D_项目新增退出重返流向.png',
         '1900 到 1904 年，归一运动大类从 20 降至 18。4 类首次出现、2 类重返、8 类在后一届没有记录。'),
    )
    for i,(code,title,number,name,description) in enumerate(cards):
        x = left+(i%2)*(column+gutter)
        y = h-292-(i//2)*605
        color = CHAPTER_COLORS[code]
        c.setStrokeColor(color)
        c.setLineWidth(1.7)
        c.line(x,y,x+column,y)
        wrap(c,f'{code}  {title}',x,y-32,column,17,23,color,'CNB')
        wrap(c,number,x,y-81,column,31,38,P['ink'],'CNB')
        y = report_figure(c,name,x,y-465,column,355,align_top=True)
        y = wrap(c,description,x,y-15,column,16,24)
        assert y >= (h-292-605-570 if i >= 2 else h-292-570)
    c.setStrokeColor(P['line'])
    c.line(left,118,w-left,118)
    wrap(c,'数据来源｜任务一归一数据、任务二逐届复核表及巴黎 2024 官方小项补充表',left,87,w-2*left,13,18,P['grey'])
    wrap(c,'晓组织 · 燕山大学｜张子涵 60% · 陈旭 40%',left,56,w-2*left,15,21,P['ink'],'CNB')
    c.save()

if __name__ == "__main__":
    make_report()
    make_poster()
    print(REPORT)
    print(POSTER)
