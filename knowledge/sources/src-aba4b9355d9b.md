---
id: "src-aba4b9355d9b"
type: "source"
title: "Multidomain Time Synchronization in the Modern Datacenter: From Network to Workload"
source_path: "Time Appliances/Multidomain Time Synchronization in the Modern Datacenter- From Network to Workload.pdf"
source_git_blob_sha: "827f28b21b62ba7195e3e672c48fa81e9fb058c4"
source_commit: "d6e362b7bb1e65327b9ff005e9b55b5850ccbb34"
source_pages: 11
review_status: "analyzed-visual"
evidence_pages: [2, 3, 5, 7, 9, 11]
text_reviewed: true
key_pages_visual_checked: [4, 6, 8]
tags: ["ocp2026", "networking"]
concepts: ["[[knowledge/concepts/network-clock-evidence]]"]
---

# Multidomain Time Synchronization in the Modern Datacenter: From Network to Workload

## 核心结论
Intel把global UTC与rack-local精确同步拆成不同timescale：机架内应用可使用较短hop的auxclock，而全球日志继续CLOCK_REALTIME。高可用还需同时跟踪多个GM的hot standby，不只等待BMCA重新选主。[[Time Appliances/Multidomain Time Synchronization in the Modern Datacenter- From Network to Workload.pdf#page=3|PDF p.3]][[Time Appliances/Multidomain Time Synchronization in the Modern Datacenter- From Network to Workload.pdf#page=7|PDF p.7]]

## 关键证据
rack-local最多两hop，可能优于50ns software-visible clock，但不必TAI可追溯；global可追GNSS/UTC且hop更多。[[Time Appliances/Multidomain Time Synchronization in the Modern Datacenter- From Network to Workload.pdf#page=3|PDF p.3]] VM以TSC为共用reference共享clock，当前PTP KVM路径往往需hypervisor与VM exit，泛化仍待完成。[[Time Appliances/Multidomain Time Synchronization in the Modern Datacenter- From Network to Workload.pdf#page=5|PDF p.5]]
Host方案用每backup GM一个vclock与Clock Manager；IPU方案固件同时跟踪多个GM，向host暴露复合单PHC。备份若未紧密同步，切换仍会产生大skew。[[Time Appliances/Multidomain Time Synchronization in the Modern Datacenter- From Network to Workload.pdf#page=7|PDF p.7]]

## 指标与条件
99.9999% availability和rack-local<50ns均为目标/潜力，不是文件测量SLA；“BMCA数秒切换”是问题陈述，无测试分布。[[Time Appliances/Multidomain Time Synchronization in the Modern Datacenter- From Network to Workload.pdf#page=2|PDF p.2]][[Time Appliances/Multidomain Time Synchronization in the Modern Datacenter- From Network to Workload.pdf#page=3|PDF p.3]][[Time Appliances/Multidomain Time Synchronization in the Modern Datacenter- From Network to Workload.pdf#page=7|PDF p.7]]

## 图表与架构
已核p.4/6/8静态导出图，global和rack-local分别跨host/IPU、privileged/unprivileged VM映射；原页含animation，PDF不能恢复时序。PTM给host-IPU共用reference而不是自动把所有timescale变成相同UTC。[[Time Appliances/Multidomain Time Synchronization in the Modern Datacenter- From Network to Workload.pdf#page=11|PDF p.11]]

## 关联与比较
[[knowledge/concepts/network-clock-evidence]]；[[knowledge/sources/src-fef1d5b111ed]]补共同GNSS坏源风险；[[knowledge/sources/src-a1c813b65c00]]给多hop误差预算。

## 不确定性与待验证
auxclock/Linux/Clock Manager支持、OCP-DC profile改进与Byzantine容错列future work。[[Time Appliances/Multidomain Time Synchronization in the Modern Datacenter- From Network to Workload.pdf#page=9|PDF p.9]] 需测试failover phase jump、VM migration、auxclock身份/漂移及应用误用不同timescale。
