---
id: "src-7bb5ed28d115"
type: "source"
title: "Short-Circuit-Bolted-Fault-Analysis-of-LVDC-Power-Distribution-Systems-for-Datacenter-Uses"
source_path: "ai-open-dc-power-distribution/Short-Circuit-Bolted-Fault-Analysis-of-LVDC-Power-Distribution-Systems-for-Datacenter-Uses.pdf"
source_git_blob_sha: "b6d33e9178c00ba804b4ebaf660d43b4d14ff97f"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 13
review_status: "analyzed-visual"
evidence_pages: [4, 5, 6, 7, 8, 9, 10, 11, 12]
text_reviewed: true
key_pages_visual_checked: [4, 5, 6, 7, 8, 9, 10]
tags: ["ocp2026", "source", "power-cooling"]
concepts: ["[[knowledge/concepts/power-cooling-grid-to-chip-contract|电网到芯片接口契约]]", "[[knowledge/concepts/power-cooling-capacity-evidence-ladder|容量证据分级]]"]
---

# 800 V 螺栓短路模型：电容、线缆阻抗与储能持续馈入

> 原始题名：Short-Circuit-Bolted-Fault-Analysis-of-LVDC-Power-Distribution-Systems-for-Datacenter-Uses。阅读范围：完整可提取文字（物理 PDF 共 13 页），关键引用图表另做视觉核对。

## 核心结论

- UL 的研究是参数化短路模拟，不是器件型式试验或弧闪试验；模型 1 为电容—线缆 RLC 回路，模型 2 加入简化 boost DC/DC 与超级电容，作者仍计划实物对照。 [[ai-open-dc-power-distribution/Short-Circuit-Bolted-Fault-Analysis-of-LVDC-Power-Distribution-Systems-for-Datacenter-Uses.pdf#page=4|PDF p.4]]、[[ai-open-dc-power-distribution/Short-Circuit-Bolted-Fault-Analysis-of-LVDC-Power-Distribution-Systems-for-Datacenter-Uses.pdf#page=5|PDF p.5]]、[[ai-open-dc-power-distribution/Short-Circuit-Bolted-Fault-Analysis-of-LVDC-Power-Distribution-Systems-for-Datacenter-Uses.pdf#page=12|PDF p.12]]
- 母线电容、导线几何/长度/温度共同改变峰值、di/dt 和 I²t；低电阻可能使峰值更大，但不同截面同时改变间距与电感，不能把截面与峰值写成严格单调关系。 [[ai-open-dc-power-distribution/Short-Circuit-Bolted-Fault-Analysis-of-LVDC-Power-Distribution-Systems-for-Datacenter-Uses.pdf#page=6|PDF p.6]]、[[ai-open-dc-power-distribution/Short-Circuit-Bolted-Fault-Analysis-of-LVDC-Power-Distribution-Systems-for-Datacenter-Uses.pdf#page=7|PDF p.7]]、[[ai-open-dc-power-distribution/Short-Circuit-Bolted-Fault-Analysis-of-LVDC-Power-Distribution-Systems-for-Datacenter-Uses.pdf#page=8|PDF p.8]]
- 储能并不只提高可用性，也会延长故障供能；选择保护器件需同时验证开断峰值、上升率与能量，而不是只匹配正常额定电流。 [[ai-open-dc-power-distribution/Short-Circuit-Bolted-Fault-Analysis-of-LVDC-Power-Distribution-Systems-for-Datacenter-Uses.pdf#page=9|PDF p.9]]、[[ai-open-dc-power-distribution/Short-Circuit-Bolted-Fault-Analysis-of-LVDC-Power-Distribution-Systems-for-Datacenter-Uses.pdf#page=10|PDF p.10]]、[[ai-open-dc-power-distribution/Short-Circuit-Bolted-Fault-Analysis-of-LVDC-Power-Distribution-Systems-for-Datacenter-Uses.pdf#page=11|PDF p.11]]
- 800 V 是该模型的导体间电压，图示单一参考点；不能把它擅自重画成 ±400 V 中点接地方案。 [[ai-open-dc-power-distribution/Short-Circuit-Bolted-Fault-Analysis-of-LVDC-Power-Distribution-Systems-for-Datacenter-Uses.pdf#page=4|PDF p.4]]

## 关键证据

| 主张与信息 | 类型、边界与架构含义 | 原始出处 |
| --- | --- | --- |
| 模型覆盖范围 | 5 mF 等母线电容、铜导线与温度扫描；简化电路不含完整真实控制器、负载控制或全系统接地故障路径。 | [[ai-open-dc-power-distribution/Short-Circuit-Bolted-Fault-Analysis-of-LVDC-Power-Distribution-Systems-for-Datacenter-Uses.pdf#page=4\|PDF p.4]]、[[ai-open-dc-power-distribution/Short-Circuit-Bolted-Fault-Analysis-of-LVDC-Power-Distribution-Systems-for-Datacenter-Uses.pdf#page=5\|PDF p.5]] |
| 振荡与阻尼 | 波形体现 RLC 欠阻尼；判断应比较 R 与 2√(L/C) 等同量纲条件，不照抄页中电阻低于电感/电容的简写为数值判据。 | [[ai-open-dc-power-distribution/Short-Circuit-Bolted-Fault-Analysis-of-LVDC-Power-Distribution-Systems-for-Datacenter-Uses.pdf#page=6\|PDF p.6]] |
| 超级电容容量公式 | 作者使用 U=U₀exp(−t/RC) 的恒电阻放电近似；不是恒功率 GPU 负载模型，不能直接据此承诺 GPU 保持时间。 | [[ai-open-dc-power-distribution/Short-Circuit-Bolted-Fault-Analysis-of-LVDC-Power-Distribution-Systems-for-Datacenter-Uses.pdf#page=9\|PDF p.9]] |
| 后续验证 | 器件仿真、硬件测量及更真实转换器/负载尚列后续工作；本结果不是所有安装条件的最坏故障包络。 | [[ai-open-dc-power-distribution/Short-Circuit-Bolted-Fault-Analysis-of-LVDC-Power-Distribution-Systems-for-Datacenter-Uses.pdf#page=12\|PDF p.12]] |

## 指标与条件

| 指标 | 数值与单位 | 对象、条件、基线及缺失项 | 原始页 |
| --- | --- | --- | --- |
| 母线/储能参数 | 母线 2、5、10 mF；超级电容 1、78、3136、23521 mF | 800 V 模型；不同电容对应不同场景，不能将最大储能默认加入每个母线案例。 | [[ai-open-dc-power-distribution/Short-Circuit-Bolted-Fault-Analysis-of-LVDC-Power-Distribution-Systems-for-Datacenter-Uses.pdf#page=4\|PDF p.4]] |
| 导线参数扫描 | 截面 8.4/42.5/150/240 mm²；长度 0.25/2/5/10 m；20/40/70°C | 较小截面中心间距 10 mm，较大 25 mm；几何不完全固定。 | [[ai-open-dc-power-distribution/Short-Circuit-Bolted-Fault-Analysis-of-LVDC-Power-Distribution-Systems-for-Datacenter-Uses.pdf#page=4\|PDF p.4]] |
| 模型 1、5 m、20°C 示例 | 8.4 mm²：峰值 16.3 kA、I²t 60,329 A²s；240 mm²：30.6 kA、239,061 A²s | 5 mF 表格条件；不是连续载流能力或电弧入射能。 | [[ai-open-dc-power-distribution/Short-Circuit-Bolted-Fault-Analysis-of-LVDC-Power-Distribution-Systems-for-Datacenter-Uses.pdf#page=7\|PDF p.7]] |
| 模型 1、0.25 m、20°C、240 mm² | 峰值 75.5 kA；I²t 264,857 A²s；di/dt 3.02 kA/µs | 该表短导线案例；不同拓扑下还可能存在其他更严苛工况。 | [[ai-open-dc-power-distribution/Short-Circuit-Bolted-Fault-Analysis-of-LVDC-Power-Distribution-Systems-for-Datacenter-Uses.pdf#page=7\|PDF p.7]] |
| 模型 2 汇总范围 | 峰值 8–70 kA；I²t 1.3–689.5 kA²s；di/dt 0.03–0.15 kA/µs | 原表单位为 kA²s，即 10⁶ A²s，不能与模型 1 的 A²s 直接比较数字；汇总并未完整逐项映射到每条图线。 | [[ai-open-dc-power-distribution/Short-Circuit-Bolted-Fault-Analysis-of-LVDC-Power-Distribution-Systems-for-Datacenter-Uses.pdf#page=10\|PDF p.10]] |

## 图表与架构

已核对 p.4–10 全部主要参数图表。p.8 上方电压图与下方电流图的颜色—电容映射不相同，需逐图看图例而不能跨图按颜色配对。p.10 长时间故障波形与高 I²t 是简化储能电路结果，未给出具体保护动作；不可据此推导某个断路器已经失效或某处弧闪等级。

## 关联与比较

- [[knowledge/comparisons/power-cooling-protection-coordination]]

- [[knowledge/concepts/power-cooling-grid-to-chip-contract|电网到芯片接口契约]]
- [[knowledge/concepts/power-cooling-capacity-evidence-ladder|容量证据分级]]

## 不确定性与待验证

- 模型初始电压、控制限流、寄生参数和开断条件能否与实测校准？
- 超级电容的连接方式、反灌路径与本地保护失效会怎样改变完整故障包络？
- 标准规定的各类故障、接地方式及容差组合是否覆盖，而不只是 bolted fault？

## 来源与版本

- [GitHub 原始文件（固定提交）](https://github.com/microarch-flow/OCP-2026/blob/d6e362b7bb1e65327b9ff005e9b55b5850ccbb34/ai-open-dc-power-distribution/Short-Circuit-Bolted-Fault-Analysis-of-LVDC-Power-Distribution-Systems-for-Datacenter-Uses.pdf)
- 来源身份 `src-7bb5ed28d115`；Git blob `b6d33e9178c00ba804b4ebaf660d43b4d14ff97f`；原始物理页数 `13`。
- 原始文件保持不变；本文为中文分析，不是讲者认可或独立实验复现。
