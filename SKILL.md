---
name: systems-figure-studio
description: Create and redraw figures for computer-systems conference papers, journal articles and doctoral dissertations. Infer Chinese or English figure labels from the target manuscript, using an integrated drawing knowledge base for models, GPUs, clusters, scheduling, inference, Agents and platform logos. Select concrete component constructions, compose and inspect figures, and deliver images or requested editable sources and manuscript integration.
---

# Systems Figure Studio

Draw the objects and relationships described in the manuscript. This skill maintains drawing methods for models, hardware, software, scheduling and workflows: 12 topics, 122 terms and 273 constructions, plus Agent samples and nine reference adaptations. All topics, recipes, tools and production rules belong to this one skill and support image generation, native editable drawing and revision of existing figures. Recipe provenance and versions are recorded in `catalog/import.json`.

**Default workflow: understand the manuscript → define the figure's explanatory role → select concrete object constructions → compose relationships and visual style → show the user the design and complete prompt → draw → inspect the actual image against the design.** Use an available image generation tool by default for new previews. When native sources are requested or a native project already exists, use the corresponding editing workflow. For text-only or color-only changes, preserve the accepted structure without redesigning it merely to follow the workflow.

## Infer manuscript type and figure language

Support conference papers, journal articles and doctoral dissertations in either Chinese or English. Read the destination manuscript's title, section, surrounding prose, caption and template to determine purpose, language and layout. Do not equate conferences or journals with English, or dissertations with Chinese.

Choose figure labels in this order: explicit user requirements for this figure → destination chapter and project terminology → dominant language of the destination prose and caption. The conversation language, reference image language and generation prompt language do not determine the output language. When adapting an English paper figure for a Chinese dissertation, follow the destination Chinese chapter. Preserve established system names, acronyms, mathematical symbols and code identifiers. Terms such as GPU and KV Cache in Chinese prose do not imply a request for bilingual labels.

Infer these choices automatically when the materials suffice, and briefly state the target manuscript type and label language before drawing. Ask only when the destination is missing or the task contains unresolved language conflicts. Fit the actual single-column, double-column or dissertation page width. For dissertations, maintain chapter relationships and terminology; for conference and journal papers, scope each figure to its argument. See [document contexts](references/document-contexts.md).

## Select object constructions before composing the figure

For a new figure or substantial redraw, open the relevant topics below and read the actual entries and concrete constructions. Reading only an index or remembering entry names is insufficient. Select topics by the objects in the figure, usually combining several topics; do not load the entire library for every figure. Inspect all topics when maintaining the whole knowledge base.

| Objects or relationships to explain | Read directly | Example constructions |
| --- | --- | --- |
| Neural networks, Transformer, Attention, GNN, MoE, vision and multimodal models | [Model structures](topics/models-deep-learning.md) | Repeated model layers with one expanded; round-node networks; Q/K/V planes; expert arrays and routers; distinct modality shapes |
| Model instances, requests, tokens, KV, speculative generation, prefill/decode | [Inference serving](topics/inference-serving.md) | Layered model bodies; token strips with content; cache-page mappings; dual-model candidate trees; KV handoffs |
| CPUs, GPUs, accelerator cards, nodes, clusters and interconnects | [Hardware and clusters](topics/hardware-cluster.md) | Central compute package and memory on a board; node cross-sections; node arrays with local expansions; heterogeneous property strips |
| Cloud, Kubernetes, platform logos, resource icons and connections | [Cloud platforms and symbols](topics/cloud-native-kubernetes.md) | Cloud contours and actual scope boundaries; logo plus platform title; resource icons and node structures; connections with ports |
| Datasets, tensors, device memory, buffers, transfers and storage | [Data and storage](topics/data-memory-storage.md) | Bundled sample sheets; slices and vector strips; occupied/free strips; logical-to-physical mappings; double buffers |
| Performance prediction, GNN prediction, static/dynamic features, costs and candidates | [Performance prediction](topics/performance-prediction.md) | Task graphs with device conditions; feature vectors and output records; paired matrices; configuration fans with a single exit |
| Scheduling, quotas, lending/reclaiming, sharing, placement, preemption and elasticity | [Scheduling and resources](topics/scheduling-resources.md) | Tenant resource strips; candidate overlays; admission gates and queues; time windows; save/restore snapshots |
| Training, parallelism, communication, LoRA, optimizers and checkpoints | [Training and distributed execution](topics/training-distributed.md) | Forward/backward paths; rank state tiles; communication trees/rings; pipeline lanes; temporary gathering and reclamation |
| RL, Actor/Critic, rollouts, versions, rewards, SFT/DPO | [Reinforcement learning and alignment](topics/rl-alignment.md) | Role-specific models with distinct outputs; trajectory strips; version tracks; paired preference branches |
| Agents, roles, tools, messages, context and workflows | [Agents and workflows](topics/agents-workflows.md); [role samples](topics/agents-approved-samples.md); [nine compositions](topics/agents-arxiv-patterns.md) | Consistent role avatars; tools and artifacts; local state loops; fork/join; role–request–device mappings |
| Frameworks, runtimes, containers, controllers, compilers and services | [Systems software](topics/systems-runtime.md) | Desired/observed state records and control paths; container ownership; model–runtime–service mappings; local graph rewrites |
| SLOs, performance observation, execution traces, faults and recovery | [Observability and reliability](topics/observability-reliability.md) | Time brackets; state snapshots; metric strips; task/kernel alignment; fault domains and takeover paths |

When an entry name is unclear, consult the [full index](references/topic-index.md) or `catalog/index.json`. Use [cross-topic recipes](examples/combined-recipes.md) for compositions. The [offline guide](guide.html) supports browsing, searching and copying all textual constructions. [Knowledge-base maintenance](references/knowledge-base.md) records sources, extension methods and validation commands. Topic bodies are the single source of truth for recipes; retain all variants without copying them into a second body of instructions.

### Make selected recipes visible

For each object needing concrete representation, determine: **object and role → entry and variant → silhouette, parts and spatial organization → labels and connection endpoints**. Before drawing, briefly show the user the key choices and resulting visible forms. Code comments or private notes do not replace this disclosure. The actual figure must show the selected parts and relationships; a delivery statement claiming that the library was used is insufficient.

For example, a training overview can combine the network skeleton in `network-model` with the forward/backward paths in `training`. An inference model can use the layered body in `model-instance`, a `token` sequence and `kv-cache` state strips. For a GPU, choose board identity, an exploded package or compute structure from `accelerator` according to its role, rather than always using the same board construction. Use `kubernetes-platform-logo` for platform-title ownership. The manuscript determines the actual structure; the existence of a recipe does not justify adding a model, platform or deployment.

When identity alone matters, an icon and short label can form a complete component. When explaining a mechanism, expose the relevant local network, state, data or resources. Allow structural drawings, icons and combinations, including coordinated avatars, modest decoration, subtle depth and approachable details where useful. Balance identity, structural explanation and the whole composition. Avoid reducing every object to a named box or requiring complex internals in every small icon.

**Fix structural problems through structural changes.** If the user finds objects abstract, shapes repetitive or the library unused, reselect and develop the relevant components. Recoloring, retitling or adding icons to otherwise identical boxes does not complete that redraw.

See the [visual asset library](references/visual-asset-library.md) for actual images and reusable forms. Accumulate useful objects as needed, distinguishing accepted references from cleaned assets; inspect leftover text, cropped edges and arrows before reuse. Figures may use GPT Image for the whole image, mixed assets or native primitives as appropriate. Editability is not required for every figure by default.

## Generate new local elements when needed

The knowledge base is an adaptable starting point, not a closed catalog. When no construction fits, or existing constructions look monotonous or inconsistent in the current composition, use GPT Image or the available image generator to design local elements for the figure. This applies to GPUs, CPUs, models, storage, nodes, Agents, tools, data objects and any other object requiring a custom form. Do not wait for the user to request every element or exhaust all entries first. Use capabilities actually exposed by the tool; writing a model name in a prompt does not select that model.

Choose whole-image generation, separately generated elements followed by composition, or a representative component extended to the figure set according to the task. Before generating an element, show its purpose, design and complete prompt. Then display and inspect the result inline, and supply selected elements as actual image inputs or assets when composing the figure. Mentioning a filename in a prompt does not reuse its image. Coordinate color, perspective, silhouette, lighting and detail density at the final figure scale; reuse an element to preserve object identity.

Standalone elements for composition usually need transparent backgrounds, complete contours and clear space for connections. Set the actual transparency parameter when supported. Keep variable labels, counts, states and arrows in the composition layer where possible instead of baking them into pixels. Generated constructions do not constitute real product photographs, official logos, precise microarchitectures or experimental results. See [element generation](references/generation-prompts.md) for prompts and checks.

Generated elements may be imported directly into draw.io or PowerPoint as separate image objects alongside native text, shapes, connectors and groups. This is a normal production path and requires no additional permission to mix assets. Each element can be moved, resized, replaced and grouped independently; text, arrows, state markers and layout remain separately editable. Rebuild internal geometry from the generated reference only when the user explicitly requires full vector output or editing of individual internal parts. Explain that image interiors remain pixels without treating every editable draw.io/PPT request as a requirement to reconstruct all elements as vectors. Do not flatten the entire figure into one image. Retain useful project assets and actual prompts without turning every candidate into a global entry or creating duplicate backups.

## Develop recipes into visual designs

Recipes provide alternative constructions, not fixed icon templates. For new figures, substantial redraws or feedback that a figure looks stiff or unattractive, first read [visual choices and trade-offs](references/visual-quality.md), then choose key objects' **silhouettes, proportions, part relationships and detail scale**. Draw on user references or library examples that have actually been inspected. Design missing forms yourself without claiming unseen sources as visual evidence.

When the user requests inspiration from research figures, search for and inspect actual figures from leading AI or systems conferences relevant to the current objects, preferring official publications or author manuscripts. Extract silhouettes, parts, grouping, connections and color roles. Update existing entries and source records using “source and figure number → retained elements → omitted content → applicable objects.” Do not merely add paper links or assume that a conference's reputation makes an entire figure worth copying.

Produce an actual preview of a key object and one representative relationship, inspect it at reduced size, then extend the design to the figure set. Show the representative preview to the user and state the adopted form. Continue authorized drawing without turning this disclosure into another approval gate. GPUs, models and storage should have recognizable features at their intended size. Adding an icon or including recipe parts does not by itself establish visual quality. Small objects may be simple; large objects should avoid empty placeholders. Precision comes from object relationships, not accumulated pins, screws or shadows.

Choose paths, lanes, local expansions or state comparisons according to the reading relationships. Reuse shapes for objects of the same kind and frames for real ownership. Do not force every object into an identical card for symmetry. Revisions addressing stiffness must examine both component forms and the whole figure's emphasis, density and spacing, beyond colors, rounded corners or thickness. Assess technical correctness and visual quality separately; more detail is not automatically more attractive.

## Understand the content and scope

- **Review, planning or recipe lookup:** read the materials and provide concrete recommendations or recipes; tool availability alone does not authorize image generation.
- **New figures or composition previews:** read the manuscript, select components and generate the figure; save actual prompts and reference roles following the [prompt guidance](references/generation-prompts.md).
- **Revision or redrawing:** inspect the original figure and surrounding prose; distinguish faithful reconstruction, translation, local repair and redesign. Preserve accepted choices.
- **Native editing or manuscript integration:** when draw.io, PPT or another native source is requested, or a native project exists, read [editable production](references/editable-production.md) and use the corresponding workflow. Acceptance of a raster draft does not automatically request vectorization or manuscript integration.
- **Figure sets:** give each figure a distinct explanatory role while sharing object identities and visual language. Do not impose a fixed count, layout or chapter coverage.

Before composing, distinguish real manuscript objects and connections from visual grouping and local expansions. Organize the main visual around the mechanism being explained. Variables and result labels do not automatically become modules; do not route connections through unrelated components for layout convenience. For complex new figures, use a [compact composition record](references/contracts.md) to check objects, operations, actual recipients and visible labels before drawing, without imposing fixed stages or approval procedures.

Read the supplied TeX entrypoint, referenced figure sources, captions and nearby paragraphs, or the specified PDF's prose and actual pages, to establish objects, inputs/outputs, dependencies, states, resource ownership and counts. Report the actual scope when only part of the material was read. Trace key visual facts to prose, equations or evidence; do not add unimplemented mechanisms or fabricated results. Style references supply only the explicitly borrowed composition, forms or colors, not facts about the target manuscript.

First identify the question the figure answers, then choose an [overview, mechanism comparison or lifecycle composition](references/figure-grammars.md). Determine parallelism, dependencies and hierarchy among research contributions from facts, not visual templates. Show the design and complete prompt as specified below, then continue authorized drawing. If the user explicitly requests prompt review first, wait for feedback before invoking drawing tools.

Automatically use natural, concise Chinese labels or accurate English terminology according to the destination manuscript. Preserve its system names, acronyms, symbols and object granularity. See [document contexts](references/document-contexts.md) for adaptation and translation.

## Choose the representation and preserve accepted design

Identify the relationship readers most need to compare or understand, then choose a single mechanism figure, an overlay of the same object or complementary panels. When uncertain, compare distinct actual examples. Avoid repeatedly applying a familiar template or adding panels only for novelty. Data overlays must share meaningful coordinates and real observations. Mechanism overlays must refer to the same object, location or state; do not merge unrelated abstraction levels into one scene.

An accepted visual design is the baseline for later revisions. Identify which proportions, transparent layers, contours, colors and local expansions aid reading and preserve them. Do not erase these features merely to reduce drawing code or standardize components. Recompose when the user has identified structural problems. Color maintains identity and emphasis; it does not replace structural choices. See [visual choices and trade-offs](references/visual-quality.md).

Records of external methods, what was read and what was adopted are in [Vivid Figures methods](references/vivid-figures-ideas.md), [figures4papers examples and methods](references/figures4papers-ideas.md) and [Framework Studio methods](references/framework-studio-ideas.md). These methods are integrated into this skill and do not require another skill to be installed or invoked.

## Color, logos and labels

Assign colors to object identities, related variants and focal points. Use light fills for bodies and darker outlines or local accents for emphasis; related hues can connect variants. Select and adapt a palette from the [visual system](references/visual-system.md) to the manuscript's roles. Preserve object colors and ordering across comparison panels. Connect overall paths and local expansions through position, form and color. See [figure organization](references/figure-grammars.md) for composition and chart rules; copying hex values while keeping a stiff layout is insufficient.

**Use varied palettes and judge the whole composition.** Consider color, form, light/dark balance and whitespace in inspected references to choose a coordinated scheme for the current figure. Earlier palettes are references to compare, not permanent defaults. Different figure types may use different color families; directly compared panels and successive states of the same object must maintain consistent encoding. Reduce competing color roles instead of mechanically reverting to blue-gray boxes or imposing a three-color limit. Combine or adjust candidates from the [visual system](references/visual-system.md) for aesthetics, recognition and manuscript consistency. Honor explicit requests to preserve particular colors.

Logos, avatars, tool symbols, chips and file icons can help identify objects. Model brands, frameworks, platforms and devices are distinct entities: place symbols on the corresponding component, boundary title or interface and compose them with structures and connections. A logo need not be an experimental variable to appear. Not every figure needs logos, and a plain-text name is not a graphical logo. Use accurate official or user-provided assets; when unavailable, use a name or placeholder rather than claiming a generated approximation is accurate. See [logo composition](references/cloud-logo-composition.md) and [component visual choices](references/visual-quality.md).

Keep object identities, technical terms and the explanations needed to decode the figure. When composition already expresses research relationships, omit editorial subtitles such as “four parallel studies.” Keep words such as “design” or “research content” only when they add necessary technical meaning; do not ban them mechanically. Put long explanations in the manuscript. Preserve counts, units and necessary scientific conditions accurately. Recipe IDs, production status and validation notes do not belong in the finished figure.

Maintain consistent stroke widths, typography hierarchy, perspective and icon detail density. Boundaries express ownership; arrows express actual flow. Do not draw mappings or candidates as executed paths. Distinguish model layers, instances, shards, ranks, roles, requests and devices. Quantitative shapes require real data or an explicitly stated schematic interpretation.

## Show the design and complete prompt before drawing

For a new figure or substantial redraw, show the user the relationship to explain, main composition, visual focus and each key object's “selected construction → visible result” before invoking a tool. Instead of merely naming the GPU entry, specify whether the figure uses a thin board, exploded package or resource-occupancy view, and how it connects to models and data.

Then provide **the complete prompt actually intended for this invocation** in a code block, including concrete forms, spatial relationships, color roles and values, connection endpoints, visible labels, reference-image roles and scientific constraints. A saved prompt file is useful but a link, summary or after-the-fact record cannot replace this advance disclosure. For native drawing, show an equivalent complete composition brief without dumping every low-level API operation. For local edits, show the complete edit instruction and what to preserve. If the design changes before submission, show the updated version.

Disclosure lets the user understand and intervene in the design; it does not automatically add an approval step. Stop at this stage when the user requests “show the prompt first” or “draw after confirmation.” Otherwise, continue authorized drawing. Honor an explicit request to omit disclosure.

## Draw, inspect and deliver

Use currently available, authorized tools. Supply reference images through the generation tool's actual mechanism and inspect local originals first. A path string is not proof that an image was supplied. Do not claim an unverifiable model version. Retry a plausibly transient failure at most once, then report the limitation; do not silently switch to a paid API. For native production, preserve independently editable text, shapes, paths and connections and verify against the actual tool capabilities.

Following the disclosure requirements above, combine manuscript facts, selected constructions, layout, palette and necessary labels into an executable prompt or native composition brief. Avoid relying on adjectives such as “advanced” or “top-conference style,” or concatenating all recipes into the drawing input. Use [figure briefs and version records](references/contracts.md) for concise documentation.

Inspect the actual image after each round using the [semantic and visual checks](references/validation.md):

- Do key objects use concrete constructions suited to their roles? Do forms and relationships explain the content, or do long text boxes still carry everything?
- Does the palette fit the composition and figure set? Are color roles and contrast clear, and do icons/logos fit the whole image?
- Are object identities, arrow endpoints, data/control distinctions, candidate/execution distinctions, states and counts accurate?
- Are parts and short labels readable at small size? Are there redundant subtitles, typos, overlaps or empty boxes?

Fix actual defects using the [iteration playbook](references/iteration-playbook.md). Passing code or primitive validation does not establish visual quality, and a prompt requirement does not prove that the generated image satisfies it. Read [compact layout](references/compact-layout.md) when exact publication dimensions matter.

Display results inline and deliver the corresponding files and actual prompts/composition records. Require native sources and manuscript compilation only within the authorized scope. After manuscript integration, inspect actual page width, captions and float placement. Keep useful drafts and provenance; distinguish inherited source-image reviews, textual recipes and acceptance of the current output. Retain the knowledge-base entries, sources, Agent samples and navigation guide. Publishing, remote synchronization and deletion of historical outputs require their own authorization.
