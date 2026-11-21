"""Publish scoped follow-up evidence and a reproducible correction record.

No automatic promotion of a medal action to complete current IOC certification.
Run after historical/secondary matching and the four isolated research replays.
"""
from pathlib import Path
from html import escape
import hashlib, json, shutil
import numpy as np
import pandas as pd
from fetch_followup_evidence import SOURCES
ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力/08_逐项外部核验'
OUT = BASE/'后续补证_20261121'
RAW = ROOT/'资料文件/外部核验/后续补证_20261121'
REPLAY = ROOT/'项目工作区/outputs/ioc_evidence_repair_recompute'
TARGETS = {
    'host_source_sensitivity': ROOT/'交付文件/任务三_专题深挖/S1_东道主效应/01_来源与口径敏感性',
    'dynasty_source_sensitivity': ROOT/'交付文件/任务三_专题深挖/S3_冠军的保质期/11_历史来源敏感性',
    'forecast_same_unit_replay': ROOT/'交付文件/任务四_开放创作/05_满分升级/14_同口径时序重训',
    'project_model_strict_replay': ROOT/'交付文件/任务四_开放创作/05_满分升级/15_原项目模型时序核验',
}
NOTES = {
    'canada_63kg': ('2018-04-19', '加拿大奥委会声明确认Girard获伦敦女子63kg金牌；颁发完成另见2018-12-03报道。', '奥委会直接声明；只覆盖该运动员该奖牌，不认证全项三色。'),
    'iwf_valentin_2019': ('2019-03-05', '伦敦金牌已向Valentín补颁。', '仪式日写3月1日，与西班牙协会2月28日相差一天；文中北京铜/里约银与IWF2025回顾相反，不采这两处颜色。'),
    'spain_valentin': ('正文2019-02-28；网站元数据2020-09-11', '西班牙协会报道IOC委员向Valentín颁发伦敦金牌。', '正文仪式日与IWF报道有一天冲突；只确认已颁金牌，不据此确定精确日或全项颜色。'),
    'iwf_valentin_2025': ('2025-04-07', '回顾列里约女子75kg铜牌、北京递补银牌及伦敦递补金牌。', '历史回顾支持运动员奖牌序列；不是完整现行项目表。伦敦75kg项目身份还与2012结果书及原代理选手身份交叉。'),
    'iwf_three_medals': ('2018-11-08', '报道Gulnoi伦敦女子58kg铜、Mohammadpour伦敦男子94kg金、Ulanov里约男子85kg铜已经补颁。', '支持三条授牌动作；不扩展到各项全部三色。'),
    'iwf_taipei_medals': ('2018-01-29', '图注和正文支持Chen女子48kg北京金、Lu女子63kg北京银，1月25日授牌。', '文章注明来源为中华台北奥委会，属于官方机构转述；总奖牌计数句存在明显范围疑点，不采用、不计独立来源数。'),
}
def main():
    OUT.mkdir(exist_ok=True)
    captures=json.loads((RAW/'获取清单.json').read_text(encoding='utf-8'))
    manifest={x['key']:x for x in captures}
    notes=[]
    for key,(date,fact,boundary) in NOTES.items():
        row=manifest[key]
        if row.get('raw_file'):
            assert hashlib.sha256((ROOT/row['raw_file']).read_bytes()).hexdigest()==row['sha256']
        notes.append(dict(source_key=key,source_url=SOURCES[key],publication_date=date,reviewed_on='2026-11-21',review_method='浏览服务逐段阅读；中文释义，非网页原件',supported_fact=fact,boundary=boundary,raw_file=row.get('raw_file',''),raw_sha256=row.get('sha256',''),capture_state='直接原件已归档' if row.get('raw_file') else '直接访问失败；仅保留阅读记录，未冒充原件'))
    pd.DataFrame(notes).to_csv(OUT/'补证来源与适用范围.csv',index=False,encoding='utf-8-sig')
    (RAW/'逐条阅读范围.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    secondary=pd.read_csv(BASE/'Olympedia独立交叉核验/历史555项独立交叉对照.csv').fillna('')
    correction=[]
    for label,old,correct,noc,kg in [('Heavyweight','Middleweight','Heavyweight','ESP',75),('Middleweight','Heavyweight','Middleweight','CAN',63)]:
        event="Weightlifting Women's "+label
        row=secondary[(secondary.Year==2012)&secondary.Event.eq(event)].iloc[0]
        assert row.Event_olympedia==correct+', Women' and row.Gold_olympedia==noc
        correction.append(dict(Year=2012,Event=event,weight_kg=kg,previous_secondary_event=old+', Women',corrected_secondary_event=row.Event_olympedia,corrected_gold=noc,event_url=row.event_url,reason='原自动匹配对事后奖牌集合赋权过大，交叉配到另一体重级别；改为性别和体重级别硬约束'))
    pd.DataFrame(correction).to_csv(OUT/'两项配对更正记录.csv',index=False,encoding='utf-8-sig')
    checks=[]
    for script,target in TARGETS.items():
        for file in (REPLAY/script).glob('*.csv'):
            if not (target/file.name).exists():continue
            a=pd.read_csv(file).fillna('');b=pd.read_csv(target/file.name).fillna('')
            assert a.shape==b.shape and list(a)==list(b),(script,file.name)
            changed=[];error=0.
            for col in a:
                if a[col].equals(b[col]):continue
                if pd.api.types.is_numeric_dtype(a[col]) and pd.api.types.is_numeric_dtype(b[col]):
                    diff=float((a[col]-b[col]).abs().max())
                    if col!='耗时秒':error=max(error,diff)
                    if diff<1e-8 or col=='耗时秒':continue
                changed.append(col)
            allowed={'替代金牌','来源','previous','current','替代上届','替代本届'} if script=='dynasty_source_sensitivity' else set()
            assert set(changed)<=allowed,(script,file.name,changed)
            checks.append(dict(script=script,file=file.name,rows=len(a),max_numeric_error=error,changed_identity_columns='|'.join(changed),numeric_conclusion_unchanged=True))
            if changed:shutil.copyfile(file,target/file.name)
        # Refresh source fingerprints without rewriting unaffected tables/figures.
        for file in (REPLAY/script).glob('*.json'):
            if (target/file.name).exists():shutil.copyfile(file,target/file.name)
    pd.DataFrame(checks).to_csv(OUT/'四组复算差异核验.csv',index=False,encoding='utf-8-sig')
    summary=dict(corrected_event_pairs=2,reviewed_source_pages=len(notes),archived_direct_responses=sum(bool(n['raw_file']) for n in notes),research_groups_replayed=4,all_numeric_conclusions_unchanged=True,new_complete_ioc_event_certifications=0,scope='修正两处项目身份；正式结果原件未齐的部分继续保留，不把两家一致当作全项现行认证')
    (OUT/'核验摘要.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    body='# 后续补证与项目配对更正（2026-11-21）\n\n'
    body+='本轮发现并修正2012年女子举重63kg和75kg的两处交叉配对。旧存档与Olympedia曾共同配错，因此“548项两家一致”只能说明记录对照，不能证明项目身份或IOC现行认证。匹配现加入性别与体重级别硬约束，45条举重配对全部检查。\n\n'
    body+=pd.DataFrame(correction).to_markdown(index=False)+'\n\n'
    body+='## 新补证及冲突\n\n'
    for n in notes:body+=f"- [{n['source_key']}]({n['source_url']})（{n['publication_date']}）：{n['supported_fact']} {n['boundary']} {n['capture_state']}。\n"
    body+='\n## 对已发表结论的影响\n\n四组研究重新运行：东道主来源敏感性、冠军控制权、同口径岭回归、原RF/GB时序模型。表内数值在1e-8容差内一致；冠军转移附表中的两个项目身份和代表团集合已纠正。固定113项仍下降7.37个百分点，排除后50项区间仍跨零；212队2028条件主榜数值未变。输入哈希与新配对同步更新。\n\n'
    body+='## 尚未闭合\n\n新增完整IOC小项三色认证仍为0。局部颁牌证据不能补全未写出的其他颜色，也不能直接确认2026年的完整现行结果。35项风险仍保留逐项待核状态；俄罗斯摔跤暂缓颁发后续、CAS拳击裁决原PDF、最终资格以及最终预测集成同构回测等未完成边界不撤销。未来预测不可能由历史补证变为百分百确定。\n\n'
    body+='## 复现顺序与下载\n\n先运行historical_ioc_event_audit.py、historical_risk_queue.py、olympedia_secondary_audit.py；四组研究通过recompute_ioc_sensitivity_isolated.py隔离复算；再运行本脚本、publish_ioc_evidence_ledger.py、validate_evidence_closure.py、publish_evidence_closure.py及PDF生成器。fetch_followup_evidence.py只用于首次归档，拒绝覆盖已有原件。原始证据不得进入页面美化脚本。\n'
    (OUT/'补证与更正说明.md').write_text(body,encoding='utf-8')
    import markdown
    template=(BASE/'关键结论闭环_20261120/index.html').read_text(encoding='utf-8')
    style=template[template.index('<style>'):template.index('</style>')+8]
    files=['两项配对更正记录.csv','补证来源与适用范围.csv','四组复算差异核验.csv','核验摘要.json','补证与更正说明.md']
    page='<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>后续补证与项目配对更正</title>'+style+markdown.markdown(body,extensions=['tables'])+'<h2>下载</h2><ul>'+''.join('<li><a href="'+escape(f)+'">'+escape(f)+'</a></li>' for f in files)+'</ul></html>'
    from bs4 import BeautifulSoup
    document=BeautifulSoup(page,'html.parser')
    for table in document.select('table'):
        table.wrap(document.new_tag('div',attrs={'class':'scroll','tabindex':'0','aria-label':'逐项配对更正，可横向查看'}))
    (OUT/'index.html').write_text(str(document),encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False))
if __name__=='__main__':main()
