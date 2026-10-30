---
type: comparison
title: "800 V 供电比较：把阶段、负载点与冷却边界对齐"
tags: [ocp2026, executive-expo]
---

# 800 V 供电比较：把阶段、负载点与冷却边界对齐

## 比较问题与范围
比较从设施输入到芯片核心的损耗与可用性。**只把同输入/输出、同负载、同冷却的数字横比**。下面的数字刻意保留各自不同边界，不形成优劣榜。

| 来源 | 原文边界和数字 | 关键限制 |
|---|---|---|
|Axiom|架构示例to-rack效率92%→97%→98%+|不是grid-to-chip；不是同站实测|
|Google|SST/原生HVDC内部估算>1% grid-to-chip收益|并列20–30%空间与9000安装小时未给统一项目规模|
|Delta|90/108 kW DC shelf最高98.5%|峰值与路线节点需分开|
|MEGMEET|100 kW AC/DC>98%；30 kW800→50V满载97.7%；10 kW峰值98.5%|不同模块/负载点，不能互相排名|
|LITEON|800→50V10kW峰98.7%/满98.1%；6kW峰98.2%/满97.8%|尺寸与功率不同|
|LITEON后级|54→12V满载96.9%；54→6V满载96.6%；54→0.8V四并800A满载87%|前两者Ta55°C；最终VRM边界不同|

证据：[[knowledge/sources/src-1899a389f6bc]] [[executive-sessions/26_From Dirt to Tokens Building AI Infrastructure as an Integrated System.pdf#page=10|PDF p.10]]；[[knowledge/sources/src-190536f5a5ce]] [[executive-sessions/24_From Chip to Grid Scaling Holistic AI Data Center Co-Design Through Op.pdf#page=18|PDF p.18]]；[[knowledge/sources/src-199810ce9b85]] [[executive-sessions/16_Delta 800 VDC Power and Cooling Solutions for Data Centers presented b.pdf#page=15|PDF p.15]]；[[knowledge/sources/src-086ed59f7391]] [[executive-sessions/36_Liquid-Cooled Power Shelf and 800 VDC platform for next generation dat.pdf#page=13|PDF p.13]] [[executive-sessions/36_Liquid-Cooled Power Shelf and 800 VDC platform for next generation dat.pdf#page=15|PDF p.15]]；[[knowledge/sources/src-99abff7266fc]] [[executive-sessions/44_Powering the AI Revolution Navigating the 800V-to-Chip Frontier presen.pdf#page=4|PDF p.4]] [[executive-sessions/44_Powering the AI Revolution Navigating the 800V-to-Chip Frontier presen.pdf#page=5|PDF p.5]] [[executive-sessions/44_Powering the AI Revolution Navigating the 800V-to-Chip Frontier presen.pdf#page=7|PDF p.7]] [[executive-sessions/44_Powering the AI Revolution Navigating the 800V-to-Chip Frontier presen.pdf#page=8|PDF p.8]] [[executive-sessions/44_Powering the AI Revolution Navigating the 800V-to-Chip Frontier presen.pdf#page=9|PDF p.9]]。

## 能效计算的常见错误
1. **乘峰值**：各级峰值可能对应不同负载。必须在同一负载工作点映射每级效率后相乘，再加配电和冷却损耗。
2. **少数一级就少一次转换**：LITEON所谓单级外部供电仍有芯片内IVR，命名不能替代功率边界。[[executive-sessions/44_Powering the AI Revolution Navigating the 800V-to-Chip Frontier presen.pdf#page=10|PDF p.10]]
3. **把预留容量当能量**：MaxLPS减少rack预留并不直接证明电费按同百分比下降。[[knowledge/sources/src-41b73a819a65]] [[executive-sessions/21_Every Megawatt Counts The Path to Building AI Factories with DSX MaxLP.pdf#page=5|PDF p.5]]
4. **把高压当安全保证**：故障检测、中断、隔离和备份分别需要设计；多rack共享供电扩大保护协调范围。[[knowledge/sources/src-d23e1373fc51]] [[executive-sessions/10_Beyond Power Density Building a Safe 800V DC Ecosystem presented by Ea.pdf#page=11|PDF p.11]]

## 架构与运维条件
Sidecar输出50V或将800V引到IT rack，是不同转换位置和维修边界。液冷电源还应把漏液时输出降额计入可用容量；BBU标称89 kW/90 s不能等于800 kW整柜90 s。[[knowledge/sources/src-a4d58f1be30f]] [[executive-sessions/50_Solving Power Density and Bandwidth Challenges in AI Infrastructure pr.pdf#page=3|PDF p.3]] [[knowledge/sources/src-086ed59f7391]] [[executive-sessions/36_Liquid-Cooled Power Shelf and 800 VDC platform for next generation dat.pdf#page=10|PDF p.10]]

## 验收建议与未决项
统一load sweep、输入电压、流量/进液温度、故障状态、计量误差；回放真实峰值和10kHz级动态负载，在DUT端量波形并控制测试夹具电感。[[knowledge/sources/src-2299f9ebe7cc]] [[executive-sessions/57_Validation Challenges for Next-Generation AI Power Racks From 100kW to.pdf#page=12|PDF p.12]] [[executive-sessions/57_Validation Challenges for Next-Generation AI Power Racks From 100kW to.pdf#page=16|PDF p.16]]
尚没有本组材料可支持跨厂商grid-to-chip效率排行榜，也没有以同推理SLA证明哪条800V路径成本最低。

[[knowledge/concepts/executive-expo-power-control-boundaries]]
