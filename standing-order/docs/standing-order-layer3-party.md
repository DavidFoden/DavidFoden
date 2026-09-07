# Standing Order — Layer Three: The Party

*Build specification, v0.1. Sits on layers one and two.*

This is the layer where a real-time game meets a tick-based simulation. That reconciliation is the hard part and §2 deals with it first, because everything else depends on getting it right.

---

## 1. What this layer is for

The party is not a special case. It is a fifth faction that hunts with the same code the camps use, poaches the same ground, and appears in the same standing matrix.

The design consequence is the thesis of the whole game: **the party damages the world by surviving.** Four peasants fall in with nothing, have to eat, and the only food is the ecology four cultures depend on. No special player-destruction verb is needed.

---

## 2. Two clocks

The world ticks every 90 seconds. Players move continuously. These are reconciled by splitting responsibility, not by slowing anything down.

**The continuous layer** (server frame rate) owns: movement, noise emission, detection, animal behaviour in the player's chamber, encounters, capture, carrying, fire, and every verb's immediate effect.

**The tick layer** (every 90s) owns: everything in layers one and two. Camp decisions, ecology, standing, succession, faith.

The bridge is an accumulator. Party actions write into `pendingWorldEffects` the moment they happen, and the next tick consumes them:

```
pendingWorldEffects = {
  preyTaken:   { chamberKey: amount },      // applied before ecologyTick
  floraTaken:  { chamberKey: amount },
  tunnelsOpened: [[a,b], ...],
  tunnelsBlocked: [[a,b], ...],
  poachedIn:   { chamberKey: [ticksPresent] },
  giftsGiven:  { campKey: {food, tools} },
  sluiceChanges: [...],
  noiseEvents: [ {chamber, magnitude, tick} ],
  observedBy:  { campKey: [events] }
}
```

**Rule: the party's effects are immediate, the world's response is not.** Kill a glowslug and the prey count drops that second. The Sporewardens don't notice until the tick. That delay is where the drama lives — the player has always already done the damage before anyone reacts.

**A camp's `sense()` reads the world including everything the party did since the last tick.** No special-casing.

---

## 3. Data model

### Party

```
party = {
  chamber:      chamberKey,          // where the group is
  peasants:     [Peasant × 2..4],
  stores:       { food: float, tools: [Tool] },
  charges:      int,                 // breaking charges, 0..3
  knowledge:    Knowledge,           // §7
  promises:     [Promise],           // §6
  capturedBy:   campKey | null,
  reputation:   { betrayals: int, giftsGiven: int, chambersEmptied: int }
}
```

The party has **no standing of its own**. Players hold their own opinions. Only `standing[camp][party]` exists.

### Peasant

```
peasant = {
  name, playerId | null,             // null = NPC follower
  hunger:    0..100,                 // 100 = starving
  condition: 0..100,                 // 0 = down
  carried:   [Item],                 // hard slot limit 6
  state:     'ok' | 'down' | 'held',
  noise:     float                   // current emission, continuous
}
```

Solo play and drop-out use the same structure: `playerId: null` means an NPC follower with identical stats. **There is no separate single-player balance.**

---

## 4. Hunger and condition

Hunger rises continuously, roughly one meal per person per 6–8 ticks (10–12 minutes real time).

| Hunger | Effect |
|---|---|
| 0–40 | None |
| 41–65 | Listening range −25% |
| 66–85 | Carry slots −2, sneaking noise +40% |
| 86–99 | Condition drains slowly, climbing unavailable |
| 100 | Condition drains fast |

**Hunger is never a bar.** It is read from the world: hearing shortens, hands get unreliable, the screen's audible range contracts. Players should notice they're struggling before anything tells them.

Condition recovers with rest and food. A peasant at condition 0 is `down`, not dead — see §5.

---

## 5. Noise, detection and encounters

### Noise

Every verb emits a magnitude. Noise propagates by tunnel distance with falloff, and any camp whose range touches the source rolls to notice.

| Verb | Magnitude |
|---|---|
| Sneak | 1 |
| Walk | 3 |
| Forage, set snare | 2 |
| Hunt (chase) | 7 |
| Build fire | 4 continuous, plus light visible one chamber out |
| Break rock | 12 |
| Block tunnel | 14 |
| Flee | 10 |
| Brawl | 9 |

`Break` and `block` being the loudest things in the game is deliberate: the two verbs that change the map are the two most likely to be witnessed.

### Detection

```
noticed = magnitude / (1 + distanceInTunnels²) > camp.alertness
```

`camp.alertness` falls with standing toward the party (friendly camps aren't watching for you) and rises while in fervour.

On notice, the camp records an observation into `observedBy`, which the next tick converts into standing effects and, for zealots, a `pursue:party` action.

### Encounters

When a camp acts on `pursue:party`, a hunting party enters the party's chamber in the continuous layer. Outcomes:

- **Evade.** Sneaking, distraction, fleeing, or a tunnel they can't follow you through.
- **Parley.** Available if standing is above `PARLEY_FLOOR` and the camp is not in fervour.
- **Brawl.** The party loses against any organised group. This is not a difficulty tuning matter — it's the design.
- **Capture.** Per the mechanics document.

### Capture

On capture:

- All carried items transfer to that camp's stores. **Tools entering a camp's stores advance its tech track**, which is how you arm the people who caught you.
- `party.capturedBy = campKey`
- Standing shifts by −8 (they consider you caught, not defeated)
- Held peasants are `state: 'held'` in that camp's home chamber

Four exits, all gameplay: **escape**, **ransom** (another camp pays, you owe them 3 gift-equivalents), **release** (a camp at Friendly or better intervenes), **labour** (work N ticks; standing +20 on completion, and you are inside a camp while its politics happen around you).

**Split capture is the primary co-op case, not an edge case.** One player held, the others free, is a rescue mission. Build for it first.

**Zealots do not capture.** A camp in fervour kills. This is the only lethal camp state and it's what makes a faith break frightening.

---

## 6. Promises

Needed because layer two's faith erosion includes *"promised something and failed to deliver."*

```
promise = { camp, kind, amount, madeAtTick, dueTick }
kind: 'food' | 'tool' | 'kill' | 'route' | 'silence'
```

Created through dialogue. Resolved automatically at `dueTick`:

- Kept: standing +15, faith +10
- Broken: standing −20, faith −18
- **Silently unkept:** if the party never mentions it again and the camp has no way to check, it resolves at `dueTick` anyway. Camps notice absence.

Promises are the main way a player can damage a relationship without doing anything at all, which is exactly right for a game about four people who mean well.

---

## 7. Knowledge

**The player's knowledge is a strict subset of world state.** This is a hard rule and it needs its own data structure, or the whole information design collapses.

```
knowledge = {
  chambersSeen:    Set<chamberKey>,
  tunnelsKnown:    Set<pairKey>,
  campsMet:        Set<campKey>,
  gospelsHeard:    Set<campKey>,        // versions of the prophecy
  facts:           [Fact],
  chronicle:       [LogEntry]            // filtered
}

fact = { subject, claim, source: campKey|'witnessed'|'ovik', tick, reliable: bool }
```

**Three ways to learn anything:** witness it, be told it, or infer it from the world (a stripped chamber, fresh sign, a body).

Facts from camps carry that camp's spin. A Mirelurk telling you the Ashfang are starving may be true, exaggerated, or an attempt to point you at a rival. `reliable` is not shown to the player — it determines whether the fact matches world state.

**The chronicle the player reads is filtered to witnessed and reported entries only.** The full log still exists for us. Sitting at a fire and comparing notes is the UI for assembling it.

**Ovik** carries roughly 3–5 facts per circuit, weighted toward the dramatic, and trades them. He is the main delivery mechanism for everything happening out of sight.

---

## 8. Verb effects

The complete mapping from the mechanics document's verbs to world state. If a verb isn't here, it has no simulation effect.

| Verb | World effect |
|---|---|
| Hunt | `preyTaken[chamber] += n`; `poachedIn[chamber]` if owned; noise 7 |
| Forage | `floraTaken[chamber] += n`; noise 2 |
| Set snare | Deferred `preyTaken` on return; noise 2 |
| Break | `tunnelsOpened`; charges −1; noise 12 |
| Block | `tunnelsBlocked`; noise 14. **Can starve a camp by cutting its hunting range** |
| Give | `giftsGiven[camp]`; standing per layer two |
| Steal | Camp stores −n; if noticed, standing −30 |
| Divert (Cistern) | `sluiceChanges`; flora regrowth multipliers change |
| Parley | Opens dialogue; may create promises, alliances, ransoms |
| Lie | Assert another camp's gospel; if checked against a camp that knows better, faith −25 |
| Signal | `noiseEvents` at a chosen location; pulls pursuit |
| Build fire | Warmth, cooking, light one chamber out, noise 4 continuous |

**`Block` deserves special attention in testing.** It's the one verb whose consequences are entirely invisible at the moment of use and potentially catastrophic three chambers away twenty ticks later. That's the game's thesis in a single action.

---

## 9. Beat triggering

Beats from the story document are evaluated at the end of each tick.

```
for beat in beatLibrary:
    if beat.trigger(world, party) and not beat.fired:
        queue(beat)
```

Rules:

- **One beat per tick maximum.** If several qualify, take the highest priority; the rest stay eligible.
- **A beat fires at most once per playthrough** unless flagged repeatable.
- **Beats never modify world state directly.** They present a situation; the player's response is what changes anything. A beat that changes the world by itself is a cutscene, and cutscenes contradict the design.
- Every beat needs a *no response* path — players will walk away, and that has to be a real outcome.

Expected coverage: a playthrough sees roughly a third of forty beats. That's correct. Groups should be able to compare notes and find they saw different games.

---

## 10. Test conditions

1. **Party effects reach the tick.** Hunt in a chamber, verify prey drops immediately and the owning camp's `sense()` reflects it on the following tick.
2. **Poaching escalates.** A party hunting an owned chamber for 6+ ticks must produce a delegation or a raid.
3. **Capture is recoverable.** All four exits reachable in testing. No state where a captured party has no route out.
4. **Split capture works.** One held, others free, rescue completes.
5. **Knowledge is a subset.** Assert that no UI surface ever reads world state directly — only `party.knowledge`. Automate it; this is the rule most likely to be broken by accident.
6. **Block starves.** Cut a camp from its only hunting range and verify it migrates, raids, or dies within 30 ticks — and that the chronicle attributes it to nobody, because nobody saw.
7. **No player, no beats.** With no party present, no beat may fire.

---

## 11. Tuning constants

| Constant | Value | Controls |
|---|---|---|
| `HUNGER_RATE` | 100 / 7 ticks | Meal frequency |
| `CARRY_SLOTS` | 6 | Per peasant |
| `CHARGES_MAX` | 3 | Breaking charges |
| `CHARGE_RECHARGE` | 40 ticks | With a dwarven tool |
| `DOWN_THRESHOLD` | condition 0 | Incapacitation |
| `CARRY_SPEED` | 0.5× | Carrying a friend |
| `LABOUR_TICKS` | 25 | Working off capture |
| `RANSOM_DEBT` | 3 gifts | Owed to whoever pays |
| `OVIK_FACTS` | 3–5 per circuit | Rumour throughput |
| `BEAT_MAX_PER_TICK` | 1 | |
| `PROMISE_WINDOW` | 20 ticks | Default due date |

---

## 12. Build order

1. Party entity, movement, hunger, carrying. No camps involved.
2. The accumulator (§2) and hunting through layer one's code. Verify a chamber can be emptied by players alone.
3. Noise and detection. Verify camps notice.
4. Encounters and capture, including split capture.
5. Knowledge model and the filtered chronicle. Do this before dialogue, or dialogue will read world state and the rule will be broken permanently.
6. Parley, gifts, promises.
7. Beat triggering.
8. Cistern verbs.
9. Test conditions in §10.

Step 5 before step 6 is the one that matters. Everything else can be reordered.
