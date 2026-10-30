---
id: "src-15ac818ed33e"
type: "source"
title: "S.A.F.E./S.O.L.I.D.：可复用安全审查与AI辅助但非自评"
source_path: "Security/Upgrading OCP S.A.F.E. and S.O.L.I.D. for the AI age.pdf"
source_git_blob_sha: "172235d8222ef49560f9205349565cdae00b573c"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 12
review_status: "analyzed-text"
evidence_pages: [1, 4, 5, 6, 7, 8, 9, 10]
tags: ["ocp", "source", "platform", "security"]
text_reviewed: true
key_pages_visual_checked: []
updated: "2026-10-30"
---

# S.A.F.E./S.O.L.I.D.：可复用安全审查与AI辅助但非自评

> 阅读范围：已阅读本文件全部可提取文字（12页）。未完成图表视觉核对；不把文字提取视作图形关系验证。

## 核心结论

- S.A.F.E.输出是评审报告而非简单pass/fail；由认可SRP执行，目的是多个客户复用审查而不是供应商重复应对。[[Security/Upgrading OCP S.A.F.E. and S.O.L.I.D. for the AI age.pdf#page=4|PDF p.4]]
- S.O.L.I.D.是具体要求库与按产品类型适用性结构，不是另一个独立审查项目。[[Security/Upgrading OCP S.A.F.E. and S.O.L.I.D. for the AI age.pdf#page=5|PDF p.5]]
- AI审查作为人工审查补充，不允许替代第三方独立评估；最终仍以SRP报告和人工验证为准。[[Security/Upgrading OCP S.A.F.E. and S.O.L.I.D. for the AI age.pdf#page=7|PDF p.7]][[Security/Upgrading OCP S.A.F.E. and S.O.L.I.D. for the AI age.pdf#page=9|PDF p.9]]

## 关键证据

- 材料明确日期为2026年10月12–15日；称S.O.L.I.D.从2026年10月mandatory、AI相关新要求从2027-01-01mandatory。这是会中政策快照，不是本文独立核验的现行规则。[[Security/Upgrading OCP S.A.F.E. and S.O.L.I.D. for the AI age.pdf#page=1|PDF p.1]][[Security/Upgrading OCP S.A.F.E. and S.O.L.I.D. for the AI age.pdf#page=5|PDF p.5]][[Security/Upgrading OCP S.A.F.E. and S.O.L.I.D. for the AI age.pdf#page=8|PDF p.8]]
- 示例覆盖CPU推测执行/微码/NVM、内存SPD/加密、PCIe IOMMU/IDE/TDISP/FLR清除。[[Security/Upgrading OCP S.A.F.E. and S.O.L.I.D. for the AI age.pdf#page=6|PDF p.6]]
- 作者称简单“review文件夹”prompt不够，需要合适harness；当时要求frontier cloud models、开放权重许可仍在研究。[[Security/Upgrading OCP S.A.F.E. and S.O.L.I.D. for the AI age.pdf#page=7|PDF p.7]]
- 评审是时间点评价，新模型出现本身不要求重审；未满足要求短报告列示的日期仍TBD。[[Security/Upgrading OCP S.A.F.E. and S.O.L.I.D. for the AI age.pdf#page=9|PDF p.9]][[Security/Upgrading OCP S.A.F.E. and S.O.L.I.D. for the AI age.pdf#page=10|PDF p.10]]

## 指标与条件

没有AI审查发现率/误报率、审查成本节省、模型比较或安全性量化；“产品没有AI审查就不安全”为作者强主张，本文件未提供支持该普遍判断的实验数据。[[Security/Upgrading OCP S.A.F.E. and S.O.L.I.D. for the AI age.pdf#page=7|PDF p.7]]

## 图表与架构

以文字政策说明为主；无待重建的技术架构或实测图。

## 关联与比较

采购应看实际报告覆盖、未满足项与供应商修复证据，不能仅凭SAFE标签或AI工具使用证明安全。

## 不确定性与待验证

需另核对正式程序版本、生效日期、获准SRP清单与适用产品；公开语料审查、企业模型数据保留和独立性也需在实际委托中明确。

