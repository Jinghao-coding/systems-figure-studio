# 统一绘图知识与维护

## 1. 当前约定与入口

本技能统一维护全部主题画法、整图构造、工具和检索信息，唯一技能入口为 [SKILL.md](../SKILL.md)。各主题直接参与绘图流程，主题正文是画法维护源；catalog 中的维护元数据与生成结果分别如下。

画法源自用户提供的 research-diagram-components v0.4.1，其来源记录、许可信息及历史校验保留在 catalog。该名称只用于追溯来源，不是需要另行调用的技能或独立工作流。

Agent 样板与九种参考改编按当前图的用途选择。来源审阅、文字配方与具体成图的验收分别记录。

**主干：主题 → 词汇 → 多种具体绘图描述。** 图面中的外形、部件、位置和连接承担解释；短标签负责身份、术语和必要边界。一个对象允许多种构造，同一种语义也允许不同视角和展开程度。数量按实际可用方案决定。

## 2. 按需读取

日常绘图从 SKILL.md 的直接主题入口读取所需画法；术语不明确时用 [主题索引](topic-index.md) 或根目录 `catalog/index.json` 定位。

| 主题 | 文件 |
|---|---|
| Cloud、云原生、Kubernetes Logo 与连线组合 | [cloud-native-kubernetes](../topics/cloud-native-kubernetes.md) |
| 硬件、异构集群、加速器与互连 | [hardware-cluster](../topics/hardware-cluster.md) |
| 数据、内存、传输与存储 | [data-memory-storage](../topics/data-memory-storage.md) |
| 神经网络、张量、视觉、MoE、推荐与模型压缩 | [models-deep-learning](../topics/models-deep-learning.md) |
| 任务性能预测与代价模型 | [performance-prediction](../topics/performance-prediction.md) |
| 集群调度、配额、共享与回收 | [scheduling-resources](../topics/scheduling-resources.md) |
| 训练、微调、并行、通信与状态 | [training-distributed](../topics/training-distributed.md) |
| RL、采样、版本与对齐 | [rl-alignment](../topics/rl-alignment.md) |
| LLM 推理、实例、批次与缓存 | [inference-serving](../topics/inference-serving.md) |
| 系统软件、控制器、运行时与编译 | [systems-runtime](../topics/systems-runtime.md) |
| 可观测性、SLO 与可靠性 | [observability-reliability](../topics/observability-reliability.md) |
| Agent、多 Agent、工具与工作流 | [agents-workflows](../topics/agents-workflows.md) |

Agent 的细化内容在 [已保留样板](../topics/agents-approved-samples.md) 和 [arXiv 改编描述](../topics/agents-arxiv-patterns.md)。已有内容足够时直接使用；只有缺口、用户要求或技术边界不确定时才补查来源。

整图构造参考 [跨主题组合](../examples/combined-recipes.md)。审美和 icon 选择参考 [视觉规范](visual-quality.md)。扩充词条使用 [模板](../templates/term-card.md)。需要核验参考再读 [来源与取舍](sourcebook.md)。

## 3. 实际绘图流程

**理解内容。** 明确图的用途、目标读者和主要对象；可以用一句话描述读者需要理解的内容。小组件可只负责身份识别，不强制解释完整机制。

**调用画法。** 找到相应词条，按语义、目标尺寸与上下文选合适构造。可以将现有描述适当改编，也可以提出新候选。只需身份时，简洁图标加短标签即可；需要解释模型、数据、状态或资源时展开相应结构。

**组织整图。** 先安排主体、阅读方向、边界与关键关系，再统一图标家族、线条、字体层级、颜色角色和透视。数据、控制、引用、放置、依赖与反馈各按实际含义表达，不为了对称随意补边。

**输出。** 要文字就给描述或完整 prompt；要求实际图形时调用可用工具；需要可编辑文件时构造原生路径、形状与文字。没有生成图片时明确保留文字候选状态，不宣称视觉验收完成。

**交互。** 用户提出的最新偏好立即用于选择和修改。只有显著改变结果且上下文不能解决的问题才追问；已经认可的方向直接沿用。不得把一次认可泛化为所有图都必须使用同一构造。

## 4. Icon 与整体观感

允许符合主题的头像、设备、终端、文档、工具、状态标记和适量装饰。图标式、结构式、图标与结构组合式均可用，不给全库设统一的图标比例。

选择标准是：角色与架构逻辑一致，和整张图乃至同一文档的视觉语言协调，细节尺度合适，不挡连接或抢占主体。少量亲和性细节可以保留，不必强求每笔装饰都有数学语义。

“减少 AI 感”指减少实际可见的问题，例如不相关的发光、厚重塑料质感、随机渐变箭头、满屏同形 UI 卡片、不同风格图标混搭、浮空装饰和乱码标签。它不是对工具的限制，也不等于禁用颜色、深度、圆角或机器人。

矩阵、缓存页、时间段和资源槽位可自然使用方格；设备身份也可用小图标。所选形体应适合当前对象，不把所有对象替换为同一种文字方框，也不强制所有对象展开内部结构。

### Logo、云边界与连接的整体使用

允许必要的 Kubernetes、云平台或实际框架标识。先说明标识哪个对象，再安排到集群边界标题、软件平台层、接口或组件标题；Logo 与资源图标、设备结构配合，不把所有内部对象替换成同一项目标识。详细视图连具体接口，折叠概览可以连 Logo＋名称组成的整体端点。

已有集群、节点、GPU、存储和互连直接复用；相关入口见 [Cloud 组合主题](../topics/cloud-native-kubernetes.md)。CPU 使用独立词条，不照搬 GPU 或专用加速器结构。整体布局要同时安排资源归属、存储位置和连线路径，避免画完后再贴 Logo、强行穿线。

使用准确素材，按标题尺度、留白和同一文档风格协调；重复次数取决于阅读需要。素材无法准确提供给生图模型时留位后排，不能把生成的近似 Logo 称为官方标识。具体组合见 [Cloud 与 Logo 指南](cloud-logo-composition.md)。

## 5. 词条写什么

每种画法的主体是一段可直接绘制的描述：**轮廓与形体、可见部件、空间组织、连接、重点和视觉处理**。按需要写，不让每个简单组件都背负冗长规格。

涉及 Logo／图标时，把标识对象、附着位置、结构关系、连线路径与整体处理写入具体画法，不能只说“可以加一个 Logo”。

并附：词汇与别名、含义、适用条件、来源与具体取舍、关键误读提醒、描述／原图／成图各自状态。配色变体可保留，但不能用换颜色冒充新结构。

科学意义与画面构造不确定时要区分：可以提出原创构造；不能把没有依据的模块、精确数量、设备能力或算法步骤补进论文。品牌先按模型、运行时、接口、机构等角色定位，未知私有结构不展开。

## 6. 学习来源与审美筛选

顶会、期刊、arXiv 与作者博客用于寻找素材；论文热度和来源级别不替代看图与审美判断。先看准确版本的实际图面，再决定整体借鉴、仅取结构、仅取配色／构图或不采用。

对留下的局部，具体记录保留什么、舍弃什么、怎样重构。把论文逻辑和视觉处理分开：漂亮外观不能改变机制，正确机制也不要求照搬难看的配色。多个来源的小组件进入同一图时需要重新协调，而非直接拼贴。

三项状态独立：原图是否看过；选中了哪些局部；我们的新图是否生成并检查。继承审图记录、技术文本阅读、原创描述和已验图样例要清楚区分。链接存在不代表生图模型已看到图片。

## 7. Prompt 与图中可见文字

把本次内容、选中的画法、布局、关系、统一视觉处理融合为一个提示词。需要生成时列出允许的可见文字，内部组织标题、检查条款和元数据不自动出现在图中。语言按用户场景确定，不默认把中文交流全部转成中文图标签。

原图不可提供给工具时，使用已整理的具体描述并说明没有直接图像条件。需要数据结果时使用真实数据作图；生成模型可以探索机制插图，但不能伪造统计坐标、实验数值或输出证据。

## 8. 交付检查

对象身份与层级清楚，依赖和连线端点准确；模型层、通道、实例、分片、角色与设备不混同。完成请求、缓存保留、可驱逐与真正释放分开；单选放置只产生一个实际结果。

同时检查主次、形体、比例、留白、配色和整图兼容性。图标帮助识别或增加适量趣味，关键结构仍然可见。缩小到目标尺寸后检查文字、箭头和局部展开；结构校验通过不等于图面漂亮。

按当前请求交付：词条／提示词请求交付文字，实际绘图请求按统一绘图流程生成并检查图片，可编辑文件仅在请求时制作。未生成、未看过或未验证的内容如实标明。主题覆盖状态见 [coverage](coverage.md)。

## 9. 检索、离线浏览与维护

- 从 [主题索引](topic-index.md) 或 `catalog/index.json` 按词条 ID／别名定位，只读相关词条及必要边界；不用一次加载全部主题。
- [离线指南](../guide.html) 用于浏览、搜索和复制文字画法，页面统一检索词条、变体、Agent 扩展、案例与规则，并显示素材状态。修改主题后再重建快照。
- 组合样板仅提供可改编构图；目标论文决定真实对象、数量、部署和机制。将选定构造融合进最终提示词，记录词条 ID 与所选变体。
- 修改主题正文或来源后，在技能根目录运行 `python3 scripts/rebuild_navigation.py`，再运行 `python3 scripts/validate.py`。脚本仅做本地索引／指南生成及结构检查，不下载素材、不生成图片。
- 维护时区分新增和继承的来源状态，更新相应统计与版本记录。历史保护独立由 `check_history.py` 检查；未经明确授权不得修改受保护 Agent 正文或通过更新哈希绕过保护。新增关联元数据放在正文之外。


## 10. 数据职责与变体维护

| 责任 | 文件 | 维护方式 |
| --- | --- | --- |
| 画法正文与词条锚点 | `topics/*.md` | 唯一正文来源；保留旧词条 ID |
| 主题、别名来源、稳定变体身份 | `catalog/topics.json`、`catalog/term-provenance.json`、`catalog/variants.json` | 独立维护，不从旧生成结果继承 |
| 来源与历史保护 | `catalog/sources.json`、`catalog/history.json`、`catalog/migration.json`、`catalog/import.json`、`catalog/agent-preservation.json` | 保留继承版本、旧链接及授权依据 |
| 当前索引、统计、浏览器载荷 | `catalog/index.json`、`catalog/statistics.json`、`catalog/browser.json`、`guide.html` | 可移除后重建；不包含时间戳 |
| 制作及检查记录 | `examples/cases.json`、案例目录、`assets/visual-library/catalog.json` | 真实输入、产物、提示词与检查，独立于文字画法状态 |

变体的 `id` 是持久身份，首次迁移已登记，后续不得重算。`term_id` 和 `heading` 只定位现有 Markdown 段落；改标题时保留 `id` 并更新 selector。排序不改变 ID。新增变体用 `v-` 加唯一标识登记，不复制正文到 JSON。浏览器使用 `#topic=…&q=…&term=…&variant=…`，并兼容旧 `#term-<id>` / `#<id>`；现有 Markdown 词条锚点不变。

已有变体先标 `unreviewed`。有依据时补充 `suitable`、`unsuitable`、`level`、`connect`、`boundary_source` 和 `cases`；没有可靠信息就保留未审状态，不自动补全科学事实。三个场景涉及的变体已按场景输入补充选择条件，但场景不是完成案例。`scenario_inputs` 指向这些输入。

文字画法保持 `recipe_status=description_ready`。旧 `image_status=not_generated` 已从生成索引移除，其历史含义保存在 `catalog/history.json`。素材保留原始 `status` / `legacy_status`，另设 `generation_record`、`source_review`、`visual_review`、`final_use`、`user_acceptance`。只有 `final_use=eligible` 且没有 reference/truncated/superseded/error 历史限制的素材进入默认最终素材选择；其他资产继续可查阅。当前使用场景必须重新确认质量和接受状态。

浏览器通过 `scripts/web/guide.html`、`guide.css`、`guide.js` 生成，全部代码和数据嵌入页面。不要手改根目录 guide.html。Markdown 渲染是安全的小型子集：标题、列表、代码、表格与有效链接；原始 HTML 不执行。外部 URL 仅允许 HTTP(S)，本地相对路径保留。筛选和定位用 hash，不需要服务器路由。

`VERSION` 是独立技能发布版本；`catalog/source-version.txt` / import 是继承知识库版本。本次工作按 Unreleased 记录，不修改已有发布版本号。
