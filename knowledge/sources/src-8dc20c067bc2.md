---
id: "src-8dc20c067bc2"
type: "source"
title: "Forging an Open Secure Control Plane for the AI Era"
source_path: "executive-sessions/22_Forging an Open Control Plane for the AI Era presented by Lattice.pdf"
source_git_blob_sha: "0a16be0ae9ff1383042c1bd3061f731ab8f5f55b"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 10
review_status: "analyzed-text"
evidence_pages: [2, 3, 4, 5, 6, 7, 8, 10]
text_reviewed: true
key_pages_visual_checked: []
tags: ["ocp2026", "source", "executive-expo"]
concepts: ["[[knowledge/concepts/executive-expo-system-control-evidence]]"]
---

# Forging an Open Secure Control Plane for the AI Era

## 核心结论
Lattice将管理从server lifecycle扩展为rack/cluster级控制：计算、电力、冷却、网络、固件和信任状态需共同决定动作，而不是若干孤立BMC。[[executive-sessions/22_Forging an Open Control Plane for the AI Era presented by Lattice.pdf#page=3|PDF p.3]][[executive-sessions/22_Forging an Open Control Plane for the AI Era presented by Lattice.pdf#page=4|PDF p.4]]
## 关键证据
架构拆管理/编排、平台固件/控制、trust/security三层，以开放接口连接；强调硬件root of trust、持续attestation、更新恢复与遥测闭环。[[executive-sessions/22_Forging an Open Control Plane for the AI Era presented by Lattice.pdf#page=5|PDF p.5]][[executive-sessions/22_Forging an Open Control Plane for the AI Era presented by Lattice.pdf#page=6|PDF p.6]][[executive-sessions/22_Forging an Open Control Plane for the AI Era presented by Lattice.pdf#page=7|PDF p.7]]
## 指标与条件
100,000+accelerators、1MW/rack作为挑战背景，没有给本方案实际管理规模、延迟、功耗收益、故障恢复或安全测试结果。[[executive-sessions/22_Forging an Open Control Plane for the AI Era presented by Lattice.pdf#page=2|PDF p.2]]
## 图表与架构
全文文字已阅读，未视觉检查架构图，未据箭头推断协议调用或控制优先级。材料没有落到具体API/profile版本。
## 关联与比较
与 [[knowledge/sources/src-8be3bec59f09|MiTAC分层管理]] 对读：本源给系统控制/信任原则，MiTAC给产品栈示例；二者都不自动证明跨厂商即插即用。
## 不确定性与待验证
需要可运行实现、信任锚/密钥生命周期、更新失效恢复、互通测试矩阵；“开放控制平面”仍需明确谁拥有控制权和如何避免新的集成锁定。[[executive-sessions/22_Forging an Open Control Plane for the AI Era presented by Lattice.pdf#page=8|PDF p.8]][[executive-sessions/22_Forging an Open Control Plane for the AI Era presented by Lattice.pdf#page=10|PDF p.10]]

## 知识网络
[[knowledge/concepts/executive-expo-system-control-evidence]]
