---
type: "concept"
title: "存储是工作负载契约：容量、尾延迟、耐久与故障恢复联合定价"
review_status: "synthesis"
tags: ["ocp", "concept", "platform", "storage"]
sources: ["[[knowledge/sources/src-e67fbded1ca5]]", "[[knowledge/sources/src-2807cd66d1aa]]", "[[knowledge/sources/src-e3d8ea7e9b34]]", "[[knowledge/sources/src-211b41341213]]", "[[knowledge/sources/src-7af780a098ba]]", "[[knowledge/sources/src-d2eace1b7b62]]", "[[knowledge/sources/src-3ac347a35e8c]]", "[[knowledge/sources/src-f07a528e26fb]]", "[[knowledge/sources/src-43a03424124b]]", "[[knowledge/sources/src-3f525f18fc6b]]", "[[knowledge/sources/src-d4ac456fb37b]]"]
updated: "2026-10-30"
---

# 存储是工作负载契约：容量、尾延迟、耐久与故障恢复联合定价

## 定义与边界

**跨源归纳：** “每 TB 更便宜”只有在目标工作负载、可用容量、可达性能、寿命与恢复预算同时成立时才是有效采购比较。原始容量密度、峰值带宽、平均延迟和器件 DWPD 不足以单独确定 AI 存储 TCO。

## 来源与证据

- **HDD 的容量增长暴露共享链路与每 TB 性能约束。** 275 MB/s/盘、8-lane 上行模型中盘数变化会改变 SAS/PCIe 最优选择；这是模型，不是接口越新就任意扩容。[[knowledge/sources/src-e67fbded1ca5|源卡]] · [[storage/Adopting-high-capacity-HDDs-navigating-throughput-and-IOPS-Limits-using-SAS-NVME-interfaces-for-the-AI-Cloud.pdf#page=6|PDF p.6]]
- **QLC 的 DRAM 节省必须按 I/O 粒度比较。** AI 大块轨迹可以容忍更大 IU，但 4K 随机写的模拟偏好小 IU 加部分 LUT 缓存。IU、RU、erase block 是三个不同粒度。[[knowledge/sources/src-2807cd66d1aa|源卡]] · [[storage/High-Capacity-QLC-Innovation.pdf#page=5|PDF p.5]] [[knowledge/sources/src-2807cd66d1aa|源卡]] · [[storage/High-Capacity-QLC-Innovation.pdf#page=10|PDF p.10]]
- **数据放置的收益要扣除保护成本。** 小 RU 的高并发开放数可能增加 SLC cache/OP；Direct Write 改变首遍 QLC 可读性，才可能移除相关保护缓存。并不是“所有 FDP 都好/坏”。[[knowledge/sources/src-211b41341213|源卡]] · [[storage/Increasing-Block-Sizing-Changes-Data-Placement-Economics.pdf#page=4|PDF p.4]] [[knowledge/sources/src-f07a528e26fb|源卡]] · [[storage/QLC-Writes-the-end-of-SLC-caching.pdf#page=9|PDF p.9]]
- **QoS 需要资源成本与超载语义。** Rate limit、WRR、deadline 和按介质时间分权不等价；服务等级目标示例不是实测 SLA。[[knowledge/sources/src-e3d8ea7e9b34|源卡]] · [[storage/IO-Prioritization-for-Optimized-Command-Handling.pdf#page=6|PDF p.6]] [[knowledge/sources/src-e3d8ea7e9b34|源卡]] · [[storage/IO-Prioritization-for-Optimized-Command-Handling.pdf#page=12|PDF p.12]]
- **失效吸收位置改变经济性。** Micron FIP 让设备显式减容，Meta block repair 尽量不整盘退役；节省 spares 的代价是集群恢复与容量重分配责任。[[knowledge/sources/src-7af780a098ba|源卡]] · [[storage/Near-Line-SSD-the-Path-to-the-Future.pdf#page=5|PDF p.5]] [[knowledge/sources/src-3ac347a35e8c|源卡]] · [[storage/QLC-Storage-in-Hyperscalefleet.pdf#page=12|PDF p.12]]
- **稳态测试本身需要正确容量定义。** Sprandom 依赖真实可用于 GC 的 OP，ECC/PI 保留字节不等于可用 OP；原稿换算式还有需核实的符号问题。[[knowledge/sources/src-d2eace1b7b62|源卡]] · [[storage/Optimizing-SSD-Performance-Testing-using-FIO-Sprandom.pdf#page=11|PDF p.11]] [[knowledge/sources/src-d2eace1b7b62|源卡]] · [[storage/Optimizing-SSD-Performance-Testing-using-FIO-Sprandom.pdf#page=12|PDF p.12]]

## KV-cache：收益发生在哪一层？

SK hynix 在明确 vLLM/LMCache/Qwen3/H100 配置下，调优后 SSD microbenchmark TTFT 约为 memory baseline 1.07–1.14×；100% hit 和相等缓存容量是关键条件。其每天可达约 57.5 TB/GPU 的 KV 写入说明容量还必须按耐久定下限。[[knowledge/sources/src-3f525f18fc6b|源卡]] · [[storage/Storage-as-a-Performance-Tier-for-LLM-Serving.pdf#page=7|PDF p.7]] [[knowledge/sources/src-3f525f18fc6b|源卡]] · [[storage/Storage-as-a-Performance-Tier-for-LLM-Serving.pdf#page=9|PDF p.9]] [[knowledge/sources/src-3f525f18fc6b|源卡]] · [[storage/Storage-as-a-Performance-Tier-for-LLM-Serving.pdf#page=11|PDF p.11]]

Samsung 的 FDP 轨迹回放在 PM9D3a、89% utilization、4× capacity writes 下将 WAF 2.600 降至 1.425；脚注明确延迟是 object-I/O completion **不是 serving TTFT**。更大传输另降低 Mcycles/GiB，但不能把这些比例相乘计算 tokens/s。[[knowledge/sources/src-d4ac456fb37b|源卡]] · [[storage/Vertical-Optimizations-for-KV-Infrastructure.pdf#page=6|PDF p.6]] [[knowledge/sources/src-d4ac456fb37b|源卡]] · [[storage/Vertical-Optimizations-for-KV-Infrastructure.pdf#page=7|PDF p.7]]

因此可建立以下测量链（本文方法归纳，非已发布规范）：

`reuse/TTL → working-set + writes/day → cache布局/IU/RU → 有效I/O与WAF → CPU/PCIe/SSD排队 → TTFT/TPOT/tokens/s → 寿命和重建成本`

## 验收与可比性矩阵

| 维度 | 至少固定的条件 | 不应替代它的指标 |
|---|---|---|
| 容量 | raw/user/filled/OP、metadata/cache占用 | 最大 raw TB |
| 性能 | I/O粒度、QD、混合比例、并发、稳态、温度 | burst峰值 GB/s |
| 服务 | 命中率、QPS、TTFT/TPOT p99、超载/恢复 | 平均块I/O延迟 |
| 寿命 | 每日host写、WAF、保修期、有效DWPD | NAND P/E单值 |
| 故障 | die/block/controller/rack范围、重建时间、减容策略 | 仅AFR或更换率 |
| 遥测 | cache fill、GC、WAF、事件与timestamp | 不带上下文的“健康” |

最后一栏遥测仍在推进：Meta明确提出所需cache/GC可见性，遥测演讲的主动健康模型标为WIP，不能把未来可观测性当现有控制闭环。[[knowledge/sources/src-3ac347a35e8c|源卡]] · [[storage/QLC-Storage-in-Hyperscalefleet.pdf#page=16|PDF p.16]] [[knowledge/sources/src-43a03424124b|源卡]] · [[storage/Recent-Advancements-in-OCP-Telemetry-for-SSDs.pdf#page=3|PDF p.3]]

## 未决问题

资料未提供可跨厂商复用的完整端到端 cost/token 模型。后续最有价值的验证是固定同一 serving trace，联合测 p99、有效 tokens/s、J/token、每日host/NAND写、故障恢复和美元成本，再判断增加SSD带宽、容量或DRAM哪项更划算。对故障相关性和利用率变化做敏感性分析，避免把单机上限变成fleet承诺。
