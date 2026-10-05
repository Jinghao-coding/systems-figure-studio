# Release checks

1. Run the README validation and test commands using the minimum supported Python 3.10. Browser logic tests require Node.js 18+. Use a temporary copy for the missing-generated-file rebuild test; preserve the active worktree.
2. `scripts/check_generated.py` must match all current generated outputs. Core tests also remove generated results in a temporary copy and rebuild twice. Run `check_history.py` without updating protected hashes to silence failures.
3. Review new artifact rights, input provenance, actual prompts and separate semantic/visual/editor/integration evidence. Exclude rejected or reference-only output from completed examples and final-use assets. Confirm image gen, draw.io and WPS/PPTX routes remain accessible.
4. Run optional dependency/export checks when available; distinguish real export from GUI editing and target-paper integration. Read the behavior evaluation record rather than treating static fixtures as successful Agent runs.
5. Keep package VERSION separate from inherited knowledge-base version. Review git status, final diff, assets and generated files. Remote push, release tags and public deployment require the owner's explicit instruction.

CI performs core rebuild, general validation, historical protection, Python/JavaScript tests and generated-file consistency. Hosted CI results are reported only after an actual hosted run.

Write release descriptions around concrete changes, usage and completed validation results. Describe known issues affecting use with their impact and resolution. Local tests and static staging are not a deployed site.
