---
type: concept
title: "供电路径与动态约束：不要把峰值效率、静态损耗与可交付算力混为一谈"
tags: [ocp2026, concept, compute-memory]
---

# 供电路径与动态约束：不要把峰值效率、静态损耗与可交付算力混为一谈

## 核心命题
从电网到晶体管的供电是跨时间尺度、跨物理边界的问题。高电压配电、短的低压大电流路径、瞬态控制与散热分别解决不同约束；任何单一效率或瓦数都不足以证明推理系统能持续交付某个 token/s。

## 先划清观测边界
|层级|材料给出的机制/证据|不能据此推出|
|---|---|---|
|电网 / POI|EPC 的并联 grid-forming BESS，报告 <2ms load-compensation loop；有实验室波形。[[fts-ai-hpc/AI-HPC-Lightning-Talks.pdf#page=20\|PDF p.20]] [[fts-ai-hpc/AI-HPC-Lightning-Talks.pdf#page=21\|PDF p.21]]|已在 GW 实际部署验证，或能替代板级快速去耦|
|转换器|Cambridge 54V→0.8V/240A 原型，90.6% **峰值**效率，1.5A/mm²。[[fts-ai-hpc/AI-HPC-Lightning-Talks.pdf#page=35\|PDF p.35]]|240A 满载点也有90.6%，或单模块已经多kA|
|两级VPD系统|AMD 8:1 IBC + 多相VPD；下一代3A/mm²、E2E>80%为目标。[[server/Reimagining-Data-Center-Power-High-Density-Architectures-for-Next-Gen-AI-Compute.pdf#page=3\|PDF p.3]] [[server/Reimagining-Data-Center-Power-High-Density-Architectures-for-Next-Gen-AI-Compute.pdf#page=8\|PDF p.8]]|可直接拿目标E2E与另一原型peak作胜负判定|
|供回电连接器|优化回流路径的 Ansys Q3D 模拟：8.5nH基线降至约0.545nH（>20MHz）。[[server/08_Reducing Parasitics, Improving Performance The Case for Low Inductance.pdf#page=6\|PDF p.6]] [[server/08_Reducing Parasitics, Improving Performance The Case for Low Inductance.pdf#page=8\|PDF p.8]]|整块PDN电感下降94%，或DC接触电阻等于100MHz AC resistance|
|板级电热|方向相关effective-k及实测校准，简化模型降低求解成本。[[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=11\|PDF p.11]] [[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=20\|PDF p.20]]|热导率可各向同性化，或两模型接近就等于对实测准确|
|焊点可靠性|Cu sintering daisy-chain在50A/mm²测试中>900h稳定，SAC305约300h出现开路。[[fts-ai-hpc/Copper-Sintering-BGA-Interconnect-for-Mitigating-Electromigration-in-High-Current-AI-Power-Delivery.pdf#page=5\|PDF p.5]]|寿命恰好3倍；>900h是未失效的右删失观察，不是确切失效时刻|

## 物理记账与归因
在固定功率、电阻、电容的**解析比较**中，`I=P/V`、`P_loss=I²R`、`E_C=CV²/2`。从6V提升到48V意味着电流1/8、该段导体损耗1/64、同C储能64倍；这不是整机效率提高64倍。[[fts-ai-hpc/AI-HPC-Lightning-Talks.pdf#page=28|PDF p.28]]

对架构探索，可把限制分成：
1. **稳态**：转换效率曲线、路径电阻、持续散热、最大电流与温升。
2. **动态**：负载步进幅度/斜率、控制回路、有效电感、电容、droop与恢复时间。
3. **可靠性**：热循环、机械应力、接触老化、故障隔离、可观测性。
4. **工作负载耦合**：训练/推理的功率时间序列和调度行为；峰值TDP不能代替时间序列。

这些是本库建模建议，不是材料给出的统一标准。若要声称改善服务p99，必须测节流/错误恢复与请求尾延迟；所列演讲没有建立这条端到端证据链。

## 三个容易误读的图表
- MOSFET effective-k 对实测偏差12/13/15/14%，2R为8/8/11/10%；“4–5”是**误差百分点差**，不是effective-k对实测只差4–5%。[[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=16|PDF p.16]]
- 该演讲实际流程是初始PI→thermal收敛→更新温度后的最终PI；流程图结束于此，不应自动描述成联合求解反复收敛。[[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=19|PDF p.19]]
- p.15“series”文字与算术加权公式矛盾；应保留冲突，不把命名错误固化到模型库。[[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=15|PDF p.15]]

## 模型接口的最小条件（本库建议）
记录输入/输出端口、效率测量边界、V/I/温度、频率/瞬态波形、几何与材料方向、冷却边界、样本数、误差/删失状态。共享的不能只有“峰值功耗”；至少应交换空间损耗分布和时间负载包络。

## 关联
[[knowledge/concepts/compute-memory-federated-model-contract|跨域模型契约]] · [[knowledge/concepts/compute-memory-package-memory-wall|封装与内存墙]] · [[knowledge/concepts/compute-memory-modular-platform-contract|模块化平台契约]]
