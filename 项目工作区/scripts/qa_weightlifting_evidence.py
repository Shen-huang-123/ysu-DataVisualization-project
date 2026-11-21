"""Identity regressions: gold reassignment must never change weight-class mapping."""
from pathlib import Path
import ast, hashlib, json, re, unittest
import pandas as pd
ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力/08_逐项外部核验'
class WeightliftingEvidenceTests(unittest.TestCase):
    def test_all_45_secondary_pairs_preserve_sex_and_class(self):
        data=pd.read_csv(BASE/'Olympedia独立交叉核验/历史555项独立交叉对照.csv')
        data=data[data.Sport.eq('Weightlifting')]
        self.assertEqual(len(data),41)
        def words(s):return set(re.sub('[^a-z]+',' ',s.lower().replace("'s",'').replace('weightlifting','')).split())
        for row in data.itertuples():self.assertEqual(words(row.Event),words(row.Event_olympedia),row.Event)
    def test_archive_weight_class_urls(self):
        data=pd.read_csv(BASE/'逐小项三色对照.csv').rename(columns={'Event_proxy':'Event'});data=data[data.Sport.eq('Weightlifting')]
        self.assertEqual(len(data),45)
        men=dict(Bantamweight=56,Featherweight=62,Lightweight=69,Middleweight=77,Heavyweight=105,**{'Light-Heavyweight':85,'Middle-Heavyweight':94,'Super-Heavyweight':105})
        women=dict(Flyweight=48,Featherweight=53,Lightweight=58,Middleweight=63,Heavyweight=75,**{'Light-Heavyweight':69,'Super-Heavyweight':75})
        for row in data.itertuples():
            male="Men's" in row.Event;label=row.Event.split("'s ")[-1];url=row.Event_olympics
            self.assertEqual(int(re.findall(r'\d+',url)[0]),(men if male else women)[label])
            self.assertEqual('women' in url,not male)
    def test_2012_gold_identities(self):
        for file,gold in [('逐小项三色对照.csv','Gold_archive'),('Olympedia独立交叉核验/历史555项独立交叉对照.csv','Gold_olympedia')]:
            data=pd.read_csv(BASE/file).rename(columns={'Event_proxy':'Event'});data=data[data.Year.eq(2012)].set_index('Event')
            self.assertEqual(data.loc["Weightlifting Women's Middleweight",gold],'CAN')
            self.assertEqual(data.loc["Weightlifting Women's Heavyweight",gold],'ESP')
    def test_raw_hashes_and_download_links(self):
        from bs4 import BeautifulSoup
        from urllib.parse import urlparse,unquote
        manifest=json.loads((ROOT/'资料文件/外部核验/后续补证_20261121/获取清单.json').read_text(encoding='utf-8'))
        for row in manifest:
            if row.get('raw_file'):self.assertEqual(hashlib.sha256((ROOT/row['raw_file']).read_bytes()).hexdigest(),row['sha256'])
            else:self.assertNotIn('sha256',row)
        path=BASE/'后续补证_20261121/index.html'
        for a in BeautifulSoup(path.read_text(encoding='utf-8'),'html.parser').select('a[href]'):
            url=urlparse(a['href'])
            if not url.scheme:self.assertTrue((path.parent/unquote(url.path)).exists())
if __name__=='__main__':unittest.main()
