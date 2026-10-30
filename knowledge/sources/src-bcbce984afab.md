---
id: "src-bcbce984afab"
type: "source"
title: "07_What Shapes CDU Performance A Comparative Study of Design Choices for "
source_path: "cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf"
source_git_blob_sha: "af76f533d9bca17503ab72fef8502892e078a5aa"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 15
review_status: "analyzed-visual"
evidence_pages: [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
text_reviewed: true
key_pages_visual_checked: [4, 5, 8, 9, 10, 11, 12]
tags: ["ocp2026", "source", "power-cooling", "cdu", "system-model", "energy"]
concepts: []
---

# 同为2.3MW的CDU：换热器选择如何改变全年冷却系统能耗

> 原始题名：07_What Shapes CDU Performance A Comparative Study of Design Choices for 。阅读范围：完整可提取文字（物理 PDF 共 15 页），关键引用图表另做视觉核对。

## 核心结论

- 固定IT侧热负荷/温度/流量后，HX选择主要改变一次侧需要的流量、回水温度、管径和泵工作点。应把CDU嵌入干冷器/冷水机/泵模型，并按气候全年积分，而非只比额定MW。 [[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=2|PDF p.2]]、[[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=6|PDF p.6]]、[[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=7|PDF p.7]]、[[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=8|PDF p.8]]、[[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=9|PDF p.9]]、[[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=10|PDF p.10]]、[[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=13|PDF p.13]]
- 研究是以Deschutes 5规格校准的模型，不是十台CDU在现场并行跑一年的结果；设备外部效率图多项为估算。 [[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=5|PDF p.5]]、[[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=7|PDF p.7]]
- 最低采购相对成本方案在此Dallas情景下年度能耗最高；更小approach、污垢和一次侧换成PG35的响应不同，某配置甚至无法满足温度。 [[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=4|PDF p.4]]、[[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=10|PDF p.10]]、[[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=11|PDF p.11]]

## 关键证据

| 主张与信息 | 类型、边界与架构含义 | 原始出处 |
| --- | --- | --- |
| 统一比较使用水FWS/PG25 TCS和固定二次侧 | 来源对ASHRAE测试条件的转述；该条件用于测试单元，不自动代表现场。规范本身未另行核验。 | [[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=6\|PDF p.6]] |
| 较热一次侧回水延迟压缩机开启 | 全年模型解释；收益集中于自然冷却/机械制冷切换区，低/高环境温度端差异较小。 | [[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=9\|PDF p.9]] |
| 工具界面允许切换设备/流体/环境等 | 截图非本卡执行记录，未运行模型或验证软件。 | [[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=12\|PDF p.12]] |

## 指标与条件

| 指标 | 数值与单位 | 对象、条件、基线及缺失项 | 原始页 |
| --- | --- | --- | --- |
| 固定比较边界 | IT2.3MW；二次侧压降50psi；FWS供26°C；TCS供/回30/39.6°C | 外部设备/模型固定；部分负荷条件源列75/50/25%，年度主例仍为固定负载。 | [[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=6\|PDF p.6]]、[[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=7\|PDF p.7]] |
| 相对采购成本 | 57%至192%，基准100% | 换热器类型/数量/程数/approach组合的相对价格图；非整站CAPEX，没有币种/报价日期/安装成本。 | [[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=4\|PDF p.4]] |
| 全年冷却系统能耗 | 图读约1.97–2.30GWh/年；Deschutes约2.00GWh/年 | Dallas温度分箱8760h、固定2.3MW IT；约17%为最高/最低跨度口径，不是IT或全站节能17%。 | [[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=10\|PDF p.10]] |
| 25°C环境一次侧流量 | 图读约660–940GPM | 同等热负荷/IT侧条件，管径还受速度准则；回水图约35.4–39.4°C，结论页34–39°C是较粗概述。 | [[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=8\|PDF p.8]]、[[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=13\|PDF p.13]] |
| 污垢敏感性 | 一次侧0.9×10⁻⁴m²K/W：三例能耗+3.0%、+7.0%、+0.4% | 分别Deschutes、brazed2HX1pass4K、gasketed1HX1K；PG35下brazed例无法达目标温度。 | [[cooling-environments/07_What Shapes CDU Performance A Comparative Study of Design Choices for .pdf#page=11\|PDF p.11]] |

## 图表与架构

视觉核对p.4、5、8–12。p.4是相对价格而非货币；p.5下方标注每个HX的结果。p.10纵轴从约1.95GWh开始，不能把图高误读成倍数差。p.7称十一种而p.13/图中十种，保留枚举不一致，不推定遗漏配置。

## 关联与比较

- [[knowledge/concepts/power-cooling-heat-reuse-boundaries]]

- 本条先保留来源级证据；跨源比较应检查工作负载、系统边界、实验条件和时间尺度，不能仅按标题归类后推导性能优劣。

## 不确定性与待验证

- 需要模型文件、设备性能图、控制策略和实际负载/气象后才可复现。
- 没有电价和生命周期/利用率折现模型，无法计算美元OPEX、回收期或TCO赢家。
- 应补泵/风机故障、污垢进程、冗余降额和现场控制动态，而不只看稳态全年积分。

## 来源与版本

- [GitHub 原始文件（固定提交）](https://github.com/microarch-flow/OCP-2026/blob/d6e362b7bb1e65327b9ff005e9b55b5850ccbb34/cooling-environments/07_What%20Shapes%20CDU%20Performance%20A%20Comparative%20Study%20of%20Design%20Choices%20for%20.pdf)
- 来源身份 `src-bcbce984afab`；Git blob `af76f533d9bca17503ab72fef8502892e078a5aa`；原始物理页数 `15`。
- 原始文件保持不变；本文为中文分析，不是讲者认可或独立实验复现。
