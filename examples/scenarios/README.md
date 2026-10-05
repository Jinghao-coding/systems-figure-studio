# 跨主题场景输入

这些输入是明确的 illustrative/synthetic 系统设定，可用于制作或评估，不是已完成的绘图案例。

| 场景 | 输入 | 核心验收 |
| --- | --- | --- |
| GNN 预测与调度 | [输入 A](gnn-scheduling.md) | 特征、预测、候选、选择与执行分开；预测直达决策者 |
| Agent 与生命周期 | [输入 B](agent-lifecycle.md) | 角色、请求、实例、设备分开；工具等待与 KV 驻留独立 |
| Kubernetes 异构集群 | [输入 C](kubernetes-cluster.md) | 平台归属、部署、物理资源和不同连接类型分开 |

本轮原生试制图经用户评价后撤出；不保留在正式案例、素材选择或浏览器中。对应实际产物由维护者保存在仓库外备份中。后续画法、布局及工具选择需要重新设计，不能把这些输入或曾执行的导出当作合格案例。

完整案例获准保留后，放入一致目录 `examples/cases/<id>/`：`input.md`、`inventory.json`、实际 `native-brief.md` 或提示词、初稿、修订记录、预览、一种权威源文件、`checks.json`。再登记到 `examples/cases.json`，并在选中变体的 `cases` 中反向关联。登记前检查记录必须分开包含 structure、semantics、visual、editor、paper_integration 及 current user_acceptance。
