---
id: "src-9a1b656bfb39"
type: "source"
title: "Building Interoperable AI Systems with Chiplets: Arm Neoverse and Cadence in an Open Ecosystem"
aliases: ["Building Interoperable AI Systems with Chiplets: Arm Neoverse and Cadence in an Open Ecosystem"]
speakers: "Saif Elsaady — Arm; Michael Posner — Cadence Design Systems"
source_path: "Server：Open Chiplet Economy/Building Interoperable AI Systems with Chiplets- Arm Neoverse and Cadence in an Open Ecosystem.pdf"
source_git_blob_sha: "9faafc0e434bec8b5c6ce934063bfbc8e4d5f578"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 11
review_status: "analyzed-visual"
text_reviewed: true
key_pages_visual_checked: [5, 6, 8, 9]
evidence_pages: [3, 4, 5, 6, 7, 8, 9, 10]
tags: ["ocp2026", "source", "compute-memory"]
concepts: ["[[knowledge/concepts/compute-memory-federated-model-contract]]", "[[knowledge/concepts/compute-memory-chiplet-system-contracts]]"]
---

# Building Interoperable AI Systems with Chiplets: Arm Neoverse and Cadence in an Open Ecosystem

## 核心结论
组合现成Neoverse CSS、Cadence接口IP/验证工具和FCSA管理框架，降低chiplet集成中的重复基础工作。**pre-integrated subsystem与开放系统契约互补，不等于任意两颗支持UCIe的chiplet可直接插接。**

## 关键证据
- Arm提供CPU/coherent interconnect/system IP及验证过的平台软件；partner增加IO/accelerators并完成chip design。[[Server：Open Chiplet Economy/Building Interoperable AI Systems with Chiplets- Arm Neoverse and Cadence in an Open Ecosystem.pdf#page=4|PDF p.4]]
- CSS N4示意含CMN-Delphi、SLC、NoC、MMU、DDR5/LPDDR6、PCIe7/6+CXL3.x、UCIe、RSE/Caliptra接口、SCP/MCP和clock/power管理，边界并非只有CPU cores。[[Server：Open Chiplet Economy/Building Interoperable AI Systems with Chiplets- Arm Neoverse and Cadence in an Open Ecosystem.pdf#page=5|PDF p.5]]
- shift-left流程用Helium virtual platform、Xcelium simulation、Palladium emulation将PCIe/CXL/DDR/controller/VIP与partner subsystem提前协同验证。[[Server：Open Chiplet Economy/Building Interoperable AI Systems with Chiplets- Arm Neoverse and Cadence in an Open Ecosystem.pdf#page=6|PDF p.6]]
- Cadence chiplet manager区分FCSA-aligned system/security/control/debug/optional safety与design-specific NoC/interface/domain subsystem；debug处于always-on domain。[[Server：Open Chiplet Economy/Building Interoperable AI Systems with Chiplets- Arm Neoverse and Cadence in an Open Ecosystem.pdf#page=8|PDF p.8]]

## 指标与条件
p.9 IO-chiplet示例为4个direct-connect UCIe/SerDes slices，每slice8×224G，共32lanes，支持UCIe-S/A，UALink/Ethernet/combo boot configurable。没有提供有效带宽、功耗、latency或最终系统成本；不能只乘lane rate推断AI吞吐。[[Server：Open Chiplet Economy/Building Interoperable AI Systems with Chiplets- Arm Neoverse and Cadence in an Open Ecosystem.pdf#page=9|PDF p.9]]

## 图表与架构
已核对p.5/6/8/9的integration boundary、测试工具链和标准化/定制分界。它是产品/方案介绍，没有公开跨厂牌互操作矩阵或silicon validation日志。

## 关联与比较
[[knowledge/concepts/compute-memory-federated-model-contract|模型契约]]：virtual platform用于早期软件/功能集成，仍需timing/thermal/PI模型；[[knowledge/concepts/compute-memory-chiplet-system-contracts|多厂商芯粒的系统契约]]：共同管理服务是接口互操作的一部分。

## 不确定性与待验证
应请求特定CSS/IP/tool版本、可交付模型的保真度、FCSA符合性范围、coherency/domain配置、boot/security依赖及partner验证结果。材料的“mature/vendor-neutral”是生态定位，不替代完整合规测试。


## 原始页码导航
[[Server：Open Chiplet Economy/Building Interoperable AI Systems with Chiplets- Arm Neoverse and Cadence in an Open Ecosystem.pdf#page=3|p.3]] · [[Server：Open Chiplet Economy/Building Interoperable AI Systems with Chiplets- Arm Neoverse and Cadence in an Open Ecosystem.pdf#page=4|p.4]] · [[Server：Open Chiplet Economy/Building Interoperable AI Systems with Chiplets- Arm Neoverse and Cadence in an Open Ecosystem.pdf#page=5|p.5]] · [[Server：Open Chiplet Economy/Building Interoperable AI Systems with Chiplets- Arm Neoverse and Cadence in an Open Ecosystem.pdf#page=6|p.6]] · [[Server：Open Chiplet Economy/Building Interoperable AI Systems with Chiplets- Arm Neoverse and Cadence in an Open Ecosystem.pdf#page=7|p.7]] · [[Server：Open Chiplet Economy/Building Interoperable AI Systems with Chiplets- Arm Neoverse and Cadence in an Open Ecosystem.pdf#page=8|p.8]] · [[Server：Open Chiplet Economy/Building Interoperable AI Systems with Chiplets- Arm Neoverse and Cadence in an Open Ecosystem.pdf#page=9|p.9]] · [[Server：Open Chiplet Economy/Building Interoperable AI Systems with Chiplets- Arm Neoverse and Cadence in an Open Ecosystem.pdf#page=10|p.10]]
