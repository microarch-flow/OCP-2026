---
id: "src-063ec92debe7"
type: "source"
title: "PLDM更新需同步参考测量与授权：把固件交付接上证明"
source_path: "manageability-workshop/Using SPDM for PLDM Firmware Updates- Authorization Policy and Measurement Manifest Capabilities.pdf"
source_git_blob_sha: "172cfd1545acb39766a019b8849699e9188e6d40"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 16
review_status: "analyzed-visual"
evidence_pages: [6, 7, 8, 9, 12, 13, 14]
tags: ["ocp", "source", "platform", "manageability-workshop"]
text_reviewed: true
key_pages_visual_checked: [8]
updated: "2026-10-30"
---

# PLDM更新需同步参考测量与授权：把固件交付接上证明

> 阅读范围：已阅读本文件全部可提取文字（16页）。关键页已视觉核对：8；不代表逐页视觉审核。

## 核心结论

- SPDM返回测量不告诉验证者“正确值是什么”；PLDM FW Update 1.3新增reference manifest携带能力，把新固件与相应参考值随包交付。[[manageability-workshop/Using SPDM for PLDM Firmware Updates- Authorization Policy and Measurement Manifest Capabilities.pdf#page=6|PDF p.6]][[manageability-workshop/Using SPDM for PLDM Firmware Updates- Authorization Policy and Measurement Manifest Capabilities.pdf#page=7|PDF p.7]]
- PLDM不规定manifest内容格式，仅带识别tag；数据中心管理系统仍负责通过可信通道把它送给Verifier，更新设备本身不等于验证策略已更新。[[manageability-workshop/Using SPDM for PLDM Firmware Updates- Authorization Policy and Measurement Manifest Capabilities.pdf#page=7|PDF p.7]][[manageability-workshop/Using SPDM for PLDM Firmware Updates- Authorization Policy and Measurement Manifest Capabilities.pdf#page=8|PDF p.8]]
- DSP0289授权协议与DSP0294政策分离，可给密钥/证书管理员和固件/恢复管理员不同privilege。[[manageability-workshop/Using SPDM for PLDM Firmware Updates- Authorization Policy and Measurement Manifest Capabilities.pdf#page=12|PDF p.12]][[manageability-workshop/Using SPDM for PLDM Firmware Updates- Authorization Policy and Measurement Manifest Capabilities.pdf#page=13|PDF p.13]]

## 关键证据

- 包可含多个manifest，通常签名，可按firmware device ID组织并支持下游设备；CoRIM只是可选参考格式。[[manageability-workshop/Using SPDM for PLDM Firmware Updates- Authorization Policy and Measurement Manifest Capabilities.pdf#page=6|PDF p.6]][[manageability-workshop/Using SPDM for PLDM Firmware Updates- Authorization Policy and Measurement Manifest Capabilities.pdf#page=9|PDF p.9]]
- 敏感命令优先包括SPDM配置变更、PLDM FW更新、Security Revision和Reset to Default；以后可扩展。[[manageability-workshop/Using SPDM for PLDM Firmware Updates- Authorization Policy and Measurement Manifest Capabilities.pdf#page=12|PDF p.12]][[manageability-workshop/Using SPDM for PLDM Firmware Updates- Authorization Policy and Measurement Manifest Capabilities.pdf#page=13|PDF p.13]]
- 支持多个policy共存并不自动给出业务策略，厂商/其他标准可定义自身授权政策。[[manageability-workshop/Using SPDM for PLDM Firmware Updates- Authorization Policy and Measurement Manifest Capabilities.pdf#page=14|PDF p.14]]

## 指标与条件

没有manifest大小、分发延迟或更新后证明可用窗口数字；“v1.3支持”是功能版本声明，非所有设备和BMC已有实现。[[manageability-workshop/Using SPDM for PLDM Firmware Updates- Authorization Policy and Measurement Manifest Capabilities.pdf#page=7|PDF p.7]]

## 图表与架构

已视觉核对p.8：manifest向Verifier、component images经Update Agent向Device的两条路径分开；这是需要协调的双交付，不是同一成功响应。

## 关联与比较

与[[knowledge/sources/src-ce8c8976d058|Owner授权的OOB更新]]及[[knowledge/sources/src-bbddc7859662|hitless证明]]构成三段：允许更新、执行更新、认可更新后的证据；三者失败处理必须共同设计。

## 不确定性与待验证

需补manifest真实性/签名根、回滚匹配、旧新参考值重叠窗口、失败原子性、策略吊销和多个policy冲突处理。

