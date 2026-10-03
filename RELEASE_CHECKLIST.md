# Release checks

For each release, run the README's three validation commands in a clean copy using Python 3.10+. Check that regeneration produces no changes to index, statistics or guide. GitHub CI automates those same checks; a workflow file is not evidence that hosted CI has run.

Review new assets and prompts for manuscript-specific/private information, third-party content, scientific errors and clear raster/vector declarations. Maintain THIRD_PARTY_NOTICES and asset provenance. Generated examples are illustrative, not performance evidence or a promise of identical image regeneration.

Before publishing, choose the destination GitHub account/repository, inspect `git status`, review the final files, and obtain the owner's instruction to upload. Never infer publication from local repository preparation. Add a release tag only for the version actually being released.

Local preparation does not certify every external license or the live behavior of image tools, draw.io or PowerPoint on a new host. Record those limits in the release description instead of calling them passed.
