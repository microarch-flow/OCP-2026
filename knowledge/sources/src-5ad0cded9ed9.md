---
id: "src-5ad0cded9ed9"
type: "source"
title: "Ciena ACC：线性redriver延长铜距，但67dB不是被动通道能力"
source_path: "expo-hall-sessions/Extending Copper for Efficient Next-Generation Scale-Up Networks presented by Ciena.pdf"
source_git_blob_sha: "cec34aa19d98f44b8ce25a61aaa73030d8232b6e"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 10
review_status: "analyzed-visual"
evidence_pages: [3, 5, 6, 7, 8]
text_reviewed: true
key_pages_visual_checked: [3, 6, 8]
tags: ["ocp2026", "expo-hall"]
concepts: ["[[knowledge/concepts/network-optical-integration]]"]
---

# Ciena ACC：线性redriver延长铜距，但67dB不是被动通道能力

## 核心结论
在200G/lane下，ACC用线性redriver延长铜距并减少retimer功耗/管理复杂度；AEC可更远但引入重定时开销。选择必须按ASIC至ASIC完整通道和FEC裕量，而非只看缆长。[[expo-hall-sessions/Extending Copper for Efficient Next-Generation Scale-Up Networks presented by Ciena.pdf#page=3|PDF p.3]] [[expo-hall-sessions/Extending Copper for Efficient Next-Generation Scale-Up Networks presented by Ciena.pdf#page=6|PDF p.6]]

## 关键证据、指标与条件
- 40dB示例预算：1.5m30AWG缆16dB+两媒体接口10dB，余14dB按1.2dB/in得到两端合计约12in、每侧6in；同图缆箭头却写15dB，记为内部1dB差异。标准reach表只是本讲转述，不作为本次外部标准核验。[[expo-hall-sessions/Extending Copper for Efficient Next-Generation Scale-Up Networks presented by Ciena.pdf#page=3|PDF p.3]]
- 8×200G表：ACC3.5m、1.5pJ/bit每端、3.3V无DC/DC；AEC4.5m、10pJ/bit每端、约2×35ns附加延迟、4+rails。ACC“Zero”指相对无重定时延迟的宣传简写，不是传播和模拟器件物理延迟为零。成本$/$$$$无实际报价。[[expo-hall-sessions/Extending Copper for Efficient Next-Generation Scale-Up Networks presented by Ciena.pdf#page=6|PDF p.6]]
- p8图是**redriver之前45dB、之后22dB**的67dB总损耗案例。右图固定后段22dB，前段45dB时BER约7×10⁻⁹，49dB约2×10⁻⁷；不是redriver把总损耗“降到22dB”。虚线约2×10⁻⁴未标具体FEC，不能据此推断post-FEC零错。[[expo-hall-sessions/Extending Copper for Efficient Next-Generation Scale-Up Networks presented by Ciena.pdf#page=8|PDF p.8]]
- ACC MSA首plugfest2026-08-31至09-04，8公司、32缆，数据尚匿名化；参与测试不等于公开互通结果已全部合格。[[expo-hall-sessions/Extending Copper for Efficient Next-Generation Scale-Up Networks presented by Ciena.pdf#page=7|PDF p.7]]

## 图表与架构
已核p3/6/8。p8左图t轴和error直方图没有解释采样/码字定义及总bit数，不推导可靠性FIT。展示是实验/器件级SI证据，非大集群运行历史。

## 关联与比较
[[knowledge/concepts/network-optical-integration]] 与 [[knowledge/comparisons/network-optics-integration-tradeoffs]]。不能把Samtec路线示意ACC~5m与本讲3.5m说成互相矛盾，测试链/速率/终端条件未统一。

## 不确定性与待验证
需功耗是否含所有lane/控制、温度、缆规、BER样本、FEC与失效恢复行为；特别检验热老化/弯折和host适配。市场销量预测来自第三方，不用作采购或商业确定事实。[[expo-hall-sessions/Extending Copper for Efficient Next-Generation Scale-Up Networks presented by Ciena.pdf#page=5|PDF p.5]]


跨源比较：[[knowledge/comparisons/network-channel-interface-budget]]。
