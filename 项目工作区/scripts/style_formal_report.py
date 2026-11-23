"""Style the final, evidence-aligned report after all content post-processing."""
from collections import Counter
from pathlib import Path
import argparse
import tempfile

import pymupdf as pdf

ROOT = Path(__file__).resolve().parents[2]
REPORT = ROOT / "交付文件/最终提交材料/报告/百年圣火_正式报告.pdf"
FONT = Path(r"C:\Windows\Fonts\simhei.ttf")
MARKER = "formal-report-editorial-style-v1"


def rgb(value):
    return tuple(int(value[i:i+2], 16) / 255 for i in (0, 2, 4))


def content(page):
    return Counter("".join(page.get_text().split()))


def restyle(source, destination):
    font = pdf.Font(fontfile=str(FONT))
    ink, teal, warm = map(rgb, ("112c39", "22636a", "d6ac62"))
    with pdf.open(source) as doc:
        if doc.metadata.get("keywords", "").endswith(MARKER):
            raise ValueError("This report already has the editorial style.")
        toc = []
        for page in doc:
            blocks = sorted(
                (block for block in page.get_text("blocks") if block[6] == 0 and block[3] < 123),
                key=lambda block: block[1],
            )
            if len(blocks) != 3:
                raise ValueError(f"Unexpected header on page {page.number + 1}")
            name, section, title = [block[4].strip() for block in blocks]
            original = content(page)
            cover = page.number == 0
            for block in blocks:
                page.add_redact_annot(pdf.Rect(block[:4]), fill=False, cross_out=False)
            page.apply_redactions(images=0, graphics=0)
            width = page.rect.width
            bg = rgb("102b38" if cover else "edf3f1")
            page.draw_rect(pdf.Rect(0, 0, width, 132), color=None, fill=bg)
            page.draw_rect(pdf.Rect(0, 0, width, 4), color=None, fill=warm if cover else teal)
            page.draw_line((46, 52), (width - 46, 52),
                           color=rgb("48626a" if cover else "c7d6d4"), width=.65)
            page.insert_font(fontname="EditorialHei", fontfile=str(FONT))

            def label(y, text, size, color):
                size = min(size, size * (width - 92) / font.text_length(text, fontsize=size))
                page.insert_text((46, y), text, fontname="EditorialHei", fontsize=size, color=color)

            label(39, name, 9, rgb("d0dddd" if cover else "526574"))
            label(76, section, 10, warm if cover else teal)
            label(113, title, 32 if cover else 25, rgb("ffffff") if cover else ink)
            page.draw_line((46, 790), (100, 790), color=teal, width=1.3)
            if content(page) != original:
                raise ValueError(f"Text changed on page {page.number + 1}")
            toc.append([1, title, page.number + 1])
        doc.set_toc(toc)
        metadata = doc.metadata
        metadata["keywords"] = " ".join(filter(None, (metadata.get("keywords"), MARKER)))
        doc.set_metadata(metadata)
        doc.save(destination, garbage=3, deflate=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", nargs="?", type=Path, default=REPORT)
    args = parser.parse_args()
    with tempfile.TemporaryDirectory(dir=args.report.parent) as working:
        output = Path(working) / args.report.name
        restyle(args.report, output)
        output.replace(args.report)
