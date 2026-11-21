"""Archive new primary-source responses without overwriting earlier captures.

HTTP success is not content certification. Browser reading and scope are recorded
separately in the correction report; a denied response is never evidence.
"""
from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor
import hashlib, json, requests
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT/'资料文件/外部核验/后续补证_20261121'
SOURCES = {
    'canada_63kg': 'https://olympic.ca/press/canadian-weightlifter-christine-girard-to-be-awarded-london-2012-olympic-gold/',
    'iwf_valentin_2019': 'https://iwf.sport/2019/03/05/lidia-valentin-recieved-olympic-gold-medal/',
    'spain_valentin': 'https://www.fedehalter.org/lydia-valentin-ha-recibido-por-fin-su-medalla-de-oro-de-londres-2012/',
    'iwf_valentin_2025': 'https://iwf.sport/2025/04/07/iwf120y-56-2016-the-first-third-olympic-medal-for-lydia-valentin/',
    'iwf_three_medals': 'https://iwf.sport/2018/11/08/three-lifters-awarded-olympic-medals/',
    'iwf_taipei_medals': 'https://iwf.sport/2018/01/29/olympic-medals-awarded-to-wei-ling-chen-and-ying-chi-lu/',
}
def fetch(item):
    key, url = item
    row = dict(key=key, url=url, attempted_utc=datetime.now(timezone.utc).isoformat())
    try:
        response = requests.get(url, timeout=(8, 20))
        row.update(status=response.status_code, final_url=response.url, bytes=len(response.content))
        valid = response.ok and len(response.content)>1500 and not any(x in response.content[:5000] for x in [b'Access Denied', b'Just a moment...', b'cf-chl-'])
        if valid:
            path = OUT/'原始页面'/(key+'.html')
            path.write_bytes(response.content)
            row.update(raw_file=str(path.relative_to(ROOT)), sha256=hashlib.sha256(response.content).hexdigest(), capture='original response; requires scoped content review')
        else:
            row['capture'] = 'failed or challenge; not primary evidence archive'
    except requests.RequestException as exc:
        row.update(capture='request failed; not evidence', error=str(exc))
    return row
if __name__ == '__main__':
    manifest = OUT/'获取清单.json'
    if manifest.exists():
        raise SystemExit('Capture already exists; use a new dated directory to preserve evidence.')
    (OUT/'原始页面').mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(max_workers=4) as pool:
        rows = list(pool.map(fetch, SOURCES.items()))
    manifest.write_text(json.dumps(rows, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(rows, ensure_ascii=False, indent=2))
