---
id: "src-86e4ca03d02c"
type: "source"
title: "Intel Agentic Rack：CPU关键路径、AMX与内存扩展的证据边界"
source_path: "expo-hall-sessions/01_Agentic AI The Agentic Rack, Powered by Intel Xeon Processors presente.pdf"
source_git_blob_sha: "ce305d985c362c342aca02bf19d8a1fcb6c6e5b7"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 15
review_status: "analyzed-visual"
evidence_pages: [2, 3, 5, 6, 7, 8, 9, 11, 12, 13]
text_reviewed: true
key_pages_visual_checked: [2, 8, 12]
tags: ["ocp2026", "expo-hall"]
concepts: ["[[knowledge/concepts/expo-evidence-to-deployment]]"]
---

# Intel Agentic Rack：CPU关键路径、AMX与内存扩展的证据边界

## 核心结论
方案把agent任务拆为模型、编排、工具执行、数据与状态，而非只扩大GPU。P核承担尾延迟敏感控制路径，密集E核处理工具并发，AMX跑路由/护栏/重排小模型，QAT/DSA/IAA负责加密、搬运、压缩；这是合理的资源分工假设，文件没有端到端p99对照。[[expo-hall-sessions/01_Agentic AI The Agentic Rack, Powered by Intel Xeon Processors presente.pdf#page=5|PDF p.5]] [[expo-hall-sessions/01_Agentic AI The Agentic Rack, Powered by Intel Xeon Processors presente.pdf#page=6|PDF p.6]] [[expo-hall-sessions/01_Agentic AI The Agentic Rack, Powered by Intel Xeon Processors presente.pdf#page=9|PDF p.9]]

## 关键证据、指标与条件
- p2编码/客服/科学/RL场景CPU时间82%/78%/70%/80%，脚注明确是**illustrative simulation estimate**，不是生产trace。p3另一组百分比是范围示意，不能当同一实测分布。[[expo-hall-sessions/01_Agentic AI The Agentic Rack, Powered by Intel Xeon Processors presente.pdf#page=2|PDF p.2]] [[expo-hall-sessions/01_Agentic AI The Agentic Rack, Powered by Intel Xeon Processors presente.pdf#page=3|PDF p.3]]
- Flat Memory Mode宣称所引负载达到全DDR5性能97.3%；IAA/zswap节省33%内存且等性能。未给负载、DDR/CXL配比、压缩率分布及p99，完整配置需另索取。[[expo-hall-sessions/01_Agentic AI The Agentic Rack, Powered by Intel Xeon Processors presente.pdf#page=7|PDF p.7]]
- 已看语义router柱图：第五代Xeon EMR、p95=445ms门槛，8/16/32/64核的BF16+AMX会话数32/32/64/64，AMX off为4/8/16/16，FP32为8/16/32/32。宣传“最多4倍”与8核的32/4=8倍不一致；不同精度基线更不能混为AMX单一贡献。32→64核不增会话也提示该实验有另一瓶颈。[[expo-hall-sessions/01_Agentic AI The Agentic Rack, Powered by Intel Xeon Processors presente.pdf#page=8|PDF p.8]]
- 同页另一个Qwen3-Coder-30B-A3B CPU子agent对云Haiku子agent实验声称token成本-25%、墙钟-6.5%、任务结果相同；任务集、调用价格、CPU摊销、网络延迟均未给，不能推出总TCO-25%。[[expo-hall-sessions/01_Agentic AI The Agentic Rack, Powered by Intel Xeon Processors presente.pdf#page=8|PDF p.8]]
- Diamond Rapids被描述为下一代：最多256核、1.28GB LLC、16内存通道、2DPC32DIMM、12800MT/s与1.6TB/s。是规格/路线信息，不是前述EMR测试硬件。[[expo-hall-sessions/01_Agentic AI The Agentic Rack, Powered by Intel Xeon Processors presente.pdf#page=11|PDF p.11]] [[expo-hall-sessions/01_Agentic AI The Agentic Rack, Powered by Intel Xeon Processors presente.pdf#page=12|PDF p.12]]

## 图表与架构
已检查p2/8/12。机架内P/E核部署是一种混合节点架构，不要误读为同一socket同时包含这两种核；p13还区分CPU-only、CPU+GPU、独立CPU rack及prefill/decode分离四类部署。[[expo-hall-sessions/01_Agentic AI The Agentic Rack, Powered by Intel Xeon Processors presente.pdf#page=6|PDF p.6]] [[expo-hall-sessions/01_Agentic AI The Agentic Rack, Powered by Intel Xeon Processors presente.pdf#page=13|PDF p.13]]

## 关联与比较
[[knowledge/concepts/expo-evidence-to-deployment]]：比较时固定每任务成功率和端到端SLO，再看CPU/内存/工具路径；不要将单路由器p95提升外推全部agent回合。

## 不确定性与待验证
须补真实任务分布、模型/上下文、并发策略、软件版本、热稳态功率、p99与内存压力结果。材料中产品及模型名称仅按来源记录，没有外部核验其发布状态。


跨源比较：[[knowledge/comparisons/expo-inference-cost-contract]]。
