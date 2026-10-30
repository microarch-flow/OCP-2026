---
type: "comparison"
title: "量子与经典系统：三种耦合域与四类不能混比的指标"
tags: ["ai-infra", "inference-architecture"]
---

# 量子与经典系统：三种耦合域与四类不能混比的指标

## 比较范围
本页基于7份量子材料，讨论加速器/互连/调度可迁移的系统问题，不预测量子替代LLM推理的日期，不做股票分析。不同qubit modality、code、noise model与application具有不同成本，physical/logical数量不能单独排名。

## 三种经典—量子耦合域
- **T：tight实时**，IQM用≲100µs说明同一timing domain，decoder/feed-forward不能依赖通用batch scheduler；关键是吞吐跟上syndrome、worst-case deadline。[[knowledge/sources/src-292296f6d7fb]] [[fts-quantum-data-center-design/Toward-Quantum-Superconducting-with-IQM-Quantum-Processors.pdf#page=9|PDF p.9]] [[fts-quantum-data-center-design/Toward-Quantum-Superconducting-with-IQM-Quantum-Processors.pdf#page=15|PDF p.15]]
- **M：intermediate共调度**，0.1ms–1s，同一allocation协调QPU、classical resources与calibration；优化对象是session与queue，不是只换NIC。[[fts-quantum-data-center-design/Toward-Quantum-Superconducting-with-IQM-Quantum-Processors.pdf#page=15|PDF p.15]] [[fts-quantum-data-center-design/Toward-Quantum-Superconducting-with-IQM-Quantum-Processors.pdf#page=16|PDF p.16]]
- **L：loose跨机构**，≳1s，重点identity/accounting/data movement与两个queue；连通服务不证明具备实时QEC。[[fts-quantum-data-center-design/Toward-Quantum-Superconducting-with-IQM-Quantum-Processors.pdf#page=15|PDF p.15]] [[fts-quantum-data-center-design/Toward-Quantum-Superconducting-with-IQM-Quantum-Processors.pdf#page=33|PDF p.33]]
Dell的QIO分application(ms)、control(µs)、physical(ns)，与该分层相符；此为跨源结构共识，不代表所有模态共享同一个deadline。[[knowledge/sources/src-b349050d00ce]] [[fts-quantum-data-center-design/The-Classical-Infrastructure-of-Fault-tolerant-Quantum-Computing.pdf#page=5|PDF p.5]]

## 四类指标必须拆开
### 1. 均值 interconnect latency ≠ decoder worst-case SLA
IQM引用Backline CPU2.3µs/GPU4.4µs与NVQLink3.84µs（σ0.035µs,n1000）均为各自配置roundtrip。没有同任务/同负载，不能CPU与GPU排名；均值也不足以保证长期syndrome无积压。[[fts-quantum-data-center-design/Toward-Quantum-Superconducting-with-IQM-Quantum-Processors.pdf#page=32|PDF p.32]]

### 2. 物理/逻辑qubit数量 ≠ 通用容错计算能力
Xanadu Aurora为12physical原型，未来logical roadmap另列；Infleqtion80physical→30logical使用指定编码与有限IQP电路，不能以2.67physical/logical外推任意算法。IQM30physical/logical与8×资源优势来自特定Barbell noise simulations，Halocene首5logical是研究/Clifford目标。[[knowledge/sources/src-137efda9bf69]] [[fts-quantum-data-center-design/01_Scaling Photonic Quantum Computers.pdf#page=6|PDF p.6]] [[fts-quantum-data-center-design/01_Scaling Photonic Quantum Computers.pdf#page=15|PDF p.15]] [[knowledge/sources/src-b1f7ae75bdcf]] [[fts-quantum-data-center-design/Neutral-atoms-for-computing-and-sensing.pdf#page=6|PDF p.6]] [[fts-quantum-data-center-design/Neutral-atoms-for-computing-and-sensing.pdf#page=8|PDF p.8]] [[fts-quantum-data-center-design/Toward-Quantum-Superconducting-with-IQM-Quantum-Processors.pdf#page=25|PDF p.25]] [[fts-quantum-data-center-design/Toward-Quantum-Superconducting-with-IQM-Quantum-Processors.pdf#page=26|PDF p.26]]

### 3. 纠缠attempt rate ≠ 成功rate ≠ 逻辑门吞吐
Nu Quantum的MHz attempt、up-to99.7%支持和300ns control latency属于QNU不同指标；testbed又列>97%fidelity和无绝对baseline的50×rate。QPI与router效率相乘，其简化成功概率再受平方项影响。[[knowledge/sources/src-2515fe19b121]] [[fts-quantum-data-center-design/Quantum-Networking-for-Scale-Out-Nu-Quantum-s-Entanglement-Fabric.pdf#page=8|PDF p.8]] [[fts-quantum-data-center-design/Quantum-Networking-for-Scale-Out-Nu-Quantum-s-Entanglement-Fabric.pdf#page=14|PDF p.14]] [[fts-quantum-data-center-design/Quantum-Networking-for-Scale-Out-Nu-Quantum-s-Entanglement-Fabric.pdf#page=17|PDF p.17]]

### 4. QKD安全网络 ≠ 分布式量子计算网络
Falqon把QKD nodes/key management接到IPSec/OTNSec/MACsec；1419km累计deployment不是单跳量子纠缠链路，更不证明远端QPU可做logical gates。QKD的密钥率/信任假设与QPU network的rate/fidelity需分别验证。[[knowledge/sources/src-0ef33d4f6a12]] [[fts-quantum-data-center-design/From-Quantum-Breakthroughs-to-Data-Center-Ready-Quantum-Secure-Networks.pdf#page=12|PDF p.12]] [[fts-quantum-data-center-design/From-Quantum-Breakthroughs-to-Data-Center-Ready-Quantum-Secure-Networks.pdf#page=13|PDF p.13]] [[fts-quantum-data-center-design/From-Quantum-Breakthroughs-to-Data-Center-Ready-Quantum-Secure-Networks.pdf#page=16|PDF p.16]]

## 商业化与成本边界
IDTechEx的QCRL与2037/2047硬件收入为市场模型而非标准认证。评估实际服务应问：完整workflow时间、classical/HPC资源、校准/冷却、错误预算、availability、运维和成本；不能只数qubits或展示quantum circuit。[[knowledge/sources/src-48d610b26c0e]] [[fts-quantum-data-center-design/Quantum-Computing-Market-in-2026-Trends-Opportunities-and-Challenges.pdf#page=15|PDF p.15]] [[fts-quantum-data-center-design/Quantum-Computing-Market-in-2026-Trends-Opportunities-and-Challenges.pdf#page=17|PDF p.17]]

## 对推理加速器的迁移价值（本知识库推论）
最值得借鉴的是deadline-aware coprocessing、确定性控制path、shared allocation和可追溯calibration；不把高并发吞吐调度系统直接放入硬实时反馈环。见[[knowledge/concepts/ai-infra-locality-and-control-timescales]]、[[knowledge/concepts/ai-infra-scaleup-acceptance]]。
