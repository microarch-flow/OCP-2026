---
id: "src-e3c54df076ca"
type: "source"
title: "MiTAC与AMD开放AI整柜：软件集成与多冷却路线的验证缺口"
source_path: "expo-hall-sessions/Scaling-the-Future-of-Open-Infrastructure-with-Advanced-Cooling-presented-by-MiTAC.pdf"
source_git_blob_sha: "6692fd2d9c10428399c6d7d7cf16a54b26145ecf"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 21
review_status: "analyzed-visual"
evidence_pages: [2, 3, 5, 6, 9, 12, 14, 15, 16, 17, 18, 19]
text_reviewed: true
key_pages_visual_checked: [2, 5, 6, 9, 12, 14, 15, 16, 17, 18, 19]
tags: ["ocp2026", "expo-hall"]
concepts: ["[[knowledge/concepts/expo-evidence-to-deployment]]"]
---

# MiTAC与AMD开放AI整柜：软件集成与多冷却路线的验证缺口

## 核心结论
材料把开放硬件/软件与冷却选择并列：AMD CPU/MI350X风冷、MI355X液冷、DDN存储、开放管理及多家热方案构成集成组合。组合丰富不等于任意混用都已合格，更不意味着一次配置可继承所有合作伙伴最佳指标。[[expo-hall-sessions/Scaling-the-Future-of-Open-Infrastructure-with-Advanced-Cooling-presented-by-MiTAC.pdf#page=2|PDF p.2]] [[expo-hall-sessions/Scaling-the-Future-of-Open-Infrastructure-with-Advanced-Cooling-presented-by-MiTAC.pdf#page=5|PDF p.5]] [[expo-hall-sessions/Scaling-the-Future-of-Open-Infrastructure-with-Advanced-Cooling-presented-by-MiTAC.pdf#page=6|PDF p.6]] [[expo-hall-sessions/Scaling-the-Future-of-Open-Infrastructure-with-Advanced-Cooling-presented-by-MiTAC.pdf#page=14|PDF p.14]]

## 关键证据、指标与条件
- OCP多节点图列2OU2N风冷、2OU4N液冷EPYC9006，以及2OU3N EPYC9004/9005；机型密度并非同CPU/功率条件的性能比较。[[expo-hall-sessions/Scaling-the-Future-of-Open-Infrastructure-with-Advanced-Cooling-presented-by-MiTAC.pdf#page=3|PDF p.3]]
- MR1100栈把MiCoreView、MiOBMC/MiOPF、ROCm、Ubuntu、Rafay、DDN和AMD Enterprise AI并置；**MiRMC FW标Coming Soon**。不能把logo墙当完整版本互操作报告。[[expo-hall-sessions/Scaling-the-Future-of-Open-Infrastructure-with-Advanced-Cooling-presented-by-MiTAC.pdf#page=6|PDF p.6]]
- 平台矩阵的1/100/1000/10000/100000+用户是定位，没有到达率、请求长度和SLO；system/rack power混用，不可按“用户/W”排名。[[expo-hall-sessions/Scaling-the-Future-of-Open-Infrastructure-with-Advanced-Cooling-presented-by-MiTAC.pdf#page=9|PDF p.9]]
- MI350P称FP4最大260B参数、450–600W TBP、较RTX Pro6000最高4.2×tokens/s/$；引用Endnote MI350P-007，但本文件未提供该测试附注，缺模型、量化质量、并发及价格基线。[[expo-hall-sessions/Scaling-the-Future-of-Open-Infrastructure-with-Advanced-Cooling-presented-by-MiTAC.pdf#page=12|PDF p.12]]
- JWS HSSVC POC主张GPU冷板压降减44%；图纵轴却写Power(kW)，图例40°C对“Simulated HSSCV@45°C”，拼写/单位/温度条件不一致。无法据图确认44%是压降还是泵功，也不能称同温度实测。[[expo-hall-sessions/Scaling-the-Future-of-Open-Infrastructure-with-Advanced-Cooling-presented-by-MiTAC.pdf#page=16|PDF p.16]]
- PG25第二供应商测试在45°C供液、约3.5/4.25/5.5LPM给回供水ΔT，五种R:C混合比例曲线相近；未定义R、没有材料腐蚀/密封长测。因此热行为接近不等于所有混配比例长寿命兼容。[[expo-hall-sessions/Scaling-the-Future-of-Open-Infrastructure-with-Advanced-Cooling-presented-by-MiTAC.pdf#page=17|PDF p.17]]
- Akash方案称降温最多10°C、冷却功耗最多降100%、~75°F环境FLOPs/W最多+22%、~120°F环境token吞吐最多+15%。不同环境/指标不可相乘；“10°C(50°F)”把绝对温度转换用于温差，10°C温差应为18°F。缺基线及整机功率范围。[[expo-hall-sessions/Scaling-the-Future-of-Open-Infrastructure-with-Advanced-Cooling-presented-by-MiTAC.pdf#page=18|PDF p.18]]
- ZutaCore两相方案称约0.3L/min/kW、>4000W/chip、平均>250W/cm²、annualized pPUE1.03及冷却能耗较单相低74%。没有完整测试方法/气候/负载，pPUE不得当作全设施PUE。[[expo-hall-sessions/Scaling-the-Future-of-Open-Infrastructure-with-Advanced-Cooling-presented-by-MiTAC.pdf#page=19|PDF p.19]]

## 图表与架构
已核p2/5/6/9/12、14–19，后段多为图片而非可提取文字。p15的GPU冷板回路连接rack manifold；p14另列CoolIT/Nidec单相、ZutaCore两相及Akash diamond三路，不能将三路热性能当作同一循环联合实测。[[expo-hall-sessions/Scaling-the-Future-of-Open-Infrastructure-with-Advanced-Cooling-presented-by-MiTAC.pdf#page=14|PDF p.14]] [[expo-hall-sessions/Scaling-the-Future-of-Open-Infrastructure-with-Advanced-Cooling-presented-by-MiTAC.pdf#page=15|PDF p.15]]

## 关联与比较
[[knowledge/concepts/expo-evidence-to-deployment]]。与Ecolab的冷却液维护条件对照：second source需要材料/化学/维护资格，不仅初始ΔT；与Frore温度收益对照应固定工作负载、环境、时钟与完整功耗边界。

## 不确定性与待验证
封面标MiTAC Confidential，AMD部分标Public；本卡只分析已给原件。需状态/版本矩阵、热与电单线图、逐方案测试报告、失泵/漏液/恢复演练及真实p99。物理PDF p14之后页脚错开一页，引用一律物理页。


跨源比较：[[knowledge/comparisons/expo-thermal-performance-contract]]。
