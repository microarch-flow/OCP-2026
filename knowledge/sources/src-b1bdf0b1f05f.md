---
id: "src-b1bdf0b1f05f"
type: "source"
title: "Integrating-Solid-State-Transformer-to-Data-Center-LVDC-Ecosystem"
source_path: "ai-open-dc-power-distribution/Integrating-Solid-State-Transformer-to-Data-Center-LVDC-Ecosystem.pdf"
source_git_blob_sha: "9ad96481ff07c12afb86382c361f43c7a425724c"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 11
review_status: "analyzed-visual"
evidence_pages: [4, 6, 7, 8, 9, 10]
text_reviewed: true
key_pages_visual_checked: [6, 7, 8]
tags: ["ocp2026", "source", "power-cooling", "sst", "lvdc", "energy-storage"]
concepts: []
---

# SST融入LVDC：集中转换、储能与800V接口提案

> 原始题名：Integrating-Solid-State-Transformer-to-Data-Center-LVDC-Ecosystem。阅读范围：完整可提取文字（物理 PDF 共 11 页），关键引用图表另做视觉核对。

## 核心结论

- Google/NVIDIA将SST、储能、DC配电和DC保护视为共同架构；集中转换旨在释放机房空间，集中储能同时支撑电网穿越和AI负载波动。 [[ai-open-dc-power-distribution/Integrating-Solid-State-Transformer-to-Data-Center-LVDC-Ecosystem.pdf#page=4|PDF p.4]]、[[ai-open-dc-power-distribution/Integrating-Solid-State-Transformer-to-Data-Center-LVDC-Ecosystem.pdf#page=6|PDF p.6]]
- Rev0.3在800V单极输出与基础性能上对齐，在中压输入/功率档位上保留两类SKU；这是规范工作进展，不是已交付SST实测。 [[ai-open-dc-power-distribution/Integrating-Solid-State-Transformer-to-Data-Center-LVDC-Ecosystem.pdf#page=7|PDF p.7]]、[[ai-open-dc-power-distribution/Integrating-Solid-State-Transformer-to-Data-Center-LVDC-Ecosystem.pdf#page=8|PDF p.8]]
- 分布冗余与Catcher是并列候选，文件未给二者可用性、成本或故障统计，不能据此判定优劣。 [[ai-open-dc-power-distribution/Integrating-Solid-State-Transformer-to-Data-Center-LVDC-Ecosystem.pdf#page=6|PDF p.6]]

## 关键证据

| 主张与信息 | 类型、边界与架构含义 | 原始出处 |
| --- | --- | --- |
| 集中转换置于DCH外，合并大量机架电池为row-level备份 | 讲者架构诉求；故障域、维护隔离和储能控制仍需系统设计 | [[ai-open-dc-power-distribution/Integrating-Solid-State-Transformer-to-Data-Center-LVDC-Ecosystem.pdf#page=4\|PDF p.4]] |
| 储能服务AC侧LVRT/爬坡、负载侧备份/功率波动两个方向 | 不能把所有储能容量仅按IT断电续航计算；无量化分配方案 | [[ai-open-dc-power-distribution/Integrating-Solid-State-Transformer-to-Data-Center-LVDC-Ecosystem.pdf#page=6\|PDF p.6]] |
| 后续规范仍需AC/DC接口、遥测、MFT局放、网络和LVDC波动控制 | 说明关键互操作和可靠性条款仍在定义 | [[ai-open-dc-power-distribution/Integrating-Solid-State-Transformer-to-Data-Center-LVDC-Ecosystem.pdf#page=9\|PDF p.9]]、[[ai-open-dc-power-distribution/Integrating-Solid-State-Transformer-to-Data-Center-LVDC-Ecosystem.pdf#page=10\|PDF p.10]] |

## 指标与条件

| 指标 | 数值与单位 | 对象、条件、基线及缺失项 | 原始页 |
| --- | --- | --- | --- |
| 输出与调节目标 | 800 Vdc单极；开关频率纹波±0.5%，静态±1%，动态±3%（TBD） | Rev0.3提案，动态项未定；非实测波形 | [[ai-open-dc-power-distribution/Integrating-Solid-State-Transformer-to-Data-Center-LVDC-Ecosystem.pdf#page=7\|PDF p.7]] |
| 效率/过载/爬坡目标 | 效率≥98%（50–100%负载）；120%持续5 s；150%约150 ms用于下游保护；20–50 MW/min | SST规范要求；未给温度、寿命、全范围效率、保护选择性实测 | [[ai-open-dc-power-distribution/Integrating-Solid-State-Transformer-to-Data-Center-LVDC-Ecosystem.pdf#page=7\|PDF p.7]] |
| SKU A | 13.8 kVac±10%；DC输出5 MW | 中压侧接口候选；短路电流能力条目不能误当成DC负载故障电流 | [[ai-open-dc-power-distribution/Integrating-Solid-State-Transformer-to-Data-Center-LVDC-Ecosystem.pdf#page=8\|PDF p.8]] |
| SKU B | 34.5 kVac±10%；DC输出5或10 MW | 两SKU服务不同hyperscaler中压接入，非机架额定功率 | [[ai-open-dc-power-distribution/Integrating-Solid-State-Transformer-to-Data-Center-LVDC-Ecosystem.pdf#page=8\|PDF p.8]] |
| 接地 | Ungrounded或HRG，要求接地故障检测 | 架构选项而非无需保护；具体接地/人身安全设计未完成 | [[ai-open-dc-power-distribution/Integrating-Solid-State-Transformer-to-Data-Center-LVDC-Ecosystem.pdf#page=7\|PDF p.7]] |

## 图表与架构

已核对 p.6 两种冗余架构、p.7 Rev0.3对齐参数和 p.8 两SKU。p.6较小的电路细节不用于推导未经披露的开关时序；p.5 LVRT曲线尚未核查，不引用其坐标。

## 关联与比较

- 本条先保留来源级证据；跨源比较应检查工作负载、系统边界、实验条件和时间尺度，不能仅按标题归类后推导性能优劣。

## 不确定性与待验证

- 未给SST产品MTBF、现场维修时间、系统可用性和效率实测，不把集中化等同于可靠性提升。
- 没有设施面积成本、转换器成本、冗余/储能资本支出或利用率，不计算TCO。
- 下一步证据是训练/推理负载库、中压电源质量用例和故障保护协同测试。

## 来源与版本

- [GitHub 原始文件（固定提交）](https://github.com/microarch-flow/OCP-2026/blob/d6e362b7bb1e65327b9ff005e9b55b5850ccbb34/ai-open-dc-power-distribution/Integrating-Solid-State-Transformer-to-Data-Center-LVDC-Ecosystem.pdf)
- 来源身份 `src-b1bdf0b1f05f`；Git blob `9ad96481ff07c12afb86382c361f43c7a425724c`；原始物理页数 `11`。
- 原始文件保持不变；本文为中文分析，不是讲者认可或独立实验复现。
