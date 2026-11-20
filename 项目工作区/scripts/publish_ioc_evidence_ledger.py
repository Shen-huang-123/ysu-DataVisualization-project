"""Publish current IOC evidence scope; partial decisions never certify full events."""
from pathlib import Path
from html import escape
import json,re,os
import pandas as pd
from evidence_guard import verify_olympedia
ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力/08_逐项外部核验'
OUT=BASE/'证据链修复_20261120'
def main():
    n=verify_olympedia();OUT.mkdir(exist_ok=True)
    base=pd.read_csv(BASE/'Olympedia独立交叉核验/历史910项双层证据总表.csv').fillna('')
    actions=pd.read_csv(BASE/'IOC决议补证_20261117/IOC逐奖牌动作与现有记录对照.csv').fillna('')
    queue=pd.read_csv(BASE/'历史555项风险优先核验清单.csv').fillna('')
    priority={(int(r.Year),r.Event):int(r.优先级) for r in queue.itertuples()}
    summaries={(int(y),e):'；'.join(f'{r.Medal}/{r.NOC}：{r.evidence_scope}' for r in g.itertuples()) for (y,e),g in actions.groupby(['Year','Event'])}
    base['队列优先级']=[priority.get((int(r.Year),r.Event),'') for r in base.itertuples()]
    base['局部IOC补证摘要']=[summaries.get((int(r.Year),r.Event),'') for r in base.itertuples()]
    base['全项现行IOC认证判定']='未由本轮独立完成；不得由来源类型或局部动作推定'
    base['原始证据完整性']='本行未逐文件检查，不外推97份Olympedia检查'
    base.loc[base['Olympedia逐项链接'].ne(''),'原始证据完整性']='对应Olympedia原页已对原清单SHA256验证'
    base['原件边界']='IOC动作台账为2026-11-17结构化阅读记录，不冒充网页原件'
    base.to_csv(OUT/'当前910项证据台账.csv',index=False,encoding='utf-8-sig');actions.to_csv(OUT/'IOC局部动作台账.csv',index=False,encoding='utf-8-sig')
    differences=pd.read_csv(BASE/'Olympedia独立交叉核验/历史555项独立交叉对照.csv').fillna('')
    differences=differences[differences['对照结果'].eq('旧存档与现行二次来源有差异')].copy()
    def explanation(row):
        if row.Event=="Modern Pentathlon Women's Individual":return '赛时铜牌与事后补颁不同；现有UIPM记录支持白俄罗斯补颁，不能用赛时册覆盖现行状态'
        if row.Year==2012 and row.Event.startswith('Canoeing'):return '旧存档缺银；IOC已有俄罗斯升银、西班牙升铜动作，须区分赛时版本'
        if row.Year==2012 and row.Event.startswith('Weightlifting'):return '旧存档缺铜；IOC已有朝鲜铜牌递补动作，不推定同项金银完整状态'
        return '旧存档缺少一色；既有官方赛时册及协会材料支持补缺，仍不证明完整现行IOC状态'
    differences['既有裁定与边界']=differences.apply(explanation,axis=1)
    differences['本轮复核范围']='恢复原件重新解析配对；沿用已有逐案来源解释，未新增在线认证'
    differences['裁定依据']='../Olympedia独立交叉核验/双来源核验报告.md；IOC局部动作台账.csv'
    differences.to_csv(OUT/'七项差异复核清单.csv',index=False,encoding='utf-8-sig')
    summary=dict(raw_pages_sha256_pass=n,events=len(base),legacy_snapshot_subset=555,secondary_agreement=548,secondary_differences=7,partial_actions=len(actions),partial_action_events=len(summaries),high_priority_snapshot_events=sum(v==1 for v in priority.values()),new_complete_current_ioc_certifications=0,note='555是旧存档主来源子集，非全局IOC未认证数。')
    (OUT/'当前证据摘要.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    paragraphs=[
      '97份Olympedia原件已从Git找回，与原清单SHA256全部一致。17个全站HTML后处理脚本已跳过外部核验证据目录，Git保留原字节。910行历史代理表和生成器已修正过强的IOC核验标签。',
      'IOC导入审核新增逐小项地址类型、原件哈希、有效日期、人工复核、完整范围和空奖牌理由检查，保留重复NOC。新闻、图书馆赛时册和局部决议不能冒充完整现行小项结果。导入审核不自动覆盖来源总表。',
      '910项包含555项2023第三方抓取存档主来源子集，其余含国际协会结果、赛时成绩册和IOC决议。555项已有Olympedia二次对照，548一致、7差异；既不是555项完全没有证据，也不能说其余355项已全部取得现行IOC完整小项认证。',
      '已读IOC局部台账12条动作涉及8项，必须保留脚注和历史时点，不能用动作数当作完整小项认证数。本轮新增完整IOC认证0项。伦敦2012男子69公斤级铜牌已有2026-11-17记录的IOC递补决定，不再写成仅有二次来源；但不推定同项金银状态。原公告和附件未全部保存，阅读记录与原件归档分开。',
      '已隔离重跑东道主来源敏感性、冠军延续来源敏感性及同口径预测基准，15张CSV与既有交付逐表一致，数值容差1e-8。修复证据字节和文案不改变奖牌值，不是新一轮全量官方认证。另从恢复原件隔离重跑555项配对，逐表核验见复算一致性记录。',
      '冠军固定113项来源替换仍下降7.37个百分点；排除后50项区间跨零，不能称所有样本均稳健。东道主关联仍受主办选择与混杂限制。同口径预测基准不等于已发布2028最终集成通过验证，也不支持机器学习优于简单基线的宣传。',
      '剩余补证优先核高风险冲突和有条件重分配事项。原队列35项高风险基于原代理与旧存档冲突分类，不等于35项全无解释。七处二次差异须区分赛时字段缺失与事后重分配；已解释不等于完整现行IOC认证。',
      '复现顺序：evidence_guard.py校验原件，qa_ioc_evidence_integrity.py检验导入边界，publish_ioc_evidence_ledger.py生成台账。原件损坏时应停止，不能重写旧哈希清单掩盖改动。recompute_ioc_sensitivity_isolated.py接对应脚本名隔离复算，不覆盖前端。'
    ]
    (OUT/'修复结果与证据边界.md').write_text('# IOC证据链修复与当前边界（2026-11-20）\n\n'+'\n\n'.join(paragraphs)+'\n',encoding='utf-8')
    files=['七项差异复核清单.csv','当前910项证据台账.csv','IOC局部动作台账.csv','当前证据摘要.json','隔离复算一致性.json','修复结果与证据边界.md']
    links=''.join(f'<li><a href="{escape(f)}">{escape(f)}</a></li>' for f in files)
    (OUT/'index.html').write_text('<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>IOC证据链修复与当前边界</title><style>body{max-width:1050px;margin:40px auto;padding:0 24px;font:16px/1.9 system-ui;color:#e8eeee;background:#101e25}a{color:#a6d8d2}h1{font-size:32px}p{margin:1.5em 0}</style><h1>IOC证据链修复与当前边界</h1>'+''.join('<p>'+escape(x)+'</p>' for x in paragraphs)+'<h2>下载与复核</h2><ul>'+links+'</ul></html>',encoding='utf-8')
    for relative in ['07_口径实验室/index.html','09_奖牌口径实验室/index.html','06_滚动叙事专题/index.html']:
        page=BASE.parent/relative
        if not page.exists():continue
        text=page.read_text(encoding='utf-8');text=re.sub(r'<!-- IOC_CHAIN_START -->.*?<!-- IOC_CHAIN_END -->','',text,flags=re.S)
        href=Path(os.path.relpath(OUT/'index.html',page.parent)).as_posix()
        notice=f'<!-- IOC_CHAIN_START --><p style="margin:2rem 6vw;line-height:1.8">历史来源：555项为旧存档来源子集，已有二次对照；不等于现行IOC全项认证。<a href="{href}">查看当前证据台账与原件核验</a></p><!-- IOC_CHAIN_END -->'
        page.write_text(text.replace('</body>',notice+'</body>'),encoding='utf-8')
    final=ROOT/'交付文件/最终提交材料'
    report=(OUT/'index.html').read_text(encoding='utf-8')
    for filename in files:
        href=Path(os.path.relpath(OUT/filename,final)).as_posix()
        report=report.replace('href="'+filename+'"','href="'+href+'"')
    (final/'IOC证据修复与复算补充说明.html').write_text(report,encoding='utf-8')
    old_report=BASE/'证据链问题核查_20261120/问题与修复顺序.md'
    old=old_report.read_text(encoding='utf-8')
    marker='> 后续修复状态：'
    if marker not in old:
        old=marker+'原件、来源标签、导入审核及当前台账已修，隔离复算已完成。下文为修复前的问题快照；当前结果见[修复说明](../证据链修复_20261120/index.html)。\n\n'+old
        old_report.write_text(old,encoding='utf-8')
    progress=ROOT/'交付文件/证据边界核验进度.md';text=progress.read_text(encoding='utf-8');text=re.sub(r'<!-- IOC_CURRENT_START -->.*?<!-- IOC_CURRENT_END -->\n*','',text,flags=re.S)
    notice='<!-- IOC_CURRENT_START -->\n## 当前状态（2026-11-20）\n\n97份Olympedia原件已恢复且SHA256全通过；910行来源标签与导入审核已修。555仅指旧存档主来源子集，不是全局IOC认证缺口。男子69公斤级铜牌已补IOC动作证据，以下旧阶段描述不代表当前状态。详见[当前台账与修复说明](任务三_专题深挖/S2_口径的魔力/08_逐项外部核验/证据链修复_20261120/index.html)。本轮新增完整IOC认证0项。\n<!-- IOC_CURRENT_END -->\n\n'
    progress.write_text(notice+text,encoding='utf-8');print(json.dumps(summary,ensure_ascii=False,indent=2))
if __name__=='__main__':main()

# Preserve conclusion-adjacent evidence notes after regeneration.
from publish_evidence_closure import main as publish_closure_notes
publish_closure_notes()
