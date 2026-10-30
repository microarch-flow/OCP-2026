---
id: "network-optics-reliability"
type: "concept"
title: "光互连可靠性：从平均 BER 转向中断、故障域与修复时间"
tags: ["ocp-2026", "networking"]
review_status: "synthesized"
---

# 光互连可靠性：从平均 BER 转向中断、故障域与修复时间

## 定义与核心判断
可靠性不是某个pre-FEC BER阈值，而是给定应用容忍窗口内的中断率、影响范围、恢复/维修时间与证据可归因性。**本页为跨源归纳，不是新的测量结果。**

## 证据链
- Meta LPO：100G/lane生产LPO-LPO，同模式/成熟度比较，中断少约2倍，实验室2.96M link-hours无模块可归因故障；不能混用生产/实验分母。[[knowledge/sources/src-6ce06488969f]] [[networking/08_Operating Linear Pluggable Optics at Hyperscale From Link Management t.pdf#page=5|PDF p.5]][[knowledge/sources/src-6ce06488969f]] [[networking/08_Operating Linear Pluggable Optics at Hyperscale From Link Management t.pdf#page=8|PDF p.8]][[knowledge/sources/src-6ce06488969f]] [[networking/08_Operating Linear Pluggable Optics at Hyperscale From Link Management t.pdf#page=9|PDF p.9]]
- Meta CPO：Phase2全中断ALIR0.2%，剔除已知ELS SMT故障0.04%；1.35M system-hours无不可维修故障，不能把零事件解释为无限寿命。[[knowledge/sources/src-ada5498062ed]] [[ocp-special-focus-photonics/Integrated-Optics-at-Scale-for-AI-Infrastructure-From-51.2T-CPO-Validation-to-Meta-s-102.4T-Integrated-Optics-Switch.pdf#page=6|PDF p.6]]
- CPO平均BER比FRO差，但中断率更低；BER健康预测在这组数据中不足。平均BER不描述错误burst、FEC codeword尾部或FW重启。[[knowledge/sources/src-ada5498062ed]] [[ocp-special-focus-photonics/Integrated-Optics-at-Scale-for-AI-Infrastructure-From-51.2T-CPO-Validation-to-Meta-s-102.4T-Integrated-Optics-Switch.pdf#page=5|PDF p.5]]
- Oracle：去DSP减少一类故障也会分散故障证据；需要local/remote×host/media归因、时间日志、跨重启保留、远端身份和安全修复。[[knowledge/sources/src-6e3f5ef8025b]] [[ocp-special-focus-photonics/Photonics-for-AI-Aligning-the-Stack-from-Components-to-Cloud.pdf#page=8|PDF p.8]][[knowledge/sources/src-6e3f5ef8025b]] [[ocp-special-focus-photonics/Photonics-for-AI-Aligning-the-Stack-from-Components-to-Cloud.pdf#page=9|PDF p.9]][[knowledge/sources/src-6e3f5ef8025b]] [[ocp-special-focus-photonics/Photonics-for-AI-Aligning-the-Stack-from-Components-to-Cloud.pdf#page=12|PDF p.12]]
- 外置laser冷板和弹性TIM证明维修边界需要热/机械协同，不是“模块可拔”四字即解决。[[knowledge/sources/src-47ddbe6839d0]] [[fti-workshop-short-reach-optical-interconnects/Rack-Ready-High-Power-ELSFPs-A-Co-Development-to-Support-CPO-Deployment-in-AI-Scale-Up-and-Scale-Out-Datacenters.pdf#page=6|PDF p.6]][[knowledge/sources/src-47ddbe6839d0]] [[fti-workshop-short-reach-optical-interconnects/Rack-Ready-High-Power-ELSFPs-A-Co-Development-to-Support-CPO-Deployment-in-AI-Scale-Up-and-Scale-Out-Datacenters.pdf#page=7|PDF p.7]]

## 适用条件与推理架构含义
我们的建议：把optical interruption与request trace/collective/KV迁移时间对齐，测每次flap的请求影响、retry放大、p99/ITL以及自动隔离后的剩余容量。训练checkpoint损失和推理SLO超标的成本函数不同；不能用训练平均throughput无影响证明推理无尾延迟损失。

成本可按“模块/ELS备件 + 现场工时 + 影响GPU时间 + 预留冗余”拆解。单模块W或购买价不涵盖blast radius、MTTR和误报造成的无谓更换。上述sources未给完整TCO，因此本页不编造$收益。

## 共识、边界与未决问题
证据支持“特定DSP-less实现可以更可靠”，不支持“所有DSP-less都更可靠”。LPO和CPO不共享故障域；不同temperature/build标准不能直接合并。未决：200G/448G跨厂方向性、连接器污染、zero-event置信界、重启证据持久性、每次中断对推理p99的实测。

## 关联
[[knowledge/comparisons/network-optics-integration-tradeoffs]] · [[knowledge/concepts/network-clock-evidence]] · [[knowledge/concepts/network-inference-acceptance]]
