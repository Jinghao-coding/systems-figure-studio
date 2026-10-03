# Visual system: coherent objects and composition

## Palette and typography

Compare multiple suitable palettes and their interaction with the current shapes, density and reading path. Existing figures are references, not a permanently preferred palette. Honor an explicit request to preserve a specific color; otherwise select for overall beauty, legibility and document coherence. Reducing excessive colors means consolidating competing semantic roles, not automatically replacing the figure with blue-gray text boxes. There is no universal three-color limit.

The blue/orange palette below is an optional starting point among several palette families; it came from a particular systems-paper iteration, not a venue rule.

| Role | Main | Pale fill |
|---|---|---|
| Ordinary requests / data paths | #4C78A8 | #E8EFF7 |
| Focal request / control / added interference | #D98C3F | #FAEBD8 |
| Text and boundaries | #252A34 | — |
| Background / supporting region | #FFFFFF | #F3F4F6 |
| Optional model layers | neutral outlines | #E9E4F2 |

Use the orange roles only in contexts where object and relationship types make them clear. Do not recolor all preparing requests orange if orange identifies one focal request. Avoid encoding success, novelty and identity indiscriminately with the same fill.

For English labels, use Arial/Helvetica-like sans-serif labels by default. For Chinese labels, choose a compatible CJK family with complete glyph coverage and consistent Latin/math pairing, following the thesis template when specified. Titles are only modestly larger. Preserve an accepted paper font when appropriate. Prefer flat fills, fine outlines and modest headings. Restrained thickness or shading may help distinguish parts; avoid effects that dominate structure. Publication-scale text around 8–9 pt is a production target, not a measurable claim about an uncalibrated generated image.

## Composition

For a new or substantially redesigned figure, select actual constructions from the integrated component topics linked directly in SKILL.md before settling the layout. Read their parts, organization and boundaries; an index entry alone is insufficient. Match the role with an icon, structural expansion, or a combination. Recoloring a generic box does not implement a new construction.

Prefer a compact overview with open workload objects, shallow functional regions and a concrete execution region. One successful option is left workflows, middle prediction above scheduling, right runtime. This is an option for that relationship structure, not a template for every system.

Fit boundaries to content. Use borders for real modules, state, tables, resources or ownership. Omit a decorative canvas frame; a whole-system boundary is legitimate when it communicates scope. Real serial processing may be left-to-right. Matched alternatives may be symmetric. Avoid equal cards when they obscure different object roles, not merely because they are equal.

A little whitespace separates ownership and paths. Repair large unused interiors by moving groups, shortening labels or simplifying scope. Small coherent decorative or personable details are allowed; choose them for the composition rather than filling every gap. Model stacks can use a few offset layers. Keep hardware perspective modest and consistent with surrounding objects; use the detail required for identification or mechanism explanation.

## Arrow vocabulary

| Relation | Default |
|---|---|
| Request/data transfer | Solid directed arrow in the chosen data color; payload label |
| Control/decision | Directed arrow in the chosen control encoding; command label |
| Completion/resource feedback | Gray dashed directed arrow; state/event label |
| Local DAG dependency | Thin charcoal directed arrow within DAG |
| Completion frontier | Charcoal vertical dashed guide, no arrowhead |
| Candidate comparison | Neutral connector or selection mark; no implied dispatch |

Line type, color, arrowheads, location and labels work together. A dashed preparing-slot border is not a feedback arrow. Keep encodings consistent for comparable entities across figures; allow defined context-specific guides. If print/grayscale makes the chosen colors ambiguous, retain explicit payload/command labels and add non-color distinctions where needed.

## Visible text

Use short object/role labels and necessary scientific annotations. Let composition express parallelism, grouping and dependency where it is sufficient. Remove redundant editorial subtitles such as “four parallel studies”; retain words like “design” only when technically informative. Keep explanation in the manuscript, while preserving units, conditions and distinctions needed to interpret the figure.

## Small identifiers

A small logo or product name is allowed when it identifies an actual model, device, engine or framework. It need not be an experimental variable. Use role labels where needed to distinguish model, framework, platform and device. A logo-plus-name endpoint can identify a collapsed object; repetition follows reading needs across instances, panels or deployments. Use accurate assets when available; otherwise use short text or reserve a placement area. Treat any generated approximate mark as an unresolved placeholder to replace or omit. Never import brands from a style reference as deployment facts.

## Consistency

Keep request identity, label scale, model glyphs and arrow semantics coherent across a figure set. Palettes may vary with figure role; preserve color mapping within direct comparisons and continuous views of the same object. Allow geometry to vary with the question: topology, comparison and lifecycle should not all look like the same pipeline. Adopt accepted choices progressively; change them when user feedback or semantics require it.

## Icons and component variants

Read the [component visual guide](visual-quality.md) when selecting icons or combining drawing families. Role avatars, devices, terminals, files and state markers are allowed. Identity-only objects need not expose internal mechanisms; mechanism views may combine an icon with a local structural expansion. Align perspective, stroke density, scale and color roles across the figure instead of turning everything into identical cards. Small personable details are acceptable when they leave the main relationships clear.

For cloud/platform figures, use [Cloud/Logo composition](cloud-logo-composition.md): distinguish a platform logo, resource-type icon and physical device. Place marks with their actual owner; plan storage scope and connector routes together. Do not infer cloud vendors, VPCs or deployment boundaries from a generic recipe.


## Additional palette choices and color roles

These alternatives may complement or replace earlier palettes when they improve the current figure. The blue/green/rose values below are recorded from Chen Liu's [figures4papers API palette](https://github.com/ChenLiu-1996/figures4papers/blob/f0bb7559abe90f5e1828797126d4d133c1bd47d7/scientific-figure-making/references/api.md); the role assignments here are adapted for systems figures. Source and review scope: [reference record](figures4papers-ideas.md).

| Choice | Colors | Useful role |
|---|---|---|
| Blue emphasis with neutral support | #0F4D92, #3775BA, #CFCECE | Focal method/path plus supporting alternatives; keep names and markers |
| Related green variants | #DDF3DE, #AADCA9, #8BCF8B | Variants in one family; lightness alone does not imply better performance |
| Rose comparison | #F6CFCB, #E9A6A1, #B64342 | A second family plus a local accent; red does not automatically mean failure |
| Additional distinct identities | #42949E, #9A4D8E | Additional categories when existing hues cannot distinguish them |

For large mechanism objects, use pale fills and dark readable text; reserve saturated colors for a smaller focal path, marker or outline. For quantitative lines, use sufficient contrast against white; pale fills suited to regions are not automatically suitable for thin curves. Check grayscale and use markers, line styles or labels where hue is insufficient. Do not label any palette colorblind-safe without testing it.

A useful soft mechanism combination can keep blue, green, pale yellow and lilac in separate input branches, with a darker outline or local warm accent. Derive the exact shades from the document's existing palette; this is a compositional option observed in the ImmunoStruct schematic, not a claim of pixel-sampled colors. Match one object's color through its input, representation and output only when identity really persists. Category, rank, state and measured magnitude are different encodings.

For ablations, one hue family and distinct labels can show related variants. Omitted components must be named; fading is not a performance score. Shared legends and stable ordering across metrics reduce decoding work. Avoid automatically painting every baseline gray or red when baseline identity matters.


## Coordinated multi-hue options

The following are independently chosen starting combinations informed by the reviewed examples' color relationships, not sampled source palettes. Use only the roles needed by the figure; do not force every swatch into it.

| Family | Pale object fills | Stronger focal colors | Possible use |
|---|---|---|---|
| Soft multibranch | #D4E5F3 blue, #DEE9CE green, #F7EDC9 yellow, #E5DAEC lilac | #386884, #805B88 | Different input/object families converging on a model or decision |
| Teal and warm sand | #D9EBE7 teal, #F2DFC7 sand, #E4E7EF slate | #39756F, #A46939 | Resource/state diagrams with warm local changes |
| Sage, rose and slate | #DEE7D7 sage, #EDD6DA rose, #DCE3ED slate | #637C51, #A65E6B, #526B8A | Related workloads, actors or alternative mechanisms |
| Blue and lavender with amber | #D7E5F2 blue, #E4DEF0 lavender, #F2E3C6 amber | #3F678E, #766095, #A27C36 | Model identities and a distinct decision/update path |

The first option draws on the multibranch organization in figures4papers; the latter options also reflect muted teal/green, blue/violet and warm evaluation accents observed in Framework Studio examples. They do not impose those examples' scientific roles. A GPU can be sage or slate when that suits the figure; it does not have to be blue. Avoid assigning an ordering or positive/negative meaning to color unless defined. Use dark neutral text, restrained outlines and non-color identity cues. Final visual inspection determines suitability, not a palette name.
