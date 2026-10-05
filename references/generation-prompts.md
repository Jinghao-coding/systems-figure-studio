# Image-first prompts

Use the available authorized image tool. Do not specify an unverifiable backend model. Attach or reference images through the tool's supported mechanism; text mentioning a path is not necessarily image input. Inspect local references before editing. Follow tool instructions over generic workflow suggestions.

## Build and show the actual prompt

Before calling the drawing tool, show the user the chosen composition, key object constructions and complete executable prompt in a code block. A saved file or a summary is not a substitute. For a local revision, show the complete edit instruction and preserved properties. “Show the prompt first” means disclose and continue authorized drawing; “draw after confirmation” or an explicit approval request means disclose and wait. Honor explicit requests to omit this display.

Choose constructions before writing prose. For a visually important object whose representation is unsettled, compare materially different silhouettes or views, then select one for its explanatory and visual effect. A color change is not a different construction. Explain the selected result briefly; do not make the user select every detail.

Write a figure-specific prompt using the fields below, replacing placeholders with actual choices. There is no universal palette, arrow-color mapping or left-to-right layout prefix to paste into every request. Choose a palette from [visual-system](visual-system.md) or design a suitable one, then state actual colors and roles in the prompt. Use figure-specific positive instructions about shapes, layering, rhythm and relationships instead of accumulating generic prohibitions.

## Figure-specific brief

```text
Document context: [Chinese dissertation / English conference or journal paper; destination chapter/section and intended placement].
Visible text language: [Chinese / English / explicit project convention; preserve specified names, acronyms and symbols].
Purpose: [what this figure lets the reader understand].
Source of mechanism: [verified paper section and facts].
Reference roles: [image A supplies layout; image B supplies mini-DAG style; facts come from the manuscript].
Composition: [main visual anchor, reading order, relative scale, open areas and local expansions; explain where the eye enters and what relationship stands out].
Palette and rendering: [actual colors assigned to context regions, object identities and focal relationships; mix light, medium and strong colors with deliberate area and adjacency; light/dark balance, label contrast, outline treatment, perspective and permitted depth].
Selected component constructions: [for each key object, name the selected term/variant and describe its silhouette, visible parts, spatial organization and attachment points; IDs belong in the record, not the image].
Meaningful small objects: [what each region contains and why; icon-only identity or local structural expansion].
Logo/icon attachment: [actual object, title/boundary/interface, asset or text placeholder, connector endpoints].
Interfaces: [source → destination, payload/action, arrow style].
Required labels and values: [short exact list; omit redundant writing-organization subtitles and production-status text].
Invariants: [a few scientific facts that must remain true].
Exclude from this figure: [details assigned to another figure].
Output: [requested image format and intended use; review happens after generation, not by declaration in this prompt].
```

Keep early geometry flexible. Freeze stable semantics first. List intended visible labels and their language; recipe IDs, planning headings and review metadata are not figure labels. Reserve strict text whitelists for tightly constrained edits; do not overconstrain a first composition with every coordinate and micro-label.

## Overview pattern

Use when the paper has workload, prediction, scheduling and execution relationships:

```text
Create a compact overview: small workflow DAGs on the left; two shallow prediction/scheduling regions in the middle; concrete model/request/resource objects on the right. Keep module relationships prominent and move algorithm detail to separate mechanism figures. Show a small prediction output record and a symbolic action table if the paper defines them. Distinguish actual commands from candidate comparisons. Show preparation/binding and feedback only as supported by the current system. Use a small shared model identifier where sufficient, repeating identifiers only where separate panels or deployments need them. Avoid equal-height empty panels.
```

## Decision and lifecycle patterns

```text
Decision comparison: use the same candidate request and workflow in both panels. Show different resource contexts, the relevant interference/slack, and the unique chosen outcome. Existing and added work have stable encodings. Numeric illustration must be explicitly labeled; axes and bar lengths must agree if quantitative. Do not invent values.
```

```text
Lifecycle: move the same focal request through paper-defined states. Show preparation, active occupancy and release with different slot treatments. Separate decision instants and asynchronous execution. A candidate is outside pre-existing occupancy until inserted. A released slot is empty. Shared immutable records remain one record feeding multiple consumers when that is the actual design.
```

## Targeted revision

```text
Revise the supplied image to fix [related defects]. Preserve [accepted layout, identities, labels and mechanisms]. Change [specific objects or connections]. The resulting figure must satisfy [observable corrected conditions]. Inspect the entire result for unintended changes.
```

A user request to correct several related errors may be one edit; do not force one generation per typo. If overall structure is wrong, redraw composition rather than patching its colors. After generation, inspect pixels: prompts do not certify correct arrows, arithmetic, glyphs or text. Keep the exact prompt and reference provenance with the version record.

## Compose from the component library

Use the [topic index](topic-index.md) to choose a construction at the appropriate detail level. Integrate its silhouette, parts, spatial organization, edges and emphasis into one figure-specific prompt. Do not concatenate full term cards or pass historical user-feedback and source-review records as image instructions. Adapt cross-topic samples to verified paper facts.

A source URL or written reference review is not an image input. If the actual source image was not supplied to the generation tool, record that the prompt used a textual construction only. Keep source inspection, recipe selection and output review as separate states. Use real data and plotting tools for measured results; component generation cannot supply experimental evidence.

For cross-language redrawing or dissertation adaptation, use [document contexts](document-contexts.md). Include exact translated labels, preserved semantic relationships and the supported scope of expansion. Reflow the composition to fit the target language and document.

## Generate a component before composing the figure

Use GPT Image or the currently available authorized image generator when a custom silhouette or visual treatment would improve an object. This route applies to any component, not only GPUs. Read the relevant recipe as semantic context, then design beyond it as needed. Show the actual component prompt before calling the tool. Request true transparency through the tool parameter when producing a transparent cutout; do not draw a checkerboard to simulate transparency.

Use this brief with actual task-specific choices:

```text
Create one isolated [object] for [role in the target scientific figure].
Depict [chosen silhouette and view], with [visible parts, proportions and spatial relationships].
Match [target palette with actual colors, outline character, depth, lighting and neighboring component style].
It will appear at [approximate size relative to the figure]; preserve [recognizable features] at that scale.
Leave [specific attachment areas] clear for connectors placed during composition.
Use a transparent background and keep the entire silhouette inside the image.
Visible text: [none, or the small set of necessary fixed labels]. Add variable labels and semantic arrows during composition.
Scientific scope: [identity-only schematic or supported structure; identify illustrative geometry].
Reference input: [actual attached image and properties to preserve, if supplied].
```

Inspect the generated element at its intended size and show it inline. Check recognizability, proportions, unwanted text, invented structure, edge quality, transparency and compatibility with neighboring objects. For substantive changes, show the revised prompt before another generation. Keep retries proportional to the task; do not generate a full asset library when a few elements suffice.

For whole-image generation, supply the chosen element through the tool's reference-image mechanism and specify which features must remain. Inspect whether they survived. For source composition, place it as a separate asset and keep labels and connectors separate. Editable draw.io/PPT delivery may directly use independent raster cutouts with native labels and connectors; no extra hybrid-format approval is needed. Reconstruct constituent shapes only when fully vector or internal-part editability is explicitly requested. Save the actual element prompt and its relationship to the composed figure.
