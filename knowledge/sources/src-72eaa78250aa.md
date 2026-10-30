---
id: "src-72eaa78250aa"
type: "source"
title: "Agile Silicon: Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows"
aliases: ["Agile Silicon: Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows"]
speakers: "Patricia Gonzalez-Guerrero — Lawrence Berkeley National Laboratory, on behalf of chiplets modularity for AI/HPC workstream"
source_path: "Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf"
source_git_blob_sha: "2f96d88eda726aa31a08221c2c58ca64e5f4074a"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 31
review_status: "analyzed-visual"
text_reviewed: true
key_pages_visual_checked: [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 26, 29, 30]
evidence_pages: [5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 26, 27, 28, 31]
tags: ["ocp2026", "source", "compute-memory"]
concepts: ["[[knowledge/concepts/compute-memory-federated-model-contract]]", "[[knowledge/concepts/compute-memory-chiplet-link-efficiency]]"]
---

# Agile Silicon: Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows

## 核心结论
演讲提出“profile算法→选择macroarchitecture→定chiplet参数→组合micro/macroarchitecture”的专用化流程。重点不是先选chiplet再找业务，而是 **数据流、内存需求、D2D成本和封装约束共同确定切分**。其主要硬件设计为假设/研究模型，不能当作已出货LLM加速器。

## 关键证据
- 专用化可能降低通用处理开销，但overspecialization与算法变化快于硬件是明确风险；100–1000×是潜力表述，不是本文所有工作负载实测。[[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=9|PDF p.9]]
- profiling示例中不同CNN/语音/LLM对array size响应不同；LLM图明确为hypothetical systolic array。p.15/16另有GenomeOcean GPU profiling，embedding与generation吞吐显著不同，但缺完整GPU/批量配置，不可横比为架构加速。[[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=12|PDF p.12]] [[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=13|PDF p.13]] [[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=14|PDF p.14]] [[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=15|PDF p.15]] [[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=16|PDF p.16]]
- 将systolic compute、SRAM scratchpad、accumulator分成可组合chiplets；NiP用packet-switched二维grid、message queues、无cache coherence，利用规则可预测dataflow。[[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=17|PDF p.17]] [[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=18|PDF p.18]]
- chiplet尺寸4×4mm，sub20nm@1GHz假设64×64PE/1MB scratchpad/64acc；sub10nm@1GHz或sub5nm@2GHz假设128×128PE/9MB/128acc。这些是参数化设计点，不是技术节点的普适面积定律。[[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=19|PDF p.19]]
- pitch20µm与>40µm标准接口假设改变可用lane数；更高频率/序列化会增加power/latency。面积预算须包含logic+NiP+D2D，而非只算MAC。[[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=20|PDF p.20]]

## 指标与条件
p.21–25分步展示同一组CNN/DeepSpeech/Transformer组合表，不能当五次独立实验。例sub20nm transformer用64array chiplets、20scratchpad、8accumulator、8embedding、10×10grid、64×64mm interposer；带宽1TB/s/chiplet是设计参数。[[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=21|PDF p.21]]

p.26是normalized latency/energy对比，能量改善并非所有node/workload都单调；baseline定义、模型校准和数值表缺失，不摘“最高数百倍”做可靠性能承诺。图中不同类别自身归一化基线也不同。[[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=26|PDF p.26]]

## 图表与架构
已视觉核对profiling、NiP、参数表与评估图；p.29/30为外部新闻/政策动机截图，不提供新微架构数据。p.27/28/31提醒bond pitch与工艺快速变化，标准要保留演进空间。

## 关联与比较
[[knowledge/concepts/compute-memory-federated-model-contract|多保真模型契约]] 承载不同假设节点；[[knowledge/concepts/compute-memory-chiplet-link-efficiency|互连效率]] 补齐message-passing的数据移动成本。对架构DSL/IR的启示：表达dataflow与资源映射，再评估chiplet边界，而非把图中每个算子都机械拆成die。

## 不确定性与待验证
真实良率/成本、NiP拥塞、多播/同步、片间带宽有效率、内存层级、可重构性与模型迭代后的迁移成本尚未量化。无服务级TTFT/TPOT/p99结果。


## 原始页码导航
[[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=5|p.5]] · [[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=7|p.7]] · [[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=8|p.8]] · [[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=9|p.9]] · [[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=10|p.10]] · [[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=11|p.11]] · [[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=12|p.12]] · [[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=13|p.13]] · [[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=14|p.14]] · [[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=15|p.15]] · [[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=16|p.16]] · [[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=17|p.17]] · [[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=18|p.18]] · [[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=19|p.19]] · [[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=20|p.20]] · [[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=21|p.21]] · [[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=26|p.26]] · [[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=27|p.27]] · [[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=28|p.28]] · [[Server：Open Chiplet Economy/Agile Silicon-Will Open Chiplet Architectures Keep Pace with Fast-Evolving AI Dataflows.pdf#page=31|p.31]]
