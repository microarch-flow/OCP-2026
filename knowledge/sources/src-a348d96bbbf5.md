---
id: "src-a348d96bbbf5"
type: "source"
title: "Cisco/AMD 模块化 SmartSwitch：DPU sled 标准化边界"
source_path: "networking/03_DPU Sled Design Standard in a Modular SmartSwitch by Cisco and AMD.pdf"
source_git_blob_sha: "db563467ed03987c1798578aaf0521a7906de34a"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 18
review_status: "analyzed-visual"
evidence_pages: [2, 3, 4, 6, 7, 8, 9, 11, 12, 14, 15, 16]
text_reviewed: true
key_pages_visual_checked: [6, 7]
tags: ["ocp2026", "networking"]
concepts: ["[[knowledge/concepts/network-executable-validation]]"]
---

# Cisco/AMD 模块化 SmartSwitch：DPU sled 标准化边界

## 核心结论
把 DPU 当作交换机机箱模块，统一电源、管理、固件和流量引导，可支持集中式网络服务卸载；但交换带宽不等于 DPU 可处理带宽，必须显式规划 NPU:DPU 超售与失效后的引流。[[networking/03_DPU Sled Design Standard in a Modular SmartSwitch by Cisco and AMD.pdf#page=3|PDF p.3]][[networking/03_DPU Sled Design Standard in a Modular SmartSwitch by Cisco and AMD.pdf#page=11|PDF p.11]][[networking/03_DPU Sled Design Standard in a Modular SmartSwitch by Cisco and AMD.pdf#page=12|PDF p.12]]

## 关键证据、指标与条件
- 代表系统 Cisco 8102-28FH-DPU-O：Q200L+AMD Elba，2RU，总标称 12.8Tb/s 中 11.2Tb/s switching、1.6Tb/s DPU processing；28×400G 外口。2×2.3kW 是 PSU 额定容量，不是实测整机功耗。[[networking/03_DPU Sled Design Standard in a Modular SmartSwitch by Cisco and AMD.pdf#page=4|PDF p.4]]
- sled 最多两个 DPU，180W 上限；接口图显示总 400GE 可分为两路 200GE，PCIe Gen4 管理连接与以太网数据通路分开。p.6 “400G per DPU slot”措辞易被读成每 ASIC 400G，应以最终 pin/spec 明确槽位定义。[[networking/03_DPU Sled Design Standard in a Modular SmartSwitch by Cisco and AMD.pdf#page=6|PDF p.6]][[networking/03_DPU Sled Design Standard in a Modular SmartSwitch by Cisco and AMD.pdf#page=7|PDF p.7]]
- 12V 经主板 hotswap 保护，sled 自行完成上下电序列；环境 0–40°C、最大穿透风量 30CFM。独立 DPU power control 不代表已证明任意在线拔插无业务损失。[[networking/03_DPU Sled Design Standard in a Modular SmartSwitch by Cisco and AMD.pdf#page=9|PDF p.9]][[networking/03_DPU Sled Design Standard in a Modular SmartSwitch by Cisco and AMD.pdf#page=14|PDF p.14]]
- 每 DPU 的虚拟 PCIe 连接暴露为 Linux netdev，承载状态/配置/升级，gNMI/gRPC 遥测；数据面示例为加密、NAT、VPC，而非 GPU collective 加速。[[networking/03_DPU Sled Design Standard in a Modular SmartSwitch by Cisco and AMD.pdf#page=14|PDF p.14]][[networking/03_DPU Sled Design Standard in a Modular SmartSwitch by Cisco and AMD.pdf#page=15|PDF p.15]]

## 图表与架构
已核 p.6/7 实物与接口框图：CPLD 有 always-on 与各 DPU 电源域，SPI/I2C/UART/JTAG 为维护路径。图上 PCIe x4/x2 分配与正文“每 DPU x2”存在平台可配置因素，不能统一宣称单一通用 lane 数。[[networking/03_DPU Sled Design Standard in a Modular SmartSwitch by Cisco and AMD.pdf#page=7|PDF p.7]][[networking/03_DPU Sled Design Standard in a Modular SmartSwitch by Cisco and AMD.pdf#page=8|PDF p.8]]

## 关联与比较
[[knowledge/concepts/network-executable-validation]]：平台标准化需同时规定发现、健康、断电、PCIe attach/detach、固件升级与数据面 failover，不能只有机械尺寸。

## 不确定性与待验证
设计表示将开源、完整信号表后续提供，非本材料已包含完整可制造规范；100G/lane、更高功率属于下一代方向。[[networking/03_DPU Sled Design Standard in a Modular SmartSwitch by Cisco and AMD.pdf#page=2|PDF p.2]][[networking/03_DPU Sled Design Standard in a Modular SmartSwitch by Cisco and AMD.pdf#page=9|PDF p.9]][[networking/03_DPU Sled Design Standard in a Modular SmartSwitch by Cisco and AMD.pdf#page=16|PDF p.16]] PCB 图约 6.5 英寸高与 p.10 6.978 英寸尺寸可能范围不同，不能直接拿来加工。页内保留 Cisco Confidential 标识，未据此扩大传播；不引用市场 TAM 推导技术价值。

