from pathlib import Path
import json
import re
import subprocess
import tempfile

ROOT=Path(__file__).resolve().parents[2]
page=ROOT/'交付文件'/'任务四_开放创作'/'01_交互式Dashboard'/'index.html'
text=page.read_text(encoding='utf-8')
names=json.loads(text.split('const nocZh=')[1].split(';const displayNoc=')[0])
rows=json.loads(text.split('const 数据=')[1].split(',情景=')[0])
assert {x['NOC'] for x in rows} <= names.keys()
assert all(re.search('[\u4e00-\u9fff]',names[x['NOC']]) for x in rows)
assert '<b title="${x.NOC}">${displayNoc(x.NOC)}</b>' in text
assert '<strong title="${x.NOC}">${displayNoc(x.NOC)}</strong>' in text
assert 'placeholder="搜索中文名称或代码"' in text
assert 'placeholder="如 中国、美国"' in text
assert text.count('id="xz-dashboard-local"')==1
scripts='\n'.join(re.findall(r'<script(?: [^>]*)?>(.*?)</script>',text,re.S))
with tempfile.TemporaryDirectory() as temp:
    script=Path(temp)/'dashboard.js';script.write_text(scripts,encoding='utf-8')
    result=subprocess.run(['node','--check',str(script)],capture_output=True,text=True)
    assert result.returncode==0,result.stderr
print(json.dumps({'passed':True,'delegations':len(names),'forecast_rows':len(rows)},ensure_ascii=False))
