# Static hosting preparation

The guide works by opening `guide.html` locally. Its scripts, styles and search payload are embedded; no CDN, account, database or network search service is needed. External source links require a network connection.

For ordinary local browsing, open the maintained `guide.html` directly; do not create a second site/skill tree. For an authorized publication, run the rebuild and README checks, then `python3 scripts/prepare_site.py --output /path/outside/repository/new-temporary-site`. The destination must not already exist and must be outside the maintained repository. It includes relative documentation/artifact links. Remove this temporary bundle after use; it is not another maintained skill installation. The Pages workflow uses its runner's temporary directory. This command does not deploy.

The optional GitHub Pages workflow is manual-only (`workflow_dispatch`). After explicit owner authorization, configure the repository Pages source as GitHub Actions, review the bundle, then manually run “Publish static guide”. The workflow publishes only the staged static files and uses the GitHub Pages environment. It is not triggered by push or pull request. No public URL is advertised until a real deployment succeeds.

Hash state uses `topic`, `q`, `term`, `variant` and `doc`, compatible with local files and static hosting without rewrite rules. Old term hashes are retained. Complex Markdown/HTML is displayed as safe text rather than executed; the renderer supports headings, lists, code, tables and links.
