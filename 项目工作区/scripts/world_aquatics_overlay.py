"""Match federation medal-tagged final records to the 910-event coverage register."""
import difflib
import json
from pathlib import Path

import pandas as pd

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力/08_逐项外部核验'
SOURCE=OUT/'历史910项来源覆盖总表.csv'
AUDIT=OUT/'世界泳联现行奥运水上项目逐项核验.csv'
PREFIX={'Artistic Swimming':'Synchronized Swimming','Open Water Swimming':'Swimming','Swimming':'Swimming','Diving':'Diving','Water Polo':'Water Polo'}

def norm(s):
    s=s.lower().replace('women\'s','women').replace('men\'s','men').replace('metres','m').replace('kilometres','km').replace('synchronized','synchronised').replace('individual medley','medley')
    s=s.replace('open water','openwater').replace('springboard','3m').replace('platform','10m')
    return ''.join(c for c in s if c.isalnum())

def main():
    base=pd.read_csv(SOURCE)
    audit=pd.read_csv(AUDIT)
    pairs=[]
    used=set()
    for _,r in audit.iterrows():
        prefix=PREFIX[r.Sport]
        candidates=base[(base.Year==r.Year)&base.Event.str.startswith(prefix+' ')]
        if r.Sport=='Open Water Swimming':candidates=candidates[candidates.Event.str.contains('Open Water')]
        if r.Sport=='Swimming':candidates=candidates[~candidates.Event.str.contains('Open Water')]
        scores=[]
        for i,c in candidates.iterrows():
            if (r.Year,i) in used:continue
            target=c.Event[len(prefix)+1:]
            if r.Sport=='Diving':
                if ('10m' in r.DisciplineName) != ('Platform' in target):continue
                if ('3m' in r.DisciplineName) != ('Springboard' in target):continue
                if ('Synchronised' in r.DisciplineName) != ('Synchronized' in target):continue
            score=difflib.SequenceMatcher(None,norm(r.DisciplineName),norm(target)).ratio()
            scores.append((score,i,target))
        score,i,target=max(scores)
        if (r.Year,i) in used:raise ValueError(f'duplicate {r.Year} {r.DisciplineName} => {target}')
        used.add((r.Year,i))
        medals=sum(len(json.loads(r[k])) for k in ('Gold','Silver','Bronze'))
        if medals<3:raise ValueError(f'insufficient medals {r.Year} {r.DisciplineName} {medals}')
        pairs.append({'Year':r.Year,'Event':base.loc[i,'Event'],'FederationEvent':r.DisciplineName,'match_score':round(score,3),'medal_count':medals,'SourceURL':r.SourceURL,'SHA256':r.SHA256})
        if score<0.45:print('LOW MATCH',r.Year,r.DisciplineName,'=>',target,round(score,2))
        if r.Year==2012 and r.DisciplineName=="Women's 100m Freestyle":
            base.loc[i,'来源等级']='赛时官方成绩册第13页已裁决：唐奕53.44秒第3，世界泳联当前接口误标第2；现行IOC授牌未核'
            base.loc[i,'来源链接']='https://digital.la84.org/digital/api/collection/p17103coll8/id/84746/download'
            base.loc[i,'来源类型']='官方原始补证（协会接口错误）'
            continue
        base.loc[i,'来源等级']='世界泳联现行奥运决赛成绩；奖牌标签逐项核验；不等同于IOC现行结果'
        base.loc[i,'来源链接']=r.SourceURL
        base.loc[i,'来源类型']='世界泳联现行逐项结果'
    pd.DataFrame(pairs).to_csv(OUT/'世界泳联与910项对照表.csv',index=False,encoding='utf-8-sig')
    base.to_csv(SOURCE,index=False,encoding='utf-8-sig')
    print('matched',len(pairs),'unique',len(used))
    print(base['来源类型'].value_counts().to_string())

if __name__=='__main__':main()
