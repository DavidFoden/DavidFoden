# Standing Order — Project Setup

*Everything needed before the first line of code. Structure, data contracts, decisions, and a task breakdown. v0.1.*

This document exists so that an agent working on the laptop can start building without asking what anything means or where anything goes. It contains no code deliberately — code is the agent's job, and pre-writing it would constrain choices that should be made in the editor.

Read alongside the master specification, which holds the rules. This holds the shape.

---

# PART 1 — Module boundaries

The single most important architectural rule, stated once:

> **The simulation must be a plain C# library with no Unity references.**

Every test condition in the master specification runs headless. The moment the simulation imports a Unity type, the test harness dies and the project loses its only objective measure of whether the world works.

Three layers, strictly one-directional:

**Core.** The world model and the tick. Ecology, camps, bands, politics, faith. Pure functions over a world state object, a seeded random source, and nothing else. No I/O, no time, no engine.

**Adapter.** Translates between Core and everything outside it. Owns serialisation, the accumulator that collects player effects between ticks, knowledge filtering, and network message shapes. This is where "what does a client get told" lives.

**Presentation.** Unity. Rendering, audio, input, UI. Reads state, writes intents. **Never** computes a simulation outcome.

Core never knows Adapter exists. Adapter never knows Presentation exists.

---

# PART 2 — Repository layout

```
standing-order/
  docs/                      the specification set, this document included
  core/                      the simulation library — no engine references
    world/                   chambers, camps, bands, the tick
    ecology/                 flora, prey, apex, migration
    politics/                relations, hierarchy, faith        (layer two)
    party/                   party as a faction, knowledge      (layer three)
    data/                    the static tables — chambers, tunnels, camps, items
    tests/                   the 37 test conditions
  adapter/                   serialisation, accumulator, knowledge filter, net shapes
  unity/                     the Unity project
    Assets/
      Scenes/
      Scripts/               presentation only
      Audio/
      Art/
      UI/
  tools/                     headless runner, seed survey, balance sweeps
  prototype/                 the JavaScript reference implementation, kept for comparison
```

**Keep the JavaScript prototype.** It is the behavioural reference. When the C# port produces a different history from the same seed, the prototype tells you which one is wrong.

---

# PART 3 — Data contracts

Field lists, types, ranges and ownership. These are the shapes the agent implements.

## Chamber — static

| Field | Type | Range | Notes |
|---|---|---|---|
| key | string | — | Stable identifier, never displayed |
| name | string | — | Displayed |
| position | vec2 | — | Map layout only |
| defensible | float | 0–1 | Defender's terrain advantage |
| slow | float | 0.6–1.4 | Traversal cost multiplier |
| floraName / preyName | string | — | Display |
| floraCap / preyCap | float | 0–60 / 0–30 | Carrying capacity |
| preyStart | float | ≤ preyCap | Initial herd |
| apex | object or null | — | name, population, threat, habitat |
| wet | bool | — | Gates aquatic predator movement |

## Chamber — runtime

| Field | Type | Range | Owner |
|---|---|---|---|
| floraStock | float | 0–floraCap | Core |
| preyPop | float | 0–preyCap | Core |
| pred | float | 0 or ≥ MIN_PRED | Core |
| apexHungry / moveCool | int | ≥ 0 | Core |
| huntedBy / lastHuntedBy | list of camp keys | — | Core, cleared each tick |
| crashed | bool | — | Core, hysteresis at 12% / 45% |
| waterAllocation | float | 0–2 | Core, set by the Cistern |

## Camp

| Field | Type | Range | Notes |
|---|---|---|---|
| key, name, short, colour | — | — | Identity |
| home | chamber key | — | The seat. Always present in holds |
| holds | list of chamber keys | ≥ 1 | Unique; no chamber in two camps |
| known | set of chamber keys | — | What this camp has scouted |
| pop | float | ≥ MIN_POP | **Includes people away in bands** |
| food | float | ≥ 0 | Stores at the seat |
| defence | float | 0–1.2 | |
| temper | float | 0–1 | **Derived from the leader** once layer two exists |
| intelligence | 0 / 1 / 2 | — | Gates the action menu |
| creed | enum | devout / opportunist / indifferent / rival | |
| venerates | string or null | — | An apex name. Taboo follows the animal |
| lastResult / ticksSinceFight | — | — | Short-term memory |
| lastSettle | int | — | Expansion cooldown |
| marchPenalty | int | 0–3 | Force-march exhaustion |
| leader, notables | objects | — | Layer two |
| faith | float | 0–100 | Layer two, devout and rival only |
| techLevel, techProgress | 0–4, 0–100 | — | Systems document |

## Band

| Field | Type | Notes |
|---|---|---|
| id, campKey | — | |
| purpose | enum | hunt / raid / settle / migrate / gift / parley / tribute / pursue |
| target | chamber or camp key | |
| members | float | Subset of camp.pop, never larger |
| carrying | object | food, tools |
| route | ordered chamber keys | **Fixed at departure, never replanned** |
| leg, progress | int, float | Position along the route |
| state | enum | outbound / working / returning |
| workLeft | float | Ticks of activity remaining |
| departedTick | int | |

## Party and Peasant

Per the master specification. The important contract: **the party has no standing of its own**, and `knowledge` is per player, not per party.

## Relations (layer two)

Asymmetric map keyed by ordered pair, values −100 to +100, plus `alliances`, `truces` (expiry ticks) and `betrayerUntil` per camp.

---

# PART 4 — Determinism

This matters more than it looks, because host-authoritative multiplayer and the automated test suite both depend on it.

**One seeded random source, owned by Core.** Nothing else generates randomness. Presentation may use unseeded randomness for purely cosmetic things that never feed back — particle jitter, idle animation selection — and nothing else.

**Fixed iteration order everywhere.** Never iterate a hash map or set where the order affects an outcome. Camps, chambers and bands are processed in a stable declared order. This is the most common source of "the same seed gave a different history."

**The tick is a pure function.** Given a world state and a seed position, the next state is fully determined. No wall-clock time, no frame rate, no engine callbacks inside Core.

**Acceptance test:** the same seed run twice, in two processes, produces byte-identical chronicles for 1,000 ticks.

---

# PART 5 — Decisions to make before starting

Each of these blocks work and none has been made yet.

| Decision | Recommendation | Why |
|---|---|---|
| Unity version | Latest LTS at start, then freeze | Mid-project upgrades cost days |
| Render pipeline | URP | Cheap, fits a dark cave, good on modest hardware |
| Networking transport | Steam relay via a Unity transport layer | No server costs, friends-list join, matches "host owns the world" |
| Audio middleware | **Wwise, provisionally** — see the audio middleware research note | Our sixteen chambers and twenty-five tunnels are already a rooms-and-portals graph, which is exactly what Wwise's spatial audio is built for. Free Indie licence covers our budget. Run the one-day comparison test before committing |
| Source control | Git with LFS | Binary assets will arrive later |
| CI | Anything that runs the headless tests on push | The 37 conditions are the safety net |
| Test framework | Standard C# test runner | Must run without Unity |

**The audio middleware decision is the one to make early**, because occlusion follows the tunnel graph rather than physical raycasts. Researched separately — the short version is that our world model is already a rooms-and-portals graph, which is the one topology Wwise is built around.

**Hard rule that follows from it:** the audio room and portal layout must be **generated from the same chamber and tunnel tables the simulation uses**, never hand-placed independently. Two sources of truth means a player eventually hears a war band through a tunnel that does not exist. The tunnel graph is the authority; audio geometry is downstream.

---

# PART 6 — Work breakdown

Tasks sized for a working session, each with an acceptance criterion drawn from the master specification's test conditions. An agent can pick these up in order.

## Phase A — Core port

| # | Task | Done when |
|---|---|---|
| A1 | Project skeleton, three modules, CI running an empty test | A failing test fails the build |
| A2 | Static data tables — 16 chambers, 25 tunnels, 4 camps, items | Loaded and validated; no chamber in two camps |
| A3 | Seeded RNG and the tick loop shell | Same seed, two processes, identical output |
| A4 | Ecology: flora, prey, apex, collapse hysteresis | Prey and flora stay in range over 1,000 ticks |
| A5 | Apex migration with habitat and MIN_PRED floor | Both apexes alive at 1,000 ticks in 12/12 seeds |
| A6 | Camp sense and score | Action mix matches the JS prototype within noise |
| A7 | Bands: commit, travel, work, return | No outcome occurs without a band present |
| A8 | Combat with the shared formula, routing at MIN_POP | ~19% assault success; no camp exterminated |
| A9 | Full invariant sweep | **All of Phase A green on 12 seeds × 1,000 ticks** |

## Phase B — Politics and faith

| # | Task | Done when |
|---|---|---|
| B1 | Relations matrix, event values, decay, observers | Grudges form and fade; latency observable |
| B2 | Chronicle lines for every standing change | Debuggable from the log alone |
| B3 | Hierarchy, loyalty, succession | A camp visibly changes behaviour after a leadership change |
| B4 | Intelligence tiers and tier-1 actions | Gift, parley and alliance each occur across 10 seeds |
| B5 | Tier-2 actions | Betrayal rare but never absent across 10 seeds |
| B6 | Creed interpretation table | Same event, four readings |
| B7 | Faith, erosion, the break | **No zealotry ever occurs without a player** |
| B8 | Schism and atonement | Every break leaves a remnant or a dead camp |

## Phase C — The party

| # | Task | Done when |
|---|---|---|
| C1 | Party and peasant models, hunger | Hunger degrades senses before it is announced |
| C2 | The accumulator | Player effects land on the next tick, not instantly |
| C3 | Noise and detection | Camps notice loud work at range |
| C4 | Encounters and capture, including split capture | All four exits reachable; no unrecoverable state |
| C5 | Knowledge model and filtered chronicle | **No surface reads world state directly** |
| C6 | Parley, gifts, promises | A silently unkept promise still resolves |
| C7 | Beat triggering | One per tick; no beat mutates world state |

## Phase D — The shell

D1 one chamber, dark, first person · D2 audio with graph occlusion · D3 headless sim hooked in with capsules · D4 LOD tiers · D5 the three diegetic screens · D6 networking · D7 band silhouettes · **D8 the legibility gate**.

**Nothing past D8 begins until the gate passes.**

---

# PART 7 — Definition of done

A task is done when it has an acceptance criterion that runs automatically, the criterion passes on twelve seeds, and the chronicle still reads like a history. That last one is a human check and it is not optional — a green test suite over an unreadable world is a failed build.

---

# PART 8 — Guard rails for an agent

Rules that override any reasonable-sounding local decision.

- **Never import an engine type into Core.**
- **Never simulate on a client.**
- **Never let a UI surface read world state directly** — only filtered knowledge.
- **Never add a combat stat, tier or level.** Fighting does not scale; that is constitutional.
- **Never make a beat change the world by itself.**
- **Never "simplify" the three scoring rules in master 5.3.** They took four rebalancing passes and each one looks redundant until it is removed.
- **Never remove the MIN_POP or MIN_PRED floors.** Ordinary attrition must not exterminate anyone; only players can.
- **When a balance change is needed, measure across twelve seeds before and after.** Single-seed tuning has been wrong every time it was tried.
- **When the C# and JavaScript versions disagree on the same seed, stop and find out why.** Do not tune until they agree.

---

# PART 9 — Asset conventions

For when art and audio arrive, so nothing needs renaming later.

**Naming.** `chamber_<key>_<variant>`, `creature_<species>_<state>`, `camp_<key>_<role>`, `ui_<screen>_<element>`, `sfx_<category>_<subject>_<variant>`, `tone_<chamberkey>`.

**Audio.** Every prey species gets one life bed and a set of incidental calls. Every chamber gets one room tone. Beds and tones must be separable in the mix, because **the absence of a life bed is a gameplay signal** and ambience must never fill the gap.

**Art.** Silhouette first — every culture and every band type is identified in bad light at distance before any detail work. The dwarven layer is square and precise; everything living is not.
