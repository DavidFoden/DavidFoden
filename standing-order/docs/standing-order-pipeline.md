# Standing Order — Build Pipeline

*Which tool does what, in what order, and why. v0.1.*

Written in response to a reasonable-sounding plan that would have cost months: *open Unity, connect MCP, build the game through the editor, whitebox with cubes, generate assets, place them.*

Two parts of that are right. The rest inverts the architecture. This document is the corrected version.

---

# PART 1 — The rule that decides everything

**Ninety percent of this game is C# logic that has nothing to do with the editor.**

Ecology, hunting ranges, growth, territory, bands, combat, relations, hierarchy, faith, schism, the party, knowledge filtering. None of it needs Unity to exist, and all of it is verifiable headless across twelve seeds.

> **Build logic as code with tests. Use MCP for presentation only.**

An agent driving the Unity editor through MCP creates GameObjects and components. That is the correct way to assemble a *scene* and the wrong way to build a *simulation*. Do it the wrong way and you lose the headless suite — and with it every objective measure this project has.

For scale: the invariant sweep caught population being duplicated on every band homecoming, expeditions being billed twice for provisions, and attackers losing 93% of assaults because the decision and the battle used different formulas. **None of those are visible in an editor.** All of them were found by twelve seeds × 1,000 ticks in under a second.

---

# PART 2 — What each tool is for

| Tool | Used for | Not used for |
|---|---|---|
| **Claude Code, file-level** | All of Core. Ecology, camps, bands, politics, faith, party, tests | Anything visual |
| **`dotnet test`** | Proving the world works. The only measurement tool | Feel, pacing, scale |
| **Unity MCP** | Scene assembly, component wiring, checking a live scene, reading console errors | Writing simulation logic |
| **Blender MCP** | Generating whitebox geometry from the chamber tables. The dwarven layer, which is parametric | Creatures, cultures, anything silhouette-led |
| **Generative 3D** | Whitebox props, background clutter, concept exploration | The four cultures, the fourteen creatures, anything a player identifies by shape |
| **Hands, or a commission** | The four cultures, the creatures, the ~20 audio assets that carry state | Bulk clutter |

---

# PART 3 — The order

### Phase A — Core, with Unity closed

Tasks A1–A9. Repo, CI, data tables, seeded RNG, the tick, ecology, apex migration, camps, bands, combat, invariant sweep.

Unity is not needed here. Leaving it closed is worth doing for a practical reason rather than a disciplinary one: **a live MCP server loads its whole tool set into the agent's context**, and during headless phases those tools are unusable noise that degrades tool selection. Nothing breaks if it is open.

**Exit criterion:** the thousand-tick no-player test passes 12/12 seeds, and the chronicle reads like a history.

This is the bulk of the real work and none of it needs an editor.

### Phase B — Politics and faith

Tasks B1–B8. Still headless, still no Unity. Relations, hierarchy, succession, diplomacy, creed, faith, schism.

**Exit criterion:** gifts, parleys and alliances occur; succession changes camp behaviour visibly; no zealotry ever occurs without a player.

### Phase C — The party

Tasks C1–C7. Two clocks, the accumulator, noise, capture, knowledge, beats. Still headless.

**Exit criterion:** no UI surface reads world state directly.

### Phase D — Now open Unity

One chamber, first person, in the dark. Audio before anything visual. Then hook the headless simulation in **as-is**, with bands as capsules.

This is where MCP earns its place: assembling scenes, wiring components, reading console output, checking that a band promoted to the Present tier appears at the right position.

### Phase E — Whitebox, generated not modelled

**The sixteen chambers already exist as data** — diameter, tunnel positions, verticality, `slow` factor, defensibility.

So the whitebox is a generation job, not a modelling job. Blender MCP reads the same chamber tables Core reads, builds geometry to spec, exports glTF, and Unity MCP imports and places it.

**Placement is never a judgement call.** Tunnel positions come from the tunnel table. Chamber dimensions come from the chamber table. If a human or an agent places a tunnel by eye, there are now two sources of truth and they will diverge.

This is the same principle as the Wwise rooms: **the tunnel graph is the authority, and geometry, audio and simulation are all downstream of it.** Three representations, one table.

### Phase F — The legibility gate

Five outside testers, thirty minutes. **Nothing past this begins until it passes.**

### Phase G — Assets

Only now. Cultures and creatures by hand or commission. Audio: library for natural sound, commissioned for the ~20 assets that carry state. Generated 3D for clutter only.

---

# PART 4 — Why "logically correct from cubes" is the wrong test

Cubes tell you whether something *looks* right. They cannot tell you whether the Sporewardens will starve on tick 340 of seed 55.

The logic is proven by the invariant sweep — populations in range, no chamber double-held, no band larger than its camp, all four camps alive at 1,000 ticks, twelve distinct outcomes from twelve seeds.

**What cubes are actually for**, at Phase D: checking that 60–120 metres feels like 60–120 metres, that a tunnel takes the 54–126 seconds the timings claim, and that the dark reads as navigable. That is a *feel* test, and it can only happen after the numbers are already right — otherwise you cannot tell whether it feels wrong because the scale is wrong or because the simulation is.

---

# PART 5 — On generated assets

Reasonable and useful for: whitebox props, background clutter, first-pass concept exploration, the parametric dwarven layer.

Poor for: **the four cultures and the fourteen creatures.** The art direction is silhouette-led — identified in bad light at distance, colour as the weakest of three channels — and that is exactly where generic generation is weakest. A generated goblin will look fine in isolation and fail the desaturation test.

Two commercial notes, since this ships through a company: generated assets carry embedded metadata flagging them as AI generated, and the developer remains responsible for store declarations and usage rights. Settle that as policy before anything ships, not at submission.

---

# PART 6 — Mixing models

Nothing in this project depends on which assistant builds it. The specification is model-agnostic and every task has a measurable acceptance criterion, which is the point.

Two practical cautions:

**Local tools favour local hosts.** Blender and Unity MCP are local stdio servers. ChatGPT connects only to remote HTTPS endpoints and cannot reach a server on your laptop directly — you would be tunnelling a local socket to a public endpoint to talk to an application on the same machine. Workable, but it is infrastructure per session.

**Never run two agents against the same repo at once.** They will produce conflicting commits and you will lose an afternoon to a merge nobody understands.

---

# PART 7 — The corrected plan, in one line

Repo → Core and tests with Unity closed → politics → party → **then** Unity, audio first → whitebox generated from the tables, not modelled by eye → **legibility gate** → assets last.

The instinct to open Unity first is the strongest wrong instinct in this project, and resisting it is what keeps every claim measurable.
