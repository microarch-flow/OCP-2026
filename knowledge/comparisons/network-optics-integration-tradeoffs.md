---
id: "network-optics-integration-tradeoffs"
type: "comparison"
title: "光互连选型对照：效率、可维修性与证据成熟度"
tags: ["ocp-2026", "networking"]
review_status: "synthesized"
---

# 光互连选型对照：效率、可维修性与证据成熟度

## 比较问题与口径
问题不是哪一个缩写胜出，而是在目标lane速率、reach、thermal与维护策略下，哪一个**失效/服务边界**最合适。本页没有统一bench平台，不把不同来源数值拼成性能排名。

## 方案与证据
- **Retimed pluggable**：模块DSP提供均衡/诊断/独立更换边界，但引入能耗、FW故障和接口。Meta某FRO对照的DSP FW/unknown事件比例不可泛化到所有模块。[[knowledge/sources/src-ada5498062ed]] [[ocp-special-focus-photonics/Integrated-Optics-at-Scale-for-AI-Infrastructure-From-51.2T-CPO-Validation-to-Meta-s-102.4T-Integrated-Optics-Switch.pdf#page=4|PDF p.4]][[knowledge/sources/src-6e3f5ef8025b]] [[ocp-special-focus-photonics/Photonics-for-AI-Aligning-the-Stack-from-Components-to-Cloud.pdf#page=4|PDF p.4]]
- **LPO**：去模块DSP、host接手均衡/联合校准。100G/lane特定LPO-LPO生产与lab有可靠性、-46%模块功耗证据；不是整机-46%。[[knowledge/sources/src-6ce06488969f]] [[networking/08_Operating Linear Pluggable Optics at Hyperscale From Link Management t.pdf#page=4|PDF p.4]][[knowledge/sources/src-6ce06488969f]] [[networking/08_Operating Linear Pluggable Optics at Hyperscale From Link Management t.pdf#page=9|PDF p.9]]
- **CPO**：最短电路径，紧耦合光引擎/ASIC；51.2T已有1.35M系统小时无不可维修故障观察。ELS外置降低主要故障维修范围，不能假定引擎永久无故障。[[knowledge/sources/src-ada5498062ed]] [[ocp-special-focus-photonics/Integrated-Optics-at-Scale-for-AI-Infrastructure-From-51.2T-CPO-Validation-to-Meta-s-102.4T-Integrated-Optics-Switch.pdf#page=6|PDF p.6]][[knowledge/sources/src-ada5498062ed]] [[ocp-special-focus-photonics/Integrated-Optics-at-Scale-for-AI-Infrastructure-From-51.2T-CPO-Validation-to-Meta-s-102.4T-Integrated-Optics-Switch.pdf#page=8|PDF p.8]]
- **NPO/socketed Open CPX**：制造返工、多供应商和混合光学更灵活；连接器/走线增加SI与448G retimer风险；尚无本组同等NPO量产RAS统计。[[knowledge/sources/src-ada5498062ed]] [[ocp-special-focus-photonics/Integrated-Optics-at-Scale-for-AI-Infrastructure-From-51.2T-CPO-Validation-to-Meta-s-102.4T-Integrated-Optics-Switch.pdf#page=8|PDF p.8]][[knowledge/sources/src-18fec3539510]] [[fti-workshop-short-reach-optical-interconnects/Beyond-Copper-Optical-Opportunities-for-AI-Scale-up-Fabrics.pdf#page=8|PDF p.8]]
- **XPO**：12.8T模块与液冷/可换引擎，物理包络可以装LPO/FRO/coherent，不能单独赋予一个pJ/bit或固定reach。[[knowledge/sources/src-18fec3539510]] [[fti-workshop-short-reach-optical-interconnects/Beyond-Copper-Optical-Opportunities-for-AI-Scale-up-Fabrics.pdf#page=7|PDF p.7]][[knowledge/sources/src-7569c3741a64]] [[ocp-special-focus-photonics/The-Interconnect-Inflection-Point-Evolving-Intra-and-Multi-Rack-Scale-Up-AI-Networks.pdf#page=5|PDF p.5]]

## 不可直接比较的数字
LPO -46%是fixed-fan实验模块功耗；CPO/NPO -60%是102.4T下一代光学规格；XPO 8×是模块capacity对OSFP；1.5OU/1RU密度还不是整机rack内可用带宽/每W。它们回答不同问题。[[knowledge/sources/src-6ce06488969f]] [[networking/08_Operating Linear Pluggable Optics at Hyperscale From Link Management t.pdf#page=9|PDF p.9]][[knowledge/sources/src-ada5498062ed]] [[ocp-special-focus-photonics/Integrated-Optics-at-Scale-for-AI-Infrastructure-From-51.2T-CPO-Validation-to-Meta-s-102.4T-Integrated-Optics-Switch.pdf#page=7|PDF p.7]][[knowledge/sources/src-18fec3539510]] [[fti-workshop-short-reach-optical-interconnects/Beyond-Copper-Optical-Opportunities-for-AI-Scale-up-Fabrics.pdf#page=7|PDF p.7]]

## 对架构评审的可执行要求（综合推导）
要求供应商提供共同reference workload和link budget，按module/port/system区分W、FIT/ALIR、repair time、sparing、灰尘/插拔/热循环。至少保留每事件raw log、每种TX/RX配对与reset后证据；同一firmware版本用同一failure定义。

## 下一份证据
200G/lane mixed-vendor方向性、NPO/CPO现场维修、448G插座/retimer预算、实际采购/运维成本。更多原始source尚在摄取，当前比较不声称覆盖全部光学路线。

## 关联
[[knowledge/concepts/network-optical-integration]] · [[knowledge/concepts/network-optics-reliability]]
