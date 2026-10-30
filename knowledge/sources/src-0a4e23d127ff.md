---
id: "src-0a4e23d127ff"
type: "source"
title: "Inference-Data-Center-2030-Memory-Pod-Fabric-with-Rightsized-Compute-presented-by-Samsung"
source_path: "fts-keynotes-awards/Inference-Data-Center-2030-Memory-Pod-Fabric-with-Rightsized-Compute-presented-by-Samsung.pdf"
source_git_blob_sha: "e750fdd0756228d7fda3d5507c4ee60108ed937b"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 7
review_status: "analyzed-visual"
evidence_pages: [2, 3, 4, 5]
tags: ["ai-infra", "fts-keynotes-awards"]
text_reviewed: "all-extractable-pages"
key_pages_visual_checked: [3, 4]
concepts: ["[[knowledge/concepts/ai-infra-locality-and-control-timescales]]"]
---

# Inference-Data-Center-2030-Memory-Pod-Fabric-with-Rightsized-Compute-presented-by-Samsung

## 核心结论
Samsung 的“2030 Inference Data Center”主张由 memory fabric 与数据/状态局部性出发，再 right-size compute。它是2030愿景，不是现有全局统一低延迟内存产品；最实用的建议是为每条 token path 定义 locality contract 和 placement instrumentation。[[fts-keynotes-awards/Inference-Data-Center-2030-Memory-Pod-Fabric-with-Rightsized-Compute-presented-by-Samsung.pdf#page=2|PDF p.2]] [[fts-keynotes-awards/Inference-Data-Center-2030-Memory-Pod-Fabric-with-Rightsized-Compute-presented-by-Samsung.pdf#page=4|PDF p.4]]

## 关键证据
光互连 memory pods 混合3D DRAM、SOCAMM、HBM5、HBM-over-optical并按 workload接GPU/NPU/ASIC等compute。[[fts-keynotes-awards/Inference-Data-Center-2030-Memory-Pod-Fabric-with-Rightsized-Compute-presented-by-Samsung.pdf#page=3|PDF p.3]] 参考域分compute+active state、context memory、shared/recovery；decode/prefill/MoE/in-network/recovery计算域按状态层级连接。[[fts-keynotes-awards/Inference-Data-Center-2030-Memory-Pod-Fabric-with-Rightsized-Compute-presented-by-Samsung.pdf#page=4|PDF p.4]]

## 指标与条件
p.4 内存层表混合 MB到TB、ns到ms的量级，L0.5/L1.5 latency仍TBD；这些不是同平台benchmark。图中Exabyte→Zettabyte是vision规模，不是可购买容量。不能把“光fabric”理解为任意远端内存拥有HBM访问延迟。[[fts-keynotes-awards/Inference-Data-Center-2030-Memory-Pod-Fabric-with-Rightsized-Compute-presented-by-Samsung.pdf#page=3|PDF p.3]] [[fts-keynotes-awards/Inference-Data-Center-2030-Memory-Pod-Fabric-with-Rightsized-Compute-presented-by-Samsung.pdf#page=4|PDF p.4]]

## 图表与架构
已看p.3–4。图特意标compute↔active state的short electrical path与跨域photonic path并存，不能据“memory-centric”删去近端HBM。图表把当前与未来tiers混排，未给每层产品/工艺/投产时间。

## 关联与比较
[[knowledge/concepts/ai-infra-locality-and-control-timescales]]；[[knowledge/concepts/ai-infra-inference-serving-shapes]]。与分离推理材料共同强调：分解不是目的，token关键路径的状态局部性与可测成本才是约束。

## 不确定性与待验证
无模型/精度/并发、KV residency、miss rate、remote access tail、memory consistency、failure recovery、成本/能效或实测良率。需把愿景分解为可验证pod边界/访问模式，不可用于当前采购性能排名。合作论坛/benchmark/reference solutions仍为开放创新倡议。[[fts-keynotes-awards/Inference-Data-Center-2030-Memory-Pod-Fabric-with-Rightsized-Compute-presented-by-Samsung.pdf#page=5|PDF p.5]]
