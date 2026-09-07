# Standing Order

A real-time co-op game for 2–4 players. You are peasants. An earthquake drops you into a dwarven ruin sealed for four hundred years, where four cultures run a full simulation of ecology, territory, politics and faith whether you are present or not.

**The pitch, in one sentence:** the goblins hunted the ridge too hard, so the dragon starved — and nobody wrote that.

---

## Layout

```
docs/         the specification set. docs/00-MASTER-standing-order.md is the source of truth
core/         the simulation — plain C#, no engine references, tested headless
adapter/      serialisation, the player-effect accumulator, knowledge filtering
unity/        the Unity project. Presentation only
prototype/    a working JavaScript implementation of layer one and embodiment
tools/        headless runner, seed survey, balance sweeps
CLAUDE.md     instructions for agents working in this repo
SETUP.md      how this project was set up, from zero
```

## Running the tests

```
dotnet test core/StandingOrder.sln
```

**This must work with Unity not installed.** If it doesn't, the architecture boundary has been broken and that is a critical bug, not an inconvenience.

## The one architectural rule

**Core has no Unity references.** Every test condition in the specification runs headless. The moment Core imports an engine type, the test suite dies and the project loses its only objective measure of whether the world works.

## Verifying a change

Never tune on one seed. Every balance claim in the documents came from **twelve seeds run headless**, and that standard holds.

The foundational test: **1,000 ticks with no player, all four camps alive, 12 of 12 seeds.** If a change breaks it, the change is wrong.

## The prototype

`prototype/deepholt_simulation.html` runs in a browser. It implements layer one and the embodiment model and passes the full invariant sweep. It is the **behavioural reference**, not shippable code.

When the C# and the prototype produce different histories from the same seed, stop and find out why before tuning anything.

## Status

| Layer | State |
|---|---|
| One — the world tick | Implemented in the prototype, passing. Not yet ported |
| Embodiment — bands | Implemented in the prototype, passing. Not yet ported |
| Two — politics and faith | Specified, unbuilt |
| Three — the party | Specified, unbuilt |
| Four — the real-time shell | Specified, unbuilt |

**Nothing past the legibility gate begins until the gate passes.** Five outside testers, thirty minutes, asked what a camp is about to do and why. 60% correct, or perception gets fixed before anything else is added.
