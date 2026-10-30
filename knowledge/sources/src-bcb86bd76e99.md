---
id: "src-bcb86bd76e99"
type: "source"
title: "Advancing Arm Server System Architecture in the OCP Ecosystem"
aliases: ["Advancing Arm Server System Architecture in the OCP Ecosystem"]
speakers: "Dong Wei；Samer El-Haj-Mahmoud（Arm）"
source_path: "server/09_SBSA Advancing Arm Server System Architecture in the OCP Ecosystem.pdf"
source_git_blob_sha: "e7ece3db364ac0e8866381dd3b3c9417769c6351"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 15
review_status: "analyzed-visual"
text_reviewed: true
key_pages_visual_checked: [2, 4, 5, 10, 12]
evidence_pages: [2, 4, 5, 6, 7, 8, 10, 12, 13]
tags: ["ocp2026", "source", "compute-memory"]
concepts: ["[[knowledge/concepts/compute-memory-modular-platform-contract]]"]
---

# Advancing Arm Server System Architecture in the OCP Ecosystem

## 核心结论
SystemReady把硬件基线、启动/安全接口、管理接口和ACS测试组成可复用platform contract，减少每个平台重复OS enablement。它不保证CPU性能相同，也不替代OS供应商的认证和支持。[[server/09_SBSA Advancing Arm Server System Architecture in the OCP Ecosystem.pdf#page=4|PDF p.4]] [[server/09_SBSA Advancing Arm Server System Architecture in the OCP Ecosystem.pdf#page=5|PDF p.5]]

## 关键证据
BSA/SBSA约束硬件体系，SBBR/BBR定义UEFI/ACPI/SMBIOS等启动接口，BBSR涉及安全，SBMR覆盖Redfish/MCTP/PLDM/SPDM等管理；ACS提供实现检查与JSON/HTML evidence。[[server/09_SBSA Advancing Arm Server System Architecture in the OCP Ecosystem.pdf#page=2|PDF p.2]] [[server/09_SBSA Advancing Arm Server System Architecture in the OCP Ecosystem.pdf#page=4|PDF p.4]] [[server/09_SBSA Advancing Arm Server System Architecture in the OCP Ecosystem.pdf#page=5|PDF p.5]]
Arm向OCP贡献SBSA/SBMR以支持多公司治理和部署反馈，测试资产仍需明确归属和版本。p.6的参考服务器SBSA level6合规实例不能推导为所有Arm服务器都达到同一level。[[server/09_SBSA Advancing Arm Server System Architecture in the OCP Ecosystem.pdf#page=6|PDF p.6]] [[server/09_SBSA Advancing Arm Server System Architecture in the OCP Ecosystem.pdf#page=7|PDF p.7]]

## 指标与条件
会议状态：公开SBSA8.0（Jul2025），OCP8.1 ALP3 WIP；SBMR3.0 ALP2公开草稿，OCP ALP4 WIP；两者REL目标2026年底。**alpha/草稿不是最终规范。**[[server/09_SBSA Advancing Arm Server System Architecture in the OCP Ecosystem.pdf#page=10|PDF p.10]] [[server/09_SBSA Advancing Arm Server System Architecture in the OCP Ecosystem.pdf#page=12|PDF p.12]]
无量化性能、功耗或节省enablement时间的实验。

## 图表与架构
ACS应作为baseline-ready门槛，失败反馈platform owner；通过后继续OS qualification。将“能安装启动标准OS”和“生产支持/性能/可靠性”分层有利于避免虚假互通承诺。[[server/09_SBSA Advancing Arm Server System Architecture in the OCP Ecosystem.pdf#page=5|PDF p.5]]

## 关联与比较
[[knowledge/concepts/compute-memory-modular-platform-contract|模块化平台契约]]：与M-PNP硬件描述互补，一个约束软件可见体系与测试，一个描述具体模块组成。

## 不确定性与待验证
本文只记录演讲时规范/认证要求快照，不作当前认证咨询。p.8将SBSA wiki误列为SBMR地址，而p.13/14分别列ocp-sbsa/ocp-sbmr；需在实施时核对正式入口，不复制错误链接作为规范身份。

## 原始页码导航
[[server/09_SBSA Advancing Arm Server System Architecture in the OCP Ecosystem.pdf#page=2|p.2]] · [[server/09_SBSA Advancing Arm Server System Architecture in the OCP Ecosystem.pdf#page=4|p.4]] · [[server/09_SBSA Advancing Arm Server System Architecture in the OCP Ecosystem.pdf#page=5|p.5]] · [[server/09_SBSA Advancing Arm Server System Architecture in the OCP Ecosystem.pdf#page=6|p.6]] · [[server/09_SBSA Advancing Arm Server System Architecture in the OCP Ecosystem.pdf#page=7|p.7]] · [[server/09_SBSA Advancing Arm Server System Architecture in the OCP Ecosystem.pdf#page=8|p.8]] · [[server/09_SBSA Advancing Arm Server System Architecture in the OCP Ecosystem.pdf#page=10|p.10]] · [[server/09_SBSA Advancing Arm Server System Architecture in the OCP Ecosystem.pdf#page=12|p.12]] · [[server/09_SBSA Advancing Arm Server System Architecture in the OCP Ecosystem.pdf#page=13|p.13]]
