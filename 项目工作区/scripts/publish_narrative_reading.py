"""Publish evidence-backed scene data and the Olympic scroll-theatre reading layer."""
from pathlib import Path
from bs4 import BeautifulSoup
import csv,json,hashlib,os
ROOT=Path(__file__).resolve().parents[2];BASE=ROOT/'交付文件';SHARED=BASE/'共享组件'
I=BASE/'任务三_专题深挖/S3_冠军的保质期/11_历史来源敏感性/固定队列三方案复算.csv'
M=BASE/'任务四_开放创作/05_满分升级/15_原项目模型时序核验'
def read(p):
 with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
intervals=[dict(n=int(r['小项数']),delta=float(r['后减前百分点']),low=float(r['区间下限']),high=float(r['区间上限'])) for r in read(I)[:3]]
scores=[r for r in read(M/'原模型五方案评分.csv') if r['选择规则']=='仅此前届次' and r['来源']=='小项二次来源']
models=[]
for y in ['2012','2016','2024']:
 row={r['模型']:float(r['MAE']) for r in scores if r['Year']==y};models.append(dict(year=y,base=row['历史加权基线'],model=row['RF60_GB40']))
us=next(r for r in read(M/'2028同口径重训情景榜.csv') if r['NOC']=='USA')
payload=dict(intervals=intervals,models=models,us=dict(base=float(us['历史加权基线']),mixed=float(us['55基线45项目'])))
payload['photos']={r['file']:dict(author=r['author'],license=r['license']) for r in json.loads((BASE/'任务三_专题深挖/媒体/图片来源与许可.json').read_text(encoding='utf-8-sig'))}
paths=['任务一_数据体检/index.html','任务二_百年全景/05_交互总览/index.html','任务三_专题深挖/统一中文入口/index.html','任务四_开放创作/index.html']
for name in paths:
 p=BASE/name;s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 d=s.select_one('#narrative-evidence-data')
 if not d:d=s.new_tag('script',attrs={'id':'narrative-evidence-data','type':'application/json'});s.head.append(d)
 d.string=json.dumps(payload,ensure_ascii=False,separators=(',',':'))
 rel=Path(os.path.relpath(SHARED,p.parent)).as_posix()
 link=s.select_one('link[href*="narrative-reading.css"]')
 if not link:link=s.new_tag('link',attrs={'rel':'stylesheet'});s.head.append(link)
 link['href']=rel+'/narrative-reading.css?v=6'
 script=s.select_one('script[src*="story-sequence.js"]');assert script,p;script['src']=rel+'/story-sequence.js?v=5';script['defer']=''
 closure=s.select_one('script[src*="research-closure.js"]')
 if closure:closure['src']=rel+'/research-closure.js?v=2'
 image_style=s.select_one('link[href*="olympic-image-stage.css"]')
 if image_style:image_style['href']=rel+'/olympic-image-stage.css?v=9'
 hero_motion=s.select_one('#hero-motion-script')
 if hero_motion and hero_motion.string:hero_motion.string=str(hero_motion.string).replace(',.xz-hero-actions','')
 # This count belongs to the old descriptive cohort, not the latest 15-case audit.
 if s.body.get('data-narrative')=='stories':
  for t in s.find_all(string=lambda t:t and '9例中8例份额上升' in t and t.parent.name not in ['script','style']):t.replace_with(str(t).replace('9例中8例份额上升','原9案描述样本中8例份额上升'))
 for style in s.select('style'):
  if style.string:style.string=str(style.string).replace('body.xz-dark button:not(#xz-theme)', 'body.xz-dark:not(.narrative-module) button:not(#xz-theme)')
 p.write_text(str(s),encoding='utf-8')
sources=[I,M/'原模型五方案评分.csv',M/'2028同口径重训情景榜.csv']
(BASE/'最终提交材料/叙事交互设计与来源.md').write_text('''# 四任务叙事交互

参考用户提供的23秒视频：场景入口、镜头推进、前后景层次和主动揭幕；不复制酒类、人物插画或商业品牌素材。使用现有奥运摄影及原来源署名。

重点参考 Noomo 的镜头章节编排（https://noomoagency.com/insights/the-power-of-digital-storytelling-website）及 Rhumb 的 Rose Island 空间叙事（https://www.rhumb.co/work/rose-island）。每段配置独立奥运照片，以透视投影的前后景推进切换；这里是摄影平面空间合成，不冒称实景三维模型。

参考 The Pudding 的问题驱动视觉叙事（https://pudding.cool/process/how-to-make-dope-shit-part-3/）和响应式叙事（https://pudding.cool/process/responsive-scrollytelling/），以及 Shorthand 的连续场景组织（https://shorthand.com/the-craft/an-introduction-to-scrollytelling/index.html）。借鉴叙事方法，不复制页面构图。

- 任务一：字段完整 → 语义风险 → 西班牙双口径名次。字段图明确为结构示意。
- 任务二：百年时间 → 单届切面 → 女性记录分母。直接读取本页归一记录，滚动不修改下方分析筛选。
- 任务三：113项原判断 → 同队列换来源 → 排除后50项区间跨零，区分来源与样本影响。
- 任务四：同单位回放误差 → 2028中性基准与条件情景 → 明示未完成验证。不将旧区间用于新基准。

桌面使用摄影背景与证据前景的连续场景，点击展开或收起证据（按钮悬停、聚焦和按下保持原位）；键盘同样可点击按钮。手机将每段与各自图表顺序排列，减少动态效果时关闭推进和揭幕动画。各任务原有图表、筛选、下载和深度页面保留。无脚本可继续读取原分析正文。

本轮控件与排版参考 IOC 品牌演进（https://www.olympics.com/ioc/news/evolving-the-look-of-the-olympic-brand）与 Gédéon 巴黎奥运动效项目（https://www.gedeon.com/projects/olympic-games-look-games）：采用清楚的文字层级、少量五色定位和章节节奏，不复制官方品牌资产。四入口同类主题、年份与视图按钮去除厚底圆角，选中细线、键盘焦点和切换反馈保留；反例面板桌面双栏、手机顺序展开。

简约叙事精修参考 Apple iPhone 产品页（https://www.apple.com/iphone/）：突出真实影像、减少重复标签及边框、保留单一主要操作；不使用Apple标识或产品素材，不隐藏证据来源。原生控件、正文和下载继续保留。第二轮优化突出桌面影像与大读数，右侧文字增加局部对比，移动端每段附对应奥运照片与署名；章节衔接采用短句与轻量链接。

复现：运行 `项目工作区/scripts/publish_narrative_reading.py` 同步四入口的数据与资源版本；共享JS/CSS直接维护。未重训或改动源CSV、正式报告数值。
''',encoding='utf-8')
(BASE/'最终提交材料/叙事交互来源记录.json').write_text(json.dumps({'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},'pages':paths,'refit':False},ensure_ascii=False,indent=2),encoding='utf-8')
print('Published four scene-driven task entries from audited inputs.')
