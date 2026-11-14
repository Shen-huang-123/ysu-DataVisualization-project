# 逐小项历史结果数据申请（待发送草稿）

**收件对象**：IOC Olympic Studies Centre，studies.centre@olympic.org。IOC 的[研究中心页面](https://www.olympics.com/ioc/olympic-studies-centre)列出该联系渠道；发送前由团队自行核对地址与身份信息。本草稿尚未发送。

## English request

Subject: Research request — current event-level medal results for Beijing 2008, London 2012 and Rio 2016

Dear Olympic Studies Centre,

We are a student team at Yanshan University preparing an educational Olympic data visualization project. We would like to verify the current, post-reallocation medal results for all Summer Olympic medal events at Beijing 2008, London 2012 and Rio 2016.

Could you advise whether an authoritative event-level export or research-access dataset is available? Ideally, each record would include Games year, sport, discipline, event, medal colour, athlete/team, NOC, result status, the date or version of the result, and a permanent official citation. We are particularly concerned about anti-doping disqualifications and later medal reallocations. A link to an existing authoritative publication or the appropriate access procedure would also be helpful.

Our working event inventory has 302, 302 and 306 event keys respectively. We can supply the inventory and explain our event-name matching process. The data will be used for academic validation and cited according to your conditions.

Thank you for your guidance.

Xiao Organization / 晓组织
Yanshan University / 燕山大学
[contact name and email to be supplied by the team]

## 接收后核验流程

1. 保存原文件及提供方说明，不改写原件；记录接收日期、版本和 SHA256。
2. 将官方字段映射到[910项导入模板](../../交付文件/任务三_专题深挖/S2_口径的魔力/08_逐项外部核验/现行IOC逐项导入模板.csv)，保留原始赛事名称与映射注释。
3. 运行 `python 项目工作区/scripts/current_ioc_import_audit.py --source <整理后的官方CSV>`，逐项检查重复、缺失、非官方链接和三色差异。
4. 对官方后续重分配先核对生效日期，再更新分析与图注；不得把赛时成绩册直接当作现行真值。

**当前状态**：团队暂无 IOC 官方导出。2026-11-12 的可复核结论仍是 4 项现行 IOC 完整重分配、7 项赛时官方补证、899 项旧抓取存档；这封草稿不增加已核验数量。
