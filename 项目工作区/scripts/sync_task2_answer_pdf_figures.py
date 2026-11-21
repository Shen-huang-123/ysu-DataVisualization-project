"""Update Task 2 figures in the locally held, paginated formal answer."""
from io import BytesIO
from pathlib import Path
from tempfile import TemporaryDirectory

from PIL import Image, ImageOps
import pymupdf

ROOT = Path(__file__).resolve().parents[2] / '交付文件'
ANSWER = ROOT / '最终提交材料/数说奥运_晓组织_正式答卷.pdf'
FIGURES = ROOT / '任务二_百年全景/04_核心图表'
NAMES = {
    'A1':'A_规模扩张与奖牌集中度', 'A2':'A_历史累计奖牌记录榜',
    'B1':'B_十二代表团兴衰曲线', 'B2':'B_强国时代热力图',
    'C1':'C_女性三层平权曲线', 'C2':'C_2024代表团女性结构差',
    'D1':'D_小项增长与项目更替', 'D2':'D_项目新增退出重返流向',
}

with TemporaryDirectory(dir=ANSWER.parent) as tmp:
    candidate=Path(tmp)/ANSWER.name
    with pymupdf.open(ANSWER) as doc:
        assert len(doc)==20
        before=[page.get_text() for page in doc]
        targets={}
        for page in doc:
            images=page.get_image_info(xrefs=True)
            for label in NAMES:
                caption=page.search_for('图 '+label+'｜')
                if not caption:
                    continue
                assert label not in targets
                y=min(box.y0 for box in caption)
                assert max(box.y0 for box in caption)-y<5
                preceding=[i for i in images if i['bbox'][3] <= y+2 and i['xref']]
                nearest=max(preceding,key=lambda i:i['bbox'][3])
                assert 0 <= y-nearest['bbox'][3]+2 < 28
                targets[label]=(page.number,nearest)
        assert targets.keys()==NAMES.keys()
        assert len({i['xref'] for _,i in targets.values()})==8
        affected={n for n,_ in targets.values()}
        unchanged={page.number:page.get_pixmap(dpi=52).digest for page in doc if page.number not in affected}
        for label,(page,old) in targets.items():
            x0,y0,x1,y1=old['bbox']
            # Use the printed box ratio, with an even white margin to preserve labels.
            width=2200
            dims=(width,round(width*(y1-y0)/(x1-x0)))
            with Image.open(FIGURES/f'{NAMES[label]}.png') as im:
                fitted=ImageOps.pad(im.convert('RGB'),dims,color='#fbfaf6')
                output=BytesIO()
                fitted.save(output,format='PNG')
            doc[page].replace_image(old['xref'],stream=output.getvalue())
        doc.save(candidate,garbage=3,deflate=True)
    with pymupdf.open(candidate) as doc:
        assert len(doc)==20 and [p.get_text() for p in doc]==before
        assert all(doc[n].get_pixmap(dpi=52).digest==fingerprint for n,fingerprint in unchanged.items())
    candidate.replace(ANSWER)
print('Eight Task 2 figures updated. 20 pages; all text and other pages verified.')
