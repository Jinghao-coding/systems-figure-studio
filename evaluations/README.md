# 绘图行为回归评估

[固定输入与预期约束](behavior-cases.json)覆盖目标语言、局部编辑、只评价、全矢量、候选执行、工具等待与 KV、平台标识、提示词交互和素材筛选。

`python3 scripts/evaluate_behavior.py` 只验证用例字段完整性；输出中的 Agent 执行与视觉评估保持 `not_run`。测试文档出现某个词不构成 Agent 行为通过。

实际评估时，在具有相应工具的宿主中逐条运行 `request` 和 `material`，保留完整工具轨迹、输入源、输出文件、提示词及修订。将轨迹归一化为如下记录，再使用 `--evidence path/to/evidence.json` 检查明确约束：

```json
{
  "review-only": {
    "trace": "traces/review-only.json",
    "observed": {"route": "review", "drawing_calls": 0},
    "visual_status": "not_applicable"
  }
}
```

`trace` 相对于 evidence 文件。归一化字段必须从真实轨迹和产物提取；评分器检查轨迹文件存在及字段相等，不自动证明轨迹归一化可信。缺失用例为 `not_run`。禁止将预期字段直接复制成“实际执行证据”。

每次报告分别记录：确定性结构约束、实际 Agent 运行、图面/人工检查。结构检查关注对象、端点、标签和素材；行为检查关注路由、调用与确认；视觉检查关注目标宽度下的可读性及语义表达。生成图不要求像素一致。

三个跨主题 [场景输入](../examples/scenarios/README.md)可用于后续完整案例建设。本轮试制图已按用户意见撤出，不纳入完成案例或行为成功记录。
