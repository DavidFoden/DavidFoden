# Standing Order — Layer Four: The Real-Time Shell

*Build specification, v0.1. Sits on layers one to three and the embodiment amendment.*

This is the layer that makes the simulation perceivable. Nothing here adds a system — it exists so that a person standing in a dark tunnel can tell what the world is doing.

**Do not start this layer until the legibility gate in §11 can be attempted.**

---

## 1. Camera and controls

**First person.** A call, and a challengeable one.

The reasons: darkness and sound are the sensing layer, and first person makes both load-bearing rather than decorative. It removes the animation quality bar for the player's own body, which matters enormously for a project running one day a week. And in co-op you still see your three friends' bodies, which is where all the physical comedy lives — someone carrying a body, someone dropping everything to run.

The cost: you can't see your own peasant. Given the party is deliberately unremarkable, that's cheap.

**Controls.** Move, sneak (hold), interact, use held item, drop, listen (hold — reduces own noise to zero and sharpens spatial audio), and a radial for the verb set. No hotbar of abilities, because there are no abilities.

**Listen must be a held input, not a toggle.** Standing still to hear is a decision with a cost, and it's the single most characteristic action in the game.

---

## 2. The chamber as a space

A graph node becomes a room. Sizes are set by the tick timings in the embodiment document, so the two never disagree.

| | |
|---|---|
| Chamber diameter | 60–120 m |
| Time to cross | 45–90 seconds |
| Tunnel length | 40–110 m |
| Time to traverse a tunnel | 0.6–1.4 ticks (54–126 s) — matches the embodiment table exactly |
| Full map traversal | roughly 15 minutes |

**Verticality is how chambers stay memorable.** Grimhollow is a wide grazing floor; the Fungal Deep is a cathedral you look up into; the Weeping Stair is a vertical descent; the Long Gallery is flat, straight and exposed. A player should know where they are from one second of geometry and room tone.

**Tunnels are gameplay, not corridors.** They're where ambushes work, where bands get blocked, and where the party can hear something coming before it arrives. Narrow enough that four peasants with pitchforks in a tunnel is a genuinely viable proposition, which is the only situation in the game where that's true.

---

## 3. Simulation level of detail

Three tiers. This is what makes a sixteen-chamber living world affordable.

| Tier | Where | What exists |
|---|---|---|
| **Present** | Party's chamber and directly adjacent | Full 3D agents, animation, physics, real positions |
| **Near** | Within three tunnels | Graph positions only, plus spatial audio cues at range |
| **Far** | Everything else | Graph state only. No audio, no rendering |

Bands promote and demote as the party moves. A band entering the Present tier instantiates at the correct position along its route, not at the chamber entrance — otherwise interception breaks.

**The simulation never changes with tier.** Layers one to three run identically whether anyone is watching. LOD governs representation only. Any bug where a camp behaves differently when observed is a critical failure, because it invalidates the entire premise.

---

## 4. Audio

The production notes make audio the priority. Here is what that means technically.

**Occlusion follows the tunnel graph, not raycasts.** Sound attenuates per tunnel traversed, using the same distance function as detection in layer three. This is cheap, it's consistent with the simulation, and it means what a player hears and what a camp hears use one code path.

**Four buses:** room tone, life, camps, party. Mixed so that life and camps are always audible above tone.

**The critical cue is silence.** A hunted-out chamber loses its life bus. That absence is how ecology teaches itself, and it must survive mixing decisions — do not let ambience fill the gap.

**Band audio at range.** A war band is audible two chambers out at magnitude 9; a hunting party at 5. This is the early-warning system, so it needs directionality that survives being three rooms away and behind rock.

**Listening mode** narrows the mix, boosts directional clarity, and drops the party's own noise floor to zero.

---

## 5. Light

Light is scarce, directional and mostly carried. Fire is the main source, and it is simultaneously warmth, cooking, safety and a beacon visible one chamber out — the trade-off is the point, and no lighting decision should soften it.

Dwarven infrastructure is the exception: channel markers and Cistern signage have their own faint residual glow, which is how players learn to recognise the built layer from the grown one at a glance.

---

## 6. Interface

**No HUD.** Not a minimal HUD — none.

- **Hunger** is read from the body: hearing range contracts, hands shake, carrying fails.
- **Standing** is read from behaviour: whether they let you in, whether they trade, whether someone watches you leave.
- **Held item** is visible in the hand. That's the only persistent on-screen information.

**Three screens exist, all diegetic:**

**The fire.** Sit at a fire and the party compares notes. This is where the filtered chronicle from layer three is read, and it's a shared screen — everyone sees it, so it's also where the arguing happens.

**The map.** A drawn paper map that fills in as you explore, and that camps can add to when they give directions. Physically held; you can't read it while running.

**Inventory.** Slot-based, visible, and shared load is negotiated in the fiction rather than in a menu.

---

## 7. Networking

**Host-authoritative, as decided in the mechanics document.**

| Concern | Approach |
|---|---|
| Simulation | Host only. Clients never simulate camps, ecology, or bands |
| Player movement | Client-predicted, host-reconciled. Movement is the only prediction |
| Bands | Replicated only in the Present tier. Near-tier bands replicate as an audio cue and a graph position |
| Tick state | Delta-replicated on tick boundaries — 90 seconds is generous, so send full camp state each tick and don't optimise early |
| Knowledge | **Per-player.** Each client holds its own `knowledge` object. The host must never send world state a player hasn't earned |
| Join in progress | Client receives the world snapshot plus an empty knowledge set — a joining friend genuinely knows nothing |

**The knowledge rule is a networking rule, not just a UI rule.** If the host sends the full chronicle and the client filters it, someone will read the packets. Filter on the host.

Twelve concurrent bands, four players, sixteen chambers. This is a small networking problem provided nobody simulates on the client.

---

## 8. Saving

Save on tick boundaries only, never mid-tick.

```
save = { seed, tick, chambers[], camps[], bands[], party, knowledgePerPlayer[], flags }
```

The world pauses between sessions per the mechanics document, so a save is a complete freeze — bands mid-journey resume exactly where they stopped.

Autosave every 10 ticks and on session end. No manual saves and no reloading to undo a consequence; that would dismantle the entire game.

---

## 9. Performance budget

Modest by design, because the interesting part is the simulation.

- Present tier: up to 60 agents rendered (two bands plus wildlife plus the party)
- Near tier: 12 bands as positions and audio sources
- Far tier: pure data, negligible
- Target: 60 fps on mid-range hardware from five years ago

If the game is ever expensive, it's because of geometry and lighting, not the simulation. The whole world model is a few hundred floats.

**On engine:** your Unity experience is the deciding factor and it's the right call. The only requirement layer four imposes is that the simulation lives in plain C# with no engine dependencies, so it can keep being run headless for the test conditions in every previous document.

---

## 10. Rendering bands

Bands are the main thing that makes the world feel inhabited, so they need to read instantly.

- **Silhouette by culture** at any distance and light level. You should know it's Ashfang before you can see a face.
- **Purpose readable from formation and equipment.** A hunting party carries snares and moves loosely. A war band moves in file and carries weapons. Players must be able to tell at a glance which one just walked past, because that decides whether they follow it or warn someone.
- **Size reads as threat.** Band member count is visible in the group's footprint.

---

## 11. The legibility gate

This is the reason layer four exists, and the checkpoint before any work in layers five and beyond.

**The test.** Five people who have not worked on the game play for 30 minutes. Then, at three separate moments, they are asked: *what is that camp about to do, and why?*

**Pass condition: 60% correct across the group.**

If they can't predict, the simulation is invisible, the differentiator doesn't exist, and the game is a cave co-op game competing with Deep Rock Galactic on Deep Rock Galactic's terms. Fix perception before adding anything.

Secondary questions worth asking in the same session:
- Which camp do you feel most warmly toward, and why? (Tests whether creed reads.)
- What did you do that you now regret? (Tests whether consequence is attributable.)
- What's happening somewhere you can't see? (Tests audio and Ovik.)

---

## 12. Test conditions

1. **LOD invariance.** Run 300 ticks with the party parked in one chamber, and 300 with the party touring the map. Camp behaviour statistics must match within noise.
2. **Band instantiation.** A band promoted to Present appears at its true route position, not at a chamber entrance.
3. **Audio range.** A war band two chambers away is audible and directionally identifiable by a blindfolded tester.
4. **Silence reads.** Testers can identify a hunted-out chamber by sound alone.
5. **Knowledge isolation.** Packet inspection shows no unearned world state reaching any client.
6. **Join in progress.** A joining player's map and chronicle are empty.
7. **Save fidelity.** Save mid-journey, reload, and every band resumes on the same route at the same progress.
8. **Frame budget.** Two bands plus wildlife plus four players in one chamber holds 60 fps.

---

## 13. Build order

1. One chamber, one tunnel, walking, first-person, in the dark.
2. Audio: room tone, occlusion by tunnel graph, listening mode. Before anything else visual.
3. Hook the headless simulation in as-is. Bands as capsules. Ugly and correct.
4. LOD tiers and band promotion.
5. Fire, map and inventory screens.
6. Networking, host-authoritative, movement prediction only.
7. Band silhouettes and formation reading.
8. **The legibility gate.** Stop here until it passes.
9. Lighting and art pass.

Steps 1 to 4 are the game. Everything after is presentation, and step 8 decides whether the presentation worked.
