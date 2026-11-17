"""Export three evidence-first figures from existing audited CSVs and publish them.
No model fitting. Run last, after other page/report generators.
"""
from pathlib import Path
import hashlib,json,os,re,shutil
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pymupdf

ROOT=Path(__file__).resolve().parents[2];D=ROOT/'交付文件';FINAL=D/'最终提交材料';OUT=FINAL/'核心证据图';OUT.mkdir(exist_ok=True)
S2=D/'任务三_专题深挖/S2_口径的魔力';S3=D/'任务三_专题深挖/S3_冠军的保质期';M=D/'任务四_开放创作/05_满分升级/15_原项目模型时序核验'
inputs=[S2/'02_数据表/S2_2024双口径完整排名.csv',S3/'11_历史来源敏感性/固定队列三方案复算.csv',M/'原模型五方案评分.csv']
ranks,cohorts,scores=[pd.read_csv(p) for p in inputs]
plt.rcParams.update({'font.sans-serif':['Microsoft YaHei','SimHei'],'axes.unicode_minus':False,'font.size':12,'pdf.fonttype':42})
ink='#183c46';teal='#227789';red='#a43d55';gold='#9a7331';paper='#faf8f2'
def frame(title,subtitle):
    fig,ax=plt.subplots(figsize=(11,6.3),facecolor=paper);ax.set_facecolor(paper)
    fig.subplots_adjust(left=.25,right=.93,top=.73,bottom=.26)
    fig.text(.06,.92,title,fontsize=21,color=ink,weight='bold')
    fig.text(.06,.84,subtitle,fontsize=11,color=ink)
    for sp in ax.spines.values():sp.set_visible(False)
    ax.tick_params(length=0,labelcolor=ink)
    return fig,ax
figures=[];records=[]
fig,ax=frame('同样按金银铜排序，换统计单位就会换名次','巴黎2024｜三个有代表性的口径变化案例；不是实力变化，也不是连续变化过程')
for i,(noc,label) in enumerate([('ESP','西班牙'),('NED','荷兰'),('JPN','日本')]):
    row=ranks[ranks.NOC.eq(noc)].iloc[0];a=int(row.official_rank);b=int(row.row_rank)
    ax.plot([0,1],[i,i],color='#b6c6c5',lw=2)
    ax.scatter([0,1],[i,i],s=750,c=[teal,red],zorder=3)
    ax.text(0,i,str(a),ha='center',va='center',color='white',weight='bold',fontsize=17)
    ax.text(1,i,str(b),ha='center',va='center',color='white',weight='bold',fontsize=17)
    ax.text(.5,i-.17,f'{int(row.Gold_official)}个金牌小项  /  {int(row.Gold_rows)}条金牌记录',ha='center',fontsize=11,color=ink)
    records.append({'代表团':label,'官方小项名次':a,'运动员行名次':b})
ax.set_yticks([0,1,2],['西班牙','荷兰','日本']);ax.set_ylim(2.5,-.6);ax.set_xlim(-.25,1.25);ax.set_xticks([0,1],['官方小项口径 · 名次','运动员行口径 · 名次']);ax.xaxis.tick_top()
assert records[0]['官方小项名次']==15 and records[0]['运动员行名次']==5
fig.text(.06,.10,'来源：S2_2024双口径完整排名.csv；两端采用相同金银铜排序，并排除AIN。',fontsize=10,color=ink)
fig.text(.06,.055,'读数边界：名次为两套完整榜中的位置；连接线只配对同一代表团，线长不编码名次差。',fontsize=10,color=ink)
figures.append(('01_统计单位与名次',fig))

fig,ax=frame('排除未决系列后，下降的区间跨过了零','小项金牌控制权｜后段1996—2016减早段1964—1976；误差线为小项成组95%区间')
for i,(_,r) in enumerate(cohorts.head(3).iterrows()):
    x=r['后减前百分点'];lo=r['区间下限'];hi=r['区间上限'];color=teal if i<2 else red
    ax.errorbar(x,i,xerr=[[x-lo],[hi-x]],fmt='o',color=color,capsize=5,lw=2.5,ms=8)
    ax.text(-17.5,i+.26,f'{x:.2f}  [{lo:.2f}, {hi:.2f}]',color=color,fontsize=11)
ax.axvline(0,color=ink,ls='--',lw=1);ax.set_xlim(-18,4);ax.set_ylim(2.65,-.6)
ax.set_yticks([0,1,2],['原代理 · 113项','二次来源替换 · 同113项','排除未决系列 · 50项']);ax.set_xlabel('卫冕率差值（百分点）；负值表示后段较低')
fig.text(.06,.10,'来源：固定队列三方案复算.csv；小项成组重抽样10,000次，种子42。',fontsize=10,color=ink)
fig.text(.06,.055,'边界：子队列变化含样本选择；二次来源及排除子集不等于现行IOC认证，也非因果检验。',fontsize=10,color=ink)
figures.append(('02_固定队列与排除敏感性',fig))

fig,ax=frame('项目模型有局部收益，但没有稳定胜过基准','原RF/GB参数冻结｜小项二次来源情景；全体代表团MAE，越低越好；同折采用相同评分池')
q=scores[scores.来源.eq('小项二次来源')&scores.选择规则.eq('仅此前届次')]
years=[2012,2016,2024];x=np.arange(3)
for k,(model,label,color) in enumerate([('历史加权基线','历史加权基准',teal),('RF60_GB40','RF60%＋GB40%',red),('55基线45项目','基准55%＋项目45%',gold)]):
    vals=q[q.模型.eq(model)].set_index('Year').loc[years].MAE.to_numpy()
    bars=ax.bar(x+(k-1)*.24,vals,.22,color=color,label=label)
    for b,v in zip(bars,vals):ax.text(b.get_x()+b.get_width()/2,v+.025,f'{v:.3f}',ha='center',fontsize=10,color=ink)
ax.set_ylim(0,2.6);ax.set_xticks(x,['2012','2016','2024']);ax.set_ylabel('MAE（小项奖牌槽/代表团）');ax.legend(frameon=False,loc='upper left',fontsize=10);ax.grid(axis='y',alpha=.12);ax.set_axisbelow(True)
fig.text(.06,.10,'来源：原模型五方案评分.csv；仅此前届次训练与候选筛选，参数不按本轮目标分数调整。',fontsize=10,color=ink)
fig.text(.06,.055,'边界：2024最近可用小项特征为2016，间隔八年；事后整理资料不等于真实赛前冻结快照。',fontsize=10,color=ink)
figures.append(('03_原模型与同口径基准',fig))
with PdfPages(OUT/'三张核心证据图.pdf') as pdf:
    for name,fig in figures:
        fig.savefig(OUT/(name+'.png'),dpi=180);fig.savefig(OUT/(name+'.pdf'));pdf.savefig(fig);plt.close(fig)
pd.DataFrame(records).to_csv(OUT/'口径名次读数.csv',index=False,encoding='utf-8-sig')
# Publish beside each relevant argument, with a readable caption and full-size link.
targets=[(S2/'09_奖牌口径实验室/index.html',0),(S3/'11_历史来源敏感性/index.html',1),(M/'index.html',2)]
titles=['同一排序规则下的统计单位对照','固定队列与排除子队列的区间比较','原RF/GB与同口径基准逐折比较']
for p,i in targets:
    t=p.read_text(encoding='utf-8');t=re.sub(r'<!-- EVIDENCE_FIGURE_START -->.*?<!-- EVIDENCE_FIGURE_END -->','',t,flags=re.S)
    rel=Path(os.path.relpath(OUT,p.parent)).as_posix();name=figures[i][0]
    block=f'<!-- EVIDENCE_FIGURE_START --><figure style="max-width:1100px;margin:2rem auto;padding:0 16px;box-sizing:border-box"><img src="{rel}/{name}.png" alt="{titles[i]}，数值、来源和限制均在图中" style="display:block;width:100%;height:auto"><figcaption>{titles[i]}。<a href="{rel}/{name}.pdf">打开矢量PDF放大阅读</a> · <a href="{rel}/三张核心证据图.pdf">三图证据册</a></figcaption></figure><!-- EVIDENCE_FIGURE_END -->'
    t=t.replace('</body>',block+'</body>');p.write_text(t,encoding='utf-8')
# Replace only the three corresponding raster images in the 20-page formal report.
p=FINAL/'报告/百年圣火_正式报告.pdf';backup=ROOT/'项目工作区/outputs/report_revision_backups';backup.mkdir(exist_ok=True)
digest=hashlib.sha256(p.read_bytes()).hexdigest();bak=backup/(p.stem+'_before_evidence_figures_'+digest[:10]+'.pdf')
if not bak.exists():shutil.copy2(p,bak)
doc=pymupdf.open(p);assert len(doc)==20
for pageid,i in [(1,0),(8,1),(11,2)]:
    pg=doc[pageid];images=pg.get_images();assert len(images)==1
    rect=pg.get_image_rects(images[0][0])[0]
    pg.add_redact_annot(rect,fill=False);pg.apply_redactions(images=2,graphics=0,text=1)
    pg.insert_image(rect,filename=str(OUT/(figures[i][0]+'.png')),keep_proportion=True)
tmp=p.with_suffix('.figures.tmp.pdf');doc.save(tmp,garbage=4,deflate=True);doc.close();tmp.replace(p)
(OUT/'来源与发布记录.json').write_text(json.dumps({'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs},'report_pages':[2,9,12],'report_page_count':20,'data_refitted':False,'regenerate':'polish_evidence_figures.py应最后运行，其他生成器会覆盖图形发布'},ensure_ascii=False,indent=2),encoding='utf-8')
print('Published three evidence figures and refreshed three formal-report images.')
