"""Independently compare old-only historical events to live Olympedia tables.

Olympedia is a specialist SECONDARY source. A match here is never labeled as a
current IOC medal award. Raw pages and SHA256 hashes are retained for review.
"""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path
import hashlib
import json
import re
import time

from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests
from scipy.optimize import linear_sum_assignment

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / '交付文件/任务三_专题深挖/S2_口径的魔力/08_逐项外部核验'
QUEUE = BASE / '历史555项风险优先核验清单.csv'
OUT = BASE / 'Olympedia独立交叉核验'
RAW = OUT / '原始页面'
RAW.mkdir(parents=True, exist_ok=True)
EDITION = {2008: 53, 2012: 54, 2016: 59}


def sport_group(name: str) -> str:
    if name.startswith('Cycling '): return 'Cycling'
    if name.startswith('Canoe '): return 'Canoeing'
    if name.startswith('Equestrian '): return 'Equestrianism'
    if name == 'Artistic Gymnastics': return 'Gymnastics'
    if name == 'Rhythmic Gymnastics': return 'Rhythmic Gymnastics'
    if name == 'Beach Volleyball': return 'Beach Volleyball'
    if name == 'Rugby Sevens': return 'Rugby Sevens'
    return name


def fetch(url: str, filename: Path) -> tuple[bytes, str]:
    if filename.exists():
        data = filename.read_bytes()
    else:
        err = None
        for attempt in range(6):
            try:
                response = requests.get(url, timeout=30, headers={'User-Agent': 'OlympicResearchAudit/1.0 (academic data verification)'})
                response.raise_for_status()
                data = response.content
                filename.write_bytes(data)
                break
            except Exception as exc:
                err = exc
                time.sleep(5 * (attempt + 1))
        else:
            raise RuntimeError(f'{url}: {err}')
    return data, hashlib.sha256(data).hexdigest()


def normal(s: str) -> str:
    s = str(s).lower().replace('women\'s', 'women').replace('men\'s', 'men')
    s = s.replace('metres', 'm').replace('meters', 'm').replace('kilometres', 'km')
    s = s.replace('synchronised', 'synchronized').replace('light-heavyweight', 'light heavyweight')
    s = s.replace('super-heavyweight', 'super heavyweight')
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()


def sex(s: str) -> str:
    w = normal(s).split()
    if 'women' in w: return 'women'
    if 'men' in w: return 'men'
    return 'mixed'


def codes(s: str) -> set[str]:
    return {x.strip() for x in str(s).split('|') if x.strip() and x.strip().lower() != 'nan'}


def token_set_ratio(a: str, b: str) -> float:
    aa, bb = set(a.split()), set(b.split())
    shared = aa & bb
    if not shared: return 0.0
    common = ' '.join(sorted(shared))
    a_full = common + ' ' + ' '.join(sorted(aa-shared))
    b_full = common + ' ' + ' '.join(sorted(bb-shared))
    return 100 * max(SequenceMatcher(None, common, a_full).ratio(), SequenceMatcher(None, common, b_full).ratio(), SequenceMatcher(None, a_full, b_full).ratio())


def sailing_alias(year: int, event: str) -> str | None:
    """Resolve legacy proxy labels against 470/Finn/49er programme labels."""
    if event == "Sailing Men's Two Person Dinghy": return 'Two-Person Dinghy, Open'
    if year == 2008 and event == 'Sailing Mixed One Person Dinghy': return 'One-Person Heavyweight Dinghy, Men'
    if year == 2008 and event == 'Sailing Mixed Skiff': return 'Skiff, Men'
    return None


def parse_sport(data: bytes, year: int, sport: str, url: str, sha: str) -> list[dict]:
    soup = BeautifulSoup(data, 'html.parser')
    rows = []
    for table in soup.find_all('table'):
        heads = [th.get_text(' ', strip=True) for th in table.find_all('th')]
        if heads[:4] != ['Event', 'Gold', 'Silver', 'Bronze']:
            continue
        for tr in table.find_all('tr'):
            cells = tr.find_all('td', recursive=False)
            if len(cells) != 7: continue
            event_link = cells[0].find('a', href=re.compile(r'^/results/'))
            if not event_link: continue
            medal = []
            for cell in (cells[2], cells[4], cells[6]):
                noc = [a.get_text(' ', strip=True) for a in cell.find_all('a', href=re.compile(r'^/countries/'))]
                medal.append('|'.join(sorted(set(noc))))
            rows.append({'Year': year, 'Sport': sport, 'Event_olympedia': event_link.get_text(' ', strip=True),
                         'Gold_olympedia': medal[0], 'Silver_olympedia': medal[1], 'Bronze_olympedia': medal[2],
                         'event_url': 'https://www.olympedia.org' + event_link['href'],
                         'sport_url': url, 'page_sha256': sha})
        break
    return rows


def main() -> None:
    queue = pd.read_csv(QUEUE, dtype=str).fillna('')
    assert len(queue) == 555 and not queue.duplicated(['Year', 'Event']).any()
    wanted = {(int(y), sp) for y, sp in zip(queue.Year, queue.Sport)}
    tasks = []
    for year, edition in EDITION.items():
        url = f'https://www.olympedia.org/editions/{edition}'
        data, _ = fetch(url, RAW / f'{year}_edition.html')
        soup = BeautifulSoup(data, 'html.parser')
        for a in soup.find_all('a', href=re.compile(fr'^/editions/{edition}/sports/')):
            name = a.get_text(' ', strip=True)
            group = sport_group(name)
            if (year, group) in wanted:
                tasks.append((year, group, 'https://www.olympedia.org' + a['href'], RAW / f'{year}_{a["href"].rstrip("/").split("/")[-1]}.html'))
    tasks = list(dict.fromkeys(tasks))
    source_rows = []
    manifest = []
    with ThreadPoolExecutor(max_workers=2) as pool:
        jobs = {pool.submit(fetch, url, file): (year, group, url, file) for year, group, url, file in tasks}
        for job in as_completed(jobs):
            year, group, url, file = jobs[job]
            data, sha = job.result()
            parsed = parse_sport(data, year, group, url, sha)
            source_rows.extend(parsed)
            manifest.append({'Year': year, 'Sport': group, 'url': url, 'file': str(file.relative_to(ROOT)),
                             'sha256': sha, 'bytes': len(data), 'medal_events': len(parsed)})
            print(f'{year} {group}: {len(parsed)} events', flush=True)
    source = pd.DataFrame(source_rows)
    source.to_csv(OUT / 'Olympedia逐项奖牌表.csv', index=False, encoding='utf-8-sig')
    pd.DataFrame(manifest).sort_values(['Year','Sport','url']).to_csv(OUT / '原始页面清单.csv', index=False, encoding='utf-8-sig')
    matched = []
    for (year, sport), left in queue.groupby(['Year','Sport']):
        right = source[(source.Year.eq(int(year))) & source.Sport.eq(sport)].reset_index(drop=True)
        left = left.reset_index(drop=True)
        if right.empty:
            for _, a in left.iterrows(): matched.append({'Year':year,'Sport':sport,'Event':a.Event,'配对状态':'无运动页面'})
            continue
        scores = np.zeros((len(left), len(right)))
        for i, a in left.iterrows():
            an = normal(a.Event).replace(normal(sport), '').strip()
            for j, b in right.iterrows():
                bn = normal(b.Event_olympedia)
                alias = sailing_alias(int(year), a.Event) if sport == 'Sailing' else None
                if alias and b.Event_olympedia != alias:
                    scores[i,j] = -1000
                    continue
                if not alias and sex(a.Event) != sex(b.Event_olympedia):
                    scores[i,j] = -1000
                    continue
                name = token_set_ratio(an, bn)
                am = [codes(a[f'{m}_archive']) for m in ('Gold','Silver','Bronze')]
                bm = [codes(b[f'{m}_olympedia']) for m in ('Gold','Silver','Bronze')]
                medal = sum(12 for x,y in zip(am,bm) if x and x==y)
                scores[i,j] = name + medal + (40 if alias else 0)
        ri, ci = linear_sum_assignment(-scores)
        for i,j in zip(ri,ci):
            a,b = left.iloc[i], right.iloc[j]
            archive_match = [codes(a[f'{m}_archive']) == codes(b[f'{m}_olympedia']) for m in ('Gold','Silver','Bronze')]
            proxy_match = [codes(a[f'{m}_proxy']) == codes(b[f'{m}_olympedia']) for m in ('Gold','Silver','Bronze')]
            name_score = token_set_ratio(normal(a.Event).replace(normal(sport), '').strip(), normal(b.Event_olympedia))
            competing = sorted(scores[i,:], reverse=True)
            margin = scores[i,j] - (competing[1] if len(competing)>1 else -1000)
            alias = sailing_alias(int(year), a.Event) if sport == 'Sailing' else None
            safe_pair = bool(scores[i,j] >= 80 and name_score >= 45 and margin >= 5 and (not alias or b.Event_olympedia == alias))
            matched.append({'Year':year,'Sport':sport,'Event':a.Event,'Event_olympedia':b.Event_olympedia,
                            'Gold_archive':a.Gold_archive,'Silver_archive':a.Silver_archive,'Bronze_archive':a.Bronze_archive,
                            'Gold_olympedia':b.Gold_olympedia,'Silver_olympedia':b.Silver_olympedia,'Bronze_olympedia':b.Bronze_olympedia,
                            'Gold_proxy':a.Gold_proxy,'Silver_proxy':a.Silver_proxy,'Bronze_proxy':a.Bronze_proxy,
                            'name_score':round(name_score,1),'match_score':round(scores[i,j],1),'next_best_margin':round(margin,1),
                            'archive_three_match':all(archive_match),'proxy_three_match':all(proxy_match),
                            '配对状态':'自动高可信配对' if safe_pair else '配对待人工核实',
                            '对照结果':('三色与旧存档一致' if all(archive_match) else '旧存档与现行二次来源有差异') if safe_pair else '不自动判定',
                            'event_url':b.event_url,'sport_url':b.sport_url,'page_sha256':b.page_sha256})
    result = pd.DataFrame(matched).sort_values(['Year','Sport','Event'])
    assert len(result) == 555 and not result.duplicated(['Year','Event']).any()
    result.to_csv(OUT / '历史555项独立交叉对照.csv', index=False, encoding='utf-8-sig')
    primary = pd.read_csv(ROOT / '交付文件/任务三_专题深挖/S2_口径的魔力/08_逐项外部核验/历史910项来源覆盖总表.csv', dtype=str).fillna('')
    assert len(primary) == 910 and not primary.duplicated(['Year','Event']).any()
    secondary = result[['Year','Event','配对状态','对照结果','event_url','page_sha256']].rename(columns={
        '配对状态':'二次来源配对状态', '对照结果':'二次来源对照结果',
        'event_url':'Olympedia逐项链接', 'page_sha256':'Olympedia原始页面SHA256'})
    combined = primary.merge(secondary, on=['Year','Event'], how='left', validate='one_to_one')
    assert len(combined) == 910 and combined['Olympedia逐项链接'].notna().sum() == 555
    assert combined.loc[combined['Olympedia逐项链接'].notna(), '来源类型'].eq('Olympics.com第三方2023抓取存档').all()
    combined.to_csv(OUT / '历史910项双层证据总表.csv', index=False, encoding='utf-8-sig')
    summary = {'captured_utc':datetime.now(timezone.utc).isoformat(), 'source':'Olympedia live sport medal tables; independent specialist secondary source, not IOC',
               'old_only_events':555, 'sport_pages':len(manifest), 'source_events':len(source),
               'high_confidence_pairs':int(result['配对状态'].eq('自动高可信配对').sum()),
               'archive_agree':int(result['对照结果'].eq('三色与旧存档一致').sum()),
               'archive_disagree':int(result['对照结果'].eq('旧存档与现行二次来源有差异').sum()),
               'pair_review':int(result['配对状态'].ne('自动高可信配对').sum()),
               'current_ioc_verified':0}
    (OUT / '核验摘要.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False,indent=2))

if __name__ == '__main__': main()
