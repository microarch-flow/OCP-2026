---
id: "src-5b3cc2f434f1"
type: "source"
title: "01_800 VDC AI Factories From Architecture Alignment to Industry Deploymen"
source_path: "ai-open-data-center/01_800 VDC AI Factories From Architecture Alignment to Industry Deploymen.pdf"
source_git_blob_sha: "676690e0b0b225d9ca16f911c7ab524003f6a359"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 19
review_status: "analyzed-visual"
evidence_pages: [3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18]
tags: ["ai-infra", "ai-open-data-center"]
text_reviewed: "all-extractable-pages"
key_pages_visual_checked: [2, 3, 4, 9, 10, 12, 13, 14, 15, 16, 17]
concepts: ["[[knowledge/concepts/ai-infra-deployment-readiness]]"]
---

# 01_800 VDC AI Factories From Architecture Alignment to Industry Deploymen

## 核心结论
NVIDIA将800VDC部署分成rack power rack、cluster power center、data-hall power block三条路径；关键区别是改造范围、灰/白空间、冗余与储能位置，而不只是提高电压。[[ai-open-data-center/01_800 VDC AI Factories From Architecture Alignment to Industry Deploymen.pdf#page=4|PDF p.4]] [[ai-open-data-center/01_800 VDC AI Factories From Architecture Alignment to Industry Deploymen.pdf#page=7|PDF p.7]] [[ai-open-data-center/01_800 VDC AI Factories From Architecture Alignment to Industry Deploymen.pdf#page=8|PDF p.8]] [[ai-open-data-center/01_800 VDC AI Factories From Architecture Alignment to Industry Deploymen.pdf#page=11|PDF p.11]]

## 关键证据
A复用facility AC、在IT行增加转换rack；B维持data hall布局，在power center转换；C偏greenfield、在power block/SST整合MV→DC与ESS，减少中间级。ESS的FRT、backup、smoothing、load averaging是不同功能，不能只写“有电池即可靠”。[[ai-open-data-center/01_800 VDC AI Factories From Architecture Alignment to Industry Deploymen.pdf#page=4|PDF p.4]] [[ai-open-data-center/01_800 VDC AI Factories From Architecture Alignment to Industry Deploymen.pdf#page=13|PDF p.13]] [[ai-open-data-center/01_800 VDC AI Factories From Architecture Alignment to Industry Deploymen.pdf#page=15|PDF p.15]]

## 指标与条件
A方案660kW、415–480VAC输入12×100A whips、800VDC输出8×125A cables，compute端1RU/90kW shelves，支持N+N；这些是方案额定参数，不是现场满载效率。p.9连接器示例却写95kW continuous shelf与380kW rack，和p.6/10的90kW不一致，应按具体版本确认，不拼成一份采购BOM。[[ai-open-data-center/01_800 VDC AI Factories From Architecture Alignment to Industry Deploymen.pdf#page=6|PDF p.6]] [[ai-open-data-center/01_800 VDC AI Factories From Architecture Alignment to Industry Deploymen.pdf#page=9|PDF p.9]] [[ai-open-data-center/01_800 VDC AI Factories From Architecture Alignment to Industry Deploymen.pdf#page=10|PDF p.10]]
C示例7blocks、6+1，SST输入5MVA不是5MW。p.17时间线A Q3 2026、B Q2 2027、C Q1 2028，属于作者readiness路线图。[[ai-open-data-center/01_800 VDC AI Factories From Architecture Alignment to Industry Deploymen.pdf#page=11|PDF p.11]] [[ai-open-data-center/01_800 VDC AI Factories From Architecture Alignment to Industry Deploymen.pdf#page=12|PDF p.12]] [[ai-open-data-center/01_800 VDC AI Factories From Architecture Alignment to Industry Deploymen.pdf#page=17|PDF p.17]]

## 图表与架构
已看架构、连接器、ESS与readiness关键页。p.3近似时间轴含未来rack power趋势，不当当前实装规格；p.10安全接口包括interlock、touch-safe、DC breaker、IMD/RCM。提取文字含NVIDIA CONFIDENTIAL，但实际渲染p.10无可见该标记，不据隐藏模板文字推断私密。[[ai-open-data-center/01_800 VDC AI Factories From Architecture Alignment to Industry Deploymen.pdf#page=3|PDF p.3]] [[ai-open-data-center/01_800 VDC AI Factories From Architecture Alignment to Industry Deploymen.pdf#page=10|PDF p.10]]

## 关联与比较
[[knowledge/concepts/ai-infra-deployment-readiness]]；[[knowledge/concepts/ai-infra-locality-and-control-timescales]]。

## 不确定性与待验证
p.18明确工程仿真→原型系统→认证→生产准备→制造部署五关。没有实测效率、保护协调曲线、热插拔/故障电流、fleet可用性或成本；deployment-ready标签不能替代这些验收证据。[[ai-open-data-center/01_800 VDC AI Factories From Architecture Alignment to Industry Deploymen.pdf#page=18|PDF p.18]]
