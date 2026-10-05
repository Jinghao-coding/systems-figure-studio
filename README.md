# Systems Figure Studio

**English** | [简体中文](README.zh-CN.md)

An agent skill for computer-systems and AI Infrastructure research figures. Turn manuscript evidence into architecture diagrams, mechanism figures, resource views and execution timelines for papers and dissertations.

**Manuscript → explanatory question → concrete constructions → objects and relationships → generation and revision → requested editable delivery → validation.**

[Skill entrypoint](SKILL.md) · [Offline recipe browser](guide.html) · [Examples and inputs](examples/showcase.md) · [Changelog](CHANGELOG.md)

## What you can do

- **Choose or review a figure:** look up constructions, compare variants and critique an existing figure without generating an image.
- **Draw or structurally redraw:** select manuscript-grounded objects and relationships, then generate, inspect and revise.
- **Make local changes:** edit labels, colors or connectors while preserving the rest of the accepted design.
- **Deliver editable work:** use draw.io or WPS/PowerPoint (PPTX), including independent generated assets with native labels and connectors. Rebuild internal geometry when full-vector or internal-editability requirements call for it.

The library covers models, inference, hardware, storage, prediction, scheduling, training, reinforcement learning, Agents, systems software, Kubernetes and observability. Stable variants include selection metadata and source links. See [generated statistics](catalog/statistics.json) for current coverage.

Color guidance includes twelve mixed palettes combining light context colors, medium object colors and stronger accents, alongside the earlier soft and vivid options. After drawing or recoloring, the agent inspects the actual figure for hierarchy, color balance, spacing, forms and target-size readability, then repairs observed problems within scope. See [palettes](references/visual-system.md) and [visual review](references/visual-quality.md#aesthetic-review).

## Install

### First installation

You need Git and an agent host that can load `SKILL.md`. This repository requires no package build or API key for installation. For a host that discovers `~/.agents/skills`, clone directly into that directory:

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/Jinghao-coding/systems-figure-studio.git ~/.agents/skills/systems-figure-studio
cd ~/.agents/skills/systems-figure-studio
```

The destination must not already exist. If you already have this checkout, use it as the single maintained installation. For another host, use its configured skill discovery directory; do not clone or copy the skill into multiple discovery roots. Refresh the host's skill list or start a new chat if needed.

The root `SKILL.md` and its sibling directories must remain together. Copying only `SKILL.md` loses the recipes, references and assets.

### Update an existing installation

```bash
cd ~/.agents/skills/systems-figure-studio
git status --short
```

If there are local changes, review and preserve them before updating. With a clean working tree:

```bash
git pull --ff-only
```

If Git reports diverged history, resolve that history before retrying. Do not reset or overwrite local work. Normal browsing uses the root `guide.html`; a second site build or skill installation is unnecessary.

### Tools needed for each route

| Task | Requirements |
| --- | --- |
| Read recipes, select variants, review material | Agent with access to the manuscript and skill files |
| Browse offline | A local browser; open `guide.html` directly |
| Generate a full figure or custom asset | An available, authorized image-generation tool such as the host's image gen capability |
| Create/edit/export draw.io | Suitable draw.io integration, editor or native-file tooling |
| Create/edit/export WPS/PowerPoint | Suitable WPS/PowerPoint integration or PPTX-generation tooling; the target editor for editor validation |
| Rebuild and run core checks | Python 3.10+; standard library only |
| Run browser logic tests | Node.js 18+ in addition to Python |

The skill supplies instructions and resources. It does not install image services, MCP servers, editor integrations or credentials. Available tools determine the executable route. Tool-specific setup and delivery checks are in [editable production](references/editable-production.md).

## Quick start

In a host supporting named skill invocation, use `$systems-figure-studio`. Otherwise ask the agent to read the installed `SKILL.md`. Attach the relevant paper section, caption, existing figure or explicit system assumptions.

**Choose a construction without drawing:**

```text
Use $systems-figure-studio to compare suitable constructions for this scheduling
mechanism. Explain the objects and relationships. Do not generate an image.
```

**Create a figure:**

```text
Use $systems-figure-studio to draw a mechanism figure from the attached paper section.
Use English labels. Show the composition, concrete object constructions, palette and
complete prompt first, then generate and inspect the figure at the intended paper width.
```

**Make a local edit:**

```text
Use $systems-figure-studio to change only “Request” to “Job” and “Device” to “GPU”.
Preserve all other labels, objects, colors and layout.
```

**Request editable delivery:**

```text
Use $systems-figure-studio to adapt this figure for a Chinese dissertation chapter.
Follow the chapter terminology and deliver a draw.io source plus a preview.
Keep key labels and relationships editable; preserve the supplied mechanism.
```

You can instead request WPS/PowerPoint (PPTX). State which parts need independent editing. Generated image internals remain raster unless reconstructed; for PPT, prefer a small number of useful editable objects. “Show the prompt first” means disclose and continue authorized drawing; “draw after my confirmation” means wait.

## Browse and reuse locally

Open `guide.html` from the checkout in a browser. It contains its own search data, scripts and styles, with no CDN or backend. On macOS, `open guide.html` opens it in the default browser. On other systems, open the file directly.

Search Chinese names, English terms and aliases across entries, variants, Agent extensions, combination recipes and rules. Copy a single construction, a whole entry, or a short composition note from up to eight selections. URL hashes preserve topic, query, term and variant. External source links require network access.

[Historical examples](examples/showcase.md) retain their production records. [Three cross-topic scenario inputs](examples/scenarios/README.md) are available for new work; they currently have no accepted complete diagrams. Asset eligibility and review status are tracked separately from recipe readiness.

## Maintain and test

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

## Version and license

[VERSION](VERSION) identifies the standalone skill release; [import metadata](catalog/import.json) records the inherited knowledge-base version separately. Changes awaiting a release are listed under Unreleased in the [changelog](CHANGELOG.md).

Original project text and code use the [MIT license](LICENSE). External works retain their own terms; see [third-party notices](THIRD_PARTY_NOTICES.md) and [asset rights](assets/visual-library/RIGHTS.md).
