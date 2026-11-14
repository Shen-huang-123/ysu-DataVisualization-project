from pathlib import Path
from zipfile import ZipFile
import re
import xml.etree.ElementTree as ET

root = Path(r'D:\虚拟C盘\数据可视化')
ns = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}
for file in sorted(root.glob('*.pptx')):
    print('\n###', file.name)
    with ZipFile(file) as z:
        slides = sorted((n for n in z.namelist() if re.fullmatch(r'ppt/slides/slide\d+\.xml', n)), key=lambda s: int(re.search(r'slide(\d+)', s).group(1)))
        print('SLIDES', len(slides))
        for name in slides:
            tree = ET.fromstring(z.read(name))
            lines = [''.join(t.itertext()).strip() for t in tree.findall('.//a:p', ns)]
            lines = [s for s in lines if s]
            if lines:
                print(re.search(r'slide(\d+)', name).group(1), ' | '.join(lines)[:370])
