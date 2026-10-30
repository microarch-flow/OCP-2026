---
id: "src-3bd90d8e4e75"
type: "source"
title: "Redfish别名与遥测标签：已发布Alias与WIP ServiceAlias分开看"
source_path: "manageability-workshop/Redfish Aliasing Support and Redfish Streaming Telemetry Enhancements.pdf"
source_git_blob_sha: "9e17fe5e50bdc4b09bbabbb931af7df881cde55a"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 15
review_status: "analyzed-text"
evidence_pages: [3, 4, 5, 7, 11, 12, 13, 14]
tags: ["ocp", "source", "platform", "manageability-workshop"]
text_reviewed: true
key_pages_visual_checked: []
updated: "2026-10-30"
---

# Redfish别名与遥测标签：已发布Alias与WIP ServiceAlias分开看

> 阅读范围：已阅读本文件全部可提取文字（15页）。未完成图表视觉核对；不把文字提取视作图形关系验证。

## 核心结论

- 用户可写Alias解决跨厂商Id发现成本，并允许为物理/业务角色命名；演讲称已加入Redfish 1.25.0与schema 2026.2。[[manageability-workshop/Redfish Aliasing Support and Redfish Streaming Telemetry Enhancements.pdf#page=3|PDF p.3]][[manageability-workshop/Redfish Aliasing Support and Redfish Streaming Telemetry Enhancements.pdf#page=4|PDF p.4]]
- ServiceAlias是服务拥有、只读、按schema规则构造的标准名称，仍in progress；TelemetryBundle和TelemetryStream也是提案/工作项。不能把三者一概标为已支持。[[manageability-workshop/Redfish Aliasing Support and Redfish Streaming Telemetry Enhancements.pdf#page=7|PDF p.7]][[manageability-workshop/Redfish Aliasing Support and Redfish Streaming Telemetry Enhancements.pdf#page=12|PDF p.12]][[manageability-workshop/Redfish Aliasing Support and Redfish Streaming Telemetry Enhancements.pdf#page=14|PDF p.14]]

## 关键证据

- Alias路径使用~前缀，可免逐级发现；同collection及共同parent下同schema类型collection要求唯一。重分配会清旧值并发AliasValueReassigned事件。[[manageability-workshop/Redfish Aliasing Support and Redfish Streaming Telemetry Enhancements.pdf#page=4|PDF p.4]]
- Telemetry Name由Schema/路径/属性构造，Label拼接ServiceAlias并可用户Alias覆盖，数组需额外消歧。单位/类型由schema承载。[[manageability-workshop/Redfish Aliasing Support and Redfish Streaming Telemetry Enhancements.pdf#page=11|PDF p.11]]
- Bundle可共享time/name/label来压缩多传感器或时间序列重复字段；epoch时间戳可在bundle和record层出现。[[manageability-workshop/Redfish Aliasing Support and Redfish Streaming Telemetry Enhancements.pdf#page=12|PDF p.12]][[manageability-workshop/Redfish Aliasing Support and Redfish Streaming Telemetry Enhancements.pdf#page=13|PDF p.13]]

## 指标与条件

p.5代码例展示三级发现GET可缩成直接单GET，非端到端网络延迟benchmark。16个温度/每5秒10分钟是打包例子，不是性能/采样上限。[[manageability-workshop/Redfish Aliasing Support and Redfish Streaming Telemetry Enhancements.pdf#page=5|PDF p.5]][[manageability-workshop/Redfish Aliasing Support and Redfish Streaming Telemetry Enhancements.pdf#page=12|PDF p.12]]

## 图表与架构

未视觉核对代码/JSON页；不把示意JSON当可直接运行格式或最终schema。

## 关联与比较

与GPU可观测性中的命名缺口直接相接；别名稳定性仍受重绑定/硬件替换影响，长期时序应同时保留资源身份与别名变更历史。后者为工程推论。

## 不确定性与待验证

需验证服务是否支持相应版本、Alias授权与持久性、热插拔序号重排、多厂商排序规则；不能因名称一致就认为采样条件或指标定义可直接横比。

