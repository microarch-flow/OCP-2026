---
id: "src-fb5996cd03af"
type: "source"
title: "CTAM：用共同测试缩小GPU固件供需验收口径差"
source_path: "Test & Validation/CTAM- Three Years of Bridging Hyperscalers and Suppliers Through GPU Accelerator Compliance.pdf"
source_git_blob_sha: "3ce6dc3ac667cbbfcb9926d21e1243df8def4533"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 8
review_status: "analyzed-text"
evidence_pages: [2, 3, 4, 5, 6]
tags: ["ocp", "source", "platform", "test-&-validation"]
text_reviewed: true
key_pages_visual_checked: []
updated: "2026-10-30"
concepts: ["[[knowledge/concepts/platform-operability-contract]]"]
---

# CTAM：用共同测试缩小GPU固件供需验收口径差

> 阅读范围：已阅读本文件全部可提取文字（8页）。未完成图表视觉核对；不把文字提取视作图形关系验证。

## 核心结论

- CTAM的价值是让供应商与hyperscaler用同一管理合规测试和结果语言，减少“各自测试通过”的验收落差；不是GPU算力benchmark。[[Test & Validation/CTAM- Three Years of Bridging Hyperscalers and Suppliers Through GPU Accelerator Compliance.pdf#page=2|PDF p.2]][[Test & Validation/CTAM- Three Years of Bridging Hyperscalers and Suppliers Through GPU Accelerator Compliance.pdf#page=3|PDF p.3]]
- 演讲称2026起hyperscaler将CTAM结果作为固件接受条件，但未提供覆盖全部客户的政策证据；应按具体采购方要求落地。[[Test & Validation/CTAM- Three Years of Bridging Hyperscalers and Suppliers Through GPU Accelerator Compliance.pdf#page=4|PDF p.4]]

## 关键证据

- 时间线标v1.0于2025年3月production release，v1.1于2025年6月引入OPP评分/机器可读结果，v1.2于2026年8月称41+ tests、4 domains、PLDM v1.3。[[Test & Validation/CTAM- Three Years of Bridging Hyperscalers and Suppliers Through GPU Accelerator Compliance.pdf#page=4|PDF p.4]]
- 后续计划列2026年底PLDM v1.3/bundling检查、2027年6月mockup/Redfish模拟、AI skills、规范1.9/2.0与recovery image；远期才是GPU RAS和AI节点之外扩展。[[Test & Validation/CTAM- Three Years of Bridging Hyperscalers and Suppliers Through GPU Accelerator Compliance.pdf#page=6|PDF p.6]]

## 指标与条件

12项初始health checks与41+ tests是测试规模，不是覆盖率/缺陷率。TTM改善、稳定性与风险降低均未给数值基线。[[Test & Validation/CTAM- Three Years of Bridging Hyperscalers and Suppliers Through GPU Accelerator Compliance.pdf#page=4|PDF p.4]][[Test & Validation/CTAM- Three Years of Bridging Hyperscalers and Suppliers Through GPU Accelerator Compliance.pdf#page=5|PDF p.5]]

## 图表与架构

未视觉核对时间线；本卡仅引用可提取文字的版本/里程碑，不推断图示依赖关系。

## 关联与比较

与开源Caliptra DV区别：CTAM主要统一外部管理接口验收；DV检验内部RTL功能/安全性质。前者通过不能替代后者。

## 不确定性与待验证

p.4/5已列PLDM v1.3支持，p.6又把其支持/捆绑检查放年底计划，可能区分部分功能与完整场景；需查实际release与测试矩阵。

