# Cloud、云原生与 Kubernetes 组合

本主题补充环境层次、Logo 位置和连接线三种表达，并聚合已有节点、设备、存储、控制与执行词条。**复用已有内容，不复制一套同名组件**。所有新增画法为文字候选；没有新增生图或论文图面审阅。

## 从整图选择已有组件

| 需要画的部分 | 已有或补充的词条 |
|---|---|
| 集群与节点 | [集群](hardware-cluster.md#cluster)、[节点](hardware-cluster.md#node)、[设备画像](hardware-cluster.md#device-profile) |
| CPU 与 GPU | [CPU](hardware-cluster.md#cpu-processor)、[GPU／加速卡](hardware-cluster.md#accelerator)、[共享模式](hardware-cluster.md#device-sharing-modes) |
| 内存与存储 | [内存显存](data-memory-storage.md#memory)、[数据集](data-memory-storage.md#storage)、[本地／共享／云存储](data-memory-storage.md#storage-services)、[数据局部性](data-memory-storage.md#dataset-locality) |
| 物理连接与数据供给 | [网络互连](hardware-cluster.md#network)、[NUMA／互连局部性](hardware-cluster.md#numa-locality)、[主机设备传输](data-memory-storage.md#host-device-buffer) |
| K8s 控制与运行 | [容器与运行环境](systems-runtime.md#deployment)、[控制器](systems-runtime.md#controller-reconcile)、[Watch／队列](systems-runtime.md#watch-workqueue)、[调度与节点执行](systems-runtime.md#pod-execution-chain)、[设备插件／驱动](systems-runtime.md#device-runtime-driver) |
| 服务、调用与观测 | [服务与资源映射](systems-runtime.md#microservice-dependency)、[RPC／事件](systems-runtime.md#rpc-event-runtime)、[可观测性主题](observability-reliability.md) |

## 本主题词条

[云平台与云原生集群](#cloud-environment) · [Kubernetes Logo](#kubernetes-platform-logo) · [连接线](#architecture-connections)

完整组合和官方素材说明见 [Cloud 与 Logo 组合指南](../references/cloud-logo-composition.md)。不要求一张图同时出现表中的全部对象；先选择本图的解释层次。与云相关的精细网络、鉴权、控制器实现仍需按实际研究补充。

<a id="cloud-environment"></a>

## Cloud、云平台与云原生集群

**词条 ID：** `cloud-environment`  
**词汇与别名：** Cloud、cloud native、云、云原生、云平台、云集群、私有云、混合云、region、availability zone、VPC、subnet  
**含义：** 运行环境、管理范围、网络范围或地域层级，以及其中的集群与服务；按本图实际需要展开。

### 云轮廓作为环境标题

在平台标题旁使用简洁云轮廓，下面用轻边界组织一个或多个集群；节点和设备直接复用已有词条。云符号只标识环境，不变成传输数据的中间步骤。复杂布局优先用标题标记而不是把所有节点挤进不规则云轮廓；简单总览可以将云轮廓本身作为整体外形。

### 云环境与集群的局部展开

外层用淡边界表示云环境，内部按实际归属组织集群、计算节点和存储；仅把一个节点向下拉出 CPU、GPU、主存与本地盘，其余节点保留简化身份。外部共享存储单独放在正确范围。由清楚的展开引线维持节点 ID，避免同一节点被误认为新增副本。

### 多云／本地并列与跨域路径

本地与远端云环境平行排列，采用相容的云、机架或节点形体，只有确实存在的请求、数据复制或控制关系跨域连接。地域、可用区、网络域和 Kubernetes 集群属于不同边界维度；重叠关系复杂时拆成逻辑与部署两幅视图，不强制画成固定层层包含。

**参考与取舍：** [C01](../references/sourcebook.md#c01)。集群组件层次以官方文本校对，云轮廓与整图布局是原创候选。

**必要边界：** 云原生不等于必须运行在公有云，也不等于只有 Kubernetes。不要无依据添加 region、VPC、托管控制面或云厂商；平台范围、网络隔离和部署归属分别标明。

**状态：** 原创／改编绘图描述可用；未生成图片。新增官方来源仅核文本，不宣称已审其图面或已获用户视觉认可。

<a id="kubernetes-platform-logo"></a>

## Kubernetes Logo 与资源图标组合

**词条 ID：** `kubernetes-platform-logo`  
**词汇与别名：** Kubernetes、K8s、logo、Logo、项目标识、平台标识、Pod 图标、Node 图标、Service 图标  
**含义：** 用准确项目标识说明平台身份，用资源图标或结构说明内部对象，并与整图层级协调。

### 集群边界标题

将官方 Kubernetes Logo 与集群名称组成一个小标题，放在实际集群边界的左上或阅读起点；内部继续画节点、Pod、服务和资源。Logo 与标题相近的视觉重量，不占据核心机制中心。独立集群或独立面板可按需重复，用 ID 区分，不在每个 CPU/GPU/Pod 上贴相同 Logo。

### 软件平台层标题

系统采用分层构图且 Kubernetes 是实现基础时，把 Logo 放在平台层标题。研究模块与既有组件以主次、强调色和短标签区分。软件层次不等于物理部署；研究模块实际在同一集群运行时，不能仅为突出贡献而移到集群边界外。

### 接口或折叠平台端点

详细图把 Logo 放在 Kubernetes API 或平台标题附近，交互箭头连到明确接口或组件；概览可以把 Logo＋准确名称作为折叠平台端点，箭头接该整体。一个视图中不要同时把 Logo 当作背景注释和独立运算节点。

### 资源图标与局部结构配合

项目 Logo 标平台，Pod、Service、Node 等图标标资源类型，实例旁保留名称或 ID。可选择社区资源图标或相容的简化构造，只在焦点对象旁展开容器、队列或设备。框架 Logo 放到对应运行时或服务标题，不组成无归属的技术栈贴纸墙。

**参考与取舍：** [C02](../references/sourcebook.md#c02)、[C04](../references/sourcebook.md#c04)。已读官方素材说明；具体位置和组合为本库设计，未用官方图面证明审美质量。

**必要边界：** 准确标识优先取官方素材；生图不能可靠保留时留位后插入真实 SVG/PNG，不把近似生成图称作官方 Logo。统一视觉尺寸、留白与标签，不扭曲标识。身份标识不表示项目方认证。

**状态：** 原创／改编绘图描述可用；未生成图片。新增官方来源仅核文本，不宣称已审其图面或已获用户视觉认可。

<a id="architecture-connections"></a>

## 架构连接线、流向与关系

**词条 ID：** `architecture-connections`  
**词汇与别名：** 连接线、连线、箭头、connector、edge、data flow、control flow、mapping、dependency、bus、switch、数据流、控制流、归属、局部展开  
**含义：** 通过端点、方向、路由和图例把资源关系、数据传输、控制动作、依赖和映射区分开。

### 分层布线与明确端口

节点或服务层按基线排列，线从面向目的地的端口出入；用短折线或柔和曲线绕开标签，为主数据路径预留通道。包含关系用边界或括号，部署映射用细引线，真正的数据／控制交互才画带方向的路径。线型含义在本图固定并附简短图例，不把“虚线”预设为所有辅助关系。

### 共享网络骨架与局部路径高亮

确有交换机、总线或共享网络时，用少量交换节点与物理链路构成骨架，计算与存储节点以简短支路接入。无向物理连线表示连通，焦点请求另用有向路径叠加；只高亮一条关键路径。简化后的总线需标为网络抽象，不能凭排版创造真实共享瓶颈或全连接拓扑。

### 主流程与外围反馈

主数据路径从左向右或从上向下展开，状态回传、监控和重试绕到外围；不同返回内容分别接真实接收者。跨越不相连的线避免视觉交点，必要时用跳线或调整通道，明确汇合处才画接点。多条同类线可以束化，保留源端与目的端映射，不用粗箭头遮盖未知关系。

**参考与取舍：** 原创绘图语法；可结合 [C01](../references/sourcebook.md#c01)、[C03](../references/sourcebook.md#c03)、[C05](../references/sourcebook.md#c05) 校对控制、数据与资源对象的技术关系。

**必要边界：** 物理互连、请求流、挂载、依赖、包含与映射不可不加说明地混用；双向箭头不自动代表两条独立链路，交叉不等于连接。没有真实数据时线宽只作强调，不标称带宽比例。

**状态：** 原创／改编绘图描述可用；未生成图片。新增官方来源仅核文本，不宣称已审其图面或已获用户视觉认可。
