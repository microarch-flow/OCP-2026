---
type: guide
title: 从推理系统问题进入材料
updated: 2026-10-30
tags: [ocp2026, guide]
---

# 从推理系统问题进入材料

不必按照 501 个文件的文件名顺序阅读。先提出一个具体系统问题，再沿概念页、对比页、源卡和原始 PDF 逐层查看证据。下面是当前已经有分析支撑的阅读路线，不代表所有材料的最终结论。范围以 [[knowledge/coverage|覆盖率]] 为准。

## 1 先确定要改善哪一种推理指标

从 [[knowledge/concepts/ai-infra-inference-serving-shapes|推理服务的组织方式]] 和 [[knowledge/concepts/network-inference-acceptance|推理网络的验收边界]] 开始。

阅读时分别记录：模型、输入/输出长度、并发、吞吐、TTFT、单 token 延迟和尾部统计。不要把集合通信带宽或训练扩展效率直接当作推理 p99 的证据。资源拆分和更多互连层次需要以具体 SLO 为理由，不以拓扑复杂度本身为收益。

## 2 扩大内存之后还要问什么

先看 [[knowledge/concepts/compute-memory-capacity-vs-datapath|容量收益与数据路径收益的归因]] 和 [[knowledge/concepts/compute-memory-cxl-failure-domain|CXL 的故障域与可观测性]]，再回到 [[knowledge/sources/src-38d499006926|Meta 的 CXL 机群故障分析]]。

重点问题：容量、带宽、数据路径、复用命中率分别改变了什么？比较对象是否使用相同容量？新增设备发生故障时能否定位并限制影响范围？业务损失、维修和软件恢复是否计入成本？没有共同测试条件的倍率先保持不可比较。

## 3 光互连与多路径网络怎样比较

先读 [[knowledge/comparisons/network-optics-integration-tradeoffs|光学集成路线的取舍]] 与 [[knowledge/comparisons/network-transport-and-buffer-context|传输及缓冲的工作负载边界]]。

然后看 [[knowledge/concepts/network-optics-reliability|光学可靠性证据]]。将现有生产观测、原型验证、目标规格和待量产路线图区分开。光模块功耗降低不等于整机功耗同幅降低；系统小时、模块小时、故障类型也不能混用。

## 4 供电与冷却怎样影响可交付系统

从 [[knowledge/sources/src-42ab3107064a|Open Rack Wide 的进度与验证]]、[[knowledge/sources/src-7371e57b6934|400V 与 800V 板级供电要求]] 和 [[knowledge/sources/src-368dfc5ed300|液冷机柜运输与存放]] 进入。

分别检查热、电、机械、运维边界。额定能力、验证载荷和实际工作负载不是同一项指标；测试通过也不自动代表已经量产。未来效率目标必须保留其负载区间、输出电压与交付时间。

## 5 如何把供应商描述变成可验证的模型

阅读 [[knowledge/concepts/compute-memory-federated-model-contract|多供应商模型契约]]、[[knowledge/concepts/ai-infra-observability-contract|可观测性契约]] 与 [[knowledge/concepts/network-executable-validation|可执行网络验证]]。

关注能力、版本、参数单位、有效范围、时间步长、状态交互及验证用例。演讲中给出的示例任务不是设备实测；某一个子系统的验证也不能替代端到端系统验证。

再看 [[knowledge/sources/src-92d1f86e9495|d-Matrix 的 Push Mode 与跨传输抽象]]：区分地址映射、打包和物理拓扑，与操作接口、完成条件、同步、顺序及重试语义。材料展示前一部分，不应因此假定后一部分已经完整定义。

## 使用知识库时的四个检查

1. 点开 PDF 页级链接，确认结论和原始图表一致。
2. 查明数字是测量、模型估计、设计目标还是宣传主张。
3. 看源卡的适用条件与未验证事项，再决定能否迁移到自己的问题。
4. 新问题仅在获准保存到本公开仓库后，整理为带来源的待验证问题；不自动写入私人聊天或公司内部信息，也不将生成式回答循环引用成新的独立证据。

维护方法见 [[knowledge/AGENTS|维护约定]]，全部来源见 [[knowledge/source-manifest|来源清单]]。
