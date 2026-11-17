"""Align current final document bodies; preserve and label legacy figure scenarios.

Run after publish_project_model_audit.py. Idempotent: fixed paragraph anchors and
PDF page regions are replaced, not appended. Never regenerate model results.
"""
from pathlib import Path
import hashlib,json,shutil
import pymupdf
from docx import Document

ROOT=Path(__file__).resolve().parents[2]
FINAL=ROOT/'交付文件/最终提交材料'
OUT=FINAL/'一致性核查'
OUT.mkdir(exist_ok=True)
BACK=ROOT/'项目工作区/outputs/report_revision_backups'
BACK.mkdir(exist_ok=True)
changes=[]
def backup(p):
    digest=hashlib.sha256(p.read_bytes()).hexdigest()
    dest=BACK/(p.stem+'_before_body_alignment_'+digest[:10]+p.suffix)
    if not dest.exists():shutil.copy2(p,dest)
    return digest

replacements=[
 ('预测：透明历史基线','预测：主阅读改用同口径的中性历史加权基准，近三次可用小项资料赋权0.2、0.3、0.5，并加入15%近期趋势。2028沿用1120总量作为比较条件，不声称是最终官方奖牌规模。原RF/GB按原参数、仅此前资料重跑：运动员行混合三折小幅改善，小项二次来源的2024基线MAE为1.872槽/队，55/45混合为1.900。45%权重没有稳定优势，保留为条件情景；原45/45/10集成不再作为主阅读。'),
 ('不确定性：历史基线','不确定性：新基准不附未经校准的80%区间。旧图中的区间仍属原版本情景，不可移植到新榜。历史版本为事后修订资料；2024小项回放最近特征为2016，间隔八年。2028新增运动、资格、主场与最终集成区间尚未完成同构回测。赛后按预设误差与覆盖指标验收，不把年份切分等同真实赛前冻结验证。'),
 ('图 IV-1｜2028 奖牌预测总览','图 IV-1｜旧版本2028条件情景图，保留展示原假设，不代表最新主阅读。最新同口径中性基准及逐折评分见任务四/05_满分升级/15_原项目模型时序核验。'),
 ('用“某代表团在同一体育大类','本专题区分两层对象：旧王朝图按代表团×体育大类连续金牌届次描述；最新正式推断按同一小项金牌控制权构建固定113项队列。早段卫冕率34.51%、后段27.14%，下降7.37个百分点；这不是个人冠军能力下降，也不能用体育大类图替代小项检验。'),
 ('跨项目比较还需解决参赛机会不均','来源敏感性：同113项替换二次来源后仍下降7.37个百分点，成组95%区间[-13.20,-1.62]；排除涉及未决项的完整系列后剩50项，下降7.33个百分点，但区间[-16.17,+1.50]跨零。不能声称排除检验也确认下降；二次来源及排除子集均非现行IOC认证。'),
 ('王朝持续时间也受到奥运届次','连续届数需区分停办、项目退出与未夺冠；旧体育大类时间轴仅作描述。正式结论以固定小项队列及完整系列来源敏感性为准。制度变化、参赛选择与运动构成没有被随机化，不据此确认竞争加剧的因果机制。自拟专题申报仍遵循组委会备案要求。'),
 ('机制与稳健性：在任务二的扩展分析中','机制与稳健性：原17个运动员行合成对照案例已复现；另建小项口径共同15案，原代理、二次来源替换、排除未决系列的平均主办届差分别为+3.02、+3.01、+2.87个百分点，成组区间均为正。巴西2016原五队匹配为+0.13，但小项合成对照原代理-0.11、替换后-0.17；统计单位与比较方法同时改变，不能拆分归因。平均关联不替每个案例背书，更不能解释成主办的因果收益。'),
]
p=FINAL/'数说奥运_晓组织_正式答卷.docx'
before=backup(p);d=Document(p);hits=[]
for prefix,new in replacements:
    # Updated opening is also an anchor on subsequent runs.
    matches=[x for x in d.paragraphs if x.text.strip().startswith(prefix) or x.text.strip()==new]
    assert len(matches)==1,(prefix,len(matches))
    if matches[0].text.strip()!=new:matches[0].text=new
    hits.append(prefix)
d.save(p)
changes.append({'path':str(p.relative_to(ROOT)),'before':before,'paragraphs':hits})

def replace_region(page,rect,text,size=10.4):
    box=pymupdf.Rect(*rect)
    page.add_redact_annot(box,fill=False)
    page.apply_redactions(images=0,graphics=0)
    page.insert_font(fontname='BodyCN',fontfile='C:/Windows/Fonts/simhei.ttf')
    left=page.insert_textbox(box,text,fontname='BodyCN',fontsize=size,lineheight=1.45,color=(.16,.21,.23))
    assert left>=0,('text overflow',page.number,left,text)

def working_pdf(path):
    src=pymupdf.open(path)
    if len(src)==20:
        doc=pymupdf.open(ROOT/'交付文件/任务四_开放创作/05_满分升级/15_原项目模型时序核验/原项目模型复核_最新交付附页.pdf')
        doc.insert_pdf(src);src.close();return doc
    assert len(src)==22 and '原项目模型复核 / 2026-11-17' in src[0].get_text()
    return src

for p in [FINAL/'报告/百年圣火_正式报告.pdf']:
    before=backup(p);doc=working_pdf(p)
    assert len(doc)==22 and '原项目模型复核 / 2026-11-17' in doc[0].get_text()
    replace_region(doc[2],(48,246,548,283),'百年全景呈现份额变化；冠军控制权采用固定小项队列；2028以中性基准为主阅读。\n新榜不附未经校准的区间；历史代理不称现行IOC授牌，主分析排除1906。')
    replace_region(doc[10],(142,326,544,373),'113项来源替换后下降7.37个百分点；排除未决系列剩50项，95%区间跨零。\n结论限于小项控制权；排除检验未确认下降，不能解释个人能力或单一制度。',9.4)
    replace_region(doc[12],(47,147,550,244),'主阅读采用同口径中性历史加权基准；2028总池1120仅为比较条件，不保证最终官方规模。\n原RF/GB同口径重跑未支持45%权重稳定占优；55/45混合与新增运动等保留为条件情景。\n下图为旧45/45/10集成版本，仅展示原假设；其点值与区间不得移植到最新基准。\n最新完整参考榜、覆盖边界与逐折误差见任务四第15项核验。')
    replace_region(doc[12],(51,750,549,779),'旧版条件情景图；主阅读以第15项核验的2028中性基准为准。',9)
    replace_region(doc[13],(142,244,544,286),'原RF/GB小项二次来源2024：基线MAE为1.872槽/队，55/45混合为1.900。\n运动员行混合三折均小幅改善，不能外推为官方奖牌预测稳定改善。',9.3)
    replace_region(doc[13],(142,326,544,372),'中性基准作为主阅读；45%项目权重只作情景，不称最优。\n真实赛前冻结资料、新增运动同构回放及最终区间校准仍未完成。',9.4)
    replace_region(doc[19],(48,241,548,273),'选择偏差；新2028基准不附未经校准区间，旧区间仅属旧情景。复算资料按任务目录交付。')
    tmp=p.with_suffix('.body-alignment.tmp.pdf');doc.save(tmp,garbage=4,deflate=True);doc.close();tmp.replace(p)
    changes.append({'path':str(p.relative_to(ROOT)),'before':before,'pages_updated':[3,11,13,14,20]})

# The answer has a different layout: never reuse report page coordinates.
p=FINAL/'数说奥运_晓组织_正式答卷.pdf'
before=backup(p);doc=working_pdf(p)
assert '专题 S3｜地缘政治' in doc[13].get_text(), 'Unexpected answer layout'
replace_region(doc[10],(66,63,560,163),replacements[6][1],10)
replace_region(doc[16],(66,471,560,527),replacements[3][1],9.5)
replace_region(doc[17],(66,328,560,401),replacements[4][1],10)
replace_region(doc[17],(66,633,560,711),replacements[5][1],10)
replace_region(doc[20],(66,425,561,511),replacements[0][1],9.4)
replace_region(doc[20],(66,518,560,579),replacements[1][1],9.1)
# Caption under the old forecast chart is on the last page; find it by text.
page=doc[21]
blocks=[b for b in page.get_text('blocks') if '图 IV-1' in b[4]]
assert len(blocks)==1
replace_region(page,(66,317,560,347),'图 IV-1｜旧版本2028条件情景图，不代表最新中性基准；完整新榜见任务四第15项核验。',9)
tmp=p.with_suffix('.body-alignment.tmp.pdf');doc.save(tmp,garbage=4,deflate=True);doc.close();tmp.replace(p)
changes.append({'path':str(p.relative_to(ROOT)),'before':before,'pages_updated':[11,17,18,21,22]})

# Keep submission PDFs within 20 pages; the two-page audit remains a separate file.
for p in [FINAL/'报告/百年圣火_正式报告.pdf',FINAL/'数说奥运_晓组织_正式答卷.pdf']:
    doc=pymupdf.open(p)
    assert len(doc)==22
    doc.delete_pages(0,1)
    tmp=p.with_suffix('.limit.tmp.pdf');doc.save(tmp,garbage=4,deflate=True);doc.close();tmp.replace(p)

(OUT/'正文同步记录.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'正文同步说明.md').write_text('''# 正式正文与最新研究对齐

2026-11-17：直接修改正式答卷DOCX的7处正文；报告PDF第3、11、13、14、20页，答卷PDF第11、17、18、21、22页分别按实际布局修改，不只依赖前置附页。

- 2028中性基准为主阅读；1120是比较条件；45%权重保留为情景，不称最优。
- 原RF/GB与独立岭回归分别解读；新基准不套用旧80%区间。
- 冠军结论采用固定小项队列；排除未决系列后的区间跨零。旧体育大类王朝图仅作描述。
- 主场平均关联与巴西反例分开，不作因果归因。
- 原预测图保留并就地标明旧版本情景，图上旧点值没有改写为新榜。

历史555项全项现行IOC核验仍未完成。未重画所有旧图，不能声称所有历史版本都已替换。

复现顺序：原模型复算 → publish_project_model_audit.py → align_final_research_body.py。重新生成正式材料后也须依次应用后两步；所有修改前版本按SHA256保存在项目工作区/outputs/report_revision_backups。
''',encoding='utf-8')
print('Aligned final bodies and labelled legacy figures.')
