---
id: "src-b681b46ceff2"
type: "source"
title: "Open Silicon Photonics for AI Systems: Extending the MHS Platform Contract"
aliases: ["Open Silicon Photonics for AI Systems: Extending the MHS Platform Contract"]
speakers: "Bijan Nowroozi（Lightmatter）；Morris Repeta（Dell）"
source_path: "server/07_Open Silicon Photonics for AI Systems Extending the MHS Platform Contr.pdf"
source_git_blob_sha: "253e81502a9ee0eef0707b6f939817a49e9750f1"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 13
review_status: "analyzed-visual"
text_reviewed: true
key_pages_visual_checked: [2, 5, 6, 7, 8, 9, 10, 11]
evidence_pages: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
tags: ["ocp2026", "source", "compute-memory"]
concepts: ["[[knowledge/concepts/compute-memory-modular-platform-contract]]", "[[knowledge/concepts/compute-memory-package-memory-wall]]"]
---

# Open Silicon Photonics for AI Systems: Extending the MHS Platform Contract

## 核心结论
光引擎从前面板笼子移入板/封装后，原本由pluggable封装包住的机械、电源、散热、管理和可维护性问题转移给tray。开放互通的缺口是系统边界契约，而不仅是光器件本身。[[server/07_Open Silicon Photonics for AI Systems Extending the MHS Platform Contr.pdf#page=3|PDF p.3]] [[server/07_Open Silicon Photonics for AI Systems Extending the MHS Platform Contr.pdf#page=4|PDF p.4]] [[server/07_Open Silicon Photonics for AI Systems Extending the MHS Platform Contr.pdf#page=6|PDF p.6]]

## 关键证据
FPO可单独拔换；NPO需OE keep-out与socket/mezzanine FRU边界；CPO中FRU通常是package，需blind-mate fiber、external laser shelf、共享冷却及DC-SCM/RAS可见性。placement class与fiber上link profile是两个不同维度。[[server/07_Open Silicon Photonics for AI Systems Extending the MHS Platform Contr.pdf#page=5|PDF p.5]] [[server/07_Open Silicon Photonics for AI Systems Extending the MHS Platform Contr.pdf#page=6|PDF p.6]]

## 指标与条件
- p.2给reticle-class、224G、switch-side、CPO可用beachfront0.90假设：copper26、CPO93.6Tb/s/direction（3.6×）、APO die-face几何上限1191Tb/s/direction（46×）。**这是几何/路由预算，非成品有效payload吞吐。** 同页柱图另是XPU侧、HBM抢占edge的情景，不能把两组数字混算。[[server/07_Open Silicon Photonics for AI Systems Extending the MHS Platform Contr.pdf#page=2|PDF p.2]]
- >400Tb/s compute-tray routing、204.8T switch-tray/1RU是设计目标/示意；无同页BER/热/可制造性完整验证。[[server/07_Open Silicon Photonics for AI Systems Extending the MHS Platform Contr.pdf#page=7|PDF p.7]] [[server/07_Open Silicon Photonics for AI Systems Extending the MHS Platform Contr.pdf#page=8|PDF p.8]]
- p.10的约10× straggler tail降低、MFU55–65% target、<5pJ/bit、互连能耗占比37%→15%、sub10ns hop等缺完整拓扑/器件/测试条件。保留为作者系统效益主张，**不能当p99推理实测**。[[server/07_Open Silicon Photonics for AI Systems Extending the MHS Platform Contr.pdf#page=10|PDF p.10]]

## 图表与架构
五维contract为mechanical/power/high-speed/thermal/management。移除CMIS cage anchor后，需给OE和laser遥测新的归属，ELS可作为可替换单元，内部fiber需service loops。[[server/07_Open Silicon Photonics for AI Systems Extending the MHS Platform Contr.pdf#page=6|PDF p.6]] [[server/07_Open Silicon Photonics for AI Systems Extending the MHS Platform Contr.pdf#page=9|PDF p.9]]

## 关联与比较
[[knowledge/concepts/compute-memory-modular-platform-contract|模块化平台契约]] · [[knowledge/concepts/compute-memory-package-memory-wall|封装内存与I/O几何约束]]。本库推论：CPO提高密度可以扩大故障维修替换范围；可靠性、可维修性和可用性不能用同一MTBF数替代。

## 不确定性与待验证
p.9引用外部Meta fleet MTBF8.2M hours、第二代50M operating hours；后者是累计运行时，不是50M小时MTBF。本文未取得其样本量/失效定义，不作为本tray已证可靠性。白皮书1.0.x与2027spec drafts是演讲快照。[[server/07_Open Silicon Photonics for AI Systems Extending the MHS Platform Contr.pdf#page=9|PDF p.9]] [[server/07_Open Silicon Photonics for AI Systems Extending the MHS Platform Contr.pdf#page=12|PDF p.12]]

## 原始页码导航
[[server/07_Open Silicon Photonics for AI Systems Extending the MHS Platform Contr.pdf#page=2|p.2]] · [[server/07_Open Silicon Photonics for AI Systems Extending the MHS Platform Contr.pdf#page=3|p.3]] · [[server/07_Open Silicon Photonics for AI Systems Extending the MHS Platform Contr.pdf#page=4|p.4]] · [[server/07_Open Silicon Photonics for AI Systems Extending the MHS Platform Contr.pdf#page=5|p.5]] · [[server/07_Open Silicon Photonics for AI Systems Extending the MHS Platform Contr.pdf#page=6|p.6]] · [[server/07_Open Silicon Photonics for AI Systems Extending the MHS Platform Contr.pdf#page=7|p.7]] · [[server/07_Open Silicon Photonics for AI Systems Extending the MHS Platform Contr.pdf#page=8|p.8]] · [[server/07_Open Silicon Photonics for AI Systems Extending the MHS Platform Contr.pdf#page=9|p.9]] · [[server/07_Open Silicon Photonics for AI Systems Extending the MHS Platform Contr.pdf#page=10|p.10]] · [[server/07_Open Silicon Photonics for AI Systems Extending the MHS Platform Contr.pdf#page=11|p.11]] · [[server/07_Open Silicon Photonics for AI Systems Extending the MHS Platform Contr.pdf#page=12|p.12]]
