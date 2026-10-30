---
id: "src-bbddc7859662"
type: "source"
title: "无中断更新的证明：从静态测量转向不变更新策略"
source_path: "Security/An Introduction to Attesting Hitlessly Updatable Systems.pdf"
source_git_blob_sha: "434ab80d69eeb74c6b24a454fa9e2aa6f9a6171e"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 18
review_status: "analyzed-visual"
evidence_pages: [2, 3, 10, 11, 12, 13, 14, 16]
tags: ["ocp", "source", "platform", "security"]
text_reviewed: true
key_pages_visual_checked: [12]
updated: "2026-10-30"
---

# 无中断更新的证明：从静态测量转向不变更新策略

> 阅读范围：已阅读本文件全部可提取文字（18页）。关键页已视觉核对：12；不代表逐页视觉审核。

## 核心结论

- Hitless update指新固件/软件激活不阻止运行工作负载前进；问题不只是减少停机，还包括证明生成之后系统仍能变更。[[Security/An Introduction to Attesting Hitlessly Updatable Systems.pdf#page=3|PDF p.3]][[Security/An Introduction to Attesting Hitlessly Updatable Systems.pdf#page=10|PDF p.10]]
- 不断获取更“新”的测量仍会再次过期；作者要求证据同时包含历史和约束未来状态的Update Policy。[[Security/An Introduction to Attesting Hitlessly Updatable Systems.pdf#page=11|PDF p.11]][[Security/An Introduction to Attesting Hitlessly Updatable Systems.pdf#page=12|PDF p.12]]
- Update Policy必须直到reset保持不变，不能被同一次hitless机制修改，否则失去对未来行为的保证。[[Security/An Introduction to Attesting Hitlessly Updatable Systems.pdf#page=16|PDF p.16]]

## 关键证据

- 更新策略示例包括anti-rollback与二次授权公钥。Verifier核对历史/当前状态，Verifier或Relying Party还需理解未来变更政策。[[Security/An Introduction to Attesting Hitlessly Updatable Systems.pdf#page=12|PDF p.12]][[Security/An Introduction to Attesting Hitlessly Updatable Systems.pdf#page=13|PDF p.13]]
- Relying Party必须拒绝不可接受的策略，不能只看当前固件测量；策略先被接受，才可能避免每次更新预先通知。[[Security/An Introduction to Attesting Hitlessly Updatable Systems.pdf#page=14|PDF p.14]]
- 文件明确假定证据完整准确、密码真实性完好，且不推荐具体证据格式；这些都是论证前提。[[Security/An Introduction to Attesting Hitlessly Updatable Systems.pdf#page=2|PDF p.2]]

## 指标与条件

无更新中断时间、SLA改善、测量开销或日志容量实测。版本1/2/3/4是时间线示例，不是实际版本。历史潜在无界，需管理其存储、完整性和验证成本。[[Security/An Introduction to Attesting Hitlessly Updatable Systems.pdf#page=16|PDF p.16]]

## 图表与架构

已视觉核对p.12时间线：证据覆盖过去/当前，策略箭头延伸到依赖方使用系统时及以后；这正是静态哈希不能承担的保证。

## 关联与比较

可与SPDM运行时授权、PLDM更新共同组成闭环：安装授权不等于可证明的未来政策；需要让证明消费者实际验证该政策。

## 不确定性与待验证

作者承认未来更新也可引入bug；策略可限制允许变更，但不能证明每次被授权的代码无漏洞。需补策略表达/撤销、日志压缩、版本依赖和跨设备一致性实现。[[Security/An Introduction to Attesting Hitlessly Updatable Systems.pdf#page=16|PDF p.16]]

