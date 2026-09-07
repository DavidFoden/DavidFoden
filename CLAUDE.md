# CLAUDE.md

This repository hosts two unrelated things:

- The GitHub profile README (`README.md` and the images beside it). Leave these alone.
- **Standing Order**, a real-time co-op game, under `standing-order/`.

For any work on the game, read `standing-order/CLAUDE.md` first. It is the authoritative agent
instruction file; everything it references lives relative to `standing-order/`.

The one architectural rule, stated here so it is never missed: **Core is plain C# with no Unity
references.** The simulation in `standing-order/core/` must build and test with `dotnet test` and
no engine installed.

CI lives at the repo root (`.github/workflows/core-tests.yml`) because GitHub only reads workflows
from there. It runs the headless suite in `standing-order/core/StandingOrder.sln` on every push.
