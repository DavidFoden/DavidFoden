# Standing Order — Content Plan

*How the writing, chambers and audio actually get made. v0.1.*

---

# PART 1 — The constraint

One developer, roughly one day a week, with an AI agent for drafting.

That is about **50 working days a year.** Every number in this document is measured against that, because a content plan that ignores throughput is a wish list.

The honest total for full content is in Part 9. It is large. Part 10 says what to cut.

---

# PART 2 — Two phases, and the line between them

**The legibility gate is the divide.** Almost nothing should be produced before it, because a world nobody can read does not need writing, art or audio.

But the gate cannot be run with nothing. Testers need enough content to read the world at all. So:

**Phase 1 — gate content.** The minimum needed to run the legibility and silent-play gates. Deliberately thin, deliberately disposable.

**Phase 2 — production content.** Everything else, and only if the gate passes.

Content produced in Phase 1 should be assumed rewritten. Do not polish it.

---

# PART 3 — Phase 1: gate content

This is the whole list. Resist adding to it.

| Item | Count | Why this much |
|---|---|---|
| Chambers whiteboxed | **3** | One rich (Fungal Deep), one poor (Ashvents), one connector (Long Gallery). Enough to test scale, tunnels and travel time |
| Room tones | 3 | One per chamber, placeholder quality |
| Life beds | 2 | Enough to test that silence reads |
| Camp sound sets | 2 | Sporewardens and Ashfang — the softest and the loudest |
| Band audio | 2 | Hunting party and war band. **The most important asset in Phase 1** |
| Beats written | **5** | B01 The offering · B03 Collected · B16 Empty ground · B36 The column · B20 The quiet chamber |
| Dialogue fragments | ~30 | Two camps only, enough for one conversation each |
| Co-signals built | 4 | Torch bloom, ceiling dust, fleeing prey, stripped chamber |
| UI screens | 1 | The fire, at wireframe quality |

That is the smallest set that lets a stranger walk into a dark tunnel, hear and see a war band pass, follow it or not, and afterwards say what a camp was about to do and why.

**Everything else waits.**

---

# PART 4 — The voice bible comes first

**Before any of the 200 fragments, write the six registers.** One page each: Sporewardens, Ashfang, Mirelurks, Assayers, Tallow, Ovik.

The test for each page: hand somebody five lines with the speaker removed and they identify who is talking. If they can't, the page is not finished and writing two hundred fragments against it will produce two hundred fragments in the same voice.

This is roughly two days of work and it gates the largest single content item in the project. Do it early — it is the highest-leverage writing in Phase 2, and it can be drafted before the gate because it costs almost nothing.

Sketches already exist in the systems document. They need expanding into pages with example lines, forbidden constructions, and how each voice handles refusal, threat, gratitude and grief.

---

# PART 5 — Batching

**Batch by type, not by area.** The instinct is to finish the Fungal Deep completely — geometry, audio, camp, dialogue — before moving on. Resist it.

Write **all six speakers' refusals in one sitting**, then all six greetings, then all six grievances. You only hear whether the voices are distinct when they are side by side, and you only catch drift when you are switching between them.

Same for chambers: whitebox all sixteen before art-passing any. Same for room tones: record or source all sixteen in one session, because they must be *distinct from each other*, which is a property of the set, not of any one of them.

The exception is Phase 1, where three chambers are built end to end precisely because the point is to test the whole vertical slice.

---

# PART 6 — Definition of done

**A beat is done when** it has a trigger already in the spec, a situation description, a reaction per creed where creed matters, at least one fact it surfaces, and a no-response path. Roughly a page.

**A fragment is done when** it names its slot, speaker, standing band, creed and world condition, reads in the right voice with the name removed, and surfaces a fact rather than flavour.

**A chamber is done (whitebox) when** it is walkable, correctly sized against the travel timings, has its tunnels in the right places, and is identifiable in one second from geometry alone.

**A room tone is done when** a tester can name the chamber blind.

**A life bed is done when** removing it is noticeable without being told.

**A co-signal is done when** the state it partners is readable with audio disabled.

---

# PART 7 — Working with an agent

What is safe to delegate, and what is not.

**Safe to draft:** dialogue fragments, item and creature descriptions, chamber descriptions, name lists, the epilogue variants. High volume, low individual stakes, and the voice bible constrains them.

**Draft then decide:** the forty beats. An agent can produce the situation text from the specified trigger. **The consequence is a design decision and stays with you** — a beat that changes the wrong thing corrupts the political state players are reasoning about.

**Never delegate:** the trigger conditions, anything that touches world state, and the tone of the chronicle. The chronicle's flat register is the entire comedic engine and it will drift toward being funny on purpose, which kills it.

**The hard rule, restated:** generated content may never invent a fact. A hallucinated grievance corrupts the simulation the player is reading. Fragments reference world state through slots filled by the simulation, never through invented specifics.

**Review protocol:** every batch gets read aloud. Voice drift and jokes-on-purpose are both audible and neither is visible on the page.

---

# PART 8 — Order of production

**Now, before the gate:** voice bible (2 days) · Phase 1 content list (Part 3).

**At the gate:** run legibility and silent-play in one session.

**After the gate, in order:**

1. **Beats, contact and revelation first** — B01–B09. These are what a new player meets, and they validate the whole beat system.
2. **Band beats** — B36–B39. Embodiment makes them the most visible thing in the game.
3. **Remaining chambers whiteboxed** — all thirteen, before any art.
4. **Room tones and life beds** — all in one session each, because distinctness is a property of the set.
5. **Faith beats** — B21–B25. The payoff, and they need layer two working.
6. **Fragments** — batched by slot, all speakers at once.
7. **Political, capture, ecological, tools and trade beats.**
8. **Art pass.**
9. **The Gate beat, endings, epilogues.**

---

# PART 9 — The honest number

Rough, and deliberately not optimistic.

| Item | Unit cost | Count | Days |
|---|---|---|---|
| Voice bible | — | 6 pages | 2 |
| Beats | ~1.5 h with drafting | 40 | 8 |
| Fragments | ~10 min each, batched | 200 | 4 |
| Chambers, whitebox | ~3 h | 16 | 6 |
| Chambers, art pass | ~2 days | 16 | 32 |
| Room tones | — | 16 | 3 |
| Life beds and creature audio | — | 14 species | 5 |
| Camp and band audio | — | 6 sets | 3 |
| Co-signals | ~half a day | 11 | 5 |
| UI screens | ~2 days | 6 | 12 |
| Endings and epilogues | — | 5 | 2 |
| Item, creature, chamber descriptions | — | ~80 | 3 |

**Roughly 85 working days of content.** At one day a week that is about **twenty months for content alone**, running alongside the code.

That number is the point of this document. It is not a reason to stop; it is a reason to decide now what gets cut rather than discovering it in month fourteen.

---

# PART 10 — The cut list

In the order things should go, and what each cut costs.

**1. Art pass on chambers — 32 days, by far the largest item.** Ship whiteboxed-plus: good lighting, good materials, minimal unique geometry. A dark cave is the most forgiving setting in games for this, and lighting does most of the work. **This is the cut to plan for, not the one to fear.**

**2. Beats, 40 down to 25.** Keep all contact, revelation, faith and band beats. Cut from political, tools and trade, which are the most substitutable. Saves 5 days.

**3. Fragments, 200 down to 120.** Fewer variants per slot, same coverage. The voices matter more than the variety. Saves 1.5 days.

**4. Creature audio, 14 species down to 8 families.** Grouped by size and habitat. **Costs more than it looks** — distinct life beds are what make silence legible per chamber — so cut this after the others, not before.

**5. UI polish.** The fire, map and inventory must be good. The menus can be plain.

**Do not cut:** the co-signals (accessibility), the room tones (chamber identity), the band audio (the early-warning system), or the voice bible. Each of those is load-bearing for something the game cannot work without.
