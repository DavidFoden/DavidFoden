# Standing Order — Build Inventory

*What exists, what must be made, and how much of it. v0.2.*

The purpose of this document is scale. Every line item has a count, so the size of the project is visible before anyone commits to it.

---

# PART 1 — What exists today

## Design

| Artefact | State |
|---|---|
| Master specification | Complete and self-contained. Premise, world, story, mechanics, all four layers, embodiment, data model, ~70 constants, 37 test conditions, glossary |
| Beat library | All 40 specified with triggers, shapes and consequences |
| The four gospels + the plate | Written, final text |
| Systems: tech, items, dialogue, character creation | Specified |
| Layer specs 1–4 + embodiment | Specified in detail |
| Production notes | Audio and art direction, names, risk register |
| **Asset register** | All ~46 audio sets, ~73 art assets and ~322 content pieces enumerated with specs, acceptance criteria and sourcing routes; Phase 1 is 19 assets |
| **CLAUDE.md** | Repo-root agent instructions — architecture rule, guard rails, verification protocol, escalation rules |
| **Unity notes** | Assembly boundary, determinism scope, NavMesh, scene streaming, Wwise pipeline, editor traps, setup order |
| **The opening** | The first ten minutes as a timed sequence with teaching order, party-size variants, failure modes and seven test conditions |
| **Content plan** | Two-phase production, gate content list, voice bible, batching, definitions of done, agent delegation rules, ~85 days estimated, cut list |
| **Accessibility design** | Dual-channel principle, co-signal table, caption rules, photosensitivity, motor, difficulty axis, 6 test conditions, and the amendments it forces |
| **Audio middleware research** | Decision note: Wwise provisionally, with a one-day comparison test specified |
| **Visual identity** | World palette, document palette, camp identity verified for greyscale separation, type, lighting, material language, six screen briefs |
| **Project setup pack** | Module boundaries, repo layout, data contracts with types and ranges, determinism rules, environment decisions, 24 tasks with acceptance criteria, agent guard rails, asset naming |

## Working code

| Artefact | State |
|---|---|
| Simulation prototype (browser, JavaScript) | Layer one **and** embodiment, running |
| — ecology | Flora, prey, apex predators, collapse and recovery, predator migration with habitats |
| — camps | Hunting ranges, growth, territorial expansion, migration, raiding, routing, taboo |
| — bands | Decisions become physical parties that travel, work and return |
| Invariant test sweep | 12 seeds × 1,000 ticks, all passing |
| Seed survey tool | Characterises twelve worlds in ~1 second |

## Settled decisions

Title · the hermit (Tallow) · the Assayers · nobody is coming from above · player-made peasants · combat exists but does not scale · clearing replaces mining · the Cistern's failure cascade · capture rather than death · 90-second tick · host-authoritative co-op · first person · no HUD.

**Nothing structural is open.**

---

# PART 2 — What must be created

## 2.1 Code

*Structure, schemas and task breakdown are specified — see the project setup document. What follows is the build itself.*

| Item | Count / size | Notes |
|---|---|---|
| Port simulation to C# | ~1,200 lines | The JS prototype is the reference implementation, not the shippable one. Must be engine-independent so headless tests keep running |
| Layer two: politics and faith | ~800 lines | Relations, hierarchy, succession, diplomacy, creed, faith, schism |
| Layer three: the party | ~1,000 lines | Two clocks, accumulator, noise, detection, capture, knowledge, promises |
| Layer four: the shell | Largest single job | Movement, LOD, audio routing, screens |
| Networking | Unknown until transport chosen | Host-authoritative, movement prediction only |
| Save / load / migration | Small | Tick-boundary snapshots, versioned |
| Test harness in CI | Small | 37 conditions, run every build |
| Telemetry | Small | Needed to measure the legibility gate |

## 2.2 World geometry

| Item | Count |
|---|---|
| Chambers to whitebox | **16** |
| Chambers to art-pass | 16 |
| Tunnels | 25, plus 6 latent (blocked) connections |
| Distinct verticality treatments | 16 — each chamber must be identifiable in one second |
| The Cistern | 1, with four working sluice gates |
| The Sealed Gate | 1, water-counterweighted |

## 2.3 Characters and creatures

| Item | Count | Notes |
|---|---|---|
| Playable peasants | 1 rig, 6 trade variants | Player-made, light customisation |
| Camp cultures | **4** | Must read by silhouette at distance and in bad light |
| Named individuals | ~16 | Leader + 2–3 notables per camp, procedurally named |
| Independents | 2 | Tallow, Ovik |
| Prey species | **14** | Each needs a distinct silhouette *and* a distinct sound |
| Apex predators | 2 | The ridge dragon, ripper eels |
| Flora types | 16 | Environmental, not creatures |
| Band formations | 2 | Hunting party vs war band, readable at a glance |

## 2.4 Audio — the priority

| Item | Count |
|---|---|
| Room tones | **16**, one per chamber, identifiable blind |
| Life beds | **14**, one per prey species |
| Apex sounds | 2, audible at range |
| Camp sound sets | 4 cultures × work / argument / movement |
| Band audio | 2, directional at two chambers' distance |
| Party foley | Footsteps by surface, breathing by hunger, carrying, fire |
| UI / diegetic | Fire, map, inventory |
| Music | **2 cues only** — the fall, and the endings |

The critical asset is **silence**: a hunted-out chamber loses its life bed, and that absence must survive the mix.

## 2.5 Interface

| Screen | Notes |
|---|---|
| Main menu | |
| Lobby / host / join | Drop-in, drop-out |
| The fire | Shared. Filtered chronicle. Where the party argues |
| The map | Hand-drawn, fills in, unreadable while moving |
| Inventory | 6 slots per peasant, shared load |
| Settings and accessibility | **Not optional — see 2.8** |
| Endings | 5 variants + a 20-tick epilogue |

## 2.6 Writing

| Item | Count |
|---|---|
| Beats to write out | **40** (all specified, none written as prose) |
| Camp voices | 6 registers — 4 camps, Tallow, Ovik |
| Dialogue fragments | **~200** slotted |
| Gospels | 4 — **done** |
| Endings text | 5 |
| Item and creature descriptions | ~50 |
| Chamber descriptions | 16 |
| Onboarding — the first ten minutes | 1, and it must be identical every time |

## 2.7 Visual identity

Not yet started, and the next thing to do.

| Item |
|---|
| Palette — the limestone/peat/malachite/ochre/rust set from the prototypes is a starting point, not a decision |
| Type — display and UI |
| UI language — no HUD, so everything must be diegetic |
| Lighting model — scarce, directional, fire-based |
| The dwarven layer — square, precise, legible against everything organic |
| Six screen mockups |

## 2.8 Accessibility

**Specified** — see the accessibility document. What remains is production, and it is not small.

| Item | Count |
|---|---|
| Audio-to-visual co-signals to build | **11**, listed in the co-signal table |
| `Listen` visual rendering | 1 feature, built alongside its audio |
| Caption layer | 1, generated from audio events only |
| Settings: flicker reduction, brightness floor, outlines, text scale, toggles, remapping | ~8 |
| Difficulty pressure axis | 4 constants, Adapter layer only |

**The co-signals are the real scope.** Torch bloom, ceiling dust, fleeing animals, drying stone, kill remains — designed into chambers from the start, because retrofitting them into finished environments is expensive and designing them in is nearly free.

## 2.9 Business

| Item | When |
|---|---|
| Steam page and capsule | **Early** — wishlists accumulate |
| Trailer | After the legibility gate |
| Age rating | Before launch |
| Early access plan | Before the page goes up |

---

# PART 3 — What we are deliberately not making

Guard rails. Every one of these will be suggested by somebody.

- Combat progression, gear tiers, levels, bosses
- Mining or terrain deformation
- PvP
- A HUD
- A scripted plot
- Runtime AI generation of facts
- Host migration in v1
- A world that ticks while nobody plays

---

# PART 4 — Order

**Done since v0.1:** the project setup pack — an agent can now start without asking what anything means or where it goes.

**Done since v0.1:** project setup pack · visual identity · audio middleware (Wwise) · accessibility design · content plan · the opening.

**Now:** the voice bible (2 days, and it gates the largest content item in the project) · the tone test · the two-day repo and CI setup · then start the project.

**Known stale:** `deepholt_codex.html` and `deepholt_region_map.html` still show fifteen chambers and pre-date bands. Regenerate when convenient — they are showcase pieces, not sources of truth.

**Next:** layer two in the simulation · one whiteboxed chamber to verify 60–120 m and the audio feel.

**Then:** layer three · the shell · **the legibility gate**.

**Only after the gate passes:** the 40 beats, 200 fragments, art pass, audio production, networking hardening, Steam page.

The gate is the pivot. Everything before it is cheap and reversible; everything after it is expensive. Do not commission audio, art or writing for a simulation nobody can read yet.
