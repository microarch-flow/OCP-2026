---
id: "src-e59f410df3c1"
type: "source"
title: "Plug-and-Play ML Pipelines for SONiC: On-Device Intelligence with Advanced Feature Extraction"
source_path: "sonic-workshop/Plug-and-Play-ML-Pipelines-for-SONiC-On-Device-Intelligence-with-Advanced-Feature-Extraction.pdf"
source_git_blob_sha: "ca9a6c9c22146f2ec2cae569bb1cefaa0cff0bf1"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 15
review_status: "analyzed-visual"
evidence_pages: [5, 6, 7, 8, 9, 10, 11, 12]
text_reviewed: true
key_pages_visual_checked: [7, 12]
tags: ["ocp-2026", "networking"]
concepts: ["[[knowledge/concepts/network-clock-evidence]]"]
---

# Plug-and-Play ML Pipelines for SONiC: On-Device Intelligence with Advanced Feature Extraction

## 核心结论
Marvell提议把SONiC已有原始遥测转换为统一feature vector，再按时延/上下文需要分流到on-switch轻模型或off-switch重模型。接口可复用不代表模型准确，也不证明控制动作安全。[[sonic-workshop/Plug-and-Play-ML-Pipelines-for-SONiC-On-Device-Intelligence-with-Advanced-Feature-Extraction.pdf#page=5|PDF p.5]][[sonic-workshop/Plug-and-Play-ML-Pipelines-for-SONiC-On-Device-Intelligence-with-Advanced-Feature-Extraction.pdf#page=7|PDF p.7]][[sonic-workshop/Plug-and-Play-ML-Pipelines-for-SONiC-On-Device-Intelligence-with-Advanced-Feature-Extraction.pdf#page=10|PDF p.10]]

## 关键证据
- 输入包括COUNTERS_DB轮询、IPFIX窗口聚合、sFlow/psample或ACL/ERSPAN镜像；时间/计数window、normalization、rate/ratio等转换由app选择。[[sonic-workshop/Plug-and-Play-ML-Pipelines-for-SONiC-On-Device-Intelligence-with-Advanced-Feature-Extraction.pdf#page=8|PDF p.8]][[sonic-workshop/Plug-and-Play-ML-Pipelines-for-SONiC-On-Device-Intelligence-with-Advanced-Feature-Extraction.pdf#page=9|PDF p.9]]
- 共用event bus、feature接口可接ONNX Runtime/TFLite/自定义engine；NOS adapter不仅读telemetry也应用actions，形成闭环。[[sonic-workshop/Plug-and-Play-ML-Pipelines-for-SONiC-On-Device-Intelligence-with-Advanced-Feature-Extraction.pdf#page=7|PDF p.7]][[sonic-workshop/Plug-and-Play-ML-Pipelines-for-SONiC-On-Device-Intelligence-with-Advanced-Feature-Extraction.pdf#page=11|PDF p.11]]
- 提案强调isolated container、cgroup CPU/memory cap、有界state、warm/fast reboot/config reload生命周期，避免饿死BGP。[[sonic-workshop/Plug-and-Play-ML-Pipelines-for-SONiC-On-Device-Intelligence-with-Advanced-Feature-Extraction.pdf#page=12|PDF p.12]]

## 指标与条件
“millisecond loop”是on-device设计目标；queue_depth812、drop_rate0.8%、queue_p95 740等是feature示例，非预测准确率或控制性能基准。[[sonic-workshop/Plug-and-Play-ML-Pipelines-for-SONiC-On-Device-Intelligence-with-Advanced-Feature-Extraction.pdf#page=6|PDF p.6]][[sonic-workshop/Plug-and-Play-ML-Pipelines-for-SONiC-On-Device-Intelligence-with-Advanced-Feature-Extraction.pdf#page=10|PDF p.10]] 文件没有吞吐、CPU成本、precision/recall、FPR、p99或故障恢复测量。

## 图表与架构
已核p.7闭环：inference actions经NOS adapter回到SONiC，而不是直接改ASIC。已核p.12的“ZERO effect”是幻灯片宣称，缺少stress test证据，不能在知识库中升级为已验证零影响。

## 关联与比较
[[knowledge/concepts/network-clock-evidence]]；[[knowledge/concepts/network-executable-validation]]。[[knowledge/sources/src-fb4535953716]]提供feature pipeline应继承的时间、support-state与provenance契约。

## 不确定性与待验证
p.13仍是HFT enhancement、FE HLD、virtual switch reference implementation与Marvell SAI support路线，不能写成全部已上线。需补out-of-distribution、模型版本回滚、动作权限/限速、false-positive隔离以及BGP/CPU压力下的negative-control测试。
