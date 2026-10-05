# Systems Figure Studio

[English](README.md) | **简体中文**

面向计算机系统与 AI Infrastructure 研究的论文绘图技能。依据文稿证据，设计架构图、机制图、资源视图与执行时间线，适用于论文和博士学位论文。

**论文材料 → 明确解释任务 → 选择具体画法 → 组织对象与关系 → 生成与修订 → 按需交付可编辑文件 → 验证。**

[技能入口](SKILL.md) · [离线画法浏览](guide.html) · [案例与输入](examples/showcase.md) · [变更记录](CHANGELOG.md)

## 能做什么

- **选择或评价画法**：查阅词条、比较变体、评价已有图，不自动生成图片。
- **新图或结构性重画**：依据文稿选择对象与关系，生成、检查并修订。
- **局部修改**：修改文字、配色或连线，保留其他已接受的设计。
- **可编辑交付**：使用 draw.io 或 WPS/PowerPoint（PPTX），可将独立生成素材与原生标签、连线组合；要求全矢量或内部可编辑时，再重建对应内部几何。

画法覆盖模型、推理、硬件、存储、预测、调度、训练、强化学习、Agent、系统软件、Kubernetes 和可观测性。变体具有稳定 ID、选择信息与来源关联，当前覆盖情况见[自动生成的统计](catalog/statistics.json)。

配色规范提供 12 组“浅色背景＋适中主体色＋鲜明／深色强调”的混合组合，同时保留原有柔和与明快方案。绘图或改色后，模型需要打开实际图面，检查主次、色彩平衡、留白、形体及目标尺寸可读性，并在授权范围内修订。详见[配色规范](references/visual-system.md)和[审美复核](references/visual-quality.md#aesthetic-review)。

## 中英文支持

README 提供中英文版本。`SKILL.md` 保持为唯一英文执行入口，多数详细主题正文保留中文；可以用中文或英文提出绘图要求。

图内语言按 **用户明确要求 → 目标章节术语 → 目标正文与图注语言** 确定。例如，用中文讨论英文论文，默认仍使用英文标签；将论文改编为中文博士论文章节时，遵循目标章节的术语。

## 安装

### 首次安装

需要 Git，以及能够加载 `SKILL.md` 的 Agent 宿主。安装本技能不需要构建软件包或填写 API Key。对于从 `~/.agents/skills` 发现技能的宿主，直接克隆到技能目录：

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/Jinghao-coding/systems-figure-studio.git ~/.agents/skills/systems-figure-studio
cd ~/.agents/skills/systems-figure-studio
```

目标目录需尚不存在。已有本仓库时，直接使用该目录作为唯一维护源。其他宿主使用其配置的技能发现目录，不要在多个目录重复克隆或复制安装。安装后如未显示，可刷新宿主技能列表或新建聊天。

根目录 `SKILL.md` 与旁边的主题、参考、素材等目录需要一起保留；只复制一个 `SKILL.md` 会缺少依赖内容。

### 更新已有安装

```bash
cd ~/.agents/skills/systems-figure-studio
git status --short
```

存在本地修改时，先检查并保留修改。工作区干净后执行：

```bash
git pull --ff-only
```

如果 Git 提示分支分叉，先处理历史差异再更新，不要重置或覆盖本地工作。日常浏览直接使用根目录 `guide.html`，无需生成第二份网站或重复安装技能。

### 各条路径需要什么工具

| 任务 | 所需能力 |
| --- | --- |
| 查画法、选变体、审阅材料 | Agent 能读取论文材料与技能文件 |
| 离线浏览 | 本地浏览器，直接打开 `guide.html` |
| 生成整图或定制素材 | 可用且已授权的图像生成工具，例如宿主提供的 image gen |
| 创建、修改、导出 draw.io | 相应 draw.io 集成、编辑器或原生文件工具 |
| 创建、修改、导出 WPS/PowerPoint | 相应 WPS/PowerPoint 集成或 PPTX 生成工具；编辑器验证需要目标编辑器 |
| 重建与基础检查 | Python 3.10+，仅标准库 |
| 浏览器逻辑测试 | 除 Python 外还需 Node.js 18+ |

技能提供执行说明与资源，不自动安装生图服务、MCP 服务、编辑器集成或密钥。具体可执行路径由宿主实际工具决定，相关交付要求见[可编辑制作规范](references/editable-production.md)。

## 快速使用

宿主支持按名称调用技能时，使用 `$systems-figure-studio`；否则让 Agent 读取已安装的 `SKILL.md`。同时提供相关章节、图注、原图或明确的系统设定。

**只选画法，不生图：**

```text
使用 $systems-figure-studio，比较适合这个调度机制的画法。
说明主要对象、关系与各方案的取舍，先不要生成图片。
```

**绘制新图：**

```text
使用 $systems-figure-studio，根据附件论文的设计章节绘制机制图，图内使用英文。
先展示构图、具体对象画法、配色与完整提示词，再生成并检查论文目标宽度下的效果。
```

**局部修改：**

```text
使用 $systems-figure-studio，只把 Request 改为 Job、Device 改为 GPU。
其他文字、对象、颜色与布局保持不变。
```

**可编辑交付：**

```text
使用 $systems-figure-studio，将这张图改编为中文博士论文章节配图。
遵循目标章节术语，交付 draw.io 源文件和预览。
关键标签和关系保持可编辑，保留材料中的实际机制。
```

也可以要求 WPS/PowerPoint（PPTX）。说明哪些部分需要独立编辑；生成图片内部仍是像素，除非另行重建。PPT 默认保留少量有用的可编辑对象。“先展示提示词”表示展示后继续已授权绘图；“等我确认再画”表示展示后等待。

## 本地浏览与复用

用浏览器打开仓库根目录 `guide.html`。页面内置检索数据、脚本和样式，不依赖 CDN 或后端。macOS 可执行 `open guide.html`，其他系统可直接打开文件。

支持用中文名称、英文术语和别名检索词条、变体、Agent 扩展、组合经验与使用规则。可复制单个画法、整个词条，或从最多 8 个选择导出简短组合说明。链接保留主题、搜索词、词条与变体定位。访问外部来源链接需要联网。

[历史案例](examples/showcase.md)保留制作记录。[三个跨主题场景输入](examples/scenarios/README.md)可用于后续绘图，目前没有验收通过的完整配图。素材可用状态、审阅状态和文字画法就绪状态分别记录。

## 维护与测试

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

## 版本与许可

[VERSION](VERSION)记录独立技能发布版本，[导入元数据](catalog/import.json)单独记录继承知识库版本。尚未发布的改动记录在[变更记录](CHANGELOG.md)的 Unreleased 部分。

原创文本与代码采用 [MIT 许可](LICENSE)。外部作品保留各自条款，详见[第三方说明](THIRD_PARTY_NOTICES.md)与[素材权利说明](assets/visual-library/RIGHTS.md)。
