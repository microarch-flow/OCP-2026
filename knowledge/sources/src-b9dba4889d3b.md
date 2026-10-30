---
id: "src-b9dba4889d3b"
type: "source"
title: "Cornelis Active Compute Fabric：把在售CN5000与CN7000目标分开"
source_path: "expo-hall-sessions/Changing workloads demand Active Compute Fabric presented by Cornelis Networks.pdf"
source_git_blob_sha: "f55196cf7ab498d08be77e0efd824d107575f212"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 13
review_status: "analyzed-visual"
evidence_pages: [2, 3, 4, 5, 8, 9, 10, 11]
text_reviewed: true
key_pages_visual_checked: [3, 11]
tags: ["ocp2026", "expo-hall"]
concepts: ["[[knowledge/concepts/network-inference-acceptance]]"]
---

# Cornelis Active Compute Fabric：把在售CN5000与CN7000目标分开

## 核心结论
作者提出在NIC和交换机嵌入计算核，执行KV搬运、MoE调度、collective及恢复。关键架构思想是让网络理解工作类型；但现有CN5000性能不能证明2027目标CN7000的in-network计算已兑现。[[expo-hall-sessions/Changing workloads demand Active Compute Fabric presented by Cornelis Networks.pdf#page=5|PDF p.5]] [[expo-hall-sessions/Changing workloads demand Active Compute Fabric presented by Cornelis Networks.pdf#page=9|PDF p.9]] [[expo-hall-sessions/Changing workloads demand Active Compute Fabric presented by Cornelis Networks.pdf#page=11|PDF p.11]]

## 关键证据、指标与条件
- CN5000对NDR400G声称最多低32%延迟、2.3倍message rate、2.5倍小消息带宽；测试双路EPYC9755、768GB DDR5-6400、Rocky9.5，CN用OPXS12.1.x/OpenMPI5.0.8，NDR用CX7/Quantum2、2mDAC及不同OpenMPI/UCX/OFED栈。不是只改变网卡的等软件对照。[[expo-hall-sessions/Changing workloads demand Active Compute Fabric presented by Cornelis Networks.pdf#page=2|PDF p.2]] [[expo-hall-sessions/Changing workloads demand Active Compute Fabric presented by Cornelis Networks.pdf#page=3|PDF p.3]]
- 应用柱图按制造/物理生命/气候分类，最高1.8/2.5/1.5倍，但未给各柱任务名、规模及置信度，不能外推LLM吞吐。[[expo-hall-sessions/Changing workloads demand Active Compute Fabric presented by Cornelis Networks.pdf#page=3|PDF p.3]]
- 900+节点Lynx自述91% scaling efficiency（测至900节点）；Stampede3 WRF+71%来自4–26节点、相对OPA100而非NDR；德国500+服务器明确nearing production，三个案例成熟度不同。[[expo-hall-sessions/Changing workloads demand Active Compute Fabric presented by Cornelis Networks.pdf#page=4|PDF p.4]]
- 路线：CN5000 400G/PCIe5 shipping；CN6000 800G/PCIe6 sampling、Q4 2026扩供预期；CN7000 1.6T/PCIe7/576×200G为2027 tape-out目标。CN6000/7000规格可变，不能记为全部量产。[[expo-hall-sessions/Changing workloads demand Active Compute Fabric presented by Cornelis Networks.pdf#page=9|PDF p.9]]
- CN7000目标每交换机96 RV64GCV核(VLEN1024)、48MB SRAM、72×1.6T端口，NIC8vector+16scalar核；100kGPU图称总1.1M核、~1.2TB SRAM、17Pb/s injection，缺NIC/GPU比例与拓扑，不能独立复算规模。[[expo-hall-sessions/Changing workloads demand Active Compute Fabric presented by Cornelis Networks.pdf#page=11|PDF p.11]]

## 图表与架构
已看p3/11。p8将prefill→decode KV传输归为TTFT关键路径是提醒而非恒等式：整体TTFT还含排队、prefill及解码启动，“不是带宽问题”的口号不能消除有限带宽约束。[[expo-hall-sessions/Changing workloads demand Active Compute Fabric presented by Cornelis Networks.pdf#page=8|PDF p.8]]

## 关联与比较
[[knowledge/concepts/network-inference-acceptance]]、[[knowledge/concepts/network-scaleup-ethernet]]：UALink/ESUN、UEC/RoCE/MRC并列支持目标不代表相同内存语义或互通已经验收。[[expo-hall-sessions/Changing workloads demand Active Compute Fabric presented by Cornelis Networks.pdf#page=10|PDF p.10]]

## 不确定性与待验证
需真实KV大小分布、并发、软件offload接口/隔离、交换机计算资源争用、失效回退与p99，以及CN7000样片、工具链及供应状态。所有性能为厂商报告，没有本次独立复现。

