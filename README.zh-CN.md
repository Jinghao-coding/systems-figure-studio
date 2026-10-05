<div align="center">

# Systems Figure Studio

**把系统机制画清楚，让论文中的对象与关系一目了然。**

面向计算机系统与 AI Infrastructure 的论文绘图技能，支持 image gen、draw.io 和 WPS/PowerPoint 制作流程。

[English](README.md) · **简体中文**

[快速开始](#quick-start) · [使用示例](#examples) · [画法库](#library) · [指南导航](#guides) · [变更记录](CHANGELOG.md)

</div>

## 从论文材料到系统配图

| 你正在做什么 | 技能如何帮助你 |
| --- | --- |
| 选择表达方式 | 比较具体画法，确定对象角色与连接位置 |
| 绘制架构或机制 | 依据文稿组织组件、关系与状态，生成并修订配图 |
| 解释执行或资源共享 | 选择时间线、占用视图、生命周期或部署映射 |
| 修改已有图 | 局部调整文字、颜色或连线，保留已接受的设计 |
| 交付可编辑文件 | 制作 draw.io 或 WPS/PowerPoint 源文件，保留所需编辑范围 |

**提供材料：** 相关论文章节、图注、原图或明确的系统设定。Agent 使用当前环境中的生图与编辑工具完成输出。

<a id="quick-start"></a>
## 快速开始

### 1. 安装到你的助手

把下面的请求发给 Agent：

```text
请安装 systems-figure-studio：
https://github.com/Jinghao-coding/systems-figure-studio

确认当前助手使用的技能目录，并检查是否已经安装。
已有安装就原地复用、保留本地修改；否则只安装一份完整仓库，
保留 SKILL.md 和配套资源。核对安装路径，告诉我如何在这里调用。
```

手动安装需要 Node.js 与 npm，按目标助手选择：

```bash
npx skills@latest add Jinghao-coding/systems-figure-studio --skill systems-figure-studio --agent codex --global
```

Claude Code 将 `codex` 换成 `claude-code`；项目级安装省略 `--global`。[skills CLI](https://github.com/vercel-labs/skills) 还支持其他助手，跨工具共享时优先选择符号链接方式。已有环境沿用一种安装方式即可。

<details>
<summary>Git 安装与更新</summary>

对于从 `~/.agents/skills` 发现技能的宿主，克隆到尚不存在的目录：

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/Jinghao-coding/systems-figure-studio.git ~/.agents/skills/systems-figure-studio
```

其他宿主使用其配置的技能目录，保留完整仓库。更新 Git 安装时，在原目录执行 `git status --short`，保留本地修改，工作区干净后执行 `git pull --ff-only`。CLI 安装使用 CLI 的更新方式。安装后按需刷新技能列表或新建聊天。

</details>

### 2. 从你的论文发起任务

```text
使用 systems-figure-studio，根据附件的设计章节绘制机制图，图内使用英文。
先展示构图、具体对象画法、配色和提示词，再生成并检查论文目标宽度下的效果。
```

Codex 可用 `$systems-figure-studio`，Claude Code 使用 `/systems-figure-studio`。其他环境采用宿主的技能调用方式，或让 Agent 读取安装目录中的 `SKILL.md`。[Claude Code 调用说明](https://code.claude.com/docs/en/skills)。

<a id="examples"></a>
## 常用场景

### 比较画法

```text
使用 systems-figure-studio，比较这个系统中 GPU 共享的几种表达方式。
说明每种视图能解释哪些对象与关系，先不要画图。
```

### 调整配色

```text
使用 systems-figure-studio，改善这张图的配色，保持现有布局。
将柔和区域色、清楚的对象色和较强的强调色组合起来。
改完查看实际图面，检查色彩平衡、可读性与整体美感。
```

### 只改两个标签

```text
使用 systems-figure-studio，只把 Request 改为 Job、Device 改为 GPU。
其他对象、文字、颜色与位置保持不变。
```

### 可编辑交付

```text
使用 systems-figure-studio，将这张图改编为中文博士论文章节配图。
遵循章节术语，交付 draw.io 源文件和预览。
关键标签和关系保持可编辑，保留材料中的实际机制。
```

也可指定 WPS/PowerPoint（PPTX），并说明哪些部分需要编辑。独立生成图片可以与原生标签、连线组合；需要重建图片内部时，明确提出全矢量要求。“先展示提示词”表示展示后继续绘图，“等我确认”表示先等待。

<a id="library"></a>
## 浏览画法库

在本地打开根目录 `guide.html`；macOS 可运行 `open guide.html`。页面支持离线检索中文名称、英文术语与别名，可复制单个变体、完整词条或所选对象的组合说明，无需另建一份网站。

主题涵盖模型、推理、CPU/GPU、存储、性能预测、调度、训练、Agent 与 Kubernetes。[配色规范](references/visual-system.md)提供柔和、明快及强弱混合方案；[视觉复核](references/visual-quality.md#aesthetic-review)用于绘图或改色后的实际图面检查。

可查阅[已有案例](examples/showcase.md)、[组合经验](examples/combined-recipes.md)和[场景输入](examples/scenarios/README.md)。各项资源保留自身状态，当前画法覆盖情况见[目录统计](catalog/statistics.json)。

<a id="guides"></a>
## 指南导航

| 需要什么 | 阅读位置 |
| --- | --- |
| 调用绘图流程 | [技能入口](SKILL.md) |
| 查找对象与画法 | [主题索引](references/topic-index.md) |
| 安排布局与关系 | [图形组织](references/figure-grammars.md) |
| 选配色、检查观感 | [视觉规范](references/visual-system.md) · [视觉质量](references/visual-quality.md) |
| 使用 image gen、记录提示词 | [生成提示词](references/generation-prompts.md) |
| 交付 draw.io 或 WPS/PPTX | [可编辑制作](references/editable-production.md) |
| 适配论文与学位论文 | [文档语境](references/document-contexts.md) · [验证](references/validation.md) |
| 贡献画法与工具 | [贡献说明](CONTRIBUTING.md) · [维护规范](references/knowledge-base.md) |

<details>
<summary>维护命令与可选检查</summary>

在仓库根目录执行：

```bash
python3 scripts/rebuild_navigation.py
python3 scripts/validate.py
python3 scripts/check_history.py
python3 scripts/check_release.py
python3 -m unittest discover -s tests -v
node --test tests/test_browser.cjs
python3 scripts/evaluate_behavior.py
python3 scripts/check_generated.py
```

行为评估命令检查固定用例；验证实际 Agent 行为需要保存真实执行证据。可选导出／PDF 检查运行 `python3 -m unittest discover -s tests/optional -v`，缺少依赖时报告 skipped。设置 `DRAWIO_BINARY` 后可运行真实 draw.io 导出测试。裁图可选依赖 Pillow，PDF 审计可选依赖 PyMuPDF，需要时在项目虚拟环境中安装。

画法正文维护在 `topics/*.md`，独立元数据维护在指定的 catalog 源文件中；索引、统计、浏览器载荷与离线页由它们重建。详见[维护规范](references/knowledge-base.md)、[贡献说明](CONTRIBUTING.md)、[验证记录](evaluations/maintenance-2026-10-05.md)和[发布检查](RELEASE_CHECKLIST.md)。

[静态托管准备](references/static-hosting.md)使用仓库外临时目录。GitHub Pages 工作流仅手动触发，安装和普通推送不会部署网站。

</details>

## 版本与许可

[VERSION](VERSION)记录独立技能发布版本，[导入元数据](catalog/import.json)单独记录继承知识库版本。尚未发布的改动记录在[变更记录](CHANGELOG.md)的 Unreleased 部分。

原创文本与代码采用 [MIT 许可](LICENSE)。外部作品保留各自条款，详见[第三方说明](THIRD_PARTY_NOTICES.md)与[素材权利说明](assets/visual-library/RIGHTS.md)。
