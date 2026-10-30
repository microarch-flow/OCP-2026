---
type: concept
title: "光互连向内移动：真正改变的是热、损耗与维修边界"
tags: [ocp2026, executive-expo]
---

# 光互连向内移动：真正改变的是热、损耗与维修边界

## 定义
Pluggable、LPO、NPO、CPO、OCI、XPO并不都属于同一分类轴。前几类描述转换位置/信号处理，XPO主要是高密可插拔形态，OCI关注光学接口路径。**跨源归纳**：避免把缩写直接等同为功耗、价格或可维护性结论。

## 来源与页级证据
- Amphenol示意NPO约9 dB与XPO约19 dB电通道预算，并指出64lane同时活动的串扰可能让单lane BER成绩失去代表性。[[knowledge/sources/src-6b3929fc1d91]] [[executive-sessions/14_Co-Designing High-Speed Copper and Optical Interconnects.pdf#page=6|PDF p.6]] [[executive-sessions/14_Co-Designing High-Speed Copper and Optical Interconnects.pdf#page=7|PDF p.7]]
- TeraHop偏好独立冷板的集成激光NPO，声称约5.5 pJ/bit含激光；Genuine Optics展示外置ELS和NPO路径，各自边界不同。[[knowledge/sources/src-3c6dee4db3ee]] [[executive-sessions/40_Open Optical Interconnect Solutions for AI Scaling presented by Teraho.pdf#page=14|PDF p.14]] [[knowledge/sources/src-b2f123d4da85]] [[executive-sessions/47_Scaling AI Infrastructure The Pivotal Role of Silicon Photonics in Ful.pdf#page=13|PDF p.13]]
- TE强调在NPO/CPO中保留可分离光路，保护昂贵ASIC不因光路维修整体更换；这限制了“CPO必定整板报废”的泛化。[[knowledge/sources/src-a4d58f1be30f]] [[executive-sessions/50_Solving Power Density and Bandwidth Challenges in AI Infrastructure pr.pdf#page=7|PDF p.7]]
- Credo用宽并行低速通道和备用纤维重映射追求低能耗与可用性，与提高单lane速率的方案不是同一种容量扩展方式。[[knowledge/sources/src-5fd8c43de698]] [[executive-sessions/58_Wider. Slower. Better Optics That Can Beat Copper presented by Credo.pdf#page=5|PDF p.5]] [[executive-sessions/58_Wider. Slower. Better Optics That Can Beat Copper presented by Credo.pdf#page=6|PDF p.6]]

## 共识与分歧
共同趋势是电距离越短越容易控制高频损耗，但更靠近ASIC意味着热耦合、装配、清洁和维修复杂性上升。集成激光/外置激光争论必须统一光耦合损耗、温度、冗余、现场替换及统计对象，不能取两家最有利数字拼比较。

4芯光纤降低纤维及端接数；宽阵列微发射器则可能增加物理纤维数以降低单lane负担。两者是不同设计自由度，不应以“光纤越少越好”作为唯一标准。[[executive-sessions/40_Open Optical Interconnect Solutions for AI Scaling presented by Teraho.pdf#page=17|PDF p.17]] [[executive-sessions/58_Wider. Slower. Better Optics That Can Beat Copper presented by Credo.pdf#page=5|PDF p.5]]

## 适用条件
先画出host die→package→PCB/线缆→光引擎→激光→连接器→fiber→对端的完整通路；逐段列插损、功耗、温度、失效率、可替换单元与工序。链路级pJ/bit要写明含不含host SerDes、DSP、FEC、激光、gearbox和两端。

## 未决问题
展台眼图/BER不证明规模网络性能；PIC历史FIT不等于新模块FIT。需要多lane并发、温度/流量、FEC、样本量、实际bit数和寿命测试。市场支持、MSA成员或路线图均不代替部署结果。

## 来源延伸
[[knowledge/sources/src-62e8ecab28d6|AEC协同设计]] · [[knowledge/sources/src-6746624f9361|FIT XPO]] · [[knowledge/sources/src-0591a95e3946|Meta网络架构]] · [[knowledge/sources/src-b36ea15b7121|跨区域网络]] · [[knowledge/sources/src-f11eeb40a10a|200G/400G光链路实验]] · [[knowledge/sources/src-7f815b7c096d|LPO/NPO/CPO共存]] · [[knowledge/comparisons/executive-expo-optics-integration-tradeoffs]]
