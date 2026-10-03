# 继承的 Agent 原图学习记录

本文件主体继承自 v0.3.1；本轮保留内容，不把它计入新增审图。当前统一规则见 [技能规范](../SKILL.md) 与 [知识维护说明](knowledge-base.md)。源包记录用户已认可 Agent 词条整理方向，原图或改编图的具体审美状态仍按记录分别理解。

# Agent / Multi-agent arXiv 图例审阅

审阅日期：2026-10-01。8 篇论文，9 张指定图（AutoGen 2 张）。以实际取得版本为准。来源已审图与我们改编图已验收是两回事；下列审美取舍为既有记录；用户现已认可 Agent 部分的整理方向，具体新图仍需检查。

只学习小组件构造，不以 arXiv 上架或会议名称作为质量保证。原图未打包，也未授予再发布权；学习时回到原文查看，改编时保持来源记录。

## AG01 · AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation

版本：`2308.08155v2`，2023-10-03；Fig. 1; Fig. 3；PDF 页：1,6。
来源：https://arxiv.org/pdf/2308.08155v2
读图方式：web PDF screenshots, pp. 1 and 6

**实际画法：** 小机器人头像配能力徽标；通过同族对象的连线形成联合对话、层级协作与动态群聊。对话内容使用气泡，角色身份与消息形态分开。
**保留：** 角色头像＋能力条；对话气泡；同一套图元复用于不同协作拓扑。
**修改或舍弃：** 减少灰底大容器和高密度小图标。能力徽标可改成通用短标签，不照搬品牌。
**取舍：** 借鉴角色构造与拓扑，重新处理比例和底色。

## AG02 · GPTSwarm: Language Agents as Optimizable Graphs

版本：`2402.16823v3`，2024-08-22；Fig. 1；PDF 页：2。
来源：https://arxiv.org/pdf/2402.16823v3
读图方式：web PDF screenshot, p. 2

**实际画法：** 用不同形状的操作节点组成单个 Agent 的局部图，再将各 Agent 小图连接为群体网络；角落的角色形象标记 Agent 身份。
**保留：** 操作—局部图—群体图的尺度层次；局部展开；跨 Agent 的通信边。
**修改或舍弃：** 去掉贯穿画面的彩虹渐变、棋盘纹理、冗余 Logo、厚阴影；不要把饱满装饰当成结构。
**取舍：** 只借结构，不收为整图审美模板。

## AG03 · Magentic-One: A Generalist Multi-Agent System for Solving Complex Tasks

版本：`2411.04468v1`，2024-11-07；Fig. 1；PDF 页：1。
来源：https://arxiv.org/pdf/2411.04468v1
读图方式：web PDF screenshot, p. 1

**实际画法：** 角色用文件、代码、终端、浏览器等小符号识别；编号执行步骤下摆放相应代码、浏览器或终端产物。
**保留：** 角色图标＋实际产物；步骤编号；同一角色在多个时刻重复出现。
**修改或舍弃：** 压缩截图文字，简化长距离虚线路径；不能把步骤重复误画成新增 Agent。
**取舍：** 借鉴工具产物型画法，不照搬全部截图及原配色。

## AG04 · AFlow: Automating Agentic Workflow Generation

版本：`2410.10762v4`，2025-04-15；Fig. 2；PDF 页：4。
来源：https://arxiv.org/pdf/2410.10762v4
读图方式：web PDF screenshot of current canonical PDF, verified as v4, p. 4

**实际画法：** 圆节点及颜色区分操作；扇入结构表现 ensemble，局部反馈与条件节点表现 debate 和 self-refine；另列节点配置与代码/图等关系表示。
**保留：** 可复用小拓扑：生成—评审—修改回路、并行候选—汇总、带历史状态的局部交互。
**修改或舍弃：** 降低粗边框和投影，少用多层虚线卡片。节点不自动等于独立 Agent 或模型实例。
**取舍：** 借鉴局部操作拓扑，重做外观。

## AG05 · Agent Lightning: Train ANY AI Agents with Reinforcement Learning

版本：`2508.03680v1`，2025-08-05；Fig. 1；PDF 页：2。
来源：https://arxiv.org/pdf/2508.03680v1
读图方式：web PDF screenshot, p. 2

**实际画法：** 左侧是 Agent、工具和小网络；上方弧线把训练轨迹送向训练引擎，下方反向弧线返回更新模型。
**保留：** 执行侧与训练侧分开；轨迹与模型更新两种返回路径。
**修改或舍弃：** 不继承中心 Logo 的较大视觉占比；训练器可按需要局部展开，而非所有图都保留空框。
**取舍：** 借鉴双向闭环与执行/训练分离。

## AG06 · AgentOrchestra: Orchestrating Multi-Agent Intelligence with the Tool-Environment-Agent (TEA) Protocol

版本：`2506.12508v6`，2026-05-28；Fig. 2；PDF 页：HTML图，未核PDF页码。
来源：https://arxiv.org/html/2506.12508v6
读图方式：opened primary arXiv HTML figure image

**实际画法：** 同风格动物头像配角色名；上方主规划器有局部展开，右上是紧凑层级角色图；下方依次放置专用子 Agent、工具、环境和管理组件。
**保留：** 统一角色图标家族；角色总览与局部展开；角色—工具的明确归属。
**修改或舍弃：** 不要搬入整页协议栈和密集图标；只取当前系统有关的局部，角色图标保持相同尺度。
**取舍：** 借鉴角色组合与层级布局，内容取舍后使用。

## AG07 · The OpenHands Software Agent SDK: A Composable and Extensible Foundation for Production Agents

版本：`2511.03690v2`，2026-04-22；Fig. 1；PDF 页：2。
来源：https://arxiv.org/pdf/2511.03690v2
读图方式：web PDF screenshot, p. 2

**实际画法：** 左右比较 V0 与 V1；多层组件边界和命名连接表达应用、SDK、workspace、tools 与 server 的依赖及运行边界，主体依然是文字矩形。
**保留：** 相同颜色追踪重构前后相对应的模块；边界和依赖关系。
**修改或舍弃：** 不能作为形体多样性范例；应由我们的词条补充进程、事件、工作区和执行产物等具体对象。
**取舍：** 只作系统软件语义及重构对照参考，不作审美模板。

## AG08 · Orchestra-o1: Omnimodal Agent Orchestration

版本：`2606.13707v1`，2026-06-10；Fig. 2；PDF 页：HTML图，未核PDF页码。
来源：https://arxiv.org/html/2606.13707v1
读图方式：opened primary arXiv HTML figure image

**实际画法：** 文件图标区分模态，主 Agent 与多个子 Agent 组合，任务依赖与并行执行局部展开；同时存在大面积金属机器人、厚阴影、多种图标及字体处理。
**保留：** 按模态呈现输入；主/子 Agent 与任务依赖对照；实际等待关系。
**修改或舍弃：** 不继承金属机器人、厚阴影和图标风格混杂。不要原样复用价格数字。
**取舍：** 不入整图审美模板；保留机制参考与反例记录。

## 暂不作为已审图证据

- MetaGPT: Meta Programming for a Multi-Agent Collaborative Framework (`2308.00352v6`)：读到 Fig.2 对共享消息池/订阅/执行反馈的说明；原图未取得，不宣称其图形外观已审。 来源：https://arxiv.org/html/2308.00352v6
- Agent Lightning v1.0: Towards Harnessed Agentic RL (`2608.17528`)：检索到2026-08条目；本轮未取得正文图，不借用旧论文图冒充新版。 来源：https://arxiv.org/abs/2608.17528
