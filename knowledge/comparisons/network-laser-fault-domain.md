---
id: "network-laser-fault-domain"
type: "comparison"
title: "激光位置、故障影响与维修边界：ELS/ILS不能只比pJ"
tags: ["ocp2026", "networking"]
review_status: "synthesized"
---

# 激光位置、故障影响与维修边界：ELS/ILS不能只比pJ

## 核心问题
外置laser让维修更容易，集成laser让光路径更短，哪一个更好？**归纳结论：先定义失效单位和业务恢复目标，再选位置；OE位置与laser位置是独立坐标。**

## 两种主张与共同约束
Lumentum比较同OE ILS、board ELS、faceplate ELSFP：隔热/可维护性逐步增强，但PM fiber和供光接口更复杂。TeraHop则强调集成laser、独立NPO冷板、避免额外3dB光损与PM连接器。这是不同设计取舍，不应挑一侧的优势当完整系统结论。[[knowledge/sources/src-5342b85e0d5d]] [[ocp-special-focus-photonics/External-Laser-Source-Architectures-for-Deployable-CPO-Based-AI-Networks.pdf#page=4|PDF p.4]][[knowledge/sources/src-d6491ea2c316]] [[ocp-special-focus-photonics/Open-Optical-Connectivity-Solutions-for-AI-Scaling.pdf#page=14|PDF p.14]]

Ayar/Wiwynn有具体ELS热设计数据：100+模块8λ×23dBm目标、45°C入水；20模块/1OU、1.3LPM、laser50±1°C。它证明该热结构可行，不证明任何共享laser布局都小故障影响；同页功率分布也并非所有样本≥23dBm目标。[[knowledge/sources/src-47ddbe6839d0]] [[fti-workshop-short-reach-optical-interconnects/Rack-Ready-High-Power-ELSFPs-A-Co-Development-to-Support-CPO-Deployment-in-AI-Scale-Up-and-Scale-Out-Datacenters.pdf#page=5|PDF p.5]][[knowledge/sources/src-47ddbe6839d0]] [[fti-workshop-short-reach-optical-interconnects/Rack-Ready-High-Power-ELSFPs-A-Co-Development-to-Support-CPO-Deployment-in-AI-Scale-Up-and-Scale-Out-Datacenters.pdf#page=7|PDF p.7]]

## 必须分开三种blast radius
1. **硬件替换范围**：XPO评估把它定义为换module还是连accelerator一起换；这不是workload范围。[[knowledge/sources/src-c5a42a17b5cf]] [[ocp-special-focus-photonics/System-Level-Evaluation-of-XPO-for-High-Density-Optical-Interconnects-in-AI-Infrastructure.pdf#page=7|PDF p.7]]
2. **物理容量损失**：Microsoft按laser分区、λ分区和shuffle展示100%→25–50%/25%，是通道占比示意；一个dense connector或共享供电仍可能共同失效。[[knowledge/sources/src-355fab7308df]] [[ocp-special-focus-photonics/Optical-Scale-Up-AI-Systems-Architectures-Standards-and-Resiliency-Strategies.pdf#page=6|PDF p.6]][[knowledge/sources/src-355fab7308df]] [[ocp-special-focus-photonics/Optical-Scale-Up-AI-Systems-Architectures-Standards-and-Resiliency-Strategies.pdf#page=7|PDF p.7]][[knowledge/sources/src-355fab7308df]] [[ocp-special-focus-photonics/Optical-Scale-Up-AI-Systems-Architectures-Standards-and-Resiliency-Strategies.pdf#page=8|PDF p.8]]
3. **业务损失**：25%lane down对同步collective、MoE专家热点或单请求KV路径可能产生非线性影响；需请求trace测量，而不是直接乘容量比例。

## 冗余不能默认独立
SROI讨论把1×800拆4×200以便降级；P^4式可靠性只有独立故障成立，共享laser/PIC/connector会破坏独立性。OCS 1:N spare池也只能换连接，不能自动迁移XPU状态。[[knowledge/sources/src-7eea0f19f00b]] [[fti-workshop-short-reach-optical-interconnects/Scale-up-optical-reliability-and-GPU-system-resiliency-to-optical-link-flaps.pdf#page=28|PDF p.28]][[knowledge/sources/src-7eea0f19f00b]] [[fti-workshop-short-reach-optical-interconnects/Scale-up-optical-reliability-and-GPU-system-resiliency-to-optical-link-flaps.pdf#page=32|PDF p.32]][[knowledge/sources/src-0ff8784e94af]] [[networking/Optically-Accelerated AI Clusters Enabled by Interoperable Multi-Vendor OCSs- Use Cases.pdf#page=8|PDF p.8]][[knowledge/sources/src-0ff8784e94af]] [[networking/Optically-Accelerated AI Clusters Enabled by Interoperable Multi-Vendor OCSs- Use Cases.pdf#page=10|PDF p.10]]

Meta CPO的已知ELS SMT故障去除前后ALIR0.2%→0.04%是**条件性分析**，说明工艺/组件归因重要，而非证明ELS天生差或好。Oracle污染归因90%L1故障、97%换模块，则提醒维护操作也是系统失效链一环。[[knowledge/sources/src-ada5498062ed]] [[ocp-special-focus-photonics/Integrated-Optics-at-Scale-for-AI-Infrastructure-From-51.2T-CPO-Validation-to-Meta-s-102.4T-Integrated-Optics-Switch.pdf#page=4|PDF p.4]][[knowledge/sources/src-ada5498062ed]] [[ocp-special-focus-photonics/Integrated-Optics-at-Scale-for-AI-Infrastructure-From-51.2T-CPO-Validation-to-Meta-s-102.4T-Integrated-Optics-Switch.pdf#page=6|PDF p.6]][[knowledge/sources/src-9f511e524c56]] [[ocp-special-focus-photonics/Lessons-learned-from-GW-scale-AI-deployments.pdf#page=11|PDF p.11]]

## 建议的验收合同
对每个laser/OE/connector/电源域建lane映射；注入单故障，记录检测时间、停顿、剩余带宽、隔离、FRU更换工时、复测与受影响请求。成本模型计备件、维修劳动、冷却、冗余容量和GPU不可用时间；没有这些分母，不从component FIT推整机TCO。[[knowledge/concepts/network-optics-reliability]]

