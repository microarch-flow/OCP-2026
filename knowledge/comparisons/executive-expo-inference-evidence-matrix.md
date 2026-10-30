---
type: comparison
title: "推理收益比较：哪些数字可复现，哪些还不能横比"
tags: [ocp2026, executive-expo]
---

# 推理收益比较：哪些数字可复现，哪些还不能横比

## 比较问题与统一口径
比较的是**同质量、同请求分布、同SLA的系统有效产出/成本**，不是厂商宣传倍数排行。以下保留每个实验本来的比较对象；没有共同基线的结果明确不可横比。

| 来源/机制 | 原文量化结果 | 已知条件 | 不可省略的限制 |
|---|---|---|---|
|Astera PCIe6 fabric|TPS +50%；prefill-heavy +90%|Qwen3.5-122B，对比两个较小switch|缺完整SLA/配置，非所有模型收益|
|Astera Leo CXL KV|“62% Faster” TTFT，TPS +22%|Qwen2.5-32B、4×H200、IntelGNR、对比CPU DRAM|与上一行不同实验；Faster不擅自改为时长降低62%|
|MARS KV池|平均TTFT80.76→15.45 s（重算→CXL-DDR）|同页另有SSD/Hybrid|尾值分位未给，不能与其他请求集排名|
|Solidigm共享SSD|p50 TTFT18.38→2.20 s|99K token、并发1、四副本轮转|避免重算，不是介质延迟比较|
|MaxLPS|同声称TPS下rack预留120→90 kW|Kimi-K2.5 FP4、8K/1K、GB200|缺尾时延，33%是机架容量提升|
|Arm CPU|Terminal1.93×、SWE2.00×机架性能|引用Signal65，对照EPYCTurin|完整方法在外部，非端到端任务成功率|
|d-Matrix AFD|845 token/s/user；64并发20,145 total|GPU attention+Corsair FFN|845×64≠20,145；同页口径未解释|

页级证据：[[knowledge/sources/src-f1226a6f9088]] [[executive-sessions/07_AI Your Way Compute Agnostic, Rack-Scale Architecture for AI Factories.pdf#page=9|PDF p.9]] [[executive-sessions/07_AI Your Way Compute Agnostic, Rack-Scale Architecture for AI Factories.pdf#page=10|PDF p.10]]；[[knowledge/sources/src-2f5c553a1e78]] [[executive-sessions/33_Introduction to Memory-centric AI Rack Systems (MARS) presented by SK .pdf#page=10|PDF p.10]]；[[knowledge/sources/src-2d7659491efb]] [[executive-sessions/54_The New Tokenomics How Data Infrastructure Increasingly Sets AI ROI pr.pdf#page=10|PDF p.10]]；[[knowledge/sources/src-41b73a819a65]] [[executive-sessions/21_Every Megawatt Counts The Path to Building AI Factories with DSX MaxLP.pdf#page=4|PDF p.4]]；[[knowledge/sources/src-2f507783aa88]] [[executive-sessions/45_Rethinking CPU Performance for the Agentic AI Era presented by Arm.pdf#page=11|PDF p.11]]；[[knowledge/sources/src-9e4b624fe6f8]] [[executive-sessions/55_The Path to Infinite Inference presented by d-Matrix.pdf#page=15|PDF p.15]]。

## 解析模型与测试结果不能混排
- Lightstorm2147 Gbps及429×训练需求是特定MHA/KV搬运预算解析，训练5Gbps也是假设；GQA与latent attention大幅改变结果。[[knowledge/sources/src-cae5c3fd8229]] [[executive-sessions/37_Multi-Dimensional Scalability for AI infrastructures.pdf#page=11|PDF p.11]]
- Hyve归一化TCO100→35是示意，不是同SLA采购对照。[[knowledge/sources/src-73c5e6030f9f]] [[executive-sessions/42_Open, Modular Rack-Scale AI Infrastructure for the Agentic Era present.pdf#page=9|PDF p.9]]
- OpenAI Pareto图给出目标函数但没有可用来排名的数值。[[knowledge/sources/src-6a803e49a956]] [[executive-sessions/17_Designing the next AI fabric When compute meets optics presented by Ce.pdf#page=3|PDF p.3]]

## 综合判断
目前可以较强支持“请求状态复用、内存/网络拓扑和功率配额会改变推理系统经济性”，不能支持“某一方案在全部推理任务上胜出”。优先级应由瓶颈定位决定：重算多→缓存，跨设备等待多→网络/分工，CPU工具堵塞→主机与存储，功率预留限制→功率调度。

## 下一份必须索取的证据
每个候选运行相同请求trace和成功判据；输出并发—吞吐—TTFT/TPOT尾分位—系统功率曲线，缓存冷/热与失效状态分列，再加入BOM、软件许可、运维与利用率。不同来源结果保留为假设生成器，不直接生成采购胜负。

[[knowledge/concepts/executive-expo-inference-sla]] · [[knowledge/concepts/executive-expo-kv-data-plane]]
