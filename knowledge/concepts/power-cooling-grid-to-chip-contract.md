---
id: power-cooling-grid-to-chip-contract
type: concept
title: "从电网到芯片的功率合同：额定 kW 之外的动态与故障边界"
tags: ["ocp2026", "power-cooling", "cross-source"]
---

# 从电网到芯片的功率合同：额定 kW 之外的动态与故障边界

## 定义

容量交付应同时描述稳态功率、负载变化、储能响应、故障选择性、恢复时序和必要冷却。以下为多份演讲的综合设计框架，不能替代当地规范或合格电气工程设计。

## 来源与页级证据

- 电网侧对大负荷提出电压扰动穿越及恢复/功率变化要求；演讲包含建议性政策框架，不是全球通用规则。[[knowledge/sources/src-668ba0e19bdd|Grid-Requirements-and-Mitigation-options-for-Large-Scale-AI-ML-Loads]] [[ai-open-dc-power-distribution/Grid-Requirements-and-Mitigation-options-for-Large-Scale-AI-ML-Loads.pdf#page=6|PDF p.6]]。
- SST方案把AC/DC转换、800V母线和储能连接起来，但效率、过载和动态指标主要是设计目标。[[knowledge/sources/src-b1bdf0b1f05f|Integrating-Solid-State-Transformer-to-Data-Center-LVDC-Ecosystem]] [[ai-open-dc-power-distribution/Integrating-Solid-State-Transformer-to-Data-Center-LVDC-Ecosystem.pdf#page=6|PDF p.6]] [[ai-open-dc-power-distribution/Integrating-Solid-State-Transformer-to-Data-Center-LVDC-Ecosystem.pdf#page=7|PDF p.7]]。
- 板上50V/12V模块提出不同效率与瞬态目标，单模块效率不能乘以不存在的满载一致条件后宣称系统收益。[[knowledge/sources/src-7371e57b6934|400V-800V-On-Board-Power-Delivery-Requirements]] [[ai-open-dc-power-distribution/400V-800V-On-Board-Power-Delivery-Requirements.pdf#page=10|PDF p.10]]。
- 故障能量依赖限流、反向阻断、储能/电容放电与保护清除时间；电压本身既不能证明危险消失，也不能独立决定弧闪强度。[[knowledge/sources/src-6f0757c36a2d|Rethinking-Power-Safety-The-Inherent-Benefits-of-800V-Low-Voltage-DC-Architectures]] [[ai-open-dc-power-distribution/Rethinking-Power-Safety-The-Inherent-Benefits-of-800V-Low-Voltage-DC-Architectures.pdf#page=6|PDF p.6]] [[ai-open-dc-power-distribution/Rethinking-Power-Safety-The-Inherent-Benefits-of-800V-Low-Voltage-DC-Architectures.pdf#page=7|PDF p.7]]。
- 固态断路器必须与区域管理、联锁及再上电策略协调；小于5μs是提出的联锁预算，并非已测量的完整部署成果。[[knowledge/sources/src-1488fa963fc0|Solid-State-Circuit-Breaker-SSCB-and-DC-Fault-Manager]] [[ai-open-dc-power-distribution/Solid-State-Circuit-Breaker-SSCB-and-DC-Fault-Manager.pdf#page=5|PDF p.5]] [[ai-open-dc-power-distribution/Solid-State-Circuit-Breaker-SSCB-and-DC-Fault-Manager.pdf#page=8|PDF p.8]]。
- 辅助负载（网络、存储、风扇、CDU）也要纳入LVDC生态，不能只给xPU供电而忽略持续散热/控制的生命线。[[knowledge/sources/src-9d2ab7f25f7f|LVDC-Building-an-Open-and-Evolving-Ecosystem]] [[ai-open-dc-power-distribution/LVDC-Building-an-Open-and-Evolving-Ecosystem.pdf#page=7|PDF p.7]]。

## 架构决策（综合判断）

1. 给出正常态、突变、降额、故障、黑启动/恢复五类合同，而不是只有机架铭牌功率。
2. 把能量存储分成电网平滑、穿越与本地故障供能三种角色；同一电容/电池可改善穿越也增加故障可用能量。
3. 冗余域和保护域应与网络/计算故障域、冷却持续能力对齐；供电恢复不等于允许所有GPU同时恢复峰值。
4. 从接地、极性和线对地电压出发定义绝缘/检修/连接器边界，不能只说“800V兼容”。[[knowledge/sources/src-8b67b806daaf|Using-the-Full-Low-Voltage-Direct-Current-Range-up-to-1500V-for-Data-Centers]] [[ai-open-dc-power-distribution/Using-the-Full-Low-Voltage-Direct-Current-Range-up-to-1500V-for-Data-Centers.pdf#page=5|PDF p.5]] [[ai-open-dc-power-distribution/Using-the-Full-Low-Voltage-Direct-Current-Range-up-to-1500V-for-Data-Centers.pdf#page=6|PDF p.6]]。

## 共识、缺口与成本

这些来源支持共同设计方向，但没有统一设备组合的端到端验收结果。经济性还缺保护器件损耗、储能寿命、备件/技能、现场维护窗口和故障停机损失；1500V的器件FoM不是美元报价，SST效率目标不是运行电费账单。

## 未决问题

- 哪组最坏负载阶跃、故障电流包络与冷却恢复时序可被所有供应商共同复现？
- 电网侧要求变化是否会穿透到作业调度、功率封顶及CDU/泵的备用供电？

