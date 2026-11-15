# GitHub 获取 IOC 网页结果的方法核查｜2026-11-15

## 找到的可执行路线

[Raymond1030/Olympics-Crawler](https://github.com/Raymond1030/Olympics-Crawler) 提供三届 Olympics.com 结果页的运动级 URL 清单和抓取代码：2008 年 41 条、2012 年 39 条、2016 年 41 条运动入口。其 [`GetOlympics.py`](https://github.com/Raymond1030/Olympics-Crawler/blob/main/GetOlympics.py) 从 `https://olympics.com/en/olympic-games/{届次}/results/{运动}` 页面解析小项、奖牌、运动员、NOC 和代表团，设计输出为按运动分开的 Excel。其 [`GetSport.py`](https://github.com/Raymond1030/Olympics-Crawler/blob/main/GetSport.py) 用 Selenium 建立运动入口清单。**仓库仅提交了入口清单和脚本，没有提交三届逐小项结果 Excel。**

另一仓库 [DavidNCamelo/Olympic-Games-DataScraping](https://github.com/DavidNCamelo/Olympic-Games-DataScraping) 用 Selenium 从 Olympics.com 抓奖牌总榜和获奖运动员。实查 `Olympic Prizes.csv` 字段为 `Event Name, Country Code, Gold, Silver, Bronze`，`Olympic medalists.csv` 字段为 `Event, Country, Athlete, Sport, Gold, Silver, Bronze`；2008、2012、2016 的运动员记录均存在，**但没有小项键或逐项来源 URL**，不能直接对 555 项逐项核验。其 README 自述部分 2024 概览值为手动补录，导入前必须单独核对。

## 本机最小实测

用 Edge/Playwright 尝试打开 `https://www.olympics.com/en/olympic-games/rio-2016/results/athletics`，本环境返回 `net::ERR_HTTP2_PROTOCOL_ERROR`；此前直连 IOC 小项页返回 502、Access Denied 或超时。故**不能声称这里已经跑通抓取，也不能把仓库脚本输出计入 555 项核验**。这可能与本环境的网络路径有关，不能据此断言所有地区或设备都无法访问。

## 下一步的可验证试验

1. 在能正常打开 Olympics.com 历史结果页的网络环境，先用浏览器访问上述单个运动页，确认页面实际显示逐小项金银铜；保存 URL、访问日期、原始 HTML 和哈希。
2. 只对一个运动运行仓库脚本，核查页面结构是否仍符合 `data-cy` 选择器；记录成功条数、缺失项、并列铜牌与团队项目的处理。脚本来自第三方，需审阅和适配后运行。
3. 若单运动通过，再按三届入口清单批量采集。每一小项保留 IOC 页面 URL、抓取日期、原始页面哈希及三色 NOC；逐项映射到项目现有 910 项台账。对 555 项逐一比对，不用总榜或运动员列表代替。
4. 对后续取消资格或重分配仍需核查 IOC 决议及页面更新时间；网页在某日显示的名次不自动证明 IOC 最终授牌。出现冲突时保留两版本与裁决链接。

如果只是要解决本机 IOC 访问故障，GitHub 仓库代码**提供了抓取方法，不提供绕过访问限制的保证**。GitHub Actions 的不同网络出口可作为小规模连通性试验，但目前尚未部署或证明可用；它也不应被当作 IOC 数据授权。可将通过审计的输出填入现有[现行 IOC 逐项导入模板](现行IOC逐项导入模板.csv)并运行 `项目工作区/scripts/current_ioc_import_audit.py`，未填记录仍保持原证据等级。
