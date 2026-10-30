---
type: concept
title: "清洁度与流体状态：TAN、bulk chemistry和板级电学互不替代"
tags: [ocp2026, concept, immersion]
---

# 清洁度与流体状态：TAN、bulk chemistry和板级电学互不替代

## 核心命题
硬件进入槽时已经携带制造/清洗历史，fluid服役后又记录材料析出、氧化、water、handling等历史。只测新液，或只用TAN/颜色判断旧液，都不足以说明板级风险。

## 两组互补实验
### 入槽前工艺：能改变电学恢复，但bulk有机谱未必分得出
KYZEN五条件共10卡，每条件两卡顺序进入同一液。完整清洗B恢复到1e10Ω最快（7.3/3.7h），漂洗不足D为16.9/31.0h；原状A30.5/21.8h。第二卡不是fresh-fluid独立重复，且仅54h停电前窗口。化学不匹配C还排除了持续在仪器floor的CH3；平均曲线不能遮住坏通道。[[cooling-immersion/Before-the-Fluid-How-Pre-Immersion-Cleaning-Chemistry-Shapes-Long-Term-Electronic-Reliability.pdf#page=4|PDF p.4]] [[cooling-immersion/Before-the-Fluid-How-Pre-Immersion-Cleaning-Chemistry-Shapes-Long-Term-Electronic-Reliability.pdf#page=6|PDF p.6]] [[cooling-immersion/Before-the-Fluid-How-Pre-Immersion-Cleaning-Chemistry-Shapes-Long-Term-Electronic-Reliability.pdf#page=7|PDF p.7]]

局部IC与表面照片保留工艺差异，GCMS/LCMS有机筛查没有清楚区分组别。这不是“无污染”，而是**所用观测对所问问题可能不敏感**；该方法本来不是trace ionic定量。[[cooling-immersion/Before-the-Fluid-How-Pre-Immersion-Cleaning-Chemistry-Shapes-Long-Term-Electronic-Reliability.pdf#page=9|PDF p.9]] [[cooling-immersion/Before-the-Fluid-How-Pre-Immersion-Cleaning-Chemistry-Shapes-Long-Term-Electronic-Reliability.pdf#page=10|PDF p.10]]

### 在役历史：相似TAN可伴随不同板电阻
多fluid EID研究80°C/500h/continuous5V，实验室TAN上升而电阻无一致下降。在役B-1约2年、E-1约6月分别比配对temperature-aged参考电阻低19.3%/85.1%；酸值相近仍不足以解释，且都不构成硬件已失效证据。[[cooling-immersion/Fluid-Oxidation-and-Electronic-Reliability-A-Multi-Fluid-EID-Measurement-Study.pdf#page=7|PDF p.7]] [[cooling-immersion/Fluid-Oxidation-and-Electronic-Reliability-A-Multi-Fluid-EID-Measurement-Study.pdf#page=14|PDF p.14]] [[cooling-immersion/Fluid-Oxidation-and-Electronic-Reliability-A-Multi-Fluid-EID-Measurement-Study.pdf#page=15|PDF p.15]] [[cooling-immersion/Fluid-Oxidation-and-Electronic-Reliability-A-Multi-Fluid-EID-Measurement-Study.pdf#page=16|PDF p.16]]

两实验不能合并成同一DOE：KYZEN没有完整公布bath温度/偏置/液体配方，不能把另一研究80°C/5V条件填过去。

## 观测量与盲区
|观测|捕获的主要信息|需要补上的边界|
|---|---|---|
|TAN|总酸量|酸种类、离子性、板表面电学；相同酸量不等效风险|
|FTIR/GCMS/LCMS|特定方法可见的分子/有机组成|检测限、目标band/光程、离子成分；全谱高相关不等于无变化|
|water ppm|绝对含水量|fluid化学、温度与相对饱和度|
|DDF/εr/DBV|给定温度/频率/电极条件下bulk介电|实际connector/PCB几何、污染、BER/重试|
|EID/SIR/leakage|给定bias和surface geometry的局部电响应|完整硬件功能、寿命、失效阈值|

这些边界由上述实验及酯材料演讲支持，并非一个已批准的统一诊断规则。酯B六天湿度实验中resistivity/DDF小变，但DBV38→约28–29kV，说明“dielectric stable”也必须分指标。[[cooling-immersion/Moving-Beyond-Interchangeability-Characterizing-Esters-among-Coolants-for-Immersion.pdf#page=7|PDF p.7]] [[cooling-immersion/Moving-Beyond-Interchangeability-Characterizing-Esters-among-Coolants-for-Immersion.pdf#page=8|PDF p.8]]

## 单相与两相不能直接互抄
Samsung两相案例指出污染在boiling sites沉积、dendrite桥接BGA的机制，并使用受控aqueous wash/DI rinse/dry。这不同于直接将未验证水或溶剂用于现场清洗；委员会对溶剂的类别风险表也不能取代具体验证流程。[[cooling-immersion/Material-Compatibility-and-Long-Term-Hardware-Integrity-of-Enterprise-SSDs-in-Two-Phase-Immersion-Cooling.pdf#page=8|PDF p.8]] [[cooling-immersion/Community-Update-Immersion-Fluids-Workstreams-Update.pdf#page=5|PDF p.5]]

## 下一步实验设计（本库建议）
先建立fluid×BOM×清洗状态矩阵，保存fresh对照与服役/补液历史；在相同bath/bias/geometry条件下并行化学、局部表面、电学和功能测量。分离temperature aging、污染添加、water和field history，避免一个“老化”标签覆盖所有机制。使用阈值前应说明其与失败/SLO的校准关系。

## 关联
[[knowledge/concepts/immersion-qualification-evidence|资格证据链]] · [[knowledge/concepts/power-cooling-fluid-assurance|流体保证]] · [[knowledge/concepts/compute-memory-channel-evidence|高速通道证据阶梯]]
