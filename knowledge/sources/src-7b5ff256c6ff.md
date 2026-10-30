---
id: "src-7b5ff256c6ff"
type: "source"
title: "硬件故障生态：CPER→分析器→政策授权→CPAD→结果闭环"
source_path: "systems-management/OCP-Hardware-Fault-Management-Workstreams-Status-and-Relationship.pdf"
source_git_blob_sha: "596b47d6382e3ebd51c35dd62a7c3521be2ec500"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 33
review_status: "analyzed-visual"
evidence_pages: [6, 7, 10, 11, 14, 17, 19, 20, 21, 23, 25, 26, 31, 33]
tags: ["ocp", "source", "platform", "systems-management"]
text_reviewed: true
key_pages_visual_checked: [6, 7, 8, 9]
updated: "2026-10-30"
---

# 硬件故障生态：CPER→分析器→政策授权→CPAD→结果闭环

> 阅读范围：已阅读本文件全部可提取文字（33页）。关键页已视觉核对：6, 7, 8, 9；不代表逐页视觉审核。

## 核心结论

- 这份panel材料有实质技术页，不仅嘉宾表：RAS API统一CPER错误/结果与CPAD动作，PLDM/Redfish映射仍处标准化/PoC阶段。[[systems-management/OCP-Hardware-Fault-Management-Workstreams-Status-and-Relationship.pdf#page=10|PDF p.10]][[systems-management/OCP-Hardware-Fault-Management-Workstreams-Status-and-Relationship.pdf#page=11|PDF p.11]][[systems-management/OCP-Hardware-Fault-Management-Workstreams-Status-and-Relationship.pdf#page=14|PDF p.14]][[systems-management/OCP-Hardware-Fault-Management-Workstreams-Status-and-Relationship.pdf#page=17|PDF p.17]]
- 自动修复闭环必须保留operator policy审批/覆盖厂商analyzer输出，HTTP202仅表示routing接受，不是修复成功。[[systems-management/OCP-Hardware-Fault-Management-Workstreams-Status-and-Relationship.pdf#page=21|PDF p.21]][[systems-management/OCP-Hardware-Fault-Management-Workstreams-Status-and-Relationship.pdf#page=23|PDF p.23]]

## 关键证据

- FMFM从CE计数阈值“都怪DIMM”转向厂商丰富错误记录与分析器，规划HBM/LPDDR、ECS、内部ECC日志和error injection。[[systems-management/OCP-Hardware-Fault-Management-Workstreams-Status-and-Relationship.pdf#page=6|PDF p.6]][[systems-management/OCP-Hardware-Fault-Management-Workstreams-Status-and-Relationship.pdf#page=7|PDF p.7]]
- PLDM读Error file得queue head，写Action file入新动作；Redfish用LogService/EventService及小OEM RASService层。[[systems-management/OCP-Hardware-Fault-Management-Workstreams-Status-and-Relationship.pdf#page=14|PDF p.14]][[systems-management/OCP-Hardware-Fault-Management-Workstreams-Status-and-Relationship.pdf#page=17|PDF p.17]]
- CPER可inline或binary attachment；critical/fatal要求发生时送达不batch。CPAD header/section descriptors由BMC检查，section bodies opaque并按PartitionID路由。[[systems-management/OCP-Hardware-Fault-Management-Workstreams-Status-and-Relationship.pdf#page=19|PDF p.19]][[systems-management/OCP-Hardware-Fault-Management-Workstreams-Status-and-Relationship.pdf#page=20|PDF p.20]][[systems-management/OCP-Hardware-Fault-Management-Workstreams-Status-and-Relationship.pdf#page=21|PDF p.21]]
- System Debug首步是人可审计、非敏感code currency/status JSON，性能退化检测为后续。[[systems-management/OCP-Hardware-Fault-Management-Workstreams-Status-and-Relationship.pdf#page=25|PDF p.25]][[systems-management/OCP-Hardware-Fault-Management-Workstreams-Status-and-Relationship.pdf#page=26|PDF p.26]]

## 指标与条件

RAS API0.96为作者称已release、HWFM2.0为2027Q1目标；没有repair成功率/时延。展示的DRAM soft PPR为模拟/PoC流程，不是全机群生产成效。[[systems-management/OCP-Hardware-Fault-Management-Workstreams-Status-and-Relationship.pdf#page=23|PDF p.23]][[systems-management/OCP-Hardware-Fault-Management-Workstreams-Status-and-Relationship.pdf#page=31|PDF p.31]][[systems-management/OCP-Hardware-Fault-Management-Workstreams-Status-and-Relationship.pdf#page=33|PDF p.33]]

## 图表与架构

已视觉核对p.6–9：内存错误分析比计数更丰富，BMC可同时是上游Endpoint与下游Initiator，CPAD向下、CPER向上。

## 关联与比较

与[[knowledge/sources/src-f471e738fe63|RAS PLDM映射]]合读，补足Redfish异步结果语义；与诊断efficacy指标结合才可验收修复价值。

## 不确定性与待验证

需错误注入授权、防重复动作、队列溢出、CPER缺失恢复、analyzer可信更新与修复失败升级；版本间样例路径可能变更，勿直接把mockup当正式API。

