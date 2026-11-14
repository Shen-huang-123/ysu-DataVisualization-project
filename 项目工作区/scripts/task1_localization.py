"""任务一网页的中文显示词典，原始审计字段不改。"""
from task2_localization import SPORT_ZH

SPORT_DISPLAY={**SPORT_ZH,
    'Cross-sport unresolved':'跨运动未确定',
    '3x3 Basketball':'三人篮球',
    'Artistic Gymnastics':'竞技体操',
    'Baseball':'棒球',
    'Beach Volleyball':'沙滩排球',
    'Canoe Slalom':'皮划艇激流回旋',
    'Canoe Sprint':'皮划艇静水',
    'Cycling BMX Freestyle':'自由式小轮车',
    'Cycling BMX Racing':'小轮车竞速',
    'Cycling Mountain Bike':'山地自行车',
    'Cycling Road':'公路自行车',
    'Cycling Track':'场地自行车',
    'Equestrianism':'马术',
    'Marathon Swimming':'马拉松游泳',
    'Rhythmic Gymnastics':'艺术体操',
    'Rugby Sevens':'七人制橄榄球',
    'Softball':'垒球',
    'Synchronized Swimming':'花样游泳',
    'Trampoline Gymnastics':'蹦床',
    'Trampolining':'蹦床',
}

STATUS_DISPLAY={
    'specific_label_unverified':'具体小项标签，尚未经官方逐项核验',
    'generic_or_context_required':'泛化标签，需结合项目与上下文',
}
RULE_DISPLAY={
    'identity':'原样归入同名大类',
    'family harmonization':'按同一体育大类归并',
    'multi-label same family':'复合标签归入同一大类',
    'event-level resolution required':'需结合具体小项判定',
}

def sport_display(value):
    if value in SPORT_DISPLAY:return SPORT_DISPLAY[value]
    parts=[x.strip() for x in value.split(', ')]
    if len(parts)>1 and all(x in SPORT_DISPLAY for x in parts):
        return '、'.join(SPORT_DISPLAY[x] for x in parts)
    raise ValueError(f'未翻译运动名称：{value}')
