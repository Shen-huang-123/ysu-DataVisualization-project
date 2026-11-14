from pathlib import Path
import json
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Image,PageBreak,Table,TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib import colors
import re
R=Path(__file__).resolve().parents[1];O=R/'outputs';D=R/'deliverables'
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
body=ParagraphStyle('body',fontName='STSong-Light',fontSize=10.5,leading=17,spaceAfter=9)
head=ParagraphStyle('head',parent=body,fontSize=21,leading=28,spaceAfter=18,textColor=colors.HexColor('#246477'))
small=ParagraphStyle('small',parent=body,fontSize=8,leading=12)
story=[]
team=json.loads((R/'docs/参赛信息.json').read_text(encoding='utf-8'))
def p(t,style=body):return Paragraph(escape(t),style)
def title(t):story.append(p(t,head))
def chart(name):
 im=Image(str(O/'figures'/f'{name}.png'));im.drawHeight*=490/im.drawWidth;im.drawWidth=490;story.append(im)
def page(t,text,image=None):
 title(t)
 if not story[:-1]:
  story.append(p(team['school']+' | '+team['team']+' | '+'；'.join(m['name']+' '+str(m['contribution_percent'])+'%' for m in team['members'])))
 for para in text.split('\n\n'):story.append(p(para))
 if image:chart(image)
 story.append(PageBreak())
def paragraphs(file):
 return [x for x in (R/'docs'/file).read_text(encoding='utf-8').split('\n\n') if x and not x.startswith(('#','核心图','复现：','产物：'))]
page('百年圣火 谁被看见','1896至2024年夏季奥运可视分析\n\n摘要：本作品从数据审计出发，分析奥运规模、女性参与及竞争结构。2024年双口径比较显示，在统一金牌排名规则后，统计单位仍改变代表团名次。九个主办案例包含增长与反例，提示主场提升及持续性不能一概而论。所有分析区分参赛记录、独立人数和小项奖牌，保留来源与不确定性。\n\n2024年已接入329个小项的外部逐项结果，并与IOC官方赛事总数核验。原CSV自2020年起的Event泛化不可逆；历史女子小项数属于字段推断。视频成片及提交渠道仍待确认。','C_female_records')
title('数据体检与统计边界')
for t in ['原始数据252565行、11列，无字段缺失。排除1906后为250832条参赛记录及38360条奖牌记录。记录不等于独立运动员人数。','player_id存在12883个一ID多姓名；670个姓名跨度超过40年。完全重复为0，但去掉ID后存在1466行重复余量，其中1315行属于艺术竞赛。保留候选并提供敏感性版本，不自动删除。','76种Sport原值全部映射到明确运动家族。家族不是IOC正式大项；2020年后Event泛化，不能直接按字符串去重恢复真实小项。1956双城按同一届统计；历史NOC分别保留；东京保留2020届次年份。']:story.append(p(t))
rows=[['检查','实测结果','处理'],['空值','0','保留语义检查'],['完全重复','0','不删除'],['去ID重复余量','1466','候选标记与敏感性'],['ID多姓名','12883','不作为人数ID'],['逗号Sport','89行','家族或赛事归属'],['1906奖牌记录','458','主分析排除']]
table=Table([[p(c,small) for c in row] for row in rows],colWidths=[160,110,220]);table.setStyle(TableStyle([('GRID',(0,0),(-1,-1),.4,colors.lightgrey),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e4edf0')),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),9)]));story.extend([table,PageBreak()])
pan=paragraphs('全景分析正文草稿.md')
for label,needle,img in [('A 规模与奖牌格局','数据中，1896','A_edition_scale'),('B 国家与历史边界','图中分别展示','B_country_trends'),('C 她的奥运','女性参赛记录占比','C_country_female_structure'),('D 项目的进入与离场','运动家族出现矩阵','D_sport_presence')]:
 page(label,next(x for x in pan if x.startswith(needle)),img)
page('S2 相同规则下的排名变化','两种计数均仅按金牌数降序，并列取最小名次，排除AIN。西班牙从第15升至第5，荷兰第6升至第3，日本第3降至第9。名次在各自完整榜中计算，图中展示15个明确映射代表团。\n\n剔除重复余量后，这15个代表团的金牌行名次均未改变。差异不来自金银铜排序规则，但也不能全归因于团体规模，原始记录完整性仍可能影响比较。','S2_same_rule_ranks')
page('S2 团体结构与解释边界','荷兰67行金牌记录中，曲棍球35行、赛艇11行，两者占68.7%。运动员行口径体现获奖成员记录的广度，小项口径体现获胜竞赛单元数。\n\n美国和中国小项金牌均为40枚，金牌行分别为131和71。金牌数并列不能称完整奖牌榜并列。外部表当前来自维基百科快照，官方页面访问受限，尚未一手核验。每枚小项金牌对应记录数也不能直接称平均队伍人数。','S2_2024_comparison')
page('S1 主办提升与反例','九个现代主办案例中八个主办届份额上升；巴西2016从前届3.04%降至2.47%。英国2012从3.96%升至6.49%，后届继续升至7.17%。\n\n法国2020为141行，与赛题引子96行不一致，2024为187行。本作品报告可复现实测值。2024无下一届数据。样本选择及项目结构可能影响结果，不作因果解释。','S1_host_windows')
page('同期比较 方法与局限','对每个主办案例，从前届与主办届均有奖牌记录的非主办代表团中，选择前届奖牌记录份额最接近的五个。同距按NOC排序，完整名单及变化保留在host_comparison_groups.csv。\n\n中国2008年的份额变化比比较组均值高约5.46个百分点，英国2012高约2.76个百分点。巴西自身下降，相对比较组却高约0.13个百分点，说明前后变化与同期比较回答不同问题。\n\n这不是因果净效应。比较组存在获奖存续筛选，未控制投入、项目结构、资格和抵制，也未验证平行趋势。团队记录并不独立，不以行数作为独立样本构造显著性结论。\n\n结论：统计单位、分母、历史边界及比较对象共同决定数据故事。先声明在数什么，再解释谁领先。')
title('来源与复现')
for t in ['主数据：Stefany De Oliveira，Summer Olympics Medals (1896-2024)，Kaggle。https://www.kaggle.com/datasets/stefanydeoliveira/summer-olympics-medals-1896-2024','上游：Nitish Sharma，Olympics 124 years Dataset (till 2020)，https://www.kaggle.com/datasets/nitishsharma01/olympics-124-years-datasettill-2020','上游：Petro Ivaniuk，Paris 2024 Olympic Summer Games，https://www.kaggle.com/datasets/piterfm/paris-2024-olympic-summer-games','外部奖牌表：https://en.wikipedia.org/wiki/2024_Summer_Olympics_medal_table 。HTML快照、SHA256及解析时间见outputs/paris2024_source_metadata.json；15个NOC显式映射连接，二手来源待核验。','复现：安装requirements.txt，运行python scripts/run_all.py。报告图文版由python scripts/report_layout.py生成。原始CSV不随包提交，清洗衍生数据遵循CC BY-NC-SA 4.0。','本地交互看板已通过筛选、排序与导出验收；实际小项及女子小项统计、视频成片尚待完成。当前版本不能视作最终提交。']:story.append(p(t))
def footer(c,doc):c.setFont('STSong-Light',9);c.drawString(42,24,'百年圣火 | 图文评审稿');c.drawRightString(550,24,str(doc.page))
SimpleDocTemplate(str(D/'百年圣火_图文评审稿.pdf'),pagesize=(595.28,841.89),rightMargin=42,leftMargin=42,topMargin=42,bottomMargin=42).build(story,onFirstPage=footer,onLaterPages=footer)
