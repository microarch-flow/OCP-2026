---
id: "src-c76628aa1fcd"
type: "source"
title: "Precision Time for AI Infrastructure: Deploying PTP Boundary Clocks at Scale"
source_path: "Time Appliances/Precision Time for AI Infrastructure- Deploying PTP Boundary Clocks at Scale.pdf"
source_git_blob_sha: "459dc6b1d258d69df8eeb9abffca748d5fc52fd9"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 13
review_status: "analyzed-visual"
evidence_pages: [2, 3, 4, 7, 8, 9, 10, 11, 12]
text_reviewed: true
key_pages_visual_checked: [6]
tags: ["ocp2026", "networking"]
concepts: ["[[knowledge/concepts/network-clock-evidence]]"]
---

# Precision Time for AI Infrastructure: Deploying PTP Boundary Clocks at Scale

## 核心结论
BC通过上游同步本地clock、再成为下游master，把grandmaster fanout与PTP处理本地化；SONiC开放栈仍需要PHY/MAC timestamp、PHC driver、ASIC FW与SAI实现共同支持，不能只开启container即假定精确时间。[[Time Appliances/Precision Time for AI Infrastructure- Deploying PTP Boundary Clocks at Scale.pdf#page=2|PDF p.2]][[Time Appliances/Precision Time for AI Infrastructure- Deploying PTP Boundary Clocks at Scale.pdf#page=3|PDF p.3]][[Time Appliances/Precision Time for AI Infrastructure- Deploying PTP Boundary Clocks at Scale.pdf#page=8|PDF p.8]]

## 关键证据
Phase1目标202611 release：single-ASIC pizza-box、one-step hardware timestamp、L3/UDP、BC；HLD已列，code PR将来提供。P2P TC与2-step BC属后续合作项，不是本次Phase1承诺。[[Time Appliances/Precision Time for AI Infrastructure- Deploying PTP Boundary Clocks at Scale.pdf#page=4|PDF p.4]][[Time Appliances/Precision Time for AI Infrastructure- Deploying PTP Boundary Clocks at Scale.pdf#page=12|PDF p.12]]
SAI PTP trap负责包上送及FW生命周期，PORT_ATTR_PTP_MODE启用one-step PHY timestamp；公共YANG/CLI、SWSS、COPP/PTP container之外，platform还需driver/PHC timestamp路径。[[Time Appliances/Precision Time for AI Infrastructure- Deploying PTP Boundary Clocks at Scale.pdf#page=7|PDF p.7]][[Time Appliances/Precision Time for AI Infrastructure- Deploying PTP Boundary Clocks at Scale.pdf#page=8|PDF p.8]]

## 指标与条件
文件没有ns误差、BC级数累积、CPU负载、failover、PTP packet-rate或业务p99数据。测试拓扑是SROS GM→SONiC BC→SONiC OC，并给domain44配置示例；是功能setup，不是大规模性能验证。[[Time Appliances/Precision Time for AI Infrastructure- Deploying PTP Boundary Clocks at Scale.pdf#page=9|PDF p.9]][[Time Appliances/Precision Time for AI Infrastructure- Deploying PTP Boundary Clocks at Scale.pdf#page=10|PDF p.10]]

## 图表与架构
已核p.6组件图：CONFIG/STATE/APPL/COUNTERS/ASIC DB连接SWSS、PTP manager/ptp4l/telemetry及syncd/SAI；避免误把software DB路径当hardware timestamp关键路径。

## 关联与比较
[[knowledge/concepts/network-clock-evidence]]；[[knowledge/sources/src-aba4b9355d9b]]多domain/standby是更高层使用需求；[[knowledge/sources/src-25482e5ef2a3]]处理NIC到CPU/GPU的last inch。

## 不确定性与待验证
需确认目标release实际合入情况，本卡只保留演讲时状态，不查询外部新版本。选择oscillator要纳入thermal/holdover/jitter；不只确认PTP protocol flag。[[Time Appliances/Precision Time for AI Infrastructure- Deploying PTP Boundary Clocks at Scale.pdf#page=11|PDF p.11]]
