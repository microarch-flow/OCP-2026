---
id: "src-2c20f7575bbc"
type: "source"
title: "Mitigating AI Training Power Oscillations- Utility Requirements and In-Rack Power Filtering"
source_path: "Rack & Power/Mitigating AI Training Power Oscillations- Utility Requirements and In-Rack Power Filtering.pdf"
source_git_blob_sha: "860e6cf9b63b1ab2ea6546ccb8ab8388a98749a9"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 15
review_status: "analyzed-visual"
evidence_pages: [3, 5, 6, 7, 8, 10, 11, 12, 13]
text_reviewed: true
key_pages_visual_checked: [3, 6, 7, 10, 11, 12]
tags: ["ocp2026", "source", "power-cooling"]
concepts: ["[[knowledge/concepts/power-cooling-grid-to-chip-contract|电网到芯片接口契约]]", "[[knowledge/concepts/power-cooling-capacity-evidence-ladder|容量证据分级]]"]
---

# AI 训练功率振荡：必须按频段和滤波位置分配责任

> 原始题名：Mitigating AI Training Power Oscillations- Utility Requirements and In-Rack Power Filtering。阅读范围：完整可提取文字（物理 PDF 共 15 页），关键引用图表另做视觉核对。

## 核心结论

- 训练的周期性计算/空闲负载不仅是平均 MW 问题，还可能落入电网机电振荡、扭振及阻抗交互频段；普通 PSU 电容不能自动覆盖全部低频扰动。 [[Rack & Power/Mitigating AI Training Power Oscillations- Utility Requirements and In-Rack Power Filtering.pdf#page=3|PDF p.3]]、[[Rack & Power/Mitigating AI Training Power Oscillations- Utility Requirements and In-Rack Power Filtering.pdf#page=5|PDF p.5]]
- 在 GPU 后级、机架 DC 母线、母线槽或 MV/HV 配置储能，保护的上游/下游器件不同；外置母线滤波器不能消除其下游 PSU/IBC 仍承受的负载摆动。 [[Rack & Power/Mitigating AI Training Power Oscillations- Utility Requirements and In-Rack Power Filtering.pdf#page=10|PDF p.10]]、[[Rack & Power/Mitigating AI Training Power Oscillations- Utility Requirements and In-Rack Power Filtering.pdf#page=11|PDF p.11]]、[[Rack & Power/Mitigating AI Training Power Oscillations- Utility Requirements and In-Rack Power Filtering.pdf#page=12|PDF p.12]]
- 建议先建立从 HV 至机箱的同步功率观测，再依据频域和可用能量选择软件、机架电容与 UPS/BESS；本文没有完整控制器或闭环现场验证。 [[Rack & Power/Mitigating AI Training Power Oscillations- Utility Requirements and In-Rack Power Filtering.pdf#page=7|PDF p.7]]、[[Rack & Power/Mitigating AI Training Power Oscillations- Utility Requirements and In-Rack Power Filtering.pdf#page=8|PDF p.8]]、[[Rack & Power/Mitigating AI Training Power Oscillations- Utility Requirements and In-Rack Power Filtering.pdf#page=13|PDF p.13]]

## 关键证据

| 主张与信息 | 类型、边界与架构含义 | 原始出处 |
| --- | --- | --- |
| 各电力公司振荡/爬坡限制对照 | 讲者汇总的现有或提议条款；不能直接作为任何站点现行接入合同或法规。 | [[Rack & Power/Mitigating AI Training Power Oscillations- Utility Requirements and In-Rack Power Filtering.pdf#page=6\|PDF p.6]] |
| PSU 内部高压电容与外部 DC/DC 电容架 | 前者受到内部电压裕量限制，后者可扩大电容有效放电深度，但增加变换器、控制及故障路径。 | [[Rack & Power/Mitigating AI Training Power Oscillations- Utility Requirements and In-Rack Power Filtering.pdf#page=11\|PDF p.11]] |
| 用 GPU 遥测预测电容充放电 | 控制方向而非经过数据集、稳定裕度及故障测试证明的算法。 | [[Rack & Power/Mitigating AI Training Power Oscillations- Utility Requirements and In-Rack Power Filtering.pdf#page=13\|PDF p.13]] |

## 指标与条件

| 指标 | 数值与单位 | 对象、条件、基线及缺失项 | 原始页 |
| --- | --- | --- | --- |
| 作者列出的振荡频带 | 区域间 0.1–0.5 Hz；区域内 0.5–0.8 Hz；本地 0.8–2 Hz；扭振 5–55 Hz | 频段示例，不是每个站点都存在这些模式。 | [[Rack & Power/Mitigating AI Training Power Oscillations- Utility Requirements and In-Rack Power Filtering.pdf#page=3\|PDF p.3]] |
| 电容能量利用比例 | DoD = 1 − (Vmin/Vmax)² | 来自电容能量关系；需另计 DC/DC 效率、额定电压、老化、峰值功率和安全余量，不能仅凭容量 F 定义缓冲能力。 | [[Rack & Power/Mitigating AI Training Power Oscillations- Utility Requirements and In-Rack Power Filtering.pdf#page=11\|PDF p.11]] |

## 图表与架构

已核对 p.3 的归一化训练功率、p.6 的公司条款表、p.7 的多层观测、p.10–12 的滤波位置。p.12 的 DC 母线示意含类似 AC 源的符号，不能据此解释为 DC 母线上存在交流电源。位置比较的重点是扰动在哪些器件之前被吸收。

## 关联与比较

- [[knowledge/concepts/power-cooling-time-scales-and-control-authority]]

- [[knowledge/concepts/power-cooling-grid-to-chip-contract|电网到芯片接口契约]]
- [[knowledge/concepts/power-cooling-capacity-evidence-ladder|容量证据分级]]

## 不确定性与待验证

- 目标站点真实振荡频谱、并网阻抗与电力公司批准的限制是什么？
- 缓冲器在最坏 SOC、温度和寿命末期是否仍满足能量、峰值功率与连续重复循环？
- 多层控制器的带宽、相位裕度、故障回退和统一时间戳如何验证？

## 来源与版本

- [GitHub 原始文件（固定提交）](https://github.com/microarch-flow/OCP-2026/blob/d6e362b7bb1e65327b9ff005e9b55b5850ccbb34/Rack%20%26%20Power/Mitigating%20AI%20Training%20Power%20Oscillations-%20Utility%20Requirements%20and%20In-Rack%20Power%20Filtering.pdf)
- 来源身份 `src-2c20f7575bbc`；Git blob `860e6cf9b63b1ab2ea6546ccb8ab8388a98749a9`；原始物理页数 `15`。
- 原始文件保持不变；本文为中文分析，不是讲者认可或独立实验复现。
