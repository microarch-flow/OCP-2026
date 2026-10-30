---
type: concept
title: "容量收益与数据路径收益的归因"
tags: [ocp2026, concept, compute-memory]
---

# 容量收益与数据路径收益的归因

## 为什么这是一条独立知识
看到“CXL/P2P/近存系统提高2×、5×、64×”时，先问：**改变的是容量、命中率、复制次数、计算位置、并发，还是物理链路？** 多项同时改变的结果可以证明某个系统方案更好，但不能识别其中单一机制的因果贡献。

## 可追溯实验对照
| 来源与实验 | 基线 → 方案 | 工作负载/指标 | 可以支持的结论 | 不能支持的结论 |
|---|---|---|---|---|
| Astera p.6 | 每vLLM128GB host → 同容量fabric | Qwen3-14B，1–2K prompt；RPS/GPU vs output tok/s/user | 短prompt/等容量性能近似 | P2P必然更快 |
| Astera p.7 | 4×128GB host → 4×256GB fabric | 2–3.5K prompt；图标约2× | 可扩容方案改善吞吐/用户速度曲线 | 纯数据路径提高2× |
| Astera p.8 | 4×128GB host → 4×(256+128)GB混合 | 5–6.5K prompt；图标约3× | 更长prompt下更多容量有利 | 等容量/等成本P2P提高3× |
| Alibaba p.8 | 等成本32GB DRAM → 128GB PCM L2 | Qwen3-8B，30users×30turns，500/500；req/s0.35→0.56；P90 TTFT86.31→44.24s | iso-cost的容量/介质组合收益 | PCM物理访问快于DRAM；P99已改善 |
| Samsung p.8 | RDIMM → RDIMM+CXL pool | LongDocQA/Llama3.1-8B；KV超过RDIMM才出现约5.6×差距 | 避免容量溢出后重算 | 无论working set大小均5.6× |
| Samsung p.11 | static → elastic（均32GB DRAM+1024GB CXL） | normalized P99 TTFT0.8→0.48；goodput2.2→7.1，SLO TTFT≤60s | 相同总pool下重分配约−40%/3.23×（本库计算） | static基线下−52%/7.1×；后者实际对DRAM96GB |
| Marvell p.10 | CPU-load DRAM → StructeraA service | Llama3.1-8B/H200，peak users16；input tok/s80813→139497；mean TTFT2162→1199ms | service/data-path整体相对DRAM约1.73×input throughput | decode输出吞吐4×；p99提升5× |
| PNM p.27 | CPU跨32GB/s链路scan → 10PNM本地scan | FAISS IVF-Flat大向量集；0.23→14.81QPS | 计算移动避免把大输入送过窄链路 | 单PNM核相对CPU核快64× |

直接证据：[[Server：Composable Memory Systems/Cost-Efficient LLM Inference via Peer-to-Peer GPU-to-Memory Expansion Datapath.pdf#page=6|PDF p.6]] · [[Server：Composable Memory Systems/Cost-Efficient LLM Inference via Peer-to-Peer GPU-to-Memory Expansion Datapath.pdf#page=7|PDF p.7]] · [[Server：Composable Memory Systems/Cost-Efficient LLM Inference via Peer-to-Peer GPU-to-Memory Expansion Datapath.pdf#page=8|PDF p.8]] · [[Server：Composable Memory Systems/Beyond DRAM- Byte-Addressable Persistent Memory via Compute Interconnects for AI.pdf#page=8|PDF p.8]] · [[Server：Composable Memory Systems/Disaggregated CXL Memory Architecture for Agentic AI- Dynamic Pooling,  Sharing, and PNM Offloading.pdf#page=8|PDF p.8]] · [[Server：Composable Memory Systems/Disaggregated CXL Memory Architecture for Agentic AI- Dynamic Pooling,  Sharing, and PNM Offloading.pdf#page=11|PDF p.11]] · [[Server：Composable Memory Systems/XPU Scale Composable Smart Memory Fabric.pdf#page=10|PDF p.10]] · [[Server：Composable Memory Systems/Disaggregated CXL Memory Architecture for Agentic AI- Dynamic Pooling,  Sharing, and PNM Offloading.pdf#page=27|PDF p.27]]。

## 共同机制：容量跨过阈值，而不是线性增加速度
[[knowledge/sources/src-7961ff4d5709|Micron模型]] 将effective reuse与S/W关联。更多容量可能从“频繁重算”跨到“工作集驻留”，收益非常大；驻留之后再加容量可能几乎无效。这解释了Astera和Samsung等容量/未溢出区域性能相近、容量不足区域拉开差距的图形。

这只是跨源一致的解释，不是已替所有实验拟合出的因果模型。真实分配策略、warm-up和arrival distribution仍会移动拐点。

## 应当做的四种实验（分析建议）
1. **Iso-capacity**：保持可用KV容量、精度、cache policy相同，只改数据路径。
2. **Iso-cost**：固定全系统预算，不只DIMM价格，比较满足相同SLO的goodput。
3. **Iso-power**：固定设备+host+switch功率边界，比较有效token/J。
4. **Ablation**：固定容量和路径，逐个打开sharing、prefetch、compression、PNM、elastic allocation。

每项同时报告TTFT与TPOT分布、input与output token计数、arrival rate、并发、context/turn分布、cache warm/cold状态、offload bytes和miss/recompute次数。

## 特别容易混淆的指标
- **input tokens/s ≠ output tokens/s**：长文档reuse可大幅提高input吞吐，而decode速度未必同幅改善。
- **mean ≠ P90 ≠ P99**：不同源采用不同统计量，不能横向排序为同一种latency。
- **归一化值≠秒/req/min**：Samsung p.11轴旁虽有单位文字，但柱值明确normalized。
- **goodput≠总吞吐**：超过SLO的请求在goodput中不计入。
- **规格峰值≠有效带宽**；**目标/估算≠测量**；**并行设备数改变≠单设备加速**。

## 阅读路径
先读 [[knowledge/sources/src-7961ff4d5709|容量门控模型]] → [[knowledge/sources/src-f667d06e3a4e|等容量与扩容P2P对照]] → [[knowledge/sources/src-c5ad8983371c|动态分配/共享/PNM]] → [[knowledge/sources/src-cfe218e09035|KV service与DMA]]。再以 [[knowledge/concepts/compute-memory-cxl-failure-domain|故障域]] 补全成本边界。
