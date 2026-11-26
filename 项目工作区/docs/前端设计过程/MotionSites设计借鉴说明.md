# MotionSites设计借鉴 · 2026-11-15

查阅了网站公开案例说明，没有购买或复制付费提示词、影片与品牌素材。

- Monolith Hero：https://motionsites.org/prompts/monolith-hero 。借鉴其影像主导、章节节奏、低干扰控制思路。
- Halden：https://motionsites.org/prompts/atlas-nav 。借鉴全幅摄影与克制界面思路。

本轮在11个现有奥运影像封面加入滚动驱动的缓慢推进和纵向视差；提供主动开启的沉浸影像模式，隐藏正文与局部暗场，保留五环，Esc或返回专题按钮退出。五色底线延续奥运色彩。页面数据、导航与图表未改；没有全页transform、跨页延时或闪光层。

动画仅绑定封面，读取每帧合并到requestAnimationFrame，减少动画模式关闭镜头变化。此轮并非重建首页隧道或将静态照片称为实拍视频。
