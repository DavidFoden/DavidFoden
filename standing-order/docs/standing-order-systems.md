# Standing Order — Systems

*Tech, items, dialogue and character creation. Build specification, v0.1.*

These four were named in earlier documents and never specified. None of them is large, but items and tech are load-bearing for two other systems each, so they need to be right.

---

# PART 1 — The tech track

## 1.1 Why it exists

Because **the party is a tech vector**. Drop a quiver, trade a knife, get captured while holding a hatchet, and eight ticks later somebody is using it on somebody. It is the funniest consequence system in the design and it costs about thirty lines of code.

It also does something quieter and more important: it makes four hundred years of decline visible. These camps are *worse* at things than their ancestors were. Tech can be lost.

## 1.2 The ladder

Five steps. Every camp sits somewhere on it.

| Level | Name | What it means | Effect |
|---|---|---|---|
| **T0** | Stone and bone | Baseline. Everyone starts at least here | — |
| **T1** | Fire discipline | Cooking and torches | `MEAT` +25% for that camp; hunting at range in dark chambers |
| **T2** | Hafted tools | Proper spears, axes, mattocks | `strength` ×1.15; clearing work −1 tick |
| **T3** | Missiles | Bows and slings | `strength` ×1.35, and raid casualties taken −30% (they fight at range) |
| **T4** | Dwarven metal | Working the Ember Galleries | `strength` ×1.6, tools no longer degrade, can force dwarven mechanisms |

**Starting levels:** Sporewardens T1 · Ashfang T1 · Mirelurks T2 · Assayers T2.

The Ashfang being lowest and hungriest is the entire engine of the system. They have the most to gain and the fewest scruples about how.

## 1.3 Advancing

Each camp holds `techProgress : 0..100` toward its next level. At 100 it advances and progress resets.

| Source | Progress |
|---|---|
| **Prosperity** — food > pop × 2 for 10 consecutive ticks | +8 per qualifying tick |
| **Observation** — witnessed another camp using the next level | +12 per sighting, max once per 5 ticks |
| **Loot** — acquired a tool of the next level (gift, theft, capture, battlefield) | +45 immediately |
| **The Ember Galleries** — holding it | ×2 on all progress toward T4 only |
| **Being taught** — the party demonstrates deliberately | +30, and standing +10 |

**Imitation rate is a camp trait**, not a constant. The Ashfang learn by watching at 1.5×; the Sporewardens at 0.6× because they have never needed to. Intelligence tier does not govern this — a dim camp can be an excellent copyist, which is exactly the Ashfang.

## 1.4 Losing it

**Tech regresses**, and this is the part that makes the setting work.

- A camp routed to `MIN_POP` loses one level if it has been above T1 for fewer than 40 ticks. The people who knew how are gone.
- Losing the Ember Galleries drops a T4 camp to T3 within 20 ticks. There is nowhere else to work metal.
- A camp in fervour loses progress at 5 per tick. Zealots do not maintain anything.

Nobody in Deepholt is climbing steadily. They oscillate, and they are all lower than their ancestors.

## 1.5 The consequences that matter

**B30 (The gift that shoots back).** Give the Ashfang anything and it comes back. Guaranteed, not random — the only variable is who they use it on and how long it takes.

**B31 (The imitation).** A camp that advanced by observation rather than loot has reproduced the thing badly. It works, mostly. 10% of uses injure the user, and **they blame the party**, because the party is where they saw it.

**B32 (The arms race).** Two camps reach the same level within 15 ticks and both know it. Mutual raid scores up, and the Ember Galleries become contested ground.

**Capture is a tech transfer.** Everything carried enters the captor's stores, which is a +45 progress event. **Getting caught while armed is how you accidentally arm your enemy** — and players will do it, and it should be devastating and funny in equal measure.

---

# PART 2 — Items and trade

## 2.1 The principle

**Value is not a number. Value is who wants it.**

There is no currency in Deepholt and there should never be one. A dwarven pipe is scrap to the Sporewardens, a weapon-haft to the Ashfang, an instrument to the Assayers, and stock to the Mirelurks. One object, four prices. That single rule makes trade a puzzle about people rather than a shop.

## 2.2 The list

Carry slots in brackets. Six slots per peasant.

**Food**
| Item | Slots | Notes |
|---|---|---|
| Fresh meat | 2 | Spoils in 8 ticks unless cooked |
| Cooked meat | 2 | Keeps 40 ticks. Requires fire |
| Foraged fungus | 1 | Poor, keeps forever, nobody wants it in trade |
| Preserved fish | 1 | Mirelurk staple. The nearest thing to currency |

**Tools — yours**
| Item | Slots | Use | Tech |
|---|---|---|---|
| Pitchfork | 2 | Reach weapon, prop a roof | T2 |
| Hatchet | 1 | Weapon, cut timber, break boards | T2 |
| Mattock | 2 | Haul rubble at double speed | T2 |
| Rope | 1 | Climb, prop, carry a friend one-handed | T1 |
| Sack | 1 | +2 carry slots for whoever holds it | T0 |
| Snare | 1 | Placed and left. Quiet food | T1 |
| Firestriker | 1 | Fire without hunting for materials | T1 |

**Dwarven scavenge**
| Item | Slots | Use | Who wants it |
|---|---|---|---|
| Pipe length | 2 | Lever, weapon, forces mechanisms | Ashfang (weapon), Assayers (instrument) |
| Channel marker | 1 | Faintly luminous. Portable light | Sporewardens (sacred), Mirelurks (sellable) |
| **Sluice key** | 1 | **Required to move the Cistern gates** | Everyone, desperately |
| Plate fragment | 1 | A piece of dwarven text | Assayers, Tallow, and anyone devout |
| Cutting tools | 2 | T4 metal. Weapon and workshop | Ashfang above all |
| Silt rake | 1 | Clears a blocked channel | Nobody knows what it is |

**Tokens**
| Item | Slots | Use |
|---|---|---|
| Proof of a deed | 0 | A trophy from a named kill or a completed promise. Makes a claim provable |
| A debt marker | 0 | Mirelurk. Physical, transferable, and they will honour whoever holds it |

## 2.3 The sluice key

**The single most important object in the game.** The Cistern gates cannot be moved without one, which means the ending cannot be reached without one.

There are three in Deepholt: Tallow has one and will not explain why; one is in the Ember Galleries, which usually means an Ashfang camp is sitting on it without knowing what it is; the third is held by whichever camp most recently made a pilgrimage to the Cistern.

That distribution guarantees the endgame runs through at least one relationship. **It cannot be soloed by exploration**, which is the point.

## 2.4 What camps will trade

Per-camp valuation. Numbers are gift-equivalents for the standing calculation in the master document.

| Item | Sporewardens | Ashfang | Mirelurks | Assayers |
|---|---|---|---|---|
| Cooked meat | 2 | **4** | 2 | 3 |
| Preserved fish | 1 | 2 | 1 | 2 |
| Foraged fungus | 0 | 1 | 0 | 1 |
| Hatchet / cutting tools | 1 | **6** | 3 | 2 |
| Pipe length | 0 | 4 | 2 | **5** |
| Channel marker | **5** | 0 | 3 | 2 |
| Plate fragment | **6** | 0 | 4 | **7** |
| Sluice key | 4 | 1 | **8** | 5 |
| Rope, sack, snare | 1 | 2 | 2 | 1 |

Read the columns and the cultures fall out of them. The Ashfang want weapons and food and nothing else. The Assayers pay most for text, because verification is their whole function. The Mirelurks are the only camp that values the sluice key correctly, which tells you they understand the endgame better than anyone.

**Giving a weapon-grade item to the Ashfang is worth 6 standing and starts a countdown.** The system should let players feel that trade clearly and take it anyway.

## 2.5 Trade rules

- **Camps trade only at Wary or better.** Below that, they take.
- **A camp will not trade away its only tool of its current tech level.**
- **Mirelurks trade at any standing above Hostile**, and will buy things they have no use for on the assumption someone else will want them. They are the market.
- **Trade is a band action** — a gift or trade requires physical delivery, and can be intercepted (see the embodiment document).

---

# PART 3 — Dialogue

## 3.1 Structure

Fragments with slots, assembled at runtime. Not written conversations.

```
fragment = {
  id,
  slot:      'greet'|'refuse'|'agree'|'grievance'|'rumour'|'demand'|
             'warn'|'part'|'react',
  speaker:   campKey | 'ovik' | 'tallow',
  role:      'leader'|'notable'|'any',
  creed:     creed | null,
  standing:  band | null,        // Blood/Hostile/Wary/Friendly/Bound
  condition: worldPredicate | null,   // e.g. lostRaidWithin(4), starving(), techJustGained()
  text:      "..."               // with {slots} for names, chambers, numbers
}
```

**Assembly:** for each slot the conversation needs, filter fragments by speaker, role, creed, standing band and condition, then take the **most specific match** — the one satisfying the most non-null filters. Ties break randomly.

Roughly 200 fragments — eight slots × four speakers × six or seven variants — yields thousands of distinct exchanges once standing, creed and world state combine.

## 3.2 The one hard rule

**Every exchange must surface at least one fact the player could not have got by looking.**

A grievance, a price, a rumour about a third camp, a fear, a name. If a conversation would be pure flavour, cut the conversation — flavour is what the chronicle and the room tone are for.

Mechanically: every assembled conversation must emit at least one `fact` into `party.knowledge`. **Assert this in tests.** It is the cheapest possible guard against dialogue becoming wallpaper.

## 3.3 Voice

Four registers, and they must be distinguishable with the speaker's name removed. That is the test.

**Sporewardens** — plural, communal, gentle. They say *we* when they mean *I*. Long sentences, no irony, and they apologise for things that are not their fault.

**Ashfang** — short. Verbs and nouns. They repeat the last thing you said back at you as a question when they do not understand it, which is often.

**Mirelurks** — precise, warm, and always already negotiating. Every sentence has a hook in it. They use your name more than anyone, because it is worth something.

**Assayers** — formal and procedural. They speak about you in the third person while you are standing there, as though filing a report. Nothing is personal, which is somehow worse.

**Tallow** — answers exactly the question asked, never the question meant. Short. Declines to speculate.

**Ovik** — a salesman's warmth over a ledger's memory. Tells you the ending of the story first and charges for the middle.

## 3.4 Runtime generation

**Stays off the critical path.** If added later it writes garnish — descriptions, small talk, texture — and **never facts**, because a hallucinated grievance corrupts the political state the player is reasoning about.

The test: could a generated line change what a player believes about the world? If yes, it must come from a fragment.

---

# PART 4 — Character creation

## 4.1 Scope

Two minutes, before the fall. Name, look, and a trade you had above.

**The trade grants a tool and one small verb improvement. It never grants a stat.** Nobody is better at fighting, carrying or surviving. They are better at one specific *thing they used to do for a living*, which is exactly the joke.

## 4.2 The trades

| Trade | Starting tool | What it means |
|---|---|---|
| **Thatcher** | Rope | Props a fissure in 2 ticks instead of 3 |
| **Swineherd** | Snare | Reads tracks with direction and age, not just presence |
| **Miller's lad** | Sack | +2 carry slots |
| **Hedge-priest** | — | **Reads a little.** Gets a partial, error-strewn reading of any plate fragment — enough to know it is mundane, not enough to know why |
| **Poacher** | Snare, firestriker | Sneaks at 25% less noise |
| **Smith's apprentice** | Hatchet | Forces dwarven mechanisms without a pipe |

Six is enough. Four players will overlap and that is fine — two poachers is a legitimate party.

**The hedge-priest is the interesting one.** It gives a party a route to the truth that does not run through Tallow, and a *worse* one — a garbled half-reading that they may well misinterpret in their own direction. A party with a hedge-priest can end up with a fifth corrupted gospel, authored by themselves.

## 4.3 Names in the chronicle

Player-chosen names appear in the chronicle in the same flat register as everything else. That is the entire payoff of letting people name their own peasants:

```
t61  The Assayers and the Mirelurk clan come to terms.
t61  Bill went into the water again.
```

Make sure the party's actions are logged with the same weight and typography as the political events. The comedy is in the equivalence, and it collapses the moment the game signposts which line is the joke.
