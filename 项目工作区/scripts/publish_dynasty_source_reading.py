"""Publish UTF-8 browser reading and retain Markdown as an explicit download."""
from pathlib import Path
import markdown
root=Path(__file__).resolve().parents[2]
folder=root/'交付文件/任务三_专题深挖/S3_冠军的保质期/11_历史来源敏感性'
stem='冠军延续来源敏感性说明'
body=markdown.markdown((folder/(stem+'.md')).read_text(encoding='utf-8'),extensions=['tables','fenced_code'])
page='''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>冠军延续来源敏感性说明</title><style>
:root{color-scheme:light dark}body{margin:0;background:#edf2ef;color:#203b42;font:16px/1.95 'Microsoft YaHei',sans-serif}main{max-width:1120px;margin:auto;padding:60px 28px}h1{font-size:clamp(28px,4vw,44px);font-weight:500;line-height:1.5}h2{font-weight:500;font-size:26px;margin-top:40px}a{color:inherit;text-underline-offset:6px}table{display:block;overflow:auto;width:100%;border-collapse:collapse;font-size:14px}th,td{padding:14px 12px;border-bottom:1px solid #829a9b40;text-align:left;white-space:nowrap}th{border-bottom:1px solid #b59b68}img{max-width:100%;height:auto}.tools{display:flex;gap:24px;flex-wrap:wrap;font-size:14px;border-bottom:1px solid #b59b6870;padding-bottom:20px}@media(prefers-color-scheme:dark){body{background:#152129;color:#e8efec}}
</style></head><body><main><nav class="tools"><a href="index.html">返回来源敏感性研究</a><a href="'''+stem+'''.md" download>下载 Markdown 原文</a></nav>'''+body+'</main></body></html>'
(folder/(stem+'.html')).write_text(page,encoding='utf-8')
for p in (root/'交付文件').rglob('*.html'):
 if p==folder/(stem+'.html'):continue
 s=p.read_text(encoding='utf-8')
 if stem+'.md' in s:p.write_text(s.replace(stem+'.md',stem+'.html'),encoding='utf-8')
print('Published reading page and updated HTML links')
