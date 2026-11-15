# GitHub 公开 IOC 数据检索｜2026-11-15

## 要解决的问题

查找可逐项核对 2008、2012、2016 三届剩余 555 项**现行 IOC 授牌结果**的公开文件。合格文件应至少包含届次、正式小项键、金银铜获奖方、来源、生成或更新日期，并能追溯后续取消资格与奖牌重分配。文件在 GitHub 上托管，本身不构成 IOC 官方认证。

## 实际检查的候选

| 仓库 | 查到的内容 | 对本问题的作用 |
| --- | --- | --- |
| [newsdev/odf](https://github.com/newsdev/odf) | README 说明仓库存放 ODF 解析工具和从 IOC ODF 表格转出的 Common Codes / Sport Codes；树中有 `competitions/OG2016/codes/`，包含 Event 等编码表。递归目录未见逐小项金银铜结果文件。 | 可辅助 2016 小项名称和代码映射；**不能核验获奖方**。其 `ODF_LICENSE` 也是文档许可说明，不能把代码表说成现行奖牌结果。 |
| [crishoj/odf-fetch](https://github.com/crishoj/odf-fetch) | README 自述是 2014 索契冬奥官方数据流的临时抓取中间件，根目录只有脚本和说明。 | 时间、赛事与本项目三届夏奥均不符；没有可用逐项结果。 |
| [kevle1/paris-2024-olympic-api](https://github.com/kevle1/paris-2024-olympic-api) | README 明称 **unofficial API**，并给出巴黎 2024 `CIS_MedalNOCs` 来源端点及保存的奖牌总榜快照。 | 只有 2024 总榜，不能覆盖 2008/2012/2016 逐小项；第三方保存也不代表 IOC 现行认证。 |
| GitHub 仓库搜索“olympedia olympic data” | 搜到的仓库说明为 Olympedia 抓取、整理或可视化。 | 可作为独立二次来源；项目已有 555/555 的 Olympedia 对照，无须重复把镜像当新增证据。 |

## 访问与判定

通过 GitHub API 查看上述仓库 README 和目录树；`newsdev/odf` 的 OG2016 文件主要是代码表。尝试直接请求 `olympics.com/OG2024` 以及推测的 `OG2016`、`OG2012`、`OG2008` 奖牌端点，本环境分别出现代理错误或超时；不能凭推测的 URL 声称这些历史端点存在或已读到结果。GitHub 搜索也没有找到可确认出处、版本和后续裁决覆盖范围的三届现行 IOC 逐小项授牌文件。

**结论：本轮未把 555 项升级为“现行 IOC 已核验”。**可以把 `newsdev/odf` 的 2016 Event 代码用于日后的键映射检查；要升级奖牌证据，仍需读取 IOC 现行小项页、IOC 明确的重分配决定，或可核验来源和日期的 IOC 授权结果导出，并逐项进入现有[导入审计模板](现行IOC逐项导入模板.csv)。已经完成的 Olympedia 二次对照和赛时成绩册核验继续按各自证据等级使用。
