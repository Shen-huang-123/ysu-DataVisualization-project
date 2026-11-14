"""S3 时间轴中文显示名。仅改变页面展示，计算仍保留原始小项键。"""
import re

from task2_localization import NOC_ZH

SPORT = {
    'Equestrianism':'马术','Rhythmic Gymnastics':'艺术体操',
    'Synchronized Swimming':'花样游泳','Beach Volleyball':'沙滩排球',
}
from task2_localization import SPORT_ZH
SPORT = {**SPORT_ZH, **SPORT}

DETAIL = {
    'Archery': {'Team':'团体','Individual':'个人'},
    'Athletics': {
        'Decathlon':'十项全能','Discus Throw':'铁饼','Hammer Throw':'链球',
        'High Jump':'跳高','Long Jump':'跳远','Pole Vault':'撑竿跳高',
        'Shot Put':'铅球','Standing High Jump':'立定跳高','Triple Jump':'三级跳远',
    },
    'Badminton': {'Singles':'单打','Doubles':'双打'},
    'Basketball': {'Basketball':'篮球'},
    'Beach Volleyball': {'Beach Volleyball':'沙滩排球'},
    'Boxing': {'Heavyweight':'重量级','Welterweight':'次中量级'},
    'Canoeing': {
        'Canadian Doubles, Slalom':'双人划艇激流回旋',
        'Kayak Doubles, 1,000 metres':'双人皮艇1000米',
        'Kayak Fours, 500 metres':'四人皮艇500米',
        'Kayak Singles, 500 metres':'单人皮艇500米',
    },
    'Cycling': {
        'Keirin':'凯林赛','Mountainbike, Cross-Country':'山地越野赛',
        'Sprint':'争先赛','Team Pursuit, 4,000 metres':'团体追逐赛4000米',
        'Team Sprint':'团体竞速赛','Individual Time Trial':'个人计时赛',
    },
    'Diving': {
        'Platform':'跳台','Springboard':'跳板',
        'Synchronized Platform':'双人跳台','Synchronized Springboard':'双人跳板',
    },
    'Equestrianism': {
        'Dressage, Individual':'盛装舞步个人赛',
        'Dressage, Team':'盛装舞步团体赛',
        'Three-Day Event, Individual':'三项赛个人赛',
    },
    'Fencing': {
        'Sabre, Individual':'个人佩剑','Sabre, Team':'团体佩剑',
        'epee, Individual':'个人重剑','epee, Team':'团体重剑',
        'Foil, Individual':'个人花剑',
    },
    'Football': {'Football':'足球'},
    'Gymnastics': {
        'Parallel Bars':'双杠','Team All-Around':'团体全能',
        'Balance Beam':'平衡木','Floor Exercise':'自由体操',
        'Individual All-Around':'个人全能',
    },
    'Hockey': {'Hockey':'曲棍球'},
    'Modern Pentathlon': {'Individual':'个人赛'},
    'Rhythmic Gymnastics': {'Group':'集体全能','Individual':'个人全能'},
    'Rowing': {
        'Coxed Eights':'八人单桨有舵手',
        'Coxless Fours':'四人单桨无舵手',
        'Coxless Pairs':'双人单桨无舵手',
        'Double Sculls':'双人双桨',
        'Single Sculls':'单人双桨',
        'Quadruple Sculls':'四人双桨',
    },
    'Sailing': {'One Person Dinghy':'单人艇'},
    'Shooting': {
        'Free Pistol, 50 metres':'50米自选手枪',
        'Air Pistol, 10 metres':'10米气手枪',
    },
    'Synchronized Swimming': {'Duet':'双人','Team':'集体'},
    'Table Tennis': {'Doubles':'双打','Singles':'单打','Team':'团体'},
    'Taekwondo': {'Heavyweight':'重量级','Featherweight':'羽量级','Welterweight':'次中量级'},
    'Tennis': {'Doubles':'双打'},
    'Water Polo': {'Water Polo':'水球'},
    'Weightlifting': {'Heavyweight':'重量级','Lightweight':'轻量级','Light-Heavyweight':'轻重量级'},
    'Wrestling': {
        'Featherweight, Freestyle':'自由式羽量级',
        'Flyweight, Freestyle':'自由式蝇量级',
        'Heavyweight, Freestyle':'自由式重量级',
        'Super-Heavyweight, Freestyle':'自由式超重量级',
        'Super-Heavyweight, Greco-Roman':'古典式超重量级',
        'Lightweight, Freestyle':'自由式轻量级',
        'Middleweight, Freestyle':'自由式中量级',
    },
}

def event_zh(event):
    for sport in sorted(SPORT, key=len, reverse=True):
        prefix = sport + ' '
        if not event.startswith(prefix):
            continue
        rest = event[len(prefix):]
        for gender, zh in (("Men's ",'男子'),("Women's ",'女子'),('Mixed ','混合')):
            if rest.startswith(gender):
                rest = rest[len(gender):]
                break
        else:
            raise ValueError(f'未识别性别: {event}')
        if sport in ('Athletics','Swimming') and re.fullmatch(r'(?:[\d,]+|4 x [\d,]+) metres(?: (?:Hurdles|Steeplechase|Freestyle|Backstroke|Breaststroke|Butterfly|Individual Medley|Medley))?(?: Relay)?',rest):
            detail = rest.replace(',','').replace(' metres','米').replace('Hurdles','栏').replace('Steeplechase','障碍').replace('Freestyle','自由泳').replace('Backstroke','仰泳').replace('Breaststroke','蛙泳').replace('Butterfly','蝶泳').replace('Individual Medley','个人混合泳').replace('Medley','混合泳').replace('Relay','接力').replace(' x ','×')
        else:
            detail = DETAIL.get(sport,{}).get(rest)
        if detail is None:
            raise ValueError(f'尚未翻译小项: {event}')
        return f'{SPORT[sport]}{zh}{detail}'
    raise ValueError(f'尚未翻译运动: {event}')
