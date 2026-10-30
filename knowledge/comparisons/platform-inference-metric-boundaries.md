---
type: "comparison"
title: "推理与机房效率指标不可混算：七种证据边界"
review_status: "synthesis"
tags: ["ocp", "platform", "comparison"]
sources: ["[[knowledge/sources/src-954c2f254f50]]", "[[knowledge/sources/src-eb561d8e385e]]", "[[knowledge/sources/src-8d1efe38d717]]", "[[knowledge/sources/src-3a6eadeb1fd2]]", "[[knowledge/sources/src-4a30c773bec5]]", "[[knowledge/sources/src-47273118489c]]", "[[knowledge/sources/src-3f525f18fc6b]]", "[[knowledge/sources/src-d4ac456fb37b]]"]
updated: "2026-10-30"
---

# 推理与机房效率指标不可混算：七种证据边界

## 比较问题与口径

“更多tokens/更少瓦/更便宜”是否证明同一服务更好？只有固定模型质量、工作负载、输出口径、延迟约束、测量范围和成本边界才可比较。以下不是产品排名，而是防止把不同证据拼成伪结论。

## 并列证据

### 1. Offline吞吐 ≠ 在线SLA
AMD Helios主旨17,000tokens/s/GPU明确是AMD-measuredMLPerfofflineconfig。没有在线TTFT、TPOT或p99约束，不能直接与interactive曲线比较。[[knowledge/sources/src-954c2f254f50|源卡]] · [[keynotes/02_Building the Next Era of AI Infrastructure.pdf#page=15|PDF p.15]]

### 2. P90交互速度 ≠ TTFT
AgentX示例AMD+TileRT约470tokens/s/user同时提示较高TTFT；prefill/decode分离可改变一个指标而恶化另一个。并且FP8与FP4、engine不同，必须保留。[[knowledge/sources/src-3a6eadeb1fd2|源卡]] · [[market-impact-adoption/04_From Silicon to Services.pdf#page=11|PDF p.11]]

### 3. 全栈相对收益随SLA改变
同一研究中的Rubinpreview，在DeepSeekV4Pro与matchingP90interactivity下，对bestGB300engine为100tok/s/user时2.1×、150时7.2×tokens/MW；utilitypower是模型、软件prerelease。这与NVIDIA主旨“up to30×”并不是相同实验条件，不能当作互相独立的验证或直接判冲突。[[knowledge/sources/src-3a6eadeb1fd2|源卡]] · [[market-impact-adoption/04_From Silicon to Services.pdf#page=12|PDF p.12]] [[knowledge/sources/src-eb561d8e385e|源卡]] · [[keynotes/06_AI Factories at Scale Advancing Open Infrastructure for Agentic AI.pdf#page=5|PDF p.5]]

### 4. KV缓存命中实验 ≠ 所有请求
SKhynix100%hitmicrobenchmark调优后SSDTTFT为DRAM的1.07–1.14×；ShareGPTmacro使用相等cachecapacity。SamsungFDP重放WAF2.600→1.425、p90object-I/O改善，脚注说不是servingTTFT。不能将它们相乘求端到端tokens/s。[[knowledge/sources/src-3f525f18fc6b|源卡]] · [[storage/Storage-as-a-Performance-Tier-for-LLM-Serving.pdf#page=7|PDF p.7]] [[knowledge/sources/src-3f525f18fc6b|源卡]] · [[storage/Storage-as-a-Performance-Tier-for-LLM-Serving.pdf#page=9|PDF p.9]] [[knowledge/sources/src-d4ac456fb37b|源卡]] · [[storage/Vertical-Optimizations-for-KV-Infrastructure.pdf#page=6|PDF p.6]]

### 5. 模型/路由选择 ≠ 单芯片提升
Intel~60%cost和>80%per-queryenergy引述多份routing研究，并保留<1%quality/performance下降条件；不能当作CrescentIsland同模型硬件实测。quality约束必须在成本比较之前定义。[[knowledge/sources/src-8d1efe38d717|源卡]] · [[keynotes/13_Put Every Prompt in Its Place.pdf#page=5|PDF p.5]]

### 6. 削峰 ≠ 减少总能量
IPS两个训练案例为ACwhippeaks−13%/−51%；没有总能量积分和训练吞吐。Nscale案例是在相同provisionedbudget下GPU+37%、throughput+49%，不能改写成相同实际耗电或每GPU提升49%。[[knowledge/sources/src-4a30c773bec5|源卡]] · [[market-impact-adoption/05_Intelligent Power Smoothing at the Vera-Rubin Rack.pdf#page=4|PDF p.4]] [[knowledge/sources/src-4a30c773bec5|源卡]] · [[market-impact-adoption/05_Intelligent Power Smoothing at the Vera-Rubin Rack.pdf#page=5|PDF p.5]] [[knowledge/sources/src-eb561d8e385e|源卡]] · [[keynotes/06_AI Factories at Scale Advancing Open Infrastructure for Agentic AI.pdf#page=13|PDF p.13]]

### 7. 模拟器reward ≠ 安全生产收益
JCI2MW/3360GPU为耦合模拟，最佳reward+11.5%，但两动作/两agent只有2/8低于85°C；另有92°Cepisode终止。独立500MW算例的+31%tokens/day不是该模拟实测，也不是现场部署。[[knowledge/sources/src-47273118489c|源卡]] · [[market-impact-adoption/More-Tokens-Same-Megawatts-How-Agentic-AI-Rewrites-AI-Factory-Economics.pdf#page=14|PDF p.14]] [[knowledge/sources/src-47273118489c|源卡]] · [[market-impact-adoption/More-Tokens-Same-Megawatts-How-Agentic-AI-Rewrites-AI-Factory-Economics.pdf#page=16|PDF p.16]] [[knowledge/sources/src-47273118489c|源卡]] · [[market-impact-adoption/More-Tokens-Same-Megawatts-How-Agentic-AI-Rewrites-AI-Factory-Economics.pdf#page=24|PDF p.24]] [[knowledge/sources/src-47273118489c|源卡]] · [[market-impact-adoption/More-Tokens-Same-Megawatts-How-Agentic-AI-Rewrites-AI-Factory-Economics.pdf#page=29|PDF p.29]]

## 可比较记录模板

每条候选数据记录：`模型/精度/质量门槛；input+output长度与复用；请求到达/并发；TTFT、TPOT、E2E及分位；有效output和totaltokens分开；芯片/机架/utility能量；测量/模拟/预测；硬件软件版本；价格与资本摊销；重复次数/置信区间`。

缺少上述项时，把数据当设计假设或需复现实验，不强行排名。商业决策最终宜看满足质量与SLA后的cost/task、J/task、有效tokens/s及失效恢复，而非让“token”同时代表输入缓存、输出生成和业务成功。

## 未决问题

现资料未提供同一真实agenttrace下跨GPU/CPU/存储/电力策略的完整联合实验。需要共享trace与可重跑recipe，并报告饱和区、故障/热节流与模型质量变化，才能把硬件PPA转为可兑现服务经济性。
