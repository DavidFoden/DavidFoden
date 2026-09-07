# Standing Order — Setup Runbook

*From nothing to a green test suite and a working agent. v0.1.*

Follow in order. Each phase ends with a check — do not proceed past a failed one.

Total: roughly half a day of your time, most of it waiting for downloads.

---

# Phase 0 — Installs

| Tool | Notes |
|---|---|
| **Git** | Plus `git lfs install` afterwards |
| **Unity Hub** | Then install the **latest LTS** from within it. Add the **Universal Render Pipeline** template and your build platform module |
| **.NET SDK** | Current LTS. This is what runs the headless tests, independent of Unity |
| **An IDE** | Rider or Visual Studio. VS Code works |
| **Claude desktop app** | For Claude Code with computer use |
| **Wwise** | *Not yet.* Phase 8 |

**Check:** `git --version`, `git lfs version`, `dotnet --version` all respond, and Unity Hub lists an installed LTS editor.

---

# Phase 1 — The repository

Create the repo and this structure. Empty folders need a `.gitkeep`.

```
standing-order/
  CLAUDE.md
  README.md
  .gitignore
  .editorconfig
  docs/
  prototype/
  core/
    StandingOrder.Core/
    StandingOrder.Core.Tests/
  adapter/
  unity/
  tools/
  .github/workflows/
```

Then, before a single binary file exists:

```
git lfs install
git lfs track "*.png" "*.jpg" "*.psd" "*.wav" "*.ogg" "*.mp3" "*.fbx" "*.blend" "*.bnk"
git add .gitattributes
```

**Check:** `.gitattributes` exists and is committed.

---

# Phase 2 — Documents in place

Copy in:

- Every `standing-order-*.md` and `00-MASTER-standing-order.md` → `docs/`
- `CLAUDE.md` → repo root, **not** `docs/`. Claude Code reads it from the root automatically
- `deepholt_simulation.html` → `prototype/`
- `00-index.md` → `docs/`

**Check:** `CLAUDE.md` is at the root, and `docs/` holds the master plus the companions.

---

# Phase 3 — Core, before Unity exists

This is deliberate. Core is built and tested **without the engine**, so the boundary is physical rather than a rule people remember.

```
cd core
dotnet new classlib -o StandingOrder.Core
dotnet new xunit   -o StandingOrder.Core.Tests
cd StandingOrder.Core.Tests
dotnet add reference ../StandingOrder.Core/StandingOrder.Core.csproj
cd ..
dotnet new sln -n StandingOrder
dotnet sln add StandingOrder.Core/StandingOrder.Core.csproj StandingOrder.Core.Tests/StandingOrder.Core.Tests.csproj
dotnet test
```

**Check:** `dotnet test` runs and passes with zero tests. That is your foundation.

---

# Phase 4 — CI

A workflow in `.github/workflows/` that on every push runs `dotnet test` against `core/StandingOrder.sln`.

Nothing about Unity. Nothing about builds. Just the tests.

**Check:** push a deliberately failing test, watch CI go red, remove it, watch it go green. **Do not skip this** — an unverified CI is worse than none, because you will trust it.

---

# Phase 5 — The Unity project

In Unity Hub, create a **3D (URP)** project at `unity/`.

Then, before anything else, in the editor:

| Setting | Where | Value |
|---|---|---|
| Asset Serialization | Project Settings → Editor | **Force Text** |
| Version Control Mode | Project Settings → Editor | **Visible Meta Files** |
| Enter Play Mode Options | Project Settings → Editor | **Leave domain reload ON** |
| Colour Space | Project Settings → Player | **Linear** |

Delete the sample scene content. Create `Assets/Scenes/`, `Assets/Scripts/`, `Assets/Audio/`, `Assets/Art/`, `Assets/UI/`.

**Check:** committing the project produces text-readable `.asset` files, not binary blobs.

---

# Phase 6 — The boundary

Two pieces:

**In Unity**, create an assembly definition for presentation scripts — `Assets/Scripts/StandingOrder.Presentation.asmdef`. Anything that touches Unity lives inside it.

**Reference Core as a compiled library.** Build `StandingOrder.Core.dll` and place it under `unity/Assets/Plugins/`, or use a build step that copies it there. **Do not** copy the Core source into `Assets/Scripts` — the moment it lives there, someone adds `using UnityEngine` and the headless tests die.

**Check:** delete the Unity folder entirely and `dotnet test` still runs. If it doesn't, the boundary is broken.

---

# Phase 7 — Connect the agent

Open the Claude desktop app, Code tab, and point it at `standing-order/`. Grant that folder and nothing else.

It will read `CLAUDE.md` automatically. Confirm it has by asking it to state the project's architecture rule — it should say Core has no Unity references without being told.

**The first session prompt:**

> Read CLAUDE.md and docs/standing-order-project-setup.md. Then implement task A2: the static data tables for 16 chambers, 25 tunnels, 6 latent connections and 4 camps, exactly as specified in docs/00-MASTER-standing-order.md Part 2. Plain C# in Core, loaded from a data file rather than hard-coded, with a validation test asserting no chamber is held by two camps and every tunnel references a real chamber. Do not touch the Unity project.

Then A3, then A4, in order.

**Check:** CI green, and `dotnet test` passes with the new validation tests.

---

# Phase 8 — Wwise, later

Not now. Install it when you reach layer four, and **pin the Unity and Wwise versions together and freeze both** — the integration is version-coupled and upgrading either mid-project is a known time sink.

When you do: the room and portal layout is **generated from the same chamber and tunnel tables Core reads**, by an editor script. Never hand-placed.

---

# The order in one line

Installs → repo and LFS → docs → **Core and tests before Unity** → CI you have seen fail → Unity with correct serialisation → the assembly boundary → the agent → Wwise much later.

---

# What "done" looks like

- `dotnet test` runs from a clean clone with no Unity installed
- CI goes red on a broken test and you have watched it happen
- Unity opens, is empty, and commits as text
- Claude Code knows the architecture rule without being reminded
- The chamber and camp tables are loaded and validated

At that point every later claim in this project is verifiable, which is the entire point of the setup.
