from pathlib import Path
import fitz
from PIL import Image, ImageDraw

root = Path(__file__).resolve().parents[2]
pdf_path = root / "交付文件" / "任务一_数据体检" / "01_报告与说明" / "任务一_数据质量与口径说明书_高分版.pdf"
out_dir = root / "项目工作区" / "outputs" / "qa" / "任务一PDF"
out_dir.mkdir(parents=True, exist_ok=True)

doc = fitz.open(pdf_path)
pages = []
for index, page in enumerate(doc):
    pix = page.get_pixmap(matrix=fitz.Matrix(1.6, 1.6), alpha=False)
    target = out_dir / f"page_{index + 1:02d}.png"
    pix.save(target)
    image = Image.open(target).convert("RGB")
    image.thumbnail((520, 735))
    pages.append(image.copy())

margin = 24
label_h = 28
cols = 2
rows = (len(pages) + cols - 1) // cols
cell_w = max(img.width for img in pages) + margin * 2
cell_h = max(img.height for img in pages) + label_h + margin * 2
sheet = Image.new("RGB", (cell_w * cols, cell_h * rows), "#dfe5e7")
draw = ImageDraw.Draw(sheet)
for index, image in enumerate(pages):
    col, row = index % cols, index // cols
    x = col * cell_w + margin
    y = row * cell_h + margin + label_h
    draw.text((x, row * cell_h + margin), f"Page {index + 1}", fill="#163b4a")
    sheet.paste(image, (x, y))
sheet.save(out_dir / "contact_sheet.png", quality=92)
print(f"pages={len(doc)}")
print(out_dir / "contact_sheet.png")
