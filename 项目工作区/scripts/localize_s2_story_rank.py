"""Show Chinese delegation names in the S2 scrollytelling ranking."""
from pathlib import Path
import json
import re
from task2_localization import NOC_ZH


def localize_story_html(html: str) -> str:
    match = re.search(r'const data=(\[.*?\]),hist=', html, re.S)
    if not match:
        raise ValueError('S2 ranking data not found')
    codes = {row['NOC'] for row in json.loads(match.group(1))}
    missing = codes - NOC_ZH.keys()
    if missing:
        raise ValueError(f'Untranslated delegation codes: {sorted(missing)}')
    names = json.dumps({code: NOC_ZH[code] for code in sorted(codes)}, ensure_ascii=False, separators=(',', ':'))
    if 'const nocZh=' not in html:
        html = html.replace('const data=', f'const nocZh={names},displayNoc=code=>nocZh[code];const data=', 1)
    html = html.replace('<b>${x.NOC}</b>', '<b title="${x.NOC}">${displayNoc(x.NOC)}</b>')
    if '<b>${x.NOC}</b>' in html:
        raise AssertionError('Raw NOC label remains in S2 ranking')
    return html


if __name__ == '__main__':
    root = Path(__file__).resolve().parents[2]
    page = root/'交付文件/任务三_专题深挖/S2_口径的魔力/06_滚动叙事专题/index.html'
    page.write_text(localize_story_html(page.read_text(encoding='utf-8')), encoding='utf-8')
    print('localized S2 story ranking')
