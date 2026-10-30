---
id: "src-478d04e7b9df"
type: "source"
title: "An Open Lightweight Serial Interconnect (LSI) for Composable AI Architecture"
aliases: ["An Open Lightweight Serial Interconnect (LSI) for Composable AI Architecture"]
speakers: "Vishal Shah — VP of Product, Credo; Allan Cantle — CEO, Nallasway"
source_path: "Server：Open Chiplet Economy/An Open Lightweight Serial Interconnect for Composable AI Architectures.pdf"
source_git_blob_sha: "40b6baf1788128cc0a870e2e414d9c41ffa994bc"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 14
review_status: "analyzed-visual"
text_reviewed: true
key_pages_visual_checked: [3, 4, 7, 8, 9, 10, 11, 12]
evidence_pages: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
tags: ["ocp2026", "source", "compute-memory"]
concepts: ["[[knowledge/concepts/compute-memory-chiplet-link-efficiency]]"]
---

# An Open Lightweight Serial Interconnect (LSI) for Composable AI Architecture

## 核心结论
LSI针对封装外、短板级通道的“中间距离”：用AXI-over-VSR保留内存/IO事务与低协议开销，在封装内D2D和long-reach SerDes之间取舍。**复用PCIe6 FLIT结构不等于整栈PCIe/CXL语义或软件兼容**。

## 关键证据
- OmniConnect的late IO binding将lane资源分给memory、C2C、networking；由VSR SerDes和lightweight AXI framer组成。[[Server：Open Chiplet Economy/An Open Lightweight Serial Interconnect for Composable AI Architectures.pdf#page=2|PDF p.2]]
- p.3对比目标通道：封装内<25mm；112G VSR约10inch/23dB；long reach>1m/30+dB。Credo声明<1pJ/bit、1.8Tb/s/mm beachfront，未给实测负载/工艺/测量边界。[[Server：Open Chiplet Economy/An Open Lightweight Serial Interconnect for Composable AI Architectures.pdf#page=3|PDF p.3]]
- 512-bit AXI五通道独立packetize，per-channel credit，经6B DLP返回；最多16data beats合并，packet可跨FLIT，稀疏流用idle填充。[[Server：Open Chiplet Economy/An Open Lightweight Serial Interconnect for Composable AI Architectures.pdf#page=7|PDF p.7]] [[Server：Open Chiplet Economy/An Open Lightweight Serial Interconnect for Composable AI Architectures.pdf#page=8|PDF p.8]] [[Server：Open Chiplet Economy/An Open Lightweight Serial Interconnect for Composable AI Architectures.pdf#page=9|PDF p.9]]
- 256B FLIT含238B DATA、4B header、8B CRC、6B FEC；可选6B DLP占用DATA空间。93%是238/256≈92.97%的**理想payload比例**，还没扣AXI packet header、DLP与idle。[[Server：Open Chiplet Economy/An Open Lightweight Serial Interconnect for Composable AI Architectures.pdf#page=10|PDF p.10]]
- 先FEC纠错，再CRC检测，失败重传；TX保存未ACK FLIT，NAK从失败位置replay，RX丢弃乱序；最多一个outstanding replay request。p.11所称≤17bit单lane burst保证依赖该三路interleaved code结构，不是任意错误图样保证。[[Server：Open Chiplet Economy/An Open Lightweight Serial Interconnect for Composable AI Architectures.pdf#page=11|PDF p.11]]

## 指标与条件
没有end-to-end memory latency、服务p99或LLM throughput测量。固定FLIT的可预测buffering不代表无排队、无credit stall；“no software stack”不取消配置/安全/管理需求。Phase1 spec目标2026-11，演讲时为draft贡献/开放评审阶段。[[Server：Open Chiplet Economy/An Open Lightweight Serial Interconnect for Composable AI Architectures.pdf#page=13|PDF p.13]]

## 图表与架构
已核对AXI→framer→SerDes→memory controller路径、packet表、DLP、FLIT与error处理。FCSA在此提供foundation/design/profile层级定位；不是LSI自动覆盖所有FCSA系统服务。[[Server：Open Chiplet Economy/An Open Lightweight Serial Interconnect for Composable AI Architectures.pdf#page=4|PDF p.4]] [[Server：Open Chiplet Economy/An Open Lightweight Serial Interconnect for Composable AI Architectures.pdf#page=12|PDF p.12]]

## 关联与比较
[[knowledge/concepts/compute-memory-chiplet-link-efficiency|互连效率与尾延迟]]；HPCM/Weaver概念将该接口作为可插拔LPDDR路径。TLL2.0和LSI解决不同协议结构，不能以同名“lightweight”当作同一标准。

## 不确定性与待验证
需规范版本、互操作测试、PHY+framer总能耗、credit RTT/buffer、sparse traffic与replay尾部、memory consistency模型。p.3的<1pJ/bit与HPCM演讲1.15pJ/bit不必矛盾，可能是PHY和完整IO边界不同，但材料没有足够信息确认。


## 原始页码导航
[[Server：Open Chiplet Economy/An Open Lightweight Serial Interconnect for Composable AI Architectures.pdf#page=2|p.2]] · [[Server：Open Chiplet Economy/An Open Lightweight Serial Interconnect for Composable AI Architectures.pdf#page=3|p.3]] · [[Server：Open Chiplet Economy/An Open Lightweight Serial Interconnect for Composable AI Architectures.pdf#page=4|p.4]] · [[Server：Open Chiplet Economy/An Open Lightweight Serial Interconnect for Composable AI Architectures.pdf#page=5|p.5]] · [[Server：Open Chiplet Economy/An Open Lightweight Serial Interconnect for Composable AI Architectures.pdf#page=6|p.6]] · [[Server：Open Chiplet Economy/An Open Lightweight Serial Interconnect for Composable AI Architectures.pdf#page=7|p.7]] · [[Server：Open Chiplet Economy/An Open Lightweight Serial Interconnect for Composable AI Architectures.pdf#page=8|p.8]] · [[Server：Open Chiplet Economy/An Open Lightweight Serial Interconnect for Composable AI Architectures.pdf#page=9|p.9]] · [[Server：Open Chiplet Economy/An Open Lightweight Serial Interconnect for Composable AI Architectures.pdf#page=10|p.10]] · [[Server：Open Chiplet Economy/An Open Lightweight Serial Interconnect for Composable AI Architectures.pdf#page=11|p.11]] · [[Server：Open Chiplet Economy/An Open Lightweight Serial Interconnect for Composable AI Architectures.pdf#page=12|p.12]] · [[Server：Open Chiplet Economy/An Open Lightweight Serial Interconnect for Composable AI Architectures.pdf#page=13|p.13]]
