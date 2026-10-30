---
id: "src-9e8eab9b92b1"
type: "source"
title: "OCP 存储规范与客户诉求：恢复、安全和可观测性的共同基线"
source_path: "storage/OCP-Storage-Specifications-Update-and-What-Customers-Care-About.pdf"
source_git_blob_sha: "2c5cec8ca1a2fdf9483dddb1d9ed4966b18fbf45"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 19
review_status: "analyzed-text"
evidence_pages: [3, 4, 5, 6, 9, 11, 12, 13, 14, 15, 16, 17, 18]
tags: ["ocp", "source", "platform", "storage"]
text_reviewed: true
key_pages_visual_checked: []
updated: "2026-10-30"
---

# OCP 存储规范与客户诉求：恢复、安全和可观测性的共同基线

> 阅读范围：已阅读本文件全部可提取文字（19页）。未完成图表视觉核对；不把文字提取视作图形关系验证。

## 核心结论

材料不仅是 panel 标题，也保留各客户的具体要求。共同方向是用可测试的恢复行为、结构化诊断、设备身份/密钥管理和统一基线降低定制分歧，而非只提升峰值带宽。[[storage/OCP-Storage-Specifications-Update-and-What-Customers-Care-About.pdf#page=9|PDF p.9]][[storage/OCP-Storage-Specifications-Update-and-What-Customers-Care-About.pdf#page=11|PDF p.11]][[storage/OCP-Storage-Specifications-Update-and-What-Customers-Care-About.pdf#page=15|PDF p.15]][[storage/OCP-Storage-Specifications-Update-and-What-Customers-Care-About.pdf#page=16|PDF p.16]]

## 关键证据

- 规格作者说明 DC NVMe 2.8 已完成、贡献中、预计 11 月或 12 月初发布；“完成稿”不能在此直接写成已发布正式标准。[[storage/OCP-Storage-Specifications-Update-and-What-Customers-Care-About.pdf#page=3|PDF p.3]]
- 2.8 重点包括一致的 error recovery/event injection workflow、可读 telemetry 与 latency data、dual CNSA 1.0/2.0 firmware signatures、SPDM 1.4.1 双 certificate bank 和兼容性。[[storage/OCP-Storage-Specifications-Update-and-What-Customers-Care-About.pdf#page=4|PDF p.4]]
- TCG non-global locking range 同 namespace 最多 16 范围、firmware download port lock、admin command history、BMaaS personality 等分别针对密钥隔离、租户权限与调试。[[storage/OCP-Storage-Specifications-Update-and-What-Customers-Care-About.pdf#page=5|PDF p.5]]
- 客户 OOB 路径并不完全一致：Google 提出 MCTP/USB，HPE 强调 I3C，Microsoft 列 I3C 与未来 USB；应区分近期支持与远期带宽方向。[[storage/OCP-Storage-Specifications-Update-and-What-Customers-Care-About.pdf#page=12|PDF p.12]][[storage/OCP-Storage-Specifications-Update-and-What-Customers-Care-About.pdf#page=13|PDF p.13]][[storage/OCP-Storage-Specifications-Update-and-What-Customers-Care-About.pdf#page=17|PDF p.17]]

## 指标与条件

HPE 列低容量 M.2 480/960/1920/3840 GB，说明高容量 AI 存储之外仍有 boot/cost 用例。这里没有任何端到端延迟、寿命或恢复成功率实测。[[storage/OCP-Storage-Specifications-Update-and-What-Customers-Care-About.pdf#page=13|PDF p.13]][[storage/OCP-Storage-Specifications-Update-and-What-Customers-Care-About.pdf#page=14|PDF p.14]]

2027 修订进度是 tentative schedule；2.9 和 SAS-SATA 更新计划不能当作交付承诺。[[storage/OCP-Storage-Specifications-Update-and-What-Customers-Care-About.pdf#page=6|PDF p.6]]

## 图表与架构

未视觉核对图形；此文件主体是文字要点。p.18 只有 Open Discussion，没有讨论实录，未给发言者补写观点。[[storage/OCP-Storage-Specifications-Update-and-What-Customers-Care-About.pdf#page=18|PDF p.18]]

## 关联与比较

与本库 SPDM/LOCK/Caliptra、TP4221 和测试计划形成闭环：安全功能需要可审计实现，QoS 需要负载条件，恢复功能需要事件注入验证。共同 spec 降低差异，但不自动证明互操作或合规。[[storage/OCP-Storage-Specifications-Update-and-What-Customers-Care-About.pdf#page=9|PDF p.9]][[storage/OCP-Storage-Specifications-Update-and-What-Customers-Care-About.pdf#page=11|PDF p.11]][[storage/OCP-Storage-Specifications-Update-and-What-Customers-Care-About.pdf#page=16|PDF p.16]]

## 不确定性与待验证

这是作者/客户在演讲时的需求与路线图；“required”应按对应 2.8 文本、profile 和版本核实。缺少正式条款、厂商支持矩阵与系统联调结果。[[storage/OCP-Storage-Specifications-Update-and-What-Customers-Care-About.pdf#page=3|PDF p.3]][[storage/OCP-Storage-Specifications-Update-and-What-Customers-Care-About.pdf#page=4|PDF p.4]][[storage/OCP-Storage-Specifications-Update-and-What-Customers-Care-About.pdf#page=5|PDF p.5]]

