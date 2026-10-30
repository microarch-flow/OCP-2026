---
id: "src-e84fa2f73a45"
type: "source"
title: "Nidec CDU：容量、可维护性与可靠性证据分层"
source_path: "expo-hall-sessions/Liquid-Cooling-Designed-for-Maximum-Uptime-and-Reliability-presented-by-Nidec.pdf"
source_git_blob_sha: "265046877cfee04be2fa4a058fac1a6fcf17ec94"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 18
review_status: "analyzed-visual"
evidence_pages: [7, 8, 9, 11, 12, 13, 14, 17]
text_reviewed: true
key_pages_visual_checked: [7, 11, 12, 13]
tags: ["ocp2026", "expo-hall"]
concepts: ["[[knowledge/concepts/expo-evidence-to-deployment]]"]
---

# Nidec CDU：容量、可维护性与可靠性证据分层

## 核心结论
本讲把可靠性落实为冗余泵、前维护、工厂/现场验收与售后体系；但大出货量、最大散热容量和24/7响应都不能单独证明生产系统可用性。[[expo-hall-sessions/Liquid-Cooling-Designed-for-Maximum-Uptime-and-Reliability-presented-by-Nidec.pdf#page=7|PDF p.7]] [[expo-hall-sessions/Liquid-Cooling-Designed-for-Maximum-Uptime-and-Reliability-presented-by-Nidec.pdf#page=8|PDF p.8]] [[expo-hall-sessions/Liquid-Cooling-Designed-for-Maximum-Uptime-and-Reliability-presented-by-Nidec.pdf#page=9|PDF p.9]] [[expo-hall-sessions/Liquid-Cooling-Designed-for-Maximum-Uptime-and-Reliability-presented-by-Nidec.pdf#page=13|PDF p.13]]

## 关键证据、指标与条件
- 全球累计出货超过13,000台CDU，是厂商规模陈述；没有设备小时、故障数量、维修时长或代际分布，不能换算MTBF/FIT。[[expo-hall-sessions/Liquid-Cooling-Designed-for-Maximum-Uptime-and-Reliability-presented-by-Nidec.pdf#page=7|PDF p.7]]
- 4U/19英寸in-rack **目标规格**：Gen2.5为250kW、深852mm、1+1泵；Gen3.0为300kW、深946mm、冗余热插拔泵。均列Redfish与expansion tank，未给容量对应水温/流量/压差。[[expo-hall-sessions/Liquid-Cooling-Designed-for-Maximum-Uptime-and-Reliability-presented-by-Nidec.pdf#page=11|PDF p.11]]
- in-row产品图并列2MW、3.2MW、6.4MW及15MW skid；这些类别不等于全部已经量产或同等条件测得。[[expo-hall-sessions/Liquid-Cooling-Designed-for-Maximum-Uptime-and-Reliability-presented-by-Nidec.pdf#page=12|PDF p.12]]
- NIR3.0标3.2MW、3°C approach、THDi≤5%、主要元件/传感器前维护，可选pH/电导率/浊度；800V输入明确仍在评估。[[expo-hall-sessions/Liquid-Cooling-Designed-for-Maximum-Uptime-and-Reliability-presented-by-Nidec.pdf#page=13|PDF p.13]] 下一步415VAC/800V共用机柜需电气修改，不能当作现有设备无改造兼容。[[expo-hall-sessions/Liquid-Cooling-Designed-for-Maximum-Uptime-and-Reliability-presented-by-Nidec.pdf#page=14|PDF p.14]]

## 图表与架构
已核p7/11/12/13。p9把standalone/FAT、安装、功能和集成系统测试分开，适合转成验收门槛；泵N-1能力、设施侧失供和现场电力切换还需整机测试，而不是仅出厂测试。[[expo-hall-sessions/Liquid-Cooling-Designed-for-Maximum-Uptime-and-Reliability-presented-by-Nidec.pdf#page=9|PDF p.9]]

## 关联与比较
[[knowledge/concepts/expo-evidence-to-deployment]]：与CoolIT单冷板15kW TTV证据层级不同；CDU额定MW、芯片热阻和全系统稳定性不能互相替代。

## 不确定性与待验证
需额定容量对应冷却液/进出水温/流量、泵失效后的降额、备用泵切换时间、漏液检测与隔离、维修不中断边界。24/7响应未定义到场或恢复SLA；制造100%流体/气体漏检不等于现场零失效。[[expo-hall-sessions/Liquid-Cooling-Designed-for-Maximum-Uptime-and-Reliability-presented-by-Nidec.pdf#page=17|PDF p.17]]


跨源比较：[[knowledge/comparisons/expo-thermal-performance-contract]]。
