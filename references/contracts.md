# Lightweight briefs and version records

Use the minimum record needed. A label edit does not need a complete paper program.

## Paper understanding and prompt outline

Use this record for a substantial new figure; reuse it during later edits.

- Document context: Chinese dissertation / English conference paper / English journal paper; target chapter/section, visible label language, terminology mapping and intended placement width when known.
- Redraw scope when applicable: source figure, faithful reconstruction / translation / redesign / expansion, preserved semantics and supported changes.
- Target manuscript/version: root LaTeX file or PDF; relevant source sections/pages; any source/PDF mismatch.
- Background and setting: workload, resources, operating constraints.
- Problem and objective: concrete bottleneck and intended improvement, distinct from measured results.
- Design logic: observation → design choice → cooperation/execution → intended effect.
- Evidence map: the section/equation/caption supporting each consequential object, edge, state or quantity.
- Figure roles: reader question and explanatory scope for each proposed figure; do not prescribe a fixed count.
- Visual outline: major regions, reading order, meaningful mini-objects, key interfaces, details omitted or assigned elsewhere.
- Component selection for new/substantial redraws: object → term/variant → visible silhouette/parts/organization → attachment points; record adaptation to paper facts and icon/structure detail level. A label-only edit can reuse the existing selection.
- Generated components when used: object role, asset path, actual element prompt, reference inputs, visual review status, figure placements and raster/native status.
- Prompt expansion: exact selected labels, edge types/endpoints, invariants, palette and layout guidance, reference-image roles.
- Uncertainty: unresolved scientific choices versus harmless visual choices the agent can make.

The outline summarizes what to draw and why; the executable prompt specifies how to depict it. Produce both in proportion to task complexity, without requiring a separate user approval unless requested or a material ambiguity remains. Paper facts govern the outline; the style reference does not supply mechanisms.

## Figure brief

- Role and reader question.
- Authoritative paper facts and unresolved semantic issues.
- Objects, key edges with direction/payload, useful boundaries.
- Exact counts/values only where meaningful; explicitly illustrative examples.
- Detail omitted or assigned to another figure.
- Style references and what may be borrowed from each.
- Requested deliverable: raster draft / native edit / integration.

## Figure set

| ID | Reader question | Evidence | Shared objects/encodings | Status |
|---|---|---|---|---|

Architecture, mechanism and lifecycle can reinforce the same paper claim while explaining different aspects. Do not delete a figure just because the prose also explains its content. Avoid redundant inventories that add no visual explanation.

## Evolving style record

Palette; label family/scale; recurring object glyphs; data/control/feedback arrow mapping; per-object state encoding; allowed identifiers; approximate footprint. Adopt accepted choices and revise when needed. No fixed canvas coordinates or format gate during initial exploration.

## Version inventory

| ID | Role | Image path | Prompt path | Reference inputs and roles | Status | Known fixes |
|---|---|---|---|---|---|---|

Status: draft, accepted composition, needs semantic correction, reference-only, superseded, deleted. An accepted composition is not necessarily a scientifically verified final figure. Save the actual generation prompt separately from revised prompts not yet run. Record tool/model identity only when known. Avoid copying a reference image into a skill if unpublished content need not be distributed there; reusable drawing rules are enough.

For cleanup, enumerate exact candidates including duplicate review copies. Preserve approved drafts, prompts and source records. Delete only within user authorization; update galleries to remove broken image links and retain a compact deletion record.

## Delivery status

Report image path/display, retained layout, important unresolved corrections and prompt location. Semantic and visual checks apply to raster work. Editable/export checks apply only to requested native work. Actual manuscript compilation applies only to integration. Do not treat unavailable or inapplicable checks as passed.


## Before drawing a complex framework

Separate the paper's relationships from their rendering. A short note alongside the figure source is enough:

- Reader question and main operation: what should be understood first, and where does that operation occur?
- Semantic relationships: producer → actual consumer, carried item and the relevant manuscript evidence.
- Rendering: module, object, edge/port label, state marker, boundary or detail callout; placement must not introduce a new relay or processing step.
- Visible text: short exact labels and required symbols; move explanations to prose when the diagram already conveys them.
- Core mechanism: input/context → operation/change → output. A result icon alone does not explain the operation that produced it.
- Repeated entities: show separate lanes when behavior differs; otherwise use multiple identities around a shared mechanism. Do not merge entities if concurrency, isolation or ownership depends on their separation.

For example, if a profiler sends a cost estimate to a scheduler while an executor receives only the selected plan, the estimate should connect to the scheduler. The executor must not appear to relay it simply because it sits between the two on the page. A model-state tag is an annotation; a model instance with its own lifecycle may be a full object. Choose by semantics, not a universal rule that all variables must be edges.

The structure may be explored through different reading paths when genuinely uncertain; alternatives should differ in explanation, not just color. Keep the record proportionate and continue authorized work without mandatory candidate counts, stage pauses or approval gates.
