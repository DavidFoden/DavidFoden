# Standing Order — Embodiment

*Decisions as physical activity. v0.1. This document amends layers one, two and three.*

---

## 1. What changes

Layers one to three treat a camp's decision as a resolved fact. `raid:mire` happens inside the tick and produces a result.

That is wrong for a 3D real-time game. A raid is a band of goblins walking three chambers, fighting, and walking back. It takes time. It is visible while it happens. And while it happens, **those goblins are not at home.**

So a decision no longer produces an outcome. A decision produces a **band** — a physical group that leaves the camp, travels, does the thing, and comes back. Outcomes happen where and when the band arrives.

This is the single biggest change to the simulation, and it makes the game better in four ways at once:

- Camps become **committed**. A camp that sends its hunters cannot instantly respond to something else. Bad timing is now possible, and bad timing is drama.
- Camps become **vulnerable while acting**. A war band three chambers from home means an undefended home. That is an entire strategy layer, for the camps and for the players.
- The world becomes **legible**. You don't read that a raid happened; you watch a war band file past you in the dark, and you know what it means. This is the answer to the legibility risk in the production notes.
- The player gains verbs we never had to invent: intercept, warn, follow, ambush, raid-while-empty.

---

## 2. The band

```
band = {
  id, campKey,
  purpose:   'hunt' | 'raid' | 'settle' | 'migrate' | 'gift' | 'parley' | 'tribute' | 'pursue',
  target:    chamberKey | campKey | 'party',
  members:   float,              // population committed, drawn from camp.pop
  carrying:  { food, tools },
  position:  { chamber, progress 0..1, towardChamber },
  state:     'outbound' | 'working' | 'returning' | 'lost',
  workLeft:  float,              // ticks of activity remaining on site
  route:     [chamberKey],       // computed at departure, not re-planned mid-journey
  departedTick: int
}
```

Bands are physical entities in the world. They render, they make noise, they can be seen, followed, avoided, ambushed, or talked to.

**Route is fixed at departure.** A band does not recalculate when the world changes. If the party blocks a tunnel ahead of them, they hit it, mill about, and have to choose — go around or go home. That failure is far more interesting than perfect pathing, and it's cheaper.

---

## 3. The cycle

Replaces "resolve" for any action with a physical component.

```
DECIDE     (tick)     camp scores actions as before, picks one
COMMIT     (tick)     band spawns; camp.pop -= members; camp.food -= provisions
TRAVEL     (continuous) band moves along route, one chamber at a time
WORK       (on site)  hunting, fighting, settling, negotiating
RETURN     (continuous) band travels home
ARRIVE     (tick)     spoils, casualties and knowledge fold back into the camp
```

The tick still drives decisions. Everything between COMMIT and ARRIVE happens in the continuous layer, alongside the players.

**Camps re-decide only at ARRIVE, or when something interrupts a band.** A camp does not issue a new intent every 90 seconds while its band is out — it has already spent those people.

---

## 4. Timings

At 90 seconds a tick:

| Activity | Duration |
|---|---|
| Traverse one tunnel | 0.6–1.4 ticks, by chamber (the Weeping Stair is slow, the Long Gallery fast) |
| Hunt on site | 2 ticks |
| Assault a camp | 1 tick |
| Settle a chamber | 3 ticks |
| Parley / gift delivery | 1 tick |
| Migrate (whole camp moving) | 2 ticks per tunnel, and the camp is helpless throughout |

So a raid on a target three chambers away is roughly **three out, one fighting, three back — around seven ticks, or ten minutes of real time.** Long enough for players to spot it, follow it, warn the target, or rob the empty camp. That number is the most important tuning value in this document.

---

## 5. Garrison and strength

`camp.pop` splits into people at home and people in bands.

```
garrison(camp) = camp.pop - sum(band.members for band of camp)
```

**Every strength calculation in layers one and two now uses the force actually present**, not the camp's total population.

```
defenceStrength(camp) = garrison(camp) * (1 + camp.def) * (1 + chamber.defensible)
raidStrength(band)    = band.members * (1 + camp.def * 0.5)
```

Consequences that fall out for free, with no extra design:

- A camp with two bands out is a soft target, and clever camps (tier 2) can score raids against exactly that condition.
- Sending too many people leaves you exposed; sending too few loses the fight. Band size becomes a real decision.
- The party can rob or raid an empty camp. Enormously tempting and enormously stupid, since the band comes home.

**Band sizing:** hunts commit 25–40% of garrison; raids 50–70%, scaled by how badly they want it; migration is everyone.

---

## 6. Interruption

A band in the field can be stopped, and this is where the player lives.

| Event | Result |
|---|---|
| Route blocked ahead | Band halts, mills for 1 tick, then re-routes or returns. Standing toward whoever blocked it drops sharply if seen |
| Ambushed by another band | Fight where they stand, in whatever chamber that is |
| Party distracts (signal verb) | Band diverts one chamber toward the noise |
| Party parleys with a band | Possible — a war band can be talked to en route, and turned back |
| Home is attacked while out | Band aborts and force-marches home, arriving in half time and exhausted (−30% strength for 3 ticks) |
| Apex predator in a chamber they pass | Casualties, possible abort |
| Band starves | If travel exceeds provisions, members are lost, then the band turns back |

**A war band that can be talked out of a raid is the most valuable single interaction in the game.** Four peasants standing in a tunnel arguing with thirty goblins, and it working, is the whole fantasy.

---

## 7. What this breaks in the existing layers

Explicit amendments. Anything not listed is unchanged.

**Layer one**
- `resolve()` no longer applies hunt or raid outcomes directly. It spawns bands.
- `preyTaken` is applied when a hunting band reaches the chamber and completes WORK, not at decision time.
- `settle` requires a band to arrive and complete 3 ticks of work. A settlement can be interrupted before it completes.
- `migrate` is a multi-tick vulnerable move, not an instant relocation.
- Ecology tick is unchanged.

**Layer two**
- `gift`, `parley` and `tribute` require a band to physically reach the target. Diplomacy has travel time, and a gift can be intercepted.
- Standing changes land at ARRIVE, not at decision.
- Succession is unaffected — it happens at home.
- Betrayal classification is evaluated at the moment of the assault, not the decision, so a camp can commit a raid and have it become a betrayal because an alliance formed while the band was walking. **That is a feature. Keep it.**

**Layer three**
- The accumulator still works as specified. Add `bandsSeen` to party knowledge.
- Noise: bands emit continuously while travelling, magnitude 5 for hunts, 9 for war bands. **A war band is audible from two chambers away**, which is the primary early warning system in the game.
- New party verbs, all built from existing ones: **follow**, **intercept** (block + brawl), **warn** (travel to the target camp and parley before the band arrives), **ambush** (hide + brawl, the one situation where peasants can win, because a tunnel is narrow).

---

## 8. The chronicle changes shape

A raid was one line. Now it's a sequence, and the player only sees the parts they witnessed.

```
t41  The Ashfang gather at the Ashvents. Forty go out.
t43  A war band passes through the Long Gallery, heading south.     [witnessed]
t46  The Ashfang fall on the Mirelurk clan at the Black Sump.
t47  The Ashfang take the field. Nine do not come home.
t51  The Ashfang return to the Ashvents with meat and two Mirelurk tools.
```

The player who was standing in the Long Gallery at t43 saw one line of that, understood nothing, and can piece the rest together from Ovik a few ticks later. That is the information design working exactly as intended.

---

## 9. Rendering and cost

Bands are the main thing populating the world visually, so they need to be cheap.

- Full simulation and rendering only in the party's chamber and the ones adjacent.
- Beyond that, bands are positions on the graph with no visual representation — but they still emit audio cues at range, because sound is the sensing layer.
- A band entering the party's chamber instantiates properly.
- Cap concurrent bands at roughly twelve. Four camps rarely field more than three at once.

---

## 10. Test conditions

1. **Commitment is real.** A camp with a band out must have reduced garrison, and a raid against it must be measurably easier.
2. **Bands can be intercepted.** Blocking a route mid-journey turns a band back, and standing drops.
3. **Empty camps are robbable.** Verify the party can steal from a camp whose garrison is out, and that the returning band reacts.
4. **Timing is legible.** From first sighting a war band to its arrival at the target, a player must have at least 4 ticks — 6 minutes — to act.
5. **Audio warning works.** A war band two chambers away must be audible before it's visible.
6. **Force-march home.** Attack a camp with a band out; the band must abort and return.
7. **No teleporting outcomes.** Assert that no standing change, prey reduction or casualty occurs without a band physically present.

Test 7 is the one that matters. It's the whole document as a single assertion.

---

## 11. Tuning constants

| Constant | Value | Controls |
|---|---|---|
| `TUNNEL_TRAVERSE` | 0.6–1.4 ticks | Per chamber, terrain-dependent |
| `HUNT_WORK` | 2 ticks | |
| `ASSAULT_WORK` | 1 tick | |
| `SETTLE_WORK` | 3 ticks | |
| `MIGRATE_PER_TUNNEL` | 2 ticks | |
| `BAND_HUNT_SHARE` | 0.25–0.40 | Of garrison |
| `BAND_RAID_SHARE` | 0.50–0.70 | Of garrison |
| `FORCE_MARCH_SPEED` | 2× | Returning to a home under attack |
| `FORCE_MARCH_PENALTY` | −30% for 3 ticks | |
| `BAND_NOISE_HUNT` | 5 | |
| `BAND_NOISE_WAR` | 9 | Audible two chambers out |
| `MAX_CONCURRENT_BANDS` | 12 | |
| `PROVISION_PER_MEMBER` | 0.5 food per tick travelled | |

---

## 12. Build order

1. Band entity and the COMMIT → TRAVEL → WORK → RETURN → ARRIVE cycle, headless. Verify the chronicle still reads like history with delays in it.
2. Garrison-aware strength. Verify camps become vulnerable while acting.
3. Interruption: blocked routes, force-march, starving bands.
4. Audio cues at range.
5. Rendering bands in and adjacent to the party's chamber.
6. The new party verbs: follow, intercept, warn, ambush.
7. Test conditions in §10.

Step 1 can be validated entirely in the headless simulation before any 3D work exists, which is where it should be proven.
