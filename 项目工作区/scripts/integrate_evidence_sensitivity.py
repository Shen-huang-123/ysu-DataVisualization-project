"""Put source sensitivity into existing task pages, with offline native controls."""
from pathlib import Path
import os,re
import pandas as pd
ROOT=Path(__file__).resolve().parents[2]
D=ROOT/'交付文件'
OUT=D/'任务三_专题深挖/S2_口径的魔力/08_逐项外部核验/未决证据三方案敏感性'
impact=pd.read_csv(OUT/'三方案名次敏感性.csv')
summary=pd.read_csv(OUT/'三方案覆盖与头部.csv')
pages=['任务一_数据体检/index.html','任务二_百年全景/05_交互总览/index.html','任务三_专题深挖/统一中文入口/index.html','任务四_开放创作/index.html']
for name in pages:
    p=D/name;s=p.read_text(encoding='utf-8')
    rel=os.path.relpath(OUT,p.parent).replace('\\','/')
    rows=''
    for year in [2008,2012,2016]:
        a=impact[(impact.Year==year)&impact.方案.eq('二次来源替换555项')].iloc[0]
        c=summary[(summary.Year==year)&summary.方案.eq('排除555项的剩余子集')].iloc[0]
        rows+=f'<tr><th scope="row">{year}</th><td>{a.金牌数名次变动代表团数}</td><td>{a.最大金牌名次位移}</td><td>{c.小项数}</td></tr>'
    html=f'''<!-- EVIDENCE_SENSITIVITY_START --><section id="evidence-sensitivity" class="research-closure" aria-labelledby="es-title"><h2 id="es-title">头部相近，精确名次仍会改变</h2><p class="rc-lead">历史三届采用三种来源方案复算：保留原代理、替换555项二次来源、排除555项。替换涉及31个小项、64个奖牌字段。</p><div class="rc-scroll" tabindex="0" aria-label="三届来源敏感性"><table class="rc-table"><thead><tr><th>届次</th><th>替换后金牌名次变动代表团数</th><th>最大名次位移</th><th>排除后剩余小项</th></tr></thead><tbody>{rows}</tbody></table></div><p>二次来源替换后三届金牌数前三名次集合相同；这不保证其他名次稳定。这里固定每届代表团池，按金牌数并列排名，不能称为IOC现行官方榜。</p><details><summary>为什么排除未决项，也不能直接解决问题？</summary><p>排除后只剩355个小项，运动构成改变；2012、2016的金牌数前三名次集合也改变。它是子集压力测试，不能替代完整奖牌榜。二次来源替换同样不是官方认证。</p></details><details><summary>这轮复算能支持哪些结论？</summary><p>巴黎2024官方小项分析不依赖这555项，可作为主证据。历史逐队精确数值应附版本与敏感性。冠军延续已追加来源敏感性：同113项替换不变，排除后50项的区间跨零。主场运动员行17案已复现，另建小项三情景对照：平均关联为正，巴西个案依方法改变。原RF/GB可迁移核心已追加时序重跑与2028同口径重训；新增运动、资格及完整集成区间仍未获同构验证。</p></details><a href="{rel}/三方案逐代表团奖牌与名次.csv" download>下载三方案逐队比较 ↗</a> · <a href="{rel}/未决证据影响报告.html">复算方法与限制 ↗</a></section><!-- EVIDENCE_SENSITIVITY_END -->'''
    s=re.sub(r'<!-- EVIDENCE_SENSITIVITY_START -->.*?<!-- EVIDENCE_SENSITIVITY_END -->','',s,flags=re.S)
    marker='<!-- RESEARCH_CLOSURE_END -->'
    assert marker in s
    s=s.replace(marker,marker+html,1)
    p.write_text(s,encoding='utf-8')
print('Sensitivity embedded in four task pages; offline details and CSV links.')

# Refresh themed reading edition after source updates.
import runpy
runpy.run_path(str(Path(__file__).with_name("publish_uncertainty_reading.py")))
