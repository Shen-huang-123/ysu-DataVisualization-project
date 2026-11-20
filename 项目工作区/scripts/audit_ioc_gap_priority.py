from pathlib import Path
import pandas as pd,json,requests,concurrent.futures,datetime
root=Path(__file__).resolve().parents[2];base=root/'交付文件/任务三_专题深挖/S2_口径的魔力/08_逐项外部核验'
d=pd.read_csv(base/'历史910项来源覆盖总表.csv').fillna('');secondary=pd.read_csv(base/'Olympedia独立交叉核验/历史555项独立交叉对照.csv').fillna('');keys=set(zip(secondary.Year.astype(int),secondary.Event))
current=pd.read_csv(base/'IOC现行奖牌重分配逐项台账.csv').fillna('');known={(int(r.Year),r.Event):r for r in current.itertuples()}
d['属于555项二次对照']=[(int(y),e) in keys for y,e in zip(d.Year,d.Event)]
d['现行结果证据状态']=['已有部分官方台账，仍需逐项审阅' if (int(y),e) in known else '未完成现行IOC三色核验' for y,e in zip(d.Year,d.Event)]
d['赛时成绩册不等于现行结果']='须同时核对取消资格与递补裁决'
d['优先级']=['优先审阅已发现差异' if (int(y),e) in known or s!='三色一致' else '常规核验' for y,e,s in zip(d.Year,d.Event,d.status)]
d.to_csv(base/'现行官方核验缺口与优先级.csv',index=False,encoding='utf-8-sig')
urls=list(dict.fromkeys([str(r.官方决议或决赛页).split(' | ')[0] for r in known.values()]+d['来源链接'].head(4).tolist()))
def probe(u):
 try:
  r=requests.get(u,timeout=15,headers={'User-Agent':'Mozilla/5.0'});return {'url':u,'status':r.status_code,'bytes':len(r.content),'final_url':r.url,'verified_medals':False}
 except Exception as e:return {'url':u,'error':str(e),'verified_medals':False}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:results=list(ex.map(probe,urls))
report={'date':'2026-11-20','historical_events':len(d),'secondary_subset':int(d['属于555项二次对照'].sum()),'existing_partial_ledger':len(known),'probes':results,'new_current_three_medal_verifications':0,'scope':'HTTP成功不等于奖牌核验；原成绩册不等于现行裁决后结果；未修改主数据'}
(base/'官方候选链接直接访问检查.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(report,ensure_ascii=False))
