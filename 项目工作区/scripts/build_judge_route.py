"""Publish a five-minute evidence route using the established document shell."""
from pathlib import Path
from html import escape
import re,json
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[2];BASE=ROOT/'交付文件/最终提交材料'
steps=[
dict(title='同一届奥运，为什么有两个名次？',time='0:00—1:00',question='西班牙15→5，是规则变了，还是我们数的东西变了？',action='打开奖牌口径实验室，在小项与运动员行两个端点间切换。中间权重只演示压力测试。',claim='同样按金银铜排序，统计单位改变名次；5个金牌小项对应40条运动员金牌记录，不能把40条称40枚官方金牌。',link='../任务三_专题深挖/S2_口径的魔力/09_奖牌口径实验室/index.html',label='打开口径实验室',fallback='核心证据图/01_统计单位与名次.pdf'),
dict(title='先确认一行记录代表什么',time='1:00—2:00',question='如果把疑似重复全部删除，会不会删掉合法记录？',action='在任务一切换疑似重复超额行剔除敏感性，查看处理前后的影响。',claim='重复候选不等于错误。保留主数据并公开剔除敏感性；团体成员各占一行，泛化标签也不能逆推出真实小项。',link='../任务一_数据体检/index.html#research-closure',label='打开数据体检',fallback='../任务一_数据体检/05_数据问题影响账本/数据问题影响账本.md'),
dict(title='一个结论能承受多少次排除？',time='2:00—3:00',question='冠军控制权的下降，在缩小样本后还确定吗？',action='比较113项的来源替换结果与排除未决系列后50项的区间，看零线是否落在区间内。',claim='同113项替换后仍下降7.37个百分点；50项排除子队列的区间跨零，不能说所有检验都确认下降。对象是小项金牌控制权，不是个人冠军能力。',link='../任务三_专题深挖/S3_冠军的保质期/11_历史来源敏感性/index.html',label='查看冠军敏感性',fallback='核心证据图/02_固定队列与排除敏感性.pdf'),
dict(title='复杂模型一定更准吗？',time='3:00—4:00',question='为什么最新2028主阅读反而采用简单基准？',action='先比较同单位逐折MAE，再看最新中性基准前十。需要讨论旧滑杆时，再展开历史情景。',claim='原RF/GB有局部收益，但小项口径没有稳定优势；45%权重只作情景。1120是比较条件，新榜不附未校准区间，新增运动与完整集成仍有验证边界。',link='../任务四_开放创作/05_满分升级/15_原项目模型时序核验/index.html',label='打开最新预测核验',fallback='核心证据图/03_原模型与同口径基准.pdf'),
dict(title='把探索权与复核权交给读者',time='4:00—5:00',question='如果不同意结论，读者能从哪里开始复核？',action='短暂展示五个实验室，再打开正式报告和三图证据册，指出CSV、方法与来源记录的位置。',claim='交互用于探索，图表用于读数，CSV与脚本用于复算。历史555项未完成现行IOC全项核验；两份正式PDF均20页，补充核验独立提供。',link='../作品总入口/index.html',label='打开五个实验室',fallback='报告/百年圣火_正式报告.pdf')]
parts=['<h1>五分钟，看清一条证据链</h1><p>建议路线与时长，实际演示请计时试讲。证据在新标签页打开；导览保留当前位置。页面和资料均可从本地打开。</p><nav aria-label="评审路线站点" class="judge-stops">']
parts+=['<a href="#step-'+str(i+1)+'">'+str(i+1)+' '+escape(x['title'])+'</a>' for i,x in enumerate(steps)];parts+=['</nav><p id="judge-position" aria-live="polite"></p>']
for i,x in enumerate(steps):
    parts.append(f'<section class="judge-step" id="step-{i+1}" aria-labelledby="judge-title-{i+1}"><p>{x["time"]} · 建议时段</p><h2 id="judge-title-{i+1}" tabindex="-1">{x["title"]}</h2><p><strong>从问题开始：</strong>{x["question"]}</p><p><strong>现场做一次：</strong>{x["action"]}</p><p><strong>这一步说明：</strong>{x["claim"]}</p><p><a target="_blank" rel="noopener" href="{x["link"]}">{x["label"]}（新标签页）</a> · <a target="_blank" rel="noopener" href="{x["fallback"]}">静态证据回退</a></p></section>')
parts+=['<div class="judge-actions" hidden><button type="button" id="judge-prev">上一站</button><button type="button" id="judge-next">下一站</button></div><hr><p><a href="核心证据图/三张核心证据图.pdf">三图证据册</a> · <a href="视频/答辩追问与证据定位.html">答辩追问</a> · <a href="提交前检查.html">提交清单</a></p><p>现场回退：三维加载慢时直接使用对应静态证据；不把本机验收称异机实测。视频成片、实际耗时及主办方渠道仍须团队落实。</p>']
s=BeautifulSoup((BASE/'00_先看这里.html').read_text(encoding='utf-8'),'html.parser')
for x in s.select('script,#ox-motion-bridge-style,aside.side'):x.decompose()
for x in s.select('aside'):x.decompose()
s.title.string='五分钟评审路线 · 数说奥运'
head=s.select_one('.head h1')
if head:head.string='从问题走到证据'
main=s.select_one('main.article');main.clear()
for x in list(BeautifulSoup(''.join(parts),'html.parser').contents):main.append(x)
for a in s.select('.top .download'):a.decompose()
style=s.new_tag('style');style.string='''.layout{display:block;max-width:1100px}.judge-stops{display:flex;flex-wrap:wrap;gap:10px 22px;margin:24px 0}.judge-stops a[aria-current="step"]{font-weight:800;text-decoration-thickness:3px}.judge-step h2{margin-top:1em}.judge-step[hidden]{display:none}.judge-actions{display:flex;gap:20px;margin:24px 0}.judge-actions[hidden]{display:none}.judge-actions button{font:inherit;color:inherit;background:transparent;border:0;border-bottom:1px solid currentColor;padding:8px 0;cursor:pointer}.judge-actions button:disabled{opacity:.4;cursor:default}.judge-actions button:focus-visible,.judge-stops a:focus-visible{outline:2px solid currentColor;outline-offset:5px}@media print{.judge-step[hidden]{display:block}.judge-actions,.judge-stops{display:none}}''';s.head.append(style)
script=s.new_tag('script');script.string='''(()=>{const panels=[...document.querySelectorAll('.judge-step')],links=[...document.querySelectorAll('.judge-stops a')],prev=document.getElementById('judge-prev'),next=document.getElementById('judge-next');let current=0;document.querySelector('.judge-actions').hidden=false;const show=(focus=false)=>{const m=location.hash.match(/^#step-([1-5])$/);current=m?Number(m[1])-1:0;panels.forEach((el,i)=>el.hidden=i!==current);links.forEach((el,i)=>{if(i===current)el.setAttribute('aria-current','step');else el.removeAttribute('aria-current')});prev.disabled=current===0;next.disabled=current===4;document.getElementById('judge-position').textContent='第 '+(current+1)+' / 5 站';if(focus)panels[current].querySelector('h2').focus()};prev.onclick=()=>location.hash='step-'+current;next.onclick=()=>location.hash='step-'+(current+2);addEventListener('hashchange',()=>show(true));show()})();''';s.body.append(script)
(BASE/'五分钟评审路线.html').write_text(str(s),encoding='utf-8')
(BASE/'五分钟评审路线.json').write_text(json.dumps(steps,ensure_ascii=False,indent=2),encoding='utf-8')
print('Built local judge route with five steps and static evidence fallbacks.')
