from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,re
import pandas as pd
from lxml import html
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'outputs'
source=OUT/'paris2024_medal_table_source.html'
tree=html.parse(str(source))
table=next(t for t in tree.xpath('//table') if 'Rank' in t.text_content() and 'NOC' in t.text_content() and len(t.xpath('.//tr'))>80)
records=[]
for tr in table.xpath('.//tr'):
 th=tr.xpath('./th[@scope="row"]')
 if not th: continue
 links=th[0].xpath('.//a[contains(@href,"at_the_2024_Summer_Olympics")]')
 if not links: continue
 nums=[x.text_content().strip() for x in tr.xpath('./td')]
 # Rank cells can span multiple rows. Last four cells always hold medal counts.
 if len(nums)<4 or not all(re.fullmatch(r'\d+',x) for x in nums[-4:]): continue
 records.append([links[0].text_content(),*map(int,nums[-4:])])
external=pd.DataFrame(records,columns=['delegation','gold','silver','bronze','total'])
assert len(external)==92, len(external)
assert (external[['gold','silver','bronze']].sum(axis=1)==external.total).all()
external.to_csv(OUT/'paris2024_published_medals_secondary.csv',index=False)
names={'USA':'United States','CHN':'China','JPN':'Japan','AUS':'Australia','FRA':'France','NED':'Netherlands','GBR':'Great Britain','KOR':'South Korea','ITA':'Italy','GER':'Germany','NZL':'New Zealand','CAN':'Canada','UZB':'Uzbekistan','HUN':'Hungary','ESP':'Spain'}
d=pd.read_csv(OUT/'olympics_flagged.csv.gz'); d=d[d.Year.eq(2024)]
rows=d[d.Medal.eq('Gold')].groupby('NOC').size().rename('gold_rows')
rows_rank=rows.rank(method='min',ascending=False)
official=external[external.delegation.ne('Individual Neutral Athletes')].sort_values(['gold','silver','bronze'],ascending=False).copy()
official['published_rank']=official[['gold','silver','bronze']].apply(tuple,axis=1).rank(method='min',ascending=False).astype(int)
c=pd.DataFrame({'NOC':list(names),'delegation':list(names.values())}).merge(official,on='delegation',validate='one_to_one')
assert len(c)==len(names)
c['gold_rows']=c.NOC.map(rows); c['gold_row_rank']=c.NOC.map(rows_rank).astype(int)
c['rows_per_published_gold']=c.gold_rows/c.gold
c.to_csv(OUT/'paris2024_scale_comparison.csv',index=False)
decomp=d[d.Medal.eq('Gold') & d.NOC.isin(names)].groupby(['NOC','sport_family']).size().rename('gold_rows').reset_index()
decomp.to_csv(OUT/'paris2024_gold_rows_by_family.csv',index=False)
metadata={'url':'https://en.wikipedia.org/wiki/2024_Summer_Olympics_medal_table','source_type':'secondary; primary-source verification pending','snapshot_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'parsed_at_utc':datetime.now(timezone.utc).isoformat(),'scope':'92 entries including unranked AIN; AIN excluded from ranked comparison','join':'15 explicitly mapped NOC codes; unmapped delegations not silently matched','primary_access':'IOC medals page Access Denied during retrieval'}
(OUT/'paris2024_source_metadata.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2),encoding='utf-8')
print(c.to_string(index=False));print(decomp[decomp.NOC.eq('NED')].to_string(index=False))
