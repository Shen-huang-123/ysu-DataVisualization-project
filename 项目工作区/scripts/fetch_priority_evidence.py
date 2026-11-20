"""Archive direct primary-source responses; failed access never counts as evidence."""
from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,requests
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'资料文件/外部核验/高风险补证_20261120';RAW=OUT/'原始页面'
SOURCES={
'iwf_reanalysis':'https://iwf.sport/anti-doping/reanalysis/',
'canada_girard':'https://olympic.ca/press/christine-girard-awarded-london-2012-and-beijing-2008-medals/',
'uww_2008':'https://uww.org/articles/ioc-sanctions-wrestlers-failing-anti-doping-test-beijing-2008',
'uww_2019':'https://uww.org/articles/ioc-determines-taymazov-fails-london-re-test',
'iwf_hsu':'https://iwf.sport/2018/06/13/hsu-shu-ching-two-time-olympic-champion-announced-her-retirement/',
'ioc_2021':'https://www.olympics.com/ioc/news/ioc-executive-board-approves-medal-reallocations-from-olympic-games-london-2012-and-pyeongchang-2018',
'cas_aloyan':'https://jurisprudence.tas-cas.org/Shared%20Documents/4927.pdf',
'iwf_2008_index':'https://iwf.sport/results/results-by-events/results-by-events-upto2018/?event_year=2008',
'iwf_2012_index':'https://iwf.sport/results/results-by-events/results-by-events-upto2018/?event_year=2012'}
def fetch(item):
    key,url=item;row=dict(key=key,url=url,attempt_utc=datetime.now(timezone.utc).isoformat())
    try:
        r=requests.get(url,timeout=(7,16));row.update(http_status=r.status_code,final_url=r.url,bytes=len(r.content))
        valid=(not url.lower().endswith('.pdf') or r.content.startswith(b'%PDF')) and r.ok and len(r.content)>1500 and b'Access Denied' not in r.content[:3000] and b'Just a moment...' not in r.content[:3000]
        if valid:
            f=RAW/(key+('.pdf' if r.content.startswith(b'%PDF') else '.html'));f.write_bytes(r.content);row.update(raw_file=str(f.relative_to(ROOT)),sha256=hashlib.sha256(r.content).hexdigest(),capture='direct response archived; scope requires content review')
        else:row['capture']='access failed or challenge; not evidence'
    except Exception as e:row.update(capture='request failed; not evidence',error=str(e))
    tokens={'canada_girard':[b'Girard',b'2012',b'2008'],'uww_2008':[b'TAYMAZOV',b'2008',b'Gold:'],'uww_2019':[b'TAYMAZOV',b'2012',b'Gold:']}
    row['accepted_primary_content']=bool(row.get('raw_file') and key in tokens and all(t in (ROOT/row['raw_file']).read_bytes() for t in tokens[key]))
    return row
if __name__=='__main__':
    RAW.mkdir(parents=True,exist_ok=True)
    with ThreadPoolExecutor(max_workers=5) as pool:rows=list(pool.map(fetch,SOURCES.items()))
    (OUT/'获取清单.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(rows,ensure_ascii=False,indent=2))
