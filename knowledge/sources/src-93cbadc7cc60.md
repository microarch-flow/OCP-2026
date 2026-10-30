---
id: "src-93cbadc7cc60"
type: "source"
title: "System level standards for Multi-vendor Chiplet Interoperability"
aliases: ["System level standards for Multi-vendor Chiplet Interoperability"]
speakers: "Itai Nadler — CEO, GSOC; Rob Pelt — Fellow, AMD"
source_path: "Server：Open Chiplet Economy/System level standards for Multi vendor chiplet interoperability.pdf"
source_git_blob_sha: "58e52fd1d6105992c3ef7ed5e8dfe0b7c7821ab5"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 11
review_status: "analyzed-visual"
text_reviewed: true
key_pages_visual_checked: [5, 6, 7, 8, 9]
evidence_pages: [3, 4, 5, 6, 7, 8, 9, 10]
tags: ["ocp2026", "source", "compute-memory"]
concepts: ["[[knowledge/concepts/compute-memory-chiplet-system-contracts]]", "[[knowledge/concepts/compute-memory-chiplet-link-efficiency]]"]
---

# System level standards for Multi-vendor Chiplet Interoperability

## 核心结论
物理/transaction互操作之外，还需共享power/performance、secure boot、RAS、clock/voltage/reset管理服务。本workstream重点是 **SCMI API/protocol通过可路由MCTP运输，并绑定I3C/UCIe/BoW管理路径**。

## 关键证据
- chiplet各自可差异化，但SoC共同服务必须有一致语义；FCSA与Chiplet Systems workstream分工协同。[[Server：Open Chiplet Economy/System level standards for Multi vendor chiplet interoperability.pdf#page=3|PDF p.3]] [[Server：Open Chiplet Economy/System level standards for Multi vendor chiplet interoperability.pdf#page=4|PDF p.4]]
- 本管理stack图：SCMI+extensions的API/protocol → DMTF MCTP → I3C/BoW/UCIe management transport。p.5对physical层的定位是此stack上下文，不应理解为FCSA整体只管PHY。[[Server：Open Chiplet Economy/System level standards for Multi vendor chiplet interoperability.pdf#page=5|PDF p.5]]
- SCMI有agent/message/channel抽象；monolithic平台常用专用memory channel，但multi-vendor系统需要统一可路由transport。MCTP通过endpoint IDs、bridge/bus owner与routing table提供路径。[[Server：Open Chiplet Economy/System level standards for Multi vendor chiplet interoperability.pdf#page=6|PDF p.6]] [[Server：Open Chiplet Economy/System level standards for Multi vendor chiplet interoperability.pdf#page=7|PDF p.7]]
- I3C frame中的MCTP header/payload再嵌SCMI header/parameters，不能省略绑定规范就认为任意SCMI设备能跨chiplet互通。[[Server：Open Chiplet Economy/System level standards for Multi vendor chiplet interoperability.pdf#page=8|PDF p.8]]

## 指标与条件
**p.9提取文本存在多栏顺序错配，以下以原图复核为准：**
| binding | p.9真实状态 |
|---|---|
| SCMI over I3C | In final review |
| SCMI over UCIe | Initial draft |
| SCMI over BoW | Not started |
[[Server：Open Chiplet Economy/System level standards for Multi vendor chiplet interoperability.pdf#page=9|PDF p.9]]
p.10说明I3C v0.93审阅中、v0.92 public draft，UCIe/BoW目标early2027。与OCE overview的CMI阶段描述不完全一致，可能是快照/命名/更新不同；不擅自挑一个合并成“最新状态”。[[Server：Open Chiplet Economy/System level standards for Multi vendor chiplet interoperability.pdf#page=10|PDF p.10]]

## 图表与架构
已检查p.5–9，尤其p.9三列状态纠正了文本抽取误序。没有management-message latency、boot/recovery时间或大规模routing验证结果。

## 关联与比较
[[knowledge/concepts/compute-memory-chiplet-system-contracts|多厂商芯粒的系统契约]]；[[knowledge/concepts/compute-memory-chiplet-link-efficiency|数据平面协议效率]]。SCMI/MCTP管理面与AXI/CHI/TLL data plane应分别建模：带宽可能小，但reset/clock/power状态转换可影响整个系统性能与恢复。

## 不确定性与待验证
需完整binding版本、endpoint discovery、权限/认证、fault/retry、message ordering和多供应商conformance测试。演讲是进展介绍，不证明所有management路径已完成互操作。


## 原始页码导航
[[Server：Open Chiplet Economy/System level standards for Multi vendor chiplet interoperability.pdf#page=3|p.3]] · [[Server：Open Chiplet Economy/System level standards for Multi vendor chiplet interoperability.pdf#page=4|p.4]] · [[Server：Open Chiplet Economy/System level standards for Multi vendor chiplet interoperability.pdf#page=5|p.5]] · [[Server：Open Chiplet Economy/System level standards for Multi vendor chiplet interoperability.pdf#page=6|p.6]] · [[Server：Open Chiplet Economy/System level standards for Multi vendor chiplet interoperability.pdf#page=7|p.7]] · [[Server：Open Chiplet Economy/System level standards for Multi vendor chiplet interoperability.pdf#page=8|p.8]] · [[Server：Open Chiplet Economy/System level standards for Multi vendor chiplet interoperability.pdf#page=9|p.9]] · [[Server：Open Chiplet Economy/System level standards for Multi vendor chiplet interoperability.pdf#page=10|p.10]]
