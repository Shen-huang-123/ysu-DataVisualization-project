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
from bs4 import BeautifulSoup
import copy
doc=BeautifulSoup(page,'html.parser')
template=BeautifulSoup((folder/'index.html').read_text(encoding='utf-8'),'html.parser')
doc.body['class']=['supplement-reading','dynasty-method-reading']
for ident in ['xz-nav','xz-menu']:
 node=template.select_one('#'+ident)
 if node:doc.body.insert(0,copy.copy(node))
assets='../../../共享组件/'
for file in ['supplement-reading.css?v=1','integrated-nav.css?v=9','unified-tables.css']:
 doc.head.append(doc.new_tag('link',rel='stylesheet',href=assets+file))
for file in ['supplement-reading.js?v=1','integrated-nav.js?v=5']:
 doc.head.append(doc.new_tag('script',src=assets+file,defer=''))
preload=doc.new_tag('script');preload.string="try{document.documentElement.dataset.suppTheme=localStorage.getItem('xz-theme')==='dark'?'dark':'light'}catch(e){}";doc.head.append(preload)
style=doc.new_tag('style');style.string='''html body.dynasty-method-reading{padding-top:76px!important}html body.dynasty-method-reading main h2{font-size:clamp(23px,2.3vw,32px)!important;font-weight:500!important;line-height:1.6!important;margin:40px 0 20px!important}html body.dynasty-method-reading main .tools{min-height:0!important} html body.dynasty-method-reading main{max-width:none!important;width:auto!important;margin:0!important;padding:32px 7vw 70px!important}html body.dynasty-method-reading main h1{max-width:none!important;font-weight:500!important;font-size:clamp(28px,2.8vw,42px)!important;line-height:1.55!important;letter-spacing:.01em!important;margin:28px 0 24px!important}html body.dynasty-method-reading main p{max-width:none!important;width:100%!important;line-height:1.95!important}html body.dynasty-method-reading .tools{background:transparent!important;border:0!important;border-bottom:1px solid #b59b6870!important;padding:0 0 20px!important}html body.dynasty-method-reading .tools a{background:transparent!important;border-radius:0!important;font-size:14px!important}html body.dynasty-method-reading main table{display:table!important;background:transparent!important}html body.dynasty-method-reading main :is(th,td){background:transparent!important;color:inherit!important}html body.dynasty-method-reading .method-table{overflow:auto;max-width:100%}@media(max-width:700px){html body.dynasty-method-reading main{padding:24px 24px 50px!important}}''';doc.head.append(style)
for table in doc.select('table'):
 wrap=doc.new_tag('div',attrs={'class':'method-table','tabindex':'0','role':'region','aria-label':'复算结果表，可横向查看'});table.wrap(wrap)
(folder/(stem+'.html')).write_text(str(doc),encoding='utf-8')
for p in (root/'交付文件').rglob('*.html'):
 if p==folder/(stem+'.html'):continue
 s=p.read_text(encoding='utf-8')
 if stem+'.md' in s:p.write_text(s.replace(stem+'.md',stem+'.html'),encoding='utf-8')
print('Published reading page and updated HTML links')
