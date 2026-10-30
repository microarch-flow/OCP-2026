---
type: "question"
title: "AI 基础设施待验证：推理加速器架构与商业化证据"
tags: ["ai-infra", "inference-architecture"]
---

# AI 基础设施待验证：推理加速器架构与商业化证据

## 本批资料能支持什么
可建立 serving-shape 决策、fabric 故障域、遥测契约、铜 scale-up 验收和证据驱动诊断框架。多数材料没有固定模型+配置+SLA+功率+价格，故不足以给加速器性价比结论。

## 按优先级补证据
1. **业务可比性**：同模型版本、量化精度、上下文/输出分布、p99 TTFT/TPOT、质量门限下 goodput 与最大并发。[[knowledge/sources/src-e3d51d9c0fe6]] 要求 SLO 而非带宽排名，[[ai-clusters/Scaling Purpose-Built AI Models via OCP Aligned Distributed Inference Fabrics.pdf#page=13|PDF p.13]]。
2. **硬件实际配置**：每 accelerator HBM/DDR 容量、PCIe/C2C、NIC/plane 数、交换拓扑、超售、功率和 thermal limits；[[knowledge/sources/src-d29c84030e6a]] 的 fabric-only latency 不足以填端到端表。
3. **失效与灰故障**：链路 flap/blackhole、故障检测→恢复 p99、残余 BW、请求重试与 checkpoint/cold-start 代价。[[knowledge/sources/src-79e676213ada]] 的阈值与案例仍不完整。
4. **监控自扰动**：生产轮询 on/off 的 BusBW、token goodput、p99；[[knowledge/sources/src-02fd0252e899]] 的 >1% 是提案门槛，不是用户系统验收结果。
5. **商业化口径**：可采购日期、批量交付、软件栈成熟度、维修/RMA、保修、TCO 假设（电费、利用率、折旧、网络/存储/人工）。峰值 tokens/s 或 roadmap 不等于可售 SLA。

## 材料完整性缺口
[[knowledge/sources/src-9167806700b4]] 与 [[knowledge/sources/src-584ef1c56cd4]] 只有一页圆桌名单；无法恢复口头内容。[[knowledge/sources/src-79e676213ada]] p.11 仍有未填占位。明确区分“全部页已读”与“演讲完整信息已取得”。

## 应避免的误读
MRC MPR=8 示例不是产品默认；Tahan cut-through -25% 不是当前交付；分离推理不是天然更快；CPO 的 pJ/bit 方向不是定量 TCO；中断构成比不是器件失效率。
