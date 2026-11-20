"""Read-only audit of saved IOC-related evidence. Never upgrades source grades."""
from pathlib import Path
import hashlib,json,subprocess
import pandas as pd
ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力/08_逐项外部核验'
OUT=BASE/'证据链问题核查_20261120'
def sha(b):return hashlib.sha256(b).hexdigest()
def main():
    base=pd.read_csv(BASE/'历史910项来源覆盖总表.csv').fillna('')
    secondary=pd.read_csv(BASE/'Olympedia独立交叉核验/历史555项独立交叉对照.csv').fillna('')
    manifest=pd.read_csv(BASE/'Olympedia独立交叉核验/原始页面清单.csv').fillna('')
    records=[]
    for row in manifest.to_dict('records'):
        relative=row['file'].replace('\\','/')
        path=ROOT/relative
        current=sha(path.read_bytes()) if path.exists() else ''
        first=subprocess.check_output(['git','log','--diff-filter=A','--format=%H','--',relative],cwd=ROOT,text=True).splitlines()[0]
        original=subprocess.check_output(['git','show',first+':'+relative],cwd=ROOT)
        records.append({'file':relative,'expected_sha256':row['sha256'],'current_sha256':current,'current_matches':current==row['sha256'],'original_commit':first,'original_matches':sha(original)==row['sha256']})
    labels={}
    for year in [2008,2012,2016]:
        table=pd.read_csv(BASE.parent/'02_数据表'/f'S2_{year}历史小项代理表.csv').fillna('')
        labels[str(year)]=int(table.provenance.str.contains('IOC官方届次结果页核验',regex=False).sum())
    result={'scope':'本地已保存证据检查，不代表2026-11-20重新访问IOC官网','event_rows':len(base),'unique_event_keys':len(base[['Year','Event']].drop_duplicates()),'source_types':{str(k):int(v) for k,v in base['来源类型'].value_counts().items()},'secondary_rows':len(secondary),'secondary_results':{str(k):int(v) for k,v in secondary['对照结果'].value_counts().items()},'raw_pages':len(records),'raw_hash_matches':sum(r['current_matches'] for r in records),'recoverable_original_hash_matches':sum(r['original_matches'] for r in records),'overstated_provenance_rows':labels,'raw_files':records}
    OUT.mkdir(exist_ok=True)
    (OUT/'核查结果.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='raw_files'},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
