---
id: "src-4cb1cfbea778"
type: "source"
title: "Open Switch Platform Architecture (OSPA): A Unified Network Switch Platform Reference Design"
source_path: "networking/10_Switch Platform Architecture A Unified Network Switch Platform Referen.pdf"
source_git_blob_sha: "73b2aeec2e7f173043c2bbd9278450b4fe8b7fab"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 16
review_status: "analyzed-visual"
evidence_pages: [5, 6, 8, 9, 10, 11, 12, 13, 14]
text_reviewed: true
key_pages_visual_checked: [11, 13]
tags: ["ocp-2026", "networking"]
concepts: ["[[knowledge/concepts/network-executable-validation]]"]
---

# Open Switch Platform Architecture (OSPA): A Unified Network Switch Platform Reference Design

## 核心结论
OSPA填补SAI未覆盖的switch平台层：电源、环境传感、inventory、OOB、firmware维护与故障诊断；不规定routing/forwarding，因而不是NOS或SAI的替代品。[[networking/10_Switch Platform Architecture A Unified Network Switch Platform Referen.pdf#page=5|PDF p.5]][[networking/10_Switch Platform Architecture A Unified Network Switch Platform Referen.pdf#page=6|PDF p.6]]

## 关键证据
- 规范偏好In-Host model：利用host CPU资源与主软件生态，不把主要平台逻辑限制在BMC内。[[networking/10_Switch Platform Architecture A Unified Network Switch Platform Referen.pdf#page=10|PDF p.10]]
- I/O Bridge FPGA在host PCIe与I2C/GPIO/SPI/MDIO/LED之间做聚合/转换。[[networking/10_Switch Platform Architecture A Unified Network Switch Platform Referen.pdf#page=11|PDF p.11]]
- CPU软件分device driver、配置驱动platform discovery、hardware-agnostic services；理想新平台只增加topology配置，而不是fork每个服务。[[networking/10_Switch Platform Architecture A Unified Network Switch Platform Referen.pdf#page=14|PDF p.14]]
- 1.0在演讲时为**提交OCP正式review**状态；示例含Minipack3N+FBOSS、Bailly CPO+SONiC、NH-4210双NOS。[[networking/10_Switch Platform Architecture A Unified Network Switch Platform Referen.pdf#page=8|PDF p.8]][[networking/10_Switch Platform Architecture A Unified Network Switch Platform Referen.pdf#page=9|PDF p.9]]

## 指标与条件
文件没有量化bring-up时间节省、维护成本或p99改善。双1GbE RJ45 OOB接口供BMC/host共享OOB switch，是参考设计配置而非数据平面带宽。[[networking/10_Switch Platform Architecture A Unified Network Switch Platform Referen.pdf#page=12|PDF p.12]]

## 图表与架构
已核p.11 host→PCIe→IOB→peripherals拓扑。p.13多级过热保护中，sensor的alert pin经CPLD直接控制voltage regulator enable/disable；软件遥测在另一条I2C路径，**硬件保护不应被误写成必须等host轮询**。[[networking/10_Switch Platform Architecture A Unified Network Switch Platform Referen.pdf#page=13|PDF p.13]]

## 关联与比较
[[knowledge/concepts/network-executable-validation]]；[[knowledge/sources/src-983fb0686005]]说明配置驱动服务/测试如何消费这一类硬件抽象。

## 不确定性与待验证
“只需配置”需要标准controller、拓扑与驱动条件成立。没有展示host hang、FPGA故障、OOB断链时的完整故障状态机；多级过热保护应进入平台验收，不能只测正常遥测。
