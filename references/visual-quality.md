# 视觉选择与取舍

## 选参考时

分别看形体、内部组织、比例留白、配色、连线和缩小后的辨识度。选择整体借鉴、只借结构、只借配色／构图或不采用，写明具体理由。不要只打分而没有可执行的取舍。

例如“保留错位薄片与局部展开；减薄轮廓；去掉大面积投影；把多套强调色统一到一组；重新安排图例”，比“高级、干净、顶会风格”更有用。

经典与近期论文都能提供方法。老图的配色不必保留，新图也不因视觉饱满就更合适。一张密集机制图可以只提取一个局部；不能提取时就不作为小组件范例。

## 使用 icon 时

可以使用角色头像、工具、文件、终端、设备、锁或状态提示。看它在当前画面中的作用：身份定位、辅助分组、提示操作，或适量亲和性装饰。它应与周围的线条、视角、颜色及细节一致。

只需识别角色时，头像＋短标签已经足够。需要解释执行或性能时，再组合状态、数据、时间轨道或资源剖面。装饰性帽子不承担全部角色含义，锁图标不代表已证明安全隔离。

不同主题无需都采用机器人；允许独立地选择半具象对象、纯结构或两者组合。跨图复用同一个角色、设备或模型时尽量延续其视觉身份。

## 降低生硬与过分 AI 感

观察成图，而不是只检查提示词中是否出现“不要 AI 感”。重点处理：

- 每个元素都被套进等大的圆角卡片，层级与对象失去差别。
- 随机发光、塑料或金属材质、厚投影、无关星星和漂浮图形争夺视觉重点。
- 一条彩虹粗箭头替代所有具体连接，端点、方向或含义不明确。
- 头像、芯片、纸页、张量来自不同画风，比例和透视没有协调。
- 模型自行加入“ZONE”“Input panel”等规划词，或文字拼写与原研究不符。

这些是需要判断的失败现象，不构成一律禁用阴影、渐变、圆角或 icon 的规则。克制的厚度、轻明暗和少量装饰可以保留，只要整体协调。

## 组件的形态与细节尺度

先判断读者在图中需要辨认的是板卡、芯片、节点、模型实例还是存储数据。构造同一对象时，先调整外轮廓与主要部件的比例，再决定颜色与细节：

- **GPU／加速卡**：小图标可用计算封装与存储件；较大图元可采用薄板卡、中央封装、两侧显存及局部金手指或安装挡片，形成清楚轮廓。主芯片不要成为没有身份的巨大空白框。散热器、风扇或外壳仅在符合所表示设备和整图风格时使用，不把消费卡外观默认套给全部加速器。
- **模型**：实例可用错位薄层配局部网络，结构图则按实际算子或层展开。层数和神经元示意数量不冒充真实规格；不让模型体与文件页束只有标签不同。
- **存储与状态**：权重文件、物理内存、逻辑KV页采用不同形体；页块的规则重复表达数据组织，文字说明其粒度。避免用几个空方块同时代表批次、显存容量、模型和配置。

轮廓、留白和部件间距比微小纹理优先。少量侧面、明暗和圆角可以使形体自然；缩小后消失或糊成噪声的针脚和纹理应删减。先查看代表组件在目标图中的实际比例，必要时比较两种构造，自行选出更适合的一种，再批量复用。

## 呆板图的重构顺序

先找出视觉焦点和阅读路径，再检查大框是否承担真实边界、说明文字是否挤占机制。对齐同类对象，同时允许主要对象与辅助对象有不同尺寸。留白用于分隔关系，不用冗余副标题填空。最后修订组件轮廓、连线与配色；无需给每张图加入新图标或立体效果。

单图放大检查负责发现端点、遮挡和细节问题，目标页宽预览负责判断整体观感与辨识度。若两者冲突，优先保住目标尺寸下的关系和主次。

## 颜色与排版

先让尺寸、留白、重复与连接形成层次，再通过颜色强调。颜色可表达类别、身份或状态，但一种局部颜色不要同时承担矛盾含义。量化色阶应有真实数据与图例。

同层级字体一致，标题、标签、辅助说明可有差异；不要把“统一”理解成所有元素同样大。没有固定的全局三色上限，也没有所有会议统一的配色模板。

## 成图检查

遮去大标题后仍应看见图中有角色、层次、分支、映射、资源或数据组织，不要求完全无文字猜出模型品牌。检查目标论文尺寸，不只看放大的原图。

具体成图才可被标为已验收。本库新增描述尚未生成图片；检索可用、链接完整、语义检查和审美验收分别记录。

<a id="aesthetic-review"></a>

## 配色后的整图审美复核

新图和配色修订完成后，模型必须打开实际导出图，判断整图是否协调、清楚、有吸引力，再决定是否需要修订。先看完整画面和目标版面宽度下的预览，再放大检查细节。只能读取源代码、颜色值或提示词时，将图面审美检查记为未验证。

先描述第一眼的视觉印象，并指出图面依据：视线首先落在哪里、画面偏拥挤还是松散、主体是否突出、颜色是否舒服而有对比。随后检查以下相互关联的因素：

| 观察维度 | 判断依据与可选修订 |
| --- | --- |
| 焦点与阅读顺序 | 最强对比是否落在要解释的对象或关系；边界、标题和 Logo 是否抢走注意力。调整局部面积、明暗或线宽。 |
| 色彩协调与视觉重量 | 浅、中、强色是否在实际面积和相邻背景上形成层次；同等重要对象是否意外失衡。可调明度、饱和度或色相，不必把整图一律调淡。 |
| 留白与构图平衡 | 组内和组间距离是否说明归属；两侧视觉重量、疏密节奏、留白是否自然。允许不对称，不以填满画布为目标。 |
| 形体与风格 | 轮廓、视角、图标、适度立体感是否协调，关键对象是否可辨；避免为了统一而抹掉对象差异。 |
| 文字与连接 | 字体层次、标签位置和线宽是否协调；折线绕行、交叉、贴边或穿字是否打断阅读。 |
| 缩小后的整体观感 | 目标宽度下是否仍有清楚的主体、流向和标签；细节是否挤成噪声，浅色小对象是否消失。 |

将主要发现简短记为“可见位置／现象 → 对阅读或观感的影响 → 实际修改 → 复看结果”，并保存对应预览路径。例：“右侧大面积深紫边界比调度器更醒目 → 焦点偏移 → 减弱边界填充，保留调度器颜色 → 重新导出查看”；这是记录示例，不是已执行历史。允许“整体协调，无需修改”，但应指出真实图面上的理由，不能只写“高级、专业、美观”。

修订优先解决最影响整体的已观察问题；改完重新导出并查看整图。局部任务仅修改授权范围，范围外问题记录为建议。拿不准两种配色时，可在同一布局、同一尺寸比较候选；不默认额外调用收费生图。没有新的具体问题时结束，不设固定审美分数、色数、面积比例或反复打磨轮数。灰度、色觉模拟和对比度检查可提供辨识证据，不能单独代表整图美感或机制正确。

方法依据：[Nature Methods 的层次、留白与显著性概述](sourcebook.md#pa05)、[Datawrapper 的明度和饱和度调整](sourcebook.md#pa02)、[Viz Palette 作者的分组与视觉重量修订](sourcebook.md#pa06)。开源方法参考：[SciencePlots](sourcebook.md#pa07) 提供字体、尺寸、线条和颜色循环的协调实践；[Penrose](sourcebook.md#pa08) 将关系与布局约束分别表达。按任务借鉴，不把工具默认样式当作审美验收。

## Cloud、平台 Logo 与连接

云轮廓、平台标识、资源类型图标与 CPU/GPU/存储形体可共存；统一视觉尺度、视角、留白与颜色角色，保留各自辨识度。标签、边界、数据流、物理链路和部署映射要一起布局。详见 [Cloud 与 Logo 组合](cloud-logo-composition.md)。

## 表达收益与视觉基线

图形选择以读者获得的信息为依据。对资源竞争，可比较设备上的占用叠加与执行时间线；对状态演化，可比较固定布局的前后快照与生命周期路径。采用哪一种取决于正文要解释的关系，不预设每张图都需要对照面板。多个视图同时保留时，各自应解决不同的理解问题。

叠加视图应有共同参照：例如在同一设备上标出驻留模型与候选请求，候选用浅色或虚线，已选对象用较清晰轮廓；不要让浅色被误解为低性能。数据图中，散点、区间带和拟合线分别需要相应观测、统计定义和模型依据，不能把这些效果当作装饰套进机制图。

修图前从现有图面辨认值得保留的设计，再修改导致误读或不协调的部分。图形层次不应在重新编码、导出矢量或改配色时丢失；若原结构需要重构，按新的表达任务安排。记录具体保留/改变的元素即可，不增加固定评分、表单或用户确认。

每轮查看完整图面，集中修复已发现的问题。完成图内检查后再查看文稿中的字号和落页；若问题只在图题或浮动位置，修改排版而非重画组件。检查已通过的部分仅在输入或设计变化时重检，避免无新问题的反复打磨。


## 从图例迁移到当前图

参考 figures4papers 的实际图面时，可拆成三个可操作选择：用对象形态区分输入和处理；用同族浅色维持关系、局部深色建立焦点；用主流程与局部展开分配视觉空间。分别决定是否适合当前图，不把完整的生物结构、球面、问答框或大幅横版直接迁入系统论文。

迁移后检查：遮去颜色还能否辨认对象？缩到论文宽度，局部展开是否仍可读？同一个颜色跨面板是否仍指同一对象？是否由于加粗轮廓、放大标题或装饰渐变压住了机制？选择的配色与构图见 [视觉规范](visual-system.md) 和 [图形组织](figure-grammars.md)，来源及已看的图例见 [阅读记录](figures4papers-ideas.md)。

## 造型选择要改变实际画面

对新图的主要视觉对象，或用户明确指出呆板的对象，比较有实质差异的候选：轮廓、视角、部件组织、局部展开和与邻近对象的关系。选出适合解释任务的构造再展开；已认可的局部修图无需重新选型。让创造性发生在这些选择中，例如实体与状态叠加、主体与爆炸展开、流动序列与固定资源的配合，而不靠随机添加装饰。不要把易于编码或库中排在最前面当作选择依据。

GPU 的选择可以是：以薄板卡侧面、安装端和封装比例辨认设备；以错位计算面与存储面解释搬移；以小型设备身份配外置时间轨道解释共享；或按有依据的微架构展开计算阵列。通用“大矩形＋小方块＋GPU 标签”只有在那些小块确实表达本文关心的资源单元时才有解释价值。图要表现设备身份而不是单元分配时，应选择更有辨识度的轮廓；无需给每张图都添加风扇、针脚或同一种 PCB。

整图的变化来自主次比例、形体差异、疏密节奏、适当的展开视角和协调色族。颜色可以丰富，层次也可以鲜明；不把“论文风格”解释为所有对象低饱和、相同浅填充和同粗黑框。先给主对象与辅助对象不同的视觉重量，再在目标尺寸检查是否形成焦点。

对照绘制前展示的设计检查实际结果：承诺的轮廓和局部展开在哪里，颜色角色是否实现，关键关系是否一眼可读？如果输出仍退化成一排同形文字框，记录为本轮视觉设计未实现，并针对构造或布局重绘。不要用“语义正确”替代视觉通过，也不因单次失败增加无关的细节规则。


## Component selection and production detail

### Make selected recipes visible

For each object needing concrete representation, determine: **object and role → entry and variant → silhouette, parts and spatial organization → labels and connection endpoints**. Before drawing, briefly show the user the key choices and resulting visible forms. Code comments or private notes do not replace this disclosure. The actual figure must show the selected parts and relationships; a delivery statement claiming that the library was used is insufficient.

For example, a training overview can combine the network skeleton in `network-model` with the forward/backward paths in `training`. An inference model can use the layered body in `model-instance`, a `token` sequence and `kv-cache` state strips. For a GPU, choose board identity, an exploded package or compute structure from `accelerator` according to its role, rather than always using the same board construction. Use `kubernetes-platform-logo` for platform-title ownership. The manuscript determines the actual structure; the existence of a recipe does not justify adding a model, platform or deployment.

When identity alone matters, an icon and short label can form a complete component. When explaining a mechanism, expose the relevant local network, state, data or resources. Allow structural drawings, icons and combinations, including coordinated avatars, modest decoration, subtle depth and approachable details where useful. Balance identity, structural explanation and the whole composition. Avoid reducing every object to a named box or requiring complex internals in every small icon.

**Fix structural problems through structural changes.** If the user finds objects abstract, shapes repetitive or the library unused, reselect and develop the relevant components. Recoloring, retitling or adding icons to otherwise identical boxes does not complete that redraw.

See the [visual asset library](visual-asset-library.md) for actual images and reusable forms. Accumulate useful objects as needed, distinguishing accepted references from cleaned assets; inspect leftover text, cropped edges and arrows before reuse. Figures may use GPT Image for the whole image, mixed assets or native primitives as appropriate. Editability is not required for every figure by default.

### Choose assets to fit the figure

The repository's visual assets are optional starting points and examples, not prescribed appearances. Depending on the manuscript's meaning, visual style, scale and composition, reuse a suitable asset, adapt one, generate a new element with an available image tool, or use native primitives. New generation is a normal design choice even when a related asset exists; there is no requirement to search or exhaust the library first. Briefly explain the selected approach when presenting the design.

For revisions or related figure sets, respect any explicit request to preserve an accepted identity or style. Prior acceptance in another figure or project does not make that asset mandatory. Keep repeated objects visually consistent within the current composition without fixing every person, Agent, model or environment to one repository image.

Give each object a form suited to what it explains. A tool workspace might use a terminal, files or network endpoint where relevant, but this is one possible construction rather than a required component list. Simple shapes are appropriate when they clearly express topology, state or timing. Check reused or generated elements for semantic fit, readability and composition quality. For transparent assets, inspect the actual alpha composition on the intended background. See [asset selection](visual-asset-library.md#asset-selection).

## Keep PowerPoint output easy to edit

Follow the small-object workflow in [editable production](editable-production.md): retain the few parts that need independent editing and use coherent images for complex artwork. That file maintains the full PPT/WPS granularity rule.

## Generate new local elements when needed

The knowledge base is an adaptable starting point, not a closed catalog. When no construction fits, or existing constructions look monotonous or inconsistent in the current composition, use GPT Image or the available image generator to design local elements for the figure. This applies to GPUs, CPUs, models, storage, nodes, Agents, tools, data objects and any other object requiring a custom form. Do not wait for the user to request every element or exhaust all entries first. Use capabilities actually exposed by the tool; writing a model name in a prompt does not select that model.

Choose whole-image generation, separately generated elements followed by composition, or a representative component extended to the figure set according to the task. Before generating an element, show its purpose, design and complete prompt. Then display and inspect the result inline, and supply selected elements as actual image inputs or assets when composing the figure. Mentioning a filename in a prompt does not reuse its image. Coordinate color, perspective, silhouette, lighting and detail density at the final figure scale; reuse an element to preserve object identity.

Standalone elements for composition usually need transparent backgrounds, complete contours and clear space for connections. Set the actual transparency parameter when supported. Keep variable labels, counts, states and arrows in the composition layer where possible instead of baking them into pixels. Generated constructions do not constitute real product photographs, official logos, precise microarchitectures or experimental results. See [element generation](generation-prompts.md) for prompts and checks.

Generated elements may be imported directly into draw.io or PowerPoint as separate image objects alongside native text, shapes, connectors and groups. This is a normal production path and requires no additional permission to mix assets. Each element can be moved, resized, replaced and grouped independently; text, arrows, state markers and layout remain separately editable. Rebuild internal geometry from the generated reference only when the user explicitly requires full vector output or editing of individual internal parts. Explain that image interiors remain pixels without treating every editable draw.io/PPT request as a requirement to reconstruct all elements as vectors. Do not flatten the entire figure into one image. Retain useful project assets and actual prompts without turning every candidate into a global entry or creating duplicate backups.

## Develop recipes into visual designs

Recipes provide alternative constructions, not fixed icon templates. For new figures, substantial redraws or feedback that a figure looks stiff or unattractive, first read [visual choices and trade-offs](visual-quality.md), then choose key objects' **silhouettes, proportions, part relationships and detail scale**. Draw on user references or library examples that have actually been inspected. Design missing forms yourself without claiming unseen sources as visual evidence.

When the user requests inspiration from research figures, search for and inspect actual figures from leading AI or systems conferences relevant to the current objects, preferring official publications or author manuscripts. Extract silhouettes, parts, grouping, connections and color roles. Update existing entries and source records using “source and figure number → retained elements → omitted content → applicable objects.” Do not merely add paper links or assume that a conference's reputation makes an entire figure worth copying.

Produce an actual preview of a key object and one representative relationship, inspect it at reduced size, then extend the design to the figure set. Show the representative preview to the user and state the adopted form. Continue authorized drawing without turning this disclosure into another approval gate. GPUs, models and storage should have recognizable features at their intended size. Adding an icon or including recipe parts does not by itself establish visual quality. Small objects may be simple; large objects should avoid empty placeholders. Precision comes from object relationships, not accumulated pins, screws or shadows.

Choose paths, lanes, local expansions or state comparisons according to the reading relationships. Reuse shapes for objects of the same kind and frames for real ownership. Do not force every object into an identical card for symmetry. Revisions addressing stiffness must examine both component forms and the whole figure's emphasis, density and spacing, beyond colors, rounded corners or thickness. Assess technical correctness and visual quality separately; more detail is not automatically more attractive.
