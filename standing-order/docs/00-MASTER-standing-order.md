# STANDING ORDER
## Master design and technical specification

*v1.1 — self-contained. Everything needed to understand and build this game.*

---

# PART 0 — How to use this document

This is the complete specification. It supersedes and consolidates every other document in the set. Where another document disagrees with this one, this one is correct.

It is written to be built from. Formulas are exact, constants are named and tabulated, and every subsystem has automated test conditions. Prose explains *why* a rule exists, because a builder who understands the intent makes better decisions than one following instructions.

**The title is `Standing Order`** — bureaucratic, deadpan, and it puts the joke and the premise in two words. The earlier working title, *Those Who Fell*, survives in-world as the gospels' phrasing.

**Other proper nouns are provisional.** The ruin, the camps, the chambers, the species. No system depends on any name.

**Status.** Layer one is implemented, running, and passing its foundational test. Layers two, three and four are specified but unbuilt. The embodiment model in Part 8 amends layers one to three and is not yet implemented.

---

# PART 1 — The game

## 1.1 What it is

A real-time, first-person, online co-op game for two to four players. You are peasants. An earthquake opened the ground beneath your village and dropped you into a dwarven ruin sealed for four hundred years. Four cultures live down there. All of them are stronger than you. Two of them think you were foretold.

You are trying to get out.

## 1.2 The differentiator

**The pitch, in one sentence:** the goblins hunted the ridge too hard, so the dragon starved — and nobody wrote that.

The underground co-op space is thoroughly worked, and Deep Rock Galactic owns it. Every competitor generates a world and then leaves it inert: the caves wait for you. This one doesn't. Four camps run a full simulation of hunting, ecology, territory, politics, succession and faith whether players are present or not.

**The rule for every design decision:** if you deleted the camps, would this feature still work? If yes, it is the wrong feature.

**Never lead the pitch with the setting.** Lead with consequence. "Co-op underground caves with goblins" loses to Deep Rock Galactic before anyone hears the good part.

## 1.3 Tone

Deadpan on two tracks at once. The chronicle records four centuries of collapse, three faction wars and a usurpation among the Ashfang — and also that Bill traded his boot for a glowslug. Same register, same timestamps.

**We never write jokes.** The comedy is structural: enormous politics, unqualified protagonists, one shared log.

## 1.4 Non-goals

- **No combat progression.** Fighting exists (4.1a), but there is no damage curve, no levels, no boss. A peasant with a hatchet on tick one is as dangerous as one on tick four hundred. What improves is your position, not your power.
- **No plot.** The story is assembled per playthrough from authored situations the simulation triggers.
- **No mining.** The digging genre is saturated. The earthquake is impersonal; nobody dug anything.
- **No PvP.** The party is one faction.

There will be constant pressure to add each of these. Every individual step is reasonable and the destination is a worse version of a game that already exists.

---

# PART 2 — The world

## 2.1 Setting

**Deepholt** is not a fortress. It is a sealed biosphere: cisterns, air shafts, fungus farms, livestock pens. The dwarves built it, then died or left. The system kept running unattended for four hundred years.

Every creature down there descends from dwarven labour, livestock or vermin. They are all fighting over the remains of infrastructure none of them can rebuild.

**The village of Marrowing** sits above, on land owned by **Count Doudelfas**. An earthquake opens a pitfall. Four villagers go down. The way back collapses behind them.

**The earthquake also cracked the seal.** Tick zero is the players' arrival. For four centuries the cavern held equilibrium; it stops holding on the day they land in it.

**Nobody is coming.** The village does not know and does not care — they were peasants, and nobody above notices they are gone. There is no rescue clock and no outside pressure of any kind. This is correct for the tone, it reinforces the isolation, and it means the endings turn purely on the Cistern and on who the party backed.

## 2.2 The map

Sixteen chambers, twenty-five tunnels. No dead ends, and no single tunnel whose collapse cuts off any part of the map. Every camp is reachable by at least two routes, so encounter order depends on which way a group turned, not on level design.

Distances from the entry point: Ashfang 2 hops, Sporewardens 3, Mirelurks 4, Assayers 4.

### Chamber table

| key | Name | def | Flora | floraCap | Prey | preyCap | prey0 | Apex |
|---|---|---|---|---|---|---|---|---|
| `fissure` | The Fissure | 0.1 | rubble weed | 3 | — | 0 | 0 | — |
| `rubble` | Rubble Stair | 0.3 | dust fungus | 5 | rock mites | 4 | 3 | — |
| `hollow` | Grimhollow | 0.5 | pale lichen | 26 | cave rothe | 16 | 12 | — |
| `ashvent` | The Ashvents | 0.2 | ash moss | 14 | ember beetles | 11 | 7 | — |
| `ember` | Ember Galleries | 0.4 | cinder mould | 10 | slag crickets | 8 | 6 | — |
| `fungal` | The Fungal Deep | 0.1 | fungal mats | 52 | glowslugs | 30 | 24 | — |
| `terrace` | Spore Terraces | 0.2 | terrace caps | 28 | pale grubs | 18 | 14 | — |
| `cistern` | The Cistern | 0.6 | water weed | 12 | cistern shrimp | 10 | 8 | — |
| `gallery` | The Long Gallery | 0.1 | floor lichen | 4 | — | 0 | 0 | — |
| `kiln` | The Kiln | 0.4 | soot fungus | 6 | rock mites | 5 | 4 | — |
| `gate` | The Sealed Gate | 0.7 | dust fungus | 3 | — | 0 | 0 | — |
| `spine` | Dragonspine Ridge | 0.8 | stone lichen | 26 | crag goats | 15 | 12 | ridge dragon (pop 1.0, threat 0.55) |
| `weeping` | Weeping Stair | 0.2 | drip moss | 13 | cave newts | 12 | 9 | — |
| `sump` | The Black Sump | 0.3 | algal scum | 30 | blindfish | 20 | 16 | ripper eels (pop 1.4, threat 0.30) |
| `stacks` | Drowned Stacks | 0.3 | flood weed | 18 | silt crabs | 13 | 10 | — |
| `rookery` | The Rookery | 0.6 | pallid moss | 16 | gloom bats | 12 | 9 | — |

`def` is the defender's terrain advantage. `floraCap` doubles as carrying capacity and as the chamber's visual size.

### Tunnels

```
fissure–rubble   fissure–hollow   rubble–ashvent   rubble–ember
hollow–gallery   hollow–kiln      ashvent–ember    ashvent–cistern
ember–fungal     fungal–terrace   fungal–cistern   terrace–stacks
terrace–sump     cistern–gallery  cistern–weeping  cistern–sump
gallery–kiln     gallery–weeping  kiln–gate        gate–spine
spine–weeping    weeping–sump     sump–stacks      spine–rookery
gate–rookery
```

**The Rookery** exists to make the Assayers viable. Reachable only through their own ground or the Sealed Gate, it gives them somewhere to hunt that their taboo permits, while keeping them poor, remote and defensible.

## 2.3 The camps

Each exists to produce a different kind of story. If two produce the same kind, one is redundant.

| | Sporewardens | Ashfang goblins | Mirelurk clan | The Assayers |
|---|---|---|---|---|
| Home | The Fungal Deep | The Ashvents | The Black Sump | Dragonspine Ridge |
| pop / food | 13 / 38 | 12 / 34 | 11 / 32 | 5 / 16 |
| def / temper | 0.1 / 0.2 | 0.2 / 0.8 | 0.4 / 0.3 | 0.7 / 0.6 |
| Creed | **Devout** | Opportunist | Indifferent | **Rival faith** |
| Intelligence | 1 | 0 | 2 | 1 |
| Taboo | Will not burn fungus | None | Debts always collected | **The dragon's prey is not food** (`taboo: ['spine']`) |
| Dramatic role | Tragedy | Farce and escalation | Transaction | Obstacle and mirror |

Starting food represents **four hundred years of stores**, not a day's meals. It was raised sharply when embodiment made hunting a multi-tick round trip — a camp now has to eat while its band is walking home.

**Sporewardens.** Pale, near-blind descendants of the dwarven farmhands. Well fed, numerous, almost undefended — they have never needed to fight for the richest chamber in Deepholt. They help first and ask nothing, which is why disappointing them is the cruellest outcome available. Emotional spine of a playthrough.

**Ashfang.** Descended from the labour gangs. Live on thin ground, permanently one bad season from starving, and the most aggressive thing in the cavern. They copy any tool they see. Every interaction makes them more dangerous, which is funny until it isn't.

**Mirelurks.** Amphibious fishers. Trade with everyone, believe nothing, and will sell the prophecy to those who do. The only camp that negotiates as an equal.

**The Assayers.** Kobolds venerating the ridge dragon. Few, poor, extremely defensible. Their position is not that the party is false but that the party is **unverified** — nobody may be conducted who has not first been shown to the wyrm. Their taboo makes them visibly irrational, which demonstrates that devotion is how everyone down here works.

> **On the name.** An assayer tests whether a thing is what it claims to be, which is precisely their function — they do not think you are false, they think you are unverified. It also establishes a pattern the whole setting should use: **every camp is named after an inherited dwarven job.** Sporewardens tended the growing beds. Assayers checked that things were what they claimed. Four hundred years later they are all still doing their jobs and none of them know why.

## 2.4 Independents

**Tallow, the hermit of the Kiln.** No camp, no territory, and the only creature in Deepholt who can read dwarven script. The exposition valve. He will answer exactly the question you asked, and it is never the question you meant.

**Ovik the walker.** A trader on a fixed circuit — Long Gallery → Cistern → Black Sump → Weeping Stair → repeat. Carries 3–5 facts per circuit, weighted toward the dramatic, and trades them with his own spin. In a real-time game he is how the chronicle reaches players without a text dump.

## 2.5 The prophecy

Every camp holds a different corrupted copy of a text about those who fall from the ceiling. It is not a prophecy. It is dwarven maintenance documentation, recopied by illiterates for four centuries. The original plate reads:

> **NOTICE — CISTERN HEAD, PLATE 4 OF 6**
>
> In event of ceiling breach: persons entering from above are to be conducted to the cistern and the gate operated per standing order.
>
> Do not operate the gate while the beds are in growth.
>
> Channel inspection: quarterly. Report silt to the works overseer.

The second line is the controlled-drain rule, stated four hundred years before anyone needed it. The third makes it unmistakably a maintenance notice, and it is played completely straight.

The four corrupted gospels are written in full in `standing-order-gospels-and-names.md`. In summary: the **Sporewardens** added a promise of returning abundance, which is why they feed you from stores they cannot spare. The **Ashfang** version decayed to *"Roof breaks. Ones fall. Take them to the water. Then it's ours"* — and nobody remembers what *ours* means. The **Mirelurks** kept the most accurate text and appended *"The conductor is owed."* The **Assayers** lost the opening entirely, so they read it as a rule about procedure and inserted their god as the authority it must pass through.

**The prophecy is never confirmed.** It is true only in effect: the camps believe it, belief moves the simulation, the simulation produces events, the events confirm the belief.

**The camps already know.** They felt the earthquake, armed themselves, and have been arguing about the players since before they stood up. Players don't learn this for hours — everything reading as unexplained hostility or baffling generosity gets retroactively explained.

**Nobody in Deepholt has ever seen two versions side by side.** The party is the first entity in four hundred years able to compare them, which is Act II's payoff.

## 2.6 The Cistern

A header pool fed by an aquifer, and four sluice gates routing water along stone channels to each district's growing beds. **Water allocation is a multiplier on each chamber's flora regrowth.** Every ecological difference on the map traces to how those sluices were set the day the dwarves left.

Nobody has moved them in four hundred years — not because they are guarded, but because nobody understands them. That is exactly why the ecology has been stable long enough for four cultures to form around it.

**Player interventions:** *re-route* (move water between districts; receiving chambers boom over 20–40 ticks, starved ones decline, and it is almost impossible to attribute) · *block* (map-wide regrowth collapse) · *open wide* (the Sump and Stacks flood, routes close, eels spread).

**Why it is the ending.** The Sealed Gate is water-counterweighted. It opens when the header pool drops below a threshold — precisely what the placard instructed.

**And that is the trap at the centre of the game.** The dwarven evacuation procedure was a one-time last-resort act, performed by the last people leaving, when it did not matter what happened to the beds afterwards. Four hundred years later the camps have made it scripture. **Every devout camp is asking the party to perform the one act that would kill them all**, and none of them know it. The Sporewardens are not wrong that the party matters. They are wrong about what the party is for.

## 2.7 What happens if the water stops

Gradual, predictable, attributable, and reversible up to a point. It is the largest thing the players can do, and it must be possible to do without understanding it.

**Stage 1 — the channels run dry. Ticks 0–8.** `waterAllocation` decays toward zero; the stone channels hold water a while, so nothing dies yet. What changes is sound: **the running water stops, map-wide, within two ticks.** The loudest signal in the game, and every camp hears it.

**Stage 2 — the beds fail. Ticks 8–20.** Flora regrowth approaches zero, `floraStock` drains, the `fed` term collapses, herds stop breeding and decline. **The richest chambers crash first and hardest**, because they had the most biomass depending on the most water. The Fungal Deep, Black Sump and Spore Terraces fail before the Ashvents. The places that made Deepholt liveable are the places that die.

**Stage 3 — the migrations. Ticks 20–40.** Camps abandon dead ground and converge on whatever still has prey. Everyone ends up in the same few chambers with the same insufficient herds, and raid scoring does the rest.

**Stage 4 — collapse. Tick 40 onward.** Camps reach `MIN_POP` and, because this is player-caused, they can die. Apex predators starve out permanently.

### Reversibility

| Restored within | Outcome |
|---|---|
| 0–20 ticks | Full recovery over 30–50 ticks. Nothing permanently lost |
| 20–40 ticks | Flora recovers; **any prey population that reached zero does not return** |
| After 40 ticks | Extinctions permanent, apex predators gone, at least one camp will not recover |

That twenty-tick window — half an hour of play — is the difference between a mistake and an atrocity, and the player has no way of knowing where the line is the first time.

### Attribution

The water stopping is audible everywhere, so **every camp knows instantly that something happened at the Cistern.**

- Party observed at the Cistern within 10 ticks → blamed. −35 standing with every camp, −25 faith with devout camps.
- Otherwise → **each camp blames whoever it already distrusts most**, −25 toward them.

An anonymous act of vandalism starts a war between two camps that had nothing to do with it, and the party watches knowing exactly whose fault it was. The best use of the standing system in the game.

### One benefit

Draining the pool empties the flooded channel between the Cistern and the Drowned Stacks, opening a route obtainable no other way. The catastrophic act has a genuine reward, which is what makes Force a choice rather than an accident.

---

# PART 3 — Story architecture

## 3.1 Why there is no plot

A plot would fight the game. Commit to "the Sporewardens betray you in chapter three" and the simulation will starve them out on tick forty for reasons nobody scripted. Instead: **invariants**, **act thresholds**, a **beat library** (all forty specified in `standing-order-beats.md`), and **dialogue architecture**.

## 3.2 Invariants

1. **You fall.** Under two minutes from launch to standing in the dark with a pitchfork.
2. **The way back closes.** Players see daylight for a few minutes and start planning to climb out before the aftershock removes the option.
3. **The camps felt it too.** Fear spike at tick zero. The first thing overheard is panic about something that happened to *them*.
3a. **You eat before you understand.** The first kill is small, grim and successful, and it feels like relief rather than damage. The chamber stripped in hour one is returned to in hour four. Hunger must be felt as survival before it is understood as consequence, or the Act III payoff evaporates.
4. **Someone recognises you** within the first hour, for reasons you cannot understand.
5. **The Gate is the ending**, and it cannot be resolved without the Cistern.

## 3.3 Acts as thresholds

**Act I — Down here.** Landing to first sustained camp contact. Hungry, dark, something moving. **Act I's job is to make hunger teach ecology** — the consequences of eating the easy prey near the landing site arrive in Act III, when nobody remembers doing it.

**Act II — They know something.** Ends when the party learns the prophecy exists. Camps react with intensity out of all proportion and nobody explains why. Usually ended by Tallow; occasionally a Mirelurk, who charges; rarely a Sporewarden, who gets it wrong interestingly.

**Act III — Consequence.** The longest act and the real game. Ends at the first irreversible change the party caused. **That condition is something the player did, not something scheduled.**

**Act IV — The Gate.** A political question wearing a puzzle's clothes. Who do you back, and what do you owe them?

## 3.4 Beats

Forty authored situations with triggers in simulation terms. Four rules: one per tick maximum · once per playthrough unless repeatable · **beats never modify world state** · every beat needs a no-response path. A playthrough sees roughly a third.

Full library in `standing-order-beats.md`.

## 3.5 Dialogue

Assembled from four inputs: **who is speaking** (leader, notable, nobody) · **standing** (governs tone, not content) · **creed** (devout interpret, opportunists evaluate, rival faiths condemn) · **world state** (what just happened to them, raised unprompted).

**Every conversation must surface at least one fact the player couldn't have got from looking.** Pure flavour gets cut — flavour is what the chronicle is for.

~200 slotted fragments, not paragraphs. Full structure, the four voices, and the one hard rule in `standing-order-systems.md`. **Runtime AI generation stays off the critical path**; if added later it writes garnish, never facts, because a hallucinated grievance corrupts the political state the player is reasoning about.

## 3.6 Quests from world state

The simulation already knows who is hungry and for which chamber, who has a grievance and how old, which notable is close to moving, what technology a camp lacks, which chamber is collapsing, and who owes whom. Template against those facts.

Three rules: quests must be **refusable** with interesting refusal · must have a **cost to someone else** · must **chain through the world, not through a script**.

## 3.7 Endings

All at the Gate. Every one runs through the same physical act: **the header pool must drop below the Gate's threshold.** What separates them is who operates the sluices and whether the pool refills.

- **Consent.** A camp controlling the Cistern performs a *controlled drain* — gates re-routed first to protect the beds, pool dropped for the few ticks the Gate needs, then closed and refilled over ~30 ticks. Deepholt survives with a scar. Requires a Bound camp that controls the Cistern, which usually means you made them dominant.
- **Purchase.** The Mirelurks run the same controlled drain, competently, for a price you will not enjoy paying.
- **Force.** Wreck the gates. The pool drains and never refills, and you walk out through Stage 3. Available to any party at any time with no allies and no understanding — **which is exactly why it must be available.**
- **Inheritance.** You don't leave. You end up operating the waterworks, which is precisely what the placard said would happen.
- **Nobody leaves.** Starved, hunted, or pursued by a faith you broke. Genuinely reachable.

**The controlled drain is a skill test with a clock**, not a dialogue choice. The Gate needs ~6 ticks below threshold; every tick past 20 moves you toward permanent extinctions. Players who understand the sluices lose nothing. Players who panic lose the Fungal Deep.

**Every ending runs the chronicle for twenty ticks after the party's exit.** The world does not stop when you leave. That last screen is the game's whole argument.

---

# PART 4 — Player mechanics

## 4.1 The verbs

**Moving.** Walk (noise 3) · Sneak (half speed, noise 1) · Climb/crawl (gated by weight) · Flee (noise 10, burns food, drops unstowed items).

**Sensing.** **Listen** (held input — stand still, own noise to zero, world resolves into direction and distance; the primary sensor) · Look · Track.

**Eating.** Hunt (noise 7, uses the camps' own hunting code) · Forage · Set snare (quiet, slow, the correct way to feed a party that doesn't want to be noticed) · Eat · Drink.

**Handling.** Carry (6 slots) · Take · **Give** (the most powerful diplomatic verb) · Steal · Drop/stash.

**Changing the world.** **Clear** (opens an obstructed passage; 4.1b; noise 12) · **Block** (collapses or barricades; noise 14) · Build (fire, snare, barricade, marker) · Divert (Cistern only).

**People.** Parley · Trade · Lie · Threaten (almost never works; exists because players will try) · **Signal/distract** (the core co-op verb) · Carry a friend.

**Fighting.** Strike · Throw · Shove · Block. See 4.1a.

**From embodiment.** Follow · Intercept · Warn · Ambush.

## 4.1a Combat

Four people with farm tools can swing them, and should. The rule is not *no fighting* — it is **fighting does not scale**.

**Weapons are tools.** Pitchfork, hatchet, mattock, a length of dwarven pipe. Each is also the thing you carry for another purpose, so arming yourself costs carry slots.

**Numbers decide fights, not skill.** One-on-one against a lone scout is winnable. Two-on-one is comfortable. Four against a band of eight is a death sentence regardless of play. No build, no dodge mastery and no gear tier changes this arithmetic — which is what keeps diplomacy load-bearing.

**Terrain is the only multiplier.** A tunnel is narrow enough that four peasants can hold it against a band that would destroy them in the open. Ambush lands the first blows free. **This is the one place players can beat a camp**, and it should feel like a tactical victory rather than a loophole.

**Wounds are slow.** Damage reduces `condition`, which recovers over ticks with rest and food, not seconds.

**Killing is remembered.** Each camp member killed is −12 standing, permanently harder to decay, and the leader may name them. Winning a fight and losing a relationship is the normal outcome.

**Against apex predators there is no fight.** They are weather. You avoid them.

## 4.1b Opening and closing routes

Peasants cannot mine, and a game about digging is the genre we are deliberately not entering.

**The map has latent connections** — passages blocked rather than absent. **Clearing one is work, not excavation.**

| Latent connection | Obstruction | To open |
|---|---|---|
| `rubble` – `hollow` | Collapsed passage | Haul rubble. 4 ticks, two people |
| `ember` – `terrace` | Jammed dwarven door | Force the mechanism. 2 ticks |
| `cistern` – `stacks` | Flooded channel | **Only by re-routing the Cistern sluices to drain it** |
| `kiln` – `cistern` | Boarded service shaft | Break the boards. 1 tick, loud |
| `fissure` – `gallery` | Fresh unstable fissure | Prop it. 3 ticks, can collapse on you |
| `spine` – `sump` | Rockfall | Haul. 5 ticks, the longest job in the game |

`rubble`–`hollow` is the sharpest: it puts the richest unclaimed chamber inside Ashfang reach. **The flooded channel is deliberate** — one route can only be opened by understanding the Cistern, so the waterworks teach themselves before the endgame depends on them.

**Blocking** is entirely within peasant capability, takes 2 ticks, and is the loudest thing in the game.

## 4.2 Time and scale

| | |
|---|---|
| One world tick | **90 seconds real time** |
| Session | 90–120 minutes (60–80 ticks) |
| Full playthrough | 6–10 hours (250–400 ticks) |
| Party hunger | one meal per person per 6–8 ticks |
| Ecological collapse | 15–30 ticks of overhunting |
| Prey recovery | 20–40 ticks |
| Camp succession | possible from tick 40 |

**The world does not tick when nobody is playing.**

## 4.3 The four-hundred-year principle

**Tick zero is not a fresh world. It is an equilibrium that has already held for centuries.** Camp populations, territory and stores are initialised at sustainable levels for the ground they hold.

> **Run 1,000 ticks with no player. If any camp dies, the starting state is wrong.**

**Currently passing, 12/12 seeds.**

## 4.4 When they catch you

**Camps do not kill you. Camps take you.** The most important rule in the specification.

- **Incapacitation.** Enough punishment puts a peasant down, not dead. Teammates carry them at half speed with no free hands.
- **Capture.** Everything carried transfers to that camp's stores — **including tools, which is a +45 tech progress event**. Getting caught while armed is how you accidentally arm your enemy. Standing −8.
- **Four exits:** escape · ransom (another camp pays; you owe 3 gift-equivalents) · release (a Friendly camp intervenes) · labour (25 ticks; standing +20, and you live inside a camp while its politics happen around you).
- **Split capture is the primary co-op case.** Build for it first.
- **Zealots kill.** The only lethal camp state.

Otherwise death comes only from starvation, apex predators, drowning and falls. Because camps can't kill you, **starvation and predators need real teeth.**

## 4.5 Multiplayer

Host-authoritative. **No host migration in v1.** Drop-in, drop-out — a joining friend inherits whatever the others have broken; a leaving player becomes an NPC follower. **Solo play is the same game**, one player and three NPC followers, identical balance. No PvP.

**The peasants are player-made.** Light creation: name, look, and a trade they had above — a starting tool and one small verb improvement, never a stat. Six trades, specified in `standing-order-systems.md`. The hedge-priest is the notable one: it gives a party a route to the truth that doesn't run through Tallow, and a worse one, so they can end up authoring a fifth corrupted gospel themselves. Making your own idiot is part of the fun, and it makes the chronicle's use of their names land harder.

## 4.6 Information design

**The player's knowledge is a strict subset of world state, and no accessibility affordance may widen that subset.**

- **No numbers.** Standing is read from behaviour.
- **Hunger is a body, not a bar.**
- **The chronicle is a memory, not a feed.** Only witnessed or reported entries.
- **The map is drawn, not given.**
- **Sound is the primary interface.**

---

# PART 5 — Layer one: the world tick

*Implemented and passing. A browser prototype runs this.*

## 5.1 The tick

```
1. SENSE       each camp reads local state
2. SCORE       rates available actions
3. PICK        highest score, with noise
4. RESOLVE     apply all intents together
5. ECOLOGY     flora, prey and predators update
6. UPKEEP      everyone eats; starvation bites
7. PROPAGATE   outcomes write into memory
8. LOG         one plain sentence per event
```

**The player is not special to this system.** *Part 8 amends steps 3–4: intents spawn physical bands rather than resolving immediately.*

## 5.2 Sense

```
upkeep    = pop × FOOD_PER_POP
grounds   = range(camp)                    // holdings + known neighbours of holdings
huntable  = Σ preyPop over grounds, EXCLUDING taboo chambers
scarcity  = 1 − min(1, huntable / max(1, pop × 0.8))
hunger    = min(1, max(0, (upkeep×3 − food)/(upkeep×3)) × 0.6 + scarcity × 0.7)
rivals    = camps holding any chamber in grounds
open      = chambers in grounds, unheld, not home
```

**`huntable` must exclude taboo ground.** Counting food a camp refuses to eat makes it believe it is surrounded by plenty while starving. This was a real bug and it silently killed the Assayers in every run.

## 5.3 Score

```
grow    = safeGrow × (rivals ? 0.4 : 1)
          × (food > pop×1.15 AND huntable > pop×1.5 ? 1 : 0)
          × max(0, 1 − pop/16)

forage  = 0.15 + hungerForage × hunger × min(1, floraStock/12) × 0.45

fortify = 0.3  (+ lossFortify if lost a raid within 4 ticks)

scout   = curiosity × (unexplored ? 1 : 0)

hunt:k  = hungerHunt × hunger × worth − risk − (k≠home ? 0.25 : 0) − (forbidden ? 1.1 : 0)
          where need  = max(0, pop×FOOD_PER_POP×7.0 − food) / MEAT
                take  = min(preyPop×HUNT_SHARE, need)
                worth = min(1, take×MEAT / max(2, pop×FOOD_PER_POP))
                risk  = pred × apex.threat × 0.35
          skipped entirely if forbidden AND hunger < 0.75

settle:k  = expansion × (preyPop/preyCap) × min(1, pop/14) − 0.5
            gated on pop ≥ 9, food > pop×1.2, ≥10 ticks since last settle

migrate:k = hungerMigrate × hunger × (preyPop_k − preyPop_home)/max(4, preyCap_home) − 0.3

raid:r  = hungerRaid × hunger
        + weakTempts × (weakness − 0.5) × 2
        + temper × 0.6
        + lootTempts × min(1, r.food / max(4, pop×2))
        + contestedGround × (r hunted my ground last tick ? 1 : 0)
        − raidReluctance
        − marchCost × (hops(home, r.home) − 1)
        + (won within 4 ticks ? winRaid : 0)
        − (fought within 3 ticks ? warWeariness : 0)

every score += uniform(−NOISE, +NOISE)
strength(c) = pop × (1 + def)
```

**Three rules encoded here that took four rebalancing passes to find. Do not "simplify" them back out:**

1. **Score expected return, not need.** `forage` scales with remaining stock, `hunt` with expected yield. Without this, camps forage empty chambers forever and never raid.
2. **Growth is gated on carrying capacity, not current food.** Otherwise every camp breeds on a food spike and starves back down, and populations only decline.
3. **Raiding pays a march cost per hop; hunting does not.** You can hunt two chambers out; marching a war party that far is another matter. Without this, everyone raids everyone from tick four.

## 5.4 Resolve

- `grow` — pop +1, food −2
- `forage` — gain = min(floraStock×0.3, pop×0.45)
- `fortify` — def +0.15, cap 1.2
- `scout` — learn a random unexplored neighbour
- `hunt:k` — take as computed; record `huntedBy`; if apex present and `pred > 0.8`, roll `threat × 0.4` for casualties
- `settle:k` — add to `holds`, food −4
- `migrate:k` — seat moves, other holdings retained, def −0.2
- `raid:r` — battle

**Battle**

**One formula serves both the decision and the fight.** When they drift apart, camps launch raids they were never going to win — an early version had attackers losing 93% of assaults because the score compared full garrisons while the battle compared a committed band against a defender with two stacking multipliers.

```
defence(c)            = garrison(c) × (1 + c.def × 0.5 + chamber.def × 0.5)   // additive
assaultForce(c, n)    = n × (1 + c.def × 0.3) × 1.15                          // 1.15 = initiative

// the raid score uses assaultForce(camp, garrison × 0.65) against defence(target)
// the assault uses assaultForce(camp, band.members) against defence(target)
```

```
MIN_POP = 2.5

a = strength(attacker) × uniform(0.8, 1.2)
d = strength(defender) × (1 + chamber.def) × uniform(0.8, 1.2)
winner = a > d ? attacker : defender

losses    = max(1, loser.pop × uniform(CASUALTY))
wasBroken = loser.pop ≤ MIN_POP
loser.pop = max(MIN_POP, loser.pop − losses)     // camps rout, they do not die
winner.pop −= max(0.3, losses × 0.4)
if loser reached MIN_POP this fight and wasn't already there:
    loser.holds = [loser.home]                   // routed: gives up all but the seat

loot = loser.food × RAID_LOOT → transfers
loser.def −= 0.1
60% chance the winner seizes one of the loser's non-seat holdings
```

Each tick: `crashed` holdings are given up with 30% probability. **Starvation also floors at `MIN_POP`** — a camp reduced that far consumes almost nothing and subsists by foraging until its ground recovers.

**Ordinary warfare cannot exterminate a camp.** This is the mechanical expression of the four-hundred-year principle: four cultures coexisted that long precisely because none could finish the others off. A beaten camp *routs* — it loses every holding but its seat and rebuilds slowly. Defeat costs territory and dignity, never existence.

Camps can still be destroyed, but **only by the players** — a faith break driving a camp into suicidal fervour, cutting them off from food with `block`, or wrecking the Cistern. That makes the death of a camp a genuine event, always attributable to somebody.

Measured: with extermination disabled, 12/12 seeds keep all four camps alive across 1,000 ticks while still producing roughly 17 routs per seed.

## 5.5 Ecology

```
eaten      = min(floraStock, preyPop × GRAZE)
floraStock = min(floraCap, floraStock − eaten + floraCap×0.2×(1 − floraStock/floraCap))

fed        = preyPop > 0 ? min(1, eaten / max(0.1, preyPop×GRAZE)) : 0
births     = preyPop × PREY_BIRTH × fed × (1 − preyPop/preyCap)
killed     = min(preyPop, pred × PRED_KILL)
preyPop    = max(0, preyPop + births − killed)

if apex:
    wellFed = min(1, killed / max(0.1, pred × PRED_KILL))
    pred    = max(0, pred + pred × (PRED_BIRTH × wellFed − PRED_DEATH))
    if pred < 0.25 → apex starves out, logged

crashed = true  when preyPop/preyCap < 0.12
crashed = false when preyPop/preyCap > 0.45
```

### Apex migration

**Predators do not sit in an empty chamber and die.** When an apex has been underfed (`fed < 0.6`) for 3–6 ticks and a neighbouring chamber holds clearly more prey — over 1.6× its current chamber, minimum 2 — it moves there. A 10-tick cooldown after any move prevents thrashing between two chambers.

**Habitat constrains where they can go.** `apex.habitat` is `'wet'` or `'any'`. The ripper eels can only move between water chambers (the Cistern, Weeping Stair, Black Sump, Drowned Stacks); the ridge dragon goes wherever it likes.

**`MIN_PRED = 0.5`.** An apex reduced by attrition becomes a single gaunt animal that roams and can recover. It is never erased by ordinary scarcity — the same principle as camp routing, and for the same reason: a dragon has been on that ridge for four hundred years. Logged as *"the ridge dragon grows gaunt in The Rookery. One is left."*

Measured: both apexes survive 1,000 ticks in all 12 seeds, with about 5 relocations per seed.

**A predator arriving where a camp lives is a headline.** `"the Mirelurk clan now share Drowned Stacks with ripper eels."` It changes that chamber's hunting risk for everyone immediately.

### Sacred ground travels

The Assayers venerate **the animal, not the place**. `camp.venerates` names an apex, and the camp's taboo is recomputed each tick as *whichever chambers that animal currently hunts in*.

So when the dragon abandons Dragonspine Ridge for The Rookery, Dragonspine stops being sacred and The Rookery becomes forbidden — the Assayers gain a hunting ground and lose another on the same tick, without a line of scripted content. Verified in the prototype: dragon in Dragonspine at t20, in The Rookery from t40, with the taboo following it exactly.

**This is the strongest argument for the whole design.** A faith's sacred geography is redrawn by an animal following its food.

The apex predator dying because its prey was overhunted by someone else — with nobody ever attacking it — is the clearest demonstration of the whole design, and it emerged unprompted in testing.

## 5.6 Upkeep

```
food −= pop × FOOD_PER_POP
if food < 0:
    lost = min(max(0, pop − MIN_POP), 1 + |food|/4)
    pop −= lost; food = 0
```

## 5.7 Resolved: the Assayers

Previously the Assayers died in every run — their taboo forbade the goats in their own chamber, leaving one small pond next door which the Mirelurks usually settled around tick 7.

**Resolved by The Rookery.** They are now viable, typically reaching 9–14 population across two or three chambers, while remaining the poorest and most remote camp. Difficulty without doom.

The taboo still bends under starvation (`hunger > 0.75`), which remains one of the best emergent sequences the simulation produces — *Starving, the Assayers break their own law and hunt crag goats in Dragonspine Ridge.* It is now a crisis they can survive.

---

# PART 6 — Layer two: politics and faith

*Specified, unbuilt. Full detail in `standing-order-layer2-politics-faith.md`.*

## 6.1 Tick extension

```
1. SENSE       + relations, alliances, faith, leadership
2. SCORE       + diplomatic actions, gated by intelligence
3. PICK
4. RESOLVE     + diplomacy settles before violence
5. PROPAGATE   + standing, loyalty, faith
6. SUCCESSION  (new) leadership challenges
7. FAITH       (new) erosion, breaks, schisms
8. LOG
```

Succession runs after outcomes so a leader can be deposed for what just happened. Faith runs last so a break registers on the tick that caused it.

## 6.2 Relations

`standing[from][to] : −100 .. +100`, **asymmetric**. Every camp has an entry for every other camp and for `party`.

| Band | Range | Meaning |
|---|---|---|
| Blood | −100 … −60 | Raids on sight, ignores march cost |
| Hostile | −59 … −25 | Raids readily, refuses parley |
| Wary | −24 … +14 | Default |
| Friendly | +15 … +49 | Trades, shares rumours, warns |
| Bound | +50 … +100 | Alliance eligible |

**Starting standing toward the party is set by creed alone:** devout +35, opportunist +5, indifferent 0, rival faith −30. This is why camps behave inexplicably in Act II.

Key event values: hunted their ground −3/tick (cap −18) · settled adjacent −6 · raided −25 (observers −5) · seized a holding −15 · blocked a tunnel they need −20 · gift of food +4/unit (cap +20) · gift of a tool +18 · shared rumour +5 · betrayal −60 (observers −30) · stealing seen −30 · broke a taboo in sacred ground −25.

**Decay** 1.5%/tick toward baseline; Blood at half rate.

**Observers** are camps that could plausibly know — within two chambers, or after Ovik passed. **Information latency is a feature.**

## 6.3 Hierarchy

```
leader   : { name, temper, ambition, tenure }
notables : [ { name, temper, ambition, loyalty 0..100 } × 2..3 ]
```

**`camp.temper` becomes derived from the leader.** That is the point: succession changes how the camp behaves.

```
challengeScore = ambition×100 − loyalty + noise(±8)
if challengeScore > CHALLENGE_THRESHOLD and leader.tenure > MIN_TENURE: challenge
```

A camp that keeps losing raids gets a new chief, and if his temper is low the camp stops raiding. Player-visible behaviour change with nothing scripted — *the war ends because someone else is in charge now.*

## 6.4 Intelligence tiers

| Tier | Camps | Adds |
|---|---|---|
| 0 | Ashfang | Layer one only |
| 1 | Sporewardens, Assayers | gift, parley, ally |
| 2 | Mirelurks | tribute, betray, incite |

One decision-maker, longer menu. Do not write a second AI.

## 6.5 Diplomatic actions

All resolve **before** raids. `gift` · `parley` (truce, 15 ticks) · `ally` (mutual ≥ +50; no raiding, mutual defence, shared hunting, automatic food transfer) · `tribute` (tier 2, strength ratio > 1.4) · **`incite`** (tier 2, worsen two other camps' relations by 15 each; 20% per tick discovery, then −35 from both). **Incite is the Mirelurks' signature and should be the most dangerous thing on the map.**

## 6.6 Betrayal

A **classification**, not an action: raiding an ally, raiding inside a truce, seizing from a Friendly camp, or withholding an alliance transfer while in surplus. −60 victim, −30 observers, and a `betrayer` flag for 40 ticks halving diplomatic effectiveness.

Classified at the moment of assault, not decision — so a camp can march out on an honest raid and arrive as traitors because an alliance formed while they walked. **Keep this.**

## 6.7 Creed

Creed sets starting standing, determines whether the camp has faith at all, and changes how the same event is **interpreted**. For *the party hunts out a chamber*: devout reads a sign (faith −12) · opportunist reads leverage (standing −5, incite +0.4) · indifferent reads vermin (standing −8) · rival reads confirmed heresy (standing −15, faith −8).

Extend per beat type. The cheapest way to make four camps feel like four cultures.

## 6.8 Faith

`camp.faith : 0..100`. Devout starts 70; rival 55.

Erosion: hunts their sacred chamber −12 · breaks their taboo −20 · promise unfulfilled −18 · seen allied with their enemy −10 · damages the Cistern −25 · gifts food while starving +8 · defends them +12 · drift +0.5/tick toward 70.

**Telling them the placard is a maintenance notice scales with standing:**

```
standing ≥ +50   → faith −5,  and a fracture: some notables believe
+15 … +49        → faith −20, they think you mistaken, not lying
−24 … +14        → faith −40, blasphemy
< −25            → faith −40 and immediate break check
```

At Bound standing this is the most interesting conversation in the game — a devout camp genuinely reckoning with the idea that their scripture is a maintenance notice, and **a schism caused by honesty rather than betrayal.**

**Every erosion event logs at the time, in language the player cannot yet interpret.** *"The Sporewardens mark the day."*

**The break** at `faith < 25`: the camp does not renounce the prophecy, it concludes the party is a false claimant.

```
hunt, forage, grow, settle, migrate × 0.2
fortify                             × 0.5
raid (other camps)                  × 0.3
pursue:party                        = 3.0 + (25 − faith) × 0.04
```

They hunt the party while starving. Historically accurate: failed prophecy produces intensified commitment, not abandonment.

**Schism** 2–4 ticks later, 80% chance: 25–40% of population leaves as a new camp, creed devout, faith 60, standing +40 toward the party, −70 both ways with the parent. **The schism is the escape valve** — without it, one mistake locks players out of a third of the map.

**Atonement** — ≥3 gifts totalling ≥3× daily upkeep over ≥15 ticks with no erosion. Each is faith +12, **and raises `pursue:party` by 0.15 for 5 ticks**, because hardliners read it as further proof of deceit.

---

# PART 7 — Layer three: the party as a faction

*Specified, unbuilt. Full detail in `standing-order-layer3-party.md`.*

## 7.1 Two clocks

**Continuous layer** owns movement, noise, detection, animals in the party's chamber, encounters, capture, carrying, fire, and every verb's immediate effect. **Tick layer** owns everything in layers one and two.

Bridged by an accumulator:

```
pendingWorldEffects = {
  preyTaken:{chamber:amount}, floraTaken:{chamber:amount},
  tunnelsOpened:[[a,b]], tunnelsBlocked:[[a,b]],
  poachedIn:{chamber:[ticks]}, giftsGiven:{camp:{food,tools}},
  sluiceChanges:[], noiseEvents:[{chamber,magnitude,tick}],
  observedBy:{camp:[events]}
}
```

**The party's effects are immediate; the world's response is not.** Kill a glowslug and the count drops that second; the Sporewardens don't notice until the tick. **That delay is where the drama lives** — the damage is always already done before anyone reacts.

## 7.2 Data model

```
party = { chamber, peasants[2..4], stores{food,tools}, knowledge,
          promises[], capturedBy, reputation }
peasant = { name, playerId|null, hunger 0..100, condition 0..100,
            carried[≤6], state:'ok'|'down'|'held', noise }
```

The party has **no standing of its own**; only `standing[camp][party]`. `playerId: null` is an NPC follower with identical stats.

## 7.3 Hunger

41–65 listening −25% · 66–85 carry −2 and sneaking noise +40% · 86–99 condition drains, no climbing · 100 condition drains fast.

## 7.4 Noise and detection

Sneak 1 · forage/snare 2 · walk 3 · fire 4 continuous · hunt 7 · brawl 9 · flee 10 · **clear 12** · **block 14**.

**The two verbs that permanently change the map are the two loudest** — clearing rubble and collapsing a tunnel are both jobs you cannot do quietly.

```
noticed = magnitude / (1 + tunnelDistance²) > camp.alertness
```

`alertness` falls with standing and rises in fervour.

## 7.5 Promises

Kept: standing +15, faith +10. Broken: −20, −18. **Silently unkept resolves anyway — camps notice absence.** The main way a player damages a relationship by doing nothing at all.

## 7.6 Knowledge

```
knowledge = { chambersSeen, tunnelsKnown, campsMet, gospelsHeard, facts[], chronicle[] }
fact = { subject, claim, source: camp|'witnessed'|'ovik', tick, reliable }
```

Three ways to learn anything: witness it, be told it, or infer it. Camp facts carry that camp's spin; `reliable` is never shown.

**Assert in tests that no UI surface ever reads world state directly.** The rule most likely to be broken by accident, and once broken the information design collapses.

## 7.7 Beat triggering

End of tick. One per tick, once per playthrough unless repeatable, **never modifies world state**, always has a no-response path.

---

# PART 8 — Embodiment: decisions as physical activity

*Amends Parts 5, 6 and 7. **Implemented in the prototype**, passing the thousand-tick test. Full detail in `standing-order-embodiment.md`.*

## 8.1 The change

A camp decision no longer produces an outcome. It produces a **band** — a physical group that leaves, travels, acts, and returns. Outcomes happen where and when the band arrives.

- Camps become **committed**. Bad timing becomes possible, and bad timing is drama.
- Camps become **vulnerable while acting**. A war band three chambers out means an undefended home.
- The world becomes **legible**. You don't read that a raid happened; you watch forty goblins file past in the dark.
- Players gain verbs nobody invented: intercept, warn, follow, ambush, raid-while-empty.

## 8.2 The band

```
band = { id, campKey, purpose, target, members, carrying,
         position:{chamber, progress, towardChamber},
         state:'outbound'|'working'|'returning'|'lost',
         workLeft, route[], departedTick }
```

**Route is fixed at departure and never re-planned.** A band that hits a blocked tunnel mills about and must choose. Worse pathing, much better drama, and cheaper.

## 8.3 Cycle and timings

```
DECIDE (tick) → COMMIT (tick) → TRAVEL (continuous) → WORK → RETURN → ARRIVE (tick)
```

Traverse one tunnel 0.6–1.4 ticks · hunt 2 · assault 1 · settle 3 · parley/gift 1 · migrate 2 per tunnel with the camp helpless throughout.

**A raid three chambers out is roughly seven ticks — ten minutes real time.** Long enough to spot it, follow it, warn the target, or rob the empty camp. **The most important tuning value in the specification.**

## 8.4 Garrison

```
garrison(camp)        = pop − Σ band.members
defenceStrength(camp) = garrison × (1 + def) × (1 + chamber.defensible)
raidStrength(band)    = band.members × (1 + camp.def × 0.5)
```

**Every strength calculation uses the force actually present.** Hunts commit 25–40% of garrison, raids 50–70%, migration everyone.

## 8.5 Interruption

Route blocked → halt, re-route or return · ambushed → fight where they stand · party signals → divert one chamber · **party parleys → a war band can be talked out of a raid en route** · home attacked → force-march at 2×, arrive at −30% for 3 ticks · apex predator on route → casualties · provisions exhausted → turn back.

Four peasants standing in a tunnel arguing with thirty goblins, and it working, is the whole fantasy.

## 8.6 Amendments

**Part 5:** `resolve()` spawns bands. `preyTaken` applies on WORK completion. `settle` needs 3 ticks on site and is interruptible. `migrate` is multi-tick and vulnerable. Ecology unchanged.

**Part 6:** gift, parley and tribute need physical delivery, and a gift can be intercepted. Standing changes land at ARRIVE. Betrayal classified at assault.

**Part 7:** add `bandsSeen` to knowledge. Bands emit noise continuously — 5 hunting, 9 war. **A war band is audible two chambers away**, the primary early-warning system.

## 8.6a Verification

Full invariant sweep, 12 seeds × 1,000 ticks, all passing:

- Every camp alive; populations grow and hold; 12/12 distinct end states
- No negative food or garrison, no chamber held by two camps, no camp without its seat
- Prey and flora always within range; no predator below `MIN_PRED`
- No band larger than its camp, no empty band persisting, **longest a band stayed in the field: 10 ticks**

Behaviour per seed over 1,000 ticks: ~927 hunting expeditions · 27 war bands · **19% assault success** · 2.0 chambers changing hands · 5.7 predator migrations · 0.6 taboos broken by starvation.

**A 19% success rate is correct, not a fault.** Assaulting a defended camp should usually fail. The payoff arrives in layer two, when tier-2 camps can deliberately time a strike at a camp whose people are in the field.

## 8.6b Economy rules the delay forces

Implementing bands broke the food economy four separate ways. All four are now fixed and all four are non-obvious, so they are recorded here as rules rather than as tuning.

**A camp's population always includes people in the field.** Bands are a subset of `camp.pop`, not a deduction from it. Casualties reduce both the band and the camp; a returning band adds only what it carries. Getting this wrong duplicates population on every homecoming — the Sporewardens reached 49.

**Only the garrison eats from the stores.** People in the field live on the provisions they carried. Charging the camp for absent members while they also consumed provisions bills every expedition twice, and starves camps that are surrounded by game.

**Provisions must cost far less than the haul.** At the first attempt a four-person band on a three-hop route consumed 4.8 food to fetch 6.3. Every expedition netted almost nothing and every camp collapsed to the floor. Provisions are now `members × 0.06 × route length`.

**Starvation is proportional to the shortfall.** A flat "lose one person" for being half a unit short kills camps that are fractionally short every tick, which is the normal state of a camp waiting for a band to come home.

**A repulsed band retreats rather than being annihilated** — attacker losses on a failed assault are 60% of the computed casualties. Without this the most aggressive camp bleeds itself to the floor and stays there.

## 8.7 Chronicle shape

```
t41  The Ashfang gather at the Ashvents. Forty go out.
t43  A war band passes through the Long Gallery, heading south.     [witnessed]
t46  The Ashfang fall on the Mirelurk clan at the Black Sump.
t47  The Ashfang take the field. Nine do not come home.
t51  The Ashfang return with meat and two Mirelurk tools.
```

The player in the Long Gallery at t43 saw one line, understood nothing, and pieces the rest together from Ovik later.

---

# PART 9 — Layer four: the real-time shell

*Specified, unbuilt. Full detail in `standing-order-layer4-realtime.md`.*

## 9.1 Camera and controls

**First person.** Darkness and sound are the sensing layer, and first person makes both load-bearing. It removes the animation quality bar for the player's own body. You still see your three friends, which is where the physical comedy lives.

**Listen must be a held input, not a toggle.** Standing still to hear is a decision with a cost.

## 9.2 Chambers as spaces

Diameter 60–120 m · cross in 45–90 s · tunnels 40–110 m · traverse 54–126 s (matching the embodiment table exactly) · full map traversal ~15 minutes.

**Verticality keeps chambers memorable.** Grimhollow a wide grazing floor, the Fungal Deep a cathedral, the Weeping Stair a vertical descent, the Long Gallery flat and exposed.

**Tunnels are gameplay** — ambush sites, chokepoints for bands, and where you hear something before it arrives.

## 9.3 Simulation LOD

**Present** (party's chamber + adjacent): full 3D agents. **Near** (within 3 tunnels): graph positions and spatial audio. **Far**: graph state only.

**The simulation never changes with tier.** Any bug where a camp behaves differently when observed invalidates the entire premise.

## 9.4 Audio

**Occlusion follows the tunnel graph, not raycasts** — cheap, consistent, and it means what a player hears and what a camp hears use one code path.

Four buses: room tone, life, camps, party. **The critical cue is silence** — a hunted-out chamber loses its life bus, and that absence is how ecology teaches itself. Do not let ambience fill the gap.

### Middleware: Wwise

**Decided.** The reasoning is specific to this game rather than general preference.

Audio here carries world state, not atmosphere — direction and distance of a war band, whether a chamber's herd is alive, what a camp is doing three rooms away. That crosses the line where audio must become independently authored data rather than clips triggered by code.

And **our world model is already a rooms-and-portals graph**: sixteen chambers, twenty-five tunnels, occlusion as attenuation per tunnel traversed. That is the exact topology Wwise's spatial audio is built around, and it is the one category where it is generally considered unmatched — games where sound propagation through the environment is a gameplay mechanic. The usual cost objection (spatial audio scaling with scene complexity) does not apply: our graph is sixteen rooms, hand-authored, and it never grows.

The free Indie licence covers projects under $250K total production budget with full platform access and no asset cap.

**The counter-argument, recorded honestly:** FMOD is friendlier for a solo developer on a first middleware project. It was rejected because choosing it means hand-rolling portal propagation — precisely the system Wwise ships, and precisely the load-bearing part.

**Sanity check before committing:** build test condition 33 (a war band two chambers away, directionally identifiable) in both free tiers, one day each. Also verify that removing a life bed from one room reads as obvious silence.

> **Hard rule.** The Wwise room and portal layout must be **generated from the same chamber and tunnel tables the simulation uses** — never hand-placed independently. Two sources of truth means a player eventually hears a war band through a tunnel that does not exist. The tunnel graph is the authority; audio geometry is downstream of it.

Unity's built-in audio remains fine for everything that is not propagation — UI, foley, the two music cues. Middleware is adopted for one reason and should not swallow the whole pipeline.

## 9.4a Visual identity

**The document palette is not the game palette.** Everything in the survey documents — limestone, peat ink, malachite — is the palette of *a paper document about Deepholt*. The game is a lightless cave. Two systems, and confusing them produces a game that looks like a spreadsheet.

**World palette** — lit almost entirely by carried fire, so a warm source against cold absence.

| Role | Hex | Notes |
|---|---|---|
| Ember (fire, near) | `#E8873A` | The only saturated warm light. Falls off fast |
| Tallow (fire, mid) | `#C4762F` | |
| Bone limestone (lit stone) | `#B9AE9A` | What most surfaces become in firelight |
| Wet slate (shadow) | `#2A2E31` | Deepholt is damp, and damp reflects |
| Deep (the dark) | `#0E1113` | **Never pure black** — a player must distinguish "unlit" from "not rendered" |
| Sump green (water) | `#2F4A44` | |
| Glow (fungal) | `#7FD0A8` | The only cool light. Should feel wrong, not beautiful |
| Iron (dwarven) | `#6E6A63` | Dull, uncorroded, obviously manufactured |
| Oxide (blood and rust) | `#8C3A24` | Shared by both, which is the point |

**Fire is always somebody's.** If a chamber is lit and nobody lit it, that is a bug.

**Document palette** — the diegetic paper layer (the carried map, notes at the fire): limestone `#D6DAD0`, peat `#241F1A`, faded peat `#524A42`, rule `#A9AFA1`, oxide `#8C3A24`. The two palettes meet only at the map screen, which is the joke: the only bright legible thing in Deepholt is a piece of paper a peasant drew.

**Camp identity is not colour-led.** It is dark, and roughly one man in twelve cannot separate greens from reds. Each camp is identified three ways — mark first, silhouette at distance, colour as reinforcement.

| Camp | Hex | Luminance | Mark | Silhouette |
|---|---|---|---|---|
| Sporewardens | `#2F5A43` | 0.083 | Spore cap — filled dome | Soft-edged, stooped, layered |
| Ashfang | `#C05A2E` | 0.187 | Notch — angular V | Scrappy, asymmetric, sharp |
| Mirelurks | `#7FA3BA` | 0.343 | Wave — double curve | Wet, smooth, laden |
| Assayers | `#E0A62B` | 0.433 | Balance — stroke with arms | Ragged, ornamented, tall |

**Accessibility test:** screenshot, desaturate, and if the camps are not distinguishable the design has failed. Verified — no adjacent luminance gap below 0.09. The first attempt failed this, with the Mirelurk slate only 0.056 from the Ashfang rust. **Re-run whenever a camp colour changes.**

**Type.** Display: a slab serif — the dwarven layer is cut, not written. Interface: a neutral grotesque with tabular figures. No third face, and no handwriting font for the map — its irregularity comes from linework. **The plate is set as signage**, all caps and mechanical, because it is signage.

**Lighting.** Three sources only: fire (warm, short, announces you), fungal glow (cold, faint, immobile), and dwarven residuals — channel markers and Cistern signage carry a faint worked luminescence, which is how a player learns to recognise the built layer at a glance.

**Material language.** Everything the dwarves built is square, precise and legible; everything living is neither. Camp structures are built from the wreckage of the first using the logic of the second — dwarven plate lashed into a windbreak. Every camp structure should read as *misuse of infrastructure*.

## 9.5 Interface

**No HUD by default.** An optional caption layer exists for accessibility — see 9.5a. Hunger read from the body, standing from behaviour, and the only persistent on-screen information is the item in your hand. Three diegetic screens: **the fire** (shared, where the filtered chronicle is read and the arguing happens), **the map** (drawn as you explore, unreadable while running), **inventory**.

## 9.5a Accessibility — the parts that change the design

The full specification is in `standing-order-accessibility.md`. Four things belong here because they constrain other systems.

**The principle: no information exists in only one channel.** Every audio cue that carries world state has a visual partner in the world — torchlight blooming at a tunnel mouth before a war band arrives, dust shaken from the ceiling, prey fleeing past you the wrong way, wet stone drying after the water stops. Diegetic, so it costs no HUD, and it improves the game with the sound on.

**`Listen` renders visually as well as audibly.** It already stops the player and costs vulnerability, so it grants no free information. While held, the world shows its disturbances — air movement, dust drift, ripples propagating from the source. Available to everyone, always; not a mode to be enabled.

**Captions are generated from audio events, never from world state.** This is a data-flow rule, not a UI one. Generating them from the simulation would quietly hand caption users knowledge the player has not earned and break the subset rule in Part 7.

**Fire modulation is rate-capped from day one.** A cave lit by torchlight is a flicker environment by design, and this cannot be retrofitted as a post-process.

**The silent-play gate.** Five testers, 30 minutes, audio disabled, asked the legibility gate's question. **Pass condition 50%**, against 60% for the hearing gate. Run it in the same session with the same build.

## 9.6 Networking

Host-authoritative. Clients never simulate. Movement is the only prediction. **Knowledge is filtered on the host, per player** — if the host sends the full chronicle and clients filter it, someone reads the packets.

## 9.7 Saving

Tick boundaries only. Autosave every 10 ticks. **No manual saves and no reloading to undo a consequence.**

## 9.8 Engine

Unity. **The only requirement: the simulation lives in plain C# with no engine dependencies**, so it can keep running headless for every test condition.

## 9.9 The legibility gate

**The hard stop before anything beyond layer four.**

Five people who have not worked on the game play for 30 minutes. At three separate moments they are asked: *what is that camp about to do, and why?* **Pass condition: 60% correct.**

If they can't predict, the simulation is invisible and this is a cave co-op game competing with Deep Rock Galactic on its own terms.

---

# PART 10 — Consolidated data model

```
Chamber { key, name, x, y, def, flora, floraCap, floraStock, prey, preyCap,
          preyPop, apex{name,pop,threat}, pred, huntedBy[], lastHuntedBy[],
          crashed, waterAllocation }

Camp    { key, name, short, colour, home, holds[], known:Set, pop, food, def,
          temper, intelligence 0..2, creed, taboo[], last, since, lastSettle,
          alive, leader{}, notables[], faith, zealot, betrayerUntil }

Band    { id, campKey, purpose, target, members, carrying, position{},
          state, workLeft, route[], departedTick }

Party   { chamber, peasants[], stores{}, knowledge{}, promises[],
          capturedBy, reputation{} }

Peasant { name, playerId, hunger, condition, carried[], state, noise }

World   { seed, tick, chambers{}, camps{}, bands[], tunnels[], latentEdges[],
          standing{}, alliances{}, truces{}, log[], pendingWorldEffects{} }
```

---

# PART 11 — All tuning constants

**Layer one — implemented values**

| Constant | Value | | Weight | Value |
|---|---|---|---|---|
| `NOISE` | 0.32 | | `hungerHunt` | 2.4 |
| `FOOD_PER_POP` | 0.5 | | `hungerForage` | 1.2 |
| `RAID_LOOT` | 0.45 | | `hungerRaid` | 1.2 |
| `CASUALTY` | 0.08 – 0.18 | | `hungerMigrate` | 2.0 |
| `GRAZE` | 0.55 | | `weakTempts` | 1.6 |
| `PREY_BIRTH` | 0.30 | | `lootTempts` | 1.0 |
| `PRED_KILL` | 0.7 | | `contestedGround` | 1.1 |
| `PRED_BIRTH` | 0.10 | | `lossFortify` | 1.8 |
| `PRED_DEATH` | 0.06 | | `winRaid` | 0.6 |
| `HUNT_SHARE` | 0.30 | | `warWeariness` | 1.2 |
| `MEAT` | 3.0 | | `raidReluctance` | 1.2 |
| **`MIN_POP`** | **2.5** | | `marchCost` | 0.9 per hop |
| | | | `safeGrow` | 1.6 |
| | | | `expansion` | 2.6 |
| **`MIN_POP`** | **2.5** |
| **`MIN_PRED`** | **0.5** |
| | | | `curiosity` | 0.6 |

**Layer two** — `STANDING_DECAY` 0.015/tick · `BLOOD_DECAY_MULT` 0.5 · `ALLY_THRESHOLD` +50 · `PARLEY_FLOOR` −50 · `TRUCE_LENGTH` 15 · `BETRAYAL_PENALTY` −60/−30 · `BETRAYER_DURATION` 40 · `CHALLENGE_THRESHOLD` 45 · `MIN_TENURE` 6 · `FAITH_START_DEVOUT` 70 · `FAITH_START_RIVAL` 55 · `FAITH_BREAK` 25 · `FAITH_DRIFT` +0.5 · `SCHISM_DELAY` 2–4 · `SCHISM_CHANCE` 0.8 · `SCHISM_SPLIT` 0.25–0.40 · `ATONE_GIFTS` 3 · `ATONE_WINDOW` 15

**Layer three** — `TICK_SECONDS` 90 · `HUNGER_RATE` 100/7 ticks · `CARRY_SLOTS` 6 · `CARRY_SPEED` 0.5× · `LABOUR_TICKS` 25 · `RANSOM_DEBT` 3 gifts · `OVIK_FACTS` 3–5 · `BEAT_MAX_PER_TICK` 1 · `PROMISE_WINDOW` 20

**Embodiment** — `PROVISION_PER_MEMBER` 0.06 per member per chamber on the route · `MAX_BANDS_PER_CAMP` 3 · `MIN_GARRISON_TO_SEND` 3 · `MIN_BAND` 2 · `TUNNEL_TRAVERSE` 0.6–1.4 · `HUNT_WORK` 2 · `ASSAULT_WORK` 1 · `SETTLE_WORK` 3 · `MIGRATE_PER_TUNNEL` 2 · `BAND_HUNT_SHARE` 0.25–0.40 · `BAND_RAID_SHARE` 0.50–0.70 · `FORCE_MARCH_SPEED` 2× · `FORCE_MARCH_PENALTY` −30% for 3 · `BAND_NOISE_HUNT` 5 · `BAND_NOISE_WAR` 9 · `MAX_CONCURRENT_BANDS` 12 · `PROVISION_PER_MEMBER` 0.5/tick travelled

**The Cistern** — `CHANNEL_DRAIN` 8 ticks · `GATE_THRESHOLD_TICKS` 6 · `REFILL_TIME` 30 · `RECOVERY_WINDOW` 20 · `EXTINCTION_WINDOW` 40 · `BLAME_LOOKBACK` 10 · `BLAME_SEEN` −35 standing / −25 faith · `BLAME_UNSEEN` −25 toward each camp's least-trusted neighbour

---

# PART 12 — Test conditions

**Foundational**
1. **Thousand-tick no-player test.** Every camp alive after 1,000 ticks with no party. **Passing — 12/12 seeds.**
2. **Faith is stable without a player.** No party, no zealotry.
3. **No player, no beats.**

**Layer one**
4. Six seeds produce six distinct outcomes.
5. Populations grow and hold, not decline monotonically.
6. Camps settle, expand, and lose ground to raids.
7. **Routs occur and are not fatal.** ~17 routs per seed per 1,000 ticks, zero camp deaths.

**Layer two**
8. Across 10 seeds × 300 ticks: at least one gift, one parley, one alliance.
9. At least one succession across 10 seeds; no camp more than four in 300 ticks.
10. Betrayal under one per 300 ticks per seed, never zero across 10 seeds.
11. Every faith break produces a remnant or a dead camp. **No permanently unreachable territory.**

**Layer three**
12. Party effects reach the tick; the owner senses them next tick.
13. Poaching an owned chamber 6+ ticks produces a delegation or a raid.
14. All four capture exits reachable; no unrecoverable captured state.
15. Split capture rescue completes.
16. **Fighting does not scale.** Four armed peasants reliably lose to eight in the open and can win in a tunnel. Verify both.
17. **Knowledge isolation** — no UI surface reads world state directly. Automate this.
18. **Latent connections.** All six openable; the flooded channel only after a Cistern re-route.
19. Block a camp's only hunting range: it migrates, raids or dies within 30 ticks, attributed to nobody.

**The Cistern**
20. **The cascade is gradual.** No camp loses population before tick 20, and the richest chambers crash before the poorest.
21. **The recovery window holds.** Restore at tick 19 and every chamber returns to within 5% within 50 ticks.
22. **Extinctions are permanent.** Restore at tick 45 and at least one prey population stays at zero.
23. **Blame lands.** Drain unobserved and verify standing drops toward each camp's least-trusted neighbour, not the party.
24. **The controlled drain is survivable.** Correctly operated, it opens the Gate with no permanent extinctions.

**Embodiment**
25. A camp with a band out has reduced garrison and is measurably easier to raid. **Currently unverified in the prototype** — across 400 ticks, no raid landed on a camp with people in the field. Raid decisions are made when a target looks weak, but a war band takes 4–5 ticks to arrive and the target's hunting party is usually home by then. *Deliberately timing a strike at an empty camp is a tier-2 behaviour and belongs to layer two, not here.*
26. Blocking a route mid-journey turns a band back.
27. The party can rob a camp whose garrison is out, and the returning band reacts.
28. From first sighting a war band to arrival: **at least 4 ticks (6 minutes) to act.**
29. Attack a camp with a band out — it force-marches home.
30. **No teleporting outcomes.** No standing change, prey reduction or casualty without a band physically present.

**Layer four**
31. **LOD invariance.** 300 ticks parked vs touring — behaviour statistics match within noise.
32. Bands promote at true route position.
33. A war band two chambers away is directionally identifiable by a blindfolded tester.
34. Testers identify a hunted-out chamber by sound alone.
35. No unearned world state reaches any client.
36. Save mid-journey, reload, bands resume identically.
37. Two bands plus wildlife plus four players holds 60 fps.

---

# PART 13 — Build order

**Layer 1 — done.** Passing its foundational test on the sixteen-chamber map.

**Embodiment — next, headless.** Bands and the COMMIT→TRAVEL→WORK→RETURN→ARRIVE cycle, then garrison-aware strength, then interruption. **Before layer two**, because it changes how every layer-two action resolves and building politics first means rewriting it. Validate entirely in the headless sim before any 3D exists.

**Layer 2.** Relations and decay → log lines → hierarchy and succession → tier-1 actions → tier-2 actions → creed interpretation → faith and the break → schism and atonement. **Do not build faith before hierarchy** — a break with no hierarchy has nothing to split.

**Layer 3.** Party and movement → accumulator and hunting → noise and detection → encounters and capture → **knowledge model and filtered chronicle** → parley, gifts, promises → beats → Cistern verbs. **Knowledge before dialogue**, or dialogue will read world state and the rule breaks permanently.

**Layer 4.** One chamber in the dark → audio before anything visual → hook the headless sim in with bands as capsules → LOD → fire, map, inventory → networking → band silhouettes → **legibility gate** → lighting and art.

**Then, and only after the gate passes:** tech tracks, quest templating, the forty beats, dialogue fragments, art pass, endings.

**Writing order:** contact beats → revelation → bands → faith → political → capture → tools and trade → the Gate. Dialogue fragments last.

---

# PART 14 — Glossary

**Band** — a physical group sent out by a camp. Travels, works, returns.
**Beat** — an authored dramatic situation with a trigger in simulation terms.
**Chamber** — a node on the map; a room in 3D.
**Chronicle** — the log of world events. The full version is a dev tool; players see a filtered subset.
**Creed** — how literally a camp takes the prophecy.
**Faith** — a devout or rival camp's conviction about the party, 0–100. Below 25 it breaks.
**Fervour / zealot** — the state after a faith break. The camp hunts the party above eating.
**Garrison** — camp population currently at home.
**Holdings** — the chambers a camp controls. The first is its seat.
**Knowledge** — the player's subset of world state.
**Latent edge** — an obstructed passage that can be cleared.
**Poaching** — hunting ground another camp holds or ranges over.
**Range** — holdings plus known neighbours of holdings.
**Rout** — a beaten camp reduced to `MIN_POP`, losing all holdings but its seat. Not death.
**Schism** — the split of a broken camp into hardliners and a loyal remnant.
**Standing** — one camp's opinion of another party, −100 to +100. Asymmetric.
**Taboo** — ground or action a camp refuses on principle, even when starving.
**Tick** — one simulation heartbeat. 90 seconds.

---

# PART 15 — Open items and risks

## Settled

Title (`Standing Order`) · the hermit (Tallow) · the Assayers (renamed from Wyrmcult) · Wwise for audio · the world and document palettes · camp identity verified for greyscale separation · nobody is coming from above · player-made peasants · truth-telling scales with standing · the Assayers are viable · the Cistern's failure state · combat exists but does not scale · clearing replaces mining.

## Open

1. ~~Systems not yet specified.~~ *Done — see `standing-order-systems.md`: the tech track, items and trade, dialogue fragments, character creation.*
2. **Chamber names** — change last; each currently tells you what the place is before you arrive, which is real work.

## Risks, ordered by likelihood of killing the project

1. **Scope against cadence.** Real-time, online co-op, persistent authoritative simulation, one day a week. *Mitigation: the layer order and the legibility gate.*
2. **Drift toward adventurers.** *Mitigation: fighting does not scale, and that rule is constitutional.*
3. **Legible to us, opaque to players.** *Mitigation: audio design, Ovik, embodied bands, the gate.*
4. **Writing volume.** *Mitigation: beats first, dialogue thin until beats are proven.*
5. **Balance regression.** Every system added has broken the previous balance. *Mitigation: the thousand-tick test as an automated check.*
6. **Multiplayer determinism.** *Mitigation: clients render, host decides.*
7. **Untested tone.** Structural comedy either lands or reads flat. *Mitigation: read a chronicle aloud to people who aren't building it and watch whether they laugh. Do this before writing forty beats.*


---

# APPENDIX A — The gospels

## A.1 The four gospels, in full

Four hundred years of copying by people who could not read, each version bent toward what its culture needed it to say. Every one of them descends from the plate above.

### The Sporewarden reading

Closest to the original, because farmhands were the last to lose the habit of copying carefully — and then four centuries of reverence padded it out.

> *When the ceiling opens, they who fall shall be brought to the water.*
> *And the water shall be opened to them.*
> *And it shall be as it was in the first days, when the beds were full and no one was hungry.*

They have read "conducted" as *escorted with honour*, and "the gate operated" as *the water shall be opened to them* — a blessing rather than an instruction. The last line is entirely invented, and it is a memory of abundance that none of them have ever seen.

**This is why they feed the party from stores they cannot spare.** They think they are the ones who bring the fallen to the water, and that the first days come back afterwards.

### The Ashfang reading

Goblins do not write. This is four hundred years of being shouted across a cave.

> *Roof breaks. Ones fall.*
> *Take them to the water.*
> *Then it's ours.*

They have kept the instruction and lost every qualifier, and "the gate operated per standing order" has decayed into a claim of ownership. Nobody remembers what *ours* refers to. Most Ashfang assume it means the water. Some assume it means the fallen.

**Which is why B03 exists.** They aren't testing you. They're collecting you.

### The Mirelurk reading

The most textually accurate version in Deepholt, because the Mirelurks kept it as a document rather than a prayer — and then appended terms.

> *When the ceiling opens, those who fall are to be conducted to the cistern.*
> *The conductor is owed.*

The second line is theirs. It is not in the plate. It has been in their copy for so long that they have genuinely forgotten it is an addition, which is the most Mirelurk fact about them: they will sell you an honest text with their invoice stapled to the back.

**They do not believe the prophecy.** They believe the second line.

### The Assayers' reading

A fragment — their copy lost its opening — plus four centuries of gloss.

> *…are to be conducted to the cistern.*
> *But the wyrm was here before the water.*
> *What the water gives, the wyrm may take.*
> *Let none be conducted who has not first been shown to the wyrm.*

Everything after the first line is theirs. Having lost the beginning, they never learned that the text concerns people who fall from the ceiling — so they read it as a rule about *procedure*, and inserted their god as the authority the procedure must pass through.

**Their position is not that the party is false. It is that the party is unverified.** That is a meaningfully different kind of hostility, and it means there is a route to them: being shown to the dragon. What that costs is a beat worth writing.

### Using them

**B06 (Four gospels)** fires once the party has heard two. The versions visibly disagree, which is what unlocks lying — quoting the Mirelurk text at the Sporewardens, or the Ashfang reading at anyone.

**The hermit's plate is the fifth version**, and the only true one. A player who reads it holds a fact that every camp would reject, weighted by standing per the truth-telling rule.

**Nobody in Deepholt has ever seen two versions side by side.** The party is the first entity in four hundred years in a position to compare them, which is the whole of Act II's payoff.

---


---

# APPENDIX B — The beat library

All forty authored situations. **Four rules:** one beat per tick maximum · once per playthrough unless marked *repeatable* · **beats never modify world state**, they present a situation and only the player's response changes anything · every beat needs a no-response path.

A playthrough sees roughly a third. Priority is 1 (highest) to 3, used only when several could fire at once.

### Contact — meeting the camps

**B01 · The offering** · *Pri 1*
**Trigger** First Sporewarden contact, standing ≥ 0.
**Shape** They feed the party unprompted, from stores they cannot spare. No conditions asked.
**Consequence** Their food drops measurably. Standing +20. An unspoken debt the party doesn't know exists.
**No response** They feed you anyway. It's worse.

**B02 · Priced** · *Pri 1*
**Trigger** First Mirelurk contact.
**Shape** They establish what the party is worth, and to whom, out loud, in front of you.
**Consequence** Opens the information economy. They name a price for the prophecy.

**B03 · Collected** · *Pri 1*
**Trigger** First Ashfang contact at standing < 0.
**Shape** They attack — badly — and lose interest if you run. Their gospel says *then it's ours*, and nobody remembers what *ours* means.
**Consequence** They have now seen whatever you defended yourself with. Tech track advances toward it.

**B04 · Unverified** · *Pri 1*
**Trigger** First Assayers contact.
**Shape** Not "you are false" — "you have not been shown to the wyrm." Trade refused pending inspection.
**Consequence** Hostile floor, but with a stated route through it. See B29.

**B05 · The greeting that isn't** · *Pri 2*
**Trigger** Any camp at standing ≥ +15 encounters the party for the third time.
**Shape** They use one peasant's name, which nobody told them.
**Consequence** First hard evidence the camps have been discussing the party since before they stood up.

---

### Revelation — learning what's going on

**B06 · The plate** · *Pri 1*
**Trigger** Party reaches the Kiln and talks to Tallow.
**Shape** He reads it flatly, including the silt and the quarterly inspection. He does not editorialise.
**Consequence** **Act II ends.** The player knows. The camps never will.

**B07 · Four gospels** · *Pri 1*
**Trigger** Prophecy heard from two different camps.
**Shape** The versions don't match, and the party is the first entity in four hundred years to notice.
**Consequence** Unlocks **lie** — quoting one camp's gospel at another.

**B08 · The plumbing** · *Pri 2*
**Trigger** Party reaches the Cistern.
**Shape** Mundane dwarven signage everywhere, revered by whoever is standing guard.
**Consequence** The player understands the endgame before any character does.

**B09 · The beds are in growth** · *Pri 1*
**Trigger** Party has read the plate AND reached the sluices.
**Shape** The warning line connects to the gates in front of them.
**Consequence** The controlled drain is now knowable. Players who miss this beat can still reach an ending — a worse one.

---

### Political — the camps against each other

**B10 · The poaching complaint** · *Pri 2* · *repeatable per camp*
**Trigger** Party hunted a chamber another camp holds, twice.
**Shape** A delegation arrives to object. Politely, the first time.
**Consequence** Comply and go hungry, or refuse and push them toward raiding.

**B11 · The ambitious one** · *Pri 1*
**Trigger** Any notable's ambition exceeds their loyalty.
**Shape** They approach the party privately with an offer.
**Consequence** Back them and trigger a succession. Refuse and they may act anyway and blame you.

**B12 · Broker** · *Pri 1*
**Trigger** Two camps at standing < −40 with each other, both ≥ +20 with the party.
**Shape** Both separately ask for help against the other, neither knowing about the other's ask.
**Consequence** The first genuine political choice with no correct answer.

**B13 · The new chief** · *Pri 2*
**Trigger** A succession occurs in a camp the party has met.
**Shape** Everything the party had negotiated is now with someone who wasn't there.
**Consequence** Standing shifts ±10. Any promises made to the old leader are now disputed.

**B14 · Word travels** · *Pri 3* · *repeatable*
**Trigger** Ovik completes a circuit after any war, betrayal or succession.
**Shape** He tells the party what happened three chambers away, with his own spin, for a price.
**Consequence** Facts enter `knowledge` with `source: ovik` and variable reliability.

**B15 · The alliance** · *Pri 2*
**Trigger** Two camps form an alliance while the party is at ≥ +15 with one of them.
**Shape** Their ally is now interested in the party, and inherits the friendlier camp's opinion at half weight.
**Consequence** Politics compound. The map has fewer independent actors.

---

### Ecological — the world eating itself

**B16 · Empty ground** · *Pri 1* · *repeatable per chamber*
**Trigger** Any chamber's prey below 12% while a camp depends on it.
**Shape** That camp arrives somewhere — as a delegation, a migration, or a raid.
**Consequence** Decided by the simulation, not by us.

**B17 · The dragon thins** · *Pri 1*
**Trigger** Dragonspine prey below 25% for 10 ticks.
**Shape** The Assayers's god is visibly starving, and they blame the party regardless of cause.
**Consequence** Creed hardens. A faith-break path opens for a camp we'd otherwise never break.

**B18 · Their own law** · *Pri 1*
**Trigger** A camp breaks its own taboo through starvation.
**Shape** The party witnesses it, or hears about it from Ovik.
**Consequence** That camp's faith drops 15 on its own, without the party doing anything. Shame is destabilising.

**B19 · Bad water** · *Pri 1*
**Trigger** The Cistern is damaged, blocked or seized.
**Shape** The water stops, audibly, everywhere. Within three ticks, camps arrive to accuse each other.
**Consequence** Cascade per master 2.7. Blame assigned by the attribution rules — and if the party wasn't seen, they watch two innocent camps go to war over it.

**B20 · The quiet chamber** · *Pri 3*
**Trigger** Party enters a chamber whose prey they personally hunted to collapse.
**Shape** No beat text. The life audio bus is simply gone.
**Consequence** None mechanically. This is the game's thesis delivered as silence.

---

### Faith — the Sporewardens, mostly

**B21 · The sign misread** · *Pri 1*
**Trigger** Any devout camp's faith below 25.
**Shape** They do not renounce the prophecy. They conclude the party is a false claimant sent to test them.
**Consequence** Zealotry. The camp begins to starve and does not care.

**B22 · The remnant** · *Pri 1*
**Trigger** 2–4 ticks after B21.
**Shape** A minority splits off, insisting the sign still holds.
**Consequence** A small, weak, permanently loyal faction — and the only route back into that territory.

**B23 · The offered penance** · *Pri 2*
**Trigger** Party gifts food to a camp in fervour.
**Shape** It is accepted and read as further proof of deceit.
**Consequence** Faith +12, and `pursue:party` +0.15 for 5 ticks. Doing the right thing makes it worse first.

**B24 · Honest** · *Pri 1*
**Trigger** Party tells a camp the placard is a maintenance notice.
**Shape** Their reaction scales with standing per master Part 15.
**Consequence** At Bound standing: some notables believe you, some don't. **A schism caused by honesty, with no zealotry attached.**

**B25 · Shown to the wyrm** · *Pri 1*
**Trigger** Party accepts the Assayers's inspection.
**Shape** They are taken to the ridge. Whatever the dragon does is not scripted — it is the apex predator behaving normally, and the Assayers interpret it afterwards.
**Consequence** Standing swings hard in whichever direction the interpretation lands.

---

### Capture — being taken

**B26 · Inside** · *Pri 1*
**Trigger** Party captured and set to labour.
**Shape** They live in a camp for 25 ticks while its politics happen around them. Succession, hunger, argument, all at close range.
**Consequence** Standing +20 on completion, and an enormous amount of `knowledge` about one camp.

**B27 · The ransom** · *Pri 1*
**Trigger** A captured party member is bought out by a third camp.
**Shape** You are handed over, having been a commodity in a negotiation you couldn't hear.
**Consequence** Debt of 3 gift-equivalents. The buyer will collect.

**B28 · The rescue** · *Pri 1*
**Trigger** One player held, the others free.
**Shape** The primary co-op situation. The camp's garrison is a real obstacle and its band schedule is a real opportunity.
**Consequence** Everything the held player learned inside (B26) enters the party's knowledge.

**B29 · The neighbour** · *Pri 2*
**Trigger** A captured party member is held alongside a prisoner from another camp.
**Shape** Somebody else's grievance, told at length, by someone with nothing to lose.
**Consequence** High-reliability facts about a camp the party may never have met.

---

### Tools and technology

**B30 · The gift that shoots back** · *Pri 1*
**Trigger** Ashfang given any tool, 8+ ticks earlier.
**Shape** They use it. On somebody.
**Consequence** The victim learns where it came from. Standing with the victim −25.

**B31 · The imitation** · *Pri 2*
**Trigger** A tier-0 camp advances a tech step by observation rather than by being given the tool.
**Shape** They have reproduced it badly. It works, mostly.
**Consequence** Combat strength up, with a failure rate. Occasionally injures its user, which they blame on the party.

**B32 · The arms race** · *Pri 2*
**Trigger** Two camps reach the same tech step within 15 ticks.
**Shape** Both know the other has it. Neither wants to be second to use it.
**Consequence** Mutual raid scores up. The Ember Galleries become contested ground.

---

### Trade and debt

**B33 · The ledger** · *Pri 2*
**Trigger** Party's third transaction with the Mirelurks.
**Shape** They show you your own entry. It is longer than you thought and older than you thought.
**Consequence** *The conductor is owed* stops being a line of scripture and becomes an invoice.

**B34 · The collector** · *Pri 1*
**Trigger** Party owes the Mirelurks 3+ gift-equivalents and hasn't paid within 30 ticks.
**Shape** They do not raid. They sell your location, your route, or your promise to someone who wants it.
**Consequence** Whichever camp bought it acts on it.

**B35 · Ovik's other trade** · *Pri 2*
**Trigger** Party has traded with Ovik three times.
**Shape** He offers to sell them something about themselves — what a camp said when they weren't there.
**Consequence** True, and worse than they expected.

---

### Bands in the field

**B36 · The column** · *Pri 2* · *repeatable*
**Trigger** A war band enters a chamber adjacent to the party while outbound.
**Shape** Forty goblins file past in the dark. You know what it means and you have four ticks.
**Consequence** Nothing, unless the party acts. Follow, warn, intercept, or let it go.

**B37 · The warning** · *Pri 1*
**Trigger** Party reaches a band's target camp before the band does.
**Shape** They have to be convinced, and they've no reason to trust you.
**Consequence** If believed: they fortify or recall a band, and standing +30. If not: they find out you were right.

**B38 · Turned** · *Pri 1*
**Trigger** Party parleys with a band en route.
**Shape** Four peasants in a tunnel arguing with thirty goblins.
**Consequence** The band aborts. **The most valuable single interaction in the game** — make sure it feels like it.

**B39 · The homecoming** · *Pri 2*
**Trigger** A band returns to a home the party has robbed, blocked, or otherwise altered.
**Shape** They arrive with spoils to find the situation changed.
**Consequence** Blame assigned by observation, or by lowest standing if unobserved.

---

### The Gate

**B40 · The last argument** · *Pri 1*
**Trigger** Party has the means to open the Gate.
**Shape** Every camp with a stake arrives, or sends word. The controlled drain is possible; the fast one is easier.
**Consequence** The ending. And then the chronicle runs twenty ticks past your exit, because the world does not stop when you leave.

---

### Writing budget

Forty beats at roughly a page each is the single highest-value writing in the project — each one produces dozens of distinct situations depending on world state.

**Write them in this order:** contact (B01–B05) → revelation (B06–B09) → bands (B36–B39, because embodiment makes them the most visible) → faith (B21–B25) → political → capture → ecological → tools and trade → B40.

Dialogue fragments stay thin until the beats are proven in play.
