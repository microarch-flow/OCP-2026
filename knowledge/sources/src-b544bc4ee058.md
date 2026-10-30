---
id: "src-b544bc4ee058"
type: "source"
title: "Pushing the Single-Phase Cold Plate Limit"
source_path: "Cooling：Cold Plate/Pushing the Single-Phase Cold Plate Limit.pdf"
source_git_blob_sha: "3396682b10abbd6e934f85a99b66dade037ff6b7"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 29
review_status: "analyzed-visual"
evidence_pages: [8, 9, 10, 11, 12, 13, 14, 16, 19, 20, 21, 22, 23, 24, 25, 27, 28]
text_reviewed: true
key_pages_visual_checked: [10, 11, 12, 16, 21, 27]
tags: ["ocp2026", "source", "power-cooling", "cold-plate", "co-design"]
concepts: []
---

# 推动单相冷板边界：芯片热图、接口热阻与全回路协同

> 原始题名：Pushing the Single-Phase Cold Plate Limit。阅读范围：完整可提取文字（物理 PDF 共 29 页），关键引用图表另做视觉核对。

## 核心结论

- 29页文件含人物介绍p.1–7、Microsoft单元冷板p.8–12、Corintis微流体p.13–19、Google系统实践p.20–24、Meta全栈约束p.25–29；不是一组统一对照试验。 [[Cooling：Cold Plate/Pushing the Single-Phase Cold Plate Limit.pdf#page=8|PDF p.8]]、[[Cooling：Cold Plate/Pushing the Single-Phase Cold Plate Limit.pdf#page=13|PDF p.13]]、[[Cooling：Cold Plate/Pushing the Single-Phase Cold Plate Limit.pdf#page=20|PDF p.20]]、[[Cooling：Cold Plate/Pushing the Single-Phase Cold Plate Limit.pdf#page=25|PDF p.25]]
- 共同方向是把均匀整片鳍片改为匹配芯片异质热点的短流道/并行单元与定向流量；需要芯片floorplan、封装、TIM和冷板联合优化。 [[Cooling：Cold Plate/Pushing the Single-Phase Cold Plate Limit.pdf#page=9|PDF p.9]]、[[Cooling：Cold Plate/Pushing the Single-Phase Cold Plate Limit.pdf#page=10|PDF p.10]]、[[Cooling：Cold Plate/Pushing the Single-Phase Cold Plate Limit.pdf#page=12|PDF p.12]]、[[Cooling：Cold Plate/Pushing the Single-Phase Cold Plate Limit.pdf#page=14|PDF p.14]]、[[Cooling：Cold Plate/Pushing the Single-Phase Cold Plate Limit.pdf#page=21|PDF p.21]]、[[Cooling：Cold Plate/Pushing the Single-Phase Cold Plate Limit.pdf#page=22|PDF p.22]]
- 冷板之外，TIM/翘曲、硅内扩散、QD压降、过滤、化学管理、材料长期蠕变和供应链良率都可能成为扩容约束；单点热阻改善不等于整机房成本下降。 [[Cooling：Cold Plate/Pushing the Single-Phase Cold Plate Limit.pdf#page=22|PDF p.22]]、[[Cooling：Cold Plate/Pushing the Single-Phase Cold Plate Limit.pdf#page=23|PDF p.23]]、[[Cooling：Cold Plate/Pushing the Single-Phase Cold Plate Limit.pdf#page=24|PDF p.24]]、[[Cooling：Cold Plate/Pushing the Single-Phase Cold Plate Limit.pdf#page=27|PDF p.27]]、[[Cooling：Cold Plate/Pushing the Single-Phase Cold Plate Limit.pdf#page=28|PDF p.28]]

## 关键证据

| 主张与信息 | 类型、边界与架构含义 | 原始出处 |
| --- | --- | --- |
| Microsoft单元冷板报告最高10°C结温下降 | 讲者原型测量；未给完整功率、入口温度、流量及重复性，不与其他供应商直接排名。 | [[Cooling：Cold Plate/Pushing the Single-Phase Cold Plate Limit.pdf#page=11\|PDF p.11]] |
| Corintis H200同流体/流量/测试架对比 | 供应商实验结果；比的是结到入口温升，不是摄氏绝对温度的百分比或性能提升。 | [[Cooling：Cold Plate/Pushing the Single-Phase Cold Plate Limit.pdf#page=16\|PDF p.16]] |
| Meta热阻分解随翘曲/功率密度变化 | 示意案例展示瓶颈迁移；无对应芯片/载荷标识，不应作为普适分摊比例。 | [[Cooling：Cold Plate/Pushing the Single-Phase Cold Plate Limit.pdf#page=27\|PDF p.27]] |

## 指标与条件

| 指标 | 数值与单位 | 对象、条件、基线及缺失项 | 原始页 |
| --- | --- | --- | --- |
| H200 GPU结到入口温升 | 29.5→23.9°C，约−19% | skived vs microfluidic；同1 LPM、同流体与试验架；功率、入口温度、压降未列。 | [[Cooling：Cold Plate/Pushing the Single-Phase Cold Plate Limit.pdf#page=16\|PDF p.16]] |
| H200 HBM结到入口温升 | 42.0→32.4°C，约−23% | 同一供应商试验；不能直接推导HBM频率或节电。 | [[Cooling：Cold Plate/Pushing the Single-Phase Cold Plate Limit.pdf#page=16\|PDF p.16]] |
| 高分辨率TTV方案 | 2kW、240通道电源、2×2mm像素 | Corintis工具能力宣称，用于非均匀热图验证；非冷板系统极限。 | [[Cooling：Cold Plate/Pushing the Single-Phase Cold Plate Limit.pdf#page=19\|PDF p.19]] |

## 图表与架构

视觉核对p.10、11、12、16、21、27。p.12明确是假设处理器热图；p.10入口区150倍Nu/约6倍HTC的关系缺少转换条件，不作为全冷板提升倍数。p.27图示基例硅/TIM/冷板35/20/45%，翘曲或功率密度改变后占比变化，不能固定套用。

## 关联与比较

- [[knowledge/comparisons/power-cooling-single-vs-two-phase]]
- 本条先保留来源级证据；跨源比较应检查工作负载、系统边界、实验条件和时间尺度，不能仅按标题归类后推导性能优劣。

## 不确定性与待验证

- 比较需要相同芯片功率图、TIM/夹紧、入口温度、泵功或压降约束、制造成本与良率。
- 供应商标注的量产百万件/年、较低温度等没有独立生产或寿命数据支持。

## 来源与版本

- [GitHub 原始文件（固定提交）](https://github.com/microarch-flow/OCP-2026/blob/d6e362b7bb1e65327b9ff005e9b55b5850ccbb34/Cooling%EF%BC%9ACold%20Plate/Pushing%20the%20Single-Phase%20Cold%20Plate%20Limit.pdf)
- 来源身份 `src-b544bc4ee058`；Git blob `3396682b10abbd6e934f85a99b66dade037ff6b7`；原始物理页数 `29`。
- 原始文件保持不变；本文为中文分析，不是讲者认可或独立实验复现。
