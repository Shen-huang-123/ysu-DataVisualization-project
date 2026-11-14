"""检查统一动效在全部交付页面的注入与脚本语法。"""
from pathlib import Path
from urllib.parse import unquote,urlparse
import re,subprocess,tempfile

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'交付文件'
pages=[
    BASE/'作品总入口'/'index.html',
    BASE/'任务一_数据体检'/'index.html',
    BASE/'任务二_百年全景'/'05_交互总览'/'index.html',
    BASE/'任务三_专题深挖'/'统一中文入口'/'index.html',
    BASE/'任务三_专题深挖'/'S1_东道主效应'/'index.html',
    BASE/'任务三_专题深挖'/'S2_口径的魔力'/'06_交互榜'/'index.html',
    BASE/'任务三_专题深挖'/'S2_口径的魔力'/'06_滚动叙事专题'/'index.html',
    BASE/'任务三_专题深挖'/'S2_口径的魔力'/'07_口径实验室'/'index.html',
    BASE/'任务三_专题深挖'/'S3_冠军的保质期'/'06_冠军王朝时间轴'/'index.html',
    BASE/'任务三_专题深挖'/'S3_冠军的保质期'/'07_王朝生存图'/'index.html',
    BASE/'任务四_开放创作'/'index.html',
    BASE/'任务四_开放创作'/'01_交互式Dashboard'/'index.html',
    BASE/'任务四_开放创作'/'02_2028洛杉矶预测'/'index.html',
    BASE/'任务四_开放创作'/'03_数据新闻'/'index.html',
    BASE/'任务四_开放创作'/'06_赛后验收单'/'index.html',
    BASE/'任务四_开放创作'/'交互看板'/'index.html',
]
with tempfile.TemporaryDirectory() as tmp:
    for i,page in enumerate(pages):
        content=page.read_text(encoding='utf-8')
        assert content.count('id="xz-motion-style"')==1,page
        assert content.count('id="xz-motion-script"')==1,page
        assert 'prefers-reduced-motion:reduce' in content,page
        assert 'body.classList.add(\'xz-leaving\')' in content,page
        for raw in re.findall(r'(?:href|src)=["\']([^"\']+)["\']',content):
            url=urlparse(raw)
            if url.scheme or raw.startswith(('#','//')):continue
            assert (page.parent/unquote(url.path)).resolve().is_file(),(page,raw)
        scripts='\n'.join(re.findall(r'<script(?: [^>]*)?>(.*?)</script>',content,re.S))
        target=Path(tmp)/f'page_{i}.js';target.write_text(scripts,encoding='utf-8')
        result=subprocess.run(['node','--check',str(target)],capture_output=True,text=True)
        assert result.returncode==0,(page,result.stderr)
print(f'{len(pages)} 个页面：动效、链接与脚本语法检查通过')
