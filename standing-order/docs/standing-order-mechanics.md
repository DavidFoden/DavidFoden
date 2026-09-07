# Standing Order — Mechanics

*v0.1. These are decisions, not options. Where I've made a call you might disagree with, it's marked.*

---

## 1. The verbs

Everything a player can do. If a system in any other document assumes a verb that isn't here, one of the two documents is wrong.

Four peasants, real time, no character classes. Everyone can do everything; the differences come from what you're carrying and what you know.

### Moving

**Walk.** Default. Moderate noise.
**Sneak.** Half speed, quarter noise. The main way to survive being somewhere you shouldn't be.
**Climb / crawl.** Gated by carried weight. Some routes close if you're loaded.
**Flee.** Sprint. Very loud, burns food fast, and you drop anything not stowed.

### Sensing

**Listen.** Stand still and the world resolves into direction and distance — hunting parties, water, an animal, an argument three chambers away. This is the primary sensor, not sight.
**Look.** Reads a chamber's state: what's grazing, what's been stripped, whose sign is on the walls.
**Track.** Reads what passed through recently and how long ago.

### Eating

**Hunt.** The party's version of what every camp does, and it uses the same code. Chase, snare, or ambush. Yields meat, makes noise, and reduces that chamber's prey.
**Forage.** Flora. Reliable, poor, quiet. Keeps you alive and never gets you ahead.
**Set snare.** Placed and left. Returns to it later. Quiet and slow — the correct way to feed a party that doesn't want to be noticed.
**Eat.** Consumes carried food. Shared or not, which is a decision the party has to make out loud when there isn't enough.
**Drink.** Water is everywhere except the dry east. Not a scarcity system; a routing constraint.

### Handling

**Carry.** Hard slot limit per person. Weight gates climbing, sneaking and fleeing.
**Take.** From the ground, a body, a store.
**Give.** Food, tools, or information, to a camp or a person. The single most powerful diplomatic verb in the game.
**Steal.** Take from a camp's stores. Enormous standing cost if seen, and camps have watchers.
**Drop / stash.** Caches you can return to, and that others can find.

### Changing the world

**Break.** Cut through weak rock, which adds a tunnel to the map. Limited charges, recharged slowly by dwarven tools you scavenge. The verb that made the whole prototype interesting.
**Block.** Collapse or barricade a tunnel. Removes an edge. Strategically enormous — you can starve a camp by cutting it from its hunting ground, and you will not immediately understand that you've done it.
**Build.** Fire, snare, barricade, marker, shelter. Fire is warmth, light, cooking, and a beacon visible from adjacent chambers.
**Divert.** Only at the Cistern and its channels. See section 3.

### People

**Parley.** Open contact with a camp. Availability depends on their creed and standing, not on the player's charisma.
**Trade.** Goods, food, information.
**Lie.** Specifically about the prophecy, once the party has heard more than one version. Mechanically: assert a rival camp's gospel as truth. High risk, high reward, and it can be checked.
**Threaten.** Almost never works. Exists because players will try it and the refusal should be characterful.
**Signal / distract.** Make deliberate noise somewhere to pull attention elsewhere. The core co-op verb: one player draws a hunting party while the others move.
**Carry a friend.** Two hands, no weapon, half speed. Non-negotiable if you want them back.

### What is deliberately absent

**Superseded — fighting exists; see master 4.1a.** There's **brawl**, which is a losing proposition against anything organised, and which exists so players learn quickly that it is one. Peasants do not fight camps. Section 5 covers what happens when they try.

---

## 2. Time and scale

Pick these numbers now, because every rate in the simulation depends on them.

| | |
|---|---|
| One world tick | **90 seconds real time** |
| Session target | **90–120 minutes**, roughly 60–80 ticks |
| Full playthrough | **6–10 hours** across several sessions, roughly 250–400 ticks |
| Party hunger | one meal per person per **6–8 ticks** (~10 minutes) |
| Ecological collapse | **15–30 ticks** of overhunting (~25–45 minutes) |
| Prey recovery | **20–40 ticks** if left alone |
| Camp succession | possible from **tick 40** onward |

The important consequence: a chamber can be hunted out inside a single session, and recover inside the next one. That's the right pace for a consequence system — long enough that nobody sees it coming, short enough that everyone lives to regret it.

**The world does not tick when nobody is playing.** I'm making this call deliberately. A world that runs while you're at work means you return to a cavern where everything you set up has been undone by nothing you saw, and that is punishing rather than dramatic. Deepholt is paused between sessions.

**But the starting state is four hundred years old.** This is the balance principle that matters most, and it's the fix for the camps dying early. Tick zero is not a fresh world — it is an equilibrium that has already held for centuries. Every camp's population, territory and food stores should be initialised at their sustainable level for the ground they hold, and the map should be seeded so that if the player never arrives, the simulation runs a thousand ticks with nobody starving.

That's a testable condition, and it should be part of the build: **run the world for 1,000 ticks with no player. If any camp dies, the starting state is wrong.** Then the player's arrival — the fissure, the hunting, the broken walls — is what tips it.

---

## 3. The Cistern

It's the dwarven waterworks, and it needs to be physical enough that damaging it has predictable consequences.

**What it is.** A header pool fed by an aquifer, and four sluice gates that route water out along stone channels to the growing beds of each district. Water allocation is what decides how fast flora regrows in each chamber. Every ecological difference on the map — why the Fungal Deep is vast and the Ashvents are thin — traces back to how those sluices were set the day the dwarves left.

**Nobody has moved them in four hundred years.** Not because they're guarded, but because nobody alive understands what they do. The camps treat the Cistern as sacred infrastructure and leave it alone, which is precisely why the ecology has been stable long enough for four cultures to form around it.

**Mechanically:** each chamber has a water allocation multiplier applied to its flora regrowth. The sluices set those multipliers. Four gates, each with three or four positions.

**What the party can do to it:**

- **Re-route.** Move water from one district to another. The receiving chambers boom over 20–40 ticks; the starved ones decline on the same timescale. Slow, enormous, and almost impossible to attribute — camps will blame whoever they already distrust.
- **Block.** Flora regrowth drops across the whole map. Everyone gets hungrier at once. This is the single most destabilising thing available, and it should be possible to do *by accident*, early, while messing about.
- **Open wide.** The Black Sump and Drowned Stacks flood. Routes close, fishing improves, the ripper eels spread.

**Why it's the ending.** The Sealed Gate is water-counterweighted — the dwarves designed it to be opened by draining the header pool, which is exactly what the placard was instructing survivors to do. So the Gate genuinely cannot be opened without the Cistern, and controlling the Cistern means controlling what everyone eats. Getting out and deciding who inherits Deepholt are the same act.

The joke lands last: the prophecy was right. They were supposed to be conducted to the cistern. It was just a maintenance instruction.

---

## 4. Names, and the thing the player never learns

The dwarven signage at the Cistern is mundane, legible to the hermit, and states the whole truth plainly. The player can read it in Act III. **No camp ever believes it.** Telling a devout camp that their scripture is a plumbing notice is available as a dialogue option and is treated as the most offensive thing the party can say — it is, structurally, the fastest route to a faith break.

---

## 5. When they catch you

**Camps do not kill you. Camps take you.** This is the most important rule in the document.

Death by camp would turn every political encounter into a combat encounter, which is the game we're specifically not making. Capture keeps the stakes real while pushing the fiction toward the systems we actually built.

**Incapacitation.** A peasant who takes enough punishment goes down rather than dying. Teammates can carry them — two hands, half speed, no weapon.

**Capture.** If the party is caught, or all four are down, the nearest hostile camp takes them. Consequences: everything carried is stripped and enters that camp's stores — including, memorably, any tool you were holding, which then enters their tech track. Standing shifts. You are held in their territory.

**Getting out.** Four routes, all of them gameplay: escape, ransom (another camp buys you, and now you owe them), release (a camp with high standing intervenes), or labour — you work for them until they consider the debt settled, which is the most interesting one because you're living inside a camp while its politics happen around you.

**Split capture is the co-op case.** One player taken while the others are free is a rescue mission, and it's the best thing this system produces. Design for it explicitly rather than treating it as an edge case.

**Actual death** comes only from starvation, apex predators, drowning and falls. All four are avoidable and all four are the player's own fault. Zealots are the exception: a camp in fervour is hunting to kill, which is what makes a faith break genuinely frightening rather than merely inconvenient.

---

## 6. Multiplayer rules

Two to four players, host-authoritative.

**The host owns the world.** The whole simulation runs on the host; clients send intents and receive state. No host migration in v1 — if the host leaves, the session ends and the world saves. This is a scope decision and it's the right one for a project running one day a week.

**Drop-in, drop-out.** A friend can join a world in progress and inherits whatever the others have already broken, which is most of the appeal. A player who leaves doesn't vanish — their peasant becomes an NPC follower who can still be killed, captured or carried. The party stays four people.

**Solo play is the same game.** One player controls one peasant and the other three follow as NPCs. Not a separate mode, not a different balance.

**No PvP.** The party is a single faction in the relations matrix. Players can disagree loudly about what to do; they cannot fight each other.

---

## 7. Information design

The core rule: **the player's knowledge is a strict subset of world state.** You know what you saw and what someone told you. Nothing else.

**No numbers.** Standing is never shown as a value. You read it from behaviour: whether they let you into their chamber, whether they trade, whether they post a watcher when you leave, whether they use your name.

**Hunger is a body, not a bar.** As the party gets hungrier, hearing range shortens, sneaking gets worse, carrying capacity falls. You feel it before you're told it.

**The chronicle is a memory, not a feed.** The full log exists in the simulation, but the player only ever sees entries they witnessed or were told. Sitting at a fire and comparing notes is how the party assembles what they know. Ovik the walker is the main delivery mechanism for everything happening out of sight, and he editorialises.

**The map is drawn, not given.** You have what you've walked and what you've been told about. Camps will trade directions.

**Sound is the primary interface.** In the dark, audio carries state that other games put on a HUD: a hunting party's direction, water level changing after you touched the sluices, a chamber going quiet because the herd is gone. Budget for audio before art.

---

## Decisions I made that are worth challenging

- **The world pauses between sessions.** Defensible either way. Persistent ticking is more dramatic and much crueller.
- **No host migration.** Purely a scope call.
- **Capture rather than death.** I'm confident on this one, but it does mean the party is nearly unkillable by the thing the game is mostly about, and that has to be paid for elsewhere — starvation and predators need real teeth.
- **90 seconds a tick.** Chosen so a collapse takes roughly half an hour. Everything scales off it, so change it now if you're going to.
