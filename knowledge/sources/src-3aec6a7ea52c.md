---
id: "src-3aec6a7ea52c"
type: "source"
title: "Caliptra 2.2 USB流式启动：共享物理链路、分离设备所有权"
source_path: "Security/Caliptra Subsystem 2.2- USB 2.0 and OCP Streaming Boot.pdf"
source_git_blob_sha: "2157b1b159f38bea2482362759e6f0ee5cb75830"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 17
review_status: "analyzed-visual"
evidence_pages: [4, 6, 7, 10, 11, 12, 13, 14, 16]
tags: ["ocp", "source", "platform", "security"]
text_reviewed: true
key_pages_visual_checked: [7, 13]
updated: "2026-10-30"
---

# Caliptra 2.2 USB流式启动：共享物理链路、分离设备所有权

> 阅读范围：已阅读本文件全部可提取文字（17页）。关键页已视觉核对：7, 13；不代表逐页视觉审核。

## 核心结论

- 2.2方案新增USB 2.0流式启动，同时保留I3C与AXI；启动时选streaming engine，不是用USB取消所有既有通道。[[Security/Caliptra Subsystem 2.2- USB 2.0 and OCP Streaming Boot.pdf#page=4|PDF p.4]][[Security/Caliptra Subsystem 2.2- USB 2.0 and OCP Streaming Boot.pdf#page=14|PDF p.14]]
- 单USB PHY+虚拟hub暴露两个独立所有权设备：Device 0属于RoT/MCU，Device 1属于SoC集成应用。[[Security/Caliptra Subsystem 2.2- USB 2.0 and OCP Streaming Boot.pdf#page=7|PDF p.7]][[Security/Caliptra Subsystem 2.2- USB 2.0 and OCP Streaming Boot.pdf#page=14|PDF p.14]]
- 启动恢复与运行时协议生命周期不同，不能把USB枚举成功当作SPDM/PLDM服务已就绪。[[Security/Caliptra Subsystem 2.2- USB 2.0 and OCP Streaming Boot.pdf#page=12|PDF p.12]][[Security/Caliptra Subsystem 2.2- USB 2.0 and OCP Streaming Boot.pdf#page=13|PDF p.13]]

## 关键证据

- Device 0 EP0提供OCP Recovery，Caliptra完成认证、测量、授权、激活；运行时Device 0可承载MCTP/SPDM/PLDM，Device 1可承载OBMF/MCTP等。[[Security/Caliptra Subsystem 2.2- USB 2.0 and OCP Streaming Boot.pdf#page=10|PDF p.10]][[Security/Caliptra Subsystem 2.2- USB 2.0 and OCP Streaming Boot.pdf#page=11|PDF p.11]][[Security/Caliptra Subsystem 2.2- USB 2.0 and OCP Streaming Boot.pdf#page=13|PDF p.13]]
- MCU先完成启动、通知SoC挂接Device 1，再reset/re-enumerate Device 0进入runtime-only。集成方必须在connect前配置资源，隔离reset/disconnect/transfer handling。[[Security/Caliptra Subsystem 2.2- USB 2.0 and OCP Streaming Boot.pdf#page=13|PDF p.13]][[Security/Caliptra Subsystem 2.2- USB 2.0 and OCP Streaming Boot.pdf#page=14|PDF p.14]]
- p.16仍写v2.2 coming soon并征集验证；因此本材料不能证明2.2正式发布或已通过全验证。[[Security/Caliptra Subsystem 2.2- USB 2.0 and OCP Streaming Boot.pdf#page=16|PDF p.16]]

## 指标与条件

USB 2.0是接口代际，两个设备是逻辑组织；“fewer pins, less power”未给引脚数/瓦数基线，不能换算PPA收益。[[Security/Caliptra Subsystem 2.2- USB 2.0 and OCP Streaming Boot.pdf#page=6|PDF p.6]][[Security/Caliptra Subsystem 2.2- USB 2.0 and OCP Streaming Boot.pdf#page=7|PDF p.7]]

## 图表与架构

已视觉核对p.7和13：USB PHY位于Caliptra子系统之外，hub内分Device 0/1；启动完成后的重新枚举是显式步骤。更细微架构p.8未视觉核对。

## 关联与比较

对系统架构有用的契约是所有权与故障隔离，而不只是带宽：共享PHY仍需保证一个设备的reset/运行时行为不会破坏另一所有权域。

## 不确定性与待验证

缺USB有效固件传输速度、重枚举延迟、启动失败恢复和独立reset测试矩阵。需查发布版RTL/固件与2.2验证结果。

