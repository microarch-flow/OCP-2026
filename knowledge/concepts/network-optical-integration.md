---
id: "network-optical-integration"
type: "concept"
title: "光学集成边界：LPO、NPO、CPO、XPO 与 Open CPX"
tags: ["ocp-2026", "networking"]
review_status: "synthesized"
---

# 光学集成边界：LPO、NPO、CPO、XPO 与 Open CPX

## 定义
这些名词不都在同一个维度：LPO描述线性/DSP分工，NPO/CPO描述光引擎相对ASIC的位置，XPO描述高密度可维护模块/热包络，Open CPX描述socketed光/铜引擎接口。因此“XPO对LPO”不一定是互斥选项。

## 来源与证据
Dell明确XPO可承载LPO或coherent DWDM，靠fly-over cable隔离ASIC与光模块；Open CPX用标准socket缩短近封装电通道。[[knowledge/sources/src-18fec3539510]] [[fti-workshop-short-reach-optical-interconnects/Beyond-Copper-Optical-Opportunities-for-AI-Scale-up-Fabrics.pdf#page=7|PDF p.7]][[knowledge/sources/src-18fec3539510]] [[fti-workshop-short-reach-optical-interconnects/Beyond-Copper-Optical-Opportunities-for-AI-Scale-up-Fabrics.pdf#page=8|PDF p.8]] Celestica把DAC/ACC/AEC/LPO/LRO/FRO/coherent置于共享包络的多引擎选择中。[[knowledge/sources/src-7569c3741a64]] [[ocp-special-focus-photonics/The-Interconnect-Inflection-Point-Evolving-Intra-and-Multi-Rack-Scale-Up-AI-Networks.pdf#page=5|PDF p.5]]

Meta对CPO/NPO的细化：CPO电路径最短、界面少、与ASIC供应链耦合；NPO有多厂模块/返工优势，但连接器和长走线增加signal-integrity风险，448G/lane若要retimer可能侵蚀能耗优势。[[knowledge/sources/src-ada5498062ed]] [[ocp-special-focus-photonics/Integrated-Optics-at-Scale-for-AI-Infrastructure-From-51.2T-CPO-Validation-to-Meta-s-102.4T-Integrated-Optics-Switch.pdf#page=8|PDF p.8]]

## 条件优先于名称
先确认lane rate、channel loss、reach、光预算、FEC、thermal与维修方式，再比较方案。Celestica的LPO 2–10m+是reach分层示意，Meta的100G/lane LPO给500m/2.5dB预算；不同design point不构成直接互斥。[[knowledge/sources/src-7569c3741a64]] [[ocp-special-focus-photonics/The-Interconnect-Inflection-Point-Evolving-Intra-and-Multi-Rack-Scale-Up-AI-Networks.pdf#page=6|PDF p.6]][[knowledge/sources/src-6ce06488969f]] [[networking/08_Operating Linear Pluggable Optics at Hyperscale From Link Management t.pdf#page=4|PDF p.4]]

## 系统选择问题
1. 哪部分电链路被缩短，retimer功耗是否真正消失？
2. 故障替换单位是module、ELS、engine还是整块switch/package？
3. bandwidth density是否计入coolant manifolds、fiber routing、power rails与维修空间？
4. 多供应商是MSA目标，还是已有交叉qualification矩阵？

这些是跨源工程归纳。没有统一平台的成本/能耗/故障实验时，不做全局排名。

## 关联
[[knowledge/comparisons/network-optics-integration-tradeoffs]] · [[knowledge/concepts/network-optics-reliability]]
