# 2026-10-05 本地实施与验证记录

## 实施范围与用户调整

从 `main`（本地 HEAD `ba83907`）开始，已有 `SKILL.md` 与 `references/editable-production.md` 的未提交 PPT 偏好修改。后者完整保留；入口里的偏好随精简转入详细规范并保留入口说明。初始实施阶段未提交、推送、发布或部署。后续用户已授权同步远程；发布与部署仍独立处理。

英文入口精简到 70 行，保留 image gen、draw.io、WPS/PPTX 三条路径，明确只评价、整图、局部编辑与附加可编辑交付的路由及提示词交互。没有修改 `topics/*.md` 正文、原有词条锚点或 Agent 保护哈希。

稳定登记全部变体 ID；其中 11 个按示意输入补充适用问题、表达层次、连接端点及不适用条件，其余明确未审阅。来源、历史统计、文字状态、资产生成记录和当前使用状态独立保存。索引、当前统计、浏览器载荷和离线页不再依赖旧生成文件。

三个原生试制图实际经历源文件生成、draw.io 导出和初稿检查。用户评价不佳并要求不保留后，图源、预览、生成脚本和修改记录均移到仓库外任务备份；本仓库没有将它们列为合格案例。保留的输入位置：

- [A：GNN 预测与调度](../examples/scenarios/gnn-scheduling.md)
- [B：Agent 生命周期](../examples/scenarios/agent-lifecycle.md)
- [C：Kubernetes 集群](../examples/scenarios/kubernetes-cluster.md)

当前 `examples/cases.json` 为空，完整案例统计为 0；原有历史案例与资产未删除。新的三个完整案例和完整系统图可编辑交付仍待重新设计。

## 最终本地检查

执行环境：macOS，Python 3.14.8，系统 Node.js，已安装 draw.io。命令均在仓库根目录执行。

| 命令 / 检查 | 结果 | 实际范围 |
| --- | --- | --- |
| `python3 scripts/rebuild_navigation.py` | passed | 当前正文与独立元数据重建索引、统计、载荷和离线页 |
| `python3 scripts/validate.py` | passed | 当前 ID、字段、本地链接、来源、素材、关联和生成一致性 |
| `python3 scripts/check_history.py` | passed | 52 个旧词条链接、继承来源、Agent 受保护正文 |
| `python3 scripts/check_release.py` | passed | 包结构、可移植路径、语法与素材依赖 |
| `python3 -m unittest discover -s tests -v` | passed | 26 tests；包含在临时副本删除全部生成结果后重建两次 |
| `node --test tests/test_browser.cjs` | passed | 9 tests；包含中英检索、安全渲染、单变体/组合导出、Python/JS 全变体导出一致性 |
| `python3 scripts/evaluate_behavior.py` | passed | 11 个固定评估用例的字段校验；Agent 与视觉结果保持 not_run |
| `python3 scripts/check_generated.py` | passed | 所有当前生成结果与内存重建完全一致 |
| `DRAWIO_BINARY=… python3 -m unittest discover -s tests/optional -v` | 1 passed, 1 skipped | 真实 draw.io 导出原有 GPU 源成功；PyMuPDF 未安装于该 Python，字体测试 skipped |
| `python3 scripts/prepare_site.py` | passed | 本地静态包；包内 Markdown 本地链接检查 passed |
| Python AST `feature_version=(3,10)` | passed | 脚本与测试的 Python 3.10 语法；最低版本实际运行交给已配置 CI |
| `node --check scripts/web/guide.js` | passed | 浏览器源语法 |
| `git diff --check` | passed | diff 空白检查 |

过程中发现并修复：搬移说明后四处相对链接失效；包检查器错误地将新增 JS/CSS 类型纳入 XML 检查；首次静态包遗漏 evaluations 文档。以上检查已重新执行并通过。

## 分层验证边界

- **结构**：实际单元测试与校验通过；SVG 审计新增图片依赖缺失检查，仍分别输出图像元素、标签与 ID 情况。
- **语义与视觉**：三个试制初稿有实际人工图面/端点检查记录，但已被用户撤出，不作为验收通过案例。
- **编辑器**：原有 GPU 原生源通过真实 draw.io 导出测试。GUI 中另有用户未保存文档，尝试打开案例触发丢弃修改提示后已取消；没有执行完整系统图的 GUI 改名、移动、图片替换和再次导出链路，不声明 round-trip 通过。
- **论文集成**：not_run，没有目标论文源文件。
- **浏览器 GUI**：not_run。Chrome 控制入口不可用；内置浏览器策略拒绝本地文件协议。已完成的是 JavaScript 功能/安全测试。
- **Agent 行为**：not_run。用例与实际轨迹评分接口已建立；没有把静态规范匹配当作行为成功。
- **Hosted CI / Pages**：not_run。CI 配置 Python 3.10 / 3.13 与 Node；Pages 仅手动触发，本次没有远程操作。

## 本地使用与迁移

直接打开根目录 `guide.html`。维护入口见 [README](../README.zh-CN.md)；变体与数据职责见 [维护说明](../references/knowledge-base.md)。正常重建不修改任何图源。后续按单一维护源要求移除了临时 `dist/site`。当前打包使用 `python3 scripts/prepare_site.py --output <仓库外的新临时目录>`；拒绝仓库内输出及覆盖已有目录，已实际测试并清理测试临时包。

旧词条 ID 和 Markdown 锚点不变，浏览器兼容旧 term hash。变体 ID 为持久身份，改标题只更新 selector。独立发布版本仍是 `0.1.1`，继承知识库版本仍是 `0.4.1`；本次记为 Unreleased。

### Mixed palettes and rendered aesthetic review

Expanded the maintained mixed-role palette table from 4 to 12 combinations, retaining previous soft and vivid pools. Added an actual-render aesthetic review to `references/visual-quality.md` and routed new drawings/color revisions through it from the entrypoint, validation and iteration references. PA05–PA08 record the Nature Methods editorial overview, Susie Lu's design notes, SciencePlots and Penrose README reading; the latter projects were not installed or executed.

Executed successfully: `python3 scripts/rebuild_navigation.py`, `python3 scripts/validate.py`, `python3 scripts/check_history.py`, `python3 scripts/check_generated.py`, and `git diff --check`. The presentation helper `render_mixed_all.py` (retained with the local conversation review artifacts, outside the repository) rendered three review sheets and checked all 72 swatch pixels against maintained RGB values. Inspected all three PNGs: labels and swatches are unclipped, role columns align, and each row shows a visible light-to-strong range. These are palette-selection previews; the new model review instruction has not been evaluated on a newly generated system figure in this turn.
