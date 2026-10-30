---
id: "src-cbd1e3d6f4f9"
type: "source"
title: "TCG数据中心信任：DICE身份、TPM安全通道与PQC迁移"
source_path: "Security/Advancing Data Center Trust- Open Standards for Attestation, Device Identity, and Post-Quantum.pdf"
source_git_blob_sha: "a3f6b0572f82d16761f5513c35e858359fd2fed8"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 17
review_status: "analyzed-visual"
evidence_pages: [8, 9, 12, 13, 14, 15]
tags: ["ocp", "source", "platform", "security"]
text_reviewed: true
key_pages_visual_checked: [13, 14]
updated: "2026-10-30"
---

# TCG数据中心信任：DICE身份、TPM安全通道与PQC迁移

> 阅读范围：已阅读本文件全部可提取文字（17页）。关键页已视觉核对：13, 14；不代表逐页视觉审核。

## 核心结论

- DICE/DPE、TPM-over-SPDM与PQC TPM分别处理组件身份/测量秘密保护、Host–TPM通道、密码迁移，不能把其中一项当成完整信任链。[[Security/Advancing Data Center Trust- Open Standards for Attestation, Device Identity, and Post-Quantum.pdf#page=8|PDF p.8]][[Security/Advancing Data Center Trust- Open Standards for Attestation, Device Identity, and Post-Quantum.pdf#page=9|PDF p.9]][[Security/Advancing Data Center Trust- Open Standards for Attestation, Device Identity, and Post-Quantum.pdf#page=12|PDF p.12]][[Security/Advancing Data Center Trust- Open Standards for Attestation, Device Identity, and Post-Quantum.pdf#page=15|PDF p.15]]
- TPM-over-SPDM的目标是Requester Host与Responder TPM之间安全通道，应对主动中间插入风险；它不是替代TPM本身。[[Security/Advancing Data Center Trust- Open Standards for Attestation, Device Identity, and Post-Quantum.pdf#page=12|PDF p.12]][[Security/Advancing Data Center Trust- Open Standards for Attestation, Device Identity, and Post-Quantum.pdf#page=13|PDF p.13]]

## 关键证据

- DPE中CDI和私钥不离开环境，向SoC其他主体提供DICE身份、测量启动和签名服务。[[Security/Advancing Data Center Trust- Open Standards for Attestation, Device Identity, and Post-Quantum.pdf#page=9|PDF p.9]]
- p.13把SPDM Secure Session置于TPM Application Layer外，内部通过TPM Protected Capabilities交换信息；仍保留TPM命令与SPDM消息外部接口。[[Security/Advancing Data Center Trust- Open Standards for Attestation, Device Identity, and Post-Quantum.pdf#page=13|PDF p.13]]
- p.14路线图显示TPM Library Spec 185、PC Client PTP 1.07与EK Credential Profile V2.7标为Published，而PC Client Certification Program仍In progress。[[Security/Advancing Data Center Trust- Open Standards for Attestation, Device Identity, and Post-Quantum.pdf#page=14|PDF p.14]]

## 指标与条件

规范版本与发布状态按本演讲记录；没有算法耗时、证书大小、总线占用或TPM吞吐的基准。PQC-ready不等于全生态产品已认证。[[Security/Advancing Data Center Trust- Open Standards for Attestation, Device Identity, and Post-Quantum.pdf#page=14|PDF p.14]][[Security/Advancing Data Center Trust- Open Standards for Attestation, Device Identity, and Post-Quantum.pdf#page=15|PDF p.15]]

## 图表与架构

已视觉核对p.13层次图与p.14依赖图，补足文本抽取缺失的规范状态和认证计划边界。

## 关联与比较

与Caliptra/DICE设备RoT互补：组件身份及端点内部可信，不自动保证离散TPM物理通道可信；必须审计链路与消息保护。

## 不确定性与待验证

外部规范与厂商实现未单独核验；缺部署兼容矩阵、老平台迁移策略、会话建立失败和密钥轮换运维数据。

