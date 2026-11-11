# AI Development Log

> One row per significant agent task. Full instructions live in [`/prompts`](../prompts/).

| Version | Agent | Task / Prompt Ref. | Changed Modules | Issues / Corrections | Student Review |
|---|---|---|---|---|---|
| v0.1.0-design | Claude Code (Claude Opus 5.5) | [prompts/v0.1.0-design-architecture.md](../prompts/v0.1.0-design-architecture.md) | `docs/**`, `uml/**`, `src/**` (skeleton only), `data/`, `tools/`, repo config | (1) Native Mermaid `C4Context`/`C4Container` layout overlapped labels → agent redrew as C4-notation flowcharts. (2) A `;` in a sequence message broke the Mermaid parser → fixed. (3) Agent found `rv1 == rv2` and that persistence reaches R² 0.46 → the design gained two model modes (AD-06). (4) The first branch shared no history with `main`, so no PR was possible → commits replayed onto `docs/v0.1.0-design` from `main` (no force-push, old branch kept). | _pending: reviewer name + findings_ |
