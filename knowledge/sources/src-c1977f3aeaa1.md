---
id: "src-c1977f3aeaa1"
type: "source"
title: "Flash-less 与 Streaming Boot：先解决 Early Firmware 的确定性"
source_path: "Open Platform Firmware (OPF)/Advancing Flash-less Boot in OCP Systems- A Streaming Firmware Architecture for Secure and Scalable.pdf"
source_git_blob_sha: "b4058e7f98a9713964b6ebc6180cff86ba6893f7"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 12
review_status: "analyzed-visual"
evidence_pages: [3, 4, 5, 7, 8, 9, 10]
tags: ["ocp", "source", "platform", "open-platform-firmware-(opf)"]
text_reviewed: true
key_pages_visual_checked: [5, 7, 9]
updated: "2026-10-30"
---

# Flash-less 与 Streaming Boot：先解决 Early Firmware 的确定性

> 阅读范围：已阅读本文件全部可提取文字（12页）。关键页已视觉核对：5, 7, 9；不代表逐页视觉审核。

## 核心结论

- 演讲把 flash-less 定义为设备不持久存储固件、streaming 定义为固件交付机制；二者相关但不是同义词。应按设备/阶段逐项盘点本地状态，而非把整机笼统称为“无闪存”。[[Open Platform Firmware (OPF)/Advancing Flash-less Boot in OCP Systems- A Streaming Firmware Architecture for Secure and Scalable.pdf#page=3|PDF p.3]]
- 真正的工程约束在 DRAM 训练前：必须在释放 CPU reset 前保证 Early FW 可用并验证；训练后才适合 SRAM 滑窗加 DRAM 缓冲。[[Open Platform Firmware (OPF)/Advancing Flash-less Boot in OCP Systems- A Streaming Firmware Architecture for Secure and Scalable.pdf#page=7|PDF p.7]]
- 方案同时存在本地 Early FW 副本、BMC 早期启动 flash 与外部固件服务，说明“去本地 flash”有范围边界；这是架构提案，不是已验证端到端部署结果。[[Open Platform Firmware (OPF)/Advancing Flash-less Boot in OCP Systems- A Streaming Firmware Architecture for Secure and Scalable.pdf#page=5|PDF p.5]][[Open Platform Firmware (OPF)/Advancing Flash-less Boot in OCP Systems- A Streaming Firmware Architecture for Secure and Scalable.pdf#page=9|PDF p.9]]

## 关键证据

- p.5 的数据路径是固件服务 → BMC → RoT FPGA SRAM/eSPI 仿真 → Host CPU，TPM/MCTP承担测量通道；CPU看到标准 SPI NOR 接口。[[Open Platform Firmware (OPF)/Advancing Flash-less Boot in OCP Systems- A Streaming Firmware Architecture for Secure and Scalable.pdf#page=5|PDF p.5]]
- p.9 比较 BMC SPI+独立 PFR flash、BMC SPI+PRoT 内部存储、eMMC 三种 Early FW 仓库，分别偏冗余、BOM、版本容量；没有用数值证明最优方案。[[Open Platform Firmware (OPF)/Advancing Flash-less Boot in OCP Systems- A Streaming Firmware Architecture for Secure and Scalable.pdf#page=9|PDF p.9]]
- 结论页把 DC-SCM 2.1+RoT 的 CPU BIOS streaming称为尚待工程实现的缺口；引用他厂生产例子不等于本方案量产证明。[[Open Platform Firmware (OPF)/Advancing Flash-less Boot in OCP Systems- A Streaming Firmware Architecture for Secure and Scalable.pdf#page=10|PDF p.10]]

## 指标与条件

- 作者给出的架构预算：Early FW ≤4 MB；后续 FW 32–256 MB；Early CPU Cache-as-RAM 64–512 KB，后续页验证粒度4 KB。对象为示例启动分阶段设计，不是测量分布。[[Open Platform Firmware (OPF)/Advancing Flash-less Boot in OCP Systems- A Streaming Firmware Architecture for Secure and Scalable.pdf#page=7|PDF p.7]]
- 文中列 MachXO5D SRAM 1–4 MB、早期平台超时“通常 <500 μs”。未给具体SKU、CPU平台和实验条件，不能外推为普遍硬限制。[[Open Platform Firmware (OPF)/Advancing Flash-less Boot in OCP Systems- A Streaming Firmware Architecture for Secure and Scalable.pdf#page=8|PDF p.8]]
- p.5 的50 ms、约1–20 s等为“简单时序”示意，未给实测样本/网络条件；不能承诺启动SLA或批量更新分钟级结果。[[Open Platform Firmware (OPF)/Advancing Flash-less Boot in OCP Systems- A Streaming Firmware Architecture for Secure and Scalable.pdf#page=5|PDF p.5]]

## 图表与架构

已视觉核对 p.5、7、9：确认本地 Early FW 标注、预取与滑窗的阶段分界，以及三种本地仓库。p.6完整流式图和p.4概念比较未逐图核对，本文不据其箭头做额外推断。

## 关联与比较

与 openSFI 的解耦目标互补：openSFI改变固件接口契约，streaming改变存储/传送/验证路径，不能相互替代。参见 [[knowledge/sources/src-47080f6e51ac|openSFI 源卡]]。

## 不确定性与待验证

- p.3 允许固件位于BMC/Host等本地外部源，p.4却概括flash-less为“根本依赖网络”；后者应视为其方案取舍，而非定义上的必然条件。[[Open Platform Firmware (OPF)/Advancing Flash-less Boot in OCP Systems- A Streaming Firmware Architecture for Secure and Scalable.pdf#page=3|PDF p.3]][[Open Platform Firmware (OPF)/Advancing Flash-less Boot in OCP Systems- A Streaming Firmware Architecture for Secure and Scalable.pdf#page=4|PDF p.4]]
- 需验证 Early FW 顺序访问假设、eSPI时限、网络失效恢复、A/B回滚、可信服务端与集中式故障域；缺启动p99、缓存miss率、恢复成功率和BOM量化。
- 安全标准编号与厂商部署案例仅为演讲陈述，本文未查验外部规范/案例。

