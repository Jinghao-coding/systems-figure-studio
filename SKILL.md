---
name: systems-figure-studio
description: Select, draw, review and revise computer-systems and AI Infrastructure research figures. Use manuscript-grounded constructions and deliver requested editable sources or paper integration.
---

# Systems Figure Studio

Turn manuscript objects, relations, states and evidence into an explanatory figure. This is the single execution entrypoint; `topics/*.md` are the sole maintained recipe bodies. Use the [offline browser](guide.html), [topic index](references/topic-index.md), and [worked examples](examples/showcase.md) for selection. Package version and inherited knowledge-base version are separate; see [provenance](catalog/import.json).

## Global constraints

- Read the target material and original figure before judging or editing. Establish the question the figure answers and trace mechanism facts to that material. References supply only explicitly borrowed visual expression, never target-system facts.
- Label language follows explicit user requirements → target chapter terminology → target prose and caption language. Chat language does not decide labels. Preserve names, symbols and object granularity.
- Select concrete constructions for each role: identity, structure, deployment, state or execution. Icons, role avatars, accurate logos and modest depth are allowed when useful. Preserve Cloud/Kubernetes, CPU/GPU, storage, cluster and connection semantics; do not turn every object into a box.
- Allow rich coordinated color within a single figure, including multiple vivid object families. Mix light context colors, medium-strength object colors and stronger accents according to role and area; preserve soft palettes as options. Choose hue count and saturation for the composition rather than applying one intensity to every object. See [visual system](references/visual-system.md).
- Preserve accepted design outside a requested local change. Distinguish candidates from execution, roles from requests/instances/devices, and waiting from resource residency. Unsupported quantities remain explicitly illustrative.
- Use only exposed, authorized tool capabilities. Do not invent model selectors or image-reference parameters, incur unapproved costs, publish, push or delete historical assets.
- Keep actual inputs, prompts/native briefs, revisions and checks. Source review, recipe readiness, artifact quality and user acceptance are independent. Never transfer historical acceptance to a new output.

## Task routing

| Request | Execute |
| --- | --- |
| Lookup, critique or choose a construction | Read the material and relevant entries/variants; provide grounded recommendations. Do not generate images. |
| New figure or structural redraw | Read → define explanatory question → choose variants → inventory objects and endpoints → disclose design/brief → generate → inspect → revise. |
| Labels, colors or local connectors | Inspect the original; name the changed objects and preserved design; apply only that scope and compare the result. Do not force a whole-figure redraw. |
| Editable delivery or paper integration | Add [editable production](references/editable-production.md) and the applicable export/integration checks to the relevant route above. |

### Disclosure and confirmation

Show the actual complete prompt or equivalent native composition brief before drawing, unless the user asks to omit it. **“Show the prompt first” means disclose and continue already authorized drawing. “Draw after confirmation” means disclose and wait.** An explicit request for approval is a wait condition; disclosure alone is not. For local edits, disclose the edit and preserved scope. Follow the host/tool protocol for the actual invocation. Details and recording conventions: [generation prompts](references/generation-prompts.md).

## Read on demand

For new or structural work, read the selected topic bodies and specific variants, not merely their titles. Use stable variant IDs from `catalog/variants.json`; selection metadata supplements the Markdown without duplicating descriptions. [Combination recipes](examples/combined-recipes.md) are starting points; resolve connections using the target material.

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


| Need | Reference |
| --- | --- |
| Figure question, object roles, endpoints and version record | [Contracts](references/contracts.md) |
| Layout, paths, lanes, comparisons and lifecycle | [Figure grammars](references/figure-grammars.md) |
| Component choice, local elements, accepted design, visual trade-offs | [Visual quality](references/visual-quality.md) |
| Palette and accurate platform/logo attachment | [Visual system](references/visual-system.md), [Cloud/logo composition](references/cloud-logo-composition.md) |
| Asset reuse, status and independent image elements | [Visual assets](references/visual-asset-library.md) |
| Manuscript language, target width and adaptation | [Document contexts](references/document-contexts.md), [compact layout](references/compact-layout.md) |
| Native editing, minimal PPT object count and export | [Editable production](references/editable-production.md) |
| Structural, semantic, visual, editor and integration checks | [Validation](references/validation.md), [iteration](references/iteration-playbook.md) |
| Sources, maintenance, variants and regeneration | [Knowledge-base maintenance](references/knowledge-base.md) |

Supported production routes are **image generation**, **draw.io**, and **WPS/PowerPoint (PPTX)**. Choose the tool from the user request and available host capabilities: image generation for whole figures or independent elements, draw.io for native system diagrams, WPS/PPTX for slide editing and delivery. A worked example using one route does not remove the others.

Native editable documents may combine independent generated images with native labels, semantic objects and connectors. Reconstruct image internals only for an explicit full-vector/internal-editability requirement. For PPT/WPS, preserve the user's small-object workflow described in editable production; grouping dozens of fragments does not reduce complexity.

## Completion

Deliver the requested recommendation or actual output with input/design records and usable paths. For new drawings and color revisions, perform the [rendered aesthetic review](references/visual-quality.md#aesthetic-review): inspect overall appeal, hierarchy, color balance, spacing and target-size readability; revise observed defects within scope and inspect again, and record structural, semantic, visual, editor and paper-integration checks separately. Report tool limitations precisely. Keep one authoritative editable source and explain whether regeneration overwrites direct edits. Do not claim generation, visual acceptance or editor round-trip from static checks alone.
