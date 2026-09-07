# Standing Order

*Design document — v0.1. Names marked (provisional) are placeholders.*

---

## What it is

A real-time online co-op game for 2–4 players. You are peasants. The ground opened during an earthquake and dropped you into a dwarven ruin that has been sealed for four hundred years. Four cultures live down there. All of them are stronger than you. Two of them think you were foretold.

You are trying to get out. Everything else that happens is the world going about its business around you.

**The pitch, in one sentence:** the goblins hunted the ridge too hard, so the dragon starved — and nobody wrote that.

---

## Why this isn't another cave game

The underground co-op space is crowded, and Deep Rock Galactic owns it. Every game in that space generates a world and then leaves it inert: the caves wait for you.

Ours doesn't. Four camps run a full simulation of hunting, ecology, politics, succession and faith whether the players are present or not. The differentiator is never the setting — it's consequence. This has to be visible in the first ten minutes or players will file the game next to the ones it isn't like.

**The rule for every design decision:** if you deleted the camps, would this still work? If yes, it's the wrong feature.

---

## The premise

The village of Marrowing (provisional) sits above land owned by Count Doudelfas (provisional). An earthquake opens a pitfall. Four villagers go down — by accident, or looking for a lost animal, or because they were the ones standing closest.

The way back up collapses behind them.

Below is **Deepholt** (provisional): not a fortress, a sealed biosphere. The dwarves built cisterns, air shafts, fungus farms and livestock pens, then died or left. The system kept running unattended for centuries. Every creature down there is descended from dwarven labour, livestock or vermin, and they are all fighting over the remains of infrastructure none of them can rebuild.

The earthquake that dropped the players also cracked the seal. **The simulation's tick zero is the players' arrival.** For four hundred years the cavern held equilibrium. It stops holding on the day you land in it.

### The party

Peasants. Pitchforks, aprons, one decent knife between four. They do not level up into heroes.

This is a load-bearing decision, not a joke. Adventurers can fight through a political situation, which would make the entire simulation optional content. Peasants can't. Every camp outmatches you, so negotiating, bribing, playing factions against each other and running away are the actual game.

Expect constant pressure to drift back toward adventurers — a sword, then a spell, then a boss. Every step that way heads toward the game we're deliberately not making. **We are not powerful.** Write it on the wall.

---

## Tone

Deadpan on both tracks at once. The chronicle records four centuries of collapse, three faction wars and a usurpation among the Ashfang — and also that Bill traded his boot for a glowslug. Same register, same timestamps.

We never write jokes. The comedy is structural: enormous politics, unqualified protagonists, one shared log.

---

## The prophecy

There is a prophecy about those who fall from the ceiling. Every camp holds a different corrupted copy.

It is not a prophecy. It is a fragment of dwarven maintenance documentation, recopied by illiterates for four hundred years:

> *When the ceiling opens, those who fall are to be conducted to the cistern.*

That was an evacuation procedure. It has been read as scripture. The players have been mistaken for messiahs; they have actually been mistaken for a plumbing callout.

**The prophecy is never confirmed.** The moment the game validates it literally, we become the thing we're parodying. It is true only in effect: the camps believe it, belief moves the simulation, the simulation produces events, the events confirm the belief.

### Creed

Each camp carries one value — how literally it takes the prophecy. This sets their opening standing toward the party *before the players have done anything*, which is how "some camps are hostile" falls out of the design rather than being an arbitrary flag.

The same action reads three ways. You hunt out a chamber: the devout see a sign, the indifferent see vermin, the opportunist sees leverage over the devout camp next door.

### The camps already know

They felt the earthquake. They armed themselves and argued about what it meant. They have been discussing you since before you stood up.

The players don't learn this for hours. Everything that reads as unexplained hostility or baffling generosity gets retroactively explained. The chronicle can even show it early — *the Sporewardens debate the sign* — while the player has no idea what that means yet.

---

## The four camps

Placeholder names from the prototype. All four differ in culture, intelligence, creed and taboo.

**The Sporewardens** — pale, near-blind farmhand descendants who tend the fungal mats in the Fungal Deep. Numerous, well-fed, poorly defended. **Devout.** They are the emotional spine of a playthrough: the camp players naturally befriend first, and therefore the one whose faith is most likely to break.

**The Ashfang goblins** — descended from the labour force. Numerous, quick, belligerent, and the fastest adopters of new technology. If you drop a quiver, they'll be shooting it back at you within the hour.

**The Mirelurk clan** — amphibious fishers of the Black Sump. Traders and opportunists. Indifferent to the prophecy except as leverage over those who aren't.

**The Assayers** — kobolds who venerate the ridge dragon. Poor, few, extremely defensible. They have their own god, so they read the prophecy as heresy. Their taboo — they will not hunt the dragon's goats even while starving — makes them visibly irrational and exploitable.

---

## Systems

### The world tick

The heartbeat, running whether players act or not. Six steps: **sense** local state → **score** available actions → **pick** the highest → **resolve** all intents together → **propagate** consequences into memory → **log** it as a plain sentence.

The players are not special to this system. Breaking a wall just edits the map that step one senses.

The log is the debugging tool and, later, the story generator. If it reads like a history you'd want to explore, the design works.

### Ecology

Every chamber holds a three-tier food web: flora that regrows toward capacity, a named prey species that eats it and breeds, and in some chambers an apex predator. Camps hunt named animals, not an abstract resource.

This gives chambers identity. The Fungal Deep is the prize — huge mats, thirty glowslugs, no predator. Dragonspine is poor and dangerous but defensible. The Sealed Gate is nearly dead rock.

Overhunting is a real failure state. Strip a chamber and the prey collapse; it recovers if left alone. Prototype behaviour worth preserving: the crag goats were hunted out on tick 2, and thirty-three ticks later the ridge dragon starved out of Dragonspine entirely. Nobody killed the dragon. They ate its food.

### Hunting ranges

A camp hunts its home chamber and any connected chamber it knows. When two camps work the same ground, a poaching term pushes them toward conflict — **territorial disputes emerge from the ecology instead of being coded as rules.**

### The party is a fifth faction

Peasants fall in with nothing and have to eat. The only food is the ecology the camps depend on.

So the party damages the ecosystem *by surviving*, using the same hunting code the camps use. Hunt the Fungal Deep and you compete with the Sporewardens, your standing drops, they range further, and they collide with someone else. Consequence without malice — nearly free to build, and the tightest possible fit between story and system.

### Politics

**Intelligence is how many options a camp can see.** A dim camp scores hunt, forage, fortify, raid, migrate. A cunning one gets extra rows: negotiate, demand tribute, offer alliance, betray. One AI, gated menu.

**Hierarchy is the same system pointed inward.** Each camp has a leader and two or three notables with loyalty and ambition. Bad ticks drain loyalty. When ambition beats loyalty, a notable takes the camp — and because the new leader has a different temperament, the camp's whole behaviour flips.

**Relations are one number per pair,** −100 to 100. Poaching drops it, shared enemies raise it, gifts raise it. Alliance is a threshold, not a special mechanic. Betrayal is an ambitious leader raiding someone whose standing is still high — and everyone else's standing with the betrayer craters, so treachery has a price the world enforces.

The party sits in the same matrix.

### Faith collapse

The most dramatic system in the game, and the inverse of everything else.

Faith erodes on specific acts: a taboo broken, a promise unkept, a sacred chamber hunted out. Each logs at the time in language the player doesn't yet understand, so the break is reconstructable in hindsight — and it will turn out to be something stupid they did in hour one.

When it snaps, the camp goes **zealot**. Fervour suppresses forage, migrate and fortify, and multiplies one score: reach the party. They will hunt you while starving. This is historically accurate, not a caricature — failed prophecy typically produces intensified commitment, not abandonment. The group concludes the sign was misread and that the false claimant must be destroyed.

**It must cost them.** A camp that ignores hunger dies, its grounds go unworked, and its neighbours' balance shifts. You didn't just make an enemy — you doomed them, and the fallout is regional.

**Schism, not uniform rage.** The camp splits: hardliners want you dead, a remnant insists the sign still holds. That's a succession crisis with a theological trigger, running through the hierarchy system. The splinter is the escape valve — one mistake shouldn't lock players out of a third of the map forever.

**Atonement exists and is expensive.** Not a dialogue apology; something material, over many ticks, which hardliners read as further proof of deceit.

### Research

Each camp has a tech level that rises with prosperity and contact. Three or four steps.

The players are a tech vector. Drop a quiver, trade a knife, and eight ticks later the Ashfang are shooting at you with it. Funniest possible consequence system, roughly thirty lines of code.

### Quests

Derive them from world state; don't generate them freely at runtime. The simulation already knows the Ashfang are out of arrows, the Sporewardens are starving, and that a notable just usurped a war-chief. Template the language against those facts and quests are never the same because the *world* is never the same — at zero cost per session. Runtime generation can be layered on later for flavour text.

---

## Real-time and co-op

Play is real-time exploration for 2–4 friends online. That has consequences worth being blunt about.

**The simulation runs on a wall clock**, one world tick every few real minutes, on an authoritative host so all players see the same world. It keeps ticking while players stand still, argue, or walk somewhere.

**The chronicle can't be a wall of text.** In real time the log surfaces as ambient information: rumours traded by camps, smoke, distant noise, a scouting party seen crossing a tunnel. The full chronicle is something you consult, not something you read.

**Scope warning.** Real-time + online co-op + a persistent authoritative simulation is a large amount of engineering for one day a week. The simulation is the differentiator and should be built first, headless, and proven. Networking is the last layer, not the first.

---

## The loop

Explore → meet a camp → work out what it wants → get it by trading, lying, hunting for it, or setting it against a neighbour → discover what that cost somewhere else on the map → repeat, further down.

Progression is not power. It's being better connected, better equipped with dwarven leftovers you don't understand, and knowing which chambers are safe when.

The exit is held by the camps. The Cistern — the dwarven regulator that decides who eats — is what everyone wants. So getting out and deciding who inherits Deepholt turn out to be the same question, and the joke is that you never wanted to inherit anything.

---

## Build order

The onion. Nothing in a later layer starts before the one before it works.

1. **Core.** Headless world tick with ecology, hunting ranges, migration and raiding. Read the log. Tune until it reads like history. *(Done — prototype exists.)*
2. **Politics.** Relations matrix, hierarchy with named notables, alliance and betrayal thresholds.
3. **Faith.** Creed, erosion triggers, zealotry, schism, atonement.
4. **The party as a faction.** Hunger, hunting, standing, dialogue.
5. **Real-time shell.** Player movement, exploration, ambient surfacing of the chronicle.
6. **Co-op.** Authoritative host, 2–4 players.
7. **Everything else.** Research, quest templating, art, UX, story polish.

---

## Open questions

- Does the village above know the party fell in? If someone is digging toward them, the players have a clock — and the camps have an enormous reason to care about them, because the players are the crack in a sealed world.
- Are the four peasants defined characters or made by players?
- Does the party ever learn the prophecy is a maintenance placard, or does only the audience?
- What does the Cistern physically do, and what happens if it stops?
- Names for everything currently in brackets.
