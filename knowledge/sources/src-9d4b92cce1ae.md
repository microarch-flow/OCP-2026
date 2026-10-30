---
id: "src-9d4b92cce1ae"
type: "source"
title: "OAC 商业采用：给既有企业机房提供跨代可维护的加速卡接口"
source_path: "market-impact-adoption/07_Open Adapter Card – AI From Small Pod to Enterprise Scale.pdf"
source_git_blob_sha: "97da6538ee41e88d1b0ad6a70ef3201f08bf37ca"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 8
review_status: "analyzed-visual"
evidence_pages: [2, 3, 4, 5, 6, 7]
tags: ["ocp", "source", "platform", "market-impact-adoption"]
text_reviewed: true
key_pages_visual_checked: [5]
updated: "2026-10-30"
concepts: ["[[knowledge/concepts/platform-open-adoption-delivery]]"]
---

# OAC 商业采用：给既有企业机房提供跨代可维护的加速卡接口

> 阅读范围：已阅读本文件全部可提取文字（8页）。关键页已视觉核对：5；不代表逐页视觉审核。

## 核心结论

OAC 针对CEM与高密度rack-scale之间的small-pod gap，强调既有电力/风冷条件、长生命周期、现场FRU和渐进扩展。标准化意图是把硅与系统roadmap解耦，不是保证任意卡任意服务器无条件兼容。[[market-impact-adoption/07_Open Adapter Card – AI From Small Pod to Enterprise Scale.pdf#page=2|PDF p.2]][[market-impact-adoption/07_Open Adapter Card – AI From Small Pod to Enterprise Scale.pdf#page=3|PDF p.3]][[market-impact-adoption/07_Open Adapter Card – AI From Small Pod to Enterprise Scale.pdf#page=4|PDF p.4]]

## 关键证据

- Card是FRU，定义air/DLC variants与DLC connectors；vendor可自定义cold plate/heatsink与optional fabric connectors。统一部分与vendor部分要分别验证。[[market-impact-adoption/07_Open Adapter Card – AI From Small Pod to Enterprise Scale.pdf#page=5|PDF p.5]]
- 五家coauthor、v0.9 publicly available、live concept designs，是早期生态采用信号；规格仍可变，不能当作v1.0完成或大规模量产。[[market-impact-adoption/07_Open Adapter Card – AI From Small Pod to Enterprise Scale.pdf#page=6|PDF p.6]][[market-impact-adoption/07_Open Adapter Card – AI From Small Pod to Enterprise Scale.pdf#page=7|PDF p.7]]
- reusable parts与共同工程可能降低工具/库存和资格成本，但材料没有给实际BOM节省或可靠性提升测量。[[market-impact-adoption/07_Open Adapter Card – AI From Small Pod to Enterprise Scale.pdf#page=4|PDF p.4]][[market-impact-adoption/07_Open Adapter Card – AI From Small Pod to Enterprise Scale.pdf#page=5|PDF p.5]]

## 指标与条件

small pod示意8–16GPU；86%racks在5–30kW、77%无升密度计划、64%air-only未列调查样本与年份，不能外推全球机房。图中DLC OAC footprint约CEM2.2×，这是几何对照，不是性能/功率2.2×。[[market-impact-adoption/07_Open Adapter Card – AI From Small Pod to Enterprise Scale.pdf#page=2|PDF p.2]][[market-impact-adoption/07_Open Adapter Card – AI From Small Pod to Enterprise Scale.pdf#page=3|PDF p.3]][[market-impact-adoption/07_Open Adapter Card – AI From Small Pod to Enterprise Scale.pdf#page=5|PDF p.5]]

## 图表与架构

已核对p.5外形对照及vendor-defined/fixed接口文字；“no cables”针对卡内部连接方式，不表示整机无需外部网络/电力/冷却连接。[[market-impact-adoption/07_Open Adapter Card – AI From Small Pod to Enterprise Scale.pdf#page=5|PDF p.5]]

## 关联与比较

与Intel主旨可组成从卡到模型路由的部署路径，但OAC mechanical互通与inference engine/driver可移植是两个不同维度。与设施platform框架一致：稳定接口应该允许实现演进。

## 不确定性与待验证

需正式版本的电气/热/机械限值、跨vendorfit/firmware/管理测试和售后支持承诺。市场gap图明确illustrative，不能当作需求预测。[[market-impact-adoption/07_Open Adapter Card – AI From Small Pod to Enterprise Scale.pdf#page=2|PDF p.2]][[market-impact-adoption/07_Open Adapter Card – AI From Small Pod to Enterprise Scale.pdf#page=7|PDF p.7]]

