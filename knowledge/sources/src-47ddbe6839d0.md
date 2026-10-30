---
id: "src-47ddbe6839d0"
type: "source"
title: "Rack-Ready High-Power ELSFPs: A Co-Development to Support CPO Deployment"
source_path: "fti-workshop-short-reach-optical-interconnects/Rack-Ready-High-Power-ELSFPs-A-Co-Development-to-Support-CPO-Deployment-in-AI-Scale-Up-and-Scale-Out-Datacenters.pdf"
source_git_blob_sha: "78c22a1c7b4742abc87f05cdfc532128efa0beb4"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 10
review_status: "analyzed-visual"
evidence_pages: [2, 3, 4, 5, 6, 7, 8, 9]
text_reviewed: true
key_pages_visual_checked: [5, 7, 8]
tags: ["ocp2026", "photonics"]
concepts: ["[[knowledge/concepts/network-optics-reliability]]"]
---

# Rack-Ready High-Power ELSFPs: A Co-Development to Support CPO Deployment

## 核心结论
Ayar Labs与Wiwynn展示的是“可插拔激光源+冷板+弹性TIM”的系统协同，而不只是激光器单体指标；可维修性依赖热接触在反复插拔后的稳定性。[[fti-workshop-short-reach-optical-interconnects/Rack-Ready-High-Power-ELSFPs-A-Co-Development-to-Support-CPO-Deployment-in-AI-Scale-Up-and-Scale-Out-Datacenters.pdf#page=2|PDF p.2]][[fti-workshop-short-reach-optical-interconnects/Rack-Ready-High-Power-ELSFPs-A-Co-Development-to-Support-CPO-Deployment-in-AI-Scale-Up-and-Scale-Out-Datacenters.pdf#page=6|PDF p.6]][[fti-workshop-short-reach-optical-interconnects/Rack-Ready-High-Power-ELSFPs-A-Co-Development-to-Support-CPO-Deployment-in-AI-Scale-Up-and-Scale-Out-Datacenters.pdf#page=7|PDF p.7]]

## 关键证据
- Wiwynn给定流量、温度、压力、分流与热阻边界，Ayar设计8×23 dBm通道ELSFP并以主动TEC保持laser set point。[[fti-workshop-short-reach-optical-interconnects/Rack-Ready-High-Power-ELSFPs-A-Co-Development-to-Support-CPO-Deployment-in-AI-Scale-Up-and-Scale-Out-Datacenters.pdf#page=2|PDF p.2]][[fti-workshop-short-reach-optical-interconnects/Rack-Ready-High-Power-ELSFPs-A-Co-Development-to-Support-CPO-Deployment-in-AI-Scale-Up-and-Scale-Out-Datacenters.pdf#page=3|PDF p.3]]
- 石墨弹性TIM由铍铜弹簧片支撑，避免笼子开口接触面积受限与插拔损坏；局部fin pitch重分配流量，表面温差从2.9°C降至0.8°C。[[fti-workshop-short-reach-optical-interconnects/Rack-Ready-High-Power-ELSFPs-A-Co-Development-to-Support-CPO-Deployment-in-AI-Scale-Up-and-Scale-Out-Datacenters.pdf#page=7|PDF p.7]]
- 1OU内冷却20个belly-to-belly ELSFP；声称数百次重复插拔未出现TIM磨损、现场无需重涂，但未给完整磨损统计或循环后热阻分布。[[fti-workshop-short-reach-optical-interconnects/Rack-Ready-High-Power-ELSFPs-A-Co-Development-to-Support-CPO-Deployment-in-AI-Scale-Up-and-Scale-Out-Datacenters.pdf#page=6|PDF p.6]]

## 指标与条件
- 100+模块表征，所有激光开启、die 50°C、回反-20 dB，冷却液入口45°C。[[fti-workshop-short-reach-optical-interconnects/Rack-Ready-High-Power-ELSFPs-A-Co-Development-to-Support-CPO-Deployment-in-AI-Scale-Up-and-Scale-Out-Datacenters.pdf#page=4|PDF p.4]]
- 输出均值23.4 dBm（σ0.32 dB）；SMSR均值53 dB（σ1.5 dB）；线宽0.16 MHz（σ0.04 MHz）；平均RIN -158 dB/Hz（σ0.8 dB/Hz）。[[fti-workshop-short-reach-optical-interconnects/Rack-Ready-High-Power-ELSFPs-A-Co-Development-to-Support-CPO-Deployment-in-AI-Scale-Up-and-Scale-Out-Datacenters.pdf#page=5|PDF p.5]]
- 页内边界：SMSR>47 dB、线宽<0.37 MHz、RIN<-154 dB/Hz。RIN曲线是**代表性单通道**，不是全批次频谱证明。[[fti-workshop-short-reach-optical-interconnects/Rack-Ready-High-Power-ELSFPs-A-Co-Development-to-Support-CPO-Deployment-in-AI-Scale-Up-and-Scale-Out-Datacenters.pdf#page=5|PDF p.5]]
- 20模块热验证：45°C入口、1.3 L/min，激光die 50±1°C；只画上侧10个模块，下侧“同样趋势”属作者陈述。[[fti-workshop-short-reach-optical-interconnects/Rack-Ready-High-Power-ELSFPs-A-Co-Development-to-Support-CPO-Deployment-in-AI-Scale-Up-and-Scale-Out-Datacenters.pdf#page=8|PDF p.8]]

## 图表与架构
已核对分布直方图、冷板截面、局部fin布局、p.8温度与功率双轴图。p.5输出直方图存在23 dBm目标以下样本，不能把“所有laser meets spec”误写为每个样本都≥23 dBm；该页为SMSR/线宽/RIN明确给了spec阈值。p.9总结的RIN正负号/方向写法有歧义，应以p.5详细定义为准。[[fti-workshop-short-reach-optical-interconnects/Rack-Ready-High-Power-ELSFPs-A-Co-Development-to-Support-CPO-Deployment-in-AI-Scale-Up-and-Scale-Out-Datacenters.pdf#page=5|PDF p.5]][[fti-workshop-short-reach-optical-interconnects/Rack-Ready-High-Power-ELSFPs-A-Co-Development-to-Support-CPO-Deployment-in-AI-Scale-Up-and-Scale-Out-Datacenters.pdf#page=9|PDF p.9]]

## 关联与比较
[[knowledge/concepts/network-optics-reliability]]；与 [[knowledge/sources/src-ada5498062ed]] 的ELS故障归因对读：可更换不等于无需可靠性验证。

## 不确定性与待验证
没有系统电功耗、TEC占比、激光寿命/故障FIT、压力损失、漏液与故障停机时间。光功率dBm不是模块供电功耗，不能用23.4 dBm直接计算TCO节省。
