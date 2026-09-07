# Standing Order — Agent Plan

*From an unzipped folder to a working game, with the exact prompts to use. v0.1.*

Keep this open beside Claude Code. Every stage has: what to install, what to say, and how you know it worked.

---

# PART 0 — What "take control" means here

Two different mechanisms, and you mostly want the second one.

**Computer use** — screenshots, mouse, keyboard, driving your desktop like a person would. Impressive, and the wrong tool for most of this. Clicking through the Unity editor is slow and error-prone.

**Local tool access** — Claude Code runs on your machine, reads and writes your files, runs commands, and talks to Blender and Unity through MCP servers listening on `localhost`. This is what actually builds the game.

So "control my laptop" in practice means: **it owns the repo and drives Blender and Unity through their APIs, while you watch and approve.** You keep the editor open and check the work; it does the typing.

---

# PART 1 — The standing context

Paste this at the start of **any** new Claude Code session, once, before asking for work. Everything else it needs is already in the folder.

> This is Standing Order — a real-time co-op game where four camps run a full simulation of ecology, territory, politics and faith whether players are present or not. The simulation is the product.
>
> Read `CLAUDE.md` first, then `docs/00-MASTER-standing-order.md` (the specification — it wins over every other document) and `docs/standing-order-project-setup.md` (the task breakdown).
>
> `prototype/deepholt_simulation.html` is a working JavaScript implementation of layer one and the embodiment model, passing 12 seeds × 1,000 ticks. It is the behavioural reference, not shippable code. If your C# ever produces a different history from the same seed, stop and tell me before tuning anything.
>
> Tell me which task you are picking up and what its acceptance criterion is before you write anything.

**Verification before you trust the session:** ask *"what is this project's one architectural rule?"* It should say Core has no Unity references, unprompted.

---

# PART 2 — The stages

Five stages, in order. **Do not reorder them.** Each depends on the one before being verifiably done.

| Stage | What gets built | Unity open? | Blender open? |
|---|---|---|---|
| 0 | Repo, Core project, CI | No | No |
| 1 | The whole simulation in C# | **No** | No |
| 2 | Sixteen whitebox chambers | No | **Yes** |
| 3 | The real-time shell | **Yes** | No |
| 4 | The legibility gate | Yes | No |

Unity stays closed through stages 0 and 1. `CLAUDE.md` says not to touch it; keeping it shut makes that physically true rather than a rule it might drift from.

---

# STAGE 0 — Foundation

**Install:** Git, Git LFS, .NET SDK, Node, the Claude desktop app. Not Unity, not Blender, not Wwise.

**You do this bit by hand** — it's five minutes and it's the one thing worth not delegating, because everything downstream assumes it's right.

```
cd "Fun Game Stuff/standing-order"
git init
git lfs install
git add .
git commit -m "Project setup: specification set, agent instructions, repo config"
```

Push to a new GitHub repo.

**Then open Claude Code**, point it at `standing-order/`, paste the standing context, and say:

> Set up the Core solution as described in `docs/standing-order-project-setup.md` Phase A task A1: a `StandingOrder.Core` class library and a `StandingOrder.Core.Tests` xunit project under `core/`, with a solution file. Confirm `dotnet test` runs green with zero tests. Do not create anything under `unity/`.

Then, to prove the safety net works:

> Add a deliberately failing test called `Deliberately_Broken`. Commit and push it so I can watch CI go red, then wait for me.

Watch the Actions tab fail. Then: *"Remove it and push."* Watch it go green.

**Done when:** `dotnet test` passes locally, and you have personally seen CI fail and recover.

---

# STAGE 1 — The simulation

**The largest stage and the most important.** Everything here is C# and tests. No engine, no art, no audio.

Work through tasks A2 to A9 one at a time. One session, one task, one commit.

**A2 — data tables:**

> Implement task A2: the static data tables for 16 chambers, 25 tunnels, 6 latent connections and 4 camps, exactly as specified in `docs/00-MASTER-standing-order.md` Part 2. Plain C# in Core, loaded from a data file rather than hard-coded. Add validation tests asserting no chamber is held by two camps, every tunnel references a real chamber, and every camp's seat is among its holdings.

**A3 — determinism:**

> Implement A3: the seeded RNG and the tick loop shell. The acceptance criterion is in `docs/standing-order-unity-notes.md` section 2 — the same seed run twice in two separate processes must produce byte-identical output for 1,000 ticks. Write that as an automated test.

**A4 to A8** — ecology, apex migration, camp sense and score, bands, combat. Each time, name the task and let it read the formulas from master Part 5. The formulas are exact; it should not be inventing any.

**A9 — the sweep:**

> Implement A9: the full invariant sweep from master Part 12, tests 1 through 7 and 25 through 30. Run it across 12 seeds × 1,000 ticks. Report the results as a table, and compare them against the prototype's numbers in master 8.6a.

**Done when:** the thousand-tick no-player test passes 12 of 12 seeds, and the chronicle reads like a history when you print it.

**This is the moment to stop and read a log properly.** If it doesn't read like the prototype's did, something is wrong that tests won't catch.

---

# STAGE 2 — Blender and the chambers

**Now install Blender** and the MCP add-on.

```
brew install uv                        # or: winget install astral-sh.uv
claude mcp add --scope user blender -- uvx blendmcp
```

Install the add-on in Blender (Edit → Preferences → Add-ons → Install from Disk), enable it, start its server from the sidebar.

**Check:** with Blender open, ask Claude Code *"what objects are in the current Blender scene?"*

Then the task that makes this whole setup worth having:

> Blender is open and connected. Read the chamber table in `docs/00-MASTER-standing-order.md` Part 2.2 and the dimensions in Part 9.2. Generate whitebox geometry for one chamber — Grimhollow — as a Blender scene: correct diameter for its `floraCap`, tunnel openings positioned toward its connected chambers, and the verticality treatment described in `docs/standing-order-visual-identity.md`. Export as glTF to `unity/Assets/Art/whitebox/`. Show me before exporting.

Look at it. Adjust the prompt. Then:

> Good. Now generate the remaining fifteen the same way, driven from the table rather than by hand. Keep a script in `tools/` so they can be regenerated when the table changes.

**That last clause is the point.** The chambers become derived from the data, not hand-built — same as the simulation, same as the Wwise rooms later. One authority, three representations.

**Done when:** sixteen whitebox chambers exist, dimensions match the spec, and re-running the script reproduces them.

---

# STAGE 3 — Unity

**Now create the Unity project**, following `WALKTHROUGH.md` steps 8 to 12: Unity 6.3 LTS, URP, Force Text, Linear, AI Assistant package, MCP bridge, Integrations → Configure Claude Code.

Then, in order:

> Task D1. Create a scene with one chamber imported from the whitebox glTF, a first-person controller, and a carried light source. Dark, per the world palette in `docs/standing-order-visual-identity.md`. No HUD. I want to walk around in it and tell you whether the scale feels right.

**Walk around it yourself.** This is the first thing in the project only you can judge — whether 60 to 120 metres feels like a chamber and whether the dark reads as navigable. Everything downstream depends on that answer.

> Task D2. Audio before anything else visual. Set up Wwise, generate the room and portal layout from the chamber and tunnel tables — never hand-placed, per the hard rule in master 9.4 — and get one room tone and one band cue working with graph-based occlusion.

> Task D3. Hook the headless simulation in. Bands as capsules. Ugly and correct: the simulation drives their positions, presentation only interpolates. LOD invariance is test 31 and it matters more than it looks.

**Done when:** you can stand in a dark chamber and hear a war band pass through the next one.

---

# STAGE 4 — The gate

Five people who have not worked on the game. Thirty minutes. Three times you ask: *what is that camp about to do, and why?*

**60% correct, or perception gets fixed before anything else is added.**

Run the silent-play version in the same session — same build, audio off, 50% pass.

**Nothing beyond this stage begins until it passes.** Not the forty beats, not the art pass, not the audio production. That is the whole reason the gate exists.

---

# PART 3 — Working rules

**One task per session, one commit per task.** The task list exists so that "what were we doing" is never a question.

**Stop it when:**
- It proposes changing a constant, formula or verb from the master
- Its C# disagrees with the prototype on the same seed
- It suggests simplifying the three scoring rules in master 5.3
- It wants to put chamber data in a `ScriptableObject`
- It reaches into `unity/` during stages 0 or 1

All of those are in `CLAUDE.md` as guard rails, but they are worth recognising yourself.

**Verify by measurement, not by reading code.** Twelve seeds, before and after. The suite is the only measurement tool; the editor is for feel.

**Read the chronicle regularly.** A green test suite over an unreadable world is a failed build, and no test catches that.

---

# PART 4 — Roughly how long

At one day a week:

| Stage | Sessions |
|---|---|
| 0 — foundation | 1 |
| 1 — the simulation | 6–8 |
| 2 — Blender chambers | 2–3 |
| 3 — the shell | 8–12 |
| 4 — the gate | 1 |

**Around five months to the gate**, and the gate is the real milestone — the point where you find out whether the idea works. Everything after it is production, and the content plan puts that at roughly twenty months more.

Which is why nothing in stages 2 through 4 should be polished. Whitebox geometry, placeholder audio, five beats. **The gate is not a demo. It is an experiment, and the result can be no.**
