from playwright.sync_api import sync_playwright
import json
from pathlib import Path

urls=[
 'https://www.olympics.com/en/olympic-games/london-2012/results',
 'https://olympics.com/en/olympic-games/london-2012/results',
 'https://www.olympics.com/ioc/news/ioc-executive-board-approves-olympic-medal-diploma-and-medallist-pin-reallocation-for-london-2012-olympic-games',
 'https://worldathletics.org/competitions/olympic-games/the-xxx-olympic-games-6999193/results/women/800-metres/final/result',
]
out=Path(__file__).resolve().parents[2]/'资料文件'/'外部核验'/'浏览器连通性测试'
out.mkdir(parents=True,exist_ok=True)
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',headless=True,args=['--disable-http2'])
    page=browser.new_page(locale='en-US')
    rows=[]
    for i,url in enumerate(urls):
        try:
            resp=page.goto(url,wait_until='domcontentloaded',timeout=30000)
            page.wait_for_timeout(3000)
            body=page.locator('body').inner_text(timeout=10000)
            rows.append({'url':url,'http_status':resp.status if resp else None,'title':page.title(),'body_length':len(body),'result_terms':[x for x in ['Semenya','Jelimo','Montaño','Montano'] if x.lower() in body.lower()]})
            (out/f'page_{i}.html').write_text(page.content(),encoding='utf-8')
        except Exception as e:rows.append({'url':url,'error':str(e)[:500]})
    browser.close()
(out/'result.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(rows,ensure_ascii=False))
