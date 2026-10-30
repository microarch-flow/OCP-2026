---
id: "src-36f6d2f1df12"
type: "source"
title: "Enabling 1MW+ IT rack power with an open rack busbar interface"
source_path: "Rack & Power/Enabling 1MW+ IT rack power with an open rack busbar interface.pdf"
source_git_blob_sha: "8f88021d1b7d039407292e6d3ce3cf7a67472a88"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 13
review_status: "analyzed-visual"
evidence_pages: [2, 5, 6, 7, 8, 9, 10, 11, 12]
text_reviewed: true
key_pages_visual_checked: [5, 6, 8, 9, 10]
tags: ["ocp2026", "source", "power-cooling", "busbar", "800v", "thermal-test"]
concepts: ["[[knowledge/concepts/power-cooling-capacity-evidence-ladder|容量证据阶梯]]"]
---

# 800 V IT 母排接口：500 kW 温升实测与 1 MW 仿真需分开

> 原始题名：Enabling 1MW+ IT rack power with an open rack busbar interface。阅读范围：完整可提取文字（物理 PDF 共 13 页），关键引用图表另做视觉核对。

## 核心结论

- TE 接口方案维持 ORv3 35 mm 宽度，用增加深度扩展载流能力，并引入 PE、功率及 sense 的插接次序；演讲反复注明这些产品还不是任何 OCP 规格的已许可贡献。 [[Rack & Power/Enabling 1MW+ IT rack power with an open rack busbar interface.pdf#page=2|PDF p.2]]、[[Rack & Power/Enabling 1MW+ IT rack power with an open rack busbar interface.pdf#page=5|PDF p.5]]、[[Rack & Power/Enabling 1MW+ IT rack power with an open rack busbar interface.pdf#page=6|PDF p.6]]、[[Rack & Power/Enabling 1MW+ IT rack power with an open rack busbar interface.pdf#page=8|PDF p.8]]
- 500 kW 对应 625 A 的实物温升测试与 750 kW/1 MW 的仿真应分级记录。实测 25°C 环境、120 分钟，仿真 55°C、无气流；不能混称“1 MW 全部测试通过”。 [[Rack & Power/Enabling 1MW+ IT rack power with an open rack busbar interface.pdf#page=9|PDF p.9]]、[[Rack & Power/Enabling 1MW+ IT rack power with an open rack busbar interface.pdf#page=10|PDF p.10]]
- PE 先接后断、sense 后接先断及可选预充有助于定义互锁序列，但未展示整个带载分断、弧闪及故障协调认证。 [[Rack & Power/Enabling 1MW+ IT rack power with an open rack busbar interface.pdf#page=7|PDF p.7]]、[[Rack & Power/Enabling 1MW+ IT rack power with an open rack busbar interface.pdf#page=8|PDF p.8]]
- 更高电流密度的液冷母排仍属后续研究方向，尚无本文中的流量、压降、漏液寿命或冷却失效数据。 [[Rack & Power/Enabling 1MW+ IT rack power with an open rack busbar interface.pdf#page=11|PDF p.11]]、[[Rack & Power/Enabling 1MW+ IT rack power with an open rack busbar interface.pdf#page=12|PDF p.12]]

## 关键证据

| 主张与信息 | 类型、边界与架构含义 | 原始出处 |
| --- | --- | --- |
| 35 mm 标准宽度、可扩展深度 | 机械兼容思路，不意味着既有 48 V 母排/插座可直接用于 800 V | [[Rack & Power/Enabling 1MW+ IT rack power with an open rack busbar interface.pdf#page=5\|PDF p.5]]、[[Rack & Power/Enabling 1MW+ IT rack power with an open rack busbar interface.pdf#page=6\|PDF p.6]] |
| 500 kW 热测试 | 电流加载样件测试，图中上端 clip 短接；不是完整 500 kW IT 负载连续运行示范 | [[Rack & Power/Enabling 1MW+ IT rack power with an open rack busbar interface.pdf#page=10\|PDF p.10]] |
| 仿真与实测接近约 6% | 厂商表述；两页环境和工况不同，需取得同条件模型验证数据再使用误差值 | [[Rack & Power/Enabling 1MW+ IT rack power with an open rack busbar interface.pdf#page=9\|PDF p.9]]、[[Rack & Power/Enabling 1MW+ IT rack power with an open rack busbar interface.pdf#page=10\|PDF p.10]] |

## 指标与条件

| 指标 | 数值与单位 | 对象、条件、基线及缺失项 | 原始页 |
| --- | --- | --- | --- |
| 母排尺寸 | 2134×35×80/130/200 mm | 分别对应 500/750/1000 kW 与约 625/937/1250 A，800 V 名义计算 | [[Rack & Power/Enabling 1MW+ IT rack power with an open rack busbar interface.pdf#page=6\|PDF p.6]] |
| 模拟最高温升 | 29.27 / 28.22 / 29.76°C | 分别 625/937/1250 A；环境 55°C、无气流、图示机架分支布局 | [[Rack & Power/Enabling 1MW+ IT rack power with an open rack busbar interface.pdf#page=9\|PDF p.9]] |
| 实测最高温升 | 约 27°C | 625 A、环境 25°C、120 min；测点 M1–M10，样本数未披露 | [[Rack & Power/Enabling 1MW+ IT rack power with an open rack busbar interface.pdf#page=10\|PDF p.10]] |

## 图表与架构

p.8 插接顺序图把 PE、预充、0 V、800 V、presence/sense 分层；p.9 三种深度不是同一母排提升电流后的曲线，而是不同几何的三组仿真。

## 关联与比较

- [[knowledge/concepts/power-cooling-capacity-evidence-ladder|容量证据阶梯]]

## 不确定性与待验证

- 需验证接触电阻老化、插拔周期、公差、污染、短路电动力和异常冷却条件。
- Touch Safe 设计及手指探针图不是独立认证报告；正式安全与施工判断需适用规范核验。

## 来源与版本

- [GitHub 原始文件（固定提交）](https://github.com/microarch-flow/OCP-2026/blob/d6e362b7bb1e65327b9ff005e9b55b5850ccbb34/Rack%20%26%20Power/Enabling%201MW%2B%20IT%20rack%20power%20with%20an%20open%20rack%20busbar%20interface.pdf)
- 来源身份 `src-36f6d2f1df12`；Git blob `8f88021d1b7d039407292e6d3ce3cf7a67472a88`；原始物理页数 `13`。
- 原始文件保持不变；本文为中文分析，不是讲者认可或独立实验复现。
