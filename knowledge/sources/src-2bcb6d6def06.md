---
id: "src-2bcb6d6def06"
type: "source"
title: "Defining-End-to-End-800VDC-System-Performance-Requirements"
source_path: "ai-open-dc-power-distribution/Defining-End-to-End-800VDC-System-Performance-Requirements.pdf"
source_git_blob_sha: "39a869c312069f4f5b3147af0968033f47d429ca"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 18
review_status: "analyzed-visual"
evidence_pages: [2, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
text_reviewed: true
key_pages_visual_checked: [2, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16]
tags: ["ocp2026", "source", "power-cooling"]
concepts: ["[[knowledge/concepts/power-cooling-grid-to-chip-contract|电网到芯片接口契约]]", "[[knowledge/concepts/power-cooling-capacity-evidence-ladder|容量证据分级]]"]
---

# 端到端 800 V 接口：阻抗、储能、耐受曲线与启动状态机

> 原始题名：Defining-End-to-End-800VDC-System-Performance-Requirements。阅读范围：完整可提取文字（物理 PDF 共 18 页），关键引用图表另做视觉核对。

## 核心结论

- NVIDIA 将设施源、分配阻抗和机架输入定义为接口边界：800 V 电压相同仍不足以保证互操作，必须公开输入阻抗、传递函数、动态负载及源控制模型。 [[ai-open-dc-power-distribution/Defining-End-to-End-800VDC-System-Performance-Requirements.pdf#page=2|PDF p.2]]、[[ai-open-dc-power-distribution/Defining-End-to-End-800VDC-System-Performance-Requirements.pdf#page=3|PDF p.3]]、[[ai-open-dc-power-distribution/Defining-End-to-End-800VDC-System-Performance-Requirements.pdf#page=7|PDF p.7]]、[[ai-open-dc-power-distribution/Defining-End-to-End-800VDC-System-Performance-Requirements.pdf#page=17|PDF p.17]]
- 储能位置随所处理事件变化：机架附近处理快速动态与短保持，整流/SST+ESS 处理更慢的功率摆动，长时备电另需能量预算；不应把不同时间尺度的 J/kW 混成一个容量值。 [[ai-open-dc-power-distribution/Defining-End-to-End-800VDC-System-Performance-Requirements.pdf#page=5|PDF p.5]]
- 输入电容和配电电感共同影响稳定性；更多电容也会改变谐振及瞬态，需同时做小信号、负载阶跃、电压耐受与硬件验证。 [[ai-open-dc-power-distribution/Defining-End-to-End-800VDC-System-Performance-Requirements.pdf#page=9|PDF p.9]]、[[ai-open-dc-power-distribution/Defining-End-to-End-800VDC-System-Performance-Requirements.pdf#page=10|PDF p.10]]、[[ai-open-dc-power-distribution/Defining-End-to-End-800VDC-System-Performance-Requirements.pdf#page=11|PDF p.11]]、[[ai-open-dc-power-distribution/Defining-End-to-End-800VDC-System-Performance-Requirements.pdf#page=12|PDF p.12]]
- 启动状态机纳入绝缘、互锁、冷却温度、反灌及缓启动；多个阈值和远程命令仍为 TBD，是讨论稿而非可直接部署的规范。 [[ai-open-dc-power-distribution/Defining-End-to-End-800VDC-System-Performance-Requirements.pdf#page=13|PDF p.13]]、[[ai-open-dc-power-distribution/Defining-End-to-End-800VDC-System-Performance-Requirements.pdf#page=17|PDF p.17]]

## 关键证据

| 主张与信息 | 类型、边界与架构含义 | 原始出处 |
| --- | --- | --- |
| 95 kW DC/DC 电源架模型 | 区分 4-makes-3 正常与失去冗余的功率；输入阻抗含 measured/fitted 曲线，但整站验证仍列后续步骤。 | [[ai-open-dc-power-distribution/Defining-End-to-End-800VDC-System-Performance-Requirements.pdf#page=7\|PDF p.7]]、[[ai-open-dc-power-distribution/Defining-End-to-End-800VDC-System-Performance-Requirements.pdf#page=12\|PDF p.12]] |
| 耐受时间—电压曲线 V2 | 包含浪涌、感性开断夹持、正常运行与可能掉输出但不损伤区域；是否保持 IT 服务不能由“不损伤”推断。 | [[ai-open-dc-power-distribution/Defining-End-to-End-800VDC-System-Performance-Requirements.pdf#page=8\|PDF p.8]] |
| 人体防护和接地页 | p.14 PPE 表明确基于 2012 NFPA 70E 且备注 2015 无 Cat 0，不能作为现行 PPE 指引；p.16 图标题 High Resistance Return 与表头 Midpoint 不一致，需作者澄清。 | [[ai-open-dc-power-distribution/Defining-End-to-End-800VDC-System-Performance-Requirements.pdf#page=14\|PDF p.14]]、[[ai-open-dc-power-distribution/Defining-End-to-End-800VDC-System-Performance-Requirements.pdf#page=15\|PDF p.15]]、[[ai-open-dc-power-distribution/Defining-End-to-End-800VDC-System-Performance-Requirements.pdf#page=16\|PDF p.16]] |

## 指标与条件

| 指标 | 数值与单位 | 对象、条件、基线及缺失项 | 原始页 |
| --- | --- | --- | --- |
| 电源架功率 | 4M3 峰值/稳态/空闲 92.6/71.3/20.0 kW；非冗余 123.5/95.0/26.6 kW | 作者示例；不是整机架 GPU 净功率，不能用峰值持续运行。 | [[ai-open-dc-power-distribution/Defining-End-to-End-800VDC-System-Performance-Requirements.pdf#page=7\|PDF p.7]] |
| 输入接口 | 每 whip 电流斜率 0.6 A/µs；典型输入电容 26 µF/kW | 与指定转换器/配电模型绑定，不是所有 800 V 设备统一标准。 | [[ai-open-dc-power-distribution/Defining-End-to-End-800VDC-System-Performance-Requirements.pdf#page=7\|PDF p.7]]、[[ai-open-dc-power-distribution/Defining-End-to-End-800VDC-System-Performance-Requirements.pdf#page=10\|PDF p.10]] |
| 稳定性示例要求 | 最小 12 µF/kW @62.4 µH；最大配电电感 250 µH/125 A whip、5 µH/1 MW block | 作者表中不同聚合边界；不可互相替换或直接推出任意线缆最大长度。 | [[ai-open-dc-power-distribution/Defining-End-to-End-800VDC-System-Performance-Requirements.pdf#page=10\|PDF p.10]] |
| 启动提案 | 10 s walk-in，至少 1024 步；输入 800 V ±5% | 绝缘、电流差和连接器温度等仍 TBD；液体入口 <45°C/出口 <85°C 是该提案条件，不是通用冷却上限。 | [[ai-open-dc-power-distribution/Defining-End-to-End-800VDC-System-Performance-Requirements.pdf#page=13\|PDF p.13]] |

## 图表与架构

已核对 p.2、4–11、13–16 所有主要图像页。p.4 的 EDPP 标注 150%/50 ms、180%/400 µs，但左图横轴仅数毫秒，属于示意且时间标尺不一致，不能当实测脉冲。p.6 母排几何/趋肤效应示例缺少完整频率和几何条件，不外推约 44% 为所有母排收益。p.13 Fault 行的 IMD 阈值方向与 TurnOn 同写 Greater than TBD，需确认故障判据，不能照抄进保护逻辑。

## 关联与比较

- [[knowledge/concepts/power-cooling-time-scales-and-control-authority]]

- [[knowledge/concepts/power-cooling-grid-to-chip-contract|电网到芯片接口契约]]
- [[knowledge/concepts/power-cooling-capacity-evidence-ladder|容量证据分级]]

## 不确定性与待验证

- 输入阻抗是否覆盖全部负载、温度、模块失效和不同控制模式？
- 供应商能否发布开放模型、测量校准和可重复的大/小信号测试？
- 耐受曲线、启动阈值与接地术语冲突解决后，如何形成版本化互操作验收？

## 来源与版本

- [GitHub 原始文件（固定提交）](https://github.com/microarch-flow/OCP-2026/blob/d6e362b7bb1e65327b9ff005e9b55b5850ccbb34/ai-open-dc-power-distribution/Defining-End-to-End-800VDC-System-Performance-Requirements.pdf)
- 来源身份 `src-2bcb6d6def06`；Git blob `39a869c312069f4f5b3147af0968033f47d429ca`；原始物理页数 `18`。
- 原始文件保持不变；本文为中文分析，不是讲者认可或独立实验复现。
