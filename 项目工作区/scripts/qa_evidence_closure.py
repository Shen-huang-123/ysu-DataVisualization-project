"""Regression checks for risk triage, final-model scope and source admission."""
from pathlib import Path
import hashlib,json,unittest
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urlparse,unquote
from evidence_guard import verify_olympedia
ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力/08_逐项外部核验/关键结论闭环_20261120'
class ClosureTests(unittest.TestCase):
    def test_35_keys_and_distinct_research_scopes(self):
        d=pd.read_csv(BASE/'35项风险重排与影响.csv');self.assertEqual(len(d),35);self.assertFalse(d.duplicated(['Year','Event']).any());self.assertEqual(int(d['原代理金牌集合改变'].sum()),10);self.assertTrue(d['东道主影响边界'].notna().all());self.assertEqual(set(d['新优先顺序']),{1,2,3})
    def test_model_reproduction_and_no_new_truth(self):
        d=json.loads((BASE/'闭环核验摘要.json').read_text(encoding='utf-8'));self.assertTrue(all(r['matches'] for r in d['model_comparisons']));self.assertEqual(d['forecast_cells'],3600);self.assertEqual(d['new_complete_ioc_certifications'],0);self.assertIn('未完成',d['full_ensemble_historical_validation'])
    def test_matrix_does_not_confuse_formula_with_validation(self):
        d=pd.read_csv(BASE/'最终预测验证矩阵.csv').set_index('对象');self.assertEqual(d.loc['完整最终集成','结论'],'未完成');self.assertEqual(d.loc['80%区间','结论'],'未通过认证');self.assertEqual(d.loc['旧排名门控集成','结论'],'通过（算术）')
    def test_new_source_originals_and_pdf_shell_not_accepted(self):
        m=json.loads((ROOT/'资料文件/外部核验/高风险补证_20261120/获取清单.json').read_text(encoding='utf-8'));accepted=[r for r in m if r['accepted_primary_content']];self.assertEqual(len(accepted),3)
        for r in accepted:self.assertEqual(hashlib.sha256((ROOT/r['raw_file']).read_bytes()).hexdigest(),r['sha256'])
        self.assertFalse(next(r for r in m if r['key']=='cas_aloyan')['accepted_primary_content']);self.assertEqual(verify_olympedia(),97)
    def test_local_download_links(self):
        for p in [BASE/'index.html',ROOT/'交付文件/最终提交材料/关键结论证据与预测验证补充说明.html']:
            s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
            for a in s.select('a[href]'):
                url=urlparse(a['href'])
                if not url.scheme:self.assertTrue((p.parent/unquote(url.path)).exists(),(p,a['href']))
if __name__=='__main__':unittest.main()
