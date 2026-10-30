---
id: "src-1b36f933cf3b"
type: "source"
title: "遥测聚合流水线：时间、空间与上下文必须共同保真"
source_path: "systems-management/Creating-Aggregation-Pipelines-to-Conquer-Large-Telemetry-Challenges.pdf"
source_git_blob_sha: "c631116e86de0f430e9a6f38c6182f3f00aa9cfa"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 28
review_status: "analyzed-text"
evidence_pages: [2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 20, 21, 22, 26, 27]
tags: ["ocp", "source", "platform", "systems-management"]
text_reviewed: true
key_pages_visual_checked: []
updated: "2026-10-30"
---

# 遥测聚合流水线：时间、空间与上下文必须共同保真

> 阅读范围：已阅读本文件全部可提取文字（28页）。未完成图表视觉核对；不把文字提取视作图形关系验证。

## 核心结论

- SCIM先提出协议无关leaf/aggregation/filter/report/control角色，再映射Redfish、YANG、OTel等，而非统一成单一transport。[[systems-management/Creating-Aggregation-Pipelines-to-Conquer-Large-Telemetry-Challenges.pdf#page=3|PDF p.3]][[systems-management/Creating-Aggregation-Pipelines-to-Conquer-Large-Telemetry-Challenges.pdf#page=4|PDF p.4]]
- 聚合有时间降采样、空间跨源、上下文筛选三类；对异常诊断，简单平均可能抹掉短时峰值，stats/irregular表示能保留不同信息。[[systems-management/Creating-Aggregation-Pipelines-to-Conquer-Large-Telemetry-Challenges.pdf#page=7|PDF p.7]][[systems-management/Creating-Aggregation-Pipelines-to-Conquer-Large-Telemetry-Challenges.pdf#page=8|PDF p.8]][[systems-management/Creating-Aggregation-Pipelines-to-Conquer-Large-Telemetry-Challenges.pdf#page=9|PDF p.9]][[systems-management/Creating-Aggregation-Pipelines-to-Conquer-Large-Telemetry-Challenges.pdf#page=11|PDF p.11]][[systems-management/Creating-Aggregation-Pipelines-to-Conquer-Large-Telemetry-Challenges.pdf#page=12|PDF p.12]]

## 关键证据

- Regular、stats、irregular time series转换需针对数学工具/带宽/噪声目的；pattern detector支持level/edge输出和release hysteresis防抖。[[systems-management/Creating-Aggregation-Pipelines-to-Conquer-Large-Telemetry-Challenges.pdf#page=10|PDF p.10]][[systems-management/Creating-Aggregation-Pipelines-to-Conquer-Large-Telemetry-Challenges.pdf#page=13|PDF p.13]][[systems-management/Creating-Aggregation-Pipelines-to-Conquer-Large-Telemetry-Challenges.pdf#page=14|PDF p.14]]
- metric含units/scale/type/path等；Bundle定义单节点时间并行序列，Super Bundle要求多节点metric名、格式、顺序匹配，均限定regular/stats。[[systems-management/Creating-Aggregation-Pipelines-to-Conquer-Large-Telemetry-Challenges.pdf#page=20|PDF p.20]][[systems-management/Creating-Aggregation-Pipelines-to-Conquer-Large-Telemetry-Challenges.pdf#page=21|PDF p.21]][[systems-management/Creating-Aggregation-Pipelines-to-Conquer-Large-Telemetry-Challenges.pdf#page=22|PDF p.22]]
- 作者希望靠近源进行pattern/alert，最后仍需minimal PoC和流水线表示方式验证。[[systems-management/Creating-Aggregation-Pipelines-to-Conquer-Large-Telemetry-Challenges.pdf#page=26|PDF p.26]][[systems-management/Creating-Aggregation-Pipelines-to-Conquer-Large-Telemetry-Challenges.pdf#page=27|PDF p.27]]

## 指标与条件

100,000+节点是SCIM charter目标规模，不是本方案已跑规模。没有压缩率、检测准确率、采集开销或端到端时延。[[systems-management/Creating-Aggregation-Pipelines-to-Conquer-Large-Telemetry-Challenges.pdf#page=2|PDF p.2]]

## 图表与架构

未视觉核对曲线示意；未从示意图读取真实传感器值或统计结果。

## 关联与比较

与Redfish TelemetryBundle/别名有重叠但定义不等价：SCIM强调流水线运算语义，DMTF强调API/编码；应明确采样区间和单位后再聚合。

## 不确定性与待验证

需补缺测插值标记、不同频率时间对齐、时钟误差、counter reset、隐私过滤和聚合后峰值/尾部损失。

