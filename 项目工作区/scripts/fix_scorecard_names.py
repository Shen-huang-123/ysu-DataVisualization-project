"""Localize the existing 2024 demo table without rebuilding its visual shell."""
from pathlib import Path
import json
import re
from task2_localization import NOC_ZH

root = Path(__file__).resolve().parents[2]
page = root / '交付文件/任务四_开放创作/06_赛后验收单/index.html'
text = page.read_text(encoding='utf-8')
match = re.search(r',D=(\[.*?\]),\$=s=>document\.querySelector\(s\)', text, flags=re.S)
if not match:
    raise RuntimeError('Could not find demo data in scorecard')
rows = json.loads(match.group(1))
missing = sorted({row['code'] for row in rows if row['code'] not in NOC_ZH})
if missing:
    raise RuntimeError(f'Missing Chinese labels: {missing}')
for row in rows:
    row['name'] = NOC_ZH[row['code']]
replacement = json.dumps(rows, ensure_ascii=False, separators=(',', ':'))
page.write_text(text[:match.start(1)] + replacement + text[match.end(1):], encoding='utf-8')
print(f'Localized {len(rows)} historic demo rows')
