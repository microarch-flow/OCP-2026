---
id: "src-ed31e0df1756"
type: "source"
title: "Path to the Megawatt Rack- A Grid-Aware, Symmetric High-Power UPS for AI Data Centers"
source_path: "ai-open-data-center/Path to the Megawatt Rack- A Grid-Aware, Symmetric High-Power UPS for AI Data Centers.pdf"
source_git_blob_sha: "75a1b0370259ebacbfbb3b7c91fe026d09ecdbba"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 19
review_status: "analyzed-visual"
evidence_pages: [4, 8, 9, 10, 12, 13, 16, 17]
tags: ["ai-infra", "ai-open-data-center"]
text_reviewed: "all-extractable-pages"
key_pages_visual_checked: [8, 9, 10, 12, 13, 16, 17, 18]
concepts: ["[[knowledge/concepts/ai-infra-locality-and-control-timescales]]"]
---

# Path to the Megawatt Rack- A Grid-Aware, Symmetric High-Power UPS for AI Data Centers

## 核心结论
Echion/Proper Voltage提出UPS电池从偶发单向backup变为频繁双向buffer：充电功率、浅循环寿命与reserve SOC可能比kWh更先决定系统大小。证据包含cell实验、厂商模拟与尚在建的柜体，三者不能混同。[[ai-open-data-center/Path to the Megawatt Rack- A Grid-Aware, Symmetric High-Power UPS for AI Data Centers.pdf#page=4|PDF p.4]] [[ai-open-data-center/Path to the Megawatt Rack- A Grid-Aware, Symmetric High-Power UPS for AI Data Centers.pdf#page=8|PDF p.8]] [[ai-open-data-center/Path to the Megawatt Rack- A Grid-Aware, Symmetric High-Power UPS for AI Data Centers.pdf#page=10|PDF p.10]] [[ai-open-data-center/Path to the Megawatt Rack- A Grid-Aware, Symmetric High-Power UPS for AI Data Centers.pdf#page=13|PDF p.13]]

## 关键证据
模型280MW compute/160MW communication、grid270MW，40s放电与4s充电组成44s周期；短低谷要求大charge power。p.10按110MW recharge/charge-rate ceiling得0.6C→183MWh、1C→110MWh、6.1C→18MWh；后者约对应270MW四分钟backup。[[ai-open-data-center/Path to the Megawatt Rack- A Grid-Aware, Symmetric High-Power UPS for AI Data Centers.pdf#page=9|PDF p.9]] [[ai-open-data-center/Path to the Megawatt Rack- A Grid-Aware, Symmetric High-Power UPS for AI Data Centers.pdf#page=10|PDF p.10]] [[ai-open-data-center/Path to the Megawatt Rack- A Grid-Aware, Symmetric High-Power UPS for AI Data Centers.pdf#page=16|PDF p.16]]

## 指标与条件
p.8 XNO 5.5Ah cell在25°C实验/寿命预期，称>30C/30C、10–90%SOC下5C/5C约50000cycles；不等于柜体长时同环境或所有循环深度。模型每天1964次buffering多为浅循环，不能与cell full-cycle寿命直接相除。[[ai-open-data-center/Path to the Megawatt Rack- A Grid-Aware, Symmetric High-Power UPS for AI Data Centers.pdf#page=8|PDF p.8]] [[ai-open-data-center/Path to the Megawatt Rack- A Grid-Aware, Symmetric High-Power UPS for AI Data Centers.pdf#page=10|PDF p.10]]
$317/$25/$10 per MWh delivered为十年**cells-only、未折现**比较，服务寿命分别来自不同spec/model/推断，未含PCS、冷却、安装与维护，不是统一全系统TCO或采购报价。[[ai-open-data-center/Path to the Megawatt Rack- A Grid-Aware, Symmetric High-Power UPS for AI Data Centers.pdf#page=10|PDF p.10]] [[ai-open-data-center/Path to the Megawatt Rack- A Grid-Aware, Symmetric High-Power UPS for AI Data Centers.pdf#page=16|PDF p.16]]

## 图表与架构
已看cell、profile、成本、电压与柜体页。p.12 regulation error为illustrative非Proper Voltage datasheet；p.17说明电池SOC/负载压降无法直接符合该800V窄rail，需DC/DC。1.6MWpeak/1MWcontinuous、80kWh48U柜体明确prototype underway、preliminary，UL等是safety path不是已获证声明。[[ai-open-data-center/Path to the Megawatt Rack- A Grid-Aware, Symmetric High-Power UPS for AI Data Centers.pdf#page=12|PDF p.12]] [[ai-open-data-center/Path to the Megawatt Rack- A Grid-Aware, Symmetric High-Power UPS for AI Data Centers.pdf#page=13|PDF p.13]] [[ai-open-data-center/Path to the Megawatt Rack- A Grid-Aware, Symmetric High-Power UPS for AI Data Centers.pdf#page=17|PDF p.17]]

## 关联与比较
[[knowledge/concepts/ai-infra-locality-and-control-timescales]]；[[knowledge/concepts/ai-infra-deployment-readiness]]。

## 不确定性与待验证
10MW×40s与110MW×4s分别约111/122kWh，页写各120kWh说明数值有舍入/波形边界，完整能量平衡和损耗尚需模型。需实柜高频双向测试、thermal runaway评估、aging/SOC reserve与故障冗余，不由单cell nail试验宣布系统安全。[[ai-open-data-center/Path to the Megawatt Rack- A Grid-Aware, Symmetric High-Power UPS for AI Data Centers.pdf#page=8|PDF p.8]] [[ai-open-data-center/Path to the Megawatt Rack- A Grid-Aware, Symmetric High-Power UPS for AI Data Centers.pdf#page=9|PDF p.9]]
