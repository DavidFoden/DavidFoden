# Standing Order — Production notes

*Art and audio direction, names, and the risks. v0.1.*

---

## Audio direction

**Budget audio before art.** In a dark cave, sound carries the information other games put on a HUD, and this game's whole premise is a world moving out of sight.

The design target: a player standing still with their eyes shut should be able to say roughly what's happening within two chambers. Direction, distance, and what kind of thing.

Four layers.

**Room tone per chamber.** Every chamber has a signature: dripping in the Weeping Stair, the low resonance of the Long Gallery, the wet slap of the Sump, the papery rustle of the Fungal Deep. Players should be able to name a chamber blind.

**Life.** The prey are audible and each species sounds distinct. This is the load-bearing one — a chamber that has been hunted out doesn't need a notification, it goes *quiet*. That silence should be genuinely unsettling, and it's the best possible way to teach ecology without a tutorial.

**Camps.** Work sounds, argument, movement of a hunting party. Direction and distance readable. A camp preparing to raid sounds different from a camp foraging, and players will learn the difference the hard way.

**The party.** Your own noise is a resource you spend. Footsteps, breathing when hungry, dropped gear, fire. Sneaking is quiet, fleeing is a broadcast.

No music during play. Score the fall, the endings, and nothing else.

---

## Art direction

Low priority, but a clear target keeps decisions cheap.

**Not heroic fantasy.** No armour, no glow, no lantern-lit adventure palette. The reference is agricultural and industrial: worn tools, wet stone, fungus, and dwarven infrastructure that is obviously infrastructure — pipes, sluices, channel markers, signage.

**Light is scarce and directional.** You mostly can't see the chamber you're in. Fire is the main light source and it's also a beacon, which is a design constraint before it's an aesthetic one.

**The camps read by silhouette and material**, not by fantasy-race design language. Sporewardens are pale and soft-edged, Ashfang are scrappy and asymmetric, Mirelurks are wet and layered, Assayers are ragged and ornamented.

**The dwarven layer is the odd one out.** Everything the dwarves built is square, precise and legible, and everything living down there is neither. That contrast is the whole setting in one image.

---

## Names

All provisional and none of them came from you. Replace freely — no system depends on a name.

| Thing | Current | Note |
|---|---|---|
| Game | Standing Order | Double meaning: the prophecy's phrasing, and four idiots down a hole |
| The ruin | Deepholt | Plain and readable |
| Village above | Marrowing | |
| Landowner | Count Doudelfas | Nod to your placeholder |
| Devout camp | The Sporewardens | |
| Aggressive camp | The Ashfang goblins | |
| Trading camp | The Mirelurk clan | |
| Rival faith | The Assayers | |
| Hermit | *unnamed* | Needs one |
| Trader | Ovik the walker | |
| The regulator | The Cistern | Keep — it's mundane on purpose |
| Chambers | Grimhollow, the Ashvents, the Fungal Deep, Spore Terraces, the Black Sump, Drowned Stacks, Dragonspine Ridge, the Weeping Stair, the Long Gallery, Ember Galleries, the Kiln, Rubble Stair, the Sealed Gate, the Fissure, the Cistern | |

The chamber names are doing real work — each one tells you what the place is before you get there — so I'd change those last.

---

## Risk register

Ordered by how likely they are to kill the project.

**1. Scope against cadence.** Real-time, online co-op, persistent authoritative simulation, one working day a week. This is the risk. Everything else is a detail.
*Mitigation:* the onion is the mitigation. Nothing in layer five starts until a player can watch the chronicle and predict what a camp does next. If that never happens, the game was never going to work and you've lost weeks, not years.

**2. Drift back toward adventurers.** Someone suggests a sword, then a spell, then a boss. Each step is individually reasonable and the destination is a worse version of a game that already exists and is beloved.
*Mitigation:* fighting exists but does not scale — no stat, tier or level may be added. Treat additions as constitutional amendments.

**3. The simulation is legible to us and opaque to players.** We can read the log. A player in a dark cave in real time cannot. If they can't perceive consequence, the entire differentiator is invisible and they'll file this next to every other cave co-op game.
*Mitigation:* the audio design above, Ovik, and the prediction test.

**4. Writing volume.** Forty beats, four camp voices, two hundred dialogue fragments. Unglamorous and the most likely thing to stall.
*Mitigation:* beats first, dialogue thin until beats are proven in play.

**5. Balance regression.** Every system added to the simulation has broken the previous balance so far — growth broke expansion, expansion broke the land rush, ranges broke the wars. Politics and faith will do it again.
*Mitigation:* the thousand-tick no-player test as an automated check. If any camp dies with no player present, the build is wrong.

**6. Multiplayer determinism.** Host-authoritative with clients sending intents is the simple answer, but a simulation this stateful will expose desync fast.
*Mitigation:* clients render, host decides, never simulate on the client.

**7. Nobody has playtested the tone.** The comedy is entirely structural — deadpan chronicle, unqualified protagonists. Structural comedy either lands completely or reads as flat.
*Mitigation:* test it early and cheaply. Read a chronicle aloud to people who aren't building it and watch whether they laugh.
