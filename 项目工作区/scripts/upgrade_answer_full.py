from pathlib import Path
from docx import Document
from docx.shared import Cm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import subprocess

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / '交付文件/最终提交材料/数说奥运_晓组织_正式答卷.docx'
subprocess.run(['py',str(ROOT/'项目工作区/scripts/fill_answer_template.py')],check=True,capture_output=True)
subprocess.run(['py',str(ROOT/'项目工作区/scripts/task3_answer_charts.py')],check=True,capture_output=True)
d = Document(BASE)

def find(starts):
    return next(p for p in d.paragraphs if p.text.startswith(starts))

def para_before(anchor, text, kind='body'):
    p = anchor.insert_paragraph_before(text)
    p.style = d.styles['Normal']
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.25
    for r in p.runs:
        r.font.name = 'Microsoft YaHei'
        r.font.size = Pt(10.5 if kind=='body' else 16)
        r.font.color.rgb = RGBColor(27,54,61) if kind=='body' else RGBColor(14,69,79)
        r.bold = kind=='head'
    if kind=='head':
        p.paragraph_format.space_before = Pt(11)
        p.paragraph_format.space_after = Pt(5)
        p.paragraph_format.keep_with_next = True
        p.paragraph_format.page_break_before = False
    return p

def image_before(anchor, rel, caption, width=13.5):
    path = ROOT/rel
    assert path.exists(), path
    p = anchor.insert_paragraph_before()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(3)
    p.paragraph_format.space_after = Pt(1)
    p.add_run().add_picture(str(path),width=Cm(width))
    c = anchor.insert_paragraph_before(caption)
    c.alignment = WD_ALIGN_PARAGRAPH.CENTER
    c.paragraph_format.space_after = Pt(5)
    for r in c.runs:
        r.font.name='Microsoft YaHei';r.font.size=Pt(8.5);r.font.italic=True;r.font.color.rgb=RGBColor(86,105,110)

# Task II: an additional core figure and a mechanism or counterexample for every perspective.
a = find('B．国家兴衰')
para_before(a,'复核反例：1904 年美国的极高份额来自当年异常狭窄的国际参赛覆盖，不能外推为现代竞技优势。若把历史累计榜直接解释为“单届实力”，长期参赛、代表团规模和团体成员数都会造成偏差。交互看板提供逐届排名切换；读者可同时检查绝对记录数、当届份额和前五集中度。')
image_before(a,'交付文件/任务二_百年全景/04_核心图表/A_历史累计奖牌记录榜.png','图 A2｜历史累计获奖记录榜。运动员行口径；排除 1906；累计量受参赛届数和团队人数影响。')

b = find('C．她的奥运')
para_before(b,'交叉验证：小多图与时代热力图使用同一逐届份额表。美国、苏联、两德、中国、日本、韩国和澳大利亚等并排展示，可直观看到冷战、抵制潮与政体断点。无参赛记录的灰格不能视为零；若把多个历史 NOC 强行合并，原本的时代转换会被错误平滑。主场分析虽提高了对机制的理解，仍只是一组带选择偏差的准实验关联。')
image_before(b,'交付文件/任务二_百年全景/04_核心图表/B_强国时代热力图.png','图 B2｜代表团时代热力图。运动员获奖记录份额；灰色为无参赛记录；排除 1906。')

c = find('D．项目演化')
para_before(c,'代表团差异是“三层平权”结论的反例检验。2024 年的女性获奖记录占比已经超过半数，但若只看参赛规模，会遮蔽不同代表团在游泳、田径、团体项目等机会结构上的差异；若只看获奖比例，又会把项目组合误读成单一的制度评价。图中只选记录量较大的代表团，降低小样本比例极端波动。')
image_before(c,'交付文件/任务二_百年全景/04_核心图表/C_2024代表团女性结构差.png','图 C2｜2024 代表团女性参赛与获奖记录占比之差。单位为百分点；运动员行口径。')

e = find('Ⅲ　专题深挖')
para_before(e,'生命周期分解显示，“小项数增加”之外还有持续的替换。首次出现定义为新增；此前出现、上届缺席后再次出现定义为重返；本届出现而下届缺席定义为本届后退出。它们均是数据操作性分类，不等于 IOC 的永久项目决定。2020 年 Event 泛化造成的缺口被公开留白，2024 采用官方 329 小项，避免制造虚假的结构断崖。')
image_before(e,'交付文件/任务二_百年全景/04_核心图表/D_项目新增退出重返流向.png','图 D2｜体育大类新增、退出与重返。依据任务一归一体育大类；排除 1906；分类为数据观察口径。')

# Template asks to copy the topic section when multiple topics are selected.
sel = find('本队所选专题：')
sel.text = '本队所选专题：S1 东道主效应、S2 口径的魔力、S3 地缘政治的投影、S4 小代表团的大突破、S5 奖牌的通货膨胀、S6 王者与传奇；另附 S7 冠军的保质期、S8 她们登上领奖台、S9 消失的赛场、S10 奖牌藏在哪些项目。自拟专题的正式参赛资格以组委会备案要求为准。'

# S1 is inserted before the existing S2 answer.
s2 = find('同一届比赛，改变统计单位')
para_before(s2,'专题 S1｜东道主效应：主场真的能换来奖牌吗？','head')
para_before(s2,'研究问题是主办届的获奖增益是否超过其原有趋势与同期其他代表团的变化。九个现代案例中，八个主办届的获奖运动员记录份额上升；中国 2008 年较前届增加 4.29 个百分点，西班牙 1992 年增加 3.71 个百分点，巴西 2016 年却下降 0.57 个百分点。反例说明“主办必然爆发”并不成立。图中同时展示主办前后届路径，避免只截取高光年份。')
image_before(s2,'交付文件/任务三_专题深挖/S1_东道主效应/S1_host_windows.png','图 S1-1｜九个现代主办案例前后届变化。运动员获奖记录份额；排除 1906；1956 双城按一届。')
para_before(s2,'机制与稳健性：在任务二的扩展分析中，17 个可用主办案例的合成对照平均主办届差为 +3.37 个百分点；14 个前期拟合较好的案例为 +2.24 个百分点，排除 1956 双城和 1980/1984 抵制届后仍为 +2.52 个百分点。图形把真实路径与合成路径并置，比单纯前后差更能显示异常增益。不过主办权由申请、投入与政治经济条件决定，提前备战和参赛名额变化仍可能影响估计；结论应表述为稳健关联，而非自然实验。')
image_before(s2,'交付文件/任务二_百年全景/04_核心图表/B_20届合成对照与稳健性.png','图 S1-2｜扩展合成对照与稳健性。指标为同届获奖运动员记录份额；非严格因果识别。')
para_before(s2,'数据与复现：任务二的 B_20届主办事件研究.csv、B_合成对照权重.csv 和 B_留一法稳健性.csv；S1 专题目录保存案例窗口和原始分析图。')
para_before(s2,'专题 S2｜口径的魔力：一张榜单到底奖励什么？','head')

iv=find('Ⅳ　开放创作')
# add more S2 evidence after existing section, before the next topic
para_before(iv,'三口径延伸：官方小项口径回答赢下多少竞赛单元，运动员行口径回答产生多少获奖者，团队内均分口径把同一获奖组总权重固定为1并分给成员。只用2024官方329小项做35次逐运动大类剔除，关键代表团的重排方向均未反转。2008、2012、2016历史小项仍有待核项，只作探索性展示，不承担正式结论的证据责任。')
image_before(iv,'交付文件/任务三_专题深挖/S2_口径的魔力/04_核心图表/S2_三口径排名路径.png','图 S2-3｜官方小项、运动员行与团队内均分三种口径的排名路径；统计单位决定结论。')

topics=[
('S3｜地缘政治的投影：缺席不等于失败',
 '1980 与 1984 两届在原始数据中分别出现 80 与 140 个代表团，提示抵制潮与制度环境可能改变参赛覆盖。但只凭总量不能判定任何单一代表团缺席的原因，也不能把未参赛当作零奖牌。图表把前后届放在同一坐标中，让异常幅度可见，再由历史资料解释事件背景。',
 '苏联、独联体联队、俄罗斯、俄罗斯奥委会代表队和个人中立运动员不能合并为一条无断点曲线；东德、西德与统一德国亦分别保留。保留历史 NOC 可看见政体重组在数据里的投影。1956 双城按一届汇总，1906 排除。此专题展示的是数据覆盖变化与身份边界，不对抵制原因做未经外部核验的因果判断。',
 '交付文件/最终提交材料/答卷附图/S3_代表团覆盖变化.png','图 S3｜逐届有记录的代表团数量。口径：原表 NOC 去重；排除 1906；1980/1984 为覆盖异常，不直接等同政治参与名单。'),
('S4｜小代表团的大突破：总量之外看项目路径',
 '中国香港、中华台北、新加坡、斐济、百慕大、约旦、科索沃等案例说明，小代表团的表现通常集中在少数优势项目。中国香港 2020 年有 8 条获奖运动员记录；新加坡 2012 年有 4 条；中华台北 1992 年有 20 条。整段历史的获奖记录总量能够展示可见度，却会受参赛年份和团队人数影响。',
 '项目拆解更有解释力：斐济的橄榄球、中华台北的棒垒球、新加坡的乒乓球、科索沃的柔道都呈现不同路径。比较“效率”时应同时报告参赛记录作分母，避免把参加届数少、规模小的代表团与百年常客直接比累计值。样本是探索性案例集合，不代表所有小代表团；团体项目获奖行数不能当作官方奖牌数。',
 '交付文件/最终提交材料/答卷附图/S4_小代表团获奖记录.png','图 S4｜七个案例的历史获奖运动员记录。口径：原表获奖行；排除 1906；总量不是效率。'),
('S5｜奖牌的通货膨胀：机会也在扩容',
 '1896 年有 143 条获奖运动员记录、12 个有记录的代表团；2024 年为 2,281 条和 206 个。绝对获奖记录增加，并不意味着同一标准下每个代表团更容易获奖。小项总量、团队人数、参赛资格和数据覆盖共同改变了“记录机会”的分母。图表并列参赛规模与获奖记录，避免把一条向上的绝对值线误读成竞技竞争变弱。',
 '对比任务二的前五代表团份额可见，绝对量上升同时伴随集中度下降。这个反直觉现象提示可视化必须同时展示绝对数和份额。2020/2024 年 Event 字段的口径变化不用于原始小项数趋势；若要说官方奖牌规模，必须切换到官方小项表。这个专题使用运动员行，主分析排除 1906。',
 '交付文件/最终提交材料/答卷附图/S5_逐届获奖记录.png','图 S5｜1896—2024 逐届获奖运动员记录。口径：运动员行；排除 1906；不可称官方奖牌枚数。'),
('S6｜王者与传奇：姓名不能直接当身份',
 '原始数据存在明显的姓名截断与编号复用风险。一个被截断的姓名字符串对应 23 条金牌行、跨四届；若直接按字符串排序，榜首看似漂亮，实际可能是错误拼接或名字缺失。数据体检发现 12,883 个 ID 对应多个姓名、670 个姓名跨度超过 40 年。两种风险同时存在：同一人被拆成多个名字，不同人被合并成一个名字。',
 '本专题把姓名榜定位为“人工核验候选清单”，展示原始姓名、首次与末次年份、涉及届次和金牌行数，不宣称正式的史上个人奖牌排名。要判断真正的奥运传奇，需要用 IOC 运动员身份资料逐人核对，并处理团体、接力与姓名变体。这里保留问题本身作为结论：数据实体识别质量足以颠覆人物榜。',
 '交付文件/最终提交材料/答卷附图/S6_姓名候选记录.png','图 S6｜原始姓名聚合的金牌行候选。未经权威身份核验，不能作为个人历史排名。'),
('S7｜冠军的保质期：王朝能延续多久？',
 '用“某代表团在同一体育大类连续夺得金牌”的连续届数定义王朝，可以把“冠军”从一次胜利转为时间结构。现有研究发现，最强王朝并非永恒；主力更替、项目改制和竞争对手成长都会打断连胜。时间轴展示各王朝起点、峰值与终点，提醒读者不要只从累计奖牌数推断持续统治。',
 '跨项目比较还需解决参赛机会不均：游泳、田径拥有较多小项，单项运动夺冠机会不同。因此专题同时呈现时代卫冕率和项目差异，并把同一体育大类连续夺冠视为研究定义，而非 IOC 官方“王朝”称号。历史记录受项目进入和退出影响，空白年份要区分未参赛、无该运动与未夺冠。该自拟专题的正式参赛资格以组委会备案要求为准。',
 '交付文件/任务三_专题深挖/S3_冠军的保质期/04_核心图表/S3_最长冠军王朝.png','图 S7-1｜最长冠军王朝。按代表团×体育大类的连续金牌届次定义；非 IOC 官方称号。'),
('S8｜她们登上领奖台：看见获奖记录的变化',
 '1896 年女性获奖运动员记录占比为 0，2024 年达到 50.3%。这条曲线比单纯参赛占比更接近领奖台上的可见度，但它仍受女子小项数量、混合小项及团体成员规模影响。女性参赛记录占比 49.1% 与获奖记录占比 50.3% 测量不同对象，两者不能互相替代，也不能由占比接近直接推出机会完全平等。',
 '分析将每届女性获奖行除以当届全部获奖行，并与任务二的三层平权曲线交叉核对。2024 女子专属小项约占官方 329 项的 45.9%，说明参赛、获奖和赛程设置并非同一个“平权指标”。原始 Sex 仅有 M/F 两值，不能用它讨论更广义的性别身份；主分析排除 1906。',
 '交付文件/最终提交材料/答卷附图/S8_女性获奖记录占比.png','图 S8｜逐届女性获奖运动员记录占比。分母为全部获奖行；排除 1906；不等于独立女性人数。'),
('S9｜消失的赛场：退场与重返如何识别',
 '拔河、槌球、马球、艺术竞赛等运动曾在奥运留下记录。花样滑冰和冰球也曾出现在夏季奥运数据中，提醒读者不能用当代夏冬项目边界倒推百年前的赛程。图中用运动家族归一后的出现届数、首次和最后出现年份刻画历史轨迹；“最后一次出现在本表”是可观察事实，不等于永久退出奥运。',
 '一个项目可能改名、拆分、合并或重返。尤其 2020 年前后 Sport 命名漂移，若直接以原始字符串判断消失，会误报体操、场地自行车等项目。因此先使用任务一的 76 项原始值归一映射，再看存在矩阵；仍不能据此替代 IOC 正式项目沿革。1906 排除，2020/2024 名称变化作为敏感性风险提示。',
 '交付文件/最终提交材料/答卷附图/S9_历史项目出现届数.png','图 S9｜历史运动家族在数据中出现的届数。归一 Sport 后计算；不代表 IOC 永久取消。'),
('S10｜奖牌藏在哪些项目：机会结构改变总榜',
 '1896—2024 的获奖运动员记录中，田径、游泳和赛艇三大运动家族合计 10,947 条，占全部主分析获奖行的 28.5%。田径 4,364 条、游泳 3,457 条、赛艇 3,126 条。条形长度同时反映小项数、举办届数和团体成员数；不能把它解释成单纯的运动难度、国家实力或官方奖牌分配。',
 '若要比较代表团优势，更合适的分母是“该运动在同届全部获奖记录”，再看某代表团所占份额，并按历史阶段分层。否则早期进入奥运、项目众多的运动天然累积更多记录。这个专题把机会结构置于奖牌格局之前，解释为什么不同国家即使官方小项成绩相似，运动员行榜仍可能明显不同。主分析排除 1906。',
 '交付文件/最终提交材料/答卷附图/S10_体育大类获奖记录.png','图 S10｜归一体育大类的历史获奖运动员记录。口径：运动员行；排除 1906；不可读为官方奖牌数。'),
]

for heading,one,two,path,caption in topics:
    para_before(iv,'专题 '+heading,'head')
    para_before(iv,one)
    image_before(iv,path,caption)
    para_before(iv,two)
    if heading.startswith('S7'):
        image_before(iv,'交付文件/任务三_专题深挖/S3_冠军的保质期/04_核心图表/S3_时代卫冕率.png','图 S7-2｜不同时代的卫冕率。须结合项目机会与参赛覆盖解读。')

supplements={
 'S3':'进一步核查时，先把“没有该代表团记录”与“参加但没有奖牌”分开编码，再回到具体年份查看参赛行、获奖行与项目分布。1980/1984 的异常若只用奖牌榜呈现，会漏掉根本没有参赛的代表团；若只用参赛总量，又会把项目设置变化和政治事件混在一起。故本专题的结论限定为数据中可见的覆盖断点，历史原因通过外部史料解释，图表本身不承担它无法证明的因果推断。复现数据为 S3/分析数据.json，源于归一后的主分析表。',
 'S4':'一个有意义的反例是斐济：橄榄球团队获奖会形成多条运动员记录，使其累计获奖行数明显高于官方奖牌枚数。若换成官方小项口径或“每参赛记录的获奖率”，排序可能改变。网页允许点击代表团查看参赛记录与优势项目，正是为了让读者从“有多少”追问“靠什么项目、投入了多少参赛机会”。该分析没有把小样本的高比率解释成普遍规律，也没有用规模筛选后的案例外推全部代表团。',
 'S5':'对“通胀”一词必须设边界：这里增长的是运动员获奖记录，而不是奖牌材质本身贬值。团体比赛人数增加，会放大行口径；小项增加，会扩大可颁奖的竞赛单元；参赛代表团增加，会改变争夺这些机会的竞争密度。把三种机制拆开，才可能讨论哪一种扩张更重要。作为稳健性检查，主报告同时展示按同届总获奖行归一的前五份额；若绝对记录和份额得出相反方向，应优先解释分母变化，而不是择一报道。',
 'S6':'姓名问题与赛题的数据质量要求直接相连。对同名跨越 40 年的 670 个姓名，应先抽样核验出生年份和参赛项目；对同一编号对应多个姓名的 12,883 个 ID，应核查编号来源和复用规则。未经这些步骤，任何“史上最强个人”都可能是实体识别错误。专题的可视化因此刻意把“候选”放在标题与图注中，不让读者误以为图表已完成身份认证。若未来接入 IOC 人物页，可逐人建立来源链接和人工判定日志。',
 'S7':'王朝持续时间也受到奥运届次间隔和停办年份影响。连续届数比连续自然年更适合比较奥运冠军，但战争造成的停办不应被错误视为卫冕失败；项目退出后也不能继续把“未获金”计入风险集。专题采用代表团×体育大类的届次序列，并把项目存在状态独立编码。时代卫冕率用来验证最长王朝是否只是少数极端案例。它揭示的是长期统治的稳定性，不评价单届运动员的个人贡献。',
 'S8':'2024 女性获奖行比例高于参赛行比例约 1.2 个百分点，并不说明女性在所有运动中拥有更高胜率，因为同一个团体项目可产生多人获奖行，而且不同性别的项目数量与队伍规模并不一致。更公平的下一步是按体育大类分层、以参赛行作分母计算同类获奖率，再与官方女子专属小项供给交叉核对。本专题先把三个分母并列，明确“被看见”“参赛机会”和“赛程配置”各自回答的问题。',
 'S9':'本专题与任务二 D 的项目生命周期分析互相校验：前者讲具体运动家族的历史，后者汇总每届新增、退出与重返数量。若二者对同一运动给出不同判断，首先检查 Sport 归一映射、1906 排除规则和 2020 后命名变化，而不是立刻修改图表结论。花样滑冰与冰球的夏奥记录也证明，“消失”可能只是从夏季赛程转移到冬季赛程。所有叙述坚持“在本表最后出现”的精确措辞。',
 'S10':'条形图的前三类占比约 28.5%，但这个集中度本身没有公平或不公平的价值判断。田径和游泳拥有较多小项，赛艇有多人艇，三者的记录生成机制不完全相同。可交叉检验两种榜：按体育大类的获奖运动员行排序，以及按官方小项机会数标准化后的代表团份额；若某国只在某一类高机会运动中领先，其总榜优势便需要分解说明。现有图提供的是全局机会地图，代表团层面的优势归因留给交互筛选。',
}
for code,body in supplements.items():
    heading=next(p for p in d.paragraphs if p.text.startswith('专题 '+code+'｜'))
    all_paras=d.paragraphs
    pos=next(i for i,p in enumerate(all_paras) if p._p is heading._p)
    next_heading=next((p for p in all_paras[pos+1:] if p.text.startswith(('专题 S','Ⅳ　'))),iv)
    para_before(next_heading,body)

# The complete backtest graphic remains in the task-four attachment; the template
# answer keeps one overview figure so its final checklist stays together.

# Consistent design, with the original template's section sequence and cover retained.
sec=d.sections[0]
sec.top_margin=Cm(2.2);sec.bottom_margin=Cm(2.0)
sec.left_margin=Cm(2.35);sec.right_margin=Cm(2.35)
for p in d.paragraphs:
    p.paragraph_format.widow_control=True
    if p.text.startswith(('Ⅰ　','Ⅱ　','Ⅲ　','Ⅳ　')):
        p.paragraph_format.space_before=Pt(6)
        p.paragraph_format.space_after=Pt(8)
        p.paragraph_format.first_line_indent=Cm(0)
        for r in p.runs:
            r.font.name='Microsoft YaHei';r.font.size=Pt(16);r.font.bold=True;r.font.color.rgb=RGBColor(10,66,76)
    elif p.text.startswith(('A．','B．','C．','D．')):
        p.paragraph_format.space_before=Pt(10);p.paragraph_format.space_after=Pt(5);p.paragraph_format.keep_with_next=True;p.paragraph_format.first_line_indent=Cm(0)
        for r in p.runs:
            r.font.name='Microsoft YaHei';r.font.size=Pt(12.5);r.font.bold=True;r.font.color.rgb=RGBColor(12,82,91)
    elif p.text.startswith('专题 S'):
        p.paragraph_format.first_line_indent=Cm(0)
        p.paragraph_format.page_break_before=False
    elif not p._p.xpath('.//w:drawing') and p.text and not p.text.startswith(('图 ','图A','图B','图C','图D')):
        p.paragraph_format.line_spacing=1.25
        p.paragraph_format.space_after=Pt(3)
        p.paragraph_format.first_line_indent=Cm(0.74)
        p.alignment=WD_ALIGN_PARAGRAPH.JUSTIFY
cover=d.paragraphs[:9]
for p in cover[:3]:p.alignment=WD_ALIGN_PARAGRAPH.CENTER
for p in cover:p.paragraph_format.first_line_indent=Cm(0)
for r in d.paragraphs[1].runs:r.font.size=Pt(26);r.font.bold=True;r.font.color.rgb=RGBColor(9,59,68)
for p in cover[3:]:p.paragraph_format.space_after=Pt(7)

BASE.parent.mkdir(parents=True,exist_ok=True)
d.save(BASE)
print(BASE)
