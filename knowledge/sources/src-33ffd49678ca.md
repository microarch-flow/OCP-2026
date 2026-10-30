---
id: "src-33ffd49678ca"
type: "source"
title: "UALink Switch API：面向 scale-up 的对象管理与租户隔离"
source_path: "networking/The UALink Switch API - A Common Abstraction for Scale-Up AI Switches.pdf"
source_git_blob_sha: "8b0a4f9547d40708b2f764cb5a5e2d588c49fb1d"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 16
review_status: "analyzed-text"
evidence_pages: [3, 4, 5, 6, 8, 10, 11, 12, 13, 14]
text_reviewed: true
key_pages_visual_checked: []
tags: ["ocp2026", "networking"]
concepts: ["[[knowledge/concepts/network-executable-validation]]"]
---

# UALink Switch API：面向 scale-up 的对象管理与租户隔离

## 核心结论
此演讲是 SMA 与交换机之间的标准 C API，不是 UALink PHY/链路协议定义，也不是新的 gNMI 传输。它试图在生态早期统一对象行为、bulk局部失败、遥测和 bring-up，避免每个 vendor SDK 迫使上层重写。[[networking/The UALink Switch API - A Common Abstraction for Scale-Up AI Switches.pdf#page=3|PDF p.3]][[networking/The UALink Switch API - A Common Abstraction for Scale-Up AI Switches.pdf#page=4|PDF p.4]][[networking/The UALink Switch API - A Common Abstraction for Scale-Up AI Switches.pdf#page=5|PDF p.5]]

## 关键证据、指标与条件
- UALink 是 load/store/atomic 语义的 scale-up；复用 Ethernet PHY 不等于运行 Ethernet packet fabric。Pod Controller/NMA/SMA 分工中，本材料只讲 SMA→switch 边界。[[networking/The UALink Switch API - A Common Abstraction for Scale-Up AI Switches.pdf#page=3|PDF p.3]][[networking/The UALink Switch API - A Common Abstraction for Scale-Up AI Switches.pdf#page=4|PDF p.4]]
- 物理 switch 可有多个 logical switching plane，各 plane 内再以 vPod 隔离租户；route type1 key 为 switch+vPod+logical-switch+dstAPU，type2 为 switch+srcAPU+srcPort+dstAPU。[[networking/The UALink Switch API - A Common Abstraction for Scale-Up AI Switches.pdf#page=6|PDF p.6]][[networking/The UALink Switch API - A Common Abstraction for Scale-Up AI Switches.pdf#page=8|PDF p.8]]
- 所有调用 bulk-first，返回逐对象状态；原子性是**每对象**，不是整个 batch。create/set 的 reflection list 返回操作后状态，unsupported 时 count=0，调用者仍需处理能力差异。[[networking/The UALink Switch API - A Common Abstraction for Scale-Up AI Switches.pdf#page=10|PDF p.10]]
- telemetry 含 FEC error、LLR replay、credit occupancy histogram；READ_AND_CLEAR 语义为原子。事件携完整当前属性快照和时间戳，意在乱序后收敛，不能在未定义时间基准时仅靠 timestamp 保证跨设备全序。[[networking/The UALink Switch API - A Common Abstraction for Scale-Up AI Switches.pdf#page=11|PDF p.11]][[networking/The UALink Switch API - A Common Abstraction for Scale-Up AI Switches.pdf#page=12|PDF p.12]]
- switch_index 要跨重启/升级稳定；bring-up 必须邻居对照 intent、vPod隔离、路由安装后才允许 workload。[[networking/The UALink Switch API - A Common Abstraction for Scale-Up AI Switches.pdf#page=8|PDF p.8]][[networking/The UALink Switch API - A Common Abstraction for Scale-Up AI Switches.pdf#page=13|PDF p.13]]

## 图表与架构
全文已读，未核图，分析以 API 列表/示例代码/明确步骤为证据。不要把 vPod 隔离直接等同物理故障独立或侧信道完全隔离。

## 关联与比较
[[knowledge/concepts/network-executable-validation]]：与 SAI 相似的对象抽象应补约束发现、错误注入和行为互操作，而非仅编译同一个头文件。

## 不确定性与待验证
header 仍在 finalized、社区发布 soon；mock SMA/SDK 是参考，不是多厂商芯片互操作结果。[[networking/The UALink Switch API - A Common Abstraction for Scale-Up AI Switches.pdf#page=14|PDF p.14]] 需验证事件丢失/重启 epoch、批操作部分成功回滚、vPod修改期间安全性、隔离失效与 capability协商。

