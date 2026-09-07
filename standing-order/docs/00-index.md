# Standing Order — document index

*The reading order, what each document is for, and what state it's in.*

---

## The set

| # | Document | What it's for | State |
|---|----------|---------------|-------|
| **0** | **`00-MASTER-standing-order.md`** | **The handoff document. Self-contained: everything below, consolidated. Start here.** | **Current** |
| 1 | `standing-order-gdd.md` | The anchor. Premise, camps, all systems, build order. | Current, except the map section |
| 2 | `standing-order-story.md` | Narrative architecture. Invariants, acts, beat library, dialogue, endings. | Current |
| 3 | `deepholt_codex.html` | The showcase. Placard, map, camps, food webs, a real timeline. Show this to people first. | **Stale** — 16 chambers, needs The Rookery |
| 4 | `deepholt_region_map.html` | The geography on its own. Tap a chamber for detail. | **Stale** — 16 chambers, needs The Rookery |
| 5 | `deepholt_simulation.html` | Layer one, running. Fifteen chambers, four camps, live chronicle. | Current |
| 6 | `standing-order-mechanics.md` | Verbs, time and scale, the Cistern, capture, multiplayer, information design. | Current |
| 7 | `standing-order-production.md` | Audio and art direction, names bible, risk register. | Current |
| 8 | `standing-order-layer2-politics-faith.md` | Layer two build spec: relations, hierarchy, diplomacy, creed, faith, schism. | Current |
| 9 | `standing-order-layer3-party.md` | Layer three build spec: the party as a faction, two clocks, noise, capture, knowledge, beats. | Current |
| 10 | `standing-order-embodiment.md` | **Amends layers 1–3.** Camp decisions become physical bands that travel, act and return in real time. | Current |
| 11 | `standing-order-systems.md` | Tech track, items and trade, dialogue fragments, character creation. | Current |
| 12 | `standing-order-beats.md` | The forty-beat library — triggers, shapes, consequences, writing order. | Current |
| 12 | `standing-order-gospels-and-names.md` | The plate, the four corrupted gospels, the hermit's name, title options. | Current |
| 13 | `standing-order-layer4-realtime.md` | Layer four build spec: camera, chambers as spaces, LOD, audio, networking, saving, the legibility gate. | Current |
| 14 | `cavern_sim.py` | Headless prototype. Best place to tune weights fast. | **Stale** — still six chambers |

If someone has ten minutes, give them the codex and then the simulation. If they have an hour, the design document then the story document.

---

## Where the onion stands

> **Note:** the embodiment document amends layers one to three. Camp decisions no longer resolve inside a tick — they spawn physical bands that travel, work and return. Read it alongside any of the three.

**Layer 1 — the world tick.** *Complete and passing its foundational test.* The thousand-tick no-player test now passes 12/12 seeds, after two changes: The Rookery gives the Assayers a hunting ground their taboo permits, and beaten camps now **rout rather than die** — ordinary warfare cannot exterminate anyone, so only players can destroy a camp. Ecology, hunting ranges, growth, territorial expansion, migration, raiding, seizure of ground, collapse and recovery — running on the sixteen-chamber map. Verified across six seeds: six different outcomes, populations that grow and hold rather than declining, camps ending up holding one to eight chambers.

Open design question, not a bug: **the Assayers die in every run.** Their taboo forbids the goats in their own chamber, leaving one small pond next door, and the Mirelurks usually settle it around tick 7. By tick 26 the newts are gone and at tick 27 the Assayers break their own law out of starvation. That is a good story — a neighbour's expansion causing a religious crisis — but decide deliberately whether they are a dying cult the party arrives in time to witness, or a faction meant to survive. Fixing it is a map or taboo change, not a number.

**Layer 2 — politics and faith.** *Specified, unbuilt.* Full build spec written: relations matrix with ranges and event values, hierarchy with loyalty and succession, intelligence tiers gating the action menu, gift/parley/ally/tribute/betray/incite, creed interpretation, faith erosion, zealotry, schism, atonement, log lines, six automated test conditions, and a tuning constants table. Ready to implement.

**Layer 3 — the party as a faction.** *Specified, unbuilt.* Two-clock reconciliation between real-time play and the 90-second tick, party and peasant data models, hunger, noise and detection, encounters and capture including split capture, promises, the knowledge subset model, verb-to-world-effect mapping, beat triggering, seven test conditions.

**Layer 4 — real-time shell.** *Specified, unbuilt.* First-person camera, chamber dimensions tied to the embodiment timings, three-tier simulation LOD, audio occlusion via the tunnel graph, no HUD, host-authoritative networking with per-player knowledge filtered on the host, saving, performance budget, band readability, and the legibility gate.

**The legibility gate is the hard stop.** Five outside testers, thirty minutes, asked three times what a camp is about to do and why. 60% correct or nothing in layer five begins.

**Layers 5+ — co-op, research, quests, art, UX.** Untouched.

---

## What's still missing

Ordered by what unblocks the most.

~~Verb list. Time and scale. The Cistern. Capture rules. Multiplayer. Information design. Art, audio, names, risks.~~ *All settled — see documents 6 and 7.*

~~Layer two written up in full.~~ *Done.*

~~Layer three.~~ *Done.*

~~Layer four.~~ *Done. All four layers are specified.*

~~The technical specification.~~ *Done — `00-MASTER-standing-order.md`.*

**1. Build the embodiment model headless**, before layer two. It changes how every layer-two action resolves, so building politics first means rewriting it.

**2. Re-verify the simulation** against the four-hundred-year principle: the starting state must be a centuries-old equilibrium, so a thousand-tick run with no player present should end with every camp alive. Do this last, once politics and faith are in.

---

## The plan

1. ~~Get the current documents in order and complete layer one.~~ *Done.*
2. Verb list, time and scale, the Cistern, capture rules. Roughly one session each.
3. Layer two written up in full as its own document: politics and faith, precisely enough to build from.
4. Layer three, then layer four, same treatment.
5. Combine everything into one handover document — premise, mechanics, entities, formulas, glossary — written for a machine to build from rather than for a person to be persuaded by.

Step 5 is the goal. Steps 2 to 4 exist so that step 5 can be written once.

---

## Naming

Everything is provisional: *Standing Order*, Deepholt, Marrowing, Count Doudelfas, the Sporewardens, the Ashfang, the Mirelurks, the Assayers, and every chamber and species name. None of it came from you. Replace any of it freely — none of the systems depend on the names.
