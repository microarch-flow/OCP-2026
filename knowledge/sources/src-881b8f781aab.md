---
id: "src-881b8f781aab"
type: "source"
title: "Bunch of Wires Flexi 1.0: a low cost, low power D2D interface"
aliases: ["Bunch of Wires Flexi 1.0: a low cost, low power D2D interface"]
speakers: "Morgan Whately — Distinguished Engineer, Infineon Technologies; Kash Johal — Founder, YorChip"
source_path: "Server：Open Chiplet Economy/Bunch of Wires Flexi 1.0 - a low cost, low power D2D interface.pdf"
source_git_blob_sha: "4de8e3fe75ee465f39d0a66cada9c66f9bb8c99e"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 11
review_status: "analyzed-visual"
text_reviewed: true
key_pages_visual_checked: [4, 5, 6, 8]
evidence_pages: [2, 3, 4, 5, 6, 7, 8, 9, 10]
tags: ["ocp2026", "source", "compute-memory"]
concepts: ["[[knowledge/concepts/compute-memory-chiplet-link-efficiency]]", "[[knowledge/concepts/compute-memory-chiplet-system-contracts]]"]
---

# Bunch of Wires Flexi 1.0: a low cost, low power D2D interface

## 核心结论
BoW.Flexi以simplicity/cost/power优先，而不是最高绝对带宽：源同步SDR、不要求独立sideband或link training，适合低成本/小规模chiplet连接。不要把Flexi1.0当作BoW2.0高速PHY的等价替代。

## 关键证据
- 最小6pin、1–128data lanes、frame支持可变长packet；基于BoW sideband电气0.65–0.95V。表中0–4Gb/s/pin为implementation-dependent范围，不能保证所有封装/节点达到4G。[[Server：Open Chiplet Economy/Bunch of Wires Flexi 1.0 - a low cost, low power D2D interface.pdf#page=3|PDF p.3]] [[Server：Open Chiplet Economy/Bunch of Wires Flexi 1.0 - a low cost, low power D2D interface.pdf#page=4|PDF p.4]]
- 双方都能initiator，transaction layer处理payload/config，link layer处理ECC/padding；config同链路访问partner寄存器，无需专用sideband。[[Server：Open Chiplet Economy/Bunch of Wires Flexi 1.0 - a low cost, low power D2D interface.pdf#page=5|PDF p.5]]
- 3bit CMD支持8类命令：posted/nonposted write、read/response、write response、virtual wire、extension、config/error。按command启用optional字段，PAD对齐lane width；ADDR1–64bit、DATA up to1024bit。[[Server：Open Chiplet Economy/Bunch of Wires Flexi 1.0 - a low cost, low power D2D interface.pdf#page=6|PDF p.6]]
- SIZE不在所有response中，fixed-size模式可省略；link-interface的virtual wire/config由transaction layer限制single-outstanding。config write无ack，不要与普通nonposted write completion混同。[[Server：Open Chiplet Economy/Bunch of Wires Flexi 1.0 - a low cost, low power D2D interface.pdf#page=7|PDF p.7]] [[Server：Open Chiplet Economy/Bunch of Wires Flexi 1.0 - a low cost, low power D2D interface.pdf#page=8|PDF p.8]]

## 指标与条件
没有ns/pJ/bit/面积实测。较少pin与无serialization是简化设计机制，不自动证明所有数据流更低端到端延迟。材料指向已发布1.0规范，同时reference RTL仍是计划；“规范发布”与“参考实现可用”不同。[[Server：Open Chiplet Economy/Bunch of Wires Flexi 1.0 - a low cost, low power D2D interface.pdf#page=4|PDF p.4]] [[Server：Open Chiplet Economy/Bunch of Wires Flexi 1.0 - a low cost, low power D2D interface.pdf#page=9|PDF p.9]] [[Server：Open Chiplet Economy/Bunch of Wires Flexi 1.0 - a low cost, low power D2D interface.pdf#page=10|PDF p.10]]

## 图表与架构
已核对BoW2.0比较表、双向源同步路径、packet结构与config/virtual-wire例子。p.8 x8 lane示例首beat由3bit CMD+5bit wire组成，virtual-wire vector内部不能插padding。

## 关联与比较
[[knowledge/concepts/compute-memory-chiplet-link-efficiency|协议粒度与有效带宽]]：Flexi frame使窄接口TLP/LLP packing行为不同于普通BoW TLL；[[knowledge/concepts/compute-memory-chiplet-system-contracts|系统契约]]：本链路不自行提供boot/security/power governance。

## 不确定性与待验证
具体lane数、clock、pad、ECC、buffer、max outstanding与application protocol mapping需要成对约定；跨工艺/封装PVT、error和power-state测试仍需独立验证。


## 原始页码导航
[[Server：Open Chiplet Economy/Bunch of Wires Flexi 1.0 - a low cost, low power D2D interface.pdf#page=2|p.2]] · [[Server：Open Chiplet Economy/Bunch of Wires Flexi 1.0 - a low cost, low power D2D interface.pdf#page=3|p.3]] · [[Server：Open Chiplet Economy/Bunch of Wires Flexi 1.0 - a low cost, low power D2D interface.pdf#page=4|p.4]] · [[Server：Open Chiplet Economy/Bunch of Wires Flexi 1.0 - a low cost, low power D2D interface.pdf#page=5|p.5]] · [[Server：Open Chiplet Economy/Bunch of Wires Flexi 1.0 - a low cost, low power D2D interface.pdf#page=6|p.6]] · [[Server：Open Chiplet Economy/Bunch of Wires Flexi 1.0 - a low cost, low power D2D interface.pdf#page=7|p.7]] · [[Server：Open Chiplet Economy/Bunch of Wires Flexi 1.0 - a low cost, low power D2D interface.pdf#page=8|p.8]] · [[Server：Open Chiplet Economy/Bunch of Wires Flexi 1.0 - a low cost, low power D2D interface.pdf#page=9|p.9]] · [[Server：Open Chiplet Economy/Bunch of Wires Flexi 1.0 - a low cost, low power D2D interface.pdf#page=10|p.10]]
