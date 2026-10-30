---
id: "src-7b98ab510cf5"
type: "source"
title: "nVent：AMD Helios 高液冷比例下仍需后门换热器"
source_path: "executive-sessions/39_nVent RDHX cooling for AMD Helios™ presented by nVent.pdf"
source_git_blob_sha: "561061cd0323fbf200e7fe95c0b48899587208b9"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 10
review_status: "analyzed-visual"
evidence_pages: [2, 3, 4, 5, 6, 7, 8]
text_reviewed: true
key_pages_visual_checked: [3, 6, 7]
tags: ["ocp2026", "source", "executive-expo"]
concepts: ["[[knowledge/concepts/executive-expo-liquid-cooling-evidence]]", "[[knowledge/concepts/sustainability-thermal-validation-ladder]]"]
---

# nVent：AMD Helios 高液冷比例下仍需后门换热器

## 核心结论
高比例直接液冷并不消除空气侧负荷：Helios 示例为 246 kW、89%/11% 液体/空气分担，残余空气热量约 27 kW，需要 RDHX 或其他房间级散热途径。[[executive-sessions/39_nVent RDHX cooling for AMD Helios™ presented by nVent.pdf#page=6|PDF p.6]]

## 关键证据
- Helios 双开门 RDHX 设计目标为 25–45 kW 热排出、48 VDC 供电、顶部或底部接管。[[executive-sessions/39_nVent RDHX cooling for AMD Helios™ presented by nVent.pdf#page=6|PDF p.6]]
- 两扇门的盘管通过 T 接共用一套控制阀/传感器；门控制器联动避免相互冲突，差压调速避免过度拉动服务器风扇。[[executive-sessions/39_nVent RDHX cooling for AMD Helios™ presented by nVent.pdf#page=7|PDF p.7]]
- 标准 RDHX 的最大 68 kW 规格对应 14°C 水和 5,885 CFM，不能套用于 Helios 的温水工况。[[executive-sessions/39_nVent RDHX cooling for AMD Helios™ presented by nVent.pdf#page=4|PDF p.4]]

## 指标与条件
p.2 用约 250 kW×11%=27.5 kW 作概略说明；p.6 的具体机架数值是 246 kW，两者为精度不同的示例而非两项测量。换热量必须与供水温度、风量和房间露点一起审核。[[executive-sessions/39_nVent RDHX cooling for AMD Helios™ presented by nVent.pdf#page=2|PDF p.2]][[executive-sessions/39_nVent RDHX cooling for AMD Helios™ presented by nVent.pdf#page=6|PDF p.6]]

## 图表与架构
p.3 区分 CWS、FWS、TCS 及 CDU；直接将设施水接到后门的图注条件是能够管理露点。不能因“空气转液体”就省略凝露控制。[[executive-sessions/39_nVent RDHX cooling for AMD Helios™ presented by nVent.pdf#page=3|PDF p.3]]

## 关联与比较
与电源液冷、液冷光模块结合，才能讨论接近完整的机架热捕获率；提高 D2C 比例仍需检查 DIMM、电源、线缆和网络设备的残余散热。

## 不确定性与待验证
N+1 风扇和控制冗余是产品设计描述，不是机房级可用性保证；尚缺单门失效、阀卡滞、传感器漂移时的实际热稳定测试。[[executive-sessions/39_nVent RDHX cooling for AMD Helios™ presented by nVent.pdf#page=5|PDF p.5]][[executive-sessions/39_nVent RDHX cooling for AMD Helios™ presented by nVent.pdf#page=8|PDF p.8]]

## 知识网络
[[knowledge/concepts/executive-expo-liquid-cooling-evidence]] · [[knowledge/concepts/sustainability-thermal-validation-ladder]]
