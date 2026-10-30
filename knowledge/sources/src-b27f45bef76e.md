---
id: "src-b27f45bef76e"
type: "source"
title: "High-Power-Density BBU and CBU Design for Evolving AI Data Center Power Architectures"
source_path: "Rack & Power/High-Power-Density BBU and CBU Design for Evolving AI Data Center Power Architectures.pdf"
source_git_blob_sha: "f548d8d6d78e96b0e735787f436216644720daad"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 14
review_status: "analyzed-visual"
evidence_pages: [3, 4, 6, 7, 8, 9, 10, 11, 12]
text_reviewed: true
key_pages_visual_checked: [6, 7, 8, 10, 11, 12]
tags: ["ocp2026", "source", "power-cooling", "bbu", "cbu", "energy-storage", "roadmap"]
concepts: ["[[knowledge/concepts/power-cooling-grid-to-chip-contract|电网到芯片接口契约]]"]
---

# BBU 与 CBU 路线图：功率密度、安全及 SOC 用途之间的取舍

> 原始题名：High-Power-Density BBU and CBU Design for Evolving AI Data Center Power Architectures。阅读范围：完整可提取文字（物理 PDF 共 14 页），关键引用图表另做视觉核对。

## 核心结论

- Panasonic 把备用供电、削峰与高频负载平滑区分为不同用途，提出 LIB 与 LIC 混合架构；共享 SOC 会降低留给停电备份的能量，额定 MW 不能脱离持续时间。 [[Rack & Power/High-Power-Density BBU and CBU Design for Evolving AI Data Center Power Architectures.pdf#page=4|PDF p.4]]、[[Rack & Power/High-Power-Density BBU and CBU Design for Evolving AI Data Center Power Architectures.pdf#page=10|PDF p.10]]、[[Rack & Power/High-Power-Density BBU and CBU Design for Evolving AI Data Center Power Architectures.pdf#page=11|PDF p.11]]
- NCA/NCM 与 LFP 复合材料追求功率能力和热稳定性平衡；250 W 级复合电芯、300 W/90 s 与 MW 级容器方案大多仍是模拟、估算或路线图。 [[Rack & Power/High-Power-Density BBU and CBU Design for Evolving AI Data Center Power Architectures.pdf#page=6|PDF p.6]]、[[Rack & Power/High-Power-Density BBU and CBU Design for Evolving AI Data Center Power Architectures.pdf#page=8|PDF p.8]]、[[Rack & Power/High-Power-Density BBU and CBU Design for Evolving AI Data Center Power Architectures.pdf#page=9|PDF p.9]]、[[Rack & Power/High-Power-Density BBU and CBU Design for Evolving AI Data Center Power Architectures.pdf#page=10|PDF p.10]]、[[Rack & Power/High-Power-Density BBU and CBU Design for Evolving AI Data Center Power Architectures.pdf#page=11|PDF p.11]]、[[Rack & Power/High-Power-Density BBU and CBU Design for Evolving AI Data Center Power Architectures.pdf#page=12|PDF p.12]]
- 热板照片报告复合样品未起火、穿刺温度曲线较低，但纵轴是归一化 index，不能读取成摄氏度，更不能证明所有电芯或整柜无起火风险。 [[Rack & Power/High-Power-Density BBU and CBU Design for Evolving AI Data Center Power Architectures.pdf#page=7|PDF p.7]]
- “零事故”出货记录为企业总体主张，没有暴露时间、型号、故障定义和第三方证据；不应转换为本代 ESS 的失效率。 [[Rack & Power/High-Power-Density BBU and CBU Design for Evolving AI Data Center Power Architectures.pdf#page=3|PDF p.3]]

## 关键证据

| 主张与信息 | 类型、边界与架构含义 | 原始出处 |
| --- | --- | --- |
| 电芯功率和备份时长 | 120 W/90 s 当前例子，200 W/90 s 下一阶段、300 W/90 s 未来目标；比较图明确标估算/模拟 | [[Rack & Power/High-Power-Density BBU and CBU Design for Evolving AI Data Center Power Architectures.pdf#page=6\|PDF p.6]]、[[Rack & Power/High-Power-Density BBU and CBU Design for Evolving AI Data Center Power Architectures.pdf#page=8\|PDF p.8]] |
| 10 ft 容器 BBU/CBU 配比 | 8 BBU、5 BBU+3 CBU、8 CBU 的概念比较，输出 1000–1500 V DC；页脚明确初步估算，仅供概念评估 | [[Rack & Power/High-Power-Density BBU and CBU Design for Evolving AI Data Center Power Architectures.pdf#page=11\|PDF p.11]] |
| 路线图时间边界 | p.10 文案说支持 2 MW today，但 p.12 将 2 MW/90 s 放在未来路线图；不得作为已量产交付确认 | [[Rack & Power/High-Power-Density BBU and CBU Design for Evolving AI Data Center Power Architectures.pdf#page=10\|PDF p.10]]、[[Rack & Power/High-Power-Density BBU and CBU Design for Evolving AI Data Center Power Architectures.pdf#page=12\|PDF p.12]] |

## 指标与条件

| 指标 | 数值与单位 | 对象、条件、基线及缺失项 | 原始页 |
| --- | --- | --- | --- |
| 200 W×90 s / 300 W×90 s | 所需能量 5 / 7.5 Wh | 理想能量换算，不含转换损耗/温度/老化余量。原表 margin 使用可用能量分母，非通常相对需求的裕量 | [[Rack & Power/High-Power-Density BBU and CBU Design for Evolving AI Data Center Power Architectures.pdf#page=6\|PDF p.6]] |
| 8 BBU 概念配置 | 300 s 备份 4.5 MW（共享 SOC）或 8 MW（不共享）；平滑 3.4 MW | 不是同时独立可用的两份能量；未给 SOC 窗口、效率、寿命 | [[Rack & Power/High-Power-Density BBU and CBU Design for Evolving AI Data Center Power Architectures.pdf#page=11\|PDF p.11]] |
| 5 BBU+3 CBU 概念配置 | 300 s 备份 4.6 MW；平滑 4.2 MW | 平滑定义为 1 s 充/放；模型估算而非现场测试 | [[Rack & Power/High-Power-Density BBU and CBU Design for Evolving AI Data Center Power Architectures.pdf#page=11\|PDF p.11]] |
| 8 CBU 概念配置 | 300 s 备份 300 kW；平滑 10 MW | 强调短时功率与长时能量不同；不可仅按 10 MW 视为 10 MW 后备系统 | [[Rack & Power/High-Power-Density BBU and CBU Design for Evolving AI Data Center Power Architectures.pdf#page=11\|PDF p.11]] |

## 图表与架构

p.6/8 放电曲线不带完整数值轴且标明模拟或预期。p.7 穿刺图纵轴为温度 index，不是绝对温度。p.11 的功率/时长矩阵比单一最高 MW 更适合架构需求拆解。

## 关联与比较

- [[knowledge/concepts/power-cooling-grid-to-chip-contract|电网到芯片接口契约]]

## 不确定性与待验证

- 需拿到寿命末期能力、循环与日历衰减、SOC 保留策略、热失控传播报告和系统认证型号/版本。
- 演讲没有币种、成本、替换周期、利用率或备用与平滑收益估值，不能推算 CAPEX/OPEX 回报。

## 来源与版本

- [GitHub 原始文件（固定提交）](https://github.com/microarch-flow/OCP-2026/blob/d6e362b7bb1e65327b9ff005e9b55b5850ccbb34/Rack%20%26%20Power/High-Power-Density%20BBU%20and%20CBU%20Design%20for%20Evolving%20AI%20Data%20Center%20Power%20Architectures.pdf)
- 来源身份 `src-b27f45bef76e`；Git blob `f548d8d6d78e96b0e735787f436216644720daad`；原始物理页数 `14`。
- 原始文件保持不变；本文为中文分析，不是讲者认可或独立实验复现。
