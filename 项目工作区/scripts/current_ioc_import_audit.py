"""Audit supplied full-event IOC evidence. Never certify from a URL alone.
Existing decisions, original books and federation results remain separate evidence.
"""
from __future__ import annotations
import argparse,hashlib,re
from datetime import date
from pathlib import Path
from urllib.parse import urlparse
import pandas as pd
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力/08_逐项外部核验'
BASE=OUT/'历史910项来源覆盖总表.csv'
PROXY=OUT.parent/'02_数据表'
REQUIRED=['Year','Event','Gold','Silver','Bronze','official_url','capture_date','source_kind','raw_file','raw_sha256','reviewer','review_date','review_status','medal_scope','Gold_empty_reason','Silver_empty_reason','Bronze_empty_reason']
def medals(value):
    """Keep repeated NOCs: this is a multiset comparison, not athlete verification."""
    return '|'.join(sorted(x.strip().upper() for x in str(value).replace(',','|').split('|') if x.strip() and x.strip().lower()!='nan'))
def validate_source(row,root=ROOT):
    errors=[]
    value=lambda key:str(row.get(key,'')).strip()
    u=urlparse(value('official_url'))
    if u.scheme!='https' or u.hostname not in {'olympics.com','www.olympics.com'} or not re.match(r'^/[a-z]{2}/olympic-games/[^/]+/results/[^/]+/[^/]+/?$',u.path):errors.append('不是IOC逐小项结果地址；新闻、图书馆及附件不等于全项现行结果')
    if value('source_kind')!='current_ioc_event' or value('medal_scope')!='full_event':errors.append('来源类别或奖牌范围不是现行完整小项')
    dates=[]
    for key in ['capture_date','review_date']:
        try:
            d=date.fromisoformat(value(key));dates.append(d)
            if d>date.today():errors.append(key+'不能在未来')
        except ValueError:errors.append(key+'须为有效ISO日期')
    if len(dates)==2 and dates[1]<dates[0]:errors.append('人工复核日期早于采集日期')
    if not value('reviewer') or value('review_status')!='approved':errors.append('缺少明确的人工内容复核')
    raw=(root/value('raw_file')).resolve()
    if not value('raw_file') or not raw.is_relative_to(root.resolve()):errors.append('原件路径不在项目内')
    elif not raw.is_file():errors.append('原件文件不存在')
    elif not re.fullmatch('[a-fA-F0-9]{64}',value('raw_sha256')) or hashlib.sha256(raw.read_bytes()).hexdigest()!=value('raw_sha256').lower():errors.append('原件SHA256不匹配')
    for medal in ['Gold','Silver','Bronze']:
        v=medals(value(medal))
        if not v and not value(medal+'_empty_reason'):errors.append(medal+'空值须解释未授予、撤销或无该色等原因')
        if v and any(not re.fullmatch('[A-Z]{3}',n) for n in v.split('|')):errors.append(medal+'含非法代表团代码格式')
    return errors

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--source',type=Path);parser.add_argument('--output-dir',type=Path,default=OUT);a=parser.parse_args();a.output_dir.mkdir(parents=True,exist_ok=True)
    base=pd.read_csv(BASE,dtype=str).fillna('');assert len(base)==910 and not base.duplicated(['Year','Event']).any()
    if a.source is None:
        template=base[['Year','Event','来源链接']].rename(columns={'来源链接':'candidate_ioc_url'})
        for col in REQUIRED:
            if col not in template:template[col]=''
        template.to_csv(a.output_dir/'现行IOC逐项导入模板.csv',index=False,encoding='utf-8-sig');print('Template only; no evidence upgraded.');return
    src=pd.read_csv(a.source,dtype=str).fillna('')
    if set(REQUIRED)-set(src):raise ValueError('Missing columns: '+str(sorted(set(REQUIRED)-set(src))))
    src['Year']=src.Year.str.strip();src['Event']=src.Event.str.strip()
    if src.duplicated(['Year','Event']).any():raise ValueError('Duplicate Year+Event')
    src['审核问题']=src.apply(lambda r:'；'.join(validate_source(r)),axis=1)
    tables=[]
    for year in [2008,2012,2016]:
        t=pd.read_csv(PROXY/f'S2_{year}历史小项代理表.csv',dtype=str).fillna('');t['Year']=str(year);tables.append(t[['Year','Event','Gold','Silver','Bronze']])
    proxy=pd.concat(tables,ignore_index=True)
    z=proxy.merge(src,on=['Year','Event'],how='left',suffixes=('_proxy','_ioc'),validate='one_to_one',indicator=True)
    for medal in ['Gold','Silver','Bronze']:z[medal+'_match']=z.apply(lambda r:medals(r[medal+'_proxy'])==medals(r[medal+'_ioc']) if r['_merge']=='both' else False,axis=1)
    good=z['_merge'].eq('both')&z['审核问题'].eq('')
    z['核验状态']='未提供完整小项证据';z.loc[z['_merge'].eq('both')&~good,'核验状态']='证据门槛未通过'
    same=z[['Gold_match','Silver_match','Bronze_match']].all(axis=1)
    z.loc[good&same,'核验状态']='已人工复核IOC来源；NOC多重集合一致'
    z.loc[good&~same,'核验状态']='已人工复核IOC来源；奖牌差异待裁决'
    z.to_csv(a.output_dir/'现行IOC逐项导入核验结果.csv',index=False,encoding='utf-8-sig')
    extra=src.merge(proxy[['Year','Event']],on=['Year','Event'],how='left',indicator=True);extra[extra['_merge'].eq('left_only')].to_csv(a.output_dir/'现行IOC导入未配对记录.csv',index=False,encoding='utf-8-sig')
    print(z['核验状态'].value_counts().to_string());print('仅审核导入证据，不覆盖来源总表；原代理仍可能合并同NOC同色多枚。')
if __name__=='__main__':main()
