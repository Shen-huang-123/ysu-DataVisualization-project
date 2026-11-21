"""Supplemental Tokyo holdout using the frozen same-unit model and a baseball analogue."""
from pathlib import Path
import hashlib
import json

import numpy as np
import pandas as pd
import pyreadr

import project_model_strict_replay as core

BASE = core.OUT.parent
OUT = BASE / '17_东京补充回放'
OUT.mkdir(exist_ok=True)
ARCHIVE = core.ROOT / '资料文件/外部核验/olympicscom_抓取存档/summer_games.rda'
archive = pyreadr.read_r(str(ARCHIVE))['summer_games']
slots = archive.loc[archive.game.eq('tokyo-2020') & archive['rank'].isin(['G','S','B']),
                    ['sport','event','rank','team']].copy()
assert slots.groupby(['sport','event']).ngroups == 339 and len(slots) == 1080
NAME = dict(zip(
    "Argentina|Australia|Belarus|Belgium|Botswana|Brazil|Bulgaria|Canada|Chinese Taipei|Croatia|Denmark|Dominican Republic|Estonia|Fiji|France|Germany|Great Britain|Greece|Hong Kong, China|Hungary|India|Ireland|Israel|Italy|Jamaica|Japan|Latvia|Mexico|Netherlands|New Zealand|Norway|People's Republic of China|Poland|Republic of Korea|Romania|Serbia|Slovakia|Spain|Sweden|Ukraine|United States of America".split('|'),
    "ARG AUS BLR BEL BOT BRA BUL CAN TPE CRO DEN DOM EST FIJ FRA GER GBR GRE HKG HUN IND IRL ISR ITA JAM JPN LAT MEX NED NZL NOR CHN POL KOR ROU SRB SVK ESP SWE UKR USA".split()
))
slots['NOC'] = slots.team.map(lambda name: NAME.get(name, name))
assert slots.NOC.str.fullmatch('[A-Z]{3}').all()
assert not slots.duplicated(['sport','event','rank','NOC']).any()
slots['Year'] = 2020

def family(slug):
    name = slug.replace('-', ' ').title()
    special = {'3x3 Basketball':'Basketball', 'Rugby Sevens':'Rugby',
               'Artistic Swimming':'Synchronized Swimming', 'Baseball Softball':'Baseball/Softball'}
    return special.get(name, core.families.get(name, 'Cycling' if slug.startswith('cycling-') else name))

slots['sport_family'] = slots.sport.map(family)
slots.to_csv(OUT/'东京存档奖牌槽.csv', index=False, encoding='utf-8-sig')
source='小项二次来源'
actual = slots.groupby(['Year','NOC','sport_family']).size().rename('records').reset_index()
core.sources[source] = pd.concat([core.sources[source],actual],ignore_index=True)
core.run(source,2020)
pd.DataFrame(core.scores).to_csv(OUT/'东京核心模型评分.csv',index=False,encoding='utf-8-sig')
pred = pd.DataFrame(core.predrows)
pred.to_csv(OUT/'东京核心逐队误差.csv',index=False,encoding='utf-8-sig')
pd.DataFrame(core.audits).drop(columns='耗时秒').to_csv(OUT/'东京训练边界.csv',index=False,encoding='utf-8-sig')
wide = pred.pivot(index='NOC',columns='模型',values='预测')
a = pred.groupby('NOC')['实际'].first().reindex(wide.index)
b = wide['历史加权基线']
p = wide['RF60_GB40']
pool = b.sum()
# Freeze the 18% cap used by the prior ex-ante scenario. Tokyo host was known.
# Archived results are targets only, including for any NOC outside the candidate pool.
rank = pd.Series({'JPN':1,'KOR':2,'MEX':3,'USA':4},name='2019 Premier12名次')
assert rank.index.isin(wide.index).all()
signal = 1/rank
signal = (signal/signal.sum()).reindex(wide.index,fill_value=0)
qualification = pd.Series({'JPN':True,'KOR':True,'MEX':True,'USA':True,'DOM':True,'ISR':True})
pd.DataFrame({'东京棒球参赛':qualification,'2019 Premier12前四名次':rank.reindex(qualification.index)}).to_csv(OUT/'东京棒球排名输入.csv',encoding='utf-8-sig')
detail = pd.DataFrame({'实际奖牌槽':a,'棒球信号单位':signal})
scores = []
for name, bonus in [('关闭排名',signal*0),('加入棒球赛前信号',signal)]:
    forecast = .45*b+.45*p+.10*(b+bonus)
    forecast.loc['JPN'] *= 1+.18*.55
    forecast = forecast/forecast.sum()*pool
    assert np.isclose(forecast.sum(),pool)
    detail[name] = forecast
    error = forecast-a
    scores.append({'情景':name,'全体MAE':error.abs().mean(),'至少5槽MAE':error[a.ge(5)].abs().mean(),
                   'RMSE':np.sqrt((error**2).mean()),'前十重合':len(set(forecast.nlargest(10).index)&set(a.nlargest(10).index)),
                   '估计池':pool,'实际池_仅评分':a.sum()})
detail.to_csv(OUT/'东京完整配方逐队对照.csv',encoding='utf-8-sig')
pd.DataFrame(scores).to_csv(OUT/'东京完整配方评分.csv',index=False,encoding='utf-8-sig')
(OUT/'东京输入清单.json').write_text(json.dumps({
    'archive_sha256':hashlib.sha256(ARCHIVE.read_bytes()).hexdigest(),
    'strict_replay_protocol':'../15_原项目模型时序核验/输入哈希与模型协议.json',
    'programme_source':'https://www.olympics.com/ioc/tokyo-2020-facts-and-figures',
    'ranking_source':'https://static.wbsc.org/uploads/federations/278/cms/documents/8d9568c2-596e-53fe-f532-d1c35832aaaa.pdf',
    'entry_source':'https://library.olympics.com/digitalCollection/DigitalCollectionAttachmentDownloadHandler.ashx?documentId=849110&parentDocumentId=849101'
},ensure_ascii=False,indent=2),encoding='utf-8')
print(pd.DataFrame(scores).to_string(index=False))
