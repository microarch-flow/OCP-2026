---
type: "concept"
title: "从电网与冷却到推理 SLA：跨层功率契约"
tags: ["ai-infra", "inference-architecture"]
---

# 从电网与冷却到推理 SLA：跨层功率契约

## 综合判断
GPU额定功率、可并网容量、储能kWh、cooling PUE都不是请求SLA。商业化需要明确在正常、降载、短故障、长故障与维修期间，哪些工作可延后、哪些必须继续，以及最小可承诺goodput。

## 时间与空间的分层
Schneider将持续AI buffering（ms–s）、FRT（100+ms）、UPS（分钟）、demand response（小时）分开，rack电容、powertrain power-battery与campus储能各有边界。EPC强调converter和grid-forming控制而非单有电池；NVIDIA Flex则要求受保护工作不因粗暴curtailment掉线。[[knowledge/sources/src-85526d8d116a]] [[ai-open-data-center/08_Supporting load smoothing, Fault Ride-through (FRT), and back up in 80.pdf#page=7|PDF p.7]] [[ai-open-data-center/08_Supporting load smoothing, Fault Ride-through (FRT), and back up in 80.pdf#page=11|PDF p.11]] [[knowledge/sources/src-0434888344e7]] [[ai-open-data-center/Enabling Grid-Compliant Data Center Growth Through Advanced Energy Storage.pdf#page=6|PDF p.6]] [[knowledge/sources/src-205bcfe0483d]] [[ai-open-data-center/05_Flexibility the Grid Can Count On Turning Curtailable Load Into Interc.pdf#page=6|PDF p.6]]

**推论**：hardware power cap的快环、请求admission的毫秒环、作业迁移/设施dispatch慢环应共享边界条件，但不必由同一controller逐事件决策。

## 储能不能只按能量选
Echion的模型中110MW短时recharge约束使不同charge C-rate需要183/110/18MWh。它提示charge power可能主导overbuild，但数字是特定280MW hall模拟；cell循环寿命、浅buffer循环与实柜寿命不是同一指标。成本仅cells-only，不能代入完整TCO。[[knowledge/sources/src-ed31e0df1756]] [[ai-open-data-center/Path to the Megawatt Rack- A Grid-Aware, Symmetric High-Power UPS for AI Data Centers.pdf#page=9|PDF p.9]] [[ai-open-data-center/Path to the Megawatt Rack- A Grid-Aware, Symmetric High-Power UPS for AI Data Centers.pdf#page=10|PDF p.10]] [[ai-open-data-center/Path to the Megawatt Rack- A Grid-Aware, Symmetric High-Power UPS for AI Data Centers.pdf#page=13|PDF p.13]]

800V架构也分改造路径与阶段：power rack/power center/power block、保护/接口/认证各有准备度。NVIDIA五阶段路线要求仿真、原型、认证、生产与部署证据，不因升压自动获得可用性。[[knowledge/sources/src-5b3cc2f434f1]] [[ai-open-data-center/01_800 VDC AI Factories From Architecture Alignment to Industry Deploymen.pdf#page=4|PDF p.4]] [[ai-open-data-center/01_800 VDC AI Factories From Architecture Alignment to Industry Deploymen.pdf#page=17|PDF p.17]] [[ai-open-data-center/01_800 VDC AI Factories From Architecture Alignment to Industry Deploymen.pdf#page=18|PDF p.18]]

## 冷却释放的MW，不等于同比例tokens
NVIDIA五城/250MW模型显示高温TCS与专用loop可降低设施开销，Chicago D2 S30→S45给23.9MW额外compute capacity；这是容量预算，不是已测吞吐。需确认高温下GPU时钟/内存错误/TPOT，且peak PUE与annual PUE用于不同决策。[[knowledge/sources/src-8779c0d1fef0]] [[ai-open-data-center/Evaluating Heat Rejection System Configurations for AI Data Centers- A Multi-Metric Analysis.pdf#page=13|PDF p.13]] [[ai-open-data-center/Evaluating Heat Rejection System Configurations for AI Data Centers- A Multi-Metric Analysis.pdf#page=16|PDF p.16]]

模块化液路需全路径pressure/flow模型与现场验收；branch assemblies可能已耗尽15psi级系统预算。维护频率MTBR（Between Repairs）不能误读成MTTR（修复耗时），频繁开合本身增加暴露。[[knowledge/sources/src-23703bf6a9da]] [[ai-open-data-center/Challenges for High Density Workloads in Modular Data Center.pdf#page=8|PDF p.8]] [[ai-open-data-center/Challenges for High Density Workloads in Modular Data Center.pdf#page=17|PDF p.17]] [[knowledge/sources/src-ec3de999ce76]] [[ai-open-data-center/OCP Modular Technology Cooling Workstream - 2026 Update.pdf#page=15|PDF p.15]] [[ai-open-data-center/OCP Modular Technology Cooling Workstream - 2026 Update.pdf#page=18|PDF p.18]]

## 三个容易误用的商业指标
1. **Curtailment%不是停机小时%**：171的0.5%与177h不能直接换算availability，需原研究energy/duration/partial-power定义。[[ai-open-data-center/05_Flexibility the Grid Can Count On Turning Curtailable Load Into Interc.pdf#page=3|PDF p.3]]
2. **Zero on-site water不是全系统零水**：170明确site+source边界；发电组合可能把水耗移到上游。[[knowledge/sources/src-70ad817f37fe]] [[ai-open-data-center/04_Can the Industry Sustain AI The Water-Energy Nexus Debate.pdf#page=4|PDF p.4]] [[ai-open-data-center/04_Can the Industry Sustain AI The Water-Energy Nexus Debate.pdf#page=5|PDF p.5]]
3. **Speed-adjusted LCOE不是电费**：CMU把未上电GPU机会成本加进LCOE，30MW案例grid$0.054→$1.01/kWh是建造时差/价值假设，不是用户账单。[[knowledge/sources/src-df915f7ad91c]] [[ai-open-data-center/Technoeconomic comparison of DC-and AC-coupled solar microgrids, natural gas, and grid.pdf#page=6|PDF p.6]] [[ai-open-data-center/Technoeconomic comparison of DC-and AC-coupled solar microgrids, natural gas, and grid.pdf#page=13|PDF p.13]]

## 建议的跨层交付契约
- 输入：utility power envelope、可用储能SOC、温度/流量/压降、故障/维护状态。
- 约束：不可中断tenant、minimum token rate、p99 TTFT/TPOT、最大功率ramp、reserve autonomy。
- 动作：功率上限、admission、batch/模型路由、非紧急任务迁移；明确谁可批准及rollback。
- 证据：真实请求trace与电/热波形同时间基准，记录SLO违约、能量、恢复时间，而非仅平滑后的POI功率。

关联：[[knowledge/concepts/ai-infra-observability-contract]]、[[knowledge/concepts/ai-infra-locality-and-control-timescales]]、[[knowledge/comparisons/ai-infra-performance-claim-evidence-matrix]]。
