---
id: "src-436ffc3e1dc3"
type: "source"
title: "Laser Sources to Simplify Slow-and-Wide Optical Interconnects"
source_path: "fti-workshop-short-reach-optical-interconnects/Laser-Sources-to-Simplify-Slow-and-Wide-Optical-Interconnects.pdf"
source_git_blob_sha: "f18f5360a9d57dc15fe7384b932a0581e0915862"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 15
review_status: "analyzed-visual"
evidence_pages: [3, 4, 5, 7, 10, 11, 13, 14]
text_reviewed: true
key_pages_visual_checked: [3, 4, 11, 13]
tags: ["ocp2026", "networking"]
concepts: ["[[knowledge/concepts/network-optical-integration]]"]
---

# Laser Sources to Simplify Slow-and-Wide Optical Interconnects

## 核心结论
Quintessent用O-band GaAs quantum-dot gain与SOI异质集成提供single-λ DFB与multi-λ comb；单腔多波长减少控制源，却仍需评估SOA、耦合损耗与共享故障域。[[fti-workshop-short-reach-optical-interconnects/Laser-Sources-to-Simplify-Slow-and-Wide-Optical-Interconnects.pdf#page=5|PDF p.5]][[fti-workshop-short-reach-optical-interconnects/Laser-Sources-to-Simplify-Slow-and-Wide-Optical-Interconnects.pdf#page=7|PDF p.7]][[fti-workshop-short-reach-optical-interconnects/Laser-Sources-to-Simplify-Slow-and-Wide-Optical-Interconnects.pdf#page=11|PDF p.11]]

## 关键证据
GaAs epi面朝下bond到预pattern SOI、去substrate、III-V加工与wafer test；硅定义cavity避免facet/再生长等工艺，known-good die是路线目标。[[fti-workshop-short-reach-optical-interconnects/Laser-Sources-to-Simplify-Slow-and-Wide-Optical-Interconnects.pdf#page=5|PDF p.5]] 8λ comb单current source、温漂共同移动，spacing由cavity定，不能理解为完全不需系统wavelength管理。[[fti-workshop-short-reach-optical-interconnects/Laser-Sources-to-Simplify-Slow-and-Wide-Optical-Interconnects.pdf#page=7|PDF p.7]]

## 指标与条件
- 3epi lots946/1019/988颗laser、WPE主群25–30%，仍处EVT foundry flow；不是全样本最低效率。[[fti-workshop-short-reach-optical-interconnects/Laser-Sources-to-Simplify-Slow-and-Wide-Optical-Interconnects.pdf#page=3|PDF p.3]]
- 初步Fabry-Perot QD aging80°C/125mA、目标30mW，>22000h；另150+器件更强加速campaign启动，不能把新campaign样本数追溯到旧数据。[[fti-workshop-short-reach-optical-interconnects/Laser-Sources-to-Simplify-Slow-and-Wide-Optical-Interconnects.pdf#page=4|PDF p.4]]
- comb alone >80mW in silicon waveguide、peak WPE>20%；comb+SOA30°C总200mW、8λ、2dB uniformity是另一配置。[[fti-workshop-short-reach-optical-interconnects/Laser-Sources-to-Simplify-Slow-and-Wide-Optical-Interconnects.pdf#page=10|PDF p.10]][[fti-workshop-short-reach-optical-interconnects/Laser-Sources-to-Simplify-Slow-and-Wide-Optical-Interconnects.pdf#page=11|PDF p.11]]
- 5不同λ DFB+SOA在SOA透明无gain状态，反馈至-15dB时RIN近-150dBc/Hz；isolator-free为“likely”判断，不是所有反射环境合格。[[fti-workshop-short-reach-optical-interconnects/Laser-Sources-to-Simplify-Slow-and-Wide-Optical-Interconnects.pdf#page=13|PDF p.13]]

## 图表与架构
已核WPE分布、aging曲线、30°C光谱与feedback散点。p.11明确out-of-band SMSR还需优化；更高SOA输出不能只算laser本身WPE。

## 关联与比较
[[knowledge/concepts/network-optical-integration]]；[[knowledge/sources/src-85e837cea055]]的ELS 1:1与mux/PIC建议提醒单源多λ的system tradeoff。

## 不确定性与待验证
ELSFP、OCI4λ×400GHz、更高power/λ及进一步可靠性仍next steps。[[fti-workshop-short-reach-optical-interconnects/Laser-Sources-to-Simplify-Slow-and-Wide-Optical-Interconnects.pdf#page=14|PDF p.14]] 缺complete ELS power、RIN全频谱/temperature、FIT置信界和field data。
