# Systems Figure Studio

[中文说明](README.zh-CN.md) · [Skill](SKILL.md) · [Recipe browser](guide.html) · [Worked examples](examples/showcase.md)

Design, generate and redraw computer-systems and AI Infrastructure paper figures from manuscript evidence. Supports conference papers, journal articles and doctoral dissertations in Chinese or English, complete image generation, custom component generation, and editable draw.io/WPS/PPTX compositions.

![Training, inference and Agent workflow illustration](assets/visual-library/mixed-task-scenes-unified.png)

*Illustrative project example, not measured data. KV retention during tool waits is one example policy. See the worked example for its input, exact revision prompt and limitations.*

## What it includes

- Topic recipes, stable variants, source records and protected Agent extensions. Current counts are generated from [catalog statistics](catalog/statistics.json).
- Automatic document/language selection from the destination section and captions; explicit user language choices take precedence over inference. Chat language does not determine figure labels.
- Paper-grounded composition, visible prompt disclosure before drawing, varied component shapes and coordinated palettes.
- GPT Image/custom-element workflows and a small separate visual asset collection.
- Hybrid editable documents: generated image elements plus editable labels, connectors and layout. Full internal vector reconstruction only when requested.

## Install locally

Use the repository root as the skill folder; no package build is required. After obtaining this repository, place it at `~/.agents/skills/systems-figure-studio` in an agent environment that discovers that directory. In an environment using a different skill root, place the same folder there. Do not install duplicate copies in multiple discovery roots.

Clone directly into the local skill directory (the destination must not already exist):

```bash
git clone https://github.com/Jinghao-coding/systems-figure-studio.git ~/.agents/skills/systems-figure-studio
```

For an existing installation, review local changes with `git status` and update with `git pull --ff-only` from that directory. Do not overwrite local edits.

The folder must contain `SKILL.md`, `topics/`, `references/`, `catalog/`, `assets/` and `scripts/`. Start a new chat or refresh the skill catalog if the host has not detected it. This repository does not install image APIs, editor plugins or credentials automatically.

## Use

```text
Use $systems-figure-studio to design a mechanism figure for the attached paper section.
Show the composition, selected component constructions and complete prompt before drawing.
Use English labels and preserve the paper's actual data flow.
```

```text
Use $systems-figure-studio to redraw this figure for my Chinese dissertation.
Generate custom components where useful and deliver an editable PPT with separate
image elements, labels and connectors. Preserve the mechanism and show the prompt first.
```

Reading/planning needs only manuscript access. Generating images needs an available, authorized image tool; specifying GPT Image in text does not install or select a backend. draw.io/WPS/PPTX editing requires a suitable editor integration or file-generation tool. The skill does not ship an MCP server. Output quality and supported formats depend on the actual tools available.

## Validate and maintain

Python 3.10+; index generation and structural validation use only the standard library:

```bash
python3 scripts/rebuild_navigation.py
python3 scripts/validate.py
python3 scripts/check_history.py
python3 scripts/check_release.py
python3 -m unittest discover -s tests -v
node --test tests/test_browser.cjs
python3 scripts/evaluate_behavior.py
python3 scripts/check_generated.py
```

Pillow is optional for `crop_white_margin.py`; PyMuPDF is optional for PDF auditing in `audit_vector_figure.py`. Install optional dependencies in a project virtual environment, not globally. Their use is not required for recipe lookup or the default image-tool workflow.

Edit `topics/*.md` as the recipe source, then rebuild the catalog and offline guide. Structural validation does not certify image quality. See [contribution guidance](CONTRIBUTING.md), [release checks](RELEASE_CHECKLIST.md) and [source notices](THIRD_PARTY_NOTICES.md).

## License and status

Version 0.1.1 makes bundled assets optional design references and adds Agent runtime/workspace examples. Choose reuse, adaptation, new image generation or native drawing according to the figure; existing assets do not prevent new generation. Original project text/code is MIT licensed; external works retain their own terms. Asset limitations are explicit in [asset terms](assets/visual-library/RIGHTS.md). Historical reference review is separate from generated-output approval. SKILL.md is the single English execution entrypoint. Most topic recipes and supporting references remain Chinese; the introductory documentation is bilingual, and figure labels follow the target manuscript's Chinese or English language.


## Offline browser and production routes

Open `guide.html` directly. Search Chinese names, English terms and aliases across entries, variants, Agent extensions, composition examples and rules. Copy one construction, a whole entry, or up to eight selections with their roles/endpoints/boundaries. Hash links retain topic, query, term and variant selection. Unreviewed metadata and missing examples remain visible.

Image generation, draw.io and WPS/PowerPoint are supported routes; actual invocation follows the host tools. “Show the prompt first” discloses then continues authorized drawing; “draw after confirmation” waits. Local edits preserve the rest of the design. Review requests do not generate images.

Core Python tooling uses the standard library; browser logic tests require Node.js 18+. Optional exporter/PDF tests: `python3 -m unittest discover -s tests/optional -v` (missing dependencies are skipped). Set `DRAWIO_BINARY` to opt into a real local draw.io export test. It checks the exporter, not GUI editing.

The new cross-topic trial images were withdrawn after user review. [Three scenario inputs](examples/scenarios/README.md) and [behavior evaluation fixtures](evaluations/README.md) remain; they are not completed visual examples. [Historical examples](examples/showcase.md) retain their original records.

For static hosting preparation, see [deployment](references/static-hosting.md). No public site is claimed. Maintained metadata, generated outputs and historical migration records are separated in [maintenance](references/knowledge-base.md). New work is recorded under Unreleased; the package and inherited knowledge-base versions remain distinct.

See the [local implementation and validation record](evaluations/maintenance-2026-10-05.md) for executed checks and current case status.
