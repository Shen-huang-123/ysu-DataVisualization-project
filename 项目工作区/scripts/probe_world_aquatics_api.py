from playwright.sync_api import sync_playwright

url='https://www.worldaquatics.com/competitions/468/olympic-games-london-2012/results'
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',headless=True)
    page=b.new_page()
    seen=[]
    page.on('response',lambda r: seen.append((r.status,r.url)) if any(t in r.url.lower() for t in ['api.','/api/','result','competition']) else None)
    try:
        page.goto(url,wait_until='domcontentloaded',timeout=30000)
        page.wait_for_timeout(9000)
        print('body',page.locator('body').inner_text(timeout=5000)[:2500])
        page.get_by_text("Women's 50m Freestyle",exact=True).first.click(timeout=5000)
        page.wait_for_timeout(5000)
        print('after',page.locator('body').inner_text(timeout=5000)[-2500:])
        print('links',[(a.inner_text()[:50],a.get_attribute('href')) for a in page.locator('a').all() if a.get_attribute('href') and 'results?' in a.get_attribute('href')][:10])
    except Exception as e:print('ERROR',str(e)[:300])
    print('responses',seen[-35:])
    b.close()
