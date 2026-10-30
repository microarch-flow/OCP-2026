---
type: comparison
title: "集成激光、外置激光与宽并行光：相同边界下再比较"
tags: [ocp2026, executive-expo]
---

# 集成激光、外置激光与宽并行光：相同边界下再比较

## 比较问题
在指定距离、总带宽、可用性和热环境下，如何选择光引擎位置、激光位置、lane速率/数量及可更换单元？本比较不宣称某缩写普遍胜出。

| 路径/来源 | 支持证据 | 换取的代价或未决条件 |
|---|---|---|
|TeraHop集成激光NPO|独立冷板；约5.5 pJ/bit含激光；6.4T初步32lane曲线|需匹配ASIC热边界、模块/激光现场更换；历史PIC FIT不能代替NPO可靠性|
|GO外置ELS/NPO|3.2T EVB回环<1e-10，ELS<8.5 W|<8.5 W只是光源；整引擎功耗/维修对照未统一|
|FIT高密XPO|12.8T/未来25.6T，液冷仿真及链路测试|体积密度与板上电通道损耗、流量、面板维修相互约束|
|Credo微发射器宽并行|不同发射器<1或<2pJ/bit；备用通道重映射|纤维数百至万量级、管理/gearbox、冗余耗尽及共同原因故障|
|TE可分离光路|NPO/CPO都可设计维修边界|连接器插损、污染与重复对准需测量|

证据：[[knowledge/sources/src-3c6dee4db3ee]] [[executive-sessions/40_Open Optical Interconnect Solutions for AI Scaling presented by Teraho.pdf#page=13|PDF p.13]] [[executive-sessions/40_Open Optical Interconnect Solutions for AI Scaling presented by Teraho.pdf#page=14|PDF p.14]]；[[knowledge/sources/src-b2f123d4da85]] [[executive-sessions/47_Scaling AI Infrastructure The Pivotal Role of Silicon Photonics in Ful.pdf#page=13|PDF p.13]]；[[knowledge/sources/src-6746624f9361]] [[executive-sessions/02_A High-Density, Liquid-Cooled Optical Interconnect Architecture for Ne.pdf#page=11|PDF p.11]] [[executive-sessions/02_A High-Density, Liquid-Cooled Optical Interconnect Architecture for Ne.pdf#page=14|PDF p.14]]；[[knowledge/sources/src-5fd8c43de698]] [[executive-sessions/58_Wider. Slower. Better Optics That Can Beat Copper presented by Credo.pdf#page=5|PDF p.5]] [[executive-sessions/58_Wider. Slower. Better Optics That Can Beat Copper presented by Credo.pdf#page=6|PDF p.6]]；[[knowledge/sources/src-a4d58f1be30f]] [[executive-sessions/50_Solving Power Density and Bandwidth Challenges in AI Infrastructure pr.pdf#page=7|PDF p.7]]。

## 必须保留的观点冲突
Genuine Optics把所比较CPO描述为极难维修/可能报废板；TE展示可分离CPO光段，TeraHop又分NPO/CPO/IOA。综合判断是**维修性取决于具体封装和连接器架构，不由CPO三个字决定**。[[executive-sessions/47_Scaling AI Infrastructure The Pivotal Role of Silicon Photonics in Ful.pdf#page=6|PDF p.6]] [[executive-sessions/40_Open Optical Interconnect Solutions for AI Scaling presented by Teraho.pdf#page=9|PDF p.9]] [[executive-sessions/50_Solving Power Density and Bandwidth Challenges in AI Infrastructure pr.pdf#page=7|PDF p.7]]

TeraHop对ELSFP额外损耗/功率的批评与GO的外置光源路线并存，缺少同拓扑对照，不能裁定谁更节能。Credo“60%降低功耗”基于约5→<2pJ/bit的链路估算，不是所有光模块或机柜。[[executive-sessions/40_Open Optical Interconnect Solutions for AI Scaling presented by Teraho.pdf#page=14|PDF p.14]] [[executive-sessions/47_Scaling AI Infrastructure The Pivotal Role of Silicon Photonics in Ful.pdf#page=16|PDF p.16]] [[executive-sessions/58_Wider. Slower. Better Optics That Can Beat Copper presented by Credo.pdf#page=7|PDF p.7]]

## 统一测试矩阵
- 电侧：全lane同时活动、host通道损耗与串扰、DSP/retimer/FEC配置。
- 光侧：功率预算、连接器数、污染/弯曲、激光冗余、pre/post-FEC BER与测试bit数。
- 热侧：流量/压降、进液温度、ASIC与激光热耦合、单泵失效。
- 运维：能否独立更换、断链窗口、盲插循环、备用通道耗尽、模块/芯片损失范围。
- 经济性：两端全部功耗、制造/测试良率、维护工时和可用吞吐，而非单器件pJ/bit。

## 未决问题
不同来源没有共享寿命统计和实测总链路边界；规模部署证据不足。PIC/laser/module/system FIT必须分别报告，伙伴名单不能代替失效率样本。

[[knowledge/concepts/executive-expo-optical-service-boundary]] · [[knowledge/concepts/executive-expo-manufacturing-service-chain]]
