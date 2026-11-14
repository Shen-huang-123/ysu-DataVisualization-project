"""Audit a supplied current IOC event-level export against the 910-event proxy.

Usage: python current_ioc_import_audit.py --source PATH_TO_OFFICIAL_CSV
The source must contain Year, Event, Gold, Silver, Bronze, official_url and
capture_date. Event names must match the provided event key template; ambiguous
or missing rows remain unverified. No source file means no verification claim.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import pandas as pd

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'交付文件'/'任务三_专题深挖'/'S2_口径的魔力'/'08_逐项外部核验'
BASE=OUT/'历史910项来源覆盖总表.csv'
PROXY=ROOT/'交付文件'/'任务三_专题深挖'/'S2_口径的魔力'/'02_数据表'
REQUIRED=['Year','Event','Gold','Silver','Bronze','official_url','capture_date']

def medals(s):
    return '|'.join(sorted({x.strip().upper() for x in str(s).replace(',','|').split('|') if x.strip() and x.strip().lower()!='nan'}))

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--source',type=Path)
    a=p.parse_args()
    base=pd.read_csv(BASE,dtype=str).fillna('')
    assert len(base)==910 and not base.duplicated(['Year','Event']).any()
    if a.source is None:
        template=base[['Year','Event','来源链接']].rename(columns={'来源链接':'candidate_ioc_url'})
        for col in ['Gold','Silver','Bronze','official_url','capture_date']:
            template[col]=''
        template.to_csv(OUT/'现行IOC逐项导入模板.csv',index=False,encoding='utf-8-sig')
        print('Template written; no current IOC results have been verified.')
        return
    src=pd.read_csv(a.source,dtype=str).fillna('')
    missing=set(REQUIRED)-set(src.columns)
    if missing:raise ValueError(f'Missing columns: {sorted(missing)}')
    src['Year']=src.Year.str.strip();src['Event']=src.Event.str.strip()
    if src.duplicated(['Year','Event']).any():
        raise ValueError('Duplicate Year+Event in supplied IOC source')
    src['source_complete']=src[REQUIRED[2:]].apply(lambda r:all(str(x).strip() for x in r),axis=1)
    src['official_domain']=src.official_url.str.match(r'^https://(www\.)?olympics\.com/|^https://library\.olympics\.com/|^https://stillmed\.olympics\.com/',case=False)
    records=[]
    for year in [2008,2012,2016]:
        proxy=pd.read_csv(PROXY/f'S2_{year}历史小项代理表.csv',dtype=str).fillna('')
        proxy['Year']=str(year)
        records.append(proxy[['Year','Event','Gold','Silver','Bronze']])
    pxy=pd.concat(records,ignore_index=True)
    assert len(pxy)==910 and not pxy.duplicated(['Year','Event']).any()
    z=pxy.merge(src[REQUIRED+['source_complete','official_domain']],on=['Year','Event'],how='left',suffixes=('_proxy','_ioc'),indicator=True)
    for medal in ['Gold','Silver','Bronze']:
        z[medal+'_match']=z.apply(lambda r:medals(r[medal+'_proxy'])==medals(r[medal+'_ioc']) if pd.notna(r[medal+'_ioc']) else False,axis=1)
    z['核验状态']='未提供现行IOC记录'
    good=z['_merge'].eq('both')&z.source_complete.eq(True)&z.official_domain.eq(True)
    z.loc[z['_merge'].eq('both')&~good,'核验状态']='来源字段不完整或非IOC域名'
    z.loc[good&z[['Gold_match','Silver_match','Bronze_match']].all(axis=1),'核验状态']='现行IOC三色一致'
    z.loc[good&~z[['Gold_match','Silver_match','Bronze_match']].all(axis=1),'核验状态']='现行IOC差异待裁决'
    z.to_csv(OUT/'现行IOC逐项导入核验结果.csv',index=False,encoding='utf-8-sig')
    print(z['核验状态'].value_counts().to_string())
    extra=src.merge(pxy[['Year','Event']],on=['Year','Event'],how='left',indicator=True)
    extra=extra[extra['_merge'].eq('left_only')]
    extra.to_csv(OUT/'现行IOC导入未配对记录.csv',index=False,encoding='utf-8-sig')
    print('Unpaired source records:',len(extra))

if __name__=='__main__':main()

