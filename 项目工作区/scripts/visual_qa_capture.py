"""Capture local static pages in Chrome for visual review, including dark mode."""
from pathlib import Path
import argparse
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[2]
CHROME = Path('C:/Program Files/Google/Chrome/Application/chrome.exe')
OUT = ROOT / '项目工作区' / 'qa_visual'

def capture(relative: str, width: int, height: int, dark: bool) -> Path:
    original = ROOT / '交付文件' / relative
    if not original.is_file():
        raise FileNotFoundError(original)
    OUT.mkdir(parents=True, exist_ok=True)
    stem = relative.replace('/', '_').replace('index.html', '').strip('_')
    image = OUT / f'{stem}_{width}_{"dark" if dark else "light"}.png'
    target = original
    temporary = original.with_name('.codex-visual-qa.html')
    if dark:
        html = original.read_text(encoding='utf-8')
        html = html.replace('<head>', '<head><script>try{localStorage.setItem("xz-theme","dark")}catch(e){}</script>', 1)
        temporary.write_text(html, encoding='utf-8')
        target = temporary
    try:
        with tempfile.TemporaryDirectory(prefix='codex-visual-qa-') as profile:
            args = [str(CHROME), '--headless=new', '--disable-gpu', '--no-first-run',
                    '--no-default-browser-check', '--disable-extensions',
                    '--force-prefers-reduced-motion=reduce',
                    f'--user-data-dir={profile}', f'--window-size={width},{height}',
                    '--virtual-time-budget=3000', f'--screenshot={image}', target.as_uri()]
            subprocess.run(args, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=25)
    finally:
        if temporary.exists():
            temporary.unlink()
    if not image.exists():
        raise RuntimeError(f'Chrome returned no screenshot: {relative}')
    return image

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('page')
    parser.add_argument('--width', type=int, default=1440)
    parser.add_argument('--height', type=int, default=900)
    parser.add_argument('--dark', action='store_true')
    args = parser.parse_args()
    print(capture(args.page, args.width, args.height, args.dark))
