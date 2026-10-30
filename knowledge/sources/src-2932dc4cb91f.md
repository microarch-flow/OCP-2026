---
id: "src-2932dc4cb91f"
type: "source"
title: "Intel FSP演进：保持Bootloader接口、内部向openSFI无状态对齐"
source_path: "Open Platform Firmware (OPF)/The Next Evolution of Intel's FSP- Aligning to openSFI and UPCI.pdf"
source_git_blob_sha: "cf6180859626124832ee2355f37ae95629b42694"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 10
review_status: "analyzed-visual"
evidence_pages: [4, 5, 7, 8, 9]
tags: ["ocp", "source", "platform", "open-platform-firmware-(opf)"]
text_reviewed: true
key_pages_visual_checked: [6]
updated: "2026-10-30"
concepts: ["[[knowledge/concepts/platform-firmware-decoupling]]"]
---

# Intel FSP演进：保持Bootloader接口、内部向openSFI无状态对齐

> 阅读范围：已阅读本文件全部可提取文字（10页）。关键页已视觉核对：6；不代表逐页视觉审核。

## 核心结论

- 演讲称FSP仍是Intel硅初始化二进制封装主载体，当前v2.5；计划中的数据中心改进不修改FSP规范、预期不影响Bootloader代码。[[Open Platform Firmware (OPF)/The Next Evolution of Intel's FSP- Aligning to openSFI and UPCI.pdf#page=4|PDF p.4]][[Open Platform Firmware (OPF)/The Next Evolution of Intel's FSP- Aligning to openSFI and UPCI.pdf#page=5|PDF p.5]]
- 改进把FSP-M从EDKII/PEI依赖中拆出、FSP-S与M独立，并使持久状态由Host管理资源承载，对齐openSFI stateless原则。[[Open Platform Firmware (OPF)/The Next Evolution of Intel's FSP- Aligning to openSFI and UPCI.pdf#page=5|PDF p.5]][[Open Platform Firmware (OPF)/The Next Evolution of Intel's FSP- Aligning to openSFI and UPCI.pdf#page=7|PDF p.7]][[Open Platform Firmware (OPF)/The Next Evolution of Intel's FSP- Aligning to openSFI and UPCI.pdf#page=8|PDF p.8]]

## 关键证据

- FSP-M在temporary RAM运行，FSP-S在physical memory运行；PEI Core从M移向S。API模式默认，dispatch环境按需启动。[[Open Platform Firmware (OPF)/The Next Evolution of Intel's FSP- Aligning to openSFI and UPCI.pdf#page=5|PDF p.5]][[Open Platform Firmware (OPF)/The Next Evolution of Intel's FSP- Aligning to openSFI and UPCI.pdf#page=8|PDF p.8]]
- 演讲将变化放在future Xeon platform，未提供具体上市SKU/日期或UPCI完整落地细节。[[Open Platform Firmware (OPF)/The Next Evolution of Intel's FSP- Aligning to openSFI and UPCI.pdf#page=9|PDF p.9]]

## 指标与条件

无boot time、代码大小、内存占用或跨Bootloader通过率；不能将内部模块解耦解释成零迁移风险。

## 图表与架构

已视觉核对p.6：Xeon 6现有API/Dispatch两流程与下一代收敛流程并列；新M采用table-driven initialization、M/S执行分开。

## 关联与比较

是厂商实现朝openSFI原则靠拢的具体例子，但并不等于FSP已经成为跨厂商openSFI最终规范实现。

## 不确定性与待验证

需实际future平台二进制/文档与Bootloader回归矩阵；“不改规范”不自动证明时序、错误语义与状态所有权完全不变。

