---
type: concept
title: "面向 架构探索 DSL/IR 的多保真模型契约"
tags: [ocp2026, concept, compute-memory]
---

# 面向 架构探索 DSL/IR 的多保真模型契约

## 核心判断
AI 驱动架构探索应在 **可追溯、有效范围明确的模型** 上优化，不应该把一个没有适用条件的模型当作事实。[[knowledge/sources/src-f364f1fe74e8|Federated Chiplet Design and Simulation]] 的贡献是 model/service contract，而不是已完成的全自动 PPAC 优化。

## 可借鉴的 IR/model 边界
| 材料中的 Manifest 字段 | 对 架构探索 DSL/IR 的建议映射（分析推论） |
|---|---|
| identity/version/hash | 锁定一次 DSE 所用参数、模型及源材料版本 |
| domains | 区分 functional、performance、thermal、PI 等后端能力 |
| boundary contract | 输入/输出的单位、端口、范围、时间步长 |
| validity/assumptions/error bounds | 防止在未验证 batch、频率、温度或流量区间外直接外推 |
| execution method | local analytic、trace replay、surrogate 或 remote black-box |
| security/commercial policy | 对受限制模型保留查询预算、许可与输出粒度 |

## 分层探索，而非一次“万能仿真”
1. 用简单带宽/容量模型排除明显不可行设计。
2. 用 queue/credit/workload 模型评估利用率与尾延迟。
3. 在候选点调用功耗/热/PI 的更高保真模型；迭代到约束收敛。
4. 保存输入、模型 hash、范围校验和结果来源；不同保真度不要合并成无标记的“实测值”。

该分层流程是本库建议。原演讲 Phase 1 仅 power + thermal、两芯粒；不能把 SI/PI/functional 或自动选芯粒能力写为已交付。

## 与芯粒互连的连接
[[knowledge/concepts/compute-memory-chiplet-link-efficiency]] 给出需要 manifest 承载的协议/流量参数。[[knowledge/concepts/compute-memory-cxl-failure-domain]] 提醒性能模型之外还需可观察的失效/恢复语义。

## 检验标准
同一设计的结果能否随模型版本复现？是否在 validated range 内？coupling 是否收敛？surrogate 误差是否可能改变候选排序？不能回答这些问题时，应保留“不确定”而不是输出虚假的小数精度。
