---
id: "src-e7f8c282fc7c"
type: "source"
title: "Simplifying High-Density Deployments- Reducing AC Whip Complexity in Multi-Power Shelves Open Rack"
source_path: "Rack & Power/Simplifying High-Density Deployments- Reducing AC Whip Complexity in Multi-Power Shelves Open Rack.pdf"
source_git_blob_sha: "5b67bdaa220dba9a90b3ecd16aac7ba668fdcc09"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 20
review_status: "analyzed-visual"
evidence_pages: [3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19]
text_reviewed: true
key_pages_visual_checked: [2, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18]
tags: ["ocp2026", "source", "power-cooling"]
concepts: ["[[knowledge/concepts/power-cooling-grid-to-chip-contract|电网到芯片接口契约]]", "[[knowledge/concepts/power-cooling-capacity-evidence-ladder|容量证据分级]]"]
---

# 减少 AC 馈线复杂度：模块化配电原型而非已证明的 TCO 改善

> 原始题名：Simplifying High-Density Deployments- Reducing AC Whip Complexity in Multi-Power Shelves Open Rack。阅读范围：完整可提取文字（物理 PDF 共 20 页），关键引用图表另做视觉核对。

## 核心结论

- Schneider 提供机架顶部横向模块与后部竖向 PDU 两种布置；目的在于把多电源架的长馈线转换为少量上游馈线和局部短跳线，并未消除下游电缆。 [[Rack & Power/Simplifying High-Density Deployments- Reducing AC Whip Complexity in Multi-Power Shelves Open Rack.pdf#page=4|PDF p.4]]、[[Rack & Power/Simplifying High-Density Deployments- Reducing AC Whip Complexity in Multi-Power Shelves Open Rack.pdf#page=6|PDF p.6]]、[[Rack & Power/Simplifying High-Density Deployments- Reducing AC Whip Complexity in Multi-Power Shelves Open Rack.pdf#page=15|PDF p.15]]
- 横向方案用一条 125 A 输入分到两条 60 A 电源架支路，示例可将 16 条上游馈线减至 8 条；这个计数不能直接套用到竖向方案。 [[Rack & Power/Simplifying High-Density Deployments- Reducing AC Whip Complexity in Multi-Power Shelves Open Rack.pdf#page=6|PDF p.6]]、[[Rack & Power/Simplifying High-Density Deployments- Reducing AC Whip Complexity in Multi-Power Shelves Open Rack.pdf#page=7|PDF p.7]]、[[Rack & Power/Simplifying High-Density Deployments- Reducing AC Whip Complexity in Multi-Power Shelves Open Rack.pdf#page=12|PDF p.12]]
- 原型照片证明机械实现，不证明保护选择性、维护工时或长期可靠性；Q1/Q3 2027 测试/量产仍是作者计划。 [[Rack & Power/Simplifying High-Density Deployments- Reducing AC Whip Complexity in Multi-Power Shelves Open Rack.pdf#page=11|PDF p.11]]、[[Rack & Power/Simplifying High-Density Deployments- Reducing AC Whip Complexity in Multi-Power Shelves Open Rack.pdf#page=13|PDF p.13]]、[[Rack & Power/Simplifying High-Density Deployments- Reducing AC Whip Complexity in Multi-Power Shelves Open Rack.pdf#page=17|PDF p.17]]、[[Rack & Power/Simplifying High-Density Deployments- Reducing AC Whip Complexity in Multi-Power Shelves Open Rack.pdf#page=19|PDF p.19]]

## 关键证据

| 主张与信息 | 类型、边界与架构含义 | 原始出处 |
| --- | --- | --- |
| 模块与机架安装 | 模块滑入底座；需要特定机架孔位/支架，不能当作所有 OCP 机架直接兼容。 | [[Rack & Power/Simplifying High-Density Deployments- Reducing AC Whip Complexity in Multi-Power Shelves Open Rack.pdf#page=8\|PDF p.8]]、[[Rack & Power/Simplifying High-Density Deployments- Reducing AC Whip Complexity in Multi-Power Shelves Open Rack.pdf#page=9\|PDF p.9]]、[[Rack & Power/Simplifying High-Density Deployments- Reducing AC Whip Complexity in Multi-Power Shelves Open Rack.pdf#page=10\|PDF p.10]] |
| 后部竖向 PDU | 需要同时评估液冷软管、网络布线、后维护及风路空间，不能仅按前视图判断可安装。 | [[Rack & Power/Simplifying High-Density Deployments- Reducing AC Whip Complexity in Multi-Power Shelves Open Rack.pdf#page=15\|PDF p.15]]、[[Rack & Power/Simplifying High-Density Deployments- Reducing AC Whip Complexity in Multi-Power Shelves Open Rack.pdf#page=16\|PDF p.16]]、[[Rack & Power/Simplifying High-Density Deployments- Reducing AC Whip Complexity in Multi-Power Shelves Open Rack.pdf#page=17\|PDF p.17]]、[[Rack & Power/Simplifying High-Density Deployments- Reducing AC Whip Complexity in Multi-Power Shelves Open Rack.pdf#page=18\|PDF p.18]] |
| 刀片级短路保护与 TCO | 摘要给功能主张；缺少分断额定值、协调曲线及含币种/工时/利用率的成本模型。 | [[Rack & Power/Simplifying High-Density Deployments- Reducing AC Whip Complexity in Multi-Power Shelves Open Rack.pdf#page=3\|PDF p.3]]、[[Rack & Power/Simplifying High-Density Deployments- Reducing AC Whip Complexity in Multi-Power Shelves Open Rack.pdf#page=19\|PDF p.19]] |

## 指标与条件

| 指标 | 数值与单位 | 对象、条件、基线及缺失项 | 原始页 |
| --- | --- | --- | --- |
| 横向配电示例 | 每输入 125 A → 2×60 A 支路；8 模块 | 电压、连续负载、环境降额和保护额定值须另核对，不仅比较电流相加。 | [[Rack & Power/Simplifying High-Density Deployments- Reducing AC Whip Complexity in Multi-Power Shelves Open Rack.pdf#page=6\|PDF p.6]] |
| 示例长馈线计数 | 16→8；四模块原型 8→4 | 仅适用于图示横向架构与所示电源架数量；下游短跳线仍存在。 | [[Rack & Power/Simplifying High-Density Deployments- Reducing AC Whip Complexity in Multi-Power Shelves Open Rack.pdf#page=7\|PDF p.7]]、[[Rack & Power/Simplifying High-Density Deployments- Reducing AC Whip Complexity in Multi-Power Shelves Open Rack.pdf#page=12\|PDF p.12]]、[[Rack & Power/Simplifying High-Density Deployments- Reducing AC Whip Complexity in Multi-Power Shelves Open Rack.pdf#page=13\|PDF p.13]] |
| 空间 | 模块宽约 72 mm；成组宽约 600 mm | 作者机械图；机架及安装支架必须留额外余量，不能用模块宽度代替完整外廓。 | [[Rack & Power/Simplifying High-Density Deployments- Reducing AC Whip Complexity in Multi-Power Shelves Open Rack.pdf#page=8\|PDF p.8]] |

## 图表与架构

已核对 p.2、6–13、15–18 的布置、尺寸与原型照片。p.18 竖向示意并未给出与横向相同的馈线减半结论，因此本卡不外推。

## 关联与比较

- [[knowledge/concepts/power-cooling-grid-to-chip-contract|电网到芯片接口契约]]
- [[knowledge/concepts/power-cooling-capacity-evidence-ladder|容量证据分级]]

## 不确定性与待验证

- 输入馈线及分支失效扩大了多少电源架的共同故障域？
- 带载维护、触电防护和支路故障分断如何验证？
- 以明确币种、机架数量、工时费率和生命周期计算，节约安装工时是否抵消新增 PDU 与维护成本？

## 来源与版本

- [GitHub 原始文件（固定提交）](https://github.com/microarch-flow/OCP-2026/blob/d6e362b7bb1e65327b9ff005e9b55b5850ccbb34/Rack%20%26%20Power/Simplifying%20High-Density%20Deployments-%20Reducing%20AC%20Whip%20Complexity%20in%20Multi-Power%20Shelves%20Open%20Rack.pdf)
- 来源身份 `src-e7f8c282fc7c`；Git blob `5b67bdaa220dba9a90b3ecd16aac7ba668fdcc09`；原始物理页数 `20`。
- 原始文件保持不变；本文为中文分析，不是讲者认可或独立实验复现。
