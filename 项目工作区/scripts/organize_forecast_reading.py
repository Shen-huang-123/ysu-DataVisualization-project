"""Postprocess forecast pages: current baseline first, legacy scenarios opt-in.
Run after any forecast page generator and publish_project_model_audit.py.
No prediction data or old control IDs are changed.
"""
from pathlib import Path
import os
from bs4 import BeautifulSoup,Tag

ROOT=Path(__file__).resolve().parents[2]
T4=ROOT/'交付文件/任务四_开放创作'
SHARED=ROOT/'交付文件/共享组件'
PAGES=['01_交互式Dashboard/index.html','index.html','02_2028洛杉矶预测/index.html','03_数据新闻/index.html','05_满分升级/09_赛前条件回放/index.html','05_满分升级/11_官方来源门控预测/index.html','09_预测风暴实验室/index.html']
for rel in PAGES:
    p=T4/rel;s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
    if rel=='05_满分升级/11_官方来源门控预测/index.html':
        s.body['class']=list(dict.fromkeys(s.body.get('class',[])+['forecast-source-page']))
    previous=s.select_one('#legacy-scenarios')
    if previous:
        previous.find('summary',recursive=False).decompose()
        previous.select_one('.forecast-archive-note').decompose()
        previous.unwrap()
    for el in s.select('link[href*="forecast-reading.css"],script[src$="forecast-reading.js"]'):el.decompose()
    policy=s.select_one('#project-reading-policy');assert policy,rel
    archive=s.new_tag('details',id='legacy-scenarios',attrs={'class':'forecast-archive'})
    summary=s.new_tag('summary');summary.string='历史情景对照｜展开旧榜、假设与回放';archive.append(summary)
    note=s.new_tag('p',attrs={'class':'forecast-archive-note'});note.string='以下保留原版本的模型、排名或区间用于比较。它们不代表最新中性基准；滑杆仍可操作，旧区间未经本次新基准校准。';archive.append(note)
    if rel=='index.html':
        nodes=s.select('main > .narrative-layout')
        opening=s.select_one('.narrative-opening')
        if opening:
            paragraph=opening.find('p')
            if paragraph:paragraph.string='先读最新中性基准与原模型核验；旧模型故事作为历史情景单独展开。'
    elif rel=='03_数据新闻/index.html':
        nodes=s.select('body > section.章')
        header=s.select_one('header.photo-editorial-hero')
        if header:
            ps=header.find_all('p')
            if ps:ps[-1].string='最新阅读以同口径中性基准与历史检验为主；原集成叙事保留为历史情景对照。'
        policy.extract();header.insert_after(policy)
    elif rel=='09_预测风暴实验室/index.html':
        policy.extract();s.select_one('.hero').insert_after(policy)
        nodes=s.select('.wrap > main,.wrap > .backtest,.wrap > footer.note')
        hero=s.select_one('.hero p')
        if hero:hero.string='先看最新中性基准。原主场、新增运动与资格滑杆保留在历史情景中，供比较旧模型对假设的敏感性。'
    else:
        main=s.main
        nodes=[x for x in main.find_all(recursive=False) if isinstance(x,Tag) and x is not policy and x.name not in ['style','script']]
    assert nodes,rel
    nodes[0].insert_before(archive)
    for x in nodes:archive.append(x.extract())
    # Retire old recommendations that conflict with current primary reading.
    for aside in list(s.body.find_all('aside')):
        if '预测来源' in aside.get_text() and '审慎预测' in aside.get_text():archive.append(aside.extract())
    for a in s.select('a[href]'):
        if '11_官方来源门控预测' in a['href'] and '审慎' in a.get_text() and not a.find_parent(id='legacy-scenarios'):
            a.string='查看旧来源门控情景'
    if rel == '05_满分升级/11_官方来源门控预测/index.html':
        if not s.select_one('[data-ex-route-slot]'):
            archive.insert_before(s.new_tag('div', attrs={'data-ex-route-slot': '', 'hidden': ''}))
    for filename,tag in [('forecast-reading.css','link'),('forecast-reading.js','script')]:
        uri=Path(os.path.relpath(SHARED/filename,p.parent)).as_posix()
        el=s.new_tag(tag)
        if tag=='link':el['rel']='stylesheet';el['href']=uri+('?v=compact-source' if rel=='05_满分升级/11_官方来源门控预测/index.html' else '');s.head.append(el)
        else:el['src']=uri;el['defer']='';s.body.append(el)
    p.write_text(str(s),encoding='utf-8')
print('Current reading and legacy scenarios separated on six forecast pages.')
