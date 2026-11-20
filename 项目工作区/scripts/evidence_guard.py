"""Keep downloaded research evidence outside presentation post-processing."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
PROTECTED=ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力/08_逐项外部核验'
def is_raw_evidence(path):
    # All external-audit HTML are source archives, not presentation pages.
    resolved=Path(path).resolve()
    return resolved.is_relative_to(PROTECTED.resolve()) or any(part in {'原始页面','原始HTML','原始JSON','原始响应'} for part in resolved.parts)
def presentation_html(root):
    return (p for p in Path(root).rglob('*.html') if not is_raw_evidence(p))
def verify_olympedia():
    import csv
    base=PROTECTED/'Olympedia独立交叉核验'
    with (base/'原始页面清单.csv').open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f))
    bad=[]
    for row in rows:
        p=ROOT/row['file'].replace('\\','/')
        if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=row['sha256']:bad.append(str(p))
    if bad:raise ValueError('原始证据哈希失败，禁止使用或重写来源清单：'+json.dumps(bad,ensure_ascii=False))
    return len(rows)
if __name__=='__main__':print('Original evidence SHA256 verified:',verify_olympedia())
