# CLAUDE.md

Project instructions for agents working in this repository. Read this before doing anything.

---

## What this is

**Standing Order** — a real-time co-op game for 2–4 players, built in Unity, where four camps run a full simulation of ecology, territory, politics and faith whether players are present or not.

The simulation is the product. Everything else serves it.

---

## Where the truth lives

| Question | File |
|---|---|
| Any rule, formula, constant or system | `docs/00-MASTER-standing-order.md` |
| Repo layout, data contracts, task list | `docs/standing-order-project-setup.md` |
| Engine-specific traps | `docs/standing-order-unity-notes.md` |
| **Which tool does what, and in what order** | `docs/standing-order-pipeline.md` |
| What a camp says and why | `docs/standing-order-beats.md`, `docs/standing-order-systems.md` |
| Colours, type, lighting | `docs/standing-order-visual-identity.md` |
| Accessibility rules that constrain other systems | `docs/standing-order-accessibility.md` |

**The master document wins.** Where any other document disagrees with it, the master is correct and the other document is stale — flag it, don't silently follow it.

**`prototype/` holds a working JavaScript implementation** of layer one and embodiment. It is the behavioural reference, not shippable code. When the C# and the prototype produce different histories from the same seed, **stop and find out why before tuning anything.**

---

## Architecture — the one rule everything hangs off

**Core is plain C# with no Unity references.** Its own assembly definition, mirrored as a standalone .NET project so tests run without the engine.

Three layers, strictly one-directional:

- **Core** — world model and tick. Pure functions over world state and a seeded random source. No I/O, no time, no engine.
- **Adapter** — serialisation, the player-effect accumulator, knowledge filtering, network shapes.
- **Presentation** — Unity. Renders state, sends intents, never computes an outcome.

**Banned inside Core:** `UnityEngine.*`, `Mathf`, `Vector2/3`, `Random`, `Time`, `Debug`, coroutines, `MonoBehaviour`, `ScriptableObject`. Use `System.Math`, plain structs, the seeded generator, an injected logger.

Do not put the chamber or camp tables in `ScriptableObject`s. They must be loadable without Unity or the headless tests cannot run the real world.

---

## Determinism

Narrow, but absolute where it applies.

- One seeded random source, owned by Core. Nothing else generates randomness that can feed back.
- **Fixed iteration order everywhere.** Never iterate a hash map or set where order affects an outcome. This is the usual cause of "the same seed gave a different history."
- No wall-clock time, frame rate or engine callback inside Core.
- Acceptance: the same seed run twice in two processes produces byte-identical chronicles for 1,000 ticks.

Cross-platform float determinism is **not** required — the architecture is host-authoritative, so two machines never independently compute the same float. Do not spend time on fixed-point arithmetic. If anyone proposes lockstep, that is a design change and needs a human decision.

---

## How to verify anything

**The headless test suite is the only measurement tool.** The editor is for feel.

Every balance claim in the design documents came from twelve seeds run headless. Hold that standard:

- **Never tune on one seed.** Measure across twelve seeds before and after any change, and report both numbers.
- A green suite over an unreadable chronicle is a failed build. Read the log.
- The foundational test: **1,000 ticks with no player, all four camps alive, 12/12 seeds.** If a change breaks this, the change is wrong.

---

## Guard rails

These override any reasonable-sounding local decision.

- **Never import an engine type into Core.**
- **Never simulate on a client.**
- **Never let a UI surface read world state directly** — only filtered knowledge. Captions are generated from audio events, never from world state.
- **Never add a combat stat, tier or level.** Fighting exists but does not scale. This is constitutional.
- **Never let a beat change the world by itself.** Beats present situations; only player responses change anything.
- **Never remove the `MIN_POP` or `MIN_PRED` floors.** Ordinary attrition must not exterminate anyone — only players can.
- **Never "simplify" the three scoring rules in master 5.3.** They took four rebalancing passes and each looks redundant until removed:
  1. Score expected return, not need.
  2. Gate growth on carrying capacity, not current food.
  3. Raiding pays a march cost per hop; hunting does not.
- **Never generate content that invents a fact.** A hallucinated grievance corrupts the political state players reason about.

---

## Definition of done

A task is done when:

1. It has an automated acceptance criterion, drawn from the master's test conditions.
2. The criterion passes on twelve seeds.
3. The chronicle still reads like a history — a human check, and not optional.

---

## Working style

**Decide alone:** implementation details, data structures, file organisation within the layout, test scaffolding, refactors that preserve behaviour.

**Ask first:** anything that changes a documented constant, adds or removes a verb, alters a formula in the master, changes the architecture, or affects what a player can perceive.

**Stop and report:** when the C# and the prototype disagree on the same seed; when a change breaks the thousand-tick test; when a guard rail seems to be blocking something genuinely necessary.

**Commits:** one task per commit, message naming the task ID from the setup document's breakdown (`A4: ecology — flora, prey, apex, collapse hysteresis`).

**When updating a documented constant**, update the master's constants table in the same commit. The documents drifted from the prototype once already — the hunt multiplier said 4.0 while the simulation used 7.0 — and it would have produced camps that starve.

---

## Do not build logic through the editor

Ninety percent of this game is C# with no editor involvement. Building it by driving Unity through MCP produces GameObjects instead of testable code, and loses the headless suite — the only objective measure this project has.

**MCP is for presentation.** Scene assembly, component wiring, reading console output. Not simulation logic. See `docs/standing-order-pipeline.md`.

Phases A, B and C are entirely headless — C# and `dotnet test`, no editor involvement. Running Unity alongside is harmless, but its MCP server loads a large tool set into context that is unusable during these phases, and more available tools means worse tool selection. Leaving it closed until Phase D is a performance choice, not a rule.

## Current state

- **Layer one and embodiment:** implemented in `prototype/`, passing the full invariant sweep. Not yet ported.
- **Layers two, three, four:** specified, unbuilt.
- **Next tasks:** A1–A3 in the setup document — repo skeleton with CI, static data tables, seeded RNG and tick shell.

Nothing past task D8 (the legibility gate) begins until the gate passes.
