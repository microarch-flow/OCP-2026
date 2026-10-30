---
id: power-cooling-capacity-evidence-ladder
type: concept
title: "容量证据阶梯：从组件规格到可交付机架"
tags: ["ocp2026", "power-cooling", "cross-source"]
---

# 容量证据阶梯：从组件规格到可交付机架

## 定义

“可支持多少kW”至少可能指机械承载、母排额定、冷板试验、全机架热稳定、故障降额运行或现场可用计算容量。不同层级的数字不能互相替代。

## 具体证据

- ORW展示4700kg负载机械验证与高功率母排方案；机械假负载DVT不是通电AI机架的热/电联合认证。[[knowledge/sources/src-42ab3107064a|Open Rack Wide (ORW)- Progress, Validation, and What's Next]] [[Rack & Power/Open Rack Wide (ORW)- Progress, Validation, and What's Next.pdf#page=6|PDF p.6]] [[Rack & Power/Open Rack Wide (ORW)- Progress, Validation, and What's Next.pdf#page=9|PDF p.9]]。
- 900mm风冷通用计算方案的650–1000W+定位和风扇效率改善，仍需机架验证；风扇W/kW改善不是服务器或机房总能耗同幅下降。[[knowledge/sources/src-8d543d42bc2d|Air-vs.-Liquid-Where-Does-Air-Cooling-Still-Win-for-General-Compute]] [[cooling-environments/Air-vs.-Liquid-Where-Does-Air-Cooling-Still-Win-for-General-Compute.pdf#page=5|PDF p.5]] [[cooling-environments/Air-vs.-Liquid-Where-Does-Air-Cooling-Still-Win-for-General-Compute.pdf#page=8|PDF p.8]]。
- 448G线缆液冷展示局部500W负载的仿真/实验；QD额外压降、插拔寿命和系统验证仍决定能否部署。[[knowledge/sources/src-f2ef9034c487|Cooling the 448G Frontier- Thermal Architecture for 500 W-Class HSIO Using Direct-to-Chip]] [[Cooling：Cold Plate/Cooling the 448G Frontier- Thermal Architecture for 500 W-Class HSIO Using Direct-to-Chip.pdf#page=10|PDF p.10]] [[Cooling：Cold Plate/Cooling the 448G Frontier- Thermal Architecture for 500 W-Class HSIO Using Direct-to-Chip.pdf#page=12|PDF p.12]]。
- CDU资格流程从PRD、接液兼容性、关键部件、测试、供应链到质量发布，表明性能数字只是资格证据的一部分。[[knowledge/sources/src-4b654daec9df|02_Cooling Distribution Unit Sub-Project Overview and Updates]] [[cooling-environments/02_Cooling Distribution Unit Sub-Project Overview and Updates.pdf#page=4|PDF p.4]]。

## 统一审阅问题（综合判断）

每个能力数字旁都应记录：**对象→工作负载/热图→边界温度/电压→持续时长→冗余态→测试方式→样本量→量产/现场状态**。没有这些条件的数字可以作为需求或目标，不宜直接进入容量承诺。

## 与生命周期的连接

可靠性余量可能在气候变化下逐渐缩小，而历史PUE/无停机记录仍看似正常；容量承诺应考虑场址极端条件和共同原因失效。[[knowledge/sources/src-5f7823cd7b2b|Climate Volatility in Daily Operations,  A Community Conversation with Operators, Hyperscalers]] [[Sustainability/Climate Volatility in Daily Operations,  A Community Conversation with Operators, Hyperscalers.pdf#page=5|PDF p.5]] [[Sustainability/Climate Volatility in Daily Operations,  A Community Conversation with Operators, Hyperscalers.pdf#page=6|PDF p.6]]。制造碳/水边界也需要独立定义，不能将机架制造阶段PCR与运行期排放相混。[[knowledge/sources/src-61f01ce4a478|Product Category Rule-style Specification for Life Cycle Assessment on Datacenter ICT-Equipment]] [[Sustainability/Product Category Rule-style Specification for Life Cycle Assessment on Datacenter ICT-Equipment.pdf#page=3|PDF p.3]]；[[knowledge/sources/src-b13993092777|Closing the Visibility Gap- An AI-Driven Supply Chain Intelligence Framework for Water Stewardship]] [[Sustainability/Closing the Visibility Gap- An AI-Driven Supply Chain Intelligence Framework for Water Stewardship.pdf#page=12|PDF p.12]]。

## 未决问题

缺少从样机→量产→现场长期统计的一致追踪链，以及把热/电降额转换为有效计算容量和合同可用性的模型。这个证据阶梯用于识别缺口，不否定已展示的局部工程价值。

