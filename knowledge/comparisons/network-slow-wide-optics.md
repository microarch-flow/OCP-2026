---
id: "network-slow-wide-optics"
type: "comparison"
title: "宽而慢的光I/O：省下SerDes之后，成本转移到哪里"
tags: ["ocp2026", "networking"]
review_status: "synthesized"
---

# 宽而慢的光I/O：省下SerDes之后，成本转移到哪里

## 定义与适用问题
slow-wide用更多低速NRZ通道换取低模拟带宽/较少高速DSP；其优势只有在ASIC原生电接口、光通道、纤维和连接器协同下成立。这里比较路线与证据成熟度，不在不一致的pJ/bit上排榜。

## 四类路线的真实边界
- **µLED阵列**：Avicena提出原生1–8G多lane，已出货evaluation kit约335×3G≈1T；>10Tb/mm²和<1pJ的主张不能等同当前约1mm²的1T kit性能。若ASIC仍输出少量200G lane，gearbox成本会回来。[[knowledge/sources/src-5cd976d9333c]] [[fti-workshop-short-reach-optical-interconnects/LED-Interconnects-Addressing-the-Future-of-Scale-In-and-Scale-Up-Connectivity.pdf#page=8|PDF p.8]][[knowledge/sources/src-5cd976d9333c]] [[fti-workshop-short-reach-optical-interconnects/LED-Interconnects-Addressing-the-Future-of-Scale-In-and-Scale-Up-Connectivity.pdf#page=12|PDF p.12]]
- **µVCSEL/VCSEL阵列**：LightXcelerate演示32G，64/100/200G属路线；57lane×32G与3.2T总量口径需澄清。Lumentum真实PCIe5 PoC是多个32G NRZ over OM3，<2.5pJ/bit仍是目标，error-free无bits/时长则不能报告零BER。[[knowledge/sources/src-576204a1c08c]] [[fti-workshop-short-reach-optical-interconnects/High-Density-Optical-I-O-Using-Micro-VCSEL-Arrays-and-Multicore-Fiber.pdf#page=6|PDF p.6]][[knowledge/sources/src-576204a1c08c]] [[fti-workshop-short-reach-optical-interconnects/High-Density-Optical-I-O-Using-Micro-VCSEL-Arrays-and-Multicore-Fiber.pdf#page=10|PDF p.10]][[knowledge/sources/src-e71619784d90]] [[ocp-special-focus-photonics/Slow-and-Wide-12.8T-VCSEL-solutions.pdf#page=5|PDF p.5]]
- **NRZ+WDM/BiDi OCI**：把4λ/方向压回一根双向纤维，减少fibers却增加激光谱线、mux、锁定/热控制约束；OCI是PHY标准，不指定唯一封装，也不替代上层内存/传输语义。[[knowledge/sources/src-3f2d49fba822]] [[ocp-special-focus-photonics/CPO, OCI.pdf#page=12|PDF p.12]][[knowledge/sources/src-355fab7308df]] [[ocp-special-focus-photonics/Optical-Scale-Up-AI-Systems-Architectures-Standards-and-Resiliency-Strategies.pdf#page=12|PDF p.12]]
- **NRZ+MCF**：4core×50G可得200G/fiber，避免WDM mux，但fanout、连接器/弯折串扰和多源成熟度转为重要成本。TeraHop“较低成本”假设MCF约4×SMF，不是完整安装报价。[[knowledge/sources/src-d6491ea2c316]] [[ocp-special-focus-photonics/Open-Optical-Connectivity-Solutions-for-AI-Scaling.pdf#page=18|PDF p.18]][[knowledge/sources/src-d6491ea2c316]] [[ocp-special-focus-photonics/Open-Optical-Connectivity-Solutions-for-AI-Scaling.pdf#page=19|PDF p.19]]

## 系统预算如何守恒（综合判断）
先固定每方向有效吞吐，再列：ASIC I/O/gearbox + driver/TIA/CDR + laser/TEC + mux/split/coupling loss + connector/fiber + 冷却。必须同时注明单端/双端、line-rate/有效payload、idle/active、是否含spares。SROI给≤5pJ/bit/end光学、≤10pJ/bit/end含SerDes等是**需求**，不是所有候选已达到。[[knowledge/sources/src-30a24adc4071]] [[fti-workshop-short-reach-optical-interconnects/Short-Reach-Optical-Interface-for-Scale-up.pdf#page=5|PDF p.5]]

带宽密度也要区分die edge、光引擎面积、faceplate、完整tray。Lightmatter指出纤维密度越高，越能为可拆FAU腾出机械空间；PPK181FAU的99.5%<2dB良率不能直接当多FAU整包良率。[[knowledge/sources/src-7c14800717c7]] [[ocp-special-focus-photonics/High-Speed-Open-Silicon-Photonics-Reference-Designs.pdf#page=6|PDF p.6]][[knowledge/sources/src-7c14800717c7]] [[ocp-special-focus-photonics/High-Speed-Open-Silicon-Photonics-Reference-Designs.pdf#page=8|PDF p.8]]

## 邻近但不同：介质波导
Point2 RF e-Tube有主动RF芯片；AttoTude基带DiAx主张无额外器件，但224G展示用了AWG预均衡和实时DSP，未给该实验线长。它们值得放进5–30m候选集，却不能凭“非光”认定更低总功率/1000倍可靠。[[knowledge/sources/src-d7ca24836953]] [[ocp-special-focus-photonics/Alternate-Scalable-AI-Interconnects.pdf#page=5|PDF p.5]][[knowledge/sources/src-d7ca24836953]] [[ocp-special-focus-photonics/Alternate-Scalable-AI-Interconnects.pdf#page=11|PDF p.11]][[knowledge/sources/src-d7ca24836953]] [[ocp-special-focus-photonics/Alternate-Scalable-AI-Interconnects.pdf#page=12|PDF p.12]]

## 未决实验
需要同ASIC电口、同有效Tb/s、同reach、同错误容忍度的lane故障/备用切换、热、装配与功耗联合测试。推理架构要先画出EP/TP/KV通信图；不存在所有连接同时改为同一种“宽光”的普适最优。[[knowledge/concepts/network-inference-acceptance]] · [[knowledge/concepts/network-optical-integration]]

