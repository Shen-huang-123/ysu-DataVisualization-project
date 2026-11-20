"""Meaningful regression checks for evidence admission and archive exclusion."""
import hashlib,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
from current_ioc_import_audit import validate_source,medals
from evidence_guard import presentation_html,verify_olympedia,PROTECTED
class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name);(self.root/'event.html').write_bytes(b'original event')
        self.row=dict(official_url='https://www.olympics.com/en/olympic-games/rio-2016/results/archery/individual-men',source_kind='current_ioc_event',medal_scope='full_event',raw_file='event.html',raw_sha256=hashlib.sha256(b'original event').hexdigest(),reviewer='manual-test',review_status='approved',capture_date='2026-11-17',review_date='2026-11-18',Gold='KOR',Silver='FRA',Bronze='USA')
    def test_reviewed_full_event(self):self.assertEqual(validate_source(self.row,self.root),[])
    def test_book_and_news_are_not_current_event(self):
        for url in ['https://library.olympics.com/book','https://www.olympics.com/ioc/news/decision','https://www.olympics.com.evil.test/en/olympic-games/rio-2016/results/archery/individual-men']:
            self.assertTrue(validate_source(dict(self.row,official_url=url),self.root))
    def test_hash_tampering(self):
        (self.root/'event.html').write_bytes(b'changed');self.assertTrue(any('SHA256' in e for e in validate_source(self.row,self.root)))
    def test_empty_medal_requires_reason(self):
        self.assertTrue(validate_source(dict(self.row,Bronze=''),self.root));self.assertEqual(validate_source(dict(self.row,Bronze='',Bronze_empty_reason='not awarded; reviewed in original'),self.root),[])
    def test_no_review_or_invalid_date(self):
        self.assertTrue(validate_source(dict(self.row,reviewer=''),self.root));self.assertTrue(validate_source(dict(self.row,capture_date='2099-01-01'),self.root))
    def test_multiplicity_is_retained(self):self.assertNotEqual(medals('USA|USA'),medals('USA'))
    def test_raw_archive_and_all_postprocessors_exclusion(self):
        self.assertEqual(verify_olympedia(),97);self.assertFalse(any(p.resolve().is_relative_to(PROTECTED.resolve()) for p in presentation_html(PROTECTED)))
if __name__=='__main__':unittest.main()
