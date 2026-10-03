# Conference papers, journal articles and doctoral dissertations

## Infer language from the destination

Document type and language are independent: a conference/journal paper or doctoral dissertation may be Chinese or English. Read the destination section, adjacent captions, manuscript terminology and template. Resolve visible-label language from explicit user instructions first, then destination-section/project conventions, then the main manuscript language. Do not infer it from chat language, the source reference image or the prompt's language. Standard English acronyms within Chinese prose do not call for bilingual labels.

When adapting a source paper into a dissertation, the destination chapter determines labels and scope. Tell the user the inferred document type and label language with the pre-drawing brief; do not ask again when the evidence is clear. Ask only when missing or conflicting destination information materially affects the result.

## Doctoral dissertations

Read the relevant chapter, its role in the dissertation and the surrounding figure references before designing. For an overall research overview, inspect the dissertation's research question and chapter relationships. For a local mechanism edit, the affected chapter context is sufficient.

Support research-problem and chapter-relationship diagrams, background illustrations, system architectures, mechanisms, algorithm workflows, execution timelines, deployment and experimental-setup schematics. Choose a figure because it clarifies a relationship or execution behavior; do not invent a pipeline or dependency among otherwise independent research chapters.

Use concise, natural academic Chinese for a Chinese dissertation and precise English labels for an English dissertation, following destination terminology. Retain defined system names, common acronyms such as GPU and KV Cache, mathematical notation and code identifiers. Reuse the dissertation's terminology, distinguishing tasks, jobs, requests, models and instances. Prefer a term mapping when translating a substantial figure; do not add redundant bilingual labels everywhere.

Keep recurring objects, symbols, colors and arrow meanings consistent across chapters while allowing each chapter's mechanism to determine its layout. A dissertation may need a local expansion, running example or several complementary figures to explain material compressed in a short paper. Add detail only when supported by the manuscript or supplied evidence. Use the actual page/text width and thesis template; extra page space is not a reason for oversized empty boxes.

## Adapt an English paper figure into the dissertation

Inspect both the source figure/caption and the destination chapter. Establish whether the request calls for label translation, faithful reconstruction, composition redesign or explanatory expansion. Infer this from the request and available context; ask only when a consequential ambiguity remains.

Preserve factual objects, direction of relationships, state transitions, quantities and claim strength. Map the source terminology to the destination chapter before drawing. Reflow translated labels and resize local regions to fit Chinese text rather than placing translations over the original bitmap. The destination chapter governs the final explanatory role and current mechanism; surface conflicts with the source figure instead of silently merging incompatible versions.

Retain shared identities across split panels or expanded views. Preserve applicable attribution and source provenance. Record the source-to-target mapping and substantive changes when useful; adaptation does not authorize editing captions, manuscript text or citations unless requested. Save the redraw separately from the original until replacement is requested.

## Conference and journal papers

Use precise Chinese or English labels consistent with the target manuscript. Focus each figure on the relationship needed to support its argument. Use accepted nomenclature and standard abbreviations; keep explanatory prose in the manuscript or caption unless short inline notes are needed to decode the figure.

Derive single-column, double-column or full-width composition from the actual template and intended placement. Conference figures often need compact composition; journal figures may support more detailed multi-panel explanations, but neither is a fixed rule. Inspect the target venue's current official instructions when compliance, dimensions, fonts, file formats or submission requirements are part of the request. Do not infer such requirements from venue reputation.

For a figure set, coordinate symbols, palette, typography and object identity. Revise composition as needed for the target document; a change of venue alone does not justify changing mechanisms or results.

## Prompts and review across languages

Record document type, destination chapter/section, intended label language, exact technical terms and placement width when known. Prompt prose may be in a different language from visible figure text; explicitly specify the visible text language and required labels. Internal planning headings and source metadata must stay outside the figure.

Inspect Chinese characters for missing strokes, garbled glyphs, accidental substitutions and inappropriate line breaks. Inspect English labels for spelling, terminology and capitalization. Check mathematical subscripts, punctuation and mixed Chinese/Latin alignment in both contexts. Native-source production needs fonts with the required glyph coverage and an export check; raster previews still require actual visual inspection. If generation cannot render required text accurately after bounded repair, preserve the best draft and provide the exact replacement labels and unresolved fixes, without calling it final.

For quantitative experimental figures, preserve the source data, units, scales and comparisons. If replotting is explicitly requested, use the existing plotting source or supplied data and deterministic plotting tools; use image generation for schematic content. A screenshot alone does not establish exact experimental values. Distinguish experimental-setup diagrams from measured result plots.
