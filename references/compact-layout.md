# Compactness at the final paper width

During image exploration, use this as qualitative guidance. Exact point-size and area measurements apply to calibrated exports or requested native production/integration; do not block raster draft delivery on those measurements.

Compactness means less paper area for the same readable argument. Cropping
white margins, making fonts smaller, and compressing a bitmap's aspect ratio
do not repair a loose internal composition.

## Establish the comparison

Read the actual `\columnwidth`/`\textwidth` and venue typography requirements.
Record source width/height, export dimensions, final placement width and the
smallest rendered type. In the absence of a venue-specific rule, aim for
8–9 pt ordinary labels; a 7 pt exception should be explicit, not accidental.

For an unrotated figure scaled uniformly:

`printed_height = column_width * source_height / source_width`

`printed_font = source_font * column_width / source_width`

Use consistent units, account for group transforms, and verify the exported
PDF rather than trusting source declarations. Prefer designing directly in
final-size points so the minimum type size stays visible during layout.

When comparing alternatives, hold paper width and typography constant.
Measure figure-plus-caption height if captions differ. Report the actual
change; do not promise an arbitrary percentage before seeing the topology.

## Recover useful area

Diagnose the largest empty rectangle or strip first. Ask whether it expresses
a real boundary, independent paths, or space for a necessary connector. If
it does not, move the connected semantic group into that area.

Typical repairs:

| Symptom | Structural repair |
|---|---|
| Tall serial stack in an architecture | Put persistent state and its controller side by side; separate component topology from algorithm order |
| Several metadata boxes say the same thing | Use fields of one job/state record |
| Long U-shaped telemetry loop creates an empty strip | Move observed resource/state closer or allocate a narrow port corridor; preserve origin and target |
| Worker frame mostly repeats deployment prose | Remove it if ownership remains clear; otherwise shrink it to the actual owned resources |
| Dense labels but large gaps between boxes | Tighten labels and gaps before changing type or allocating both columns |
| Every module has a subtitle | Retain only subtitles needed to decode the figure; put the rest in caption/body |
| Huge job stack or GPU drawing | Reduce it to the smallest truthful resource/queue primitive, keeping multiplicity explicit |
| Smaller raster but unchanged paper whitespace | Inspect TeX float glue, lists, caption height and column balancing separately |

Size boxes from measured text plus consistent padding. A useful starting
point at 8–9 pt type is 3–5 pt interior padding and 6–12 pt between neighboring
objects; change these to fit ports, labels and stroke widths. These are design
starting points, not universal acceptance thresholds.

Align genuine peers; do not force records, resources and services into one
uniform card grid. Prefer a few short orthogonal connections, but never erase
a causal dependency just to lower the edge count. Reserve label space along
an edge before routing it. Place labels outside unrelated nodes and maintain
clearance from arrowheads and cylinder boundaries.

## Check before exporting

- Inspect internal whitespace independently of the canvas bounding box.
  A perimeter feedback loop can make a sparse figure's bounding box look full.
- Check corners and spaces between groups for balance. Small coherent decorative
  details are allowed; they should not obscure relationships or merely fill every gap.
- Compare at the actual column width, not just a full-screen preview.
- Verify critical distinctions in grayscale and count the lowest type sizes.
- Recheck arrows after compaction: connections can silently switch ports.
- Trim only uniform outer margins after the composition is accepted.

Preserve useful breathing room. A diagram packed so tightly that data paths
appear connected to a cache-control box has failed compactness even if its
area is small. Compactness and semantic clarity must pass together.
