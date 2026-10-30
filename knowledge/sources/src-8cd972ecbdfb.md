---
id: "src-8cd972ecbdfb"
type: "source"
title: "Applying OCP ORv3 and ORW Design Principles to Rack-Scale Arm AI Infrastructure with Supermicro"
source_path: "Rack & Power/Applying OCP ORv3 and ORW Design Principles to Rack-Scale Arm AI Infrastructure with Supermicro.pdf"
source_git_blob_sha: "46db3875fb408904a3dbc58519414ee03ec2dad2"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 13
review_status: "analyzed-visual"
evidence_pages: [2, 3, 4, 5, 6, 7, 8, 9, 11, 12]
text_reviewed: true
key_pages_visual_checked: [7, 8]
tags: ["ocp2026", "source", "power-cooling", "arm", "rack-design", "serviceability"]
concepts: []
---

# Arm 与 Supermicro：先按 agent 工作负载定义机架，再协同电热与维护

> 原始题名：Applying OCP ORv3 and ORW Design Principles to Rack-Scale Arm AI Infrastructure with Supermicro。阅读范围：完整可提取文字（物理 PDF 共 13 页），关键引用图表另做视觉核对。

## 核心结论

- 方案把 agentic 工作负载分成 CPU/运行时、数据服务和模型服务；机架设计不仅受加速器功率影响，也受内存容量、网络带宽、数据局部性与编排吞吐约束。 [[Rack & Power/Applying OCP ORv3 and ORW Design Principles to Rack-Scale Arm AI Infrastructure with Supermicro.pdf#page=2|PDF p.2]]、[[Rack & Power/Applying OCP ORv3 and ORW Design Principles to Rack-Scale Arm AI Infrastructure with Supermicro.pdf#page=3|PDF p.3]]、[[Rack & Power/Applying OCP ORv3 and ORW Design Principles to Rack-Scale Arm AI Infrastructure with Supermicro.pdf#page=4|PDF p.4]]
- ORv3 与 ORW 示例保持开放电源、冷却、机械及管理接口，宽度、节点组织、CDU 位置和电源架冗余随容量变化。没有给真实 agent 基准吞吐或每任务能耗。 [[Rack & Power/Applying OCP ORv3 and ORW Design Principles to Rack-Scale Arm AI Infrastructure with Supermicro.pdf#page=6|PDF p.6]]、[[Rack & Power/Applying OCP ORv3 and ORW Design Principles to Rack-Scale Arm AI Infrastructure with Supermicro.pdf#page=7|PDF p.7]]、[[Rack & Power/Applying OCP ORv3 and ORW Design Principles to Rack-Scale Arm AI Infrastructure with Supermicro.pdf#page=8|PDF p.8]]、[[Rack & Power/Applying OCP ORv3 and ORW Design Principles to Rack-Scale Arm AI Infrastructure with Supermicro.pdf#page=9|PDF p.9]]、[[Rack & Power/Applying OCP ORv3 and ORW Design Principles to Rack-Scale Arm AI Infrastructure with Supermicro.pdf#page=11|PDF p.11]]
- 原页内部数字存在不一致：ORv3 正文约 82.5 kW、图 84 kW；ORW 正文 44OU、图标 48OU。应索取正式 BOM/布局，不把本演讲当冻结设计。 [[Rack & Power/Applying OCP ORv3 and ORW Design Principles to Rack-Scale Arm AI Infrastructure with Supermicro.pdf#page=7|PDF p.7]]、[[Rack & Power/Applying OCP ORv3 and ORW Design Principles to Rack-Scale Arm AI Infrastructure with Supermicro.pdf#page=8|PDF p.8]]、[[Rack & Power/Applying OCP ORv3 and ORW Design Principles to Rack-Scale Arm AI Infrastructure with Supermicro.pdf#page=9|PDF p.9]]

## 关键证据

| 主张与信息 | 类型、边界与架构含义 | 原始出处 |
| --- | --- | --- |
| Arm 全栈贡献 | SBSA/SBMR 标准化、ADAC、FCSA、服务器硬件/固件框架；页脚标注部分贡献进行中、服务器规格为未来贡献 | [[Rack & Power/Applying OCP ORv3 and ORW Design Principles to Rack-Scale Arm AI Infrastructure with Supermicro.pdf#page=5\|PDF p.5]] |
| 机架可维护性作为接口验收 | 替换计算节点、维护电源架与液路、访问网络和线缆；未给 MTTR 或故障恢复测试 | [[Rack & Power/Applying OCP ORv3 and ORW Design Principles to Rack-Scale Arm AI Infrastructure with Supermicro.pdf#page=11\|PDF p.11]]、[[Rack & Power/Applying OCP ORv3 and ORW Design Principles to Rack-Scale Arm AI Infrastructure with Supermicro.pdf#page=12\|PDF p.12]] |
| ORv3 节点数解释 | 正文“16 nodes 2OU4N”与 128 CPUs / 图中 64 nodes 并存，合理解释为 16 个四节点机箱，但原用词须澄清 | [[Rack & Power/Applying OCP ORv3 and ORW Design Principles to Rack-Scale Arm AI Infrastructure with Supermicro.pdf#page=7\|PDF p.7]] |

## 指标与条件

| 指标 | 数值与单位 | 对象、条件、基线及缺失项 | 原始页 |
| --- | --- | --- | --- |
| ORv3 示例 | 128 CPUs，约 82.5 kW；3×72 kW shelf，2+1 | 21 英寸/44OU，液冷，机内 CDU；图标总功率 84 kW，不能无说明合并 | [[Rack & Power/Applying OCP ORv3 and ORW Design Principles to Rack-Scale Arm AI Infrastructure with Supermicro.pdf#page=7\|PDF p.7]]、[[Rack & Power/Applying OCP ORv3 and ORW Design Principles to Rack-Scale Arm AI Infrastructure with Supermicro.pdf#page=9\|PDF p.9]] |
| ORW 示例 | 148 nodes / 296 CPUs，约 185 kW；6×72 kW shelf，4+2 | 42 英寸，液冷，行级 CDU；正文 44OU 与图中 48OU 不一致 | [[Rack & Power/Applying OCP ORv3 and ORW Design Principles to Rack-Scale Arm AI Infrastructure with Supermicro.pdf#page=8\|PDF p.8]]、[[Rack & Power/Applying OCP ORv3 and ORW Design Principles to Rack-Scale Arm AI Infrastructure with Supermicro.pdf#page=9\|PDF p.9]] |
| AC 引入 | ORv3 6 路、ORW 12 路，415 V/60 A | 设计描述，未注明完整三相接线、功率因数和设施冗余边界，不由此计算可用容量 | [[Rack & Power/Applying OCP ORv3 and ORW Design Principles to Rack-Scale Arm AI Infrastructure with Supermicro.pdf#page=7\|PDF p.7]]、[[Rack & Power/Applying OCP ORv3 and ORW Design Principles to Rack-Scale Arm AI Infrastructure with Supermicro.pdf#page=8\|PDF p.8]] |

## 图表与架构

p.7/8 的架图展示电源架与计算层交错布置，以及 ORv3 占用机内 CDU 空间、ORW 使用外置 CDU 的容量差异。原页 ORv3 22,848 cores 与其板型/CPU 数难以直接核对，本文不采用该值推导算力。

## 关联与比较

- 本条先保留来源级证据；跨源比较应检查工作负载、系统边界、实验条件和时间尺度，不能仅按标题归类后推导性能优劣。

## 不确定性与待验证

- 需要一致的 OU、节点/机箱、CPU 型号和核心数清单，以及内存带宽、网络拓扑与工作负载实测。
- 电源架冗余不自动等于整个 AC 路径或 CDU 冗余；必须检查共同故障域、液路维修隔离和恢复控制。

## 来源与版本

- [GitHub 原始文件（固定提交）](https://github.com/microarch-flow/OCP-2026/blob/d6e362b7bb1e65327b9ff005e9b55b5850ccbb34/Rack%20%26%20Power/Applying%20OCP%20ORv3%20and%20ORW%20Design%20Principles%20to%20Rack-Scale%20Arm%20AI%20Infrastructure%20with%20Supermicro.pdf)
- 来源身份 `src-8cd972ecbdfb`；Git blob `46db3875fb408904a3dbc58519414ee03ec2dad2`；原始物理页数 `13`。
- 原始文件保持不变；本文为中文分析，不是讲者认可或独立实验复现。
