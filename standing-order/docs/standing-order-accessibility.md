# Standing Order — Accessibility

*Design specification, v0.1. This is design work, not polish — it amends the existing specs, and those amendments are listed in Part 11.*

---

# PART 1 — The problem, stated honestly

This game deliberately puts world state in audio. Direction and distance of a war band, whether a herd is alive, what a camp is doing three chambers away, whether the water has stopped. The production notes put audio ahead of art for exactly that reason.

**As specified, a deaf player cannot play this game at all.** Not "plays it worse" — cannot perceive the systems the whole design exists to make perceivable.

The obvious fix is a HUD, and the no-HUD rule is load-bearing for the information design. So the work is finding a visual channel that is not a HUD, and that is the substance of this document.

Doing it now costs a few design decisions. Doing it after the shell is built costs a rewrite.

---

# PART 2 — The principle

> **No information exists in only one channel.**

Not "add captions." Every world state that a player is expected to perceive has **a sound and a physical tell in the world**. The tell is diegetic — light, dust, movement, water, wear — so it costs no HUD and it improves the game for everyone, including players with the sound on.

This is the same reasoning as camp identity: colour, mark and silhouette, three channels, colour weakest. Apply it to the whole game.

---

# PART 3 — The co-signal table

The core of the work. Every audio cue in the design gets a visual partner.

| State | Audio cue | Visual co-signal |
|---|---|---|
| War band approaching | Band noise, magnitude 9, two chambers | **Torchlight bloom at the tunnel mouth** before they arrive; dust shaken from the ceiling; prey animals fleeing past you the wrong way |
| Hunting party moving | Band noise, magnitude 5 | Fainter, single torch; no dust; animals disturbed but not stampeding |
| Chamber hunted out | Life bed absent — silence | Visibly no animals, stripped flora, bones and old traces, tracks going nowhere |
| Camp at work | Work sounds, direction | Smoke, firelight through the tunnel, moving silhouettes, drying racks |
| Camp preparing to raid | Different work sound set | Weapons being brought out, banners raised, the camp visibly gathering |
| Apex predator present | Distinctive call at range | Kill remains, cleared ground, prey absent in a ring around it, claw wear on stone |
| Water stopped (Cistern) | Running water ceases, map-wide | **Water level visibly drops**, channels darken, wet stone dries over the following ticks |
| Party hunger | Breathing changes | Hands shake, carrying fails, vision contracts — already specified |
| Your own noise | Footstep volume by surface | Dust and disturbance under your feet; startled small animals |
| A promise coming due | — | A physical token given at the time, visibly carried |
| Chamber identity | Room tone | Geometry and verticality — already specified, each chamber identifiable in one second |

**Note that most of these make the game better regardless.** Torchlight preceding a war band through a tunnel is a good scare whether or not you can hear it.

---

# PART 4 — Listen as a perception mode

`Listen` is already a held input that stops the player, silences their own noise, and sharpens spatial audio. It is the natural place to put a visual channel, because **it already has a cost** — you are standing still and vulnerable — so it grants no free information.

While held, the world renders its disturbances: air movement toward sound sources, dust drifting, water ripples propagating from the direction of the source, faint pulses along the tunnel that carries it. Direction and rough distance, expressed as physics rather than an icon.

**Available to everyone, always.** Not an accessibility mode that has to be enabled and admitted to. It is simply what concentrating looks like.

**Must be offered as toggle as well as hold** — see Part 8.

---

# PART 5 — The caption layer

Even with Parts 3 and 4, some information will remain audio-first. So: an **optional non-speech caption layer**, off by default, giving positional captions — the source, a direction, a distance band. *Scraping — north-east — far.*

**The no-HUD rule bends here, deliberately.** A design principle that excludes players is not a principle worth keeping. But it bends carefully:

- Off by default, so the intended experience is unchanged
- Styled as the paper layer — peat ink on limestone, the document palette — so it reads as the peasant's notes rather than a game overlay
- Positional and specific, never a transcript of the mix
- Never reveals more than the audio would. **Captions describe what a listener could hear, not what the simulation knows.** A caption must never leak world state the player has not earned, or it breaks the knowledge rule in Part 7 of the master spec.

That last point is the one to guard. It would be easy to implement captions from world state instead of from the audio events, and that would quietly hand caption users a knowledge advantage.

---

# PART 6 — Low vision and darkness

The game is deliberately dark, which is its own barrier.

- **Brightness floor and contrast options**, including a "raise the dark" setting that lifts `#0E1113` toward legibility without turning the cave into daylight
- **Interactable outlines** — an optional subtle rim on things that can be picked up, cleared, or talked to
- **Scalable interface text** on all three diegetic screens; the map and the fire must survive 150% text
- **The map must be legible at low contrast**, since it is paper in firelight

---

# PART 7 — Photosensitivity

**Specific and serious here, because fire is the primary light source and fire flickers.** A cave lit by torchlight is a flicker environment by design.

- A **flicker reduction** setting that damps the amplitude of fire modulation without removing warmth or falloff
- No strobing on any event — the Cistern cascade, assaults, and endings must not use rapid light pulses
- Cap the modulation rate of all light sources below the standard risk threshold

This needs to be built into the lighting model from the start, not added as a post-process later.

---

# PART 8 — Motor

- **Every held input has a toggle alternative.** `Listen` and `Sneak` are both held by design; both need toggles
- **Fully remappable controls**, including for the verb radial
- **No timing-critical inputs.** There are none currently and none should be added — carrying a friend, clearing rubble and forcing a mechanism are all duration, not dexterity
- **No mashing.** Escape from capture must never be a rapid-press
- Adjustable radial dwell time

---

# PART 9 — Cognitive, and the difficulty axis

**The chronicle at the fire is dense by design**, and it will be a barrier. Give it filters — this camp, this chamber, this session — and a plain-language summary line per entry group.

**Difficulty adjusts pressure, never numbers.** Do not add or remove camps, bands or enemies; that would change the simulation and invalidate the balance. Adjust the pressure the player is under:

| Setting | What it changes |
|---|---|
| Hunger rate | The clock, not the world |
| Band travel speed | How long you have to react to a sighting |
| Capture consequences | How much is taken, how long labour lasts |
| Faith erosion rate | How quickly a mistake becomes a crisis |

Every one of those is a player-facing constant. None of them touches Core.

---

# PART 10 — Multiplayer and communication

Co-op with voice chat excludes players who cannot use it.

- **The `signal` verb doubles as a ping.** It already exists as a gameplay action — deliberate noise at a chosen point — and it should also place a visible, temporary mark for the party. One verb, two jobs
- **Text chat with scalable text**
- **Subtitles for all diegetic speech**, including Tallow and Ovik
- A joining player's empty map and chronicle must be explicable without someone explaining it aloud

---

# PART 11 — What this changes in the existing specs

Explicit amendments. This is the part that justifies doing it now.

**Master 9.5 (Interface).** "No HUD" becomes "no HUD by default." An optional caption layer exists, styled as the paper layer, off by default.

**Master 9.6 (Networking).** Captions are generated from **audio events**, not from world state, so the knowledge rule holds. This is a data-flow constraint, not a UI one.

**Master 9.4 (Audio) and the art brief.** Every audio cue now requires a visual partner. This is real production scope: torch bloom, ceiling dust, fleeing animals, drying stone, kill remains. **Add to the inventory.**

**Master 9.x (Lighting).** Fire modulation must be rate-capped and dampable from the start.

**Master 4.1 (Verbs).** `Listen` gains a visual perception rendering, and both `Listen` and `Sneak` require toggle alternatives. `Signal` gains a ping function.

**Master 4.6 (Information design).** The strict subset rule now has a second clause: *and no accessibility affordance may widen that subset.*

**Systems — difficulty.** A player-facing pressure axis exists, and it must live in the Adapter layer, never in Core.

---

# PART 12 — Test conditions

Added to the master's list, and one of them is a gate.

**A1 — The silent-play gate.** Five testers play 30 minutes **with audio disabled**, then answer the legibility gate's question: *what is that camp about to do, and why?* **Pass condition: 50% correct**, against 60% for the hearing gate. If a deaf player cannot read the world at close to the same rate, Part 3 is incomplete.

**A2 — Caption honesty.** Automated. No caption may reference an entity the player's `knowledge` does not contain.

**A3 — Desaturation.** Screenshot, desaturate, camps distinguishable. Already verified; re-run on any colour change.

**A4 — Flicker.** No light source modulates above the risk threshold with flicker reduction off, and modulation amplitude drops measurably with it on.

**A5 — Text scale.** All three diegetic screens legible and unclipped at 150%.

**A6 — Toggle parity.** Every held input completable as a toggle.

---

# PART 13 — What to do first

1. **Add the co-signals to the art brief now**, before any chamber is built. Retrofitting torch bloom and ceiling dust into finished environments is expensive; designing them in is nearly free.
2. **Cap fire modulation in the lighting model** on day one of the shell.
3. **Build `Listen`'s visual rendering alongside its audio**, not after — they are the same feature.
4. **Run the silent-play gate at the same session as the legibility gate.** Same testers, same build, headphones off for one of the three questions.
