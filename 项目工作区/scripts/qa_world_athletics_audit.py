from pathlib import Path
import hashlib
import pandas as pd

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'交付文件'/'任务三_专题深挖'/'S2_口径的魔力'/'08_逐项外部核验'
d=pd.read_csv(OUT/'世界田联现行奥运田径逐项核验.csv',dtype=str).fillna('')
assert len(d)==138 and not d.duplicated(['Year','Event']).any()
assert d.http_status.eq('200').all()
assert d.status.str.startswith('世界田联现行决赛三色已抽取').all()
assert d.official_url.str.startswith('https://worldathletics.org/').all()
assert d.Gold_current.ne('').all() and d.Silver_current.ne('').all()
for r in d.itertuples(index=False):
    raw=(ROOT/r.saved_html).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==r.html_sha256,(r.Year,r.Event)
    assert b'<html' in raw.lower() and b'worldathletics' in raw.lower()
special=d[d.status.str.contains('并列银牌')]
assert set(zip(special.Year,special.Event))=={
    ('2008',"Athletics Women's 100 metres"),
    ('2012',"Athletics Men's High Jump"),
}
base=pd.read_csv(OUT/'历史910项来源覆盖总表.csv',dtype=str).fillna('')
assert len(base)==910 and base['来源类型'].eq('世界田联现行竞赛结果').sum()==138
assert base['来源类型'].eq('Olympics.com第三方2023抓取存档').sum()==555
print('QA PASS: 138 unique current-federation pages, hashes and ties; 910 coverage rows')
