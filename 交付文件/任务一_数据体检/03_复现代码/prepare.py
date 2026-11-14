"""Preserve raw rows; add explicit analysis flags and reproducible aggregates."""
from pathlib import Path
import json
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'99_运行生成'; OUT.mkdir(exist_ok=True)
def resolve_source_csv():
 import os
 candidates=[]
 if os.environ.get('OLYMPICS_CSV'): candidates.append(Path(os.environ['OLYMPICS_CSV']))
 candidates += [Path.cwd()/'olympics_dataset.csv',ROOT/'olympics_dataset.csv',ROOT.parents[1]/'资料文件'/'原始资料'/'olympics_dataset.csv']
 for candidate in candidates:
  if candidate.is_file(): return candidate.resolve()
 raise FileNotFoundError('未找到 olympics_dataset.csv；可放在当前目录、总项目资料目录，或设置 OLYMPICS_CSV。')

SOURCE=resolve_source_csv()
d=pd.read_csv(SOURCE)
families={}
for family, sports in {
 'Gymnastics':['Gymnastics','Artistic Gymnastics','Rhythmic Gymnastics','Trampolining','Trampoline Gymnastics'],
 'Cycling':['Cycling','Cycling Road','Cycling Track','Cycling Mountain Bike','Cycling BMX Racing','Cycling BMX Freestyle'],
 'Canoeing':['Canoeing','Canoe Sprint','Canoe Slalom'],
 'Equestrian':['Equestrianism','Equestrian'],
 'Artistic Swimming':['Synchronized Swimming','Artistic Swimming'],
 'Swimming':['Swimming','Marathon Swimming'],
 'Basketball':['Basketball','3x3 Basketball'],
 'Volleyball':['Volleyball','Beach Volleyball'],
 'Baseball/Softball':['Baseball','Softball','Baseball/Softball'],
 'Rugby':['Rugby','Rugby Sevens'],
}.items():
 for sport in sports: families[sport]=family

def family(s):
 parts=s.split(', ')
 fs={families.get(p,p) for p in parts}
 return next(iter(fs)) if len(fs)==1 else 'Cross-sport unresolved'

mapping=pd.DataFrame({'Sport':sorted(d.Sport.unique())})
mapping['sport_family']=mapping.Sport.map(family)
mapping['rule']=mapping.Sport.map(lambda x:'multi-label same family' if ',' in x and family(x)!='Cross-sport unresolved' else ('event-level resolution required' if ',' in x else ('family harmonization' if x in families else 'identity')))
mapping.to_csv(OUT/'sport_mapping.csv',index=False,encoding='utf-8-sig')
d.insert(0,'source_row',range(2,len(d)+2))
d['sport_family']=d.Sport.map(family)
# The only cross-family combination present has one triathlon event and one cycling event.
cross=d.Sport.eq('Cycling Road, Triathlon')
d.loc[cross & d.Event.eq("Women's Individual"),'sport_family']='Triathlon'
d.loc[cross & d.Event.eq("Women's Individual Time Trial"),'sport_family']='Cycling'
d['sport_resolution']= 'raw or family mapping'
d.loc[cross,'sport_resolution']='event-based cross-family resolution'
generic={'Men','Women','Men Team','Women Team','Mixed Team','Team','Relay Only Athlete',"Men's Individual","Women's Individual","Men's Team","Women's Team","Men's Singles","Women's Singles"}
d['event_status']=d.Event.map(lambda s:'generic_or_context_required' if s in generic else 'specific_label_unverified')
d['include_main']=d.Year.ne(1906)
cols=[c for c in pd.read_csv(SOURCE,nrows=0).columns if c!='player_id']
d['duplicate_candidate']=d.duplicated(cols,keep=False)
d['duplicate_excess']=d.duplicated(cols,keep='first')
d['is_medal']=d.Medal.ne('No medal')
d.to_csv(OUT/'olympics_flagged.csv.gz',index=False,compression='gzip')
main=d[d.include_main]
for name,frame in [('main',main),('exclude_duplicate_excess',main[~main.duplicate_excess]),('include_1906',d)]:
 agg=frame.groupby('Year').agg(records=('Sex','size'),female_records=('Sex',lambda s:s.eq('F').sum()),medal_rows=('is_medal','sum'),delegations=('NOC','nunique'),sport_families=('sport_family','nunique'))
 agg['female_record_share']=agg.female_records/agg.records
 agg.to_csv(OUT/f'edition_{name}.csv')
main.groupby(['Year','NOC','Sex','sport_family','Medal']).size().rename('records').to_csv(OUT/'analysis_cube.csv')
dup=d[d.duplicate_candidate].groupby('Year').agg(candidate_rows=('source_row','size'),excess_rows=('duplicate_excess','sum'))
dup.to_csv(OUT/'duplicate_by_year.csv')
d.groupby(['Year','event_status']).size().rename('records').to_csv(OUT/'event_quality_by_year.csv')
assert len(d)==252565 and d.sport_family.notna().all()
assert not d.sport_family.eq('Cross-sport unresolved').any()
assert int(main.is_medal.sum())==38360
summary={'rows':len(d),'mapping_values':len(mapping),'flagged_duplicate_rows':int(d.duplicate_candidate.sum()),'duplicate_excess_rows':int(d.duplicate_excess.sum()),'main_medal_rows':int(main.is_medal.sum()),'main_records':len(main),'context_required_rows':int(d.event_status.eq('generic_or_context_required').sum())}
(OUT/'preparation_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary,indent=2))
