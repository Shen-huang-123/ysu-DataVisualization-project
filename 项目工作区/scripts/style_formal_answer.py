"""Apply the formal answer's print palette without changing its pagination."""
from pathlib import Path
import argparse
import re
import tempfile

import pymupdf
from docx import Document

from add_answer_evidence_table import publish as add_evidence
from check_answer_pdf_page_limit import enforce_page_limit
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import RGBColor

INK = "142E3B"
TEAL = "24646A"
MUTED = "485F69"


def color_runs(paragraph, color):
    for run in paragraph.runs:
        if run.text.strip():
            run.font.color.rgb = RGBColor.from_string(color)


def rule(paragraph):
    props = paragraph._p.get_or_add_pPr()
    borders = props.find(qn("w:pBdr"))
    if borders is None:
        borders = OxmlElement("w:pBdr")
        props.insert_element_before(borders, "w:shd", "w:tabs", "w:spacing", "w:ind", "w:jc", "w:rPr")
    border = borders.find(qn("w:bottom"))
    if border is None:
        border = OxmlElement("w:bottom")
        borders.append(border)
    for name, value in {"val": "single", "sz": "6", "space": "1", "color": "C3D6D5"}.items():
        border.set(qn(f"w:{name}"), value)


def style_answer(source, destination):
    document = Document(source)
    for index, paragraph in enumerate(document.paragraphs):
        text = paragraph.text.strip()
        if paragraph.style.name == "Title":
            color_runs(paragraph, INK)
            rule(paragraph)
        elif paragraph.style.name == "Heading 1":
            color_runs(paragraph, INK)
            rule(paragraph)
        elif paragraph.style.name == "Heading 2" or index == 0:
            color_runs(paragraph, TEAL)
        elif re.match(r"^图\s*(?:[A-D]\d|S\d|\d|Ⅳ)", text):
            color_runs(paragraph, MUTED)
    document.save(destination)


def finalize_pdf(exported, previous, destination):
    """Keep the published high-resolution figures and restore evidence links."""
    with tempfile.TemporaryDirectory(dir=destination.parent) as scratch:
        candidate = Path(scratch) / destination.name
        with pymupdf.open(exported) as doc, pymupdf.open(previous) as old:
            if len(doc) not in (len(old), len(old) + 1):
                raise ValueError("Word export changed the answer pagination.")
            for page, prior in zip(doc, old):
                images = page.get_image_info(hashes=True, xrefs=True)
                previous_images = prior.get_image_info(hashes=True, xrefs=True)
                if len(images) != len(previous_images):
                    raise ValueError(f"Image layout changed on page {page.number + 1}")
                for image, previous_image in zip(images, previous_images):
                    if image["digest"] != previous_image["digest"]:
                        stream = old.extract_image(previous_image["xref"])["image"]
                        page.replace_image(image["xref"], stream=stream)
            doc.save(candidate, garbage=3, deflate=True)
        enforce_page_limit(candidate)
        ready = destination.parent / (destination.stem + ".evidence-candidate.pdf")
        if ready.exists():
            raise FileExistsError(ready)
        candidate.replace(ready)
        try:
            add_evidence(ready)
            with pymupdf.open(ready) as doc, pymupdf.open(previous) as old:
                if len(doc) != len(old):
                    raise ValueError("Published page count changed.")
                for page, prior in zip(doc, old):
                    normalize = lambda text: "".join(text.split())
                    if normalize(page.get_text()) != normalize(prior.get_text()):
                        raise ValueError(f"Published text changed on page {page.number + 1}")
                    if len(page.get_links()) != len(prior.get_links()):
                        raise ValueError(f"Published links changed on page {page.number + 1}")
            ready.replace(destination)
        finally:
            ready.unlink(missing_ok=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument('--preserve-pdf', type=Path)
    args = parser.parse_args()
    if args.preserve_pdf:
        finalize_pdf(args.source, args.preserve_pdf, args.destination)
    else:
        style_answer(args.source, args.destination)
