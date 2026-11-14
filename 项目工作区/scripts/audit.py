from pathlib import Path
import json, hashlib, zipfile
import xml.etree.ElementTree as ET
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'outputs'
OUT.mkdir(exist_ok=True)
DATA = ROOT.parent / '资料文件' / '原始资料'

def resolve_source_csv():
    import os
    candidates = []
    if os.environ.get('OLYMPICS_CSV'):
        candidates.append(Path(os.environ['OLYMPICS_CSV']))
    candidates += [Path.cwd()/'olympics_dataset.csv', ROOT/'olympics_dataset.csv', DATA/'olympics_dataset.csv']
    for candidate in candidates:
        if candidate.is_file(): return candidate.resolve()
    searched = '\n'.join(f'- {candidate}' for candidate in candidates)
    raise FileNotFoundError(f'未找到 olympics_dataset.csv。已检查：\n{searched}\n也可设置 OLYMPICS_CSV 环境变量。')

p = resolve_source_csv()
d = pd.read_csv(p)
med = d[d.Medal.ne('No medal')]
generic = d.Event.str.fullmatch(r'Men|Women|Men Team|Women Team|Relay Only Athlete', case=False, na=False)
result = {
 'sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
 'shape': list(d.shape), 'columns': list(d.columns),
 'missing': d.isna().sum().to_dict(),
 'distinct': d.nunique().to_dict(),
 'exact_duplicate_rows': int(d.duplicated().sum()),
 'duplicates_without_id': int(d.drop(columns='player_id').duplicated().sum()),
 'medals': d.Medal.value_counts().to_dict(),
 'years': sorted(d.Year.unique().tolist()),
 'sex': d.Sex.value_counts().to_dict(),
 'season': d.Season.value_counts().to_dict(),
 'comma_sport_rows': int(d.Sport.str.contains(',', na=False).sum()),
 'generic_event_rows_strict_list': int(generic.sum()),
 'medal_rows_1906': int(med.Year.eq(1906).sum()),
 'cities_1956': d.loc[d.Year.eq(1956),'City'].value_counts().to_dict(),
 'id_multiple_names': int(d.groupby('player_id').Name.nunique().gt(1).sum()),
 'names_spanning_over_40_years': int(d.groupby('Name').Year.agg(lambda s:s.max()-s.min()).gt(40).sum()),
}
(OUT/'audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
d.groupby(['Year','Sex']).size().unstack(fill_value=0).to_csv(OUT/'participation_rows_by_year_sex.csv')
d.groupby(['Year','Sport']).size().rename('rows').to_csv(OUT/'sport_inventory.csv')
d.groupby(['Year','Event']).size().rename('rows').to_csv(OUT/'event_inventory.csv')
d[d.drop(columns='player_id').duplicated(keep=False)].to_csv(OUT/'duplicate_candidates.csv',index=False)
with zipfile.ZipFile(DATA/'数说奥运_答卷模板.docx') as z:
 tree=ET.fromstring(z.read('word/document.xml'))
 ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
 text='\n'.join(''.join(p.itertext()) for p in [])
 paragraphs=[''.join(p.itertext()) for p in tree.findall('.//w:p',ns)]
 # Read only text runs, preserving paragraph and table reading order.
 paragraphs=[''.join(t.text or '' for t in p.findall('.//w:t',ns)) for p in tree.findall('.//w:p',ns)]
 (OUT/'template_text.txt').write_text('\n'.join(paragraphs),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
