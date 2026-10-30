---
id: "src-66eed8f6331f"
type: "source"
title: "SPDM更新：Hybrid、统一授权政策与渐进FRU签名"
source_path: "manageability-workshop/SPDM Update- Hybrid, Authorization Policy and Standard Signatures (FRU).pdf"
source_git_blob_sha: "0308a12f0b85f094fe5ba5b3eee844fa2137f33b"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 11
review_status: "analyzed-text"
evidence_pages: [2, 5, 6, 7, 8, 9, 10]
tags: ["ocp", "source", "platform", "manageability-workshop"]
text_reviewed: true
key_pages_visual_checked: []
updated: "2026-10-30"
---

# SPDM更新：Hybrid、统一授权政策与渐进FRU签名

> 阅读范围：已阅读本文件全部可提取文字（11页）。未完成图表视觉核对；不把文字提取视作图形关系验证。

## 核心结论

- 材料为工作组WIP，1.5 Hybrid方向强调最小变更和有限组合，端点不可自由mix-and-match。[[manageability-workshop/SPDM Update- Hybrid, Authorization Policy and Standard Signatures (FRU).pdf#page=2|PDF p.2]][[manageability-workshop/SPDM Update- Hybrid, Authorization Policy and Standard Signatures (FRU).pdf#page=5|PDF p.5]]
- DSP0289定义授权机制，DSP0294定义跨SPDM/PLDM动作的政策配置；身份认证成功不等于拥有固件更新或密钥管理权限。[[manageability-workshop/SPDM Update- Hybrid, Authorization Policy and Standard Signatures (FRU).pdf#page=8|PDF p.8]]
- FRU签名需支持不同制造阶段/组织增量写入，不能只在最终一次签整个对象。[[manageability-workshop/SPDM Update- Hybrid, Authorization Policy and Standard Signatures (FRU).pdf#page=10|PDF p.10]]

## 关键证据

- Hybrid列4种签名与3种key exchange组合，均围绕MLDSA87/MLKEM1024加传统算法；是本草案列表，非所有密码组合。[[manageability-workshop/SPDM Update- Hybrid, Authorization Policy and Standard Signatures (FRU).pdf#page=6|PDF p.6]]
- OCP GET_ATTESTATION请求推动自包含签名远程验证与profile discovery/claim读取。[[manageability-workshop/SPDM Update- Hybrid, Authorization Policy and Standard Signatures (FRU).pdf#page=7|PDF p.7]]
- 统一签名格式希望适用于多工作组和传统/PQC；FRU提案以file table中签名文件及覆盖文件头部来支持增量扩展签名。[[manageability-workshop/SPDM Update- Hybrid, Authorization Policy and Standard Signatures (FRU).pdf#page=9|PDF p.9]][[manageability-workshop/SPDM Update- Hybrid, Authorization Policy and Standard Signatures (FRU).pdf#page=10|PDF p.10]]

## 指标与条件

演讲标DSP0289为2025年12月、DSP0294为2026年8月；是文档状态陈述，没有互通率/握手性能/签名开销。[[manageability-workshop/SPDM Update- Hybrid, Authorization Policy and Standard Signatures (FRU).pdf#page=8|PDF p.8]]

## 图表与架构

FRU增量签名图未视觉核对，本文只使用文字所述分阶段覆盖要求，不补写完整签名链。

## 关联与比较

对应设备身份provisioning、PLDM更新授权和供应链信息三个层面：统一crypto机制仍需要每个操作定义权限与所签对象。

## 不确定性与待验证

需回查最终规范的算法名称编码、签名覆盖/删除/重排防护、政策冲突优先级与撤销。

