# Editable document production — only when requested

Do not load this route merely because an image draft was accepted. Manual redrawing by the user is a valid endpoint.

## Choose one authoritative source

Use the user's editor when specified. Otherwise prefer the existing figure
source and its exporter. For a new figure, live-text SVG is a practical
portable default. Native draw.io XML offers convenient GUI editing; TikZ
suits a TeX-centered workflow. Use PPTX only when that is the intended editor.
Do not generate every format by default.

## Prefer a small number of editable slide objects

For PowerPoint/WPS figures and decks, keep the editable object count as small as practical. Two or three main objects are a useful starting point, not a hard limit. Keep titles, body text and the few parts likely to change editable; insert complex illustrations as one complete image or a few coherent image regions. Preserve meaningful detail and readable labels inside those images. Do not split artwork, arrows, borders, icons or individual words into dozens of native objects just to maximize editability. Grouping dozens of child shapes does not reduce the underlying object count. Use a native table or chart as a single object when its data needs editing. Full internal reconstruction applies only when the user explicitly requests it. Preserve unrelated content during local edits.

Before drawing, choose which few objects need independent editing. At delivery, inspect both top-level objects and nested group members, and consolidate unnecessary fragmentation. Do not add objects to reach a minimum count or remove necessary information to meet an arbitrary cap. This preference takes precedence over default fine-grained reconstruction in the references for PPT output.

For PPTX, the small-object workflow above governs the granularity of the following guidance. Whole diagrams may remain images with a few editable overlays; the per-component and native-label requirements below apply to other formats or explicitly requested fine-grained PPT reconstruction.

## Choose the required level of editability

A request for editable draw.io or PPT normally permits independent generated image elements alongside native labels, shapes and connectors. Importing these elements is a supported production route, not an exception requiring another approval. Only an explicit full-vector or internal-part-editability requirement calls for rebuilding each element as native geometry.

Keep one generated component per image object, preserve transparency and aspect ratio, and embed assets when supported so the document does not depend on temporary paths. Place labels, state overlays and relationship arrows separately; group related parts for convenient movement. Verify the saved document preserves the images and permits independent movement, resizing, replacement and label editing. State that an image object's internal pixels are not individually editable shapes. Do not flatten the whole diagram into one image.

The source must expose individual semantic objects and labels at the requested level:


- **SVG:** live `<text>`/`<tspan>`, native paths and shapes, stable IDs, logical
  groups. No full-canvas `<image>` or hidden HTML screenshot.
- **draw.io:** native cells with editable labels and source/target-connected
  edges, plus independent image cells for generated components. A pasted SVG/PNG is an editable image object, not a reconstruction of its internal geometry.
- **TikZ:** named nodes/coordinates and editable labels/paths; include the
  compilable source and its dependencies or build command.
- **PPTX:** a small number of native text/table/chart objects and coherent picture objects, at the selected editing granularity. Whole-figure images are supported; expose internal parts only when explicitly requested.

Use a shared layout specification or one source exporter for PDF and any
optional raster rendering when practical. Avoid hand-maintaining independent
geometries that drift.
Document which source is authoritative if both a generator and editable
export are delivered; regeneration may overwrite direct edits to the export.

## Raster concepts and reference images

An image-model draft can suggest composition, but the paper and accepted
semantic contract determine topology. Keep records, labels and connectors native; resources may be separate generated image objects unless full internal editability is requested. Do not trace noisy raster borders or turn
text into hundreds of contour paths. Do not copy a generated arrow error
merely to match the reference image.

An intentional photograph, heatmap, or generated component asset can coexist with vector annotations when a hybrid deliverable is appropriate. Keep each asset separate, declare its role and pixel-level editability limit, and keep labels/connectors native. If the user requires fully native editable schematics, reconstruct generated components as individual shapes instead of embedding them. A PDF containing an embedded PNG is not a fully vector export of the architecture.

## Precision and editing

- Use named nodes, ports and connectors; keep an edge inventory with relation
  type and source/target IDs. Do not identify a connection only by color.
- Avoid lines through unrelated nodes; use explicit junction dots only for
  real fan-in/fan-out. A crossing is not a junction.
- Keep control metadata separate from data delivery and telemetry. Endpoint
  errors remain scientific errors even when the figure looks polished.
- Use font metrics for text fit and calculate the final-paper font size.
  Preserve live text in source and selectable text in PDF; embed fonts in PDF
  when supported. Report substitutions and recheck widths.
- Keep revision artifacts separate from accepted paper figures until the
  requested integration step. Reopen the source in the intended editor when
  available and confirm a label and a connector can be edited separately.
  XML parsing alone does not prove editor round-trip fidelity.

## Export and evidence

When PDF output is requested, export it from the authoritative source and use it directly for preview. Describe it as hybrid when it includes raster components; claim fully vector output only when verified.
If a visual inspection tool needs a raster image, render a temporary image
from that same PDF or source. For this native-production route, deliver a raster preview when it helps inspection or is requested. The normal image-first workflow delivers the generated image. Check labels, vector content and
fonts in the PDF. At final placement,
`font_final = font_in_export * column_width / export_page_width` for an
ordinary uniformly scaled figure. Apply additional TeX scaling if present.

Run the lightweight audit for SVG/PDF delivery:

```bash
python scripts/audit_vector_figure.py \
  --svg figure.svg --pdf figure.pdf \
  --column-width-pt 240 --min-font-pt 8 \
  --require-label Scheduler --output audit.json
```

The script uses Python's standard library for SVG and requires PyMuPDF only
when a PDF is supplied. Resolve dependencies through the available workspace
runtime; do not assume an interpreter has them installed.

It detects missing live text, duplicate IDs, raster image elements, missing
required text, empty PDF path/text content and too-small PDF fonts at the
specified column width. `--allow-raster-assets` permits an explicitly intended
raster inset; the report still records the count. Outlined source labels are not editable text. A display PDF may use outlined glyphs if explicitly needed for export compatibility, provided the authoritative source retains editable text; report that exception. The script does **not** establish correct ownership,
meaningful grouping, edge attachment, unobstructed routing, whitespace
quality, editor compatibility, font licensing, or paper integration. Those
require source inspection and rendered/editor evidence.

Deliver the authoritative source, vector PDF, and a concise record of checks
and any remaining limits. The PDF is the default preview; a separate PNG is
optional. Never use a file extension as evidence of editability.

The script accepts SVG, PDF, or both; other source formats require their native checks. `structure_checks_passed` covers only the supplied artifacts. SVG required labels match whole normalized text elements; PDF label search remains extracted-text substring matching. Missing object IDs, partial outlining and raster inset scope still need manual inspection. `--allow-raster-assets` is a broad override, not an inset-size validator.
