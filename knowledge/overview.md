---
type: overview
title: 这批材料中的系统架构主线
updated: 2026-10-30
tags: [ocp2026, overview]
---

# 这批材料中的系统架构主线

这批材料反复讨论的工程问题是：如何把芯片、内存、网络、供电、冷却和运维组织成可交付的 AI 系统。它们提供了许多具体进展，但不能仅凭厂商演讲、路线图或不同条件下的倍率，得出一种架构普遍最优的结论。

下面是跨来源归纳。每个入口继续链接到逐篇笔记及原始 PDF 页；它不是对厂商结果的独立复现。

## 1 推理系统有更多拆分方式 评价标准也必须更完整

材料中的部署选择已经包括 prefill/decode、draft/verify、attention/FFN 等不同计算域的安排。拆分可以让不同的算力、存储与带宽资源更匹配任务，也会增加传输、同步、队列和状态迁移开销。

有意义的问题不是“拆得越细是否越先进”，而是具体工作负载在目标用户体验下获得多少有效输出、消耗多少能量、需要多少设备。单用户速度、总吞吐、TTFT、每 token 延迟和整条响应尾延迟必须分别记录，不能混成一个性能名次。

阅读入口：[[knowledge/concepts/ai-infra-inference-serving-shapes|推理组织方式]]、[[knowledge/concepts/executive-expo-inference-sla|推理 SLA 与比较边界]]、[[knowledge/comparisons/platform-inference-metric-boundaries|不同推理指标的边界]]。

## 2 内存创新不仅增加带宽 也改变重算与驻留条件

CXL 池化、GPU 到扩展内存的直接数据路径、SSD KV cache 和近数据处理，为扩大工作集、跨请求复用和减少数据搬运提供了不同方法。容量跨过工作集阈值时，减少重算本身就可能带来很大的收益。

因此，一个同时扩容和改路径的系统实验可以说明组合方案有价值，却不能单独证明链路快了同样倍数。需要把容量、缓存策略、命中率、数据路径、并发和成本作为不同变量。容量收益还要与故障隔离、可观测性和恢复代价一起评估。

阅读入口：[[knowledge/concepts/compute-memory-capacity-vs-datapath|容量收益与数据路径收益归因]]、[[knowledge/concepts/compute-memory-kv-placement|KV 放置]]、[[knowledge/concepts/compute-memory-cxl-failure-domain|CXL 故障域]]、[[knowledge/concepts/platform-storage-workload-contract|存储工作负载契约]]。

## 3 互连需要按作用范围和协议层次理解

Scale-up、scale-out、scale-across 面对不同的消息规模、往返时间、故障域和同步要求。多路径、深缓冲、光交换、LPO/NPO/CPO 也并非回答同一个问题。它们有真实的部署经验与工程进展，比较时需要保留各自作用的层次。

在光学侧，要分清模块、激光源、交换系统和整机的功率及维修边界。在协议侧，要分清链路控制、传输语义、拥塞控制算法、通信库和应用完成条件。“统一抽象”或一种互连名称，不能自动补齐所有层次的语义与验证。

阅读入口：[[knowledge/comparisons/network-transport-and-buffer-context|传输与缓冲的工作负载边界]]、[[knowledge/comparisons/network-optics-evidence-ladder|光学证据阶梯]]、[[knowledge/concepts/network-inference-acceptance|推理网络验收]]、[[knowledge/sources/src-92d1f86e9495|跨传输 Push Mode 的已公开与未定义部分]]。

## 4 供电与冷却是动态系统约束

800V、机柜供电侧柜、液冷、浸没和热回收材料讨论的不只是更高的额定功率。可用容量还受到冗余、暂态、故障切除、负载波动、热惯性、流体状态及现场操作流程的影响。

架构评估需要区分元件能力、整机资格试验、仿真和现场运行。局部部件节能不等于全站节能；稳态效率也不等于在真实负载轨迹下的年度成本。工作负载管理、功率控制和安全保护的时间尺度与职责应分别描述。

阅读入口：[[knowledge/concepts/power-cooling-grid-to-chip-contract|从电网到芯片的约束]]、[[knowledge/concepts/ai-infra-power-to-sla-contract|功率与 SLA 的关系]]、[[knowledge/concepts/immersion-qualification-evidence|浸没资格证据]]、[[knowledge/concepts/immersion-thermal-to-inference-slo|热表现与推理 SLO]]。

## 5 开放接口只有能部署 能验证 能维护才形成系统价值

模块化硬件、chiplet、开放固件和管理协议降低组合与复用的门槛，但并不自动保证系统可用。多供应商方案需要明确版本、能力、状态交接、有效范围和失败行为；遥测还应交代可观测内容、采样频率、时间对齐及其自身的资源开销。

材料中的现场案例反复说明：部件仍显示“健康”并不保证系统没有瓶颈；能够读取一个计数器，也不等于能够正确归因。设计、验证、升级、故障处理和备件替换应是一条连续的证据链。

阅读入口：[[knowledge/concepts/compute-memory-federated-model-contract|多供应商模型契约]]、[[knowledge/concepts/compute-memory-modular-platform-contract|模块化平台契约]]、[[knowledge/concepts/platform-firmware-decoupling|固件解耦]]、[[knowledge/concepts/platform-operability-contract|可运维性契约]]、[[knowledge/concepts/network-clock-evidence|时钟与遥测证据]]。

## 6 商业化比较要落到交付和有效服务成本

真实方案的价值可能来自更多驻留容量、更高有效利用率、更短部署周期、更少中断或更容易维护，而不只是某项峰值更高。相应地，成本边界需要纳入计算设备、网络、机架、供电冷却、软件支持、闲置与备用资源、故障损失和更新周期。

本材料集没有统一的报价、寿命期、利用率或服务边界，不能据此生成可靠的厂商 TCO 排名。可以先整理输入变量和可比较条件，再建立自己的成本模型。PUE、碳排放和用水指标也必须先对齐分母、地域、时间与系统边界。

阅读入口：[[knowledge/concepts/platform-open-adoption-delivery|开放方案的采用与交付]]、[[knowledge/concepts/executive-expo-manufacturing-service-chain|制造与服务链]]、[[knowledge/concepts/sustainability-functional-units-and-energy-boundaries|功能单位与能耗边界]]、[[knowledge/comparisons/sustainability-metric-reversal-and-accounting|指标反转与核算]]。

## 下一步怎么使用

以一个具体问题检索知识库，然后带着工作负载、约束、指标和测试条件回查原始证据。把“材料已经给出的信息”和“还需要测量或向供应商索取的信息”分开，避免把缺失条件自动补成有利假设。

[[knowledge/reading-guide|阅读路线]] · [[knowledge/source-quality|来源质量与限制]] · [[knowledge/index|总入口]]
