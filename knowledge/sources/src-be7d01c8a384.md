---
id: "src-be7d01c8a384"
type: "source"
title: "OCP NIC 2026: Gen 7 and Liquid Cooling – More Speed and Power Ahead"
aliases: ["OCP NIC 2026: Gen 7 and Liquid Cooling – More Speed and Power Ahead"]
speakers: "Thomas Ng（Intel）；Jason Rock（Dell Technologies）"
source_path: "server/05_OCP NIC 2026 Gen 7 and liquid cooling – More speed and power ahead.pdf"
source_git_blob_sha: "dffb04bc791d1854c66aec9befc6496d8dcfc445"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 10
review_status: "analyzed-visual"
text_reviewed: true
key_pages_visual_checked: [3, 5, 6, 8]
evidence_pages: [3, 4, 5, 6, 7, 8]
tags: ["ocp2026", "source", "compute-memory"]
concepts: ["[[knowledge/concepts/compute-memory-modular-platform-contract]]", "[[knowledge/concepts/compute-memory-power-path-and-dynamics]]"]
---

# OCP NIC 2026: Gen 7 and Liquid Cooling – More Speed and Power Ahead

## 核心结论
OCP NIC演进同时涉及PCIe7信号预算、管理描述、瞬态功率、液冷和高功率连接器，不能把它简化成端口速率翻倍。高速链路能力需要与系统功率/散热许可一起协商。[[server/05_OCP NIC 2026 Gen 7 and liquid cooling – More speed and power ahead.pdf#page=3|PDF p.3]] [[server/05_OCP NIC 2026 Gen 7 and liquid cooling – More speed and power ahead.pdf#page=7|PDF p.7]] [[server/05_OCP NIC 2026 Gen 7 and liquid cooling – More speed and power ahead.pdf#page=8|PDF p.8]]

## 关键证据
- v1.7引入PCIe7支持，插损预算拟对齐CEM7以避免OCP NIC额外更严材料要求；1.6Tbps是支持目标/接口能力，不是应用吞吐实测。[[server/05_OCP NIC 2026 Gen 7 and liquid cooling – More speed and power ahead.pdf#page=3|PDF p.3]]
- CLB/CBB与thermal fixture用于不同层面的compliance/thermal测试。[[server/05_OCP NIC 2026 Gen 7 and liquid cooling – More speed and power ahead.pdf#page=4|PDF p.4]]
- FRU过渡到DMTF DSP0220并保持IPMI兼容；slide指出旧3-byte制造时间字段2027-11-24后有歧义，建议清零并加指向DMTF records的OEM record。此处是演讲迁移方案，不代替正式规范实施。[[server/05_OCP NIC 2026 Gen 7 and liquid cooling – More speed and power ahead.pdf#page=5|PDF p.5]]
- power excursion indication让BMC理解短时需求；不能仅按静态TDP配置供电。[[server/05_OCP NIC 2026 Gen 7 and liquid cooling – More speed and power ahead.pdf#page=7|PDF p.7]]

## 指标与条件
200W连接方案标 **Active Development**，考虑SFF-TA-1037 4C+ EP，需旧卡兼容，同时阻止新高功率卡在TA-1002旧槽错误上电；hardware interlock与FRU aux/main最大功率查询均是必要约束。[[server/05_OCP NIC 2026 Gen 7 and liquid cooling – More speed and power ahead.pdf#page=8|PDF p.8]]
液冷reference design要求solid faceplate，目标近100%热捕获到液体；这是设计目标，不是已经测出的所有NIC液冷效率。[[server/05_OCP NIC 2026 Gen 7 and liquid cooling – More speed and power ahead.pdf#page=6|PDF p.6]]

## 图表与架构
p.8 connector/板厚讨论与p.6 cold plate图表明机械、电流与冷却不可独立升级。更高网络速率会改变可服务性与系统管理接口，不只是SerDes。

## 关联与比较
[[knowledge/concepts/compute-memory-modular-platform-contract|模块化平台契约]] · [[knowledge/concepts/compute-memory-power-path-and-dynamics|供电动态约束]]。

## 不确定性与待验证
最终200W连接器、Gen7/CEM损耗和新form factor尚需正式发布文档确认；无BER、温升或流阻/泄漏测试结果，不提供production-ready保证。

## 原始页码导航
[[server/05_OCP NIC 2026 Gen 7 and liquid cooling – More speed and power ahead.pdf#page=3|p.3]] · [[server/05_OCP NIC 2026 Gen 7 and liquid cooling – More speed and power ahead.pdf#page=4|p.4]] · [[server/05_OCP NIC 2026 Gen 7 and liquid cooling – More speed and power ahead.pdf#page=5|p.5]] · [[server/05_OCP NIC 2026 Gen 7 and liquid cooling – More speed and power ahead.pdf#page=6|p.6]] · [[server/05_OCP NIC 2026 Gen 7 and liquid cooling – More speed and power ahead.pdf#page=7|p.7]] · [[server/05_OCP NIC 2026 Gen 7 and liquid cooling – More speed and power ahead.pdf#page=8|p.8]]
