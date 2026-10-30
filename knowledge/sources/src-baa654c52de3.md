---
id: "src-baa654c52de3"
type: "source"
title: "Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference"
aliases: ["Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference"]
speakers: "Allan Cantle — CEO, Nallasway; contributors Amphenol, Crealien, Credo, Empower, FIT, LOTES"
source_path: "server/02_Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference.pdf"
source_git_blob_sha: "fd2dd8435f655af6e729de5cb408eb49152203f3"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 20
review_status: "analyzed-visual"
text_reviewed: true
key_pages_visual_checked: [5, 7, 8, 11, 12, 13, 15, 16, 17, 18]
evidence_pages: [2, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
tags: ["ocp2026", "source", "compute-memory"]
concepts: ["[[knowledge/concepts/compute-memory-chiplet-link-efficiency]]", "[[knowledge/concepts/compute-memory-kv-placement]]"]
---

# Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference

## 核心结论
HPCM2026/Weaver提出用大量socketed buffered LPDDR模块、轻量串行接口和有机基板，在单reticle compute die周围同时增加容量与带宽。**这是寻求adopter与PoC的概念方案**，不是已量产的“无需HBM即可取代GPU”结论。p.19明确请求帮助把concept变为PoC。[[server/02_Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference.pdf#page=19|PDF p.19]]

## 关键证据
- OmniConnect LSI作为可后绑定IO：memory/scale-up/scale-out比例可选；演讲宣称AXI over112Gb/s VSR SerDes、1.15pJ/bit、约35ns one-way、noncoherent memory interface。此为方案参数，未给系统级测量条件。[[server/02_Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference.pdf#page=3|PDF p.3]]
- Weaver1 memory buffer连接4×x32 LPDDR5X-9600，用12×112G transceiver；OC-DDIMM模块16–64GB，基于96pad/0.5mm pitch的M.2派生connector。[[server/02_Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference.pdf#page=9|PDF p.9]] [[server/02_Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference.pdf#page=10|PDF p.10]]
- 50modules×12lanes=600memory lanes，另128fabric transceivers；容量0.8–3.2TB/XPU，Weaver1目标7.5TB/s；Weaver2 11.5TB/s为目标值。[[server/02_Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference.pdf#page=5|PDF p.5]] [[server/02_Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference.pdf#page=11|PDF p.11]]
- 115×150×40mm模块，48V输入、1650W预算；2OU 16–18modules约30kW，其中每module分800W XPU+850W memory。**去掉HBM不等于低功耗**。[[server/02_Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference.pdf#page=12|PDF p.12]] [[server/02_Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference.pdf#page=18|PDF p.18]]

## 指标与条件
p.8对比的是不同封装/系统边界的容量、带宽和bounding area：Weaver方案3.2TB/7.5TB/s/138cm²等为设计对比，不能直接推导tokens/s或成本优势。p.5/p.7同行产品曲线混合已发表数据、第三方来源及2027早期HBM4E假设；本库不据此复述未来产品性能为事实。[[server/02_Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference.pdf#page=8|PDF p.8]] [[server/02_Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference.pdf#page=5|PDF p.5]] [[server/02_Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference.pdf#page=7|PDF p.7]]

p.15 routability study：600diff pairs从33mm die edge引出，26µm trace、breakout15µm、最差routing loss7.5dB。原页channel budget“~25dB?”带问号；不能写成已验证SI margin。[[server/02_Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference.pdf#page=15|PDF p.15]]

p.17 CFD边界2LPM总流量，按0.4LPM/kW经验估算探索至约5kW热负载，但热源耦合和低流量动态仍列为next actions。**不是完成5kW热验证**。[[server/02_Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference.pdf#page=17|PDF p.17]]

## 图表与架构
已核对module/block diagram、package装配、routing、cold-plate与2OU概念图。单/两相混合冷板先经DIMM区再到XPU沸腾区，压力策略是抑制back-pressure/flow reversal；p.16真空/沸点描述为设计方案，尚需完整热流耦合和实际测试。[[server/02_Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference.pdf#page=16|PDF p.16]]

## 关联与比较
[[knowledge/concepts/compute-memory-chiplet-link-efficiency|Chiplet链路有效带宽]]：600lane raw bandwidth仍需扣协议/流量利用率；[[knowledge/concepts/compute-memory-kv-placement|KV placement]]：此方案偏“直接高容量内存层”，与外部KV tier/PNM是不同系统取舍。

## 不确定性与待验证
待验证silicon/connector availability、channel BER、module serviceability及实际良率、memory-controller数量与调度、全工作集有效带宽、功率/冷却成本、真实LLM serving性能。p.14的“no module assembly yield loss”是可插拔架构主张，不能当实测良率100%。


## 原始页码导航
[[server/02_Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference.pdf#page=2|p.2]] · [[server/02_Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference.pdf#page=3|p.3]] · [[server/02_Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference.pdf#page=5|p.5]] · [[server/02_Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference.pdf#page=7|p.7]] · [[server/02_Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference.pdf#page=8|p.8]] · [[server/02_Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference.pdf#page=9|p.9]] · [[server/02_Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference.pdf#page=10|p.10]] · [[server/02_Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference.pdf#page=11|p.11]] · [[server/02_Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference.pdf#page=12|p.12]] · [[server/02_Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference.pdf#page=13|p.13]] · [[server/02_Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference.pdf#page=14|p.14]] · [[server/02_Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference.pdf#page=15|p.15]] · [[server/02_Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference.pdf#page=16|p.16]] · [[server/02_Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference.pdf#page=17|p.17]] · [[server/02_Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference.pdf#page=18|p.18]] · [[server/02_Breaking the Memory Capacity-Bandwidth Tradeoff for Agentic Inference.pdf#page=19|p.19]]
