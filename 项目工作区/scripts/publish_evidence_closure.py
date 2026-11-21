"""Publish conclusion-adjacent source notes and an auditable closure supplement."""
from pathlib import Path
from html import escape
import json,os,re
import pandas as pd
ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力/08_逐项外部核验/关键结论闭环_20261120'
FINAL=ROOT/'交付文件/最终提交材料'
def main():
    if not (BASE/'闭环核验摘要.json').exists():return
    info=json.loads((BASE/'闭环核验摘要.json').read_text(encoding='utf-8'))
    risk=pd.read_csv(BASE/'35项风险重排与影响.csv');matrix=pd.read_csv(BASE/'最终预测验证矩阵.csv');scores=pd.read_csv(BASE/'实际模型基线对比.csv')
    paragraphs=[
      '2026-11-21后续核查：发现2012女子举重63kg/75kg在旧存档和Olympedia中共同交叉配对，现已加入性别与级别硬约束并更正。四组隔离复算的数值结论在1e-8容差内不变，冠军转移附表项目身份已纠正。新增核读6篇官方机构资料、归档2篇原件；4篇直接访问受限，仅保留阅读记录。颁牌日期及新闻局部颜色冲突保留说明，新增完整IOC小项三色认证仍为0。',
      '本轮完成35项逐条分类、对关键结论的影响评估、实际发布模型的复算核验，以及核心图旁来源说明。未完成的官方授牌状态和完整集成联合历史验证继续明确保留，不把访问成功或公式重现称作全部预测能力验证。',
      f"35项中有{info['gold_changes']}项原代理金牌集合与二次来源不同，{info['baseline_sensitive_events']}项在单项退回原代理时会改变2028中性主榜。重新分为10项金牌变动优先、8项其他预测或冠军转移关联、17项其余后续核查。这是待核优先级，不是35项真伪裁决。",
      f"单项退回原代理对1120固定总池、同一212队主榜的最大点值变化为{info['maximum_one_event_baseline_change']:.3f}单位。此为一次只变一项的敏感性，不是误差上界，不能相加，也不证明对东道主和冠军结论同样影响很小。冠军与主办关联须读各自替换/排除检验。",
      '新归档加拿大奥委会颁牌报道和两篇UWW历史报道，均保留原字节与SHA256。IWF复检名单通过浏览服务读取，直接下载403；CAS地址返回HTML壳而非PDF，未计为裁决原件。IOC男子69公斤级铜牌及女子69公斤级暂缓银牌的正文已复读，只确认明确动作，不擅自补全现行三色。',
      '发现UWW2019对伦敦120kg摔跤的金银名单与IOC2021并列金决定不是同一时点；较晚IOC决定还附俄罗斯选手暂缓颁发条件。本轮没有找到足以确认后续实际颁发的资料，故不能用禁赛结束日期替代颁发证据。',
      '当前主榜212队、50行原模型评分及10465行逐队误差可在1e-8容差内复现。修复整套运行后2028项目格混入历史折的导出问题，重跑只含3600个2028项目格，实际标签全空，预测值与已交付数据一致。原45/45/10排名门控集成的127队公式也可重构，但算术重构不是同构历史回测。',
      '小项二次来源下，2012/2016/2024的基线MAE约为1.288/1.366/1.872，55/45混合约为1.280/1.303/1.900。2024折混合更差，不支持稳定优于基线或45%最优。历史记录为事后整理版，缺逐届真实赛前冻结快照。',
      '完整集成的同构历史验证仍缺五项新增运动统一事前输入、可比资格和主场外推检验，80%区间也未获得该最终集成及新基准的独立覆盖率认证。因此中性基准继续作为主阅读；机器学习、排名、主场、资格保持条件情景，旧区间仅作旧基线参考宽度，不套到新主榜或集成。',
      '来源稳定性图说明：东道主效应是历史关联，非主办的因果效应；冠军固定113项下降7.37个百分点，来源替换不变，但排除后50项区间跨零；奖牌口径实验2024以329小项为主证据，历史代理与二次来源另列。',
      '复现：先evidence_guard.py；再隔离运行project_model_strict_replay.py；运行validate_evidence_closure.py及publish_evidence_closure.py。新补证原件与下载清单位于资料文件/外部核验/高风险补证_20261120。新完整IOC认证仍为0项；未据新局部来源静默修改主数据。'
    ]
    body='# 关键结论证据闭环核验（2026-11-20）\n\n'+'\n\n'.join(paragraphs)+'\n\n## 最终预测验证矩阵\n\n'+matrix.to_markdown(index=False)+'\n\n## 实际模型与基线\n\n'+scores[['Year','模型','MAE','RMSE']].to_markdown(index=False)+'\n'
    (BASE/'关键结论核验说明.md').write_text(body,encoding='utf-8')
    (FINAL/'关键结论证据与预测验证补充说明.md').write_text(body,encoding='utf-8')
    link_files=['35项风险重排与影响.csv','最终预测验证矩阵.csv','实际模型基线对比.csv','闭环核验摘要.json','关键结论核验说明.md','../后续补证_20261121/index.html']
    links=''.join(f'<li><a href="{escape(f)}">{escape(f)}</a></li>' for f in link_files)
    style='body{max-width:1120px;margin:40px auto;padding:0 24px;background:#101e25;color:#e8eeee;font:16px/1.85 system-ui}a{color:#a6d8d2}h1{font-size:32px}p{margin:1.3em 0}table{border-collapse:collapse;width:100%;font-size:14px}td,th{text-align:left;padding:10px;border-bottom:1px solid #65777b;vertical-align:top}.scroll{overflow:auto}@media print{@page{size:A4;margin:16mm}body{max-width:none;margin:0;padding:0;background:white;color:#17282e;font-size:10pt}a{color:#17282e}h1{font-size:20pt}h2{break-after:avoid}.validation-matrix{break-before:page}.download-section{display:none}tr{break-inside:avoid}.scroll{overflow:visible}table{font-size:8.5pt}td,th{padding:5px}p{orphans:3;widows:3}}'
    page='<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>关键结论证据闭环核验</title><style>'+style+'</style><h1>关键结论证据闭环核验</h1>'+''.join('<p>'+escape(t)+'</p>' for t in paragraphs)+'<h2 class="validation-matrix">最终预测验证矩阵</h2><div class="scroll">'+matrix.to_html(index=False,border=0)+'</div><h2>实际模型与基线</h2><div class="scroll">'+scores[['Year','模型','MAE','RMSE']].round(4).to_html(index=False,border=0)+'</div><section class="download-section"><h2>下载与逐项复核</h2><ul>'+links+'</ul></section></html>'
    (BASE/'index.html').write_text(page,encoding='utf-8')
    final_page=page
    for filename in link_files:final_page=final_page.replace('href="'+filename+'"','href="'+Path(os.path.relpath(BASE/filename,FINAL)).as_posix()+'"')
    (FINAL/'关键结论证据与预测验证补充说明.html').write_text(final_page,encoding='utf-8')
    # One legacy entry was missing the current-baseline reading block.
    from bs4 import BeautifulSoup
    import ast
    dashboard=ROOT/'交付文件/任务四_开放创作/01_交互式Dashboard/index.html'
    text=dashboard.read_text(encoding='utf-8')
    if 'id="project-reading-policy"' not in text:
        original=ROOT/'交付文件/任务四_开放创作/09_预测风暴实验室/index.html'
        policy=BeautifulSoup(original.read_text(encoding='utf-8'),'html.parser').select_one('#project-reading-policy')
        policy.select_one('[data-evidence-closure]').decompose() if policy.select_one('[data-evidence-closure]') else None
        css=''
        tree=ast.parse((ROOT/'项目工作区/scripts/publish_project_model_audit.py').read_text(encoding='utf-8'))
        for node in tree.body:
            if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='css' for t in node.targets):css=ast.literal_eval(node.value)
        block=css+str(policy)
        text=re.sub(r'(<main\b[^>]*>)',lambda m:m.group(1)+block,text,count=1)
    text=text.replace('切换新增项目情景，查看预测排名、点估计与80%不确定性区间。预测不是答案，而是一组可以被检验的假设。','先读同口径中性基准；旧模型与未校准区间保留为可展开的历史情景。')
    dashboard.write_text(text,encoding='utf-8')
    # Reuse the existing archive organizer on this entry only.
    organizer=ROOT/'项目工作区/scripts/organize_forecast_reading.py'
    class DashboardOnly(ast.NodeTransformer):
        def visit_Assign(self,node):
            if any(isinstance(t,ast.Name) and t.id=='PAGES' for t in node.targets):node.value=ast.List(elts=[ast.Constant('01_交互式Dashboard/index.html')],ctx=ast.Load())
            return self.generic_visit(node)
    tree=DashboardOnly().visit(ast.parse(organizer.read_text(encoding='utf-8')));ast.fix_missing_locations(tree)
    exec(compile(tree,str(organizer),'exec'),{'__name__':'dashboard_reading','__file__':str(organizer)})
    captions=[
      ('交付文件/任务三_专题深挖/S1_东道主效应/index.html','host-proof-charts','来源：既有运动员行分析，另有小项来源替换与排除检验。核查：三方案结果可复现。边界：主办选择、抵制、身份与项目变化仍可能混杂，图中关联不能直接解释为主办的因果收益。'),
      ('交付文件/任务三_专题深挖/S3_冠军的保质期/07_王朝生存图/index.html','curve','来源：历史小项代理与二次来源情景。核查：固定113项来源替换仍下降7.37个百分点；排除后50项区间跨零。边界：研究的是代表团同小项金牌控制权，不是个人寿命，也未证明竞争加剧是原因。'),
      ('交付文件/任务三_专题深挖/S2_口径的魔力/07_口径实验室/index.html','rule-ranking-table','来源：2024年329小项表是主证据；历史三届为代理与分层对照。核查：换统计单位会改变榜单，已有35项历史高风险逐项清单。边界：规则实验不是新的官方排名，历史代理未获全项IOC认证。'),
      ('交付文件/任务三_专题深挖/S2_口径的魔力/09_奖牌口径实验室/index.html','rank-chart','来源：2024年329小项表。核查：三口径保持各自定义；历史证据和高风险逐项记录单列。边界：运动员行反映团队规模，不等同于官方小项奖牌；不能据此判断公平性。'),
      ('交付文件/任务四_开放创作/01_交互式Dashboard/index.html','project-reading-policy','来源：最新中性基准。核查：当前主榜可复现；旧集成与旧区间须主动展开比较。边界：未校准的旧区间不能作为此主榜或完整集成的80%预测区间。'),
      ('交付文件/任务四_开放创作/index.html','project-reading-policy','来源：截至2024数据重训的中性小项基准，1120仅为固定比较条件。核查：212队主榜及实际模型历史评分可重现；2024折55/45混合误差略高于基线。边界：完整集成的排名、主场、资格和80%区间未通过联合历史认证。'),
      ('交付文件/任务四_开放创作/09_预测风暴实验室/index.html','chart','以下交互图属于保留的条件情景。核查：旧集成公式可重构，不等于预测能力通过验证。边界：旧区间仅为旧基线参考宽度，不能称当前中性主榜或完整集成的已校准80%区间。'),
      ('交付文件/任务四_开放创作/05_满分升级/15_原项目模型时序核验/index.html','project-reading-policy','核验范围：原RF/GB参数、严格年份回放、212队2028中性主榜。边界：事后整理数据不等于真实时点冻结资料；排名门控、主场、资格和区间的完整联合验证仍未完成。')]
    for name,target,message in captions:
        p=ROOT/name
        if not p.exists():continue
        text=p.read_text(encoding='utf-8');text=re.sub(r'<!-- EVIDENCE_CLOSURE_START -->.*?<!-- EVIDENCE_CLOSURE_END -->','',text,flags=re.S)
        found=re.search(r'<[a-zA-Z][^>]*\bid=["\x27]'+re.escape(target)+r'["\x27][^>]*>',text)
        if not found:
            if name.endswith('15_原项目模型时序核验/index.html'):found=re.search(r'<h1\b[^>]*>.*?</h1>',text,flags=re.S)
            if not found:raise ValueError('Missing evidence caption target '+name+' '+target)
        href=Path(os.path.relpath(BASE/'index.html',p.parent)).as_posix()
        note='<!-- EVIDENCE_CLOSURE_START --><aside data-evidence-closure="20261120" style="margin:18px 0;padding:14px 0;border-top:1px solid #89959466;line-height:1.85;font-size:14px">'+escape(message)+' <a href="'+href+'">逐项证据与验证矩阵</a></aside><!-- EVIDENCE_CLOSURE_END -->'
        # Before SVG/table/chart containers; inside a reading section, after its opening tag.
        position=found.end() if target=='project-reading-policy' else found.start()
        p.write_text(text[:position]+note+text[position:],encoding='utf-8')
    ledger=BASE.parent/'证据链修复_20261120/index.html'
    text=ledger.read_text(encoding='utf-8')
    text=re.sub(r'<!-- CLOSURE_LINK_START -->.*?<!-- CLOSURE_LINK_END -->','',text,flags=re.S)
    link='<!-- CLOSURE_LINK_START --><p><a href="../关键结论闭环_20261120/index.html">35项风险重排、实际预测模型验证与图旁证据说明</a></p><!-- CLOSURE_LINK_END -->'
    ledger.write_text(text.replace('</html>',link+'</html>'),encoding='utf-8')
    print('Published eight conclusion-adjacent notes and final supplement.')
if __name__=='__main__':main()
