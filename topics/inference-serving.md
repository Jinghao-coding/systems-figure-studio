# LLM 推理与服务

请求输入、已提交输出、候选 token、KV 与权重有不同身份。先确定实例与阶段归属，再选择图形。

本主题包含 **14 个词条**。正文是可执行的绘图描述，不是已生成组件。来源已审与改编已验图是两个独立状态。统一配色、icon 与整体审美规则见 [视觉规范](../references/visual-quality.md)。

## 词条索引

[模型身份与实例](#model-instance) · [请求](#request) · [批处理与运行集合](#batch) · [Token 与生成候选](#token) · [Prefill / Decode](#prefill-decode) · [KV Cache 与前缀共享](#kv-cache) · [模型加载与驻留](#model-loading) · [Prefill／Decode 分离与 KV 交接](#pd-handoff) · [分块 Prefill 与连续批次](#chunked-prefill) · [投机生成、验证与回退](#speculative-verification) · [前缀共享、引用与驱逐](#prefix-cache-lifecycle) · [多模型与多 LoRA 服务](#multi-model-lora-serving) · [专家驻留、缓存与搬移](#expert-residency) · [推理资源预算与准入](#inference-budget)

<a id="model-instance"></a>

## 模型身份与实例

**词条 ID：** `model-instance`  
**词汇与别名：** LLM、VLM、model instance、replica、shard、Qwen、千问、DeepSeek、Llama、Gemma、Mistral、GPT  
**含义：** 模型类型、完整实例、分片与物理部署的关系。

### 有层次的独立模型体

每个实例用重复层轮廓或薄片骨架表示，前景有一个展开层；每个实例有独立ID，模型类型标签与ID分开。

### 参数平面和实例外壳

实例边界中以窄权重面和一条执行路径表达驻留模型；复制实例时复制完整对象，不只复制标签。

### 有归属的分片集合

一个模型的多个切片分布在不同rank，虚括号或共享模型ID连接它们；不把每片画成完整模型。

**参考与取舍：** [R07](../references/sourcebook.md#r07)、[R24](../references/sourcebook.md#r24)。重复层与分片分别是局部形体参考；实例数量、类型与实际部署独立确认。

**必要边界：** 层、完整副本、参数分片、版本四种身份不能混淆。

**状态：** 绘图描述可用；改编示例图未生成。具体构图、数量与外观按本次研究内容核对。

<a id="request"></a>

## 请求

**词条 ID：** `request`  
**词汇与别名：** request、请求、prompt、endpoint、query、tokenization  
**含义：** 一次提交及其输入、约束和生成状态。

### 带实际 token 内容的请求行

ID旁展示短token序列，输入与输出分段，焦点请求局部展开；不用相同大小空卡片替代所有请求。

### 有长度轮廓的请求条

多个请求共享起点但长度不同，末端只突出本轮token；外侧请求身份不随排序而改变。

### 字段页与 token 带并置

前面一张请求页显示两三项约束，侧面短token带显示上下文内容；数据与约束不塞进一行标签。

**参考与取舍：** [R21](../references/sourcebook.md#r21)、[R06](../references/sourcebook.md#r06)、[R10](../references/sourcebook.md#r10)。借鉴所列来源的局部形体或组织关系；各候选是改编描述，不表示每种画法都直接出现在原图。

**必要边界：** 长度编码须说明代表token数或时间；待进入批次的请求在边界外。

**状态：** 绘图描述可用；改编示例图未生成。具体构图、数量与外观按本次研究内容核对。

<a id="batch"></a>

## 批处理与运行集合

**词条 ID：** `batch`  
**词汇与别名：** batching、continuous batching、dynamic batching、请求池、waiting、running、并发请求  
**含义：** 一个时刻共同执行的请求或样本集合。

### 请求序列的成组切片

多个长短序列组成batch包络，保留每行ID与分段；没有顺序承诺时不用队首箭头。

### 一次迭代的token截面

从多条请求上同时抽取本轮输入token组成紧凑截面；前后请求仍可追踪。

### 随迭代变化的集合

三个时刻使用相同请求条布局，已完成退出，新请求进入，持续请求保持身份；不要画静态固定batch。

**参考与取舍：** [R21](../references/sourcebook.md#r21)、[R10](../references/sourcebook.md#r10)、[R25](../references/sourcebook.md#r25)。借鉴所列来源的局部形体或组织关系；各候选是改编描述，不表示每种画法都直接出现在原图。

**必要边界：** 输入序列、运行集合、本轮token矩阵是不同对象。

**状态：** 绘图描述可用；改编示例图未生成。具体构图、数量与外观按本次研究内容核对。

<a id="token"></a>

## Token 与生成候选

**词条 ID：** `token`  
**词汇与别名：** token、prompt、decode、sampling、EOS、speculative、token tree、accepted、rejected  
**含义：** 序列元素、嵌入和候选生成路径。

### 序列片与向量对照

上方token小片，下方对应窄embedding向量；两层各自数量含义清楚。

### 候选分支树

公共前缀作主干，候选token沿不同枝出现，最终路径突出，未选分支保留为候选而非已生成输出。

**参考与取舍：** [R06](../references/sourcebook.md#r06)、[R14](../references/sourcebook.md#r14)、[R23](../references/sourcebook.md#r23)。借鉴所列来源的局部形体或组织关系；各候选是改编描述，不表示每种画法都直接出现在原图。

**必要边界：** token节点不等于整请求；候选集合不等于已接受序列。

**状态：** 绘图描述可用；改编示例图未生成。具体构图、数量与外观按本次研究内容核对。

<a id="prefill-decode"></a>

## Prefill / Decode

**词条 ID：** `prefill-decode`  
**词汇与别名：** prefill、decode、chunked prefill、PD分离、vLLM、SGLang、TensorRT-LLM  
**含义：** 输入处理与后续生成阶段。

### 长阶段与短迭代节奏

prefill用一段长区间，decode用重复短片；chunked模式把同一prefill拆成带关联ID的片段。

### token处理截面对比

prefill侧一次展示一组输入token，decode侧突出当前token并引用已存KV；不同阶段数据形状直接可见。

**参考与取舍：** [R25](../references/sourcebook.md#r25)、[R21](../references/sourcebook.md#r21)。借鉴所列来源的局部形体或组织关系；各候选是改编描述，不表示每种画法都直接出现在原图。

**必要边界：** 长短只作示意，不能当实测；P/D分离需另给部署边界。

**状态：** 绘图描述可用；改编示例图未生成。具体构图、数量与外观按本次研究内容核对。

<a id="kv-cache"></a>

## KV Cache 与前缀共享

**词条 ID：** `kv-cache`  
**词汇与别名：** KV Cache、block table、逻辑块、物理块、prefix cache、radix tree、引用计数、eviction  
**含义：** 请求关联的 KV 数据、映射和前缀共享。

### 页块映射

逻辑连续token页通过记录连接到不连续物理块；焦点页展开四五个槽位，空槽可见。

### 公共前缀树

共享段只出现一次，分叉后各有自己的后缀；前缀树和物理缓存可以用引用线关联。

### 长缓存条与新增切片

缓存随decode增长，已有段不动，只有右端新增，必要时另分配物理块；同对象连续出现。

**参考与取舍：** [R22](../references/sourcebook.md#r22)、[R23](../references/sourcebook.md#r23)、[R19](../references/sourcebook.md#r19)。借鉴所列来源的局部形体或组织关系；各候选是改编描述，不表示每种画法都直接出现在原图。

**必要边界：** 完成、无引用、可驱逐、物理释放分别画；共享不等于复制。

**状态：** 绘图描述可用；改编示例图未生成。具体构图、数量与外观按本次研究内容核对。

<a id="model-loading"></a>

## 模型加载与驻留

**词条 ID：** `model-loading`  
**词汇与别名：** cold start、warmup、resident、offloading、preload、模型加载、卸载、实例复用  
**含义：** 权重加载、驻留与执行可用状态。

### 权重切片穿越存储层

同一模型的参数切片从源存储面穿过传输路径进入实例；已加载与待加载区段可分辨。

### 加载与执行的交叠视图

上层按层展示权重片就绪，下层执行相应层；同一layer编号保持，空隙只在实际等待处出现。

**参考与取舍：** [R07](../references/sourcebook.md#r07)、[R22](../references/sourcebook.md#r22)、[R28](../references/sourcebook.md#r28)。借鉴所列来源的局部形体或组织关系；各候选是改编描述，不表示每种画法都直接出现在原图。

**必要边界：** 传输、反序列化、初始化和执行不能并成一个“Loading”框。

**状态：** 绘图描述可用；改编示例图未生成。具体构图、数量与外观按本次研究内容核对。

<a id="pd-handoff"></a>

## Prefill／Decode 分离与 KV 交接

**词条 ID：** `pd-handoff`  
**词汇与别名：** PD disaggregation、prefill、decode、KV transfer、DistServe  
**含义：** 请求在两类实例之间推进以及中间状态传输。

### 双实例群与可追踪交接

Prefill 与 Decode 各有独立实例组，用少量错位模型层和设备小轮廓表现组内结构。焦点请求沿上方进入 Prefill，生成的 KV 片束经过传输区接到 Decode，输出 token 从另一侧连续展开。

### 请求主线与数据传输双轨

请求控制路径与 KV 搬移路径平行排列，保留同一请求 ID；Decode 开始的依赖连到 KV 可用点。只展开一次交接，其他实例折叠在组边界后。

**参考与取舍：** [S10](../references/sourcebook.md#s10)。保留分阶段实例与显式 KV 桥；原图方框密集，仅作分层关系参考，外形另行设计。

**必要边界：** 实例不一定等于一张 GPU；控制消息、KV 数据和权重是不同对象，传输方向按实现确定。

**状态：** 绘图描述可用；改编示例图未生成。具体构图、数量与外观按本次研究内容核对。

<a id="chunked-prefill"></a>

## 分块 Prefill 与连续批次

**词条 ID：** `chunked-prefill`  
**词汇与别名：** chunked prefill、continuous batching、decode priority、token budget  
**含义：** 长 prompt 分块与持续 decode 请求的迭代组织。

### 长输入带切段并穿插

一个 prompt 长带分成带序号的块，每轮 batch 收入下一块及已有 decode token。相同请求持续保留 ID，完成请求在下一轮退出，新请求在真实准入点加入。

### 容量框与迭代列

每个迭代用同尺度预算区表示，内部按实际 token 或计算预算装入块；prefill 块与单步 decode 采用不同长度形体。若宽度表示 token 数，不能同时当作执行时间。

**参考与取舍：** [R21](../references/sourcebook.md#r21)、[R25](../references/sourcebook.md#r25)。借鉴请求行和长短计算节奏，按本次 token／时间轴的定义重构。

**必要边界：** batch 大小、token 数与时延不是同一尺度；分块顺序和 decode 连续性由策略决定。

**状态：** 绘图描述可用；改编示例图未生成。具体构图、数量与外观按本次研究内容核对。

<a id="speculative-verification"></a>

## 投机生成、验证与回退

**词条 ID：** `speculative-verification`  
**词汇与别名：** speculative decoding、target、draft、accept reject、token tree  
**含义：** 候选 token 的提出、验证与最终提交。

### 独立双模型与候选树

Draft 和 Target 使用同一风格的两组独立模型层，分别标角色和实例。Draft 输出小型 token 树，共同前缀只画一次，Target 的验证结果突出接受路径，其他分支保留淡轮廓。

### 候选序列与提交边界

上下对齐候选 token 和已提交 token，验证点之后只保留实际接受部分；拒绝处标清后续重新采样或回退的起点。省略复杂分支时仍保留目标验证者，不仅画一条加速箭头。

**参考与取舍：** 尚无专门原图。原创或通用构造候选；没有已绑定的专门原图。

**必要边界：** 不是所有投机方案都有独立 Draft 模型；拒绝后的 KV 和 token 处理按算法，不能随意接受候选。

**状态：** 绘图描述可用；改编示例图未生成。具体构图、数量与外观按本次研究内容核对。

<a id="prefix-cache-lifecycle"></a>

## 前缀共享、引用与驱逐

**词条 ID：** `prefix-cache-lifecycle`  
**词汇与别名：** prefix cache、radix tree、refcount、cache eviction、SGLang、KV reuse  
**含义：** 公共前缀对象、使用者和回收条件。

### 共享树干与引用端点

公共前缀形成一段连续树干，各请求从分叉处延伸；物理缓存块只画一份，由多个请求引用。引用计数作为小角标，焦点分支局部展开到 KV 页，避免把树节点全画成模型。

### 访问—释放引用—回收快照

相同树位置在三个时刻保持，访问改变活跃标记，请求结束减少引用；仍缓存的节点保留，真正驱逐才从映射中移除。被其他请求使用的公共祖先不能无条件一起删除。

**参考与取舍：** [R23](../references/sourcebook.md#r23)、[S09](../references/sourcebook.md#s09)。共享前缀树形体参考 R23；S09 仅支持完成与物理回收分离的边界，不是前缀树来源。

**必要边界：** 引用为零不必立即回收；缓存驻留状态与分配器空闲状态分别表示。

**状态：** 绘图描述可用；改编示例图未生成。具体构图、数量与外观按本次研究内容核对。

<a id="multi-model-lora-serving"></a>

## 多模型与多 LoRA 服务

**词条 ID：** `multi-model-lora-serving`  
**词汇与别名：** multi model、multi LoRA、adapter serving、model switch、base weights  
**含义：** 基础权重、适配器与请求路由的共享关系。

### 共享主干与适配片

基础模型只有一份主干，多个带身份的适配片排列在侧面；请求根据指定 adapter 接到相应旁路。只展开一个适配器如何作用于层，其他保持窄片，避免把每个适配器都画成完整模型。

### 驻留架与加载窗口

已驻留的基础模型与 adapter 保留在设备附近，未驻留者在远端页束；切换时画真实加载或缓存命中路径。请求队列和加载队列分开，避免把已选模型当作立即可运行。

**参考与取舍：** [R01](../references/sourcebook.md#r01)。所列来源仅为相关机制或局部组织依据，具体画面由本条重新构造。

**必要边界：** 共享程度与合批能力依框架；不同基础模型不能自动共享全部参数。

**状态：** 绘图描述可用；改编示例图未生成。具体构图、数量与外观按本次研究内容核对。

<a id="expert-residency"></a>

## 专家驻留、缓存与搬移

**词条 ID：** `expert-residency`  
**词汇与别名：** MoE inference、expert offload、expert residency、expert cache  
**含义：** 被选专家与内存驻留状态的对应。

### 专家目录与驻留槽

上方是专家身份目录，下方 GPU 驻留槽显示当前权重片，未驻留专家在主存；token 路由首先选专家，再检查是否可执行。未命中者经过搬移路径而非直接出结果。

### 路由热区与局部迁移

专家选择矩阵旁展开一个频繁使用专家的权重迁移过程，其他专家保留简化状态。热区强度只有真实统计才量化，否则用“示意”与少量标记表达。

**参考与取舍：** 尚无专门原图。原创或通用构造候选；没有已绑定的专门原图。

**必要边界：** 专家被选中不等于权重驻留；路由改变、专家迁移与参数分片是不同机制。

**状态：** 绘图描述可用；改编示例图未生成。具体构图、数量与外观按本次研究内容核对。

<a id="inference-budget"></a>

## 推理资源预算与准入

**词条 ID：** `inference-budget`  
**词汇与别名：** KV budget、token budget、batch budget、memory admission、OOM  
**含义：** 请求集合在计算与存储约束下进入执行。

### 双预算尺与请求小格

当前请求集合旁分开画 token 预算和 KV 容量尺，新请求使用描边小格放在集合外；检查通过后才进入 batch。保留已有占用与候选增量，不能用同一颜色掩盖变化。

### 增长轨道与提前回收点

KV 占用沿迭代逐步增长，上限为固定参考线；在触发点明确暂停准入、驱逐或预占等实际动作。没有预测长度时，不画所有请求未来占用都已准确可知。

**参考与取舍：** [S09](../references/sourcebook.md#s09)、[S10](../references/sourcebook.md#s10)。所列来源仅为相关机制或局部组织依据，具体画面由本条重新构造。

**必要边界：** 计算预算与内存预算不同；最大输出长度、当前长度和实际完成长度分别处理。

**状态：** 绘图描述可用；改编示例图未生成。具体构图、数量与外观按本次研究内容核对。
