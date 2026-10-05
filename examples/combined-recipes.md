# 跨主题组合描述

以下是可直接改编的整体构造样板，均为文字候选，没有生成图片。每个场景中的数字、具体架构、标签与算法由本次研究内容补齐，不直接充当任何已完成实验的证据。

## 1. 任务性能预测驱动调度

左侧用一个带稳定任务 ID 的小型算子 DAG 表示任务，图穿过少量斜置编码平面，节点身份保持。硬件条件从侧面以独立属性条进入，实时观测放在下方有时间窗口的短记录里。只将实际使用的特征连接到融合位置。右侧对几种候选资源配置给出带单位的时长或显存预测，未选者保留轻轮廓，最后只有一个选择指向资源底板中的落点。任务图、特征、预测记录和设备使用不同形体，但共享线宽与色彩逻辑。

可组合词条：`graph-hardware-prediction`、`static-dynamic-features`、`multi-target-prediction`、`cost-model-search`、`topology-placement`。

可见短标签示例：Job A、Graph features、Device、Observed window、Predicted time、Memory、Selected。先确认图中标签语言再使用；示例不是强制文字清单。

## 2. 在线推理与离线训练资源借还

画面上方保留在线请求流，下方为同一组设备资源。资源底线、安全余量和允许训练借用的部分采用明确分界，不混成一块未定义利用率。时间沿左到右推进；训练在可借区运行后，负载触发回收，状态从保存或停止、释放、推理实例准备逐步推进。原来训练占用的槽在实际释放点才变空，推理只有就绪后进入运行状态。用简洁服务和训练模型小结构定位参与者，主体放在资源与时间的对应上。

可组合词条：`quota`、`training-inference-reclaim`、`preempt-resume`、`model-loading`、`lifecycle`。

## 3. Prefill—KV 交接—Decode

两类实例组并列，组内模型可以用少量层叠片与一个展开层表示。请求在上方进入 Prefill；生成的 KV 用与权重不同的数据片束经过传输区到 Decode。控制请求和中间数据保留同一请求身份，依赖线落到 KV 可用点。Decode 右侧展开连续 token，并保留后续缓存增长。多 GPU 实例用共同实例边界，不把一片权重、一个实例和一张设备混为一体。外围保留适量设备小轮廓即可。

可组合词条：`pd-handoff`、`model-instance`、`kv-cache`、`host-device-buffer`、`inference-budget`。

## 4. 分布式训练中的临时参数聚合与通信重叠

固定几个 rank 的位置，参数分片在各自位置以编号薄片表示。焦点层在执行前形成临时完整视图，完成后按配置重分片；梯度走独立 ReduceScatter 路径。下方只有两条主要时间轨道：当前层计算与下一层参数预取，必要的同步点用短垂线表示。实例、rank、层号保持可追踪。临时完整参数只在存活区间出现，图中不会随着迭代增加永久副本。配色按参数身份分组而不按每个框随机着色。

可组合词条：`fsdp-reshard`、`gradient-overlap`、`training-state`、`data-parallel`。

## 5. RL 采样、策略版本与训练

采样侧使用当前算法中的角色模型或同风格 Agent 图标，输出轨迹带，带上来源策略版本。轨迹经真实存在的评分与信号处理进入训练，更新后的权重沿独立反向路径返回。异步时保留多个采样器正在使用的不同版本，不让新权重发布瞬间覆盖已产生轨迹的来源。需要解释设备执行时，把逻辑角色映射到下方少量设备泳道；多个角色可在同设备顺序执行。角色、数据和资源三层保持区别。

可组合词条：`rl-rollout-train`、`policy-version`、`reward-advantage-mask`，以及已保留的 Agent AP07、AP09。

## 6. 系统软件的控制与执行分界

上方用规格页和观测页形成协调闭环，变化事件先进入工作队列；下方显示实际容器、进程或服务实例。动作经过边界接口改变受控对象，状态随后返回。若同时展示设备执行，应用经运行时与驱动提交内核，设备插件只留在资源发现和分配侧。终端、容器和设备的小符号按同一家族处理，少量边界框仅表达真实归属。控制、数据与内核执行不画成同一条连续箭头。

可组合词条：`controller-reconcile`、`watch-workqueue`、`pod-execution-chain`、`device-runtime-driver`、`process-isolation`。

## 7. 云原生集群与平台标识

复用集群、节点、CPU/GPU、内存和存储词条，按实际范围放置云轮廓及 Kubernetes Logo；节点仅展开焦点，存储区分本地与共享，物理互连与数据访问分别说明。Logo 不变成独立计算步骤，研究模块不因强调而改变真实部署归属。两种完整文字组合见 [Cloud 与 Logo 指南](../references/cloud-logo-composition.md)。


## 可执行场景输入

[GNN 预测与调度](scenarios/gnn-scheduling.md)、[Agent 生命周期](scenarios/agent-lifecycle.md)、[Kubernetes 异构集群](scenarios/kubernetes-cluster.md)提供具体对象和机制假设。当前是输入材料，不是已验收案例；[案例状态](scenarios/README.md)单独记录。
