---
id: "src-137efda9bf69"
type: "source"
title: "01_Scaling Photonic Quantum Computers"
source_path: "fts-quantum-data-center-design/01_Scaling Photonic Quantum Computers.pdf"
source_git_blob_sha: "318b2262611aa22c9b11fae08740446d034c047f"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 16
review_status: "analyzed-visual"
evidence_pages: [2, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15]
tags: ["ai-infra", "fts-quantum-data-center-design"]
text_reviewed: "all-extractable-pages"
key_pages_visual_checked: [6, 15]
concepts: ["[[knowledge/concepts/ai-infra-quantum-classical-boundary]]"]
---

# 01_Scaling Photonic Quantum Computers

## 核心结论
Xanadu 的光子量子路线把通用容错系统设想为网络化模块的数据中心，而非单box；即使量子计算光学部分不需要冷却，控制服务器、FPGA、探测器与同步仍是大规模经典基础设施问题。后半为结合文件规模描述的解读，不推断所有探测器免制冷。[[fts-quantum-data-center-design/01_Scaling Photonic Quantum Computers.pdf#page=4|PDF p.4]] [[fts-quantum-data-center-design/01_Scaling Photonic Quantum Computers.pdf#page=13|PDF p.13]] [[fts-quantum-data-center-design/01_Scaling Photonic Quantum Computers.pdf#page=14|PDF p.14]]

## 关键证据
Aurora为full-architecture prototype，含qubit generation、entanglement、homodyne gates与实时feed-forward；作者称35 PIC、3substrates、12 **physical** qubits、86billion modes及real-time error correction decoding。物理qubit/mode数不能换算logical qubit。[[fts-quantum-data-center-design/01_Scaling Photonic Quantum Computers.pdf#page=6|PDF p.6]] [[fts-quantum-data-center-design/01_Scaling Photonic Quantum Computers.pdf#page=7|PDF p.7]] [[fts-quantum-data-center-design/01_Scaling Photonic Quantum Computers.pdf#page=8|PDF p.8]] [[fts-quantum-data-center-design/01_Scaling Photonic Quantum Computers.pdf#page=9|PDF p.9]] [[fts-quantum-data-center-design/01_Scaling Photonic Quantum Computers.pdf#page=10|PDF p.10]] [[fts-quantum-data-center-design/01_Scaling Photonic Quantum Computers.pdf#page=11|PDF p.11]]

## 指标与条件
- 30×loss reduction、100×hardware-overhead reduction是作者宣称，PDF未说明比较基线/误差条/如何测量，不据此推算计算加速比或成本。[[fts-quantum-data-center-design/01_Scaling Photonic Quantum Computers.pdf#page=6|PDF p.6]]
- p.15路线：2029 up to200 logical qubits、2030 up to500、2031 1000+；fault-tolerance目标2028–2029、QDC operational2029–2030。均为目标，非已达成。表中Loss24.1→1.0未在该页明确单位，不擅自写dB或%。[[fts-quantum-data-center-design/01_Scaling Photonic Quantum Computers.pdf#page=15|PDF p.15]]

## 图表与架构
已看p.6原型照片/说明与p.15 roadmap，确认logical指标从2029列起而非2026；避免提取文字丢列导致年份错配。

## 关联与比较
[[knowledge/concepts/ai-infra-quantum-classical-boundary]]。对推理加速器架构的直接价值是研究模块化、反馈、同步、制造与classic control scaling，而非量子即将替代LLM inference。

## 不确定性与待验证
多页明确research/prototype preliminary、ongoing validation、未必代表future commercial performance。[[fts-quantum-data-center-design/01_Scaling Photonic Quantum Computers.pdf#page=2|PDF p.2]] 缺logical gate性能/纠错后吞吐、功率、控制延迟、系统成本与业务utility；本次未查引述Nature论文，世界首创等表述只保留为作者claim。[[fts-quantum-data-center-design/01_Scaling Photonic Quantum Computers.pdf#page=5|PDF p.5]]
