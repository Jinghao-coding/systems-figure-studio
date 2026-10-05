<div align="center">

# Systems Figure Studio

**Make systems mechanisms visible. Turn paper evidence into clear figures.**

A figure-design skill for computer systems and AI Infrastructure, with image generation, draw.io and WPS/PowerPoint workflows.

**English** · [简体中文](README.zh-CN.md)

[Quick start](#quick-start) · [Examples](#examples) · [Recipe library](#library) · [Guides](#guides) · [Changelog](CHANGELOG.md)

</div>

## From manuscript to figure

| Your task | What the skill helps you produce |
| --- | --- |
| Choose a visual explanation | Suitable constructions, object roles and connection choices |
| Draw an architecture or mechanism | A figure grounded in the paper's components, relationships and states |
| Explain execution or resource sharing | Timelines, occupancy views, lifecycle paths and deployment mappings |
| Revise an existing figure | Scoped label, color or connector changes that preserve accepted design |
| Prepare editable delivery | draw.io or WPS/PowerPoint sources with the requested editable elements |

**Bring:** the relevant paper section, a caption, an existing figure or explicit system assumptions. The agent uses its available image-generation and editor tools to produce the requested output.

<a id="quick-start"></a>
## Quick start

### 1. Install for your agent

Send this request to your agent:

```text
Install systems-figure-studio from:
https://github.com/Jinghao-coding/systems-figure-studio

Find the skill directory used by this agent and check for an existing installation.
Reuse that installation and preserve local edits. Otherwise install the complete
repository once, including SKILL.md and supporting resources.
Verify the installed path and explain how to invoke the skill here.
```

For manual installation with Node.js and npm, choose your target agent:

```bash
npx skills@latest add Jinghao-coding/systems-figure-studio --skill systems-figure-studio --agent codex --global
```

For Claude Code, replace `codex` with `claude-code`. Omit `--global` for a project installation. The [skills CLI](https://github.com/vercel-labs/skills) also supports other agents; prefer its symlink option when sharing one installation across tools. Choose one installation method for an existing setup.

<details>
<summary>Git installation and updates</summary>

For a host discovering `~/.agents/skills`, clone into a directory that does not yet exist:

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/Jinghao-coding/systems-figure-studio.git ~/.agents/skills/systems-figure-studio
```

Use your host's configured skill directory if it differs. Keep the full repository together. To update a Git installation, run `git status --short` in that checkout, preserve local changes, then run `git pull --ff-only` with a clean working tree. CLI installations use the CLI's update mechanism instead. Refresh skill discovery or start a new chat after installation when needed.

</details>

### 2. Start with your paper

```text
Use systems-figure-studio to draw a mechanism figure from the attached design section.
Use English labels. Show the composition, object constructions, palette and prompt,
then generate the figure and inspect it at the intended paper width.
```

Codex supports `$systems-figure-studio`; Claude Code uses `/systems-figure-studio`. In other environments, use the host's skill invocation or ask it to read the installed `SKILL.md`. [Claude Code invocation](https://code.claude.com/docs/en/skills).

<a id="examples"></a>
## Common tasks

### Compare constructions

```text
Use systems-figure-studio to compare ways to show GPU sharing in this system.
Explain which objects and relationships each view makes clear. Do not draw yet.
```

### Recolor an existing figure

```text
Use systems-figure-studio to improve this figure's colors while preserving its layout.
Mix soft region fills with clearer object colors and stronger focal accents.
Inspect the rendered result for balance, readability and overall visual appeal.
```

### Change two labels

```text
Use systems-figure-studio to change only “Request” to “Job” and “Device” to “GPU”.
Keep every other object, label, color and position unchanged.
```

### Deliver an editable figure

```text
Use systems-figure-studio to adapt this figure for my Chinese dissertation chapter.
Use the chapter's terminology and deliver a draw.io source plus a preview.
Keep key labels and relationships editable, following the supplied mechanism.
```

You may request WPS/PowerPoint (PPTX) instead and specify which parts need editing. Independent generated images can be combined with native labels and connectors; request full-vector output when image internals also need reconstruction. “Show the prompt first” continues authorized drawing after disclosure; “wait for my confirmation” pauses before drawing.

<a id="library"></a>
## Explore the recipe library

Open the root `guide.html` locally; on macOS, run `open guide.html`. The browser works offline and searches Chinese names, English terms and aliases. Copy a variant, a full entry or combination notes for selected objects. No separate site build is needed.

Topics cover models, inference, CPUs/GPUs, storage, performance prediction, scheduling, training, Agents and Kubernetes. The [palette guide](references/visual-system.md) includes soft, vivid and mixed-strength combinations. The [visual review](references/visual-quality.md#aesthetic-review) checks the actual composition after drawing and recoloring.

Browse [recorded examples](examples/showcase.md), [combination recipes](examples/combined-recipes.md) and [scenario inputs](examples/scenarios/README.md). Each resource records its own state; current library coverage is in [catalog statistics](catalog/statistics.json).

<a id="guides"></a>
## Guides

| Need | Read |
| --- | --- |
| Invoke the workflow | [Skill entrypoint](SKILL.md) |
| Find objects and constructions | [Topic index](references/topic-index.md) |
| Organize layouts and relationships | [Figure grammars](references/figure-grammars.md) |
| Select colors and review appearance | [Visual system](references/visual-system.md) · [Visual quality](references/visual-quality.md) |
| Use image gen or record prompts | [Generation prompts](references/generation-prompts.md) |
| Deliver draw.io or WPS/PPTX | [Editable production](references/editable-production.md) |
| Fit a paper or dissertation | [Document contexts](references/document-contexts.md) · [Validation](references/validation.md) |
| Contribute recipes and tooling | [Contributing](CONTRIBUTING.md) · [Maintenance](references/knowledge-base.md) |

<details>
<summary>Maintainer commands and optional checks</summary>

Run from the repository root:

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

The behavior command validates evaluation fixtures; real agent behavior requires retained execution evidence. Optional exporter/PDF checks run with `python3 -m unittest discover -s tests/optional -v`; missing dependencies are reported as skipped. Set `DRAWIO_BINARY` to opt into real draw.io export testing. Pillow is optional for image cropping, and PyMuPDF for PDF auditing; use a project virtual environment when installing them.

Maintain recipe bodies in `topics/*.md` and independent metadata in the designated catalog source files. Rebuild the index, statistics, browser payload and guide from those sources. See [maintenance](references/knowledge-base.md), [contributing](CONTRIBUTING.md), [validation records](evaluations/maintenance-2026-10-05.md) and [release checks](RELEASE_CHECKLIST.md).

[Static hosting preparation](references/static-hosting.md) uses a temporary bundle outside the checkout. The GitHub Pages workflow runs only when manually triggered; installation and normal pushes do not deploy a website.

</details>

## Version and license

[VERSION](VERSION) identifies the standalone skill release; [import metadata](catalog/import.json) records the inherited knowledge-base version separately. Changes awaiting a release are listed under Unreleased in the [changelog](CHANGELOG.md).

Original project text and code use the [MIT license](LICENSE). External works retain their own terms; see [third-party notices](THIRD_PARTY_NOTICES.md) and [asset rights](assets/visual-library/RIGHTS.md).
