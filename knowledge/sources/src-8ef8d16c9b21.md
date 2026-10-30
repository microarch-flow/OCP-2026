---
id: "src-8ef8d16c9b21"
type: "source"
title: "Fluid Velocity and Erosion Updates"
source_path: "Cooling：Cold Plate/Fluid Velocity and Erosion Updates.pdf"
source_git_blob_sha: "2b4639eb80ab374fa34353eaddc002702a2e8cab"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 25
review_status: "analyzed-visual"
evidence_pages: [2, 4, 5, 6, 7, 9, 12, 14, 15, 17, 18, 21, 22, 23, 24]
text_reviewed: true
key_pages_visual_checked: [4, 5, 6, 15, 22]
tags: ["ocp2026", "source", "power-cooling", "fluid", "erosion"]
concepts: []
---

# 高流速 PG25：没有宏观侵蚀不等于保护膜没有余量损失

> 原始题名：Fluid Velocity and Erosion Updates。阅读范围：完整可提取文字（物理 PDF 共 25 页），关键引用图表另做视觉核对。

## 核心结论

- 此文件是两段合编：p.1–17为Castrol/Meta高流速铜管试验与失效分析；p.18–25为SABIC热塑性材料加速筛选方法，后者结果尚未完成。 [[Cooling：Cold Plate/Fluid Velocity and Erosion Updates.pdf#page=2|PDF p.2]]、[[Cooling：Cold Plate/Fluid Velocity and Erosion Updates.pdf#page=17|PDF p.17]]、[[Cooling：Cold Plate/Fluid Velocity and Erosion Updates.pdf#page=18|PDF p.18]]、[[Cooling：Cold Plate/Fluid Velocity and Erosion Updates.pdf#page=23|PDF p.23]]、[[Cooling：Cold Plate/Fluid Velocity and Erosion Updates.pdf#page=24|PDF p.24]]
- 在特定PG25、铜管和93天试验中未观测到可分辨的宏观减薄，但弯头的有机/azole保护膜比直管薄。流速能力应绑定几何、化学状态、时间及检测分辨率，而非推广成PG25通用安全上限。 [[Cooling：Cold Plate/Fluid Velocity and Erosion Updates.pdf#page=4|PDF p.4]]、[[Cooling：Cold Plate/Fluid Velocity and Erosion Updates.pdf#page=5|PDF p.5]]、[[Cooling：Cold Plate/Fluid Velocity and Erosion Updates.pdf#page=14|PDF p.14]]、[[Cooling：Cold Plate/Fluid Velocity and Erosion Updates.pdf#page=15|PDF p.15]]
- 浊度升高而电导率/pH相对平稳，后续颗粒分析发现试验场地带入污染；单项流体遥测不能证明回路洁净。 [[Cooling：Cold Plate/Fluid Velocity and Erosion Updates.pdf#page=6|PDF p.6]]、[[Cooling：Cold Plate/Fluid Velocity and Erosion Updates.pdf#page=7|PDF p.7]]

## 关键证据

| 主张与信息 | 类型、边界与架构含义 | 原始出处 |
| --- | --- | --- |
| 超声壁厚测量中途更换传感器 | 更换前波动显著；原文结论限定在更换后仪器变化范围内稳定，不是零侵蚀的高精度证明。 | [[Cooling：Cold Plate/Fluid Velocity and Erosion Updates.pdf#page=5\|PDF p.5]] |
| XPS显示弯头膜薄、硫化物信号更显著 | 讲者基于表面分析的机制解释；MIC为潜在指标而非已证明微生物根因，铅来源也属推测。 | [[Cooling：Cold Plate/Fluid Velocity and Erosion Updates.pdf#page=9\|PDF p.9]]、[[Cooling：Cold Plate/Fluid Velocity and Erosion Updates.pdf#page=12\|PDF p.12]]、[[Cooling：Cold Plate/Fluid Velocity and Erosion Updates.pdf#page=14\|PDF p.14]]、[[Cooling：Cold Plate/Fluid Velocity and Erosion Updates.pdf#page=15\|PDF p.15]] |
| 热塑性材料采用ASTM D543浸泡与施加应变筛选 | 研究提案；需要与流动、污染物、长期服役建立关联，计划首轮2027Q1完成。 | [[Cooling：Cold Plate/Fluid Velocity and Erosion Updates.pdf#page=21\|PDF p.21]]、[[Cooling：Cold Plate/Fluid Velocity and Erosion Updates.pdf#page=22\|PDF p.22]]、[[Cooling：Cold Plate/Fluid Velocity and Erosion Updates.pdf#page=23\|PDF p.23]]、[[Cooling：Cold Plate/Fluid Velocity and Erosion Updates.pdf#page=24\|PDF p.24]] |

## 指标与条件

| 指标 | 数值与单位 | 对象、条件、基线及缺失项 | 原始页 |
| --- | --- | --- | --- |
| 铜管试验 | 6.2 m/s；2232小时（93天）；内径25.4mm、壁厚1.65mm | Castrol ON DLC PG25；C12200/H58、未预钝化；页面未充分给出运行温度分布。 | [[Cooling：Cold Plate/Fluid Velocity and Erosion Updates.pdf#page=4\|PDF p.4]] |
| 溶解铜 | 各取样日均<1 ppm | ASTM D6130；不等于表面保护层没有变化。 | [[Cooling：Cold Plate/Fluid Velocity and Erosion Updates.pdf#page=6\|PDF p.6]] |
| 有机/azole膜 | 弯头约8nm、直管约35nm，约4.4倍差异 | 讲者XPS深度分析解释；不是管壁厚度或剩余寿命。 | [[Cooling：Cold Plate/Fluid Velocity and Erosion Updates.pdf#page=15\|PDF p.15]] |
| 聚合物筛选 | 23°C 7天，0/0.5/1%应变；扩展80°C 14/42天、0/1% | 初始及计划扩展条件，不代表合格寿命。 | [[Cooling：Cold Plate/Fluid Velocity and Erosion Updates.pdf#page=22\|PDF p.22]] |

## 图表与架构

视觉检查p.4、5、6、15、22。保留壁厚曲线的传感器更换事件与不确定性；没有把浊度变化直接归因铜腐蚀。XPS峰图未逐峰独立重拟合，化学态与膜厚为讲者解释。

## 关联与比较

- [[knowledge/concepts/power-cooling-fluid-assurance]]
- 本条先保留来源级证据；跨源比较应检查工作负载、系统边界、实验条件和时间尺度，不能仅按标题归类后推导性能优劣。

## 不确定性与待验证

- 需更长暴露、多流速/温度/几何/配方的复现实验。
- 尚无泵功、系统节能或经济性数据；“提高流速更节能”不能从本试验直接量化。

## 来源与版本

- [GitHub 原始文件（固定提交）](https://github.com/microarch-flow/OCP-2026/blob/d6e362b7bb1e65327b9ff005e9b55b5850ccbb34/Cooling%EF%BC%9ACold%20Plate/Fluid%20Velocity%20and%20Erosion%20Updates.pdf)
- 来源身份 `src-8ef8d16c9b21`；Git blob `2b4639eb80ab374fa34353eaddc002702a2e8cab`；原始物理页数 `25`。
- 原始文件保持不变；本文为中文分析，不是讲者认可或独立实验复现。
