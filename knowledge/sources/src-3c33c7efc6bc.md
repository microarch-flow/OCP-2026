---
id: "src-3c33c7efc6bc"
type: "source"
title: "Architecting Near-Packaged Optics for AI Datacenters: Key Technology Choices and Trade-offs"
source_path: "fti-workshop-short-reach-optical-interconnects/Architecting-Near-Packaged-Optics-for-AI-Datacenters-Key-Technology-Choices-and-Trade-offs.pdf"
source_git_blob_sha: "02f28b91d306ac3b987ddfa9b281467f453e972a"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 9
review_status: "analyzed-visual"
evidence_pages: [2, 3, 4, 5, 6, 7, 8]
text_reviewed: true
key_pages_visual_checked: [2, 5]
tags: ["ocp2026", "networking"]
concepts: ["[[knowledge/concepts/network-optical-integration]]"]
---

# Architecting Near-Packaged Optics for AI Datacenters: Key Technology Choices and Trade-offs

## 核心结论
Nokia把NPO的关键选择拆为modulator、laser位置与package/thermal/repair三维。NPO可接近CPO能耗同时替换engine，但“可替换”并不等于前面板hot-swap；内部laser也仍需避开ASIC热区。[[fti-workshop-short-reach-optical-interconnects/Architecting-Near-Packaged-Optics-for-AI-Datacenters-Key-Technology-Choices-and-Trade-offs.pdf#page=2|PDF p.2]][[fti-workshop-short-reach-optical-interconnects/Architecting-Near-Packaged-Optics-for-AI-Datacenters-Key-Technology-Choices-and-Trade-offs.pdf#page=3|PDF p.3]][[fti-workshop-short-reach-optical-interconnects/Architecting-Near-Packaged-Optics-for-AI-Datacenters-Key-Technology-Choices-and-Trade-offs.pdf#page=6|PDF p.6]][[fti-workshop-short-reach-optical-interconnects/Architecting-Near-Packaged-Optics-for-AI-Datacenters-Key-Technology-Choices-and-Trade-offs.pdf#page=8|PDF p.8]]

## 关键证据
InP可monolithic laser，SiPh/TFLN需另一种laser集成；高带宽/低损耗/低驱动/热稳定/量产规模没有一个modulator全面领先。socket与host attach、known-good die、wafer test、被动对准共同决定可制造性。[[fti-workshop-short-reach-optical-interconnects/Architecting-Near-Packaged-Optics-for-AI-Datacenters-Key-Technology-Choices-and-Trade-offs.pdf#page=4|PDF p.4]][[fti-workshop-short-reach-optical-interconnects/Architecting-Near-Packaged-Optics-for-AI-Datacenters-Key-Technology-Choices-and-Trade-offs.pdf#page=6|PDF p.6]]

## 指标与条件
已核p.2概括link energy：retimed约15pJ/bit、LRO约10、LPO/NPO/CPO约6、D2D集成<4且“years from volume”。没有统一lane/reach/laser边界或测试平台，不能作为精确A/B。
已核p.5 laser-to-mod损耗示例：monolithic0.25dB、bonded0.5–1dB、in-package1.5dB、ELSFP2dB；越外置热/维修越容易，但纤维/connector及光功率增加。是架构预算，不是全供应商规格。[[fti-workshop-short-reach-optical-interconnects/Architecting-Near-Packaged-Optics-for-AI-Datacenters-Key-Technology-Choices-and-Trade-offs.pdf#page=5|PDF p.5]]

## 图表与架构
p.5同时说明ELS可供4–16lanes，独立激光替换换来共享故障域；内部laser简化PM fiber与前面板，却需替换整个engine。Nokia6-inch InP产能扩展是厂商计划，不是本文件的yield/可靠性数据。[[fti-workshop-short-reach-optical-interconnects/Architecting-Near-Packaged-Optics-for-AI-Datacenters-Key-Technology-Choices-and-Trade-offs.pdf#page=7|PDF p.7]]

## 关联与比较
[[knowledge/concepts/network-optical-integration]]；[[knowledge/comparisons/network-optics-integration-tradeoffs]]；[[knowledge/sources/src-50163e1444b2]]展示集成laser NPO另一实现。

## 不确定性与待验证
缺少现场维修时间、hot/cold insertion能力、lifetime与成本。应在相同modulator入光功率下算ELS分光/connector损耗，不能把“~6pJ”当任何NPO设计都可达到。
