---
id: "expo-evidence-to-deployment"
type: "concept"
title: "展台方案到架构决策：先识别证据等级与系统边界"
tags: ["ocp2026", "networking"]
review_status: "synthesized"
---

# 展台方案到架构决策：先识别证据等级与系统边界

## 定义
展台资料可证明供应商提出了什么方案，却不自动证明该方案已量产、在目标负载上更快，或具有更低整机成本。这里把**参考设计、样机/曲线、未来量产目标、部署案例、工作负载实测**分开管理。

## 跨源证据与分歧
- Intel 把 agent 的 CPU 时间占比写为示意性仿真；同一资料又给第五代 Xeon 上语义路由器的固定 p95 会话数。两者不能拼成“CPU占80%、所以某CPU可使业务加速4倍”。[[knowledge/sources/src-86e4ca03d02c]] [[expo-hall-sessions/01_Agentic AI The Agentic Rack, Powered by Intel Xeon Processors presente.pdf#page=2|PDF p.2]] [[knowledge/sources/src-86e4ca03d02c]] [[expo-hall-sessions/01_Agentic AI The Agentic Rack, Powered by Intel Xeon Processors presente.pdf#page=8|PDF p.8]]
- Arm/Meta 的价值是1OU双节点参考设计复用及 Yosemite/Rainier 平台；设计资料须 NDA，部分标准贡献仍在进行/未来。宣传2倍规模性能，没有在文件内给可复现基线。[[knowledge/sources/src-273c2c87ddf0]] [[expo-hall-sessions/05_From Silicon to Rack Arm and Meta Scaling AI Infrastructure Through OC.pdf#page=4|PDF p.4]] [[knowledge/sources/src-273c2c87ddf0]] [[expo-hall-sessions/05_From Silicon to Rack Arm and Meta Scaling AI Infrastructure Through OC.pdf#page=8|PDF p.8]] [[knowledge/sources/src-273c2c87ddf0]] [[expo-hall-sessions/05_From Silicon to Rack Arm and Meta Scaling AI Infrastructure Through OC.pdf#page=10|PDF p.10]] [[knowledge/sources/src-273c2c87ddf0]] [[expo-hall-sessions/05_From Silicon to Rack Arm and Meta Scaling AI Infrastructure Through OC.pdf#page=11|PDF p.11]]
- LITEON 的1.1MW是5+1冗余容量，最大装机1.3MW，而N+N只有660kW；PSU/CBU/BBU量产分别指向2027年，并不是2026年已有整套量产可靠性结果。[[knowledge/sources/src-e1afbfae08ba]] [[expo-hall-sessions/08_LITEON 1MW Power Rack Solution for AI Data Center presented by LITEON.pdf#page=3|PDF p.3]] [[knowledge/sources/src-e1afbfae08ba]] [[expo-hall-sessions/08_LITEON 1MW Power Rack Solution for AI Data Center presented by LITEON.pdf#page=4|PDF p.4]] [[knowledge/sources/src-e1afbfae08ba]] [[expo-hall-sessions/08_LITEON 1MW Power Rack Solution for AI Data Center presented by LITEON.pdf#page=6|PDF p.6]]
- AiVRES 将下一代Rubin机柜规格与B200欧洲项目并列。后者的60天交付案例不能证明前者187/227kW规格已获同样部署验证。[[knowledge/sources/src-d9e1255601d0]] [[expo-hall-sessions/02_Aivres Liquid-Cooling AI Data Center Solutions Based on NVIDIA GPUs, p.pdf#page=13|PDF p.13]] [[knowledge/sources/src-d9e1255601d0]] [[expo-hall-sessions/02_Aivres Liquid-Cooling AI Data Center Solutions Based on NVIDIA GPUs, p.pdf#page=24|PDF p.24]]

## 用于推理架构的验收流程（综合建议）
1. **定义任务及SLO**：完成一个合格agent任务的成本、TTFT/TPOT/端到端p99，不能只取token价格或单算子吞吐。
2. **统一系统边界**：计算、内存、互联、冗余电源、CDU/设施功率均进入账本；名牌容量不等于运行功率。
3. **锁定成熟度**：可购料号、固件版本、量产日期、已部署规模与现场运行时间分别索证。
4. **异常工况**：热稳态、N-1、链路故障、内存压力、并发工具调用、冷启动下复测尾延迟。
5. **先对齐后比较**：同负载、同正确率、同延迟门槛、同功率边界；条件不全时保留为候选方案，不制造排名。

## 未决问题
厂商的“效率”可能分别指算力/W、可用容量、热交换比、转换效率或开发周期。每项须回源确认分母及测量方法，再进入商业模型。参见 [[knowledge/concepts/network-inference-acceptance]] 与 [[knowledge/comparisons/network-optics-evidence-ladder]]。


## 按决策问题继续阅读

- [[knowledge/comparisons/expo-power-conversion-boundaries]]
- [[knowledge/comparisons/expo-thermal-performance-contract]]
- [[knowledge/comparisons/expo-inference-cost-contract]]
- [[knowledge/comparisons/network-channel-interface-budget]]
