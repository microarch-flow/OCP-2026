---
id: "network-clock-evidence"
type: "concept"
title: "时间对齐的遥测证据：不确定窗口、缺失语义与安全闭环"
tags: ["ocp-2026", "networking"]
review_status: "synthesized"
---

# 时间对齐的遥测证据：不确定窗口、缺失语义与安全闭环

## 定义与共识
同一dashboard时间窗不等于同一物理时刻。每样本需local→UTC映射、offset/skew、freshness、WOU及source provenance；缺失support或权限应保持显式。[[knowledge/sources/src-fb4535953716]] [[Time Appliances/Clock-Aligned Telemetry for AI Clusters- From BMC to GPU to Fleet.pdf#page=5|PDF p.5]][[knowledge/sources/src-fb4535953716]] [[Time Appliances/Clock-Aligned Telemetry for AI Clusters- From BMC to GPU to Fleet.pdf#page=6|PDF p.6]][[knowledge/sources/src-fb4535953716]] [[Time Appliances/Clock-Aligned Telemetry for AI Clusters- From BMC to GPU to Fleet.pdf#page=8|PDF p.8]]

## 三个不同的时间问题
1. **事件关联**：光链路flap与GPU stall的先后若落在重叠WOU内，不应声称确定因果。Oracle要求timestamped事件与reset后保留。[[knowledge/sources/src-6e3f5ef8025b]] [[ocp-special-focus-photonics/Photonics-for-AI-Aligning-the-Stack-from-Components-to-Cloud.pdf#page=9|PDF p.9]]
2. **控制采样**：1s live telemetry目标不捕捉所有微burst；forensic路径需不同成本/粒度。SONiC on-device “ms loop”是架构意图而非实测保证。[[knowledge/sources/src-fb4535953716]] [[Time Appliances/Clock-Aligned Telemetry for AI Clusters- From BMC to GPU to Fleet.pdf#page=7|PDF p.7]][[knowledge/sources/src-e59f410df3c1]] [[sonic-workshop/Plug-and-Play-ML-Pipelines-for-SONiC-On-Device-Intelligence-with-Advanced-Feature-Extraction.pdf#page=10|PDF p.10]]
3. **调度可寻址性**：OCS实验认为共同绝对时间接口比进一步压低ns同步误差更紧迫，但其测试共享kernel clock，真实PTP仍未来工作。[[knowledge/sources/src-96d8cd0fedf0]] [[Time Appliances/Precision-Time Circuit Switching for AI Training Fabrics- When Packet Switching Is Enough.pdf#page=4|PDF p.4]][[knowledge/sources/src-96d8cd0fedf0]] [[Time Appliances/Precision-Time Circuit Switching for AI Training Fabrics- When Packet Switching Is Enough.pdf#page=9|PDF p.9]][[knowledge/sources/src-96d8cd0fedf0]] [[Time Appliances/Precision-Time Circuit Switching for AI Training Fabrics- When Packet Switching Is Enough.pdf#page=12|PDF p.12]]

## 安全闭环（综合建议）
feature vector必须继承quality/WOU/schema版本，否则聚合会把采样偏差包装成模型确定性。模型可输出建议不代表动作应自动执行；至少需要capability gate、阈值、cgroup、回滚、动作审计与负对照测试。Marvell的“ZERO effect”尚缺CPU/转发stress测试。[[knowledge/sources/src-e59f410df3c1]] [[sonic-workshop/Plug-and-Play-ML-Pipelines-for-SONiC-On-Device-Intelligence-with-Advanced-Feature-Extraction.pdf#page=7|PDF p.7]][[knowledge/sources/src-e59f410df3c1]] [[sonic-workshop/Plug-and-Play-ML-Pipelines-for-SONiC-On-Device-Intelligence-with-Advanced-Feature-Extraction.pdf#page=12|PDF p.12]]

## 未决问题
怎样计算并传播WOU？边缘clock loss如何降级？采样/预测误差与真实event time uncertainty如何分开？源文件没有统一生产benchmark，需要原始trace和校时状态。

## 关联
[[knowledge/concepts/network-optics-reliability]] · [[knowledge/concepts/network-ocs-control]] · [[knowledge/concepts/network-inference-acceptance]]
