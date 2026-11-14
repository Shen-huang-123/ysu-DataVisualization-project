"""Apply the Olympic editorial system and remove the retired 3D medal."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DELIVERY = ROOT / '交付文件'
SITE = ROOT / '项目工作区/sites/la28-fullscore/dist'
ENTRIES = {
    '作品总入口/index.html',
    '任务一_数据体检/index.html',
    '任务二_百年全景/05_交互总览/index.html',
    '任务三_专题深挖/统一中文入口/index.html',
    '任务四_开放创作/index.html',
}
RAILS = {
    '作品总入口/index.html': ('总览', '四个任务 · 一条证据链'),
    '任务一_数据体检/index.html': ('01 数据体检', '从可信口径开始'),
    '任务二_百年全景/05_交互总览/index.html': ('02 百年全景', '从一届赛事看见一个世纪'),
    '任务三_专题深挖/统一中文入口/index.html': ('03 专题深挖', '十个问题，十条线索'),
    '任务四_开放创作/index.html': ('04 开放创作', '把历史证据带向未来'),
}

STYLE = '''<style id="olympic-editorial-style">
/* Editorial art direction: archival sport photography, warm paper, precise type. */
::selection{background:#c2a46c;color:#101c24}
#xz-nav{background:#101e24ed!important;border-bottom:1px solid #e6dcc444!important;backdrop-filter:blur(18px)!important}
#xz-menu{background:#152930e8!important;backdrop-filter:blur(24px) saturate(1.3)!important;border:1px solid #e9e2d655!important;box-shadow:0 24px 70px #08171c55!important}
#xz-nav .xz-mark{background:#b79b6a!important;color:#17252b!important;box-shadow:none!important;border-radius:2px!important}
#xz-nav .xz-brand,#xz-nav .xz-links a,#xz-nav button{color:#f4eee2!important}
#xz-progress{background:linear-gradient(90deg,#2b7894 0 20%,#b9a16e 20% 40%,#d4d4cf 40% 60%,#5f9d86 60% 80%,#ba6570 80% 100%)!important}
body.ed-entry{--ed-ink:#14272c;--ed-paper:#f5f1e8;--ed-gold:#b79b6a}
body.ed-entry{background:#f5f1e8!important;color:#14272c!important}
body.ed-entry :is(.xz-section-top h2,.section-head h2,main h2){letter-spacing:-.04em}
body.ed-entry header.photo-editorial-hero,body.ed-entry header.hero{border-radius:0!important;box-shadow:none!important;border-bottom:1px solid #b8a177!important}
body.ed-entry header.photo-editorial-hero:before,body.ed-entry header.hero:before{content:'';position:absolute;top:0;left:0;width:100%;height:4px;background:linear-gradient(90deg,#3d8095 0 20%,#b99d65 20% 40%,#e4e2d8 40% 60%,#659d88 60% 80%,#bc6570 80% 100%);z-index:8}
body.ed-entry header.photo-editorial-hero:after,body.ed-entry header.hero .hero-graphic{display:none!important}
body.ed-entry header.photo-editorial-hero:after{display:block!important;content:'';position:absolute;left:clamp(16px,3vw,56px)!important;top:clamp(80px,10vh,120px)!important;bottom:clamp(30px,5vh,75px);width:min(72%,870px)!important;height:auto!important;border:1px solid #ffffff55;border-radius:5px;background:linear-gradient(125deg,#0e2933bd,#0e29338c 52%,#1c3f4752);box-shadow:inset 0 1px #ffffff35,0 25px 60px #07171a3d;backdrop-filter:blur(20px) saturate(1.15);-webkit-backdrop-filter:blur(20px) saturate(1.15);transform:translate3d(var(--ed-x,0px),var(--ed-y,0px),0);transition:transform .35s ease;z-index:1;pointer-events:none}
body.ed-entry header.photo-editorial-hero>*:not(.ed-particles){position:relative;z-index:3}
body.ed-entry header.hero .hero-copy{background:#102b33a6;border:1px solid #ffffff55;border-radius:5px;box-shadow:inset 0 1px #ffffff30,0 25px 60px #07171a3d;backdrop-filter:blur(20px) saturate(1.15);-webkit-backdrop-filter:blur(20px) saturate(1.15);padding:clamp(24px,3.2vw,48px);max-width:min(780px,72%)}
body.ed-entry .xz-path>a{background:#ffffffa8!important;backdrop-filter:blur(16px) saturate(1.12);-webkit-backdrop-filter:blur(16px) saturate(1.12);border:1px solid #ffffffdb!important;box-shadow:0 15px 40px #324a4812,inset 0 1px #fff!important}
body.ed-entry .xz-path>a:hover{background:#fffef2d9!important;box-shadow:0 25px 50px #324a4820!important}
body.ed-entry.xz-dark .xz-path>a{background:#1a3039ce!important;color:#f4eee2!important;border-color:#ffffff35!important}
body.ed-entry :is(.filters,.controls,.toolbar){backdrop-filter:blur(16px) saturate(1.1);-webkit-backdrop-filter:blur(16px) saturate(1.1)}
body.ed-entry header.photo-editorial-hero h1,body.ed-entry header.hero h1{font-family:'Noto Serif SC','Songti SC','SimSun',Georgia,serif!important;font-weight:600!important;letter-spacing:-.065em!important;line-height:1.16!important;text-wrap:balance;text-shadow:0 4px 28px #081b1d88}
body.ed-entry header.photo-editorial-hero :is(.xz-eyebrow,.eyebrow,.tag),body.ed-entry header.hero :is(.xz-eyebrow,.eyebrow,.tag){font-size:12px!important;letter-spacing:.24em!important;text-transform:uppercase;color:#dfc996!important}
body.ed-entry header.photo-editorial-hero :is(.xz-lead,.lead),body.ed-entry header.hero .hero-copy p{max-width:660px!important;font-size:clamp(16px,1.4vw,20px)!important;line-height:1.8!important;color:#f1eee5!important}
body.ed-entry :is(.xz-primary,.xz-secondary){border-radius:2px!important;box-shadow:none!important;min-height:48px!important;letter-spacing:.03em}
body.ed-entry .xz-primary{background:#c3a66e!important;color:#17282e!important;border-color:#c3a66e!important}
body.ed-entry .xz-secondary{background:transparent!important;color:#f5f0e4!important;border:1px solid #e9e0cd9c!important}
body.ed-entry :is(.xz-primary,.xz-secondary):hover{transform:translateY(-3px)!important;filter:brightness(1.08)}
body.ed-entry :is(.xz-path>a,.topic-card,.story-card){border-radius:2px!important;box-shadow:none!important;transition:transform .45s cubic-bezier(.22,1,.36,1),border-color .3s ease,background .3s ease!important}
body.ed-entry :is(.xz-path>a,.topic-card,.story-card):hover{transform:translateY(-5px)!important;border-color:#b89b66!important}
body.ed-entry .xz-section-top{border-top:1px solid #b1a996!important;padding-top:28px!important}
body.ed-entry .xz-section-top>span{font-size:11px!important;font-weight:800;letter-spacing:.18em;text-transform:uppercase;color:#8e7651!important}
body.hero-motion.ed-entry header.photo-editorial-hero,body.hero-motion.hero-motion-portal.ed-entry header.hero{height:auto!important;min-height:clamp(620px,78vh,870px)!important;max-height:none!important;overflow:hidden!important}
body.hero-motion.ed-entry header.photo-editorial-hero{padding:clamp(100px,12vh,160px) clamp(28px,6vw,100px) clamp(75px,9vh,120px)!important}
body.ed-entry header.photo-editorial-hero h1{max-width:min(850px,68%)!important;margin:.22em 0 .3em!important}
body.ed-entry header.photo-editorial-hero .xz-lead,body.ed-entry header.photo-editorial-hero .xz-hero-actions{max-width:min(660px,68%)!important}
body.ed-entry header.hero .hero-copy{position:relative;z-index:3}
.ed-particles{position:absolute!important;left:0;right:0;top:0;z-index:40!important;overflow:hidden;pointer-events:none;contain:paint;opacity:.42}
.ed-particle{position:absolute;top:var(--start);left:var(--left);width:var(--size);height:calc(var(--size)*2.8);border-radius:999px;background:var(--color);opacity:0;transform:translate3d(0,-20px,0) rotate(var(--turn));animation:ed-fall var(--duration) linear var(--delay) infinite;will-change:transform,opacity}
.ed-particle:nth-child(3n){height:var(--size);border-radius:50%}
@keyframes ed-fall{0%{opacity:0;transform:translate3d(0,-20px,0) rotate(var(--turn))}12%{opacity:.48}78%{opacity:.35}100%{opacity:0;transform:translate3d(var(--drift),var(--travel),0) rotate(calc(var(--turn) + 240deg))}}
/* One material system across hero, cards and controls. */
body.ed-entry header.photo-editorial-hero:after{border-radius:26px!important;background:linear-gradient(125deg,#112d39d9,#173b468c 56%,#244e565e)!important;border:1px solid #ffffff75!important;box-shadow:inset 0 1px #ffffff70,0 25px 70px #06191c4d!important;backdrop-filter:blur(26px) saturate(1.2)!important;-webkit-backdrop-filter:blur(26px) saturate(1.2)!important}
body.ed-entry header.hero .hero-copy{border-radius:26px!important;background:linear-gradient(125deg,#112d39d0,#173b4699)!important;border-color:#ffffff75!important;backdrop-filter:blur(26px) saturate(1.2)!important;-webkit-backdrop-filter:blur(26px) saturate(1.2)!important}
body.ed-entry .xz-path>a{border-radius:20px!important;background:#ffffffb9!important;border:1px solid #ffffffed!important;box-shadow:0 12px 36px #263f4112,inset 0 1px #fff!important;backdrop-filter:blur(24px) saturate(1.14)!important;-webkit-backdrop-filter:blur(24px) saturate(1.14)!important}
body.ed-entry :is(.xz-primary,.xz-secondary){border-radius:999px!important;padding-inline:24px!important;transition:transform .28s cubic-bezier(.22,1,.36,1),background .28s,box-shadow .28s!important}
body.ed-entry :is(.xz-primary,.xz-secondary):active{transform:translateY(1px) scale(.985)!important}
body.ed-entry :is(.filters,.controls,.toolbar){border-radius:18px;backdrop-filter:blur(20px) saturate(1.15);-webkit-backdrop-filter:blur(20px) saturate(1.15)}
#xz-menu{border-radius:20px!important}
#xz-menu{color:#f5f0e6!important}
#xz-menu a{color:#f5f0e6!important}
#xz-menu small{color:#b9cdc9!important}
#xz-menu a:hover{background:#ffffff20!important}
#xz-nav .xz-mark{border-radius:50%!important;box-shadow:inset 0 0 0 1px #fff9,0 0 0 3px #c9b98c33!important}
body.ed-entry .xz-path>a{color:#1b343a!important;padding:clamp(26px,3vw,38px)!important;min-height:250px}
body.ed-entry .xz-path h3{color:inherit!important;font-family:'Noto Serif SC','Songti SC','SimSun',Georgia,serif!important;font-weight:600!important;letter-spacing:-.035em}
body.ed-entry .xz-path p{color:#526970!important;line-height:1.75!important}
body.ed-entry .xz-path small{color:#8f784e!important}
body.ed-entry .xz-path strong{color:#2c6571!important}
body.ed-entry .xz-path>a:after{font-family:Georgia,serif;font-size:clamp(104px,12vw,170px)!important;font-weight:400!important;color:#b7aa8d25!important;bottom:-35px!important;right:14px!important}
body.ed-entry.xz-dark .xz-path>a{color:#f4eee2!important}
body.ed-entry.xz-dark .xz-path p{color:#c6d6d6!important}
body.ed-entry.xz-dark .xz-path strong{color:#b4d7cf!important}
body.ed-entry{transition:background-color .35s ease,color .35s ease}
body.ed-entry.xz-dark{background:#0b1d24!important;color:#edf5ef!important}
body.ed-entry.xz-dark :is(.xz-section-top h2,.section-head h2,main h2){color:#f1f3e9!important}
body.ed-entry.xz-dark .xz-section-top{border-color:#436069!important}
body.ed-entry.xz-dark .xz-section-top>span{color:#d6ba80!important}
body.ed-entry.ed-home.xz-dark .xz-path>a{background:#142d35!important;color:#f4eee2!important;backdrop-filter:none!important}
body.ed-entry.ed-home.xz-dark .xz-path>a:hover{background:#1c3b43!important}
/* Dark mode needs a dark card surface as well as light text. */
body.ed-entry.xz-dark:not(.ed-home) .xz-path>a{background:#18343c!important;color:#f2f4ec!important;border-color:#4a6870!important;box-shadow:0 14px 36px #06151b66,inset 0 1px #ffffff19!important}
body.ed-entry.xz-dark:not(.ed-home) .xz-path>a:hover{background:#21444c!important;border-color:#83a99c!important}
body.ed-entry.xz-dark .xz-path small{color:#d7bd88!important}
body.ed-entry.xz-dark .xz-path p{color:#c8d9d5!important}
body.ed-entry.xz-dark .xz-path strong{color:#9bd7ca!important}
body.xz-dark.ed-module-2 main .card,body.xz-dark.ed-module-1 main .xz-kpis article{background:#17333b!important;color:#edf3eb!important;border-color:#49626b!important}
body.xz-dark.ed-module-2 main .card small,body.xz-dark.ed-module-1 main .xz-kpis span{color:#c5d8d3!important}
body.xz-dark.ed-module-1 main .ip-context h2,body.xz-dark.ed-module-2 main .t2-intro h2,body.xz-dark.ed-module-3 main .section-head h2{color:#eef3eb!important}
body.xz-dark.ed-module-1 main .ip-context p,body.xz-dark.ed-module-2 main .t2-intro p,body.xz-dark.ed-module-3 main .section-head p{color:#c2d5d0!important}
body.xz-dark.ed-module-2 main .cards .big{color:#8edbd1!important}
body.xz-dark.ed-module-2 main .cards .card:first-child .big{color:#f4f4e8!important}
body.xz-dark.ed-module-2 main .filters label{color:#d8e9e4!important}
body.xz-dark.ed-module-2 main .filters select{background:#193841!important;color:#eef5ee!important;border-color:#5c7b7e!important}
body.xz-dark.ed-module-3 main .filters button:not(.active){color:#e6f0e9!important;border-color:#6d8987!important}
/* Leaderboards and their controls must retain contrast after theme changes. */
body.xz-dark.interactive-polish :is(.controls,.控制,.xz-toolbar){background:#193841!important;border-color:#52767b!important;color:#edf5ef!important}
body.xz-dark.interactive-polish :is(.ip-field,.ip-context p,.section-head p){color:#cbded8!important}
body.xz-dark.interactive-polish :is(select,input:not([type=range])){background:#102a32!important;color:#f0f6ef!important;border-color:#638287!important}
body.xz-dark.interactive-polish :is(.card,.卡,.xz-kpis article){background:#17333b!important;color:#edf5ef!important;border-color:#527078!important}
body.xz-dark.interactive-polish :is(.card small,.卡 small,.xz-kpis span){color:#c7dad4!important}
body.xz-dark.interactive-polish table{background:#142d35!important;color:#edf5ef!important;border-color:#4b6970!important}
body.xz-dark.interactive-polish tbody tr:nth-child(even){background:#1b3b42!important}
body.xz-dark.interactive-polish tbody tr:hover{background:#254b50!important}
body.xz-dark.interactive-polish tbody :is(th,td){color:#edf5ef!important;border-color:#3d5d63!important}
body.xz-dark.interactive-polish thead th{color:#f2f8f3!important}
body.xz-dark :is(#榜,.榜) .行{color:#edf5ef!important;border-color:#47646b!important}
body.xz-dark :is(#榜,.榜) .行 b{color:#f4f7ef!important}
body.xz-dark :is(#榜,.榜) .区间{color:#c8dad3!important}
body.xz-dark :is(#榜,.榜) .轨{background:#35545a!important}
/* Task 2 atlas: the section headed “谁参与，谁留下成绩？” has its own light palette. */
body.xz-dark.task2-redesign main .t2-section-head h2{color:#f2f7f1!important}
body.xz-dark.task2-redesign main .t2-section-head p{color:#c8dad5!important}
body.xz-dark.task2-redesign main .t2-section-head span{color:#e2bf83!important}
body.xz-dark.task2-redesign main .t2-table-wrap{background:#142d35!important;border-color:#527078!important;box-shadow:0 14px 34px #07192155!important}
body.xz-dark.task2-redesign main .t2-table-wrap table{background:#142d35!important;color:#edf5ef!important}
body.xz-dark.task2-redesign main .t2-table-wrap thead th{background:#1d4148!important;color:#f2f8f2!important}
body.xz-dark.task2-redesign main .t2-table-wrap tbody td{color:#edf5ef!important;border-color:#45646b!important}
body.xz-dark.task2-redesign main .t2-table-wrap tbody tr:nth-child(even){background:#1d3941!important}
body.xz-dark.task2-redesign main .t2-table-wrap tbody tr:hover{background:#285158!important}
/* Photo-led chapters establish a clear visual hierarchy on the home page. */
body.ed-home main .xz-section:first-of-type .xz-path>a{min-height:330px!important;display:flex!important;flex-direction:column;justify-content:flex-end;background-color:#132b33!important;background-size:cover!important;background-position:center!important;color:#fff9ed!important;border-color:#ffffff47!important;box-shadow:0 18px 42px #0c29312b!important}
body.ed-home main .xz-section:first-of-type .xz-path>a:nth-child(1){background-image:linear-gradient(0deg,#09232be8,#17343b51),url('../任务三_专题深挖/媒体/archive.jpg')!important}
body.ed-home main .xz-section:first-of-type .xz-path>a:nth-child(2){background-image:linear-gradient(0deg,#09232be8,#17343b51),url('../任务三_专题深挖/媒体/growth.jpg')!important}
body.ed-home main .xz-section:first-of-type .xz-path>a:nth-child(3){background-image:linear-gradient(0deg,#09232be8,#17343b51),url('../任务三_专题深挖/媒体/dynasty.jpg')!important}
body.ed-home main .xz-section:first-of-type .xz-path>a:nth-child(4){background-image:linear-gradient(0deg,#09232be8,#17343b51),url('../任务三_专题深挖/媒体/la.jpg')!important}
body.ed-home main .xz-section:first-of-type .xz-path>a :is(h3,p,small,strong){position:relative;z-index:2;color:#fff9ed!important;text-shadow:0 2px 16px #061b20aa}
body.ed-home main .xz-section:first-of-type .xz-path>a small{color:#e7cd97!important}
body.ed-home main .xz-section:first-of-type .xz-path>a strong{margin-top:12px;color:#f6d99f!important}
body.ed-home main .xz-section:first-of-type .xz-path>a:after{color:#ffffff19!important}
body.ed-entry .xz-section{padding-block:clamp(84px,9vw,132px)!important}
body.ed-entry :is(.xz-section-top h2,.section-head h2){font-family:'Noto Serif SC','Songti SC','SimSun',Georgia,serif!important;font-weight:600!important;line-height:1.2!important;letter-spacing:-.045em!important}
body.ed-entry.ed-home header.photo-editorial-hero:after{display:none!important;content:none!important}
body.ed-entry.ed-home .xz-path>a{background:#fffdfa!important;backdrop-filter:none!important;-webkit-backdrop-filter:none!important}
/* Cover typography lives directly on photography; no glass screen on any entry. */
body.ed-entry header.photo-editorial-hero:after{display:none!important;content:none!important}
body.ed-entry header.hero .hero-copy{background:transparent!important;border:0!important;border-radius:0!important;box-shadow:none!important;backdrop-filter:none!important;-webkit-backdrop-filter:none!important;padding:0!important}
body.ed-entry header.photo-editorial-hero h1,body.ed-entry header.hero h1{animation:ed-type-in .9s cubic-bezier(.22,1,.36,1) both;animation-delay:.08s;text-shadow:0 5px 26px #061b23bb!important}
body.ed-entry header.photo-editorial-hero :is(.xz-eyebrow,.eyebrow),body.ed-entry header.hero .eyebrow{animation:ed-type-in .65s cubic-bezier(.22,1,.36,1) both}
body.ed-entry header.photo-editorial-hero :is(.xz-lead,.lead),body.ed-entry header.hero .hero-copy p{animation:ed-type-in .9s cubic-bezier(.22,1,.36,1) .22s both;text-shadow:0 2px 16px #061b23af}
body.ed-entry header.photo-editorial-hero .xz-hero-actions{animation:ed-type-in .9s cubic-bezier(.22,1,.36,1) .36s both}
body.ed-entry header.photo-editorial-hero :is(h1,.xz-eyebrow,.xz-lead,.xz-hero-actions){translate:0 var(--ed-text-y,0px)}
body.ed-entry header.hero .hero-copy{translate:0 var(--ed-text-y,0px)}
body.ed-entry header.photo-editorial-hero h1 em,body.ed-entry header.hero h1 em{color:#e4c48d!important}
@keyframes ed-type-in{from{opacity:0;transform:translateY(28px);filter:blur(5px)}to{opacity:1;transform:translateY(0);filter:blur(0)}}
#xz-nav .xz-links a{position:relative}
#xz-nav .xz-links a:after{content:'';position:absolute;left:12px;right:12px;bottom:5px;height:1px;background:#d6b776;transform:scaleX(0);transform-origin:left;transition:transform .35s cubic-bezier(.22,1,.36,1)}
#xz-nav .xz-links a:hover:after,#xz-nav .xz-links a[aria-current="page"]:after{transform:scaleX(1)}
@view-transition{navigation:auto}
::view-transition-old(root){animation:.22s ease-in both ed-page-out}
::view-transition-new(root){animation:.48s cubic-bezier(.22,1,.36,1) both ed-page-in}
@keyframes ed-page-out{to{opacity:0;transform:translateX(-14px)}}
@keyframes ed-page-in{from{opacity:0;transform:translateX(14px)}}
body.ed-motion-ready .ed-reveal{opacity:0;transform:translateY(22px);transition:opacity .7s ease,transform .7s cubic-bezier(.22,1,.36,1)}
body.ed-motion-ready .ed-reveal.ed-visible{opacity:1;transform:none}
/* Track markings and five-color lane signals tie all four task chapters together. */
body.ed-module-0{--ed-module:#bb9b61}body.ed-module-1{--ed-module:#5d94af}body.ed-module-2{--ed-module:#65a58b}body.ed-module-3{--ed-module:#c7a76f}body.ed-module-4{--ed-module:#bc737b}
.ed-chapter-rail{position:relative;z-index:2;display:flex;align-items:center;gap:clamp(18px,3vw,46px);min-height:74px;padding:12px clamp(22px,6vw,100px);background:#10262e;color:#f6f1e7;border-bottom:1px solid #e5d5b542;font:700 13px/1.3 'Microsoft YaHei',system-ui,sans-serif;letter-spacing:.09em}
.ed-rail-name{white-space:nowrap;color:#f3e5c9}.ed-rail-caption{margin-left:auto;font-size:12px;color:#b8ccc9;letter-spacing:.12em;text-align:right}
.ed-rail-lanes{display:flex;align-items:center;gap:5px;min-width:138px}.ed-rail-lanes i{display:block;width:22px;height:3px;border-radius:99px;background:var(--lane);opacity:.9;animation:ed-lane 3.6s ease-in-out infinite;animation-delay:var(--delay)}
.ed-rail-lanes i:nth-child(1){--lane:#4e95ae;--delay:0s}.ed-rail-lanes i:nth-child(2){--lane:#c8a764;--delay:.18s}.ed-rail-lanes i:nth-child(3){--lane:#e6e6dc;--delay:.36s}.ed-rail-lanes i:nth-child(4){--lane:#6eaa90;--delay:.54s}.ed-rail-lanes i:nth-child(5){--lane:#c57077;--delay:.72s}
@keyframes ed-lane{0%,70%,100%{opacity:.5;transform:scaleX(.88)}35%{opacity:1;transform:scaleX(1)}}
body[class*="ed-module-"] main :is(.xz-section-top>span,.ip-context small,.t2-kicker,.section-head small){color:var(--ed-module)!important}
body.ed-entry header.photo-editorial-hero .xz-eyebrow:before{background:var(--ed-module)!important;width:28px!important;height:3px!important}
body.ed-entry main .xz-section-top{border-top:1px solid color-mix(in srgb,var(--ed-module) 45%,#aeb9b6)!important}
body.ed-entry main .xz-path>a:before{background:linear-gradient(90deg,var(--ed-module),#dccba5)!important}
body.ed-module-1 main .ip-context,body.ed-module-2 main .t2-intro,body.ed-module-3 main .section-head,body.ed-module-4 main .xz-note{border-left:3px solid var(--ed-module)!important;padding-left:clamp(18px,2.5vw,34px)!important}
@media(max-width:700px){.ed-chapter-rail{min-height:62px;gap:16px;padding-inline:20px}.ed-rail-lanes{min-width:0}.ed-rail-lanes i{width:13px}.ed-rail-caption{display:none}}
@media(prefers-reduced-motion:reduce){.ed-rail-lanes i{animation:none!important;opacity:1;transform:none}}
@media(max-width:800px){body.ed-entry header.photo-editorial-hero h1,body.ed-entry header.photo-editorial-hero .xz-lead,body.ed-entry header.photo-editorial-hero .xz-hero-actions{max-width:100%!important}body.hero-motion.ed-entry header.photo-editorial-hero,body.hero-motion.hero-motion-portal.ed-entry header.hero{min-height:0!important}body.hero-motion.ed-entry header.photo-editorial-hero{padding:92px 22px 70px!important}body.ed-entry header.photo-editorial-hero h1{font-size:clamp(42px,8.5vw,70px)!important;line-height:1.2!important}body.ed-entry header.photo-editorial-hero:after{left:10px;right:10px;top:72px;bottom:20px;width:auto}body.ed-entry header.hero .hero-copy{max-width:100%}.ed-particle:nth-child(n+13){display:none}.ed-particles{opacity:.46}}
@media(prefers-reduced-motion:reduce){body.ed-motion-ready .ed-reveal{opacity:1!important;transform:none!important;transition:none!important}.ed-particles{display:none!important}body.ed-entry header.photo-editorial-hero:after{transform:none!important}::view-transition-old(root),::view-transition-new(root){animation-duration:.01ms!important}}
@media(prefers-reduced-motion:reduce){body.ed-entry header.photo-editorial-hero :is(h1,.xz-eyebrow,.xz-lead,.xz-hero-actions),body.ed-entry header.hero :is(.hero-copy,.eyebrow,h1,p){animation:none!important;translate:none!important;filter:none!important}}
/* A small spatial Olympic emblem lives in the free side of photographic covers. */
header.photo-editorial-hero,header.hero{isolation:isolate}
.ed-rings-scene{position:absolute!important;right:clamp(28px,6vw,112px);top:50%;width:clamp(190px,25vw,350px);aspect-ratio:1.55;z-index:2!important;pointer-events:none;perspective:900px;transform:translateY(-38%);opacity:.88;filter:drop-shadow(0 24px 22px #06192088)}
.ed-rings-plate{position:absolute;inset:0;transform-style:preserve-3d;transform:rotateX(calc(-13deg + var(--ed-ring-x,0deg))) rotateY(calc(-17deg + var(--ed-ring-y,0deg)));animation:ed-rings-breathe 8s ease-in-out infinite;will-change:transform}
.ed-ring{position:absolute;width:34%;aspect-ratio:1;border:clamp(7px,.9vw,12px) solid var(--ring-color);border-radius:50%;box-shadow:inset 2px 3px 3px #ffffffa0,inset -3px -4px 5px #05171b77,2px 5px 0 color-mix(in srgb,var(--ring-color) 58%,#06161c),5px 11px 18px #06181b7d;transform:translateZ(var(--ring-z));opacity:.98}
.ed-ring:nth-child(1){left:1%;top:5%;--ring-color:#2489be;--ring-z:16px}.ed-ring:nth-child(2){left:33%;top:5%;--ring-color:#222e35;--ring-z:8px}.ed-ring:nth-child(3){left:65%;top:5%;--ring-color:#d44d55;--ring-z:16px}.ed-ring:nth-child(4){left:17%;top:38%;--ring-color:#e9b73d;--ring-z:22px}.ed-ring:nth-child(5){left:49%;top:38%;--ring-color:#4aa479;--ring-z:22px}
.ed-rings-scene:before{content:'';position:absolute;inset:-18% -12%;border-radius:50%;background:radial-gradient(ellipse,#f4dca329,transparent 67%);filter:blur(15px)}
@keyframes ed-rings-breathe{0%,100%{transform:rotateX(calc(-13deg + var(--ed-ring-x,0deg))) rotateY(calc(-17deg + var(--ed-ring-y,0deg))) translateY(0)}50%{transform:rotateX(calc(-9deg + var(--ed-ring-x,0deg))) rotateY(calc(-10deg + var(--ed-ring-y,0deg))) translateY(-9px)}}
body.xz-dark .ed-rings-scene{opacity:.96;filter:drop-shadow(0 24px 24px #020b0dcc)}
@media(max-width:900px){.ed-rings-scene{right:22px;top:auto;bottom:32px;width:clamp(150px,27vw,215px);transform:none;opacity:.54}body.ed-entry header.photo-editorial-hero h1{max-width:100%!important}}
@media(max-width:600px){.ed-rings-scene{width:130px;right:12px;bottom:14px;opacity:.35}}
@media(prefers-reduced-motion:reduce){.ed-rings-plate{animation:none!important;will-change:auto}}
</style>'''

SCRIPT = '''<script id="olympic-editorial-script">(()=>{
const crest=document.querySelector('header.photo-editorial-hero,header.hero');
if(crest&&!crest.querySelector('.ed-rings-scene')){
  const scene=document.createElement('div');scene.className='ed-rings-scene';scene.setAttribute('aria-hidden','true');
  scene.innerHTML='<div class="ed-rings-plate"><i class="ed-ring"></i><i class="ed-ring"></i><i class="ed-ring"></i><i class="ed-ring"></i><i class="ed-ring"></i></div>';
  crest.appendChild(scene);
}
if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;
if(crest&&matchMedia('(pointer:fine) and (min-width:901px)').matches){
  let frame=0;crest.addEventListener('pointermove',event=>{if(frame)return;frame=requestAnimationFrame(()=>{
    const r=crest.getBoundingClientRect(),x=(event.clientX-r.left)/r.width-.5,y=(event.clientY-r.top)/r.height-.5;
    crest.style.setProperty('--ed-ring-y',(x*11).toFixed(1)+'deg');crest.style.setProperty('--ed-ring-x',(-y*8).toFixed(1)+'deg');frame=0;
  })},{passive:true});crest.addEventListener('pointerleave',()=>{crest.style.setProperty('--ed-ring-x','0deg');crest.style.setProperty('--ed-ring-y','0deg')});
}
const colors=['#4288a3','#c3a56d','#e7e3d7','#6aa68c','#bd6c73'];
const layer=document.createElement('div');layer.className='ed-particles';layer.setAttribute('aria-hidden','true');document.body.appendChild(layer);
let dots=[];
function placeParticles(){
  const height=Math.max(document.documentElement.scrollHeight,document.body.scrollHeight,innerHeight);
  const count=Math.min(44,Math.max(18,Math.ceil(height/270)));
  layer.style.height=height+'px';
  if(dots.length!==count){layer.replaceChildren();dots=[];for(let i=0;i<count;i++){const dot=document.createElement('i');dot.className='ed-particle';layer.appendChild(dot);dots.push(dot)}}
  dots.forEach((dot,i)=>{const start=(i+.18)/count*height,travel=Math.max(70,height-start);const duration=Math.max(14,travel/75);dot.style.cssText=`--left:${(i*37+9)%97}%;--start:${start.toFixed(0)}px;--travel:${travel.toFixed(0)}px;--size:${2+i%4}px;--color:${colors[i%5]};--duration:${duration.toFixed(1)}s;--delay:${(-i*2.3%duration).toFixed(1)}s;--drift:${(i%2?1:-1)*(28+i%6*15)}px;--turn:${i*27}deg`})
}
placeParticles();
addEventListener('load',placeParticles,{once:true});
addEventListener('resize',placeParticles,{passive:true});
if('ResizeObserver'in window)new ResizeObserver(()=>requestAnimationFrame(placeParticles)).observe(document.body);
for(const hero of document.querySelectorAll('body.ed-entry header.photo-editorial-hero,body.ed-entry header.hero')){
  hero.style.setProperty('--ed-text-y','0px');
}
if(matchMedia('(min-width:801px)').matches){
  const heroes=[...document.querySelectorAll('body.ed-entry header.photo-editorial-hero,body.ed-entry header.hero')];let frame=0;
  addEventListener('scroll',()=>{if(frame)return;frame=requestAnimationFrame(()=>{for(const hero of heroes){const r=hero.getBoundingClientRect();if(r.bottom>0&&r.top<innerHeight)hero.style.setProperty('--ed-text-y',Math.max(-24,Math.min(24,-r.top*.045)).toFixed(1)+'px')}frame=0})},{passive:true});
}
if(!('IntersectionObserver'in window))return;
const els=[...document.querySelectorAll('main .xz-section-top,main .section-head,main h2,main .xz-path>a')].slice(0,45);
const observer=new IntersectionObserver(entries=>{for(const entry of entries)if(entry.isIntersecting){entry.target.classList.add('ed-visible');observer.unobserve(entry.target)}},{threshold:.08,rootMargin:'0px 0px 32px 0px'});
els.forEach(el=>{el.classList.add('ed-reveal');observer.observe(el)});
document.body.classList.add('ed-motion-ready');
})();</script>'''


def update(source: str, rel: str) -> str:
    source = re.sub(r'<style id="olympic-depth-style">.*?</style>', '', source, flags=re.S)
    source = re.sub(r'<script id="olympic-depth-script">.*?</script>', '', source, flags=re.S)
    source = re.sub(r'<!-- OLYMPIC_DEPTH_STAGE_START -->.*?<!-- OLYMPIC_DEPTH_STAGE_END -->', '', source, flags=re.S)
    source = re.sub(r'<style id="olympic-editorial-style">.*?</style>', '', source, flags=re.S)
    source = re.sub(r'<script id="olympic-editorial-script">.*?</script>', '', source, flags=re.S)
    source = re.sub(r'<!-- OLYMPIC_CHAPTER_RAIL_START -->.*?<!-- OLYMPIC_CHAPTER_RAIL_END -->', '', source, flags=re.S)
    source = re.sub(r'(<header[^>]*class=")od-host ', r'\1', source, count=1)
    body = re.search(r'<body([^>]*)>', source)
    if not body:
        raise ValueError(f'Body missing: {rel}')
    opening = body.group(0)
    opening = re.sub(r'\b(?:ed-entry|ed-home|ed-module-[0-4])\s*', '', opening)
    module = 0
    for number, prefix in enumerate(('任务一_', '任务二_', '任务三_', '任务四_'), 1):
        if rel.startswith(prefix):
            module = number
            break
    opening = opening.replace('class="', f'class="ed-module-{module} ', 1) if 'class="' in opening else opening[:-1] + f' class="ed-module-{module}">'
    if rel in ENTRIES:
        opening = opening.replace('class="', 'class="ed-entry ', 1) if 'class="' in opening else opening[:-1] + ' class="ed-entry">'
    if rel == '作品总入口/index.html':
        opening = opening.replace('class="', 'class="ed-home ', 1)
    source = source[:body.start()] + opening + source[body.end():]
    if rel in RAILS:
        name, caption = RAILS[rel]
        lanes = '<span class="ed-rail-lanes" aria-hidden="true">' + '<i></i>' * 5 + '</span>'
        rail = f'<!-- OLYMPIC_CHAPTER_RAIL_START --><div class="ed-chapter-rail"><span class="ed-rail-name">{name}</span>{lanes}<span class="ed-rail-caption">{caption}</span></div><!-- OLYMPIC_CHAPTER_RAIL_END -->'
        source = source.replace('</header>', '</header>' + rail, 1)
    if '</head>' not in source or '</body>' not in source:
        raise ValueError(f'Incomplete page: {rel}')
    return source.replace('</head>', STYLE + '</head>', 1).replace('</body>', SCRIPT + '</body>', 1)


def main() -> None:
    pages = sorted(DELIVERY.rglob('index.html'))
    for path in pages:
        rel = path.relative_to(DELIVERY).as_posix()
        before = path.read_text(encoding='utf-8')
        after = update(before, rel)
        if after != before:
            path.write_text(after, encoding='utf-8')
        if SITE.exists():
            target = SITE / path.relative_to(DELIVERY)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, target)
    print(f'Editorial design applied to {len(pages)} pages; no medal remains.')


if __name__ == '__main__':
    main()
