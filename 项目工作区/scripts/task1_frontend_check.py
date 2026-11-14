from pathlib import Path
import json,re
from task1_localization import STATUS_DISPLAY,RULE_DISPLAY,sport_display
from task2_localization import NOC_ZH

ROOT=Path(__file__).resolve().parents[2]
page=ROOT/'交付文件'/'任务一_数据体检'/'index.html'
text=page.read_text(encoding='utf-8')
data=json.loads(text.split('const D=')[1].split(';const $=')[0])
assert all(x['event_status_zh']==STATUS_DISPLAY[x['event_status']] for x in data['status'])
assert all(x['Sport_zh']==sport_display(x['Sport']) and x['sport_family_zh']==sport_display(x['sport_family']) and x['rule_zh']==RULE_DISPLAY[x['rule']] for x in data['mapping'])
assert all(x['delegation']==NOC_ZH[x['NOC']] for x in data['compare'])
assert 'esc(x.event_status_zh)' in text
assert 'esc(x.Sport_zh)' in text and 'esc(x.sport_family_zh)' in text and 'esc(x.rule_zh)' in text
assert 'esc(x.delegation)' in text and '<b>${esc(x.NOC)}</b>' not in text
assert '输入代码或英文名称' not in text and '例如：Basketball' not in text
assert "left.append(...cards.slice(0,mid))" in text and "right.append(...cards.slice(mid))" in text
assert '#qc-list .xz-qc-col{display:flex;flex-direction:column' in text
assert (ROOT/'项目工作区'/'sites'/'la28-fullscore'/'dist'/'任务一_数据体检'/'index.html').read_text(encoding='utf-8')==text
print(json.dumps({'passed':True,'statuses':len(data['status']),'sport_mappings':len(data['mapping']),'delegations':len(data['compare'])},ensure_ascii=False))
