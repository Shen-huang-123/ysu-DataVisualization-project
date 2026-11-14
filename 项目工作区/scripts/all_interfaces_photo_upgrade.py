"""Give every remaining deliverable interface a photographic editorial header.

This post-processing step is intentionally small: it leaves the charts, controls,
data and scripts in each page untouched. Run it after other page generators.
"""
from __future__ import annotations

import html
import json
import os
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DELIVERY = ROOT / "交付文件"
MEDIA = DELIVERY / "任务三_专题深挖" / "媒体"
CREDITS = {item["key"]: item for item in json.loads((MEDIA / "图片来源与许可.json").read_text(encoding="utf-8"))}

# The ten main Task 3 stories already have their own art direction and photo stage.
PAGES = {
    "任务一_数据体检/index.html": ("growth", "archive", "数据档案"),
    "任务二_百年全景/05_交互总览/index.html": ("sports", "archive", "百年全景"),
    "作品总入口/index.html": ("host", "portal", "奥运数据故事"),
    "任务三_专题深挖/S2_口径的魔力/06_交互榜/index.html": ("lens", "lab", "冠军榜"),
    "任务三_专题深挖/S2_口径的魔力/07_口径实验室/index.html": ("archive", "lab", "口径实验室"),
    "任务三_专题深挖/S3_冠军的保质期/07_王朝生存图/index.html": ("dynasty", "lab", "王朝生存图"),
    "任务四_开放创作/index.html": ("la", "la", "洛杉矶 2028"),
    "任务四_开放创作/01_交互式Dashboard/index.html": ("la", "la", "预测看板"),
    "任务四_开放创作/02_2028洛杉矶预测/index.html": ("la", "la", "预测方法"),
    "任务四_开放创作/03_数据新闻/index.html": ("la", "la", "数据新闻"),
    "任务四_开放创作/06_赛后验收单/index.html": ("la", "la", "赛后验收"),
    "任务四_开放创作/交互看板/index.html": ("la", "la", "交互看板"),
}

START = "<!-- ALL_INTERFACES_PHOTO_START -->"
END = "<!-- ALL_INTERFACES_PHOTO_END -->"

for relative, (photo_key, tone, label) in PAGES.items():
    path = DELIVERY / relative
    if not path.exists():
        raise FileNotFoundError(path)
    source = path.read_text(encoding="utf-8")
    source = re.sub(re.escape(START) + r".*?" + re.escape(END), "", source, flags=re.S)
    source = re.sub(r'<span class="photo-editorial-credit">.*?</span>', '', source, count=1, flags=re.S)
    source = re.sub(r'<body\b[^>]*>', lambda m: m.group(0).replace('photo-editorial photo-tone-' + tone, ''), source, count=1)
    source = re.sub(r'<header\b[^>]*>', lambda m: m.group(0).replace('photo-editorial-hero', ''), source, count=1)
    source = re.sub(r'\sclass=["\']\s*["\']', '', source)
    if '</head>' not in source:
        source = source.replace('<main>', '</head><body><main>', 1)
    if not re.search(r'<body(?=[\s>])', source, flags=re.I):
        source = source.replace('</head>', '</head><body>', 1)
        source = source.replace('</html>', '</body></html>', 1)
    credit = CREDITS[photo_key]
    photo_path = os.path.relpath(MEDIA / credit["file"], path.parent).replace("\\", "/")
    css = f"""
<style id="all-interfaces-photo-style">
/* A photographic frame, with the original data interface retained below. */
body.photo-editorial {{ background-image:radial-gradient(circle at 50% -8%,rgba(33,76,83,.11),transparent 42%) !important; }}
body.photo-editorial header.photo-editorial-hero {{
  position:relative !important; isolation:isolate; overflow:hidden;
  min-height:clamp(260px,38vw,490px); padding:clamp(35px,6vw,88px) clamp(26px,6vw,100px) !important;
  display:flex; flex-direction:column; justify-content:center; align-items:flex-start;
  background-image:linear-gradient(100deg,rgba(9,27,33,.92) 0%,rgba(10,34,42,.75) 43%,rgba(15,37,45,.22) 100%),url('{html.escape(photo_path, quote=True)}') !important;
  background-position:center,center 45% !important; background-size:cover !important;
  color:#f9f6ee !important; box-shadow:0 20px 50px rgba(21,44,50,.14);
}}
body.photo-editorial header.photo-editorial-hero :is(h1,h2,h3,p,em,strong,small,span) {{color:inherit;}}
body.photo-editorial header.photo-editorial-hero h1 {{max-width:930px; font-size:clamp(2.35rem,5.2vw,5.5rem) !important; line-height:1.08 !important; letter-spacing:-.045em; text-shadow:0 3px 24px rgba(0,0,0,.22);}}
body.photo-editorial header.photo-editorial-hero p {{max-width:750px; text-shadow:0 1px 12px rgba(0,0,0,.3);}}
body.photo-editorial header.photo-editorial-hero a {{transition:transform .25s ease,background .25s ease,box-shadow .25s ease;}}
body.photo-editorial header.photo-editorial-hero a:hover {{transform:translateY(-3px); box-shadow:0 12px 24px rgba(0,0,0,.18);}}
body.photo-editorial header.photo-editorial-hero .xz-hero-orbit {{display:none !important;}}
body.photo-editorial .photo-editorial-credit {{
  display:block; width:fit-content; max-width:calc(100% - 32px); margin:10px clamp(16px,3vw,45px) 0 auto;
  font:11px/1.5 system-ui,'Microsoft YaHei',sans-serif; letter-spacing:.02em;
  color:#52656a; background:rgba(255,255,255,.82); border:1px solid rgba(20,53,59,.13);
  border-radius:999px; padding:5px 12px;
}}
body.photo-editorial .photo-editorial-credit a {{color:#176b79;text-decoration:underline;text-underline-offset:2px;}}
body.photo-editorial header.photo-editorial-hero::after {{content:'';position:absolute;inset:0;z-index:-1;pointer-events:none;background:linear-gradient(0deg,rgba(3,15,19,.2),transparent 35%);}}
body.photo-editorial.photo-tone-archive header.photo-editorial-hero {{background-image:linear-gradient(100deg,rgba(39,31,25,.91),rgba(39,31,25,.72) 44%,rgba(39,31,25,.15)),url('{html.escape(photo_path, quote=True)}') !important;}}
body.photo-editorial.photo-tone-la header.photo-editorial-hero {{background-image:linear-gradient(100deg,rgba(15,30,43,.92),rgba(16,42,54,.68) 46%,rgba(16,42,54,.13)),url('{html.escape(photo_path, quote=True)}') !important;}}
body.photo-editorial.photo-tone-lab header.photo-editorial-hero {{min-height:clamp(230px,30vw,365px);}}
body.photo-editorial.photo-tone-portal header.photo-editorial-hero {{min-height:clamp(430px,65vw,720px);}}
body.photo-editorial :is(.xz-card,.card,.panel) {{transition:transform .28s ease,box-shadow .28s ease;}}
body.photo-editorial :is(.xz-card,.card,.panel):hover {{transform:translateY(-3px);box-shadow:0 16px 36px rgba(18,41,46,.12);}}
@media(max-width:700px) {{
  body.photo-editorial header.photo-editorial-hero {{min-height:330px;padding:38px 20px 62px !important;background-position:center,58% center !important;}}
  body.photo-editorial header.photo-editorial-hero h1 {{font-size:clamp(2rem,9vw,3rem) !important;}}
  body.photo-editorial .photo-editorial-credit {{margin:8px 12px 0 auto;font-size:10px;max-width:calc(100% - 24px);border-radius:10px;}}
}}
@media(prefers-reduced-motion:reduce) {{body.photo-editorial * {{scroll-behavior:auto !important;transition-duration:0s !important;animation-duration:0s !important;}}}}
</style>
"""
    # A local, licensed image is visible in every header. The credit also makes
    # clear that these photographs illustrate context, not the dataset itself.
    def add_class(match, class_name):
        tag = match.group(0)
        cls = re.search(r'\bclass=["\']([^"\']*)["\']', tag)
        if cls:
            return tag[:cls.start(1)] + (cls.group(1).strip() + ' ' + class_name).strip() + tag[cls.end(1):]
        return tag[:-1] + f' class="{class_name}">'
    source = re.sub(r'<body\b[^>]*>', lambda m: add_class(m, f'photo-editorial photo-tone-{tone}'), source, count=1)
    source = re.sub(r'<header\b[^>]*>', lambda m: add_class(m, 'photo-editorial-hero'), source, count=1)
    by = "历史影像" if photo_key != "la" else "1984 年洛杉矶历史影像"
    credit_markup = f'<span class="photo-editorial-credit">{by} · <a href="{html.escape(credit["source"], quote=True)}" target="_blank" rel="noopener">Wikimedia Commons</a> · {html.escape(credit["license"])} · {html.escape(label)}</span>'
    source = source.replace("</header>", "</header>" + credit_markup, 1)
    source = source.replace("</head>", START + css + END + "</head>", 1)
    path.write_text(source, encoding="utf-8")
    print(relative, photo_key)
