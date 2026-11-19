"""Render the host sensitivity evidence and integrate it without changing existing controls."""
from pathlib import Path
import os,re,json,hashlib
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader

ROOT=Path(__file__).resolve().parents[2];T3=ROOT/'交付文件/任务三_专题深挖';BASE=T3/'S1_东道主效应';OUT=BASE/'01_来源与口径敏感性'
s=pd.read_csv(OUT/'三方案共同案例摘要.csv');r=pd.read_csv(OUT/'三方案逐主办案例.csv')
headline='平均主场关联保持为正，巴西反例随口径与方法改变'
intro='15个共同历史主办案例中，小项原代理平均差值为+3.02个百分点，二次来源替换后为+3.01；排除未决同名系列后为+2.87。对应成组95%区间均在零以上。这是样本内关联，不能证明主办的因果收益。'
counter='巴西2016：原“五队匹配、运动员行”比较为+0.13个百分点；小项合成对照原代理为−0.11，替换后为−0.17，排除后为−1.22。统计单位与比较方法同时变化，不能拆分归因；“巴西仍有相对优势”仅适用于原来的特定比较。英国2012在排除情景也由正转负，不能以平均值替每个案例背书。'
method='原运动员行合成对照17个案例已逐例复现，最大误差小于0.00001个百分点。另建1948—2016的小项代理，三方案共同15案；原模型17案与新模型15案不可直接作增减比较。555项记录不包含个人名单，因此没有据此重分配运动员奖牌。'
boundary='B仅替换555项的奖牌代表团；C在所有历史年份剔除相关209条同名小项系列，运动构成明显改变，不能称为纠偏后的真值。各案例固定原小项情景的对照池，分别重拟合权重；参赛行特征保持不变。小项代理同NOC同色多枚可能合并，二次来源及剩余子集均非现行IOC逐项认证。图中区间按主办案例重抽样；另按13个主办代表团整簇重抽样，三方案区间也均为正（详见CSV）。两者均不消除选择、抵制、身份与规则混杂。'

plt.rcParams.update({'font.sans-serif':['Microsoft YaHei','SimHei'],'axes.unicode_minus':False})
fig,ax=plt.subplots(figsize=(10,4.3),facecolor='#f7f3eb');ax.set_facecolor('#f7f3eb')
for i,z in enumerate(s.itertuples()):
    x=z.平均差值;lo=z.区间下限;hi=z.区间上限
    ax.errorbar(x,2-i,xerr=[[x-lo],[hi-x]],fmt='o',color=['#247487','#247487','#a64155'][i],capsize=5,lw=2)
    ax.text(5.6,2-i,f'{x:+.2f}  [{lo:+.2f}, {hi:+.2f}]',va='center',fontsize=10)
ax.axvline(0,ls='--',lw=1,color='#68777d');ax.set_xlim(-.3,9.4);ax.set_ylim(-.6,2.8)
ax.set_yticks([2,1,0],['小项原代理','二次来源替换','排除未决同名系列'])
ax.set_xlabel('主办届减合成对照（百分点）；横线为案例成组95%区间')
ax.set_title('同15个主办案例：平均关联为正，不代表每届都受益',loc='left',fontsize=14,pad=18)
for spine in ax.spines.values():spine.set_visible(False)
ax.tick_params(length=0);fig.tight_layout();fig.savefig(OUT/'主场来源敏感性.png',dpi=160);plt.close(fig)

def table():
    names={2008:'中国2008',2012:'英国2012',2016:'巴西2016'}
    a=r.pivot(index='host_year',columns='方案',values='gap_pp')
    return '<table><caption>逐案例合成对照差值，单位：百分点</caption><thead><tr><th>案例</th><th>小项原代理</th><th>二次来源</th><th>排除系列</th></tr></thead><tbody>'+''.join(f'<tr><th>{names[y]}</th>'+''.join(f'<td>{a.loc[y,n]:+.2f}</td>' for n in ['小项原代理','小项二次来源替换','排除未决同名系列'])+'</tr>' for y in names)+'</tbody></table>'
style='''<style>#host-source-sensitivity{width:auto;max-width:none;margin:2rem clamp(24px,6vw,100px);padding:clamp(24px,3vw,40px) 0;box-sizing:border-box;border-block:1px solid #87999866;font-family:inherit;line-height:1.85}#host-source-sensitivity :is(h2,h3,p){max-width:none!important;width:100%;box-sizing:border-box}#host-source-sensitivity h2{font-size:clamp(22px,3vw,32px);line-height:1.4}#host-source-sensitivity img{display:block;width:100%;max-width:none!important;height:auto;margin:24px 0}#host-source-sensitivity table{width:100%;border-collapse:collapse;font-size:clamp(12px,1.2vw,16px)}#host-source-sensitivity th,#host-source-sensitivity td{padding:10px 4px;text-align:left;border-bottom:1px solid #87999866}#host-source-sensitivity caption{text-align:left}#host-source-sensitivity summary{cursor:pointer;font-weight:600}#host-source-sensitivity a{overflow-wrap:anywhere}</style>'''
def block(parent):
    rel=Path(os.path.relpath(OUT,parent)).as_posix()
    return '<!-- HOST_SOURCE_START -->'+style+f'<section id="host-source-sensitivity"><h2>{headline}</h2><p>{intro}</p><img loading="lazy" src="{rel}/主场来源敏感性.png" alt="同15个主办案例三情景的平均差值与区间均为正"><h3>反例：巴西的“相对优势”取决于怎么比较</h3><p>{counter}</p>'+table()+f'<details><summary>为什么这不是原模型的“官方修正版”？</summary><p>{method}</p><p>{boundary}</p></details><p><a href="{rel}/三方案逐主办案例.csv" download>下载逐案例结果</a> · <a href="{rel}/主场来源与口径敏感性说明.md">方法与输入记录</a> · <a href="{rel}/主场来源与口径敏感性补充报告.pdf">PDF补充报告</a></p></section><!-- HOST_SOURCE_END -->'

paths=[BASE/'index.html',BASE/'S1东道主分析.html',ROOT/'交付文件/任务二_百年全景/05_交互总览/index.html',T3/'统一中文入口/index.html']
for p in paths:
    text=p.read_text(encoding='utf-8');text=re.sub(r'<!-- HOST_SOURCE_START -->.*?<!-- HOST_SOURCE_END -->','',text,flags=re.S)
    assert '</body>' in text.lower()
    text=re.sub('</body>',lambda _:block(p.parent)+'\n</body>',text,count=1,flags=re.I);p.write_text(text,encoding='utf-8')
(OUT/'index.html').write_text('<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>主场来源与口径敏感性</title></head><body style="margin:0;background:#f7f3eb;color:#172a30;font-family:Microsoft YaHei,sans-serif">'+block(OUT)+'</body></html>',encoding='utf-8')

md='\n\n<!-- HOST_SOURCE_START -->\n## 2026-11-17：主场来源与口径敏感性\n\n'+intro+'\n\n'+counter+'\n\n'+method+'\n\n'+boundary+'\n\n数据与方法：S1_东道主效应/01_来源与口径敏感性；复现脚本 `host_source_sensitivity.py`，页面集成与补充PDF脚本 `integrate_host_sensitivity.py`。2028尚未在本轮重训。\n<!-- HOST_SOURCE_END -->\n'
for p in [BASE/'S1东道主分析.md',T3/'三篇旗舰专题_研究闭环.md',T3/'十专题深度核验.md',ROOT/'交付文件/证据边界核验进度.md',ROOT/'项目交接_请新AI先读.md']:
    text=p.read_text(encoding='utf-8');text=re.sub(r'\n*<!-- HOST_SOURCE_START -->.*?<!-- HOST_SOURCE_END -->\n*','',text,flags=re.S);p.write_text(text+md,encoding='utf-8')

# Supplement preserves provenance of old figures rather than rewriting their units.
pdfmetrics.registerFont(TTFont('HostCN',r'C:\Windows\Fonts\simhei.ttf'))
pdf=OUT/'主场来源与口径敏感性补充报告.pdf';c=canvas.Canvas(str(pdf),pagesize=A4);w,h=A4
def page(title,num):
    c.setFillColorRGB(.969,.953,.922);c.rect(0,0,w,h,fill=1,stroke=0);c.setFillColorRGB(.09,.16,.19);c.setFont('HostCN',20);c.drawString(35,h-55,title);c.setFont('HostCN',9);c.drawString(35,25,f'2026-11-17 · 主场来源与口径敏感性 · {num}/2')
def paragraph(text,y):
    line='';c.setFont('HostCN',11)
    for ch in text:
        if pdfmetrics.stringWidth(line+ch,'HostCN',11)>w-70:
            c.drawString(35,y,line);y-=20;line=ch
        else:line+=ch
    if line:c.drawString(35,y,line);y-=20
    return y-14
page('平均关联仍在，个案必须限定方法',1);y=paragraph(intro,h-100)
im=ImageReader(str(OUT/'主场来源敏感性.png'));iw,ih=im.getSize();height=(w-70)*ih/iw;c.drawImage(im,35,y-height,w-70,height);y-=height+30
y=paragraph(counter,y);paragraph(method,y);c.showPage()
page('完整方法与证据边界',2);y=paragraph(boundary,h-100)
y=paragraph('95%区间：固定15个共同主办案例，重抽样10000次，种子42。前三期用于拟合，各案例固定对照池，权重非负且和为1。对照池排除观察窗口内的主办代表团。优化目标保持旧模型；有限差分不收敛时使用同目标的解析梯度与正比例缩放。',y)
y=paragraph('补充结果：',y)
for z in r[r.host_year.isin([2008,2012,2016])].itertuples():y=paragraph(f'{z.host_year} {z.host_NOC} · {z.方案}：差值{z.gap_pp:+.3f}，前拟合RMSPE={z.pre_rmspe:.3f}个百分点。',y)
paragraph('完整CSV、对照权重、逐届小项覆盖、输入SHA256与复现脚本随项目交付。原始输入与既有主场图未覆盖；本补充不等于完成现行IOC核验，也未更新2028训练管线。',y);c.showPage();c.save()

# Supersede the earlier global statement in generated pages and its generator.
old='主场运动员行与2028预测尚未在本轮重新估计，其各自边界继续保留。'
new='主场运动员行17案已复现，另建小项三情景对照：平均关联为正，巴西个案依方法改变。2028预测尚未在本轮重训。'
for p in [*list((ROOT/'交付文件').rglob('index.html')),ROOT/'项目工作区/scripts/integrate_evidence_sensitivity.py']:
    text=p.read_text(encoding='utf-8')
    if old in text:p.write_text(text.replace(old,new),encoding='utf-8')
p=ROOT/'README.md';text=p.read_text(encoding='utf-8');line='\n- [主场来源与口径敏感性](交付文件/任务三_专题深挖/S1_东道主效应/01_来源与口径敏感性/index.html)：原17案复现与小项15案三情景；巴西反例限定比较方法。\n'
if '主场来源与口径敏感性](交付文件' not in text:p.write_text(text+line,encoding='utf-8')
print('Integrated host evidence:',len(paths),'existing pages; standalone and two-page PDF supplement.')

# Refresh the complete web reading edition after material updates.
import runpy
runpy.run_path(str(Path(__file__).with_name("publish_flagship_reading.py")))
