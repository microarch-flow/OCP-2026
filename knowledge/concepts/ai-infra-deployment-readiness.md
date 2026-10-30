---
type: "concept"
title: "部署就绪不是部件通过：从芯片到设施的验收链"
tags: ["ai-infra", "inference-architecture"]
---

# 部署就绪不是部件通过：从芯片到设施的验收链

## 定义
部署就绪要求部件、系统、集群、制造过程、设施动态行为与运维恢复同时有证据。“设计可用”与“日复一日可交付”是不同问题。

## 来源链与对应缺口
- **铜fabric**：PRBS合格不能覆盖带载重传、热漂移、collective straggler；还缺统一故障注入阈值。[[knowledge/sources/src-79e676213ada]]，[[ai-clusters/Test-Methodology-and-Practice-for-Multi-Accelerator-Copper-Scaleup-Domain-Interconnect-and-Communication-Library.pdf#page=5|PDF p.5]] [[ai-clusters/Test-Methodology-and-Practice-for-Multi-Accelerator-Copper-Scaleup-Domain-Interconnect-and-Communication-Library.pdf#page=6|PDF p.6]] [[ai-clusters/Test-Methodology-and-Practice-for-Multi-Accelerator-Copper-Scaleup-Domain-Interconnect-and-Communication-Library.pdf#page=7|PDF p.7]]
- **AEC**：Meta经验把CMIS/firmware reset race、cross-NIC互通、thermal cycling、SPC/MES/工厂产线加入qualification。[[knowledge/sources/src-0d0cf7f22ace]]，[[ai-open-data-center/Large-Scale Deployment of 800Gb-s Active Electrical Cables in Meta Data Centers for AI Applications.pdf#page=7|PDF p.7]] [[ai-open-data-center/Large-Scale Deployment of 800Gb-s Active Electrical Cables in Meta Data Centers for AI Applications.pdf#page=8|PDF p.8]] [[ai-open-data-center/Large-Scale Deployment of 800Gb-s Active Electrical Cables in Meta Data Centers for AI Applications.pdf#page=9|PDF p.9]] [[ai-open-data-center/Large-Scale Deployment of 800Gb-s Active Electrical Cables in Meta Data Centers for AI Applications.pdf#page=13|PDF p.13]]
- **液冷设施**：IST静态最大负载不能验证AI workload动态响应，Level5b使用真实compute调PID、定operating envelope、校准digital twin。[[knowledge/sources/src-5f5db420b1c0]]，[[ai-open-data-center/COMMISSIONING LIQUID COOLED DATA CENTERS WITH COMPUTING EQUIPMENT FOR OPERATIONAL READINESS.pdf#page=3|PDF p.3]] [[ai-open-data-center/COMMISSIONING LIQUID COOLED DATA CENTERS WITH COMPUTING EQUIPMENT FOR OPERATIONAL READINESS.pdf#page=9|PDF p.9]]
- **机械与维护**：automation-native optics/trays需要刚性抓取、统一基准、可验证seating和减少自由度，且同时服务人和机器人。[[knowledge/sources/src-8c4b19335fd8]]，[[ai-open-data-center/02_Automation-Ready Infrastructure Design From Light to Compute.pdf#page=7|PDF p.7]] [[ai-open-data-center/02_Automation-Ready Infrastructure Design From Light to Compute.pdf#page=12|PDF p.12]] [[ai-open-data-center/02_Automation-Ready Infrastructure Design From Light to Compute.pdf#page=17|PDF p.17]]
- **建筑与容量**：OpenDC v0.7的2027/2028+密度、净空、重量与pipe边界是设计目标，不能把chip peak直接当可部署容量。[[knowledge/sources/src-921c40327385]]，[[ai-open-data-center/Next-Generation ML Infrastructure- The Open DC Architecture.pdf#page=4|PDF p.4]] [[ai-open-data-center/Next-Generation ML Infrastructure- The Open DC Architecture.pdf#page=6|PDF p.6]] [[ai-open-data-center/Next-Generation ML Infrastructure- The Open DC Architecture.pdf#page=7|PDF p.7]] [[ai-open-data-center/Next-Generation ML Infrastructure- The Open DC Architecture.pdf#page=12|PDF p.12]]
- **储能安全**：product certification、application、installation、acceptance四层须分别核验；具体法规由实际地区/时间/方案决定。[[knowledge/sources/src-6a834c28374b]]，[[ai-open-data-center/The New Focus on Energy Storage Systems Safety.pdf#page=3|PDF p.3]] [[ai-open-data-center/The New Focus on Energy Storage Systems Safety.pdf#page=4|PDF p.4]]

## 共识与不可比较处
共识不是某个厂商更可靠，而是最初qualification的外推边界有限。AEC160个匿名供应商样本不能推整fleetMTBF；24–72h burn-in不能证明多年寿命；OpenDC每foot线性密度不能换成每rack的功率承诺。

## 对推理硬件商业化的决策清单（综合推论）
1. 芯片BOM与软件可复现：模型、精度、上下文、p99、batch/并发与功率。
2. 系统互操作：NIC/firmware/CMIS/CCL/driver版本矩阵。
3. 动态验收：burst、temperature cycling、monitoring overhead、灰故障与恢复。
4. 制造可追溯：多厂/产线process capability、持续SPC/MES、变更回归。
5. 设施就绪：功率瞬态、冷却control、结构/净空、人员与机器人维护。
6. 运营承诺：RMA、spares、MTTR、升级/回滚和跨供应商责任。

## 未决问题
资料没有一套横跨上述层次的同一推理系统/同一SLA成本模型。不可据此给“某加速器更划算”的采购结论。
