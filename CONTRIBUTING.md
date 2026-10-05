# Contributing

Edit the relevant `topics/*.md` body; do not duplicate recipe prose into JSON. Preserve term IDs and anchors. Register stable variant IDs/selectors in `catalog/variants.json`; renaming a heading updates its selector, never its ID. Reviewed selection metadata needs suitable/unsuitable questions, level, connection endpoints and a boundary source. Unknown fields remain explicitly unreviewed. See [maintenance](references/knowledge-base.md) and the [term template](templates/term-card.md).

Independent term provenance belongs in `catalog/term-provenance.json`; new source records belong in `catalog/sources.json`. Generated index/statistics/browser data are never input authorities. Run all commands in the README after editing; do not manually patch guide.html. Browser source lives in `scripts/web/`. Add focused tests when changing parsing, search, copy/export, source handling or validation.

For visual artifacts, retain actual inputs, prompt/native instructions, revisions, source rights and separate structural, semantic, visual, editor and integration checks. Register complete cases with reciprocal variant links. Retain separate readiness/review/final-use/acceptance states. Do not fabricate old prompts or carry previous user acceptance into new output. Reference-only, truncated or superseded assets stay searchable but excluded from default final-use selection.

Protected Agent bodies and their recorded hashes must not change without explicit authorization. Keep added metadata outside those bodies. `scripts/check_history.py` verifies the inherited source and legacy link contract separately from general validation. An authorized future change needs its actual authorization and provenance recorded; a new hash alone is not approval.

No paid generation, credentials, publication or deployment is needed for default CI. Optional editor/dependency tests are separate and report skipped when unavailable. Behavioral fixtures need actual Agent runs to produce behavioral results; fixture validation only checks their structure.
