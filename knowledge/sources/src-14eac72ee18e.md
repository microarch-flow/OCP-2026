---
id: "src-14eac72ee18e"
type: "source"
title: "Accelerating High-Power Server Design Through Board-Level Electro-Thermal Co-Simulation of VRMs and PDNs"
aliases: ["Accelerating High-Power Server Design Through Board-Level Electro-Thermal Co-Simulation of VRMs and PDNs"]
speakers: "Mike Wu（Microsoft）；Steven Chien（Wiwynn）"
source_path: "server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf"
source_git_blob_sha: "ada83ea338ad0e8632a9117432b5e20c6fc2db25"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 24
review_status: "analyzed-visual"
text_reviewed: true
key_pages_visual_checked: [8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21]
evidence_pages: [4, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23]
tags: ["ocp2026", "source", "compute-memory"]
concepts: ["[[knowledge/concepts/compute-memory-power-path-and-dynamics]]", "[[knowledge/concepts/compute-memory-federated-model-contract]]"]
---

# Accelerating High-Power Server Design Through Board-Level Electro-Thermal Co-Simulation of VRMs and PDNs

## 核心结论
缺少vendor详细热模型时，可用材料/几何构造方向相关的effective conductivity，并把电损耗位置交给热求解、温度场再交回PI。关键不是“一个k解决所有热问题”，而是早期近似有物理依据、有实测校准和已知误差。[[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=10|PDF p.10]] [[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=18|PDF p.18]] [[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=19|PDF p.19]]

## 关键证据
串联模型 `1/k_eff=Σ(v_i/k_i)`、并联模型 `k_eff=Σ(v_i k_i)` 依赖热流方向和结构。PCB in-plane/through-plane分别处理；示例FR4/Cu、12导电层、总厚2.34mm得到64.2/0.36 W/(m·K)，不能把64.2当各向同性值。[[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=8|PDF p.8]] [[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=9|PDF p.9]] [[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=10|PDF p.10]] [[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=11|PDF p.11]]

## 指标与条件
|比较|结果与解释|
|---|---|
|PCB effective-k vs copper-pour模型|列出器件对test偏差约8–15%，两种PCB表达接近；接近不意味着都无误差。[[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=12\|PDF p.12]]|
|Diode，epoxy参考0.7 vs series0.96 W/(m·K)|对test偏差10%→3%，限定该封装与测试，不是任意器件都3%。[[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=13\|PDF p.13]] [[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=14\|PDF p.14]]|
|MOSFET，2R vs effective-k|2R对test8/8/11/10%，effective-k12/13/15/14%；差4–5**个百分点**，不是effective-k对实测只差4–5%。[[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=16\|PDF p.16]]|
|简化ET thermal model vs传统|mesh0.54×、calculation time0.55×、test deviation0.9×；相对基线的46%/45%减少，没有绝对秒数或机器设置。[[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=20\|PDF p.20]]|

## 图表与架构
p.19明确三步：PI初算→thermal收敛→更新温度的最终PI，然后结束；**不能改写成双求解器反复迭代到联合固定点**。p.18的双向箭头表达信息交换，不覆写p.19给出的实际workflow。[[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=18|PDF p.18]] [[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=19|PDF p.19]]
p.21热图对照IR照片，支持热点位置较符合的定性观察，但色阶各异，不从颜色直接算逐像素误差。若干器件图片标AI-generated illustrative，不作实物验证证据。[[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=21|PDF p.21]]

## 关联与比较
[[knowledge/concepts/compute-memory-power-path-and-dynamics|供电动态约束]] · [[knowledge/concepts/compute-memory-federated-model-contract|模型契约]]：应带各向异性、损耗空间分布、边界温度/流量和误差，不只交换单一峰值功耗。

## 不确定性与待验证
p.15文字称“series structure”，公式却为并联算术加权，106 W/(m·K)亦与该公式方向一致；保留标注矛盾，不能直接复制错误命名。模型需扩展到不同封装、via局部热通道和2.5D/3D，p.23也列为后续工作。[[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=15|PDF p.15]] [[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=23|PDF p.23]]

## 原始页码导航
[[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=4|p.4]] · [[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=5|p.5]] · [[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=8|p.8]] · [[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=9|p.9]] · [[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=10|p.10]] · [[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=11|p.11]] · [[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=12|p.12]] · [[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=13|p.13]] · [[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=14|p.14]] · [[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=15|p.15]] · [[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=16|p.16]] · [[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=18|p.18]] · [[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=19|p.19]] · [[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=20|p.20]] · [[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=21|p.21]] · [[server/Accelerating-High-Power-Server-Design-Through-Board-Level-Electro-Thermal-Co-Simulation-of-VRMs-and-PDNs.pdf#page=23|p.23]]
