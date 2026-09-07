# Standing Order — Layer Two: Politics and Faith

*Build specification, v0.1. Written to be implemented from, not read for pleasure.*

Layer one (ecology, hunting, growth, expansion, raiding) is built and running. This document specifies what sits on top of it. Field names match the existing simulation where they already exist.

---

## 1. Where this sits in the tick

Layer one's tick is: **sense → score → pick → resolve → propagate → log.**

Layer two adds two steps and extends three:

```
1. SENSE      + read relations, alliances, faith, leadership
2. SCORE      + diplomatic actions, gated by intelligence tier
3. PICK       unchanged
4. RESOLVE    + settle diplomatic actions before violence
5. PROPAGATE  + move standing, loyalty, faith
6. SUCCESSION (new) leadership challenges resolve
7. FAITH      (new) erosion checks, breaks, schisms
8. LOG        unchanged
```

Order matters. Succession runs *after* the tick's outcomes so a leader can be deposed for what just happened. Faith runs last so a break registers on the tick that caused it.

---

## 2. Relations

### Data

Standing is **asymmetric** — A's opinion of B is not B's opinion of A. Store as a map keyed by pair-with-direction.

```
standing[from][to] : float, range -100 .. +100
```

Every camp has an entry for every other camp and for `party`.

| Band | Range | Meaning |
|---|---|---|
| Blood | −100 to −60 | Will raid on sight, ignores march cost |
| Hostile | −59 to −25 | Raids readily, refuses parley |
| Wary | −24 to +14 | Default. Trades reluctantly, no help |
| Friendly | +15 to +49 | Trades freely, shares rumours, warns of danger |
| Bound | +50 to +100 | Alliance eligible (see §5) |

### Starting values

Camps start at a value derived from four hundred years of coexistence, not at zero:

```
standing[a][b] = -10 + 12*(territories do not touch) - 8*(shared border)
                 + creedModifier(a, b)
```

Standing toward `party` at tick zero is set by creed alone:

| Creed | Starting standing toward the party |
|---|---|
| Devout | +35 |
| Opportunist | +5 |
| Indifferent | 0 |
| Rival faith | −30 |

This is what makes camps behave inexplicably in Act II. They are reacting to a prophecy the player has not heard.

### What moves standing

Applied in PROPAGATE. All values are per event unless marked per tick.

| Event | Effect on the aggrieved party's standing | Effect on observers |
|---|---|---|
| Hunted in a chamber the other holds | −3 per tick, capped −18 per chamber | — |
| Settled a chamber adjacent to their holdings | −6 | — |
| Raided them | −25 | −5 |
| Seized a holding from them | −15 | −4 |
| Blocked a tunnel they depend on | −20 | — |
| Gift of food | +4 per unit, cap +20 per tick | +1 |
| Gift of a tool or weapon | +18 | +2 |
| Shared a rumour they didn't have | +5 | — |
| Fighting a camp they are Hostile toward | +2 per tick | — |
| Betrayal (see §6) | −60 | −30 |
| Stealing from stores, seen | −30 | −6 |
| Broke a taboo in their sacred ground | −25, and faith erosion (§8) | — |

**Decay.** Every tick, standing moves 1.5% toward that pair's baseline. Grudges fade; they don't vanish. Blood-band standing decays at half rate.

**Observers** are all living camps other than the two involved, and only if they could plausibly know — which means within two chambers, or after Ovik has passed through. Information latency is a feature: a camp can be friendly toward someone who betrayed a neighbour three chambers away, until the news arrives.

---

## 3. Hierarchy

### Data

Each camp gains:

```
leader   : { name, temper 0..1, ambition 0..1, tenure int }
notables : [ { name, temper 0..1, ambition 0..1, loyalty 0..100 }, ... ]  // 2-3
```

`camp.temper` (already used by layer one's raid scoring) becomes **derived from the leader**, not a fixed camp property. This is the whole point: a succession changes how the camp behaves.

Names are generated per camp from a per-culture syllable table. They need to be memorable enough that the chronicle reads like a history.

### Loyalty

Notable loyalty moves in PROPAGATE:

| Condition | Loyalty change |
|---|---|
| Camp won a raid this tick | +4 |
| Camp lost a raid this tick | −7 |
| Camp starved this tick | −6 |
| Camp gained a holding | +5 |
| Camp lost a holding | −8 |
| Camp is well fed (food > pop × 1.5) | +2 |
| Faith broke (§8) | −15 |
| Otherwise | +1 drift toward 60 |

Clamp 0..100.

### Succession

Runs in step 6. For each notable:

```
challengeScore = notable.ambition * 100 - notable.loyalty + noise(±8)
if challengeScore > 45 and leader.tenure > 6:
    challenge
```

Resolution is a single weighted roll against `leader.ambition * 60 + meanLoyalty(notables) * 0.4`. Two outcomes:

**Challenger wins.** They become leader. `camp.temper` becomes their temper. The deposed leader either leaves (removed) or becomes a notable with loyalty 0 — which usually means another challenge shortly. Standing toward all other camps shifts by ±10 randomly: a new leader is an unknown quantity.

**Challenger loses.** They are removed. Remaining notables lose 10 loyalty. `leader.tenure` resets.

Either way, log it. `"Vekk the Quiet takes the Ashfang. The old chief is not seen again."`

### Why this matters mechanically

A camp that keeps losing raids gets a new leader, and if that leader's temper is low, the camp stops raiding entirely. Player-visible behaviour change with no scripting: **the war ends because someone else is in charge now.**

---

## 4. Intelligence tiers

`camp.intelligence : 0 | 1 | 2`. This gates which actions appear in the score table. Everything else about scoring is unchanged.

| Tier | Camps | Actions available |
|---|---|---|
| 0 | Ashfang | Layer one only: hunt, forage, fortify, grow, migrate, settle, raid, scout |
| 1 | Sporewardens, Assayers | + gift, parley, ally |
| 2 | Mirelurks | + tribute, betray, incite |

One AI, longer menu. Do not write a second decision-maker for clever camps.

---

## 5. Diplomatic actions

All resolve in step 4, **before** raids, so a truce accepted this tick prevents this tick's violence.

**`gift:<target>`** — send food. Cost: 10–20% of stores. Score rises with hunger of the target (they know), with standing already being positive, and when the camp is at war with someone else and wants a friend. Effect per §2.

**`parley:<target>`** — propose a truce. Only available if `standing[self][target] > -50`. Target accepts if their standing toward self is > −20 and they are not currently Blood. A truce sets a `truce[pair] = tick + 15` marker; raids between the pair score −5 while it holds. Breaking a truce early is a betrayal (§6).

**`ally:<target>`** — only if mutual standing ≥ +50. Creates `alliance[pair]`. Effects while it holds:
- Neither can raid the other (score forced to −99)
- If one is raided, the other's raid score against the aggressor gains +1.2
- Hunting in each other's ranges no longer counts as poaching
- Food flows: if one is starving and the other has surplus, an automatic gift each tick

**`tribute:<target>`** (tier 2) — demand food under threat. Available if `strength(self) > strength(target) * 1.4`. Target complies if the strength gap is real and their standing is above Hostile; complies at a cost of 12 standing and 15% of stores. If they refuse, the demander's raid score against them gains +1.5 for the next 5 ticks.

**`incite:<a>,<b>`** (tier 2) — spend a rumour to worsen relations between two other camps by 15 each. Costs nothing material. If discovered (20% per tick while it persists, higher if Ovik has been through), both targets drop 35 standing toward the inciter. **This is the Mirelurks' signature move and it should be the most dangerous thing on the map.**

---

## 6. Betrayal

Betrayal is not a separate action. It's a *classification* applied when a camp does violence to someone it had an obligation to:

- raids an ally
- raids inside an active truce
- seizes a holding from a camp at Friendly or better
- refuses to honour an automatic alliance food transfer while in surplus

Effects: the standard raid penalties, **plus** −60 to the victim, −30 to every observer, and a `betrayer` flag on the camp for 40 ticks that halves the effectiveness of all its diplomatic actions.

Scoring: an ambitious leader with high temper will take a betrayal when the material gain is large enough to clear that cost. It should be rare, and when it happens the chronicle should make it feel like a rupture.

---

## 7. Creed

`camp.creed : 'devout' | 'opportunist' | 'indifferent' | 'rival'`

Creed does three things:
1. Sets starting standing toward the party (§2)
2. Determines whether the camp has a `faith` value at all — only `devout` and `rival` do
3. Changes how the camp *interprets* the same event

Interpretation table for a single event — the party hunts out a chamber:

| Creed | Reading | Mechanical effect |
|---|---|---|
| Devout | A sign; testing or judgement | faith −12, standing unchanged |
| Opportunist | Leverage over the devout | standing −5, incite score +0.4 |
| Indifferent | Vermin | standing −8 |
| Rival | Confirmation of heresy | standing −15, faith(rival) −8 |

Extend this table per beat type. It is the cheapest possible way to make four camps feel like four cultures.

---

## 8. Faith

`camp.faith : 0..100`, only for devout and rival creeds. Starts at 70 (devout) / 55 (rival, meaning firm conviction the party is false).

### Erosion

| Event | Faith change |
|---|---|
| Party hunts in the camp's sacred chamber | −12 |
| Party breaks a taboo of that camp | −20 |
| Party promises something and fails to deliver within 20 ticks | −18 |
| Party is seen allied with a camp this one is Hostile toward | −10 |
| Party damages the Cistern | −25 |
| Party gifts food while the camp is starving | +8 |
| Party defends the camp, or the camp's enemy is raided after the party is asked | +12 |
| Party tells them the placard is a maintenance notice | −40 |
| Drift | +0.5 per tick toward 70 |

**Every erosion event logs at the time**, in language the player cannot yet interpret. `"The Sporewardens mark the day."` The player scrolls back later and finds the exact moment.

### The break

When `faith < 25`, the camp enters **zealot** state. It does not renounce the prophecy. It concludes the party is a false claimant.

Zealot effects on scoring:

```
hunt, forage, grow, settle, migrate   × 0.2
fortify                                × 0.5
pursue:party                           = 3.0 + (25 - faith) * 0.04
raid (other camps)                     × 0.3
```

The camp will hunt the party while starving. That is the point. Population declines every tick it stays in fervour, its holdings go unworked, and its neighbours' balance shifts — the fallout is regional, and the player caused it.

Zealots kill. This is the one exception to the capture rule in the mechanics document, and it is what makes a faith break frightening rather than inconvenient.

### Schism

2–4 ticks after a break, roll once. On success (80%), the camp splits:

- 25–40% of population leaves as a new camp
- New camp inherits culture, one holding (the smallest), creed `devout`, faith 60
- Standing toward the party: +40
- Standing between the two halves: −70 both ways, and they are eligible to raid each other

The remnant is small, weak, permanently loyal, and the party's only route back into that territory. Without it, one mistake locks players out of a third of the map. **The schism is not flavour, it is the escape valve.**

### Atonement

Available to a zealot camp's hardliners, expensive on purpose:

```
requires: gift food ≥ 3× the camp's daily upkeep, in at least 3 separate gifts
          across ≥ 15 ticks
          AND no erosion event during that window
effect:   faith += 12 per qualifying gift
```

Hardliners read atonement as further proof of deceit: while a camp is in fervour, each gift also raises `pursue:party` by 0.15 for 5 ticks. Doing the right thing makes the immediate danger worse before it makes it better.

---

## 9. The party as a faction

The party is an entry in every table above. Specifically:

- `standing[camp][party]` exists for all camps
- The party has no `standing` of its own — players hold their opinions themselves
- The party occupies a chamber, hunts using layer one's hunting code, and counts as a poacher
- The party holds no territory and cannot be raided in the layer-one sense; camps that want to act on the party use `pursue:party`, which resolves as an encounter (capture rules per the mechanics document)
- The party can be a target of `tribute` and a beneficiary of `gift`
- The party cannot formally `ally`, but a camp at Bound standing behaves as an ally: it warns, shelters and shares

---

## 10. Log lines

Layer two must produce readable chronicle entries or none of it is visible. Minimum set:

```
POLITICS  "The Mirelurk clan send meat to the Assayers."
          "The Ashfang demand tribute of the Sporewardens, and are refused."
          "The Sporewardens and the Mirelurk clan come to terms."
          "Word spreads that the Mirelurks set the Ashfang against the Assayers."
BETRAYAL  "The Mirelurk clan raid the Sporewardens, their own allies. It is not forgotten."
SUCCESSION "Vekk the Quiet takes the Ashfang after the third failed raid."
          "Ordek's challenge fails. The Ashfang close ranks."
FAITH     "The Sporewardens mark the day."                  (erosion, opaque)
          "The Sporewardens no longer speak of the sign."   (faith < 40)
          "The Sporewardens name the fallen false."          (break)
          "A remnant of the Sporewardens keeps the old reading."  (schism)
```

---

## 11. Test conditions

Automated, run on every build.

1. **Thousand-tick no-player test.** Run 1,000 ticks with no party. Every camp must be alive at the end. If not, the starting state is wrong — see the four-hundred-year principle in the mechanics document.
2. **Diplomacy fires.** Across ten seeds × 300 ticks, at least one gift, one parley and one alliance must occur.
3. **Succession fires.** At least one leadership change across ten seeds, and no camp may have more than four in 300 ticks (that would mean loyalty is broken).
4. **Betrayal is rare.** Fewer than one per 300 ticks per seed on average, and never zero across ten seeds.
5. **Faith is stable without a player.** With no party, no camp may enter zealot state. Faith only breaks because of the players.
6. **Schism recovers.** In every case where a break occurs, a remnant must exist or the camp must die. No permanently unreachable territory.

---

## 12. Tuning constants

Collected for one place to edit.

| Constant | Value | What it controls |
|---|---|---|
| `STANDING_DECAY` | 0.015 / tick | How fast grudges fade |
| `BLOOD_DECAY_MULT` | 0.5 | Deep hatred fades slower |
| `ALLY_THRESHOLD` | +50 | Mutual standing needed for alliance |
| `PARLEY_FLOOR` | −50 | Below this, no talking |
| `TRUCE_LENGTH` | 15 ticks | |
| `BETRAYAL_PENALTY` | −60 / −30 | Victim / observers |
| `BETRAYER_DURATION` | 40 ticks | |
| `CHALLENGE_THRESHOLD` | 45 | Succession trigger |
| `MIN_TENURE` | 6 ticks | Grace period for a new leader |
| `FAITH_START_DEVOUT` | 70 | |
| `FAITH_BREAK` | 25 | Zealotry threshold |
| `FAITH_DRIFT` | +0.5 / tick | Toward 70 |
| `SCHISM_DELAY` | 2–4 ticks | |
| `SCHISM_CHANCE` | 0.8 | |
| `SCHISM_SPLIT` | 0.25–0.40 | Share of population leaving |
| `ATONE_GIFTS` | 3 | Minimum separate gifts |
| `ATONE_WINDOW` | 15 ticks | |

---

## 13. Build order within layer two

1. Relations matrix and decay. Nothing else works without it. Verify grudges form and fade.
2. Log lines for standing changes, so the rest is debuggable.
3. Hierarchy and succession. Verify leaders change and camp behaviour visibly changes with them.
4. Intelligence tiers and the tier-1 actions (gift, parley, ally).
5. Tier-2 actions (tribute, betray, incite).
6. Creed and the interpretation table.
7. Faith, erosion, and the break.
8. Schism and atonement.
9. Run the test conditions in §11.

Steps 1–3 are the foundation. Steps 7–8 are the payoff. Do not build 7 before 3, because a faith break with no hierarchy has nothing to split.
