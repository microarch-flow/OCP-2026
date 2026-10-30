---
id: "src-368dfc5ed300"
type: "source"
title: "Considerations for Shipping and Storage of 1-Phase Cold Plate Liquid Cooled Racks & Servers"
source_path: "Cooling：Cold Plate/Considerations for Shipping and Storage of 1-Phase Cold Plate Liquid Cooled Racks & Servers.pdf"
source_git_blob_sha: "7457f967fe3e48ce4e5b88d76302b1d4d336596f"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 21
review_status: "analyzed-visual"
evidence_pages: [5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 17, 19]
text_reviewed: true
key_pages_visual_checked: [9, 10, 15]
tags: ["ocp2026", "source", "power-cooling", "cold-plate", "logistics", "reliability"]
concepts: []
---

# 单相冷板运输与仓储：把热膨胀、腐蚀和现场作业一起设计

> 原始题名：Considerations for Shipping and Storage of 1-Phase Cold Plate Liquid Cooled Racks & Servers。阅读范围：完整可提取文字（物理 PDF 共 21 页），关键引用图表另做视觉核对。

## 核心结论

- Meta 与 NVIDIA 将运输方案分为全湿、部分湿、氮气保护干式、压缩空气排液半干式；没有单一最优解，选择依赖物流温控、现场充排液能力和库存周期。 [[Cooling：Cold Plate/Considerations for Shipping and Storage of 1-Phase Cold Plate Liquid Cooled Racks & Servers.pdf#page=5|PDF p.5]]、[[Cooling：Cold Plate/Considerations for Shipping and Storage of 1-Phase Cold Plate Liquid Cooled Racks & Servers.pdf#page=6|PDF p.6]]、[[Cooling：Cold Plate/Considerations for Shipping and Storage of 1-Phase Cold Plate Liquid Cooled Racks & Servers.pdf#page=7|PDF p.7]]、[[Cooling：Cold Plate/Considerations for Shipping and Storage of 1-Phase Cold Plate Liquid Cooled Racks & Servers.pdf#page=8|PDF p.8]]、[[Cooling：Cold Plate/Considerations for Shipping and Storage of 1-Phase Cold Plate Liquid Cooled Racks & Servers.pdf#page=17|PDF p.17]]
- 架构分析：液冷可靠性边界应延伸至运输、备件与 RMA，而不是只验证运行时温度。讲者明确指出硬件抗膨胀能力不同、腐蚀和货架寿命缺少量化共识。 [[Cooling：Cold Plate/Considerations for Shipping and Storage of 1-Phase Cold Plate Liquid Cooled Racks & Servers.pdf#page=19|PDF p.19]]

## 关键证据

| 主张与信息 | 类型、边界与架构含义 | 原始出处 |
| --- | --- | --- |
| 全湿到货可免预充，但需运输/仓储温控；部分湿需要补液 | 经验性方案权衡，不是四组长期失效率实验 | [[Cooling：Cold Plate/Considerations for Shipping and Storage of 1-Phase Cold Plate Liquid Cooled Racks & Servers.pdf#page=5\|PDF p.5]]、[[Cooling：Cold Plate/Considerations for Shipping and Storage of 1-Phase Cold Plate Liquid Cooled Racks & Servers.pdf#page=6\|PDF p.6]]、[[Cooling：Cold Plate/Considerations for Shipping and Storage of 1-Phase Cold Plate Liquid Cooled Racks & Servers.pdf#page=9\|PDF p.9]] |
| 干式需排液、氮气保护、到货放气与预充；半干式省氮气却腐蚀风险高 | p.9 的运输/仓储风险分开列示；干式仓储仍需氮气更新，不能解读为无需维护 | [[Cooling：Cold Plate/Considerations for Shipping and Storage of 1-Phase Cold Plate Liquid Cooled Racks & Servers.pdf#page=7\|PDF p.7]]、[[Cooling：Cold Plate/Considerations for Shipping and Storage of 1-Phase Cold Plate Liquid Cooled Racks & Servers.pdf#page=8\|PDF p.8]]、[[Cooling：Cold Plate/Considerations for Shipping and Storage of 1-Phase Cold Plate Liquid Cooled Racks & Servers.pdf#page=9\|PDF p.9]] |
| 全湿建议使用抑制型冷却液及钝化表面，干式建议预钝化后氮气置换；jumper hose 避免气/液/铜交界 | 讲者建议；柔性连接的机械寿命与可承受膨胀量未测量披露 | [[Cooling：Cold Plate/Considerations for Shipping and Storage of 1-Phase Cold Plate Liquid Cooled Racks & Servers.pdf#page=13\|PDF p.13]]、[[Cooling：Cold Plate/Considerations for Shipping and Storage of 1-Phase Cold Plate Liquid Cooled Racks & Servers.pdf#page=14\|PDF p.14]]、[[Cooling：Cold Plate/Considerations for Shipping and Storage of 1-Phase Cold Plate Liquid Cooled Racks & Servers.pdf#page=15\|PDF p.15]] |
| 运输温变宜用装有热传感器的 dummy rack 实测 | 验证路径；文中引用 IEC 60721-3-2 但本文未独立审查标准 | [[Cooling：Cold Plate/Considerations for Shipping and Storage of 1-Phase Cold Plate Liquid Cooled Racks & Servers.pdf#page=12\|PDF p.12]] |

## 指标与条件

| 指标 | 数值与单位 | 对象、条件、基线及缺失项 | 原始页 |
| --- | --- | --- | --- |
| 填充比例 | 全湿近100%；部分湿90–95%；干式<10%；半干式<50% | p.9 对方案的分类；不是允许残液量的通用标准 | [[Cooling：Cold Plate/Considerations for Shipping and Storage of 1-Phase Cold Plate Liquid Cooled Racks & Servers.pdf#page=9\|PDF p.9]] |
| 冷却液体积变化 | 升温到沸点附近约4%；冻结相关PG25约2–5%、水约9% | 讲者近似值；图是典型PG25密度/温度曲线，不能当作任意配方或组件耐压值 | [[Cooling：Cold Plate/Considerations for Shipping and Storage of 1-Phase Cold Plate Liquid Cooled Racks & Servers.pdf#page=10\|PDF p.10]] |
| 延长湿式存储建议 | 20–25°C | 讲者温控建议；未给可接受最长时长、腐蚀速率或配方依赖 | [[Cooling：Cold Plate/Considerations for Shipping and Storage of 1-Phase Cold Plate Liquid Cooled Racks & Servers.pdf#page=13\|PDF p.13]] |

## 图表与架构

已核对 p.9 四种方案的运输/仓储矩阵、p.10 PG25 双轴曲线、p.15 jumper hose 示意图。矩阵中的高/中/低是相对风险分级，不是故障概率。

## 关联与比较

- [[knowledge/concepts/power-cooling-fluid-assurance]]
- 本条先保留来源级证据；跨源比较应检查工作负载、系统边界、实验条件和时间尺度，不能仅按标题归类后推导性能优劣。

## 不确定性与待验证

- 各液体配方、钝化状态、残气体积、温度历程对应的最长存储期未量化。
- 半干式“无需温控”只描述讲者方案，不是冻结、密封、材料温度范围均已消失。
- 没有 CAPEX、运输费用、现场工时或保修成本，不能据此直接做 TCO 排名。

## 来源与版本

- [GitHub 原始文件（固定提交）](https://github.com/microarch-flow/OCP-2026/blob/d6e362b7bb1e65327b9ff005e9b55b5850ccbb34/Cooling%EF%BC%9ACold%20Plate/Considerations%20for%20Shipping%20and%20Storage%20of%201-Phase%20Cold%20Plate%20Liquid%20Cooled%20Racks%20%26%20Servers.pdf)
- 来源身份 `src-368dfc5ed300`；Git blob `7457f967fe3e48ce4e5b88d76302b1d4d336596f`；原始物理页数 `21`。
- 原始文件保持不变；本文为中文分析，不是讲者认可或独立实验复现。
