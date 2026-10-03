# Systems Figure Studio

[中文说明](README.zh-CN.md) · [Skill](SKILL.md) · [Recipe browser](guide.html) · [Worked examples](examples/showcase.md)

Design, generate and redraw computer-systems and AI Infrastructure paper figures from manuscript evidence. Supports conference papers, journal articles and doctoral dissertations in Chinese or English, complete image generation, custom component generation, and editable draw.io/PPT compositions.

![Training, inference and Agent workflow illustration](assets/visual-library/mixed-task-scenes-unified.png)

*Illustrative project example, not measured data. KV retention during tool waits is one example policy. See the worked example for its input, exact revision prompt and limitations.*

## What it includes

- 12 topics, 122 terms and 273 textual drawing constructions, with source records and Agent extensions. These counts describe recipes, not 273 rendered assets.
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

Reading/planning needs only manuscript access. Generating images needs an available, authorized image tool; specifying GPT Image in text does not install or select a backend. draw.io/PPT editing requires a suitable editor integration or file-generation tool. The skill does not ship an MCP server. Output quality and supported formats depend on the actual tools available.

## Validate and maintain

Python 3.10+; index generation and structural validation use only the standard library:

```bash
python3 scripts/rebuild_navigation.py
python3 scripts/validate.py
python3 scripts/check_release.py
```

Pillow is optional for `crop_white_margin.py`; PyMuPDF is optional for PDF auditing in `audit_vector_figure.py`. Install optional dependencies in a project virtual environment, not globally. Their use is not required for recipe lookup or the default image-tool workflow.

Edit `topics/*.md` as the recipe source, then rebuild the catalog and offline guide. Structural validation does not certify image quality. See [contribution guidance](CONTRIBUTING.md), [release checks](RELEASE_CHECKLIST.md) and [source notices](THIRD_PARTY_NOTICES.md).

## License and status

Version 0.1.0 is the first standalone release preparation. Original project text/code is MIT licensed; external works retain their own terms. Asset limitations are explicit in [asset terms](assets/visual-library/RIGHTS.md). Historical reference review is separate from generated-output approval. SKILL.md is the single English execution entrypoint. Most topic recipes and supporting references remain Chinese; the introductory documentation is bilingual, and figure labels follow the target manuscript's Chinese or English language.
