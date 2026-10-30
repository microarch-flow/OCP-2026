---
id: "src-e1afbfae08ba"
type: "source"
title: "LITEON 1.1MW HVDC机柜：冗余容量、储能与量产时间分层"
source_path: "expo-hall-sessions/08_LITEON 1MW Power Rack Solution for AI Data Center presented by LITEON.pdf"
source_git_blob_sha: "f1ecd5e0f4f96de1f0594a626029c53b980221b8"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 11
review_status: "analyzed-visual"
evidence_pages: [2, 3, 4, 5, 6, 7, 8, 9]
text_reviewed: true
key_pages_visual_checked: [3, 4, 8]
tags: ["ocp2026", "expo-hall"]
concepts: ["[[knowledge/concepts/expo-evidence-to-deployment]]"]
---

# LITEON 1.1MW HVDC机柜：冗余容量、储能与量产时间分层

## 核心结论
架构在独立44OU电源柜中完成AC→±400/800VDC、储能与配电，再在IT柜做800→50VDC。所谓1MW不是单电源模块，整套冗余/备电容量随配置变化；多数部件量产目标在2027，不能当作2026现场验证。[[expo-hall-sessions/08_LITEON 1MW Power Rack Solution for AI Data Center presented by LITEON.pdf#page=2|PDF p.2]] [[expo-hall-sessions/08_LITEON 1MW Power Rack Solution for AI Data Center presented by LITEON.pdf#page=3|PDF p.3]]

## 关键证据、指标与条件
- 6×220kW shelf=1.32MW安装容量；5+1约1.1MW、N+N仅660kW。每shelf8×27.5kW 400V PSU，415VAC输入；两600kW DC-PDU，每个4×150kW熔断隔离分支/200A whip，维护一个分支损失150kW是该配电粒度，并不保证该IT负载不中断。[[expo-hall-sessions/08_LITEON 1MW Power Rack Solution for AI Data Center presented by LITEON.pdf#page=3|PDF p.3]] [[expo-hall-sessions/08_LITEON 1MW Power Rack Solution for AI Data Center presented by LITEON.pdf#page=7|PDF p.7]]
- 220kW shelf称峰值>98%、满载>97%、hold-up>20ms；图中480VAC实线与calculated曲线分开，415VAC满载接近97%。红“peak spec”线约97.5%，不同于正文>98%表达。PTT测试样品目标2026-11，MP目标2027Q2。[[expo-hall-sessions/08_LITEON 1MW Power Rack Solution for AI Data Center presented by LITEON.pdf#page=4|PDF p.4]]
- CBU每模块18kW/5s、每shelf108kW，六shelf约648kW，**并不能在1.1MW满负载下维持全额5s**。采用EDLC，图另列LIC15s方案；CBU MP目标2027Q2。[[expo-hall-sessions/08_LITEON 1MW Power Rack Solution for AI Data Center presented by LITEON.pdf#page=3|PDF p.3]] [[expo-hall-sessions/08_LITEON 1MW Power Rack Solution for AI Data Center presented by LITEON.pdf#page=5|PDF p.5]]
- BBU每shelf180kW/60s，6×约1.08MW；模块30kW/60s或15kW/120s，LFP、设计寿命10年，0–40°C。寿命是设计值非现场历史；MP目标2027Q3。[[expo-hall-sessions/08_LITEON 1MW Power Rack Solution for AI Data Center presented by LITEON.pdf#page=6|PDF p.6]]
- 1OU120kW DC/DC称峰值>98.5%、满载>98%，但曲线横轴只到约360A、50V对应18kW量级，且末端约97.9%；图很可能是子模块而非整shelf，原文未标清，不能据此证明120kW整架效率。[[expo-hall-sessions/08_LITEON 1MW Power Rack Solution for AI Data Center presented by LITEON.pdf#page=8|PDF p.8]]

## 图表与架构
已看p3/4/8。RMC经CAN汇聚各shelf控制器，内部PMBus，上层Ethernet/Redfish；这是管理路径，不替代熔断/过压等电气保护闭环。[[expo-hall-sessions/08_LITEON 1MW Power Rack Solution for AI Data Center presented by LITEON.pdf#page=9|PDF p.9]]

## 关联与比较
[[knowledge/concepts/expo-evidence-to-deployment]]：商业测算使用“失去一组电源后的可用IT kW”，并把CBU平滑秒级负载与BBU电源中断保持分开；不得相加为同一独立冗余来源。

## 不确定性与待验证
需整套转换链效率、双极失衡/单极故障、N+N切换波形、动态负载稳定性、保护选择性、认证报告及预期寿命的温度/循环条件。没有推理吞吐或p99数据。


跨源比较：[[knowledge/comparisons/expo-power-conversion-boundaries]]。
