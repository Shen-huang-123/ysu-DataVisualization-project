"""Render the limited headings/lists/links used by the three presentation notes.
Reuses existing HTML shell, preserves styles/scripts, and touches no task data.
"""
from pathlib import Path
from html import escape
import re

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'交付文件/最终提交材料'
template=BASE/'视频/视频讲解脚本.html'
def inline(s):
    s=escape(s)
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',s)
    s=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',s)
    return re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
def render(text):
    blocks=[]
    for part in re.split(r'\n\s*\n',text.strip()):
        lines=part.splitlines()
        if re.match(r'^#{1,3} ',part):
            n=len(part.split(' ')[0]);blocks.append(f'<h{n}>'+inline(part[n+1:])+f'</h{n}>')
        elif all(re.match(r'^(- |\d+\. )',x) for x in lines):
            tag='ul' if lines[0].startswith('- ') else 'ol'
            blocks.append('<'+tag+'>'+''.join('<li>'+inline(re.sub(r'^(- |\d+\. )','',x))+'</li>' for x in lines)+'</'+tag+'>')
        else:blocks.append('<p>'+inline(' '.join(lines))+'</p>')
    return '\n'.join(blocks)
for md in [BASE/'视频/视频讲解脚本.md',BASE/'视频/答辩追问与证据定位.md',BASE/'提交前检查.md']:
    dest=md.with_suffix('.html');shell=(dest if dest.exists() else template).read_text(encoding='utf-8')
    if not dest.exists():
        shell=shell.replace('视频讲解脚本',md.stem)
    shell,n=re.subn(r'(<main\b[^>]*class="article"[^>]*>).*?(</main>)',lambda m:m[1]+render(md.read_text(encoding='utf-8'))+m[2],shell,count=1,flags=re.S)
    assert n==1,md
    dest.write_text(shell,encoding='utf-8')
print('Synced three presentation HTML companions.')
