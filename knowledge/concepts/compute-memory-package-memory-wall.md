---
type: concept
title: "封装内存墙：shoreline、热、容量与带宽的不同约束"
tags: [ocp2026, concept, compute-memory]
---

# 封装内存墙：shoreline、热、容量与带宽的不同约束

## 核心判断
把更多内存靠近compute可以降低数据移动能耗，但会竞争die edge、bond/TSV、面积、热通道与供电资源。不同方案“突破内存墙”的对象不同，不能用一个TB/s值排名。

| 路线 | 主要收益机制 | 新约束/代价 | 来源成熟度 |
|---|---|---|---|
| Custom HBM base die | 把PHY/controller从compute die移出，释放面积/shoreline | base-die D2D功耗、stack热阻、volume hybrid-bond yield、memory vendor协同 | [[knowledge/sources/src-883fafcb5701\|Marvell]]：IP/设计主张+文献/路线估算，部分验证待做 |
| DRAM-on-compute | 更密hybrid bonds、独立bank宽bus、低距离 | capacity density/层数、thermal、repair、制造成本 | [[knowledge/sources/src-ea79b85c21ec\|GUC]]：vendor方案数据，需区分silicon-proven代际与execution |
| Socketed buffered LPDDR | 大量可换module扩capacity，绕开HBM先进封装 | 数百SerDes、板/基板routing、connector、850W级memory预算 | [[knowledge/sources/src-baa654c52de3\|HPCM/Weaver]]：concept→PoC目标 |
| 外部CXL/PCM/SSD tier | 独立扩容、提高reuse、pool utilization | 访问路径、容量阈值、随机IOPS、管理与故障域 | [[knowledge/concepts/compute-memory-kv-placement\|CMS/KV路径]] |
| 光chiplet | 跨package/rack增加reach/radix | EIC/PIC D2D、clock域、FEC/retimer、fiber attach、thermal/test | [[knowledge/sources/src-7d3aae069517\|Eliyan]]：接口方案比较 |

## 比较时必须统一的分母
- TB/s per stack、per reticle die、per package与内部aggregate NoC throughput不同。
- pJ/bit可能只含PHY，也可能含controller或完整path；normal/peak activity不同。
- W/mm²可能是TDP除logic面积，也可能是局部HBM PHY热点；不可混用。
- 4layer DRAM-on-logic对12layer HBM的MB/mm²比较含层数差异，不是单纯cell density。
- package-level目标节能/面积回收并不等于相同比例的LLM tokens/s提高。

## 共同设计的因果链（分析推论）
workload访问分布 → memory/controller activity → D2D功率 → PDN/温度 → 频率/错误与节流 → 有效带宽/服务延迟。

因此应让performance model与power/thermal/PI至少共享activity、voltage、temperature边界。[[knowledge/concepts/compute-memory-federated-model-contract|模型契约]] 提供版本/有效范围/units记录，避免将未校准的不同厂商“峰值”拼成不存在的最优系统。

## 未解决问题
缺少统一BOM、yield/repair、sustained BW、工作负载能耗和p99测试，当前材料足以形成设计空间与待验证清单，不足以宣布某路线普遍获胜。
