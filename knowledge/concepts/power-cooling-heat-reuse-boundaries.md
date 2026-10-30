---
id: power-cooling-heat-reuse-boundaries
type: concept
title: "热回收的四道门槛：温度、时序、受热方与净收益"
tags: ["ocp2026", "power-cooling", "cross-source"]
---

# 热回收的四道门槛：温度、时序、受热方与净收益

## 定义与结论

热回收不是把服务器功耗标成可售热量。**可回收热、可交付热、真正替代的外部热和项目净收益是四个不同量**。以下为已读热回收/冷却资料的综合判断，不是项目可研或通用节能保证。

## 来源与页级证据

| 来源 | 对决策有用的证据 | 保留边界 | 证据 |
| --- | --- | --- | --- |
| 热回收 readiness 方法 | 先过技术、运营、市场与监管门槛，再进行加权评分 | 高综合分不能抵消受热方缺失或温度根本不可用 | [[knowledge/sources/src-a146b844179d\|来源卡]] [[cooling-environments/01_Building a Scalable Waste Heat Ecosystem Datacenter Waste Heat, Offtak.pdf#page=5\|PDF p.5]]、[[cooling-environments/01_Building a Scalable Waste Heat Ecosystem Datacenter Waste Heat, Offtak.pdf#page=7\|PDF p.7]]、[[cooling-environments/01_Building a Scalable Waste Heat Ecosystem Datacenter Waste Heat, Offtak.pdf#page=12\|PDF p.12]]、[[cooling-environments/01_Building a Scalable Waste Heat Ecosystem Datacenter Waste Heat, Offtak.pdf#page=15\|PDF p.15]]、[[cooling-environments/01_Building a Scalable Waste Heat Ecosystem Datacenter Waste Heat, Offtak.pdf#page=16\|PDF p.16]] |
| Heat reuse 创新组合 | MEE、热网/热模块等提出跨用途方案 | 部分为概念或后续路线图；缺少成熟现场经济性，不把目标年份当已投运 | [[knowledge/sources/src-89064d490590\|来源卡]] [[cooling-environments/05_Heat Reuse Sub-Project Overview and Updates + Economics Tool Contribut.pdf#page=8\|PDF p.8]]、[[cooling-environments/05_Heat Reuse Sub-Project Overview and Updates + Economics Tool Contribut.pdf#page=10\|PDF p.10]]、[[cooling-environments/05_Heat Reuse Sub-Project Overview and Updates + Economics Tool Contribut.pdf#page=11\|PDF p.11]]、[[cooling-environments/05_Heat Reuse Sub-Project Overview and Updates + Economics Tool Contribut.pdf#page=21\|PDF p.21]]、[[cooling-environments/05_Heat Reuse Sub-Project Overview and Updates + Economics Tool Contribut.pdf#page=22\|PDF p.22]]、[[cooling-environments/05_Heat Reuse Sub-Project Overview and Updates + Economics Tool Contribut.pdf#page=34\|PDF p.34]] |
| 热泵/ORC 案例 | 演讲提供具体能量流和年发电量估算，便于检查分母与等效时长 | 单列“发电”而排除热泵用电会夸大净收益；年发电量折算的等效供电时长须核算 | [[knowledge/sources/src-573d42e9d351\|来源卡]] [[cooling-environments/06_Waste Heat Recovery Pathways for AI Data Centers Emerging Opportunitie.pdf#page=9\|PDF p.9]]、[[cooling-environments/06_Waste Heat Recovery Pathways for AI Data Centers Emerging Opportunitie.pdf#page=12\|PDF p.12]]、[[cooling-environments/06_Waste Heat Recovery Pathways for AI Data Centers Emerging Opportunitie.pdf#page=15\|PDF p.15]]、[[cooling-environments/06_Waste Heat Recovery Pathways for AI Data Centers Emerging Opportunitie.pdf#page=16\|PDF p.16]]、[[cooling-environments/06_Waste Heat Recovery Pathways for AI Data Centers Emerging Opportunitie.pdf#page=18\|PDF p.18]]、[[cooling-environments/06_Waste Heat Recovery Pathways for AI Data Centers Emerging Opportunitie.pdf#page=21\|PDF p.21]]、[[cooling-environments/06_Waste Heat Recovery Pathways for AI Data Centers Emerging Opportunitie.pdf#page=23\|PDF p.23]] |
| CDU 全年系统模型 | 固定 IT 负荷下比较热交换器/温差与冷却系统年能耗 | 约 1.97–2.30 GWh 是冷却系统边界，不是整站或 IT 年能耗 | [[knowledge/sources/src-bcbce984afab\|来源卡]] [[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=4\|PDF p.4]]、[[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=5\|PDF p.5]]、[[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=8\|PDF p.8]]、[[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=9\|PDF p.9]]、[[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=10\|PDF p.10]]、[[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=11\|PDF p.11]]、[[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=12\|PDF p.12]] |

## 四道门槛（综合框架）

1. **温度与品质。** 服务器出口温度、换热端差、冷却回路条件与受热方最低温度共同决定是否要热泵；较高出水温度可能改善热回收，却可能改变芯片、泵、风扇或冷却能耗。不能只最大化某一侧温度。[[knowledge/sources/src-a146b844179d|来源卡]] [[cooling-environments/01_Building a Scalable Waste Heat Ecosystem Datacenter Waste Heat, Offtak.pdf#page=5|PDF p.5]]、[[cooling-environments/01_Building a Scalable Waste Heat Ecosystem Datacenter Waste Heat, Offtak.pdf#page=7|PDF p.7]] [[knowledge/sources/src-bcbce984afab|来源卡]] [[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=5|PDF p.5]]、[[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=8|PDF p.8]]、[[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=9|PDF p.9]]、[[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=10|PDF p.10]]
2. **时间匹配。** AI 负载与受热需求不一定同步，季节性供暖尤其如此；不能用全年余热总量直接替代逐时匹配。储热可能是缓解手段，这是工程推论，须另建可用能量、损耗和成本模型，而非本材料已证明的储热方案。[[knowledge/sources/src-573d42e9d351|来源卡]] [[cooling-environments/06_Waste Heat Recovery Pathways for AI Data Centers Emerging Opportunitie.pdf#page=7|PDF p.7]]、[[cooling-environments/06_Waste Heat Recovery Pathways for AI Data Centers Emerging Opportunitie.pdf#page=23|PDF p.23]]
3. **有实际受热方。** 距离、网络接口、合同、停供责任和备用热源影响可交付热，不是仅凭有余热就自动产生收入。[[knowledge/sources/src-a146b844179d|来源卡]] [[cooling-environments/01_Building a Scalable Waste Heat Ecosystem Datacenter Waste Heat, Offtak.pdf#page=12|PDF p.12]]、[[cooling-environments/01_Building a Scalable Waste Heat Ecosystem Datacenter Waste Heat, Offtak.pdf#page=15|PDF p.15]]、[[cooling-environments/01_Building a Scalable Waste Heat Ecosystem Datacenter Waste Heat, Offtak.pdf#page=16|PDF p.16]]
4. **净能量与净经济。** 纳入热泵、泵、输配、备用和控制用电，分开记录节约的外部能源与新增的数据中心能耗；再讨论成本与排放，避免同一热量双重记账。[[knowledge/sources/src-573d42e9d351|来源卡]] [[cooling-environments/06_Waste Heat Recovery Pathways for AI Data Centers Emerging Opportunitie.pdf#page=15|PDF p.15]]、[[cooling-environments/06_Waste Heat Recovery Pathways for AI Data Centers Emerging Opportunitie.pdf#page=16|PDF p.16]]、[[cooling-environments/06_Waste Heat Recovery Pathways for AI Data Centers Emerging Opportunitie.pdf#page=18|PDF p.18]] [[knowledge/sources/src-bcbce984afab|来源卡]] [[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=10|PDF p.10]]、[[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=11|PDF p.11]]、[[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=12|PDF p.12]]

## 可复核的数量检查

- **理论年热量不等于年销售量。** 1 MW×8760 h=8.76 GWh 只是在全年满负荷、未扣损失/不可回收份额的算术上限；实际交付还要按利用率和时间匹配计算。此为计算关系，不是来源保证。[[knowledge/sources/src-a146b844179d|来源卡]] [[cooling-environments/01_Building a Scalable Waste Heat Ecosystem Datacenter Waste Heat, Offtak.pdf#page=5|PDF p.5]]、[[cooling-environments/01_Building a Scalable Waste Heat Ecosystem Datacenter Waste Heat, Offtak.pdf#page=7|PDF p.7]]
- **热泵 + ORC 不能只看 ORC 电量。** 演讲示例约 500 kW 热、166.7 kW 热泵电输入、100 kW 发电，按该边界净电仍约 −66.7 kW；这不排除其他用途价值，但不是自给发电闭环。[[knowledge/sources/src-573d42e9d351|来源卡]] [[cooling-environments/06_Waste Heat Recovery Pathways for AI Data Centers Emerging Opportunitie.pdf#page=15|PDF p.15]]、[[cooling-environments/06_Waste Heat Recovery Pathways for AI Data Centers Emerging Opportunitie.pdf#page=16|PDF p.16]]
- **年发电量的等效时长要核算。** 演讲估计一个 30 MW 机房余热一年可发电 8.4 GWh，并称可供该机房约半天；8400 MWh÷30 MW=280 h、约 11.7 天，文字类比不一致。这里是年发电量，不是储热容量，也不是可连续供电的备电承诺。[[knowledge/sources/src-573d42e9d351|来源卡]] [[cooling-environments/06_Waste Heat Recovery Pathways for AI Data Centers Emerging Opportunitie.pdf#page=16|PDF p.16]]
- **节能比例必须写分母。** CDU 案例约 17% 是冷却系统年能耗最大/最小方案间跨度的特定口径，不能变成整站节电 17%。热交换器相对成本尺度也不是已报价 CAPEX。[[knowledge/sources/src-bcbce984afab|来源卡]] [[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=10|PDF p.10]]、[[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=11|PDF p.11]]、[[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=12|PDF p.12]]

## 成本与生命周期最小数据包

在比较路线前至少取得以下同口径输入；这些是分析所需字段，不是已知报价：

| 类别 | 必需边界 |
| --- | --- |
| 投资 | 币种、价格年份、热泵/换热器/管网/土建/控制/备用设备、接入与土地费用、所承担方 |
| 运行 | IT/受热方逐时负荷、温度、热泵部分负荷效率、泵/输配损耗、电/热/水费与维护 |
| 利用与寿命 | 合同量和季节性、可用率、回收系统寿命、设备更换、受热方退出或迁移风险 |
| 排放 | 被替代供热的实际能源、时段电力排放、隐含碳和寿命、避免双重申报的分配规则 |
| 服务责任 | 热网中断/服务器检修的备用措施、补偿责任、不得损害 IT 热安全与维护能力 |

当前来源不足以给出跨地区通用回本年数、统一货币 TCO 或“热回收必然更低碳”。后续应以一个具体站点和真实受热负荷完成逐时能量、费用和可靠性联合模型。

关联：[[knowledge/concepts/power-cooling-capacity-evidence-ladder|容量证据分级]] · [[knowledge/comparisons/power-cooling-single-vs-two-phase|单相与两相比对]]

