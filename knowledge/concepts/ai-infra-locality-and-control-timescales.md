---
type: "concept"
title: "局部性与控制时间尺度：把关键路径放在正确的位置"
tags: ["ai-infra", "inference-architecture"]
---

# 局部性与控制时间尺度：把关键路径放在正确的位置

## 跨源综合判断
AI 基础设施反复出现同一模式：慢环设策略/边界，快环在资源附近执行；远端共享增加弹性，却不能抹去传播、排队、端点及状态搬移成本。以下是跨领域架构类比，不代表实验结果可互换。

## 三组可核查证据
1. **推理状态**：Samsung2030 vision把compute+active state留短电路径，跨域由photonic fabric连接，要求每token path的locality contract。[[knowledge/sources/src-0a4e23d127ff]]，[[fts-keynotes-awards/Inference-Data-Center-2030-Memory-Pod-Fabric-with-Rightsized-Compute-presented-by-Samsung.pdf#page=4|PDF p.4]]；Distributed Inference Profile要求先测最小单元，KV搬移按volume/usable BW/contention验证。[[knowledge/sources/src-e3d51d9c0fe6]]，[[ai-clusters/Scaling Purpose-Built AI Models via OCP Aligned Distributed Inference Fabrics.pdf#page=4|PDF p.4]] [[ai-clusters/Scaling Purpose-Built AI Models via OCP Aligned Distributed Inference Fabrics.pdf#page=10|PDF p.10]]
2. **无线控制**：Au-RU慢环约400ms到pin；局部decision56µs，但完整stimulus→carrier HIGH29ms。把decision放本地确实缩短决策链，不等于执行器完整响应也是56µs。[[knowledge/sources/src-cb52a46e9263]]，[[ai-computing-continuum/07_The Autonomous AI-RU Closing the RIC intelligence gap to the radio thr.pdf#page=5|PDF p.5]] [[ai-computing-continuum/07_The Autonomous AI-RU Closing the RIC intelligence gap to the radio thr.pdf#page=6|PDF p.6]]
3. **功率控制**：chip/rack CBU、row/sidecar storage、facility BESS分别覆盖快瞬态、bridging/peak shaving、长backup/grid support，共bus须控制协调。[[knowledge/sources/src-bb504cebac57]]，[[ai-open-data-center/Hardware Mitigations for AI-ML Workloads Power Fluctuation.pdf#page=6|PDF p.6]] [[ai-open-data-center/Hardware Mitigations for AI-ML Workloads Power Fluctuation.pdf#page=7|PDF p.7]] [[ai-open-data-center/Hardware Mitigations for AI-ML Workloads Power Fluctuation.pdf#page=8|PDF p.8]]

## 云控制平面不应吞掉快速控制环
[[knowledge/sources/src-e3d51d9c0fe6]]明确快速congestion control保留在NIC/switch/transport，controller负责intent与topology/health。[[ai-clusters/Scaling Purpose-Built AI Models via OCP Aligned Distributed Inference Fabrics.pdf#page=11|PDF p.11]] [[knowledge/sources/src-4778c6a11dec]]要求IT/OT交换，但未给稳定性/安全证明；其p.9静态PDF图没有可读有效曲线，不可量化控制改善。[[ai-open-data-center/07_Open Systems for AI Why Open Communities Are Essential for the Next Er.pdf#page=9|PDF p.9]] [[ai-open-data-center/07_Open Systems for AI Why Open Communities Are Essential for the Next Er.pdf#page=10|PDF p.10]]

## 对推理加速器架构的应用（推论）
逐条token path列出必须本地的active weights/KV、中层context、远端durable/recovery状态；给每次迁移明确字节量、时延预算、失效fallback。分别记录微秒级memory/transport环、毫秒级服务scheduler环、秒级设施控制环，避免平均数掩盖关键路径。

## 适用边界与证据不足
Samsung2030为愿景；RAN为KPI replay+硬件prototype；energy storage为设计方向。三者不共同证明某套系统已达到p99、节能或TCO目标。下一步用真实模型负载/实际radio或储能器件验证，不能跨域照搬数字。
