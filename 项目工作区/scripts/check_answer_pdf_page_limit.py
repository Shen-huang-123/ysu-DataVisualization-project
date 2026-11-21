"""Keep the formal answer within the 20-page limit after Word export."""
from pathlib import Path
import tempfile

import pymupdf

ROOT = Path(__file__).resolve().parents[2]
ANSWER = ROOT / '交付文件/最终提交材料/数说奥运_晓组织_正式答卷.pdf'
PAGE_LIMIT = 20
CHECKLIST = '提交材料核对清单'

def enforce_page_limit(path):
    with tempfile.TemporaryDirectory(dir=path.parent) as directory:
        candidate = Path(directory) / path.name
        with pymupdf.open(path) as doc:
            if doc.page_count <= PAGE_LIMIT:
                print(f'Answer PDF: {doc.page_count} pages')
                return
            if doc.page_count != PAGE_LIMIT + 1:
                raise ValueError('Unexpected overflow. Review the exported answer before editing.')
            checklist_page = doc[PAGE_LIMIT]
            lines = [line.strip() for line in checklist_page.get_text().splitlines() if line.strip()]
            if len(lines) < 3 or CHECKLIST not in lines[1] or len(lines) > 12:
                raise ValueError('The overflow page is not the known submission checklist.')
            expected = [(doc[i].get_text(), doc[i].get_pixmap(dpi=72).digest) for i in range(PAGE_LIMIT)]
            doc.delete_page(PAGE_LIMIT)
            doc.save(candidate,garbage=3,deflate=True)
        with pymupdf.open(candidate) as revised:
            assert revised.page_count == PAGE_LIMIT
            assert [(page.get_text(), page.get_pixmap(dpi=72).digest) for page in revised] == expected
        candidate.replace(path)
    print(f'Answer PDF: {PAGE_LIMIT} pages. Text and rendered pages 1–{PAGE_LIMIT} verified.')

if __name__ == '__main__':
    enforce_page_limit(ANSWER)
