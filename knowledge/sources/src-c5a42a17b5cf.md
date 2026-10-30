---
id: "src-c5a42a17b5cf"
type: "source"
title: "Microsoft/Arista XPO评估：212G仿真平台上的FRO/LRO/LPO边界"
source_path: "ocp-special-focus-photonics/System-Level-Evaluation-of-XPO-for-High-Density-Optical-Interconnects-in-AI-Infrastructure.pdf"
source_git_blob_sha: "f6df7ec889390f099b88ce82a51e174e4d7d1364"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 20
review_status: "analyzed-visual"
evidence_pages: [6, 7, 9, 10, 11, 12, 14, 16, 18, 19]
text_reviewed: true
key_pages_visual_checked: [12, 14, 16, 18]
tags: ["ocp2026", "networking"]
concepts: ["[[knowledge/concepts/network-optical-integration]]"]
---

# Microsoft/Arista XPO评估：212G仿真平台上的FRO/LRO/LPO边界

## 核心结论
XPO是可承载多种光电架构的formfactor，而非一种固定PHY。此实验表明同一封装下FRO余量最稳、LRO对光损更敏感、LPO TX仍需优化；它是retimer-based emulation，不是已完成GPU/switch系统验收。[[ocp-special-focus-photonics/System-Level-Evaluation-of-XPO-for-High-Density-Optical-Interconnects-in-AI-Infrastructure.pdf#page=9|PDF p.9]][[ocp-special-focus-photonics/System-Level-Evaluation-of-XPO-for-High-Density-Optical-Interconnects-in-AI-Infrastructure.pdf#page=18|PDF p.18]][[ocp-special-focus-photonics/System-Level-Evaluation-of-XPO-for-High-Density-Optical-Interconnects-in-AI-Infrastructure.pdf#page=19|PDF p.19]]

## 关键证据、指标与条件
- 4颗Agera3 retimer×16lane，212Gb/s，32AWG flyover300/600/900mm，液冷。switch侧固定300mm，另一端变化；测0/3dB光衰减。p.11标bump-to-bump15/19/23dB，但p.12/14横轴14/18/22dB，保留1dB内部差异。[[ocp-special-focus-photonics/System-Level-Evaluation-of-XPO-for-High-Density-Optical-Interconnects-in-AI-Infrastructure.pdf#page=9|PDF p.9]][[ocp-special-focus-photonics/System-Level-Evaluation-of-XPO-for-High-Density-Optical-Interconnects-in-AI-Infrastructure.pdf#page=10|PDF p.10]][[ocp-special-focus-photonics/System-Level-Evaluation-of-XPO-for-High-Density-Optical-Interconnects-in-AI-Infrastructure.pdf#page=11|PDF p.11]][[ocp-special-focus-photonics/System-Level-Evaluation-of-XPO-for-High-Density-Optical-Interconnects-in-AI-Infrastructure.pdf#page=12|PDF p.12]][[ocp-special-focus-photonics/System-Level-Evaluation-of-XPO-for-High-Density-Optical-Interconnects-in-AI-Infrastructure.pdf#page=14|PDF p.14]]
- FRO-FRO多点接近BER显示floor1e-13，长cable端约1e-12，0/3dB光损变化小；不是已证明BER为零。线为median、阴影IQR，不是全lane最坏值。[[ocp-special-focus-photonics/System-Level-Evaluation-of-XPO-for-High-Density-Optical-Interconnects-in-AI-Infrastructure.pdf#page=12|PDF p.12]]
- LRO-LRO接收端无DSP，3dB衰减后BER明显变差；p.14 accelerator长cable median约1e-7量级，比无衰减高，不能只看SNR约1dB变化就认为无影响。[[ocp-special-focus-photonics/System-Level-Evaluation-of-XPO-for-High-Density-Optical-Interconnects-in-AI-Infrastructure.pdf#page=14|PDF p.14]]
- LPO-FRO中switch侧~1e-10，accelerator侧~1e-8量级，作者给可接受1e-7范围并归因LPO TX。p.18还包含LPO-LPO，3dB衰减下可有~1e-6量级样本；不能把mixed-pair结果推广到LPO-LPO。[[ocp-special-focus-photonics/System-Level-Evaluation-of-XPO-for-High-Density-Optical-Interconnects-in-AI-Infrastructure.pdf#page=16|PDF p.16]][[ocp-special-focus-photonics/System-Level-Evaluation-of-XPO-for-High-Density-Optical-Interconnects-in-AI-Infrastructure.pdf#page=18|PDF p.18]]
- 204.8T/1OU@200G、409.6T/1OU@400G和500W/module cooling envelope是形态/热设计能力，不是测试平台有效吞吐或实际耗电。[[ocp-special-focus-photonics/System-Level-Evaluation-of-XPO-for-High-Density-Optical-Interconnects-in-AI-Infrastructure.pdf#page=6|PDF p.6]]

## 图表与架构
已核4页BER/SNR/boxplot。p.7特别将blast radius定义为硬件更换成本范围，而非workload影响；前面板FRU小，不保证该模块故障只影响一个请求。[[ocp-special-focus-photonics/System-Level-Evaluation-of-XPO-for-High-Density-Optical-Interconnects-in-AI-Infrastructure.pdf#page=7|PDF p.7]]

## 关联与比较
[[knowledge/concepts/network-optical-integration]]：800G LPO现场优于FRO与这里212G-lane LPO裕量有限并不冲突，代际、器件、channel和调参不同。

## 不确定性与待验证
材料明确下一步扩vendor/组合、标准化tuning、从emulation走向switch/accelerator。缺功耗实测、长时burst/flap、热循环和工作负载结果；“推理1–2代无需更深集成”为设计观点而非普遍容量界限。[[ocp-special-focus-photonics/System-Level-Evaluation-of-XPO-for-High-Density-Optical-Interconnects-in-AI-Infrastructure.pdf#page=7|PDF p.7]][[ocp-special-focus-photonics/System-Level-Evaluation-of-XPO-for-High-Density-Optical-Interconnects-in-AI-Infrastructure.pdf#page=19|PDF p.19]]

