# 当前主题与词条索引

按需读主题；Cloud 主题复用关联词条，不重复立项。

## Cloud 与云原生组合

[主题正文](../topics/cloud-native-kubernetes.md) · 云平台、Kubernetes Logo、连接线及相关节点、CPU/GPU、存储、控制与执行组件；下列关联条目复用同一知识目录，不重复计数。

[Cloud、云平台与云原生集群](../topics/cloud-native-kubernetes.md#cloud-environment) · [Kubernetes Logo 与资源图标组合](../topics/cloud-native-kubernetes.md#kubernetes-platform-logo) · [架构连接线、流向与关系](../topics/cloud-native-kubernetes.md#architecture-connections)

关联已有条目：[集群](../topics/hardware-cluster.md#cluster) · [计算节点与服务器](../topics/hardware-cluster.md#node) · [CPU、核心与主机处理](../topics/hardware-cluster.md#cpu-processor) · [GPU 与加速卡](../topics/hardware-cluster.md#accelerator) · [异构设备画像](../topics/hardware-cluster.md#device-profile) · [NUMA 与互连局部性](../topics/hardware-cluster.md#numa-locality) · [空间分区、时间共享与并发](../topics/hardware-cluster.md#device-sharing-modes) · [网络与互连](../topics/hardware-cluster.md#network) · [内存、显存与缓冲区](../topics/data-memory-storage.md#memory) · [数据集与存储](../topics/data-memory-storage.md#storage) · [本地、共享与云存储](../topics/data-memory-storage.md#storage-services) · [数据分片与缓存局部性](../topics/data-memory-storage.md#dataset-locality) · [主机—设备传输与缓冲](../topics/data-memory-storage.md#host-device-buffer) · [容器与运行环境](../topics/systems-runtime.md#deployment) · [控制器与协调循环](../topics/systems-runtime.md#controller-reconcile) · [Watch、缓存与工作队列](../topics/systems-runtime.md#watch-workqueue) · [调度绑定与节点执行](../topics/systems-runtime.md#pod-execution-chain) · [设备插件、运行时与驱动](../topics/systems-runtime.md#device-runtime-driver) · [微服务调用图与执行资源](../topics/systems-runtime.md#microservice-dependency) · [RPC、IPC 与事件循环](../topics/systems-runtime.md#rpc-event-runtime)

## 硬件与异构集群

[主题正文](../topics/hardware-cluster.md) · 集群、节点、GPU／加速卡、内部执行单元、互连与共享方式

[集群](../topics/hardware-cluster.md#cluster) · [计算节点与服务器](../topics/hardware-cluster.md#node) · [GPU 与加速卡](../topics/hardware-cluster.md#accelerator) · [线程、算子与计算单元](../topics/hardware-cluster.md#compute) · [网络与互连](../topics/hardware-cluster.md#network) · [异构设备画像](../topics/hardware-cluster.md#device-profile) · [NUMA 与互连局部性](../topics/hardware-cluster.md#numa-locality) · [空间分区、时间共享与并发](../topics/hardware-cluster.md#device-sharing-modes) · [CPU、核心与主机处理](../topics/hardware-cluster.md#cpu-processor)

## 数据、内存与存储

[主题正文](../topics/data-memory-storage.md) · 数据集、样本、存储、搬移、缓冲、局部性与内存映射

[内存、显存与缓冲区](../topics/data-memory-storage.md#memory) · [数据集与存储](../topics/data-memory-storage.md#storage) · [样本与数据加载](../topics/data-memory-storage.md#data-pipeline) · [主机—设备传输与缓冲](../topics/data-memory-storage.md#host-device-buffer) · [预取与双缓冲](../topics/data-memory-storage.md#prefetch-double-buffer) · [数据分片与缓存局部性](../topics/data-memory-storage.md#dataset-locality) · [Embedding 查找与缓存](../topics/data-memory-storage.md#embedding-cache) · [虚拟映射与分配器状态](../topics/data-memory-storage.md#virtual-physical-memory) · [本地、共享与云存储](../topics/data-memory-storage.md#storage-services)

## 深度学习与模型结构

[主题正文](../topics/models-deep-learning.md) · 神经网络、张量、Attention、GNN、MoE、视觉、多模态、推荐与压缩

[张量、向量与矩阵](../topics/models-deep-learning.md#tensor) · [算子与算子融合](../topics/models-deep-learning.md#operator) · [神经网络](../topics/models-deep-learning.md#network-model) · [注意力机制](../topics/models-deep-learning.md#attention) · [视觉网络与特征图](../topics/models-deep-learning.md#vision) · [GNN 与图表示](../topics/models-deep-learning.md#gnn) · [MoE 与专家](../topics/models-deep-learning.md#moe) · [多模态模型](../topics/models-deep-learning.md#multimodal) · [扩散与生成模型](../topics/models-deep-learning.md#diffusion) · [推荐模型与稀疏特征](../topics/models-deep-learning.md#recommendation) · [量化与反量化](../topics/models-deep-learning.md#quantization) · [剪枝与稀疏表示](../topics/models-deep-learning.md#sparsity) · [教师—学生蒸馏](../topics/models-deep-learning.md#distillation) · [MHA、GQA 与 MQA](../topics/models-deep-learning.md#attention-head-sharing) · [推荐模型与特征交互](../topics/models-deep-learning.md#feature-interaction)

## 任务性能预测

[主题正文](../topics/performance-prediction.md) · 任务结构、硬件条件、静动态特征、预测器训练使用、多目标、干扰与不确定性

[预测器与代价模型](../topics/performance-prediction.md#predictor) · [计算图与硬件条件预测](../topics/performance-prediction.md#graph-hardware-prediction) · [静态特征与动态观测](../topics/performance-prediction.md#static-dynamic-features) · [预测器离线训练与在线使用](../topics/performance-prediction.md#predictor-train-serve) · [多目标性能与资源输出](../topics/performance-prediction.md#multi-target-prediction) · [共置干扰与性能预测](../topics/performance-prediction.md#interference-prediction) · [预测范围、校准与泛化](../topics/performance-prediction.md#prediction-uncertainty) · [执行依赖与关键路径预测](../topics/performance-prediction.md#trace-critical-path) · [候选配置与代价模型搜索](../topics/performance-prediction.md#cost-model-search)

## 集群调度与资源管理

[主题正文](../topics/scheduling-resources.md) · 准入、排序、放置、配额、Gang、回填、抢占、弹性与训推借还

[调度器](../topics/scheduling-resources.md#scheduler) · [配额、借用与回收](../topics/scheduling-resources.md#quota) · [放置与候选比较](../topics/scheduling-resources.md#placement) · [共享、隔离与干扰](../topics/scheduling-resources.md#sharing) · [准入、排序与放置](../topics/scheduling-resources.md#admission-ranking) · [多资源需求与可行性](../topics/scheduling-resources.md#multi-resource-demand) · [Gang 与整组资源预留](../topics/scheduling-resources.md#gang-reservation) · [回填时间窗](../topics/scheduling-resources.md#backfill-window) · [抢占、迁移与恢复](../topics/scheduling-resources.md#preempt-resume) · [弹性分配与重配置](../topics/scheduling-resources.md#elastic-allocation) · [在线推理与离线训练借还](../topics/scheduling-resources.md#training-inference-reclaim) · [碎片、局部性与拓扑放置](../topics/scheduling-resources.md#topology-placement)

## 训练、微调与分布式执行

[主题正文](../topics/training-distributed.md) · 前反向、并行、通信、状态分片、微调、混合精度与检查点

[集合通信](../topics/training-distributed.md#collective) · [训练迭代](../topics/training-distributed.md#training) · [分布式并行](../topics/training-distributed.md#parallelism) · [训练状态内存](../topics/training-distributed.md#training-state) · [微调、LoRA 与 Adapter](../topics/training-distributed.md#peft) · [检查点、恢复与重计算](../topics/training-distributed.md#checkpoint) · [数据并行与梯度同步](../topics/training-distributed.md#data-parallel) · [张量并行](../topics/training-distributed.md#tensor-parallel) · [流水线、microbatch 与气泡](../topics/training-distributed.md#pipeline-microbatch) · [专家并行与 token 分派](../topics/training-distributed.md#expert-parallel) · [序列并行与上下文并行](../topics/training-distributed.md#sequence-context-parallel) · [FSDP 与状态聚合再分片](../topics/training-distributed.md#fsdp-reshard) · [梯度分桶与通信重叠](../topics/training-distributed.md#gradient-overlap) · [优化器状态与卸载](../topics/training-distributed.md#optimizer-offload) · [混合精度与损失缩放](../topics/training-distributed.md#mixed-precision) · [激活检查点与重计算](../topics/training-distributed.md#activation-recompute) · [异步检查点与可靠恢复](../topics/training-distributed.md#async-checkpoint)

## 强化学习与对齐

[主题正文](../topics/rl-alignment.md) · 采样、评分、策略更新、异步版本、样本信号、SFT 与偏好优化

[模型角色](../topics/rl-alignment.md#model-roles) · [强化学习与对齐](../topics/rl-alignment.md#rl) · [Rollout、评分与策略更新](../topics/rl-alignment.md#rl-rollout-train) · [异步采样与策略版本](../topics/rl-alignment.md#policy-version) · [奖励、优势与样本掩码](../topics/rl-alignment.md#reward-advantage-mask) · [SFT 与偏好优化](../topics/rl-alignment.md#sft-dpo)

## LLM 推理与服务

[主题正文](../topics/inference-serving.md) · 请求、批次、实例、阶段分离、KV、投机、驻留与资源预算

[模型身份与实例](../topics/inference-serving.md#model-instance) · [请求](../topics/inference-serving.md#request) · [批处理与运行集合](../topics/inference-serving.md#batch) · [Token 与生成候选](../topics/inference-serving.md#token) · [Prefill / Decode](../topics/inference-serving.md#prefill-decode) · [KV Cache 与前缀共享](../topics/inference-serving.md#kv-cache) · [模型加载与驻留](../topics/inference-serving.md#model-loading) · [Prefill／Decode 分离与 KV 交接](../topics/inference-serving.md#pd-handoff) · [分块 Prefill 与连续批次](../topics/inference-serving.md#chunked-prefill) · [投机生成、验证与回退](../topics/inference-serving.md#speculative-verification) · [前缀共享、引用与驱逐](../topics/inference-serving.md#prefix-cache-lifecycle) · [多模型与多 LoRA 服务](../topics/inference-serving.md#multi-model-lora-serving) · [专家驻留、缓存与搬移](../topics/inference-serving.md#expert-residency) · [推理资源预算与准入](../topics/inference-serving.md#inference-budget)

## 系统软件与运行时

[主题正文](../topics/systems-runtime.md) · 控制器、工作队列、容器、驱动、进程、异步执行、编译与图重放

[容器与运行环境](../topics/systems-runtime.md#deployment) · [编译器与执行优化](../topics/systems-runtime.md#compiler) · [框架、机构与服务边界](../topics/systems-runtime.md#api-framework) · [控制器与协调循环](../topics/systems-runtime.md#controller-reconcile) · [Watch、缓存与工作队列](../topics/systems-runtime.md#watch-workqueue) · [调度绑定与节点执行](../topics/systems-runtime.md#pod-execution-chain) · [设备插件、运行时与驱动](../topics/systems-runtime.md#device-runtime-driver) · [进程、线程与隔离边界](../topics/systems-runtime.md#process-isolation) · [RPC、IPC 与事件循环](../topics/systems-runtime.md#rpc-event-runtime) · [背压与流量控制](../topics/systems-runtime.md#backpressure) · [IR、图重写与代码生成](../topics/systems-runtime.md#compiler-lowering) · [CUDA Graph 捕获与重放](../topics/systems-runtime.md#cuda-graph) · [微服务调用图与执行资源](../topics/systems-runtime.md#microservice-dependency)

## 可观测性与可靠性

[主题正文](../topics/observability-reliability.md) · 指标、执行轨迹、瓶颈、SLO、对象状态、故障与恢复

[对象生命周期](../topics/observability-reliability.md#lifecycle) · [SLO 与性能记录](../topics/observability-reliability.md#slo) · [执行轨迹与链路追踪](../topics/observability-reliability.md#trace) · [指标与性能观测](../topics/observability-reliability.md#metrics) · [故障、版本与恢复](../topics/observability-reliability.md#fault) · [验证、记录与选择结果](../topics/observability-reliability.md#validation) · [采样窗口与硬件计数器](../topics/observability-reliability.md#profiling-window) · [任务、算子与内核关联](../topics/observability-reliability.md#trace-correlation) · [计算、访存与通信瓶颈](../topics/observability-reliability.md#bottleneck-roofline) · [故障、重试与有效恢复](../topics/observability-reliability.md#reliability-retry)

## Agent 与工作流

[主题正文](../topics/agents-workflows.md) · 保留已认可的 Agent 身份、协作、消息、工具、产物与执行映射画法

[工作流与 DAG](../topics/agents-workflows.md#workflow) · [Agent 与多 Agent](../topics/agents-workflows.md#agent) · [工具调用与产物](../topics/agents-workflows.md#tool) · [上下文、记忆与 RAG](../topics/agents-workflows.md#context-memory) · [分支、路由与循环](../topics/agents-workflows.md#routing)
