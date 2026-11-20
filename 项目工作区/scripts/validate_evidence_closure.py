"""Close risk triage and publication validation without inventing complete IOC evidence."""
from pathlib import Path
from collections import Counter
import ast,hashlib,json,re
import numpy as np
import pandas as pd
ROOT=Path(__file__).resolve().parents[2]
E=ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力/08_逐项外部核验'
T4=ROOT/'交付文件/任务四_开放创作'
OUT=E/'关键结论闭环_20261120'
MODEL=T4/'05_满分升级/15_原项目模型时序核验'
REPLAY=ROOT/'项目工作区/outputs/ioc_evidence_repair_recompute/project_model_strict_replay'
def code_set(s):return set(re.findall(r'\b[A-Z]{3}\b',str(s)))
def main():
    OUT.mkdir(exist_ok=True)
    script=ROOT/'项目工作区/scripts/project_model_strict_replay.py'
    class Redirect(ast.NodeTransformer):
        def visit_Assign(self,node):
            if any(isinstance(t,ast.Name) and t.id=='OUT' for t in node.targets):node.value=ast.Call(func=ast.Name(id='Path',ctx=ast.Load()),args=[ast.Constant(str(ROOT/'项目工作区/outputs/ioc_closure_model_setup'))],keywords=[])
            return self.generic_visit(node)
    tree=Redirect().visit(ast.parse(script.read_text(encoding='utf-8')));ast.fix_missing_locations(tree)
    ns={'__name__':'audit_setup','__file__':str(script)};exec(compile(tree,str(script),'exec'),ns)
    table=ns['sources']['小项二次来源'];totals=table.groupby(['Year','NOC']).records.sum().reset_index();pool=ns['candidate_pool'](2028);years=ns['years_by']['小项二次来源']
    base=pd.Series(ns['baseline'](totals,years,2028,pool)*1120,index=pool)
    forecast=pd.read_csv(MODEL/'2028同口径重训情景榜.csv').set_index('NOC');assert np.max(np.abs(base-forecast['历史加权基线'].reindex(pool)))<1e-8
    queue=pd.read_csv(E/'历史555项风险优先核验清单.csv').fillna('');queue=queue[queue['优先级'].eq(1)]
    secondary=pd.read_csv(E/'Olympedia独立交叉核验/历史555项独立交叉对照.csv').fillna('')
    risk=queue.merge(secondary[['Year','Event','Gold_olympedia','Silver_olympedia','Bronze_olympedia','对照结果','event_url']],on=['Year','Event'],validate='one_to_one');assert len(risk)==35
    actions=pd.read_csv(E/'IOC决议补证_20261117/IOC逐奖牌动作与现有记录对照.csv').fillna('');action_keys=set(zip(actions.Year,actions.Event))
    transfers=pd.read_csv(ROOT/'交付文件/任务三_专题深挖/S3_冠军的保质期/11_历史来源敏感性/受影响控制权转移.csv')
    for index,row in risk.iterrows():
        proxy=Counter();revision=Counter()
        for med in ['Gold','Silver','Bronze']:
            proxy.update(code_set(row[med+'_proxy']));revision.update(code_set(row[med+'_olympedia']))
        delta=Counter(proxy);delta.subtract(revision)
        t=totals.copy()
        for noc,value in delta.items():
            if not value:continue
            key=t.Year.eq(row.Year)&t.NOC.eq(noc)
            if key.any():t.loc[key,'records']+=value
            else:t=pd.concat([t,pd.DataFrame([dict(Year=row.Year,NOC=noc,records=value)])],ignore_index=True)
        assert t.records.ge(0).all()
        alt=pd.Series(ns['baseline'](t,years,2028,pool)*1120,index=pool)
        effect=float((alt-base).abs().max());rank=int((alt.round(10).rank(method='min',ascending=False)-base.round(10).rank(method='min',ascending=False)).abs().max())
        gold_changed=code_set(row.Gold_proxy)!=code_set(row.Gold_olympedia)
        missing=any(not code_set(row[m+'_archive']) for m in ['Gold','Silver','Bronze'])
        risk.loc[index,'原代理金牌集合改变']=gold_changed
        risk.loc[index,'旧存档缺奖牌字段']=missing
        risk.loc[index,'已有IOC局部动作']=(row.Year,row.Event) in action_keys
        risk.loc[index,'单项退回原代理_2028基准最大变化']=effect
        risk.loc[index,'单项退回原代理_最大名次变化']=rank
        risk.loc[index,'影响范围']='单项反事实、1120固定池、同一212队基准；非因果、非全模型重训，不能相加'
        risk.loc[index,'问题类型']='旧存档缺字段或事后变化' if row['对照结果']!='三色与旧存档一致' else '原代理与两份后续记录不同'
        risk.loc[index,'原始证据补证状态']='已完成二次来源重解析；不据此认证完整IOC结果'
        note='仍需逐色现行证据；无新原件不自动改数值'
        source=row.event_url
        if (row.Year,row.Event) in action_keys:
            note='已有IOC局部动作，须保留日期与限制；完整现行三色仍未闭合'
            source=' | '.join(actions[(actions.Year==row.Year)&(actions.Event==row.Event)].source_url.unique())
        if row.Event.startswith('Weightlifting'):
            note+='；IWF复检页支持取消资格背景，不决定奖牌递补'
            source+=' | https://iwf.sport/anti-doping/reanalysis/'
        if row.Event=="Weightlifting Women's Middleweight":
            note+='；加拿大奥委会原页确认Girard的2008铜牌和2012金牌，非全项认证'
            source+=' | https://olympic.ca/press/christine-girard-awarded-london-2012-and-beijing-2008-medals/'
        if row.Year==2008 and row.Event=="Wrestling Men's Super-Heavyweight, Freestyle":
            note+='；新归档UWW2017排名支持RUS金牌，仍非IOC现行完整认证';source+=' | https://uww.org/articles/ioc-sanctions-wrestlers-failing-anti-doping-test-beijing-2008'
        if row.Year==2012 and row.Event=="Wrestling Men's Super-Heavyweight, Freestyle":
            note+='；UWW2019银牌表述已被IOC2021并列金牌决定更新；俄选手附暂缓颁发条件，后续实际颁发未确认'
        if row.Year==2016:note+='；里约拳击原银牌被撤销不等于已决定递补；CAS地址本轮未返回PDF原件'
        risk.loc[index,'逐项裁定与未决点']=note;risk.loc[index,'追溯链接']=source
        related=transfers[transfers.Event.eq(row.Event)&(transfers.from_year.eq(row.Year)|transfers.to_year.eq(row.Year))]
        risk.loc[index,'关联冠军转移行数']=len(related)
        risk.loc[index,'关联卫冕判定变化行数']=int(related['原卫冕'].ne(related['替代卫冕']).sum())
        risk.loc[index,'东道主影响边界']='已在555项整体替换及排除检验中考察；未逐项因果归因'
        risk.loc[index,'新优先顺序']=1 if gold_changed else 2 if effect>1e-8 or len(related) else 3
    risk=risk.sort_values(['新优先顺序','单项退回原代理_2028基准最大变化','Year','Event'],ascending=[True,False,True,True]);risk.to_csv(OUT/'35项风险重排与影响.csv',index=False,encoding='utf-8-sig')
    comparisons=[]
    for name in ['2028同口径重训情景榜.csv','原模型五方案评分.csv','2028未归一项目格预测.csv','原模型逐队误差.csv']:
        a=pd.read_csv(REPLAY/name).fillna('');b=pd.read_csv(MODEL/name).fillna('');ok=a.shape==b.shape and list(a)==list(b);error=0.
        if ok:
            for col in a:
                if pd.api.types.is_numeric_dtype(a[col]) and pd.api.types.is_numeric_dtype(b[col]):
                    diff=float((a[col].astype(float)-b[col].astype(float)).abs().max());error=max(error,diff);ok=ok and diff<1e-8
                else:ok=ok and a[col].equals(b[col])
        comparisons.append(dict(file=name,rows=len(a),matches=bool(ok),max_numeric_error=error))
    assert all(x['matches'] for x in comparisons),comparisons
    cells=pd.read_csv(REPLAY/'2028未归一项目格预测.csv');assert cells.Year.eq(2028).all() and cells.实际.isna().all()
    audit=pd.read_csv(REPLAY/'逐折选择与训练边界.csv');strict=audit[audit['选择规则'].eq('仅此前届次')];assert (strict['训练最大届']<strict.Year).all() and (strict['选择数据最大届']<strict.Year).all()
    legacy=pd.read_csv(T4/'05_满分升级/11_官方来源门控预测/LA2028审慎来源门控预测榜.csv').set_index('NOC')
    raw=.45*legacy.forecast_total_neutral+.45*legacy.ml_project_forecast+.1*(legacy.forecast_total_neutral+legacy['已核验排名奖励'])
    raw.loc['USA']*=1+float(legacy.synthetic_control_host_rate.iloc[0])*.55
    legacy_rebuilt=raw/raw.sum()*legacy.forecast_total_programme.sum();formula_error=float((legacy_rebuilt-legacy['审慎集成预测']).abs().max());assert formula_error<1e-8
    matrices=[('当前2028中性主榜','212队榜单与固定1120条件池复算','通过','原主榜逐队一致，不代表1120是官方规模'),('RF/GB与55/45情景','原参数三来源三折严格年份回放','通过（事后回放）','小项2024混合误差略高；不宣称权重稳定最优'),('时间边界','筛选和训练早于目标届','通过','事后修订数据不是逐届真实赛前冻结版本'),('项目格下载','只导出2028，实际标签全空','通过（已修生成器）','原脚本全流程会混入历史折；本轮修复'),('旧排名门控集成','实际发布127队公式重构','通过（算术）','45/45/10、美国主场与归一化可重现，不等于预测能力验证'),('新增运动排名','五运动统一事前快照与奥运资格','未完成','已有排名核验和类比，缺同构历史参赛结构与全套冻结输入'),('主场加成','该最终集成中主场增量的独立外推验证','未完成','历史主办关联及来源敏感性不是该增量的独立验证'),('资格规则','最终资格名单和政策','情景','不能把竞技排名直接当资格；2028最终身份未定'),('80%区间','发布新基准及完整集成的同构留出覆盖率','未通过认证','旧lower80/upper80沿袭旧基线，不能套到新主榜或集成'),('完整最终集成','同源单位、冻结排名、主场、资格及区间的联合历史验证','未完成','保留为条件实验；不宣称已完成完整端到端回测')]
    pd.DataFrame(matrices,columns=['对象','核验问题','结论','适用边界']).to_csv(OUT/'最终预测验证矩阵.csv',index=False,encoding='utf-8-sig')
    score=pd.read_csv(REPLAY/'原模型五方案评分.csv');score=score[score.来源.eq('小项二次来源')&score.选择规则.eq('仅此前届次')&score.模型.isin(['历史加权基线','55基线45项目'])];score.to_csv(OUT/'实际模型基线对比.csv',index=False,encoding='utf-8-sig')
    summary=dict(risk_events=len(risk),gold_changes=int(risk['原代理金牌集合改变'].sum()),baseline_sensitive_events=int(risk['单项退回原代理_2028基准最大变化'].gt(1e-8).sum()),risk_order={str(k):int(v) for k,v in risk['新优先顺序'].value_counts().items()},maximum_one_event_baseline_change=float(risk['单项退回原代理_2028基准最大变化'].max()),model_comparisons=comparisons,legacy_formula_max_error=formula_error,forecast_cells=len(cells),forecast_only_2028=True,new_complete_ioc_certifications=0,full_ensemble_historical_validation='未完成；本轮完成可复现性和证据适用范围核验',input_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [E/'历史555项风险优先核验清单.csv',E/'Olympedia独立交叉核验/历史555项独立交叉对照.csv',MODEL/'2028同口径重训情景榜.csv',script]})
    (OUT/'闭环核验摘要.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(summary,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
