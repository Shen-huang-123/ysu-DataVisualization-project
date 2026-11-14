"""Capture current World Aquatics Olympic final medal results, with raw JSON and hashes."""
import concurrent.futures as cf
import hashlib
import json
import re
from pathlib import Path

import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / '交付文件/任务三_专题深挖/S2_口径的魔力/08_逐项外部核验'
RAW = ROOT / '资料文件/外部核验/世界泳联现行结果JSON'
RAW.mkdir(parents=True, exist_ok=True)
COMPETITIONS = {2008: 657, 2012: 468, 2016: 262}

def get_one(t):
    year, sport, name, eid = t
    url = f'https://api.worldaquatics.com/fina/events/{eid}'
    r = requests.get(url, timeout=35)
    r.raise_for_status()
    content = r.content
    (RAW / f'{year}_{eid}.json').write_bytes(content)
    data = r.json()
    finals = [h for h in data.get('Heats', []) if 'final' in str(h.get('Name','')).lower() and 'semi' not in str(h.get('Name','')).lower()]
    finals.sort(key=lambda h: len(h.get('Results', [])), reverse=True)
    if not finals:
        raise ValueError(f'No final: {year} {sport} {name}')
    result = finals[0]
    medals = {}
    for x in result.get('Results', []):
        tag = x.get('MedalTag')
        if tag in ('G','S','B'):
            medals.setdefault(tag, []).append({'NOC': x.get('NAT'), 'name': x.get('FullName'), 'rank': x.get('Rank')})
    return {'Year':year,'Sport':sport,'DisciplineName':name,'EventId':eid,'SourceURL':url,
            'PageURL':f'https://www.worldaquatics.com/competitions/{COMPETITIONS[year]}/results?event={eid}&unit=final',
            'SHA256':hashlib.sha256(content).hexdigest(),'FinalName':result.get('Name'),
            'Gold':json.dumps(medals.get('G',[]),ensure_ascii=False),
            'Silver':json.dumps(medals.get('S',[]),ensure_ascii=False),
            'Bronze':json.dumps(medals.get('B',[]),ensure_ascii=False),
            'MedalTagsComplete':all(medals.get(k) for k in ('G','S','B'))}

def main():
    tasks=[]
    for year,cid in COMPETITIONS.items():
        r=requests.get(f'https://api.worldaquatics.com/fina/competitions/{cid}/events',timeout=35)
        r.raise_for_status()
        (RAW/f'{year}_competition_events.json').write_bytes(r.content)
        for sport in r.json()['Sports']:
            for d in sport['DisciplineList']:
                tasks.append((year,sport['Name'],d['DisciplineName'],d['Id']))
    with cf.ThreadPoolExecutor(max_workers=10) as pool:
        rows=list(pool.map(get_one,tasks))
    df=pd.DataFrame(rows).sort_values(['Year','Sport','DisciplineName'])
    df.to_csv(OUT/'世界泳联现行奥运水上项目逐项核验.csv',index=False,encoding='utf-8-sig')
    print('rows',len(df),'complete',df.MedalTagsComplete.sum())
    print(df.groupby(['Year','Sport']).size().to_string())
    print('incomplete',df.loc[~df.MedalTagsComplete,['Year','Sport','DisciplineName']].to_string(index=False))

if __name__=='__main__':main()
