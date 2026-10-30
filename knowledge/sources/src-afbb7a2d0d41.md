---
id: "src-afbb7a2d0d41"
type: "source"
title: "平台Composite Attestation：签名绑定设备集合而非拼一袋证据"
source_path: "Security/BMC-Mediated Platform Composite Attestation via Redfish.pdf"
source_git_blob_sha: "4beca96c565ec162103b1cb8bb1251ba9a619b00"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 14
review_status: "analyzed-visual"
evidence_pages: [2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13]
tags: ["ocp", "source", "platform", "security"]
text_reviewed: true
key_pages_visual_checked: [4, 8]
updated: "2026-10-30"
concepts: ["[[knowledge/concepts/platform-dynamic-trust-lifecycle]]"]
---

# 平台Composite Attestation：签名绑定设备集合而非拼一袋证据

> 阅读范围：已阅读本文件全部可提取文字（14页）。关键页已视觉核对：4, 8；不代表逐页视觉审核。

## 核心结论

- 单设备证明不能证明“哪些设备组成此平台”；提案由BMC RoT作为Lead Attester签自己的测量、统一nonce和各原生证据digest，再用Platform CoRIM核对预期组成。[[Security/BMC-Mediated Platform Composite Attestation via Redfish.pdf#page=2|PDF p.2]][[Security/BMC-Mediated Platform Composite Attestation via Redfish.pdf#page=3|PDF p.3]][[Security/BMC-Mediated Platform Composite Attestation via Redfish.pdf#page=5|PDF p.5]][[Security/BMC-Mediated Platform Composite Attestation via Redfish.pdf#page=9|PDF p.9]]
- 平台签名不替代子设备原始验签；应保留native evidence字节并独立验证，防止中间relay把无签名数据洗成可信证据。[[Security/BMC-Mediated Platform Composite Attestation via Redfish.pdf#page=6|PDF p.6]][[Security/BMC-Mediated Platform Composite Attestation via Redfish.pdf#page=8|PDF p.8]]

## 关键证据

- BMC Linux负责收集/转送，BMC RoT负责签Composite EAT；Vendor CoRIM给设备参考值，Platform CoRIM给Lead Attester/环境集合/数量等预期。[[Security/BMC-Mediated Platform Composite Attestation via Redfish.pdf#page=4|PDF p.4]]
- env.*标签关联digest与detached Claims-Set，digest输入为确定编码CBOR Claims-Set而不是bundle外包bstr。[[Security/BMC-Mediated Platform Composite Attestation via Redfish.pdf#page=6|PDF p.6]]
- 只有次级具有自身RoT/签名身份才构成嵌套Lead Attester；MCTP桥接不必嵌套，无签名relay不能继承信任。[[Security/BMC-Mediated Platform Composite Attestation via Redfish.pdf#page=8|PDF p.8]]
- 作者称有SDK和早期OpenBMC采用，但profile、Redfish扩展及跨厂商互通仍待标准化。[[Security/BMC-Mediated Platform Composite Attestation via Redfish.pdf#page=11|PDF p.11]][[Security/BMC-Mediated Platform Composite Attestation via Redfish.pdf#page=12|PDF p.12]][[Security/BMC-Mediated Platform Composite Attestation via Redfish.pdf#page=13|PDF p.13]]

## 指标与条件

从N次逐设备Redfish请求到一个平台scope请求是API模型目标；流程仍包含202异步和GET结果、底层N设备收集，不是“一次网络往返”或O(1)设备工作。无延迟/QPS/证据大小测量。[[Security/BMC-Mediated Platform Composite Attestation via Redfish.pdf#page=2|PDF p.2]][[Security/BMC-Mediated Platform Composite Attestation via Redfish.pdf#page=7|PDF p.7]]

## 图表与架构

已视觉核对p.4信任/收集边界、p.8嵌套结构。

## 关联与比较

与[[knowledge/sources/src-df74b2260c89|Redfish设备签名测量]]相比，增加平台组成/防替换检查；与hitless策略相比仍需处理收集期间/之后设备状态变化。

## 不确定性与待验证

需定义统一nonce下的时间偏斜、缺失设备、热插拔、嵌套nonce绑定、故障容错与Platform CoRIM更新授权；“completeness可检查”依赖可信预期清单。

