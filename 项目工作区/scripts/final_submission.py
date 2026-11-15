"""Build the judge-facing report and readable A2 poster from submitted artifacts."""
from pathlib import Path
from shutil import copy2
import csv
import json
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, A2
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from PIL import Image
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from task2_localization import NOC_ZH

ROOT = Path(__file__).resolve().parents[2]
DEL = ROOT / "交付文件"
FINAL = DEL / "最终提交材料"
FONT = r"C:\Windows\Fonts\simhei.ttf"
pdfmetrics.registerFont(TTFont("SimHei", FONT))
INK = HexColor("#162b3a")
TEAL = HexColor("#176979")
RED = HexColor("#ad3658")
MUTED = HexColor("#526574")
PAPER = HexColor("#faf9f6")
RULE = HexColor("#dbe4e8")
W, H = A4
body = ParagraphStyle("body", fontName="SimHei", fontSize=10.4, leading=17.3,
                      textColor=INK, wordWrap="CJK")
small = ParagraphStyle("small", parent=body, fontSize=9.1, leading=14.3)


def txt(c, text, x, y, size=10, color=INK):
    c.setFont("SimHei", size)
    c.setFillColor(color)
    c.drawString(x, y, text)


def para(c, text, x, top, width, style=body):
    p = Paragraph(text, style)
    _, height = p.wrap(width, 1000)
    p.drawOn(c, x, top-height)
    return top-height


def image_fit(c, path, x, y, width, height):
    im = Image.open(path)
    iw, ih = im.size
    scale = min(width/iw, height/ih)
    dw, dh = iw*scale, ih*scale
    c.drawImage(ImageReader(im), x+(width-dw)/2, y+(height-dh)/2,
                width=dw, height=dh, preserveAspectRatio=True, mask="auto")


def chrome(c, number, section, title):
    c.setFillColor(PAPER)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setStrokeColor(RULE)
    c.line(45, 789, W-45, 789)
    txt(c, "百年圣火  /  晓组织 · 燕山大学", 45, 800, 9, MUTED)
    txt(c, section, 45, 760, 10, RED)
    txt(c, title, 45, 725, 21, INK)
    c.line(45, 52, W-45, 52)
    txt(c, "1896—2024 夏季奥运数据观察  |  运动员记录与官方小项严格区分", 45, 35, 8, MUTED)
    txt(c, str(number).zfill(2), W-63, 35, 9, MUTED)


def report_page(c, num, section, title, paragraphs, chart=None, note=""):
    chrome(c, num, section, title)
    top = 695
    for text in paragraphs:
        top = para(c, text, 48, top, W-96) - 11
    if chart:
        upper = min(top-6, 530)
        lower = 98 if note else 80
        image_fit(c, chart, 52, lower, W-104, max(30, upper-lower))
    if note:
        para(c, note, 52, 91, W-104, small)
    c.showPage()


def argument_page(c, num, section, title, steps, chart, note):
    """A readable claim / counterexample / revised claim page for key findings."""
    chrome(c, num, section, title)
    labels=("原判断", "反例", "修正结论")
    colors=(MUTED, RED, TEAL)
    tops=(684, 602, 520)
    for label, color, top, content in zip(labels, colors, tops, steps):
        c.setFillColor(color)
        c.roundRect(48, top-56, 75, 53, 8, fill=1, stroke=0)
        txt(c, label, 58, top-35, 10, HexColor("#ffffff"))
        c.setStrokeColor(RULE)
        c.line(135, top-59, W-48, top-59)
        end=para(c, content, 143, top-4, W-195, body)
        if end < top-58: raise ValueError(f"Argument text overflow: {title} / {label}")
    c.setFillColor(HexColor("#efeee9"))
    c.roundRect(48, 112, W-96, 318, 11, fill=1, stroke=0)
    image_fit(c, chart, 58, 121, W-116, 300)
    para(c, note, 52, 94, W-104, small)
    c.showPage()


T2 = DEL / "任务二_百年全景/04_核心图表"
S2 = DEL / "任务三_专题深挖/S2_口径的魔力/04_核心图表"
S3 = DEL / "任务三_专题深挖/S3_冠军的保质期/04_核心图表"
T4 = DEL / "任务四_开放创作/02_2028洛杉矶预测/核心图表"
TMAP = DEL / "任务三_专题深挖/11_结论稳定性地图"
EXTRA = FINAL / "答卷附图"
EXTRA.mkdir(parents=True,exist_ok=True)
pred=pd.read_csv(DEL/"任务四_开放创作/02_2028洛杉矶预测/LA2028机器学习集成预测榜.csv").nsmallest(15,'ensemble_rank').iloc[::-1]
plt.rcParams['font.sans-serif']=['Microsoft YaHei','SimHei','DejaVu Sans']
plt.rcParams['axes.unicode_minus']=False
fig,ax=plt.subplots(figsize=(10,6),facecolor='#f5f1e9');ax.set_facecolor('#f5f1e9')
ax.barh([NOC_ZH.get(x,x) for x in pred.NOC],pred.ensemble_total,color='#1b7587')
for i,r in enumerate(pred.itertuples()):ax.plot([r.lower80,r.upper80],[i,i],color='#b44857',lw=1.5)
ax.set_xlabel('预测小项奖牌（枚）');ax.set_title('洛杉矶2028：点估计与80%情景区间',loc='left',fontweight='bold',color='#173447')
ax.spines[['top','right']].set_visible(False);ax.grid(axis='x',color='#ded8cd');ax.set_axisbelow(True)
fig.tight_layout();fig.savefig(EXTRA/'2028预测榜_中文.png',dpi=180,facecolor=fig.get_facecolor());plt.close(fig)
metrics = json.loads((DEL/"任务二_百年全景/02_数据表/任务二关键指标.json").read_text(encoding="utf-8"))
assert metrics["events_2024"] == 329 and metrics["women_events_2024"] == 151
assert round(metrics["female_participation_2024"]*100, 1) == 49.1
assert round(metrics["female_medal_2024"]*100, 1) == 50.3
rank_file = DEL/"任务三_专题深挖/S2_口径的魔力/02_数据表/S2_2024三口径完整排名.csv"
with rank_file.open(encoding="utf-8-sig", newline="") as handle:
    ranks = {(r["NOC"],r["lens"]):float(r["Gold"]) for r in csv.DictReader(handle)}
for noc,rows,units in [("USA",131,40),("CHN",71,40),("NED",67,15),("ESP",40,5)]:
    assert ranks[(noc,"rows")] == rows and ranks[(noc,"official")] == units
report = FINAL / "报告/百年圣火_正式报告.pdf"
report.parent.mkdir(parents=True, exist_ok=True)
c = canvas.Canvas(str(report), pagesize=A4, pageCompression=1)
c.setTitle("百年圣火：谁被看见？｜正式报告")

chrome(c, 1, "摘要  /  作品导读", "谁被看见，取决于我们在数什么")
top = 681
for p in [
    "同一届奥运、同一套金银铜排序规则，只因统计单位不同，西班牙的2024年金牌榜名次就从官方小项口径第15位变成运动员行口径第5位。美国与中国同获40个金牌小项，却分别对应131行与71行运动员金牌记录。排名重排是口径效应，不能直接解释为实力变化。",
    "我们审计252,565条夏奥记录，以2024年329个小项结果核对口径，并用逐运动剔除与跨届代理检验稳健性。百年全景呈现规模扩张与份额变化；冠军王朝追踪控制权寿命；2028预测附赛前假设、历史回测和不确定性区间。历史小项代理不称现行IOC授牌，主分析排除1906并保留代表团身份边界。",
]:
    top = para(c, p, 49, top, W-98) - 16
image_fit(c, T2/"00_封面总览英雄图.png", 52, 105, W-104, min(410, top-117))
txt(c, "张子涵 60%  ·  陈旭 40%   |   2026年11月", 49, 77, 9, MUTED)
c.showPage()

pages = [
 ("01  数据体检", "先给每个数字一个单位", [
  "原始数据为252,565行、11列。一行表示一名运动员在一届的一个小项中的一条记录；团体成员分别占行。主分析排除IOC现行口径不承认的1906届，得到250,832条参赛记录、38,360条奖牌记录。历史NOC分立，1956年墨尔本与斯德哥尔摩按同届汇总，东京仍记为2020届。",
  "76种Sport原值均映射为运动家族；89条逗号拼接记录按Event和规则处理。2020年起Event泛化，不能从Men、Women等值反推出具体小项。姓名和player_id不可靠，作品不把记录数或ID数称为独立运动员人数。12项质量检查的代码、结果与处理决定见任务一。",
 ], None, "口径来源：任务一《数据质量与口径说明书》；原始CSV不随包提交。"),
 ("01  数据体检", "小项与记录行不能混为一谈", [
  "2024年的外部逐项结果层包含329个小项与329个金牌单元；326项有上游结果链接，3项按同站路径规则补充并明确标记。IOC官方回顾核验了329项的赛事总数。它是补充结果层，不修复原CSV中已丢失的小项名称。",
  "原CSV的运动员奖牌记录为2,281行。官方小项口径回答“赢了多少比赛单元”，运动员行口径回答“有多少获奖成员记录”。任一图表的图注都应说明使用哪种口径。",
 ], S2/"S2_金牌数量与获奖者规模.png", "2024小项结果层的来源及3项构造链接见任务一核验说明。"),
 ("02  百年全景 A", "规模扩张与奖牌通胀", [
  "1896至2024年，参赛记录从380增至14,892，代表团从12增至206；奖牌记录从143增至2,281。绝对数量增长同时受比赛项目、团队规模与参与覆盖影响，不能直接等同于竞技优势增长。",
  "按运动员奖牌记录统计，前五代表团的同届份额从1896年的83.9%降至2024年的41.8%。压力测试显示早期与现代届次中位数也下降，换成2016年前历史奖牌组代理仍同向；但2016至2024年前五份额从39.3%回升到41.8%，不能写成逐届持续下降。完整复算见任务二“结论压力测试”。",
 ], T2/"A_规模扩张与奖牌集中度.png", "图中参赛、奖牌均按运动员行；主分析排除1906。"),
 ("02  百年全景 B", "国家兴衰要保留历史断点", [
  "美国、苏联、两德、中国、日本等代表团的轨迹反映制度、参赛资格、抵制和项目组合的共同变化。作品保留URS、FRG、GDR、GER等NOC原边界；某届缺席留空，不用零奖牌连接成连续曲线。",
  "用同届奖牌记录份额比较可减轻赛事规模膨胀，但仍受团体项目人数影响。历史累计榜只用于规模描述，不能直接当作官方历史奖牌榜。",
 ], T2/"B_十二代表团兴衰曲线.png", "口径：同届运动员奖牌记录份额；历史政体分列。"),
 ("02  百年全景 C", "人数接近，不等于机会完全对称", [
  "2024年女性参赛记录占49.1%，女性奖牌记录占50.3%；官方329个小项中女子专属小项为151个，占45.9%。三层指标的分母不同，混合项目、团体人数和项目结构使它们不能互相替代。",
  "2024年女性获奖行占比比参赛行高1.185个百分点；按运动家族对称分解，内部构成贡献+1.294、项目权重贡献-0.109个百分点。正负项目抵消，整体50.3%不代表每项运动均衡，也不是个人获奖概率。2020年Event泛化，不能以其唯一值充当女子小项数；完整分解见任务二补充研究。",
 ], T2/"C_女性三层平权曲线.png", "女性参赛和奖牌指标按记录行；2024小项指标按外部逐项结果层。"),
 ("02  百年全景 D", "项目表在进入、退出与重返", [
  "从早期拔河、马球、艺术竞赛，到跆拳道、滑板、冲浪和霹雳舞，奥运项目表持续更替。历史花样滑冰和冰球出现在夏季奥运记录中，提醒我们不能用今天的冬夏边界回填过去。",
  "1896—2016的小项数量主要由赛题Event字段估计；2020因泛化留空；2024使用外部329项结果。图中的项目进入、退出、重返按归一运动家族描述，不能与官方小项数量简单相加。",
 ], T2/"D_小项增长与项目更替.png", "图中2020小项数量留空是主动的可比性处理。"),
 ("03  主专题 S2", "同一规则下，排名仍然改变", [
  "在同为“按金、银、铜依次排序”的规则下，2024年西班牙由官方小项口径第15位升至运动员行口径第5位，荷兰由官方第6位升至行口径第3位，日本则由官方第3位降至行口径第9位。美国与中国官方小项金牌各40枚，但运动员金牌记录分别为131行与71行。",
  "这是统计单位改变排名的反直觉案例。若把前者直接写成官方奖牌，就会把团体成员重复算作多枚奖牌。作品另设团队内均分口径，用三条路径展示指标选择如何影响榜单。",
 ], S2/"S2_三口径排名路径.png", "三口径定义及完整榜见任务三S2报告和数据表。"),
 ("03  主专题 S2", "机制不是偶然：跨届检验", [
  "荷兰2024年的67行金牌记录中，曲棍球35行、赛艇11行，两项共占68.7%。团队项目成员规模解释了金牌行相对小项的膨胀，但记录完整性与并列奖牌同样需要留意。",
  "2008、2012、2016三个届次的同口径代理检验中，平均绝对名次变化约为3.7、3.7、3.9位，提示重排机制在这些历史代理中重复出现。其中555项已与Olympedia独立对照，548项三色一致、7项有差异；仍不能称现行IOC逐项授牌，其证据等级低于2024外部逐项结果层。",
 ], S2/"S2_跨届机制稳定性.png", "检验只说明口径效应稳定，不说明哪一种排名更公平。"),
 ("03  创新专题", "冠军王朝的保质期", [
  "把1896—2016年的同一小项金牌归属改写为相邻届次的控制权转移，得到4,511次可比转移；相邻届同代表团卫冕率为29.5%。该指标衡量小项控制权延续，不等同于运动员个人卫冕。",
   "固定1960—2016每届连续且名称稳定的113个小项后，1964—1976与1996—2016的代表团卫冕率仍从34.5%降至27.1%，差7.37个百分点；按小项成组重抽样的95%区间为下降1.62至13.20个百分点。但17种运动中8种与总体方向相反；性别及疑似多人赛制分层仅提供机制线索，不能作因果解释。",
 ], S3/"S3_时代卫冕率.png", "自选专题作为附加叙事；正式按S7申报时需遵循赛题备案要求。"),
 ("03  辅专题 S1", "东道主增益有反例", [
  "九个现代主办案例中八个主办届奖牌记录份额上升，巴西2016却从前届3.04%降至2.47%。英国2012从3.96%升至6.49%，后届还升至7.17%。这些反例说明“主办必有短期高峰、随后回落”并不成立。",
  "任务二另给出匹配差分中的差分与合成对照等稳健性分析；主办权并非随机分配，投资、资格、项目设置和外部环境未完全控制，因此结果是有条件的经验估计，不能写成严格因果净效应。",
 ], T2/"B_主场效应与项目贡献.png", "主场图采用运动员奖牌记录份额；方法与诊断见任务二正式报告。"),
 ("04  开放创作", "洛杉矶2028：可检验的预测", [
  "透明基线按最近三届0.2、0.3、0.5加权，并加入15%的近期趋势；根据IOC公布的353个奖牌小项缩放。项目级集成模型将基线、随机森林/梯度提升和新增项目排名信号按45%/45%/10%组合。",
   "东道主与新增项目优势作为显式情景处理。消融检验显示关闭项目模型会使各代表团预测绝对变化合计约176枚，关闭主场调整约24.8枚，关闭新增运动排名信号约2.8枚；这些是固定奖牌池下的条件敏感度，不能相加或解释为因果贡献。已修正中性基线误含早期美国+12枚情景、导致主场重复计入的问题。",
 ], EXTRA/"2028预测榜_中文.png", "预测方法、权重、来源快照与完整榜见任务四交付目录。"),
 ("04  开放创作", "回测与不确定性边界", [
  "透明基线的代表团总奖牌历史回测MAE约2.74枚；实际获得至少5枚奖牌的代表团约4.57枚。80%区间由历史基线残差的10%与90%分位构造，不应称为集成模型的独立校准区间。",
  "代表团小项奖牌总量回放可迁移核心：2012年混合模型MAE为2.46枚，劣于基线2.02；2016年两者约2.15；2024年混合模型2.66，优于基线2.85，但前十重合从9降至8。逐队拆解显示2012年55队改善、65队变差。另用运动员获奖行同单位作项目检验，全体运动单元三届均不如简单基线；但只看有获奖的单元，2024模型反而改善。后者为事后分组，两套统计单位不能合并。",
  "逐队拆解发现2024年身份制度是主要风险线索：RUS、ROC与AIN不能按历史代码自动拼接。排除四个身份敏感代码后，混合模型对其余代表团的MAE为2.18枚，基线为2.30枚。西班牙18枚官方小项奖牌对应83条运动员获奖行，提示项目行预测转换时需警惕团队规模；这些只是误差线索，不能认定单一因果来源。",
  ], T4/"历史回测散点.png", "逐队误差图谱与可迁移核心滚动回放见任务四；榜单应与资格情景、区间来源和假设一起阅读。"),
 ("03  补充专题 S3—S4", "缺席与突破，都需要正确的分母", [
   "S3 地缘政治：1980、1984届在数据中分别出现80、140个代表团。IOC一手文献核对了两届抵制背景、1992联队及独立参赛身份、2024个人中立与难民身份；数据只记录出现或缺席，不能反推个别代表团的唯一政治动机。历史身份分列，不拼成无断点国家曲线。",
   "S4 小代表团：原七个突破故事是叙事选例，无一符合客观最小四分位门槛。把未获奖者放回分母，2000—2024年符合至少三届、典型参赛行不高于5的62个国家代表团中，53个未获奖、8个仅在一届获奖、1个在两届获奖。2024首次获奖者尚无下一届可观察，不能标为无法延续。获奖行数不是官方小项奖牌效率。",
 ], EXTRA/"S3_代表团覆盖变化.png", "S3图为逐届有记录的NOC数量；S4案例与交互详见任务三专题页。主分析排除1906。"),
 ("03  补充专题 S5—S6", "记录变多了，名字也可能不可靠", [
  "S5 奖牌通胀：1896年143条获奖运动员记录，2024年2,281条。小项增加、团队成员数及参赛覆盖共同扩张了记录机会；前五代表团份额却从83.9%降至41.8%。绝对量上升和集中度下降可以同时成立，故需要把记录数与同届份额并排阅读。",
  "S6 王者与传奇：原始表有姓名截断、同名跨越40年以上及一个ID对应多个姓名的情况。按姓名聚合得到的23条金牌行候选不能直接认定为某位运动员的真实成绩；人物榜必须逐个连接权威身份资料核验。该专题把“无法可靠识别个人”作为数据发现，而非用漂亮排名掩盖错误。",
 ], EXTRA/"S5_逐届获奖记录.png", "图为运动员获奖记录，非官方小项奖牌；姓名候选证据见任务三S6。"),
 ("03  补充专题 S8—S9", "她们被看见，赛场也在更替", [
  "S8 她们登上领奖台：女性获奖运动员记录占比从1896年的0%升至2024年的50.3%，与女性参赛记录占比49.1%以及女子专属小项占比45.9%回答不同问题。团体规模和项目设置会改变三种比例，不能以单一50%宣称机会已完全对称。",
  "S9 消失的赛场：拔河、槌球、马球与艺术竞赛的最后出现年份提供项目更替线索；花样滑冰与冰球也曾出现在夏季奥运记录。Sport名称改写、拆分及重返会造成假退出，因此先用任务一的运动家族映射，再将“本表最后出现”与IOC正式项目沿革严格区分。",
 ], EXTRA/"S8_女性获奖记录占比.png", "图为女性获奖行占全部获奖行比例；主分析排除1906。S9项目矩阵见任务二与任务三。"),
 ("03  补充专题 S10", "项目机会结构，藏在总榜背后", [
  "S10 奖牌藏在哪些项目：田径4,364条、游泳3,457条、赛艇3,126条，前三运动家族共10,947条获奖运动员记录，占主分析获奖记录的28.5%。这些总量同时受小项数量、举办届次和团队成员数影响，不是运动难度或代表团实力的直接测量。",
  "要比较代表团真正的项目优势，下一步应计算同届该运动获奖记录中的代表团份额，并与官方小项机会数交叉核对。S3—S10各专题有独立交互页面、分析数据和研究说明；S7等自拟专题的正式申报资格仍以组委会备案规则为准。",
 ], EXTRA/"S10_体育大类获奖记录.png", "图为1896—2024归一体育大类的运动员获奖记录；主分析排除1906。"),
  ("03  十专题共同方法", "十个直觉，经得起几次换口径？", [
   "每个专题先写出未经检验的直觉，再给出替代统计单位或纳入规则、反例和证据边界。五个跨任务核心结论另设17项预先指定的口径、窗口与门槛变体：长期集中度下降4/4、近期反弹2/2、代表团小项卫冕率下降4/4；显著排名重排只在运动员行的2/4变体成立，原七例代表最小团体在0/3变体成立。变体相关，不是结论为真的概率。",
   "例如西班牙2024金牌排名从官方小项第15变为运动员行第5；原S4七个故事案例均不符合客观最小四分位门槛；2024女子获奖行占50.3%，女子专属小项却占45.9%。它们要求我们先明确问题与分母，再决定结论能说到哪里。完整十题证据卡与复算表见任务三“结论稳定性地图”。",
  ], TMAP/"结论稳定性地图.png", "红色为口径敏感，蓝色为证据不足；逐题原始数据和来源可从专题卡进入。"),
]
# Lead with the counterintuitive result, then show the data audit that supports it.
lead = next(i for i, item in enumerate(pages) if item[1] == "同一规则下，排名仍然改变")
pages.insert(0, pages.pop(lead))
# The two short audit pages left a large blank area; merge them around one
# explanatory figure while retaining the key exclusions and quality rules.
pages[1] = (
    "01  数据体检", "先给每个数字一个单位", [
        "原始表有252,565行、11列，一行是一名运动员在一届、一个小项中的一条记录，团体成员各占一行。主分析排除1906届，得到250,832条参赛记录、38,360条奖牌记录；1956双城按同届汇总，历史代表团身份分列。",
        "76种Sport原值归为运动家族；89条逗号拼接记录按规则处理。2020年起Event泛化，不能据Men、Women反推具体小项。姓名与player_id不可靠，记录行不称独立运动员人数。12项质量检查的代码、结果和处理决定见任务一。",
        "2024年外部逐项结果层有329个金牌小项，而原CSV有2,281条运动员奖牌记录。前者回答赢了多少比赛单元，后者记录多少获奖成员。外部结果层也不能修复CSV中已丢失的小项名称；图表必须标出所用统计单位。",
    ], S2/"S2_金牌数量与获奖者规模.png",
    "口径与复算：任务一《数据质量与口径说明书》；2024外部逐项结果层的来源与链接标记见同目录。"
)
del pages[2]
for idx, item in enumerate(pages, 2):
    section,title,paragraphs,chart,note=item
    arguments={
      "冠军王朝的保质期": (
        "同一代表团对小项金牌的控制，似乎越来越难长期保持。",
        "在固定队列的17种运动中，8种卫冕率与总体下降方向相反；时间窗也改变下降幅度。",
        "固定113个连续小项后，早段34.5%、后段27.1%，整体下降7.37个百分点。结论限于小项控制权，不能归因为个人能力或单一制度。",
      ),
      "回测与不确定性边界": (
        "项目级机器学习加入历史基线，应当让预测持续变准。",
        "2012年混合模型MAE 2.46枚，劣于基线2.02枚；赛前回放中主场调整未在三届都改善误差，估计率还都触及18%上限。",
        "2024年混合核心在赛前估计奖牌池下MAE为2.77枚，优于基线2.94枚；但2024奖牌池低估63枚。资格变化和新增运动仍是未解决的不确定性。",
      ),
      "缺席与突破，都需要正确的分母": (
        "七个引人注目的夺牌故事，很容易被看作最小代表团的共同轨迹。",
        "七例均不满足严格下四分位规模门槛；把未获奖者放回分母，62个团中53个未获奖、8个仅一届获奖。",
        "一届获奖是突破，不自动成为持续崛起。另有1个团在两届获奖；2024首次获奖者没有下一届可随访。S3缺席与身份边界仍单列。",
      ),
      "十个直觉，经得起几次换口径？": (
        "一张图表若很有说服力，其结论似乎就足够稳固。",
        "预设17个口径与窗口变体中，原七例代表最小团体0/3成立；显著排名重排仅在2/4变体成立。",
        "长期集中度下降4/4、近期反弹2/2、固定小项卫冕率下降4/4。结论应随统计单位和纳入规则陈述；变体通过率不是事实概率。",
      ),
    }
    if title in arguments:
        special=chart
        if title=="冠军王朝的保质期":special=DEL/"任务三_专题深挖/S3_冠军的保质期/10_王朝机制与反例/逐运动反例.png"
        if title=="回测与不确定性边界":special=DEL/"任务四_开放创作/05_满分升级/09_赛前条件回放/赛前条件回放.png"
        if title=="缺席与突破，都需要正确的分母":special=DEL/"任务三_专题深挖/S4_小代表团的大突破/03_突破还是持续/突破持续分布.png"
        argument_page(c,idx,section,title,arguments[title],special,note)
    else:report_page(c,idx,*item)

chrome(c, len(pages)+2, "结论  /  局限与复现", "先声明在数什么，再解释谁领先")
y=688
for p in [
 "三个主要发现：第一，奥运规模扩张与奖牌份额长期去集中化并存，但2016—2024出现反向波动，不能写成单调趋势；第二，女性参与记录接近平衡仍不等于小项机会完全对称；第三，同一金牌排名规则下，运动员行与小项口径仍能显著重排榜单，并在多届重复出现。",
 "证据边界：原CSV自2020年起Event泛化、运动员身份不可靠；历史小项估计并非逐项官方表；主场效应存在选择偏差；2028预测区间来自有限回测。所有中间表、清洗代码、映射和质量检查按任务目录交付。",
 "三项创新交互：口径实验室用连续权重寻找榜单换位阈值；王朝生存图按运动与年代展示优势寿命，并标记2016右删失；2028赛后验收单预先固定MAE、排名相关和前十命中，等待实际成绩。复现顺序：先运行任务一，再运行任务二、三、四；完整方法和数据表以各任务目录为准。",
]: y=para(c,p,49,y,W-98)-18
txt(c,"核心参考资料",49,y-5,13,TEAL); y-=24
refs=[
 "Stefany De Oliveira, Summer Olympics Medals (1896–2024), Kaggle；赛题主数据，CC BY-NC-SA 4.0。",
 "Nitish Sharma, Olympics 124 years Dataset (till 2020), Kaggle；主数据历史上游。",
 "Petro Ivaniuk, Paris 2024 Olympic Summer Games, Kaggle；主数据2024上游。",
 "IOC, Paris 2024: Record-breaking Olympic Games on and off the field；329小项结构核验。",
 "Olympics.com, Paris 2024 Results；逐项结果入口。法兰西岛大区开放数据平台：2024逐项获奖开放数据。",
 "IOC, LA28 event programme 与 five additional sports 公告；2028项目总数与新增运动。",
 "国际单项联合会排名快照及获取日期见任务四模型说明；逐项URL与构造标记见任务一数据表。",
]
for i,p in enumerate(refs,1): y=para(c,str(i)+". "+p,50,y,W-100,small)-9
c.showPage()

chrome(c, 20, "资料  /  来源与连接逻辑", "外部数据如何进入作品")
y=690
sources=[
 ("赛题主数据", "https://www.kaggle.com/datasets/stefanydeoliveira/summer-olympics-medals-1896-2024", "文件olympics_dataset.csv；清洗保留原字段，以Year、NOC、Sport归一结果构建历史统计。历史上游Nitish Sharma与2024上游Petro Ivaniuk见赛题2.1及任务一说明。"),
 ("2024逐项获奖", "https://data.smartidf.services/api/explore/v2.1/catalog/datasets/paris-2024-resultats-des-medailles-pour-chaque-discipline-olympique/exports/csv", "法兰西岛大区开放平台；1,044条原始记录按Code_Discipline + Event聚合成329个小项。与主CSV按届次、代表团和归一运动家族比较，绝不覆盖泛化Event。快照哈希和3条构造链接见任务一审计JSON。"),
 ("IOC赛事结构", "https://www.olympics.com/ioc/news/paris-2024-record-breaking-olympic-games-on-and-off-the-field", "用于独立核验巴黎2024共329个奖牌小项；具体获奖结果入口见olympics.com/en/paris-2024/medals。"),
 ("LA28项目设置", "https://www.olympics.com/ioc/news/la28-event-programme-marks-strong-commitment-towards-innovation-and-gender-equality", "用于353个奖牌小项的预测规模假设。新增运动的国际排名来源与快照日期列在任务四“新增项目权威排名特征.csv”，只作为预测情景输入。"),
]
for name,url,method in sources:
    txt(c,name,49,y,11,TEAL);y-=11
    y=para(c,url,50,y,W-100,small)-7
    y=para(c,method,50,y,W-100,small)-23
txt(c,"完整字段字典、质量检查代码、外部快照与复现命令，分别见任务一至任务四目录。",49,y,9,MUTED)
c.showPage()
c.save()

# The base report is 19 pages; this evidence appendix makes the submitted PDF 20.
from build_evidence_hierarchy import OUT as EVIDENCE_OUT
from append_evidence_report_page import append_page
append_page()

# A2 poster: fewer claims, larger labels, and two readable self-drawn comparisons.
PW, PH = A2
poster = FINAL / "海报/百年圣火_A2海报_正式版.pdf"
poster.parent.mkdir(parents=True, exist_ok=True)
p = canvas.Canvas(str(poster), pagesize=A2, pageCompression=1)
p.setTitle("百年圣火｜A2数据海报")
p.setFillColor(PAPER); p.rect(0,0,PW,PH,fill=1,stroke=0)
txt(p,"百年圣火",70,PH-123,53,TEAL)
txt(p,"谁被看见，取决于我们在数什么",72,PH-173,25,INK)
txt(p,"1896—2024 夏季奥运数据观察  /  晓组织 · 燕山大学",73,PH-208,13,MUTED)
p.setStrokeColor(RULE);p.line(70,PH-233,PW-70,PH-233)

cards=[("252,565","原始参赛记录行"),("329","巴黎2024小项"),("49.1%","2024女性参赛记录占比")]
for i,(value,label) in enumerate(cards):
    x=72+i*358
    p.setFillColor(HexColor("#e8eff1"));p.roundRect(x,PH-365,333,108,12,fill=1,stroke=0)
    txt(p,value,x+21,PH-307,32,TEAL);txt(p,label,x+21,PH-338,13,MUTED)

txt(p,"01  同一届奥运，两种金牌计数",72,PH-433,22,INK)
txt(p,"运动员金牌行统计获奖成员；小项金牌统计获胜比赛单元。",73,PH-464,14,MUTED)
table_y=PH-535
for i,(name,rows,units) in enumerate([("美国",131,40),("中国",71,40),("荷兰",67,15),("西班牙",40,5)]):
    yy=table_y-i*67
    txt(p,name,77,yy,17,INK)
    p.setFillColor(HexColor("#dfe9ec"));p.roundRect(185,yy-5,550,22,6,fill=1,stroke=0)
    p.setFillColor(TEAL);p.roundRect(185,yy-5,550*rows/131,22,6,fill=1,stroke=0)
    txt(p,f"{rows} 行",750,yy,16,TEAL)
    txt(p,f"官方小项 {units} 金",918,yy,15,RED)
txt(p,"同为40枚小项金牌，美国131行、中国71行；荷兰15枚小项金牌对应67行获奖记录。",73,PH-819,13,MUTED)

txt(p,"02  女性参与接近平衡，小项结构仍有距离",72,PH-888,22,INK)
for i,(label,value) in enumerate([("女性参赛记录",49.1),("女性奖牌记录",50.3),("女子专属小项",45.9)]):
    yy=PH-951-i*65
    txt(p,label,77,yy,16,INK)
    p.setFillColor(HexColor("#dfe9ec"));p.roundRect(260,yy-4,650,23,6,fill=1,stroke=0)
    p.setFillColor(RED if i==2 else TEAL);p.roundRect(260,yy-4,650*value/60,23,6,fill=1,stroke=0)
    txt(p,f"{value:.1f}%",947,yy,18,RED if i==2 else TEAL)
txt(p,"三种分母不同；人数接近不能代替项目机会的结构分析。",73,PH-1149,13,MUTED)

txt(p,"03  反直觉：主场优势并非人人都有",72,PH-1225,22,INK)
txt(p,"九个现代主办案例中八个主办届份额上升；巴西2016却由3.04%降至2.47%。",73,PH-1270,16,INK)
txt(p,"主办权并非随机分配。匹配与合成对照提供参照，不能给出严格因果净效应。",73,PH-1305,13,MUTED)

p.setStrokeColor(RULE);p.line(70,PH-1385,PW-70,PH-1385)
txt(p,"口径与来源",72,PH-1428,19,TEAL)
for i,line in enumerate([
 "主分析排除1906；历史NOC分立；1956双城按同届；2020年后Event泛化不用于小项趋势。",
 "主数据：Kaggle Summer Olympics Medals (1896–2024)及两个上游；许可CC BY-NC-SA 4.0。",
 "2024逐项结果：开放数据平台；IOC官方核验329小项。完整来源、代码和质量检查见任务一。",
 "预测、冠军王朝与交互专题见作品总入口。团队：张子涵60%，陈旭40%。",
]): txt(p,line,73,PH-1472-i*31,12,MUTED)
p.save()

# The editorial poster is generated from the submitted tables. Keep this call
# after the legacy drawing block so future report rebuilds retain the final art.
from runpy import run_path
run_path(str(ROOT / '项目工作区/scripts/poster_zine.py'), run_name='__main__')

for src in (report, poster):
    copy2(src, ROOT/"项目工作区/deliverables"/src.name)
print(report)
print(poster)
