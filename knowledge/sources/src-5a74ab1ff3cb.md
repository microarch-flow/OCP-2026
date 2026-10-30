---
id: "src-5a74ab1ff3cb"
type: "source"
title: "Towards an Extensible Framework for Near Data Processing in AI: Integration Experiences with oneAPI, OpenXLA, and PyTorch"
aliases: ["Towards an Extensible Framework for Near Data Processing in AI: Integration Experiences with oneAPI, OpenXLA, and PyTorch"]
speakers: "Wonjae Lee；Vishnu Charan Thummala；Somnath Roy（Samsung Electronics）"
source_path: "fti-workshop-data-centric-computing/Towards-an-Extensible-Framework-for-Near-Data-Processing-in-AI-Integration-Experiences-with-oneAPI-OpenXLA-and-PyTorch.pdf"
source_git_blob_sha: "8cb62774b32a64fa2519c7746b051d0597c1b148"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 16
review_status: "analyzed-visual"
text_reviewed: true
key_pages_visual_checked: [2, 3, 7, 8, 9, 11, 12, 13, 14]
evidence_pages: [2, 3, 4, 7, 8, 9, 11, 12, 13, 14]
tags: ["ocp2026", "source", "compute-memory"]
concepts: ["[[knowledge/concepts/compute-memory-ndp-contract]]", "[[knowledge/concepts/compute-memory-partitioning-placement-ir]]"]
---

# Towards an Extensible Framework for Near Data Processing in AI: Integration Experiences with oneAPI, OpenXLA, and PyTorch

## 核心结论
“接通 backend”与“高效异构执行”是两件事。oneAPI Level Zero、OpenXLA PJRT、PyTorch backend 暴露不同契约层；Samsung 的 PoC 证明一些路径能跑通，但 GPU+NDP 的分区、放置、同步和动态形状仍是主要工作。[[fti-workshop-data-centric-computing/Towards-an-Extensible-Framework-for-Near-Data-Processing-in-AI-Integration-Experiences-with-oneAPI-OpenXLA-and-PyTorch.pdf#page=2|PDF p.2]] [[fti-workshop-data-centric-computing/Towards-an-Extensible-Framework-for-Near-Data-Processing-in-AI-Integration-Experiences-with-oneAPI-OpenXLA-and-PyTorch.pdf#page=9|PDF p.9]]

## 关键证据
|接入路径|已做/暴露的边界|限制|
|---|---|---|
|PyTorch XPU→oneDNN→SYCL/UR→Level Zero→NDC|在 Arm CXL NDP 上运行预编译 kernels；为兼容 PoC 模拟 Intel GPU properties|该路径的枚举和编译假设偏 Intel GPU；SPIR-V→Arm 编译尚缺，不能称通用透明 oneAPI 支持。[[fti-workshop-data-centric-computing/Towards-an-Extensible-Framework-for-Near-Data-Processing-in-AI-Integration-Experiences-with-oneAPI-OpenXLA-and-PyTorch.pdf#page=3\|PDF p.3]] [[fti-workshop-data-centric-computing/Towards-an-Extensible-Framework-for-Near-Data-Processing-in-AI-Integration-Experiences-with-oneAPI-OpenXLA-and-PyTorch.pdf#page=4\|PDF p.4]]|
|PyTorch/XLA→HLO→PJRT plugin→NDC|映射 device、buffer/memory space、executable、execute/event，验证端到端执行|只卸载部分图需要跨设备 MPMD 编排，本文评估路径尚不成熟；locality 决定实际收益。[[fti-workshop-data-centric-computing/Towards-an-Extensible-Framework-for-Near-Data-Processing-in-AI-Integration-Experiences-with-oneAPI-OpenXLA-and-PyTorch.pdf#page=7\|PDF p.7]] [[fti-workshop-data-centric-computing/Towards-an-Extensible-Framework-for-Near-Data-Processing-in-AI-Integration-Experiences-with-oneAPI-OpenXLA-and-PyTorch.pdf#page=8\|PDF p.8]] [[fti-workshop-data-centric-computing/Towards-an-Extensible-Framework-for-Near-Data-Processing-in-AI-Integration-Experiences-with-oneAPI-OpenXLA-and-PyTorch.pdf#page=9\|PDF p.9]]|
|SPEL native PyTorch 扩展|eager、advertised op offload/CPU fallback、profiler、lazy tensor storage、sharding hints|graph mode 标 WIP；新 API/参数和后端维护不能忽略。[[fti-workshop-data-centric-computing/Towards-an-Extensible-Framework-for-Near-Data-Processing-in-AI-Integration-Experiences-with-oneAPI-OpenXLA-and-PyTorch.pdf#page=12\|PDF p.12]] [[fti-workshop-data-centric-computing/Towards-an-Extensible-Framework-for-Near-Data-Processing-in-AI-Integration-Experiences-with-oneAPI-OpenXLA-and-PyTorch.pdf#page=13\|PDF p.13]]|

## 指标与条件
p.14 截图展示 **Qwen3-0.6B** 在 SPEL+NDC/CMMDC 上产生输出与 profiler；它证明一次功能路径，不是吞吐/功耗对比，也不是大模型服务 SLA。没有可据此推算的 p99、tok/s 或端到端 speedup。[[fti-workshop-data-centric-computing/Towards-an-Extensible-Framework-for-Near-Data-Processing-in-AI-Integration-Experiences-with-oneAPI-OpenXLA-and-PyTorch.pdf#page=14|PDF p.14]]

## 图表与架构
p.8 将 compile/control flow 与 data-memory flow 分开，强调矩阵等大对象要驻留 NDC 可访问内存。p.12 中 chHBM/CMMDC/future device 的 connector/runtime/compiler 各自存在，统一前端不意味着统一机器执行能力。[[fti-workshop-data-centric-computing/Towards-an-Extensible-Framework-for-Near-Data-Processing-in-AI-Integration-Experiences-with-oneAPI-OpenXLA-and-PyTorch.pdf#page=8|PDF p.8]] [[fti-workshop-data-centric-computing/Towards-an-Extensible-Framework-for-Near-Data-Processing-in-AI-Integration-Experiences-with-oneAPI-OpenXLA-and-PyTorch.pdf#page=12|PDF p.12]]

## 关联与比较
[[knowledge/concepts/compute-memory-ndp-contract|近数据卸载契约]] 与 [[knowledge/concepts/compute-memory-partitioning-placement-ir|分区与放置 IR]]：适合把语义图、placement、executable、events、memory ownership 分开表达。lazy allocation 应由图/访问计划支撑，不是无限延迟所有分配。

## 不确定性与待验证
关于动态 shape、DTensor、OpenXLA 的不足是演讲时该团队评估路径的经验，不能当所有版本/实现的永久结论。SPEL 的“end of OCP open source”是发布承诺，本文未额外验证。需补 eager/graph parity、fallback 数据复制、alias/view/mutation、numerical drift、错误传播和混合设备的性能测试。

## 原始页码导航
[[fti-workshop-data-centric-computing/Towards-an-Extensible-Framework-for-Near-Data-Processing-in-AI-Integration-Experiences-with-oneAPI-OpenXLA-and-PyTorch.pdf#page=2|p.2]] · [[fti-workshop-data-centric-computing/Towards-an-Extensible-Framework-for-Near-Data-Processing-in-AI-Integration-Experiences-with-oneAPI-OpenXLA-and-PyTorch.pdf#page=3|p.3]] · [[fti-workshop-data-centric-computing/Towards-an-Extensible-Framework-for-Near-Data-Processing-in-AI-Integration-Experiences-with-oneAPI-OpenXLA-and-PyTorch.pdf#page=4|p.4]] · [[fti-workshop-data-centric-computing/Towards-an-Extensible-Framework-for-Near-Data-Processing-in-AI-Integration-Experiences-with-oneAPI-OpenXLA-and-PyTorch.pdf#page=7|p.7]] · [[fti-workshop-data-centric-computing/Towards-an-Extensible-Framework-for-Near-Data-Processing-in-AI-Integration-Experiences-with-oneAPI-OpenXLA-and-PyTorch.pdf#page=8|p.8]] · [[fti-workshop-data-centric-computing/Towards-an-Extensible-Framework-for-Near-Data-Processing-in-AI-Integration-Experiences-with-oneAPI-OpenXLA-and-PyTorch.pdf#page=9|p.9]] · [[fti-workshop-data-centric-computing/Towards-an-Extensible-Framework-for-Near-Data-Processing-in-AI-Integration-Experiences-with-oneAPI-OpenXLA-and-PyTorch.pdf#page=11|p.11]] · [[fti-workshop-data-centric-computing/Towards-an-Extensible-Framework-for-Near-Data-Processing-in-AI-Integration-Experiences-with-oneAPI-OpenXLA-and-PyTorch.pdf#page=12|p.12]] · [[fti-workshop-data-centric-computing/Towards-an-Extensible-Framework-for-Near-Data-Processing-in-AI-Integration-Experiences-with-oneAPI-OpenXLA-and-PyTorch.pdf#page=13|p.13]] · [[fti-workshop-data-centric-computing/Towards-an-Extensible-Framework-for-Near-Data-Processing-in-AI-Integration-Experiences-with-oneAPI-OpenXLA-and-PyTorch.pdf#page=14|p.14]]
