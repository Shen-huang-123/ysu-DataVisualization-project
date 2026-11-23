"""Publish a complete evidence route using the established document shell."""
from pathlib import Path
from html import escape
import re,json
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[2];BASE=ROOT/'交付文件/最终提交材料'
steps=[
dict(title='同一届奥运，为什么有两个名次？',question='西班牙15→5，是规则变了，还是我们数的东西变了？',action='打开奖牌口径实验室，在小项与运动员行两个端点间切换。中间权重只演示压力测试。',claim='同样按金银铜排序，统计单位改变名次；5个金牌小项对应40条运动员金牌记录，不能把40条称40枚官方金牌。',link='../任务三_专题深挖/S2_口径的魔力/09_奖牌口径实验室/index.html#rank-discovery',label='打开口径实验室',fallback='核心证据图/01_统计单位与名次.pdf'),
dict(title='先确认一行记录代表什么',question='如果把疑似重复全部删除，会不会删掉合法记录？',action='在任务一切换疑似重复超额行剔除敏感性，查看处理前后的影响。',claim='重复候选不等于错误。保留主数据并公开剔除敏感性；团体成员各占一行，泛化标签也不能逆推出真实小项。',link='../任务一_数据体检/index.html#research-closure',label='打开数据体检',fallback='../任务一_数据体检/05_数据问题影响账本/数据问题影响账本.html'),
dict(title='一个结论能承受多少次排除？',question='冠军控制权的下降，在缩小样本后还确定吗？',action='切换113项来源替换与排除后50项情景，观察区间与零线，并核对点估计和样本数。',claim='同113项替换后仍下降7.37个百分点；50项排除子队列的区间跨零，不能说所有检验都确认下降。对象是小项金牌控制权，不是个人冠军能力。',link='../任务三_专题深挖/S3_冠军的保质期/11_历史来源敏感性/index.html#interval-discovery',label='查看冠军敏感性',fallback='核心证据图/02_固定队列与排除敏感性.pdf'),
dict(title='复杂模型一定更准吗？',question='为什么最新2028主阅读反而采用简单基准？',action='切换口径、模型与届次，查看未胜过同口径基准的回测，再看最新中性基准前十。需要讨论旧滑杆时，再展开历史情景。',claim='原RF/GB有局部收益，但小项口径没有稳定优势；45%权重只作情景。1120是比较条件，新榜不附未校准区间，新增运动与完整集成仍有验证边界。',link='../任务四_开放创作/05_满分升级/15_原项目模型时序核验/index.html#model-discovery',label='打开最新预测核验',fallback='核心证据图/03_原模型与同口径基准.pdf'),
dict(title='把探索权与复核权交给读者',question='如果不同意结论，读者能从哪里开始复核？',action='短暂展示五个实验室，再打开正式报告和三图证据册，指出CSV、方法与来源记录的位置。',claim='交互用于探索，图表用于读数，CSV与脚本用于复算。历史555项未完成现行IOC全项核验；两份正式PDF均20页，补充核验独立提供。',link='../作品总入口/index.html',label='打开五个实验室',fallback='报告/百年圣火_正式报告.pdf')]

steps.insert(2,dict(title='百年扩张之后，谁获得了机会？',question='参与记录接近平衡，是否就代表机会完全相同？',action='在百年全景中联动届次、性别和项目，先观察绝对规模，再比较相应份额与项目结构。',claim='2024女性参赛记录约占49.1%，获奖记录约占50.3%；这里统计的是记录，不能改称独立人数，也不能据此认定赛程机会完全对称。历史身份与缺席断点需要分别解释。',link='../任务二_百年全景/05_交互总览/index.html',label='探索百年全景',fallback='报告/百年圣火_正式报告.pdf'))
steps.insert(4,dict(title='主场平均受益，为什么还有反例？',question='平均关联为正，是否意味着每个主办国都会受益？',action='对照原17案与共同小项15案，再查看巴西在不同来源、口径与方法下的结果。',claim='15个共同案例三情景平均差约为+3.02、+3.01、+2.87个百分点；巴西可出现负值。平均正关联不能保证个案受益，口径与比较方法同时改变时，也不能将差异归因于单一因素或主场因果效应。',link='../任务三_专题深挖/S1_东道主效应/01_来源与口径敏感性/index.html',label='查看主场反例',fallback='报告/百年圣火_正式报告.pdf'))
steps.insert(5,dict(title='其余专题如何组成完整解释？',question='除了榜单、冠军和主场，作品还解释了哪些问题？',action='进入十专题入口，按问题选择专题；再对照结论稳定性地图，逐项查看原判断、复核、反例与保留边界。',claim='十专题分别讨论不同问题，不能用一个显著结果替代全部论证。描述性关联、样本纳入规则、替代分母与历史解释须分别交代；一手档案不足的解释保留为待证假说。',link='../任务三_专题深挖/统一中文入口/index.html',label='阅读十个专题',fallback='../任务三_专题深挖/11_结论稳定性地图/index.html'))
notes=[
('把官方小项与运动员行分开，再固定金银铜排序规则比较。','中间权重是压力测试，不是新的官方公平榜。'),
('先定义记录单位，再按编号、重复候选、缺失与项目映射逐项检查；用影响账本复算处理后果。','疑似重复不自动删除；历史泛化标签无法无损恢复。'),
('绝对量、份额和机会结构分层比较，切换筛选时同时核对分母。','女性记录份额不等于独立参赛人数；历史代表团不直接并入现今国家。'),
('固定113小项队列做来源替换，再用排除未决系列的50项子队列检验。','排除会改变样本，不能把50项解释成同一113项的纯来源替换。'),
('保持共同案例，比较三种来源情景，并将原17案复现与15案共同小项结果分列。','观察性比较不自动识别因果；个案对平均结论具有约束。'),
('逐专题检查问题、指标、分母、样本与反例，按稳定性决定结论措辞。','历史解释的可信度取决于档案与纳入规则，不能只凭趋势图推定机制。'),
('使用早于目标届的训练和选择信息，逐折比较原RF/GB、55/45集成与同单位简单基准。','独立岭回归核验不是原RF/GB；历史冻结快照、新增运动同构回测及完整集成区间仍有缺口。'),
('从页面回到报告、CSV、来源记录和脚本，区分可交互探索与可复算证据。','555项未完成现行IOC逐项核验；本机检查不等于第二台设备或现场验收。')]
for step,(method,boundary) in zip(steps,notes):
    step.update(method=method,boundary=boundary)

parts=['<h1>从问题出发，完整探索证据链</h1><p>以讲清问题、方法、发现、反例与证据边界为标准，不设固定讲解时长。可顺序探索，也可选择站点深入。证据在新标签页打开；导览保留当前位置。页面和资料均可从本地打开。</p><nav aria-label="评审路线站点" class="judge-stops">']
parts+=['<a href="#step-'+str(i+1)+'">'+str(i+1)+' '+escape(x['title'])+'</a>' for i,x in enumerate(steps)];parts+=['</nav><p id="judge-position" aria-live="polite"></p>']
for i,x in enumerate(steps):
    parts.append(f'<section class="judge-step" id="step-{i+1}" aria-labelledby="judge-title-{i+1}"><p>第 {i+1} 站 · 评审探索</p><h2 id="judge-title-{i+1}" tabindex="-1">{x["title"]}</h2><p><strong>从问题开始：</strong>{x["question"]}</p><p><strong>现场做一次：</strong>{x["action"]}</p><p><strong>方法与口径：</strong>{x["method"]}</p><p><strong>这一步说明：</strong>{x["claim"]}</p><p><strong>反例与边界：</strong>{x["boundary"]}</p><p><a target="_blank" rel="noopener" href="{x["link"]}">{x["label"]}（新标签页）</a> · <a target="_blank" rel="noopener" href="{x["fallback"]}">静态证据回退</a></p></section>')
parts+=['<div class="judge-actions" hidden><button type="button" id="judge-prev">上一站</button><button type="button" id="judge-next">下一站</button></div><hr><p><a href="核心证据图/三张核心证据图.pdf">三图证据册</a> · <a href="视频/答辩追问与证据定位.html">答辩追问</a> · <a href="提交前检查.html">提交清单</a></p><p>现场回退：三维加载慢时直接使用对应静态证据；不把本机验收称异机实测。视频成片、实际耗时及主办方渠道仍须团队落实。</p>']
s=BeautifulSoup((BASE/'00_先看这里.html').read_text(encoding='utf-8'),'html.parser')
for x in s.select('script,#ox-motion-bridge-style,aside.side'):x.decompose()
for x in s.select('aside'):x.decompose()
s.title.string='评审探索路线 · 数说奥运'
head=s.select_one('.head h1')
if head:head.string='从问题走到证据'
main=s.select_one('main.article');main.clear()
for x in list(BeautifulSoup(''.join(parts),'html.parser').contents):main.append(x)
main.select_one('.judge-stops').insert_before(BeautifulSoup('<section aria-labelledby="judge-study-checks"><h2 id="judge-study-checks">任务三关键结论与复核</h2><ul>\n<li><strong>西班牙排名</strong>\u3000官方小项第 15，运动员行第 5。足球和水球贡献 33 条额外金牌记录；全榜剔除足球后仍领先 3 位，35 种单项剔除的方向一致。<a href="../任务三_专题深挖/S2_口径的魔力/09_奖牌口径实验室/index.html?ef-lens=rows&amp;ef-noc=ESP&amp;exclude=Football#sport-removal">打开足球剔除与复算表</a></li>\n<li><strong>巴西主场反例</strong>\u3000运动员行的五队匹配比较为 +0.13 个百分点，小项代理的三种合成对照均为负。统计单位和比较方法同时改变。<a href="../任务三_专题深挖/S1_东道主效应/01_来源与口径敏感性/index.html">查看巴西对照</a></li>\n<li><strong>冠军延续</strong>\u3000固定 113 项的卫冕率下降 7.37 个百分点；排除未决系列后剩 50 项，点估计下降 7.33 个百分点，95% 区间跨零。<a href="../任务三_专题深挖/S3_冠军的保质期/09_固定小项队列检验/index.html#dynasty-source-sensitivity">查看区间和逐届数据</a></li>\n</ul></section>','html.parser').section)
for a in s.select('.top .download'):a.decompose()
style=s.new_tag('style');style.string='''.layout{display:block;max-width:1100px}.judge-stops{display:flex;flex-wrap:wrap;gap:10px 22px;margin:24px 0}.judge-stops a[aria-current="step"]{font-weight:800;text-decoration-thickness:3px}.judge-step h2{margin-top:1em}.judge-step[hidden]{display:none}.judge-actions{display:flex;gap:20px;margin:24px 0}.judge-actions[hidden]{display:none}.judge-actions button{font:inherit;color:inherit;background:transparent;border:0;border-bottom:1px solid currentColor;padding:8px 0;cursor:pointer}.judge-actions button:disabled{opacity:.4;cursor:default}.judge-actions button:focus-visible,.judge-stops a:focus-visible{outline:2px solid currentColor;outline-offset:5px}@media print{.judge-step[hidden]{display:block}.judge-actions,.judge-stops{display:none}}''';s.head.append(style)
script=s.new_tag('script');script.string='''(()=>{const panels=[...document.querySelectorAll('.judge-step')],links=[...document.querySelectorAll('.judge-stops a')],prev=document.getElementById('judge-prev'),next=document.getElementById('judge-next');let current=0;document.querySelector('.judge-actions').hidden=false;const show=(focus=false)=>{const m=location.hash.match(/^#step-([0-9]+)$/);current=m&&Number(m[1])>=1&&Number(m[1])<=panels.length?Number(m[1])-1:0;panels.forEach((el,i)=>el.hidden=i!==current);links.forEach((el,i)=>{if(i===current)el.setAttribute('aria-current','step');else el.removeAttribute('aria-current')});prev.disabled=current===0;next.disabled=current===panels.length-1;document.getElementById('judge-position').textContent='第 '+(current+1)+' / '+panels.length+' 站';if(focus)panels[current].querySelector('h2').focus()};prev.onclick=()=>location.hash='step-'+current;next.onclick=()=>location.hash='step-'+(current+2);addEventListener('hashchange',()=>show(true));show()})();''';s.body.append(script)
(BASE/'评审探索路线.html').write_text(str(s),encoding='utf-8')
# Preserve existing bookmarks with the same current content, without a redirect flash.
(BASE/'五分钟评审路线.html').write_text(str(s),encoding='utf-8')
for name in ['评审探索路线.json','五分钟评审路线.json']:
    (BASE/name).write_text(json.dumps(steps,ensure_ascii=False,indent=2),encoding='utf-8')
print('Built local judge route with eight steps and static evidence fallbacks.')
