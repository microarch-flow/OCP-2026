---
id: "src-d53a163f26fd"
type: "source"
title: "Addressing Discovery and Topology Challenges in M-PESTI Systems"
aliases: ["Addressing Discovery and Topology Challenges in M-PESTI Systems"]
speakers: "Tamer Gudu；Aleksandar Jovanovic（AMD）"
source_path: "server/01_Addressing Discovery and Topology Challenges in M-PESTI Systems.pdf"
source_git_blob_sha: "4e29e3c3ccc6f12f5bbdb9d9f6d85ab794c0f7b4"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 11
review_status: "analyzed-visual"
text_reviewed: true
key_pages_visual_checked: [4, 5, 6, 8]
evidence_pages: [3, 4, 5, 6, 7, 8, 9]
tags: ["ocp2026", "source", "compute-memory"]
concepts: ["[[knowledge/concepts/compute-memory-modular-platform-contract]]"]
---

# Addressing Discovery and Topology Challenges in M-PESTI Systems

## 核心结论
M-PESTI 是半双工 UART sideband/control，不是主机数据高速互连。AMD 提案在 FPGA 内以高时钟 TDM 复用控制/UART 逻辑、把每路状态存 BRAM，让多条物理线路同时进展，避免逐 target 完整事务轮询造成长 discovery。[[server/01_Addressing Discovery and Topology Challenges in M-PESTI Systems.pdf#page=3|PDF p.3]] [[server/01_Addressing Discovery and Topology Challenges in M-PESTI Systems.pdf#page=5|PDF p.5]] [[server/01_Addressing Discovery and Topology Challenges in M-PESTI Systems.pdf#page=6|PDF p.6]]

## 关键证据
逐 target discovery 和 active virtual-wire 更新使完成时间随 N 线性增长；简单复制 UART 又增加面积。方案按 bit/sample 级切换 context、保持各线路输出，逻辑共享但时序独立。[[server/01_Addressing Discovery and Topology Challenges in M-PESTI Systems.pdf#page=4|PDF p.4]] [[server/01_Addressing Discovery and Topology Challenges in M-PESTI Systems.pdf#page=6|PDF p.6]]
MUX 后 break event 可能在未选线路上被漏掉；提案显式 select/ack→discovery→response/timeout，低电平时可标 simple presence，而不是假设 snooper 总能捕获任意 break。[[server/01_Addressing Discovery and Topology Challenges in M-PESTI Systems.pdf#page=7|PDF p.7]] [[server/01_Addressing Discovery and Topology Challenges in M-PESTI Systems.pdf#page=8|PDF p.8]]

## 指标与条件
- 原页记账：64 targets、2048-byte payload、44µs/byte，discovery≈5.77s；16 virtual-wire bytes 时 active round≈45ms。不是所有 M-PESTI 实现的固定时延。[[server/01_Addressing Discovery and Topology Challenges in M-PESTI Systems.pdf#page=4|PDF p.4]]
- `Fsys=250K × N × sampling rate`：64 initiators、4×采样需64MHz；8×需128MHz。“no additional latency”依赖达到这类调度时钟及存取约束，并无 RTL 面积/时序实测表。[[server/01_Addressing Discovery and Topology Challenges in M-PESTI Systems.pdf#page=5|PDF p.5]]

## 图表与架构
p.6 的 BRAM 保存 state/input/output registers，counter 选择 target，output FF 保持线路直到下次扫描。它把控制逻辑面积与并发线路数解耦，但 BRAM容量、I/O引脚、时钟和验证仍随规模增加。[[server/01_Addressing Discovery and Topology Challenges in M-PESTI Systems.pdf#page=6|PDF p.6]]

## 关联与比较
[[knowledge/concepts/compute-memory-modular-platform-contract|模块化平台契约]]：低速 discovery 延迟与错误路径影响系统启动/重配置，并非只要 connector 兼容即可组合。

## 不确定性与待验证
建议预期 early2027 贡献，属于提案而非已纳入标准。尚需确认多级MUX、超时/失联、同步break、BRAM冲突、采样裕度与版本兼容。[[server/01_Addressing Discovery and Topology Challenges in M-PESTI Systems.pdf#page=9|PDF p.9]]

## 原始页码导航
[[server/01_Addressing Discovery and Topology Challenges in M-PESTI Systems.pdf#page=3|p.3]] · [[server/01_Addressing Discovery and Topology Challenges in M-PESTI Systems.pdf#page=4|p.4]] · [[server/01_Addressing Discovery and Topology Challenges in M-PESTI Systems.pdf#page=5|p.5]] · [[server/01_Addressing Discovery and Topology Challenges in M-PESTI Systems.pdf#page=6|p.6]] · [[server/01_Addressing Discovery and Topology Challenges in M-PESTI Systems.pdf#page=7|p.7]] · [[server/01_Addressing Discovery and Topology Challenges in M-PESTI Systems.pdf#page=8|p.8]] · [[server/01_Addressing Discovery and Topology Challenges in M-PESTI Systems.pdf#page=9|p.9]]
