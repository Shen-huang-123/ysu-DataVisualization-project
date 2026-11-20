"""Publish the original RF/GB audit, reading policy and latest delivery notice."""
from pathlib import Path
import os,re,json,hashlib,shutil,tempfile
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pymupdf
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from docx import Document
from docx.oxml import OxmlElement
from task2_localization import NOC_ZH

ROOT=Path(__file__).resolve().parents[2];T4=ROOT/'交付文件/任务四_开放创作';OUT=T4/'05_满分升级/15_原项目模型时序核验';FINAL=ROOT/'交付文件/最终提交材料'
s=pd.read_csv(OUT/'原模型五方案评分.csv');a=pd.read_csv(OUT/'逐折选择与训练边界.csv');forecast=pd.read_csv(OUT/'2028同口径重训情景榜.csv');strict=s[s.选择规则.eq('仅此前届次')]
title='原RF/GB有局部收益，但45%权重尚无稳定依据'
intro='保留原随机森林280棵、梯度提升220棵及60/40组合，重跑三种口径、三个留出届次。运动员行口径下，55/45混合的全体MAE三折均小幅改善；小项口径下表现不稳定，2024均略差。不同单位的误差不能横比。'
selection='正式模型的全时期筛选会把2024的AIN和霹雳舞提前纳入；严格历史筛选则是KUW而非AIN，且不含霹雳舞。仅在2024运动员行诊断中，含目标届筛选的混合MAE为3.961，严格筛选为3.978，存在约0.017行/队的乐观差异。这不是独立因果估计；旧滚动回放本来已按此前数据筛选，不能把所有旧回测都称为相同泄漏。'
policy='主阅读使用中性历史加权基准；RF/GB及55/45混合保留为条件情景，不把45%称为最优或经稳定验证的权重，也不在看过这三折后重新搜索一个“最好”的权重。新增运动、主场和资格仍单列情景。最新2028核心已用截至2024数据重训，但并非原完整集成的同构历史验证。'
boundary='历史小项是同Year、Sport、Event、Medal、NOC去重的奖牌槽代理，同NOC同色多枚可能合并；2024目标来自既有逐项表。全部45个discipline按预设结构映射至运动家族，未依评分调映射。不能可靠匹配的2020小项未进入小项训练；2024小项回放最近奖牌特征为2016，间隔八年。运动员行分支可使用2020，须分开解读。'
temporal='每折仅用目标前数据选100个代表团及最多45个运动家族，目标届标签在特征面板中强制置零，仅在评分阶段读取。2012只有2008一个训练届次，样本不足以另做可靠内层调参，所以冻结原参数。历史数据仍是事后整理修订版；没有取得逐届真实赛前冻结快照，严格年份切分不等于真实时点验证。'
coverage='未进入历史特征的项目仍计入实际评分：2016的高尔夫、七人制橄榄球；2024小项分支的霹雳舞、滑板、攀岩和冲浪。2024已建模格覆盖实际小项槽约93.97%，其余没有被删除。所有模型采用相同候选与评分池、相同事前估计总池，并公开零奖牌队与实际至少5单位子集；不得与旧132队评分直接横比。'
outlook='2028新榜沿用既有1120总量作为比较条件，不保证最终官方规模；主阅读无额外主场、排名或资格加成。最近两次可用小项奖牌数据是2024与2016，时间不等距。榜中不附未经校准的80%区间，不将旧集成区间套到新模型。二次来源不是现行IOC逐项核验，555项全项认证缺口没有因此消失。'

plt.rcParams.update({'font.sans-serif':['Microsoft YaHei','SimHei'],'axes.unicode_minus':False})
z=strict[strict.来源.eq('小项二次来源')];models=['历史加权基线','RF60_GB40','55基线45项目']
fig,ax=plt.subplots(figsize=(10,4.6),facecolor='#f7f3eb');ax.set_facecolor('#f7f3eb');x=np.arange(3)
for i,(model,color) in enumerate(zip(models,['#247487','#a64155','#b88c43'])):
    values=z[z.模型.eq(model)].sort_values('Year').MAE.to_numpy();bars=ax.bar(x+(i-1)*.24,values,.22,label=model,color=color)
    for b,v in zip(bars,values):ax.text(b.get_x()+b.get_width()/2,v+.025,f'{v:.3f}',ha='center',fontsize=10)
ax.set_xticks(x,['2012','2016','2024\n最近小项特征：2016']);ax.set_ylim(0,2.6);ax.set_ylabel('MAE（小项奖牌槽/代表团；越低越好）');ax.set_title('原RF/GB同口径重训：混合有时改善，2024仍略差',loc='left',fontsize=14,pad=16);ax.legend(ncol=3,frameon=False,loc='upper left');ax.spines[['top','right']].set_visible(False);fig.tight_layout();fig.savefig(OUT/'原项目模型同口径核验.png',dpi=160);plt.close(fig)

def summary_table(source):
    q=strict[strict.来源.eq(source)].pivot(index='Year',columns='模型',values='MAE')
    return '<table><caption>'+source+' · 全体MAE（仅在同单位内比较）</caption><thead><tr><th>届次</th><th>历史基线</th><th>RF/GB</th><th>55/45混合</th></tr></thead><tbody>'+''.join('<tr><th>'+str(y)+'</th>'+''.join(f'<td>{q.loc[y,m]:.3f}</td>' for m in models)+'</tr>' for y in q.index)+'</tbody></table>'
css='''<style>.project-audit{font-family:inherit;max-width:1100px;margin:3rem auto;padding:clamp(18px,3vw,36px);box-sizing:border-box;border-block:1px solid #87979566;line-height:1.85}.project-audit h2{font-size:clamp(22px,3vw,32px);line-height:1.4}.project-audit img{display:block;width:100%;height:auto;margin:24px 0}.project-audit table{width:100%;border-collapse:collapse;font-size:clamp(12px,1.2vw,16px);margin-block:20px}.project-audit th,.project-audit td{text-align:left;padding:10px 4px;border-bottom:1px solid #87979566}.project-audit caption{text-align:left}.project-audit summary{cursor:pointer;font-weight:600}.project-audit a{overflow-wrap:anywhere}.project-audit select{font:inherit;color:inherit;background:transparent;border:1px solid #87979599;padding:8px 12px;max-width:100%}.project-audit option{color:#172a30;background:#f7f3eb}</style>'''
def audit_block(parent):
    rel=Path(os.path.relpath(OUT,parent)).as_posix()
    return '<!-- PROJECT_MODEL_START -->'+css+f'<section id="project-model-audit" class="project-audit"><h2>{title}</h2><p>{intro}</p><img loading="lazy" src="{rel}/原项目模型同口径核验.png" alt="小项二次来源情景的历史基线、RF/GB和55/45混合逐折MAE">'+summary_table('小项二次来源')+f'<details><summary>看运动员行与原代理：换口径后是否同样成立？</summary>'+summary_table('运动员行原口径')+summary_table('小项原代理')+f'<p>{coverage}</p></details><details><summary>看前视风险、训练时间与证据边界</summary><p>{selection}</p><p>{temporal}</p><p>{boundary}</p></details><h3>据此调整正式阅读方式</h3><p>{policy}</p><p>{outlook}</p><p><a href="{rel}/原模型五方案评分.csv" download>50行完整评分</a> · <a href="{rel}/原模型逐队误差.csv" download>逐队误差</a> · <a href="{rel}/原项目模型核验说明.md">方法与限制</a> · <a href="{rel}/原项目模型复核_最新交付附页.pdf">PDF核验附页</a></p></section><!-- PROJECT_MODEL_END -->'

def reading_block(parent):
    rel=Path(os.path.relpath(OUT,parent)).as_posix()
    # Plain indexing avoids namedtuple mangling of columns beginning with digits.
    rows=''.join(f'<tr><td>{int(r["主阅读基准名次"])}</td><th>{NOC_ZH.get(r["NOC"],r["NOC"])}</th><td>{r["历史加权基线"]:.1f}</td><td>{r["55基线45项目"]:.1f}</td></tr>' for _,r in forecast.head(10).iterrows())
    return '<!-- PROJECT_READING_START -->'+css+f'<section id="project-reading-policy" class="project-audit"><h2>2028主阅读：先看中性基准，再比较模型情景</h2><p>{policy}</p><p>{outlook}</p><details open><summary>最新重训基准前十与45%项目情景</summary><table><caption>条件总池1120；未加主场、排名或资格调整。按基准总量排序。</caption><thead><tr><th>序</th><th>代表团</th><th>中性基准</th><th>55/45情景</th></tr></thead><tbody>{rows}</tbody></table></details><p><a href="{rel}/2028同口径重训情景榜.csv" download>下载最新完整参考榜</a> · <a href="{rel}/index.html">原模型逐折核验</a></p><p><small>本页其他旧榜、排名门控和区间控件保留为既有条件情景；其点值和区间不能套用到本次新基准。</small></p></section><!-- PROJECT_READING_END -->'

paths=[T4/'01_交互式Dashboard/index.html',T4/'index.html',T4/'02_2028洛杉矶预测/index.html',T4/'03_数据新闻/index.html',T4/'05_满分升级/09_赛前条件回放/index.html',T4/'05_满分升级/11_官方来源门控预测/index.html',T4/'09_预测风暴实验室/index.html']
for p in paths:
    text=p.read_text(encoding='utf-8')
    for tag in ['PROJECT_MODEL','PROJECT_READING']:text=re.sub(f'<!-- {tag}_START -->.*?<!-- {tag}_END -->','',text,flags=re.S)
    # Put the policy before analytical content; preserve navigation/hero and existing controls.
    if '<main' in text:
        text=re.sub(r'(<main\b[^>]*>)',lambda m:m.group(1)+reading_block(p.parent),text,count=1)
    else:text=re.sub(r'(<body\b[^>]*>)',lambda m:m.group(1)+reading_block(p.parent),text,count=1)
    text=re.sub('</body>',lambda _:audit_block(p.parent)+'\n</body>',text,count=1,flags=re.I);p.write_text(text,encoding='utf-8')
(OUT/'index.html').write_text('<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>原RF/GB项目模型核验</title></head><body style="margin:0;background:#f7f3eb;color:#172a30;font-family:Microsoft YaHei,sans-serif">'+audit_block(OUT)+reading_block(OUT)+'</body></html>',encoding='utf-8')

md='# '+title+'\n\n'+intro+'\n\n## 具体的前视风险\n\n'+selection+'\n\n## 冻结协议与时间边界\n\n'+temporal+'\n\n'+boundary+'\n\n'+coverage+'\n\n## 主阅读决策\n\n'+policy+'\n\n'+outlook+'\n\n## 完整逐折评分\n\n'+s.to_markdown(index=False)+'\n\n## 每折数据覆盖\n\n'+a.drop(columns=['特征哈希','耗时秒']).to_markdown(index=False)+'\n\n## 复现\n\n`py 项目工作区/scripts/project_model_strict_replay.py`，再运行 `py 项目工作区/scripts/publish_project_model_audit.py`。原参数冻结，不使用本轮目标分数调参；可用训练届次过少，不宣称已充分识别超参数或最优混合权重。本报告是事后时序复算，非独立前瞻验证。所有原始输入与旧榜保留，另发2028重训核心对照榜；没有伪造2028实际成绩或校准区间。\n'
(OUT/'原项目模型核验说明.md').write_text(md,encoding='utf-8')
append='\n\n<!-- PROJECT_MODEL_START -->\n## 2026-11-17：原RF/GB项目模型重跑与阅读决策\n\n'+intro+'\n\n'+selection+'\n\n'+policy+'\n\n'+outlook+'\n\n'+coverage+'\n\n详见任务四/05_满分升级/15_原项目模型时序核验；复算 project_model_strict_replay.py，发布 publish_project_model_audit.py。独立岭回归的失败不能外推为原RF/GB完全无效；原RF/GB的运动员行改善也不能外推成官方奖牌预测稳定改进。\n<!-- PROJECT_MODEL_END -->\n'
for p in [T4/'02_2028洛杉矶预测/预测方法与验证方案.md',ROOT/'交付文件/证据边界核验进度.md',ROOT/'项目交接_请新AI先读.md']:
    text=p.read_text(encoding='utf-8');text=re.sub(r'\n*<!-- PROJECT_MODEL_START -->.*?<!-- PROJECT_MODEL_END -->\n*','',text,flags=re.S);p.write_text(text+append,encoding='utf-8')

# Two current pages lead the final PDFs, so the dated update is read before legacy results.
pdfmetrics.registerFont(TTFont('ProjectCN',r'C:\Windows\Fonts\simhei.ttf'))
pdf=OUT/'原项目模型复核_最新交付附页.pdf';c=canvas.Canvas(str(pdf),pagesize=A4);w,h=A4
MARKER='原项目模型复核 / 2026-11-17'
def page(title,num):
    c.setFillColorRGB(.969,.953,.922);c.rect(0,0,w,h,fill=1,stroke=0);c.setFillColorRGB(.09,.16,.19);c.setFont('ProjectCN',9);c.drawString(35,h-30,MARKER);c.setFont('ProjectCN',20);c.drawString(35,h-65,title);c.setFont('ProjectCN',8);c.drawString(35,24,f'最新核验说明 · {num}/2 · 本附页优先于旧版预测能力表述')
def para(text,y,size=10):
    c.setFont('ProjectCN',size);line=''
    for ch in text:
        if pdfmetrics.stringWidth(line+ch,'ProjectCN',size)>w-70:c.drawString(35,y,line);y-=18;line=ch
        else:line+=ch
    if line:c.drawString(35,y,line);y-=18
    assert y>42,('PDF overflow',y)
    return y-10
page('原模型有局部收益，尚不足以确认45%权重',1);y=para(intro,h-100)
im=ImageReader(str(OUT/'原项目模型同口径核验.png'));iw,ih=im.getSize();hh=(w-70)*ih/iw;c.drawImage(im,35,y-hh,w-70,hh);y-=hh+25
y=para(selection,y);y=para(policy,y);para(outlook,y);c.showPage()
page('研究闭环更新与证据边界',2);y=para(temporal,h-100);y=para(boundary,y);y=para(coverage,y)
y=para('冠军延续：同113项替换二次来源后仍下降7.37个百分点，区间[-13.20,-1.62]；排除未决系列后剩50项，区间[-16.17,+1.50]跨零，不能称排除检验也确认下降。',y)
y=para('主场：原17个运动员行案例复现；另建小项三情景，同15个案例的平均关联仍为正。巴西2016原五队匹配+0.13个百分点，但小项合成对照原代理-0.11、替换后-0.17；单位与方法同时改变，不能分离归因或宣称普遍获益。',y)
para('最终材料阅读规则：2024口径分析是主要证据；历史三届555项尚未全项完成现行IOC核验。本轮未修订全部旧图、旧排名与原集成区间，均按原版本情景阅读。海报已检查，仍围绕2024西班牙口径差异，无本轮模型能力或2028精确点值，不需改图。完整复算与逐队数据见任务四/05_满分升级/15_原项目模型时序核验。',y);c.showPage();c.save()

backup=ROOT/'项目工作区/outputs/report_revision_backups';backup.mkdir(exist_ok=True)
changes=[]
for p in [FINAL/'报告/百年圣火_正式报告.pdf',FINAL/'数说奥运_晓组织_正式答卷.pdf']:
    before=hashlib.sha256(p.read_bytes()).hexdigest();bak=backup/(p.stem+'_before_project_audit_'+before[:10]+'.pdf')
    src=pymupdf.open(p)
    if MARKER not in src[0].get_text() and not bak.exists():shutil.copy2(p,bak)
    first=2 if MARKER in src[0].get_text() else 0
    new=pymupdf.open();new.insert_pdf(src,from_page=first);new.set_metadata(src.metadata)
    tmp=p.with_name(p.stem+'.project-audit.tmp.pdf');new.save(tmp,garbage=4,deflate=True);new.close();src.close();tmp.replace(p)
    changes.append(dict(path=str(p.relative_to(ROOT)),before=before,after=hashlib.sha256(p.read_bytes()).hexdigest(),method='前置两页最新核验；原有正文保留；重跑替换不叠加'))

p=FINAL/'数说奥运_晓组织_正式答卷.docx';before=hashlib.sha256(p.read_bytes()).hexdigest();doc=Document(p);start='最新核验｜原项目模型复核 2026-11-17';end='【最新核验说明结束】'
paras=doc.paragraphs;found=False
for para0 in paras:
    if para0.text==start:found=True
    if found:
        finish=para0.text==end;el=para0._element;el.getparent().remove(el)
        if finish:break
if start not in '\n'.join(x.text for x in Document(p).paragraphs):
    bak=backup/(p.stem+'_before_project_audit_'+before[:10]+'.docx')
    if not bak.exists():shutil.copy2(p,bak)
first=doc.paragraphs[0]
for text in [start,intro,selection,policy,outlook,'研究更新：S3排除未决系列后的50项区间跨零；主场巴西反例依赖口径与方法。555项全项现行IOC认证尚未完成。最新前端与PDF附页提供完整数据。',end]:first.insert_paragraph_before(text)
doc.save(p);changes.append(dict(path=str(p.relative_to(ROOT)),before=before,after=hashlib.sha256(p.read_bytes()).hexdigest(),method='前置最新核验正文，旧内容按版本保留'))

# Make the formal-material entrance point at the latest results as well.
p=FINAL/'00_先看这里.html';text=p.read_text(encoding='utf-8');text=re.sub(r'<!-- PROJECT_FINAL_START -->.*?<!-- PROJECT_FINAL_END -->','',text,flags=re.S)
rel=Path(os.path.relpath(OUT,p.parent)).as_posix();notice=f'<!-- PROJECT_FINAL_START --><aside style="max-width:1100px;margin:2rem auto;padding:24px;border-block:1px solid #87979566;line-height:1.8"><h2>2026-11-17 最新模型核验</h2><p>{policy}</p><p>正式报告与答卷PDF正文已同步；两页核验独立保存，DOCX含最新说明；海报维持2024口径主线。<a href="{rel}/index.html">查看原RF/GB逐折结果与重训参考榜</a></p></aside><!-- PROJECT_FINAL_END -->'
text=text.replace('</body>',notice+'</body>');p.write_text(text,encoding='utf-8')
(OUT/'最终交付同步记录.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2),encoding='utf-8')
p=ROOT/'README.md';text=p.read_text(encoding='utf-8');line='\n- [原RF/GB项目模型时序核验](交付文件/任务四_开放创作/05_满分升级/15_原项目模型时序核验/index.html)：原参数三口径复算、2028同口径重训核心及正式材料最新附页。中性基准为主阅读，45%项目权重保留为情景。\n'
if '原RF/GB项目模型时序核验](' not in text:p.write_text(text+line,encoding='utf-8')
print('Published original model audit, latest 2028 core and final PDF/DOCX notices.')

# Restore the current-first reading hierarchy after rebuilding policy blocks.
import runpy
runpy.run_path(str(ROOT/'项目工作区/scripts/organize_forecast_reading.py'),run_name='__main__')

# Reapply reviewed web presentation after regenerating audit blocks.
import runpy
runpy.run_path(str(Path(__file__).with_name("publish_project_chart_style.py")))

# Preserve conclusion-adjacent evidence notes after regeneration.
from publish_evidence_closure import main as publish_closure_notes
publish_closure_notes()
