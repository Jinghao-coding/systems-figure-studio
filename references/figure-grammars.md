# Figure roles and component drawing recipes

## Pick the reader question

| Role | Show | Leave for other figures |
|---|---|---|
| Overview | Modules, key objects, interfaces, useful ownership/deployment | Full state machines, cost matrices, algorithm steps |
| Decision example | Same input, candidates, decision, consequence | Repeated entire architecture |
| Lifecycle | Same object across states, events, resource acquisition/release | Unrelated deployment details |
| Protocol | Participants, message order, overlap, waits | Decorative cycles or invented timings |
| Resource view | Capacity, residency, occupancy and owner where relevant | Measured-looking values without data |
| Predictor view | Actual inputs, processing roles and outputs | Unsupported internal network/tree details |

Use the number of figures the argument needs. A three-figure overview/decision/lifecycle set worked for one scheduling paper; it is not a universal requirement. Architecture does not need a feedback loop unless one matters in the actual system. Show genuine branches and fan-in; do not substitute generic circles for a defined topology.

## Concrete small components

The table below is a compact starting point. For alternative shapes and domain-specific constructions, use the [component topic index](topic-index.md); for multi-topic compositions, see [combined recipes](../examples/combined-recipes.md). Select the figure role first, then adapt only the needed components.

| Component | Useful drawing | Check |
|---|---|---|
| Workflow | Small fork/join DAG, short IDs, highlighted focal node | Dependencies and identities persist across views |
| Request collection | Aligned short tiles with IDs and optional ellipsis | Visual order does not invent FIFO semantics |
| Feature input | Compact vector bars/cells, labels for actual feature groups | A decision tree is a predictor, not automatically a feature |
| Predictor | One small processing glyph or faithful known structure | Do not invent internals to make it lively |
| Action/lookup table | Actual small rows/columns with defined index and symbolic values | Index, meaning and mutability match the paper |
| Scheduler | A small input set and candidate/resource or frontier inset | Show the decision, not every algorithm condition |
| Model instances | Flat layer stacks; distinct large target and small draft when applicable | A separate target-only instance stays distinct |
| Runtime | Endpoint groups, request slots and shared-resource strip | No unsupported endpoint-to-GPU mapping |
| Preparing / active / free | Outlined/dashed slot / occupied slot / empty slot, with labels | State is independent of request identity |
| Slack / interference | Baseline branch bars, bracket, hatched absorbed extension, exposed extension | Causal meaning and numerical decomposition agree |
| Model lease | Small lease label or lock adjacent to protected object | Encodes actual eviction protection, not decoration |

## Small examples, not new system facts

For an illustrative placement comparison, repeat the SAME candidate request and workflow in both panels. Existing endpoint occupants may differ. Name other affected workflows separately. If costs are 24 and 22 and lower is better, only the 22 candidate is selected. Do not show two unrelated inputs as evidence of a placement decision.

For a lifecycle, carry the SAME focal tile through the states. Count existing occupancy before inserting the candidate. At release, show an empty slot rather than leaving the request in a dashed slot. Distinguish a logical state from a concrete queue implementation.

For a model deployment, large/small stacks show role or relative model size only when supported; stack-layer counts are schematic unless explicitly defined. A logo supplements target/draft/engine labels. Do not copy Qwen, DeepSeek or hardware counts from another paper.

## Learn from references

Inspect actual figures and separate three things: explanatory role, composition, and styling. A conference predecessor may provide useful visual continuity while its deployment or mechanism is outdated. Borrow miniature objects and readable interfaces, then redraw relationships from the current manuscript. When drawing on a corpus, record only figures actually inspected and distinguish observed practice from your chosen palette.


## Overall route with local explanation

Use an open main route for the central input–processing–output relationship, then a smaller aligned inset for the relationship readers need to inspect. Match the inset to the actual object using a connector, repeated identity or a labeled callout. In a systems figure, this could be a device pool with one board expanded, a workflow with one request lifecycle, or a model with one layer expanded. Insets need not be equal-sized cards. Their headers stay within their own panel and far enough from the previous panel to avoid mistaken grouping.

Use different representations where the objects differ: token strips for sequences, small graphs for dependencies, vectors for encoded features and an appropriate model construction for processing. A concatenated strip means concatenation only when the method actually concatenates; attention or other fusion needs its own operation. This follows the visual organization of the reviewed [figures4papers examples](figures4papers-ideas.md), not their scientific content.

## Quantitative comparison and complementary panels

Choose the comparison first: grouped bars or points for methods across conditions, consistent small multiples for metrics, a line for an ordered independent variable, and a distribution/interval view when variation is the question. Keep method order, color, units and legend mapping stable. A shared external legend is useful when it saves space; an entire legend panel is optional. Choose the layout at publication width rather than copying an ultra-wide source canvas and shrinking everything.

Length-encoded bars normally start at zero. For small differences use a point/interval plot or an explicitly marked zoom/broken axis with enough context; never automatically set a bar baseline from the minimum value. A trend may use a focused range when ticks and scope remain clear. Error bars and bands require a defined statistic and real measurements; no decorative uncertainty. Hiding category ticks is appropriate only when position/group identity is completely recoverable from nearby labels or the legend.

An overview, ablation and local mechanism view can complement each other when each answers a different question. Do not force every figure into this trio. A shaded sphere or surface is useful for geometry only when that geometry matters; for GPUs, topology or occupancy use the corresponding object grammar instead of borrowing a 3D effect.


## Main mechanism, connectors and local details

Choose the visual focus from this figure's explanatory role: interactions for a protocol, changing state for a lifecycle, decisions and consequences for scheduling, or data transformations when they clarify the mechanism. A background overview need not claim a contribution. Data flow remains valid for systems/method diagrams when it is the clearest truthful explanation; it is not limited to dataset papers.

A line must terminate at its actual producer/consumer or at a clearly marked visual anchor. If an intermediate module does not handle an item, route around it. Similar parallel edges may share a corridor, but preserve distinct endpoints and payloads when technically relevant. Dashed feedback, a dashed candidate and a detail callout need distinguishable context/labels; do not add unlabeled rails to make a diagram look technical.

Place internal operations either inside the main object or in its connected detail view. The detail should add information; avoid repeating an entire miniature workflow in both locations. Use a bracket or thin neutral non-flow connector for magnification. Keep a small context/topology view subordinate when the main task is to explain a local mechanism. Space and visual weight follow explanation needs, without a fixed module count or area quota.
