# Standing Order — Visual Identity

*Palette, type, lighting, material language and screen briefs. Specification only — no assets. v0.1.*

---

# PART 1 — The one distinction that matters

**The document palette is not the game palette.**

Everything you've seen so far — the limestone background, the peat ink, the malachite bars — is the palette of a *survey document about Deepholt*. It is pale because it is paper. The game is a lightless cave four hundred metres underground.

They are two related but separate systems, and confusing them will produce a game that looks like a spreadsheet.

- **The world palette** is what the player sees through a first-person camera by firelight.
- **The document palette** is the diegetic paper layer — the map you carry, notes at the fire. It is the survey palette, because in the fiction it *is* paper.

Both are specified below. They meet only at the map screen, which is the joke: the only bright, legible thing in Deepholt is a piece of paper somebody drew.

---

# PART 2 — The world palette

Lit almost entirely by carried fire, so the palette is a warm source against cold absence.

| Role | Colour | Hex | Notes |
|---|---|---|---|
| Fire, near | Ember | `#E8873A` | The only saturated warm light. Falls off fast |
| Fire, mid | Tallow | `#C4762F` | Named for the hermit, and for what light costs |
| Stone, lit | Bone limestone | `#B9AE9A` | What most surfaces become in firelight |
| Stone, shadow | Wet slate | `#2A2E31` | Not black. Deepholt is damp, and damp reflects |
| The dark | Deep | `#0E1113` | Near-black with a blue cast. **Never pure black** |
| Water | Sump green | `#2F4A44` | Still, dark, slightly luminous where it moves |
| Fungal light | Glow | `#7FD0A8` | The only cool light source. Cold, faint, everywhere in the Deep |
| Dwarven metal | Iron | `#6E6A63` | Dull, uncorroded, obviously manufactured |
| Blood and rust | Oxide | `#8C3A24` | Shared by both, which is the point |

**Rules.**

Fire is the only bright thing, and it is always *yours* or somebody's — never ambient. If a chamber is lit and nobody lit it, that is a mistake.

**Never pure black.** The dark has a blue cast and a faint texture, because a player must be able to tell "unlit" from "nothing rendered."

The fungal glow is the one exception to fire, and it should make the Fungal Deep feel wrong rather than beautiful — cold light with no heat, in the richest chamber in the world.

---

# PART 3 — Camp identity, and why it isn't colour

Four camps must be identifiable in bad light at distance. Colour alone cannot carry that, for two reasons: it is dark, and roughly one man in twelve cannot separate the greens from the reds.

**So every camp is identified three ways, and colour is the weakest of them.**

| Camp | Colour | Hex | Luminance | Mark | Silhouette |
|---|---|---|---|---|---|
| Sporewardens | Deep green | `#2F5A43` | darkest | A spore cap — a filled dome | Soft-edged, stooped, layered in cloth |
| Ashfang | Bright rust | `#C05A2E` | mid-bright | A notch — an angular V | Scrappy, asymmetric, sharp protrusions |
| Mirelurks |  Pale slate |  `#7FA3BA` | mid | A wave — a horizontal double curve | Wet, smooth, heavily laden |
| Assayers | Bright ochre | `#E0A62B` | brightest | A balance — a vertical stroke with two arms | Ragged, ornamented, tall |

**Luminance is deliberately spread** across the four so they separate on a greyscale monitor. That is the accessibility test: **screenshot the game, desaturate it, and if you cannot tell the camps apart, the design has failed.**

Verified. Relative luminance runs 0.083 · 0.187 · 0.343 · 0.433, with no adjacent gap below 0.09. The first attempt failed this — the original Mirelurk slate `#6A8CA0` sat only 0.056 from the Ashfang rust, which is invisible desaturated. It was lightened until it cleared. **Re-run this check whenever a camp colour changes.**

The mark appears on banners, tools, territory markers and the map. It is the primary identifier; colour is reinforcement; silhouette does the work at distance.

---

# PART 4 — The document palette

The diegetic paper layer — the carried map, notes at the fire, the plate rubbings.

| Role | Colour | Hex |
|---|---|---|
| Paper | Limestone | `#D6DAD0` |
| Ink | Peat | `#241F1A` |
| Faded ink | Peat soft | `#524A42` |
| Rule lines | Rule | `#A9AFA1` |
| Correction, urgency | Oxide | `#8C3A24` |

Warm firelight falls across it in use, so the paper is never seen at full brightness — it is a pale object in an orange pool of light, which is what makes it feel like a real thing being held rather than an overlay.

---

# PART 5 — Type

Two families, both with a reason.

**Display — a slab serif.** Chapter cards, the endings, the plate. Slab because the dwarven layer is square and manufactured, and the type should feel cut rather than written. `Zilla Slab` is the working choice.

**Interface — a neutral grotesque with tabular figures.** The map, the fire, inventory. It must be legible small, in low contrast, over paper texture. `Archivo` is the working choice.

**No third face.** No handwriting font for the map — the map is drawn by a peasant, so its irregularity comes from the linework, not from a typeface pretending to be handwritten.

**The plate is set differently from everything else.** All caps, tight, mechanical, with its notice number. It should look like signage because it is signage, and that is the entire joke.

---

# PART 6 — Lighting

**Light is carried, scarce and directional.** Fire is the main source and it is simultaneously warmth, cooking, safety and a beacon visible one chamber away. No lighting decision may soften that trade.

Three sources only:

**Fire.** Warm, flickering, short range, and it announces you.
**Fungal glow.** Cold, faint, immobile, concentrated in the Deep and the Terraces. Enough to navigate by, not enough to work by.
**Dwarven residuals.** Channel markers and Cistern signage carry a faint worked luminescence. This is how a player learns to recognise the built layer from the grown one at a glance — follow the faint straight lines and you find infrastructure.

Everything else is the dark, and the dark has a floor colour, never true black.

---

# PART 7 — Material language

The setting in one image: **everything the dwarves built is square, precise and legible; everything living down there is neither.**

**The dwarven layer.** Cut stone, iron, right angles, consistent dimensions, incised lettering. Undamaged where it survives, because it was over-engineered. Signage everywhere, all of it mundane.

**The grown layer.** Fungal mats, moss, silt, irregular chambers, wet surfaces, accretion. Nothing is straight.

**The camps.** Built from the wreckage of the first using the logic of the second — dwarven plate lashed into a windbreak, a channel marker used as a tent pole. Every camp structure should read as *misuse of infrastructure*, because that is the whole premise.

---

# PART 8 — Screen briefs

Six screens. No HUD, so all of them are objects or moments rather than overlays.

**Main menu.** The plate, lit by a single fire, filling the frame. Options set as further lines on the notice. No characters, no vista, no dragon.

**Lobby.** Four places at a fire. Empty places are visibly empty. Joining fills one.

**The fire.** The shared screen where the party compares notes and the filtered chronicle is read. Warm pool of light, paper palette, everyone's peasant present. This is where arguing happens, so it must accommodate four people looking at one document.

**The map.** A held sheet, drawn in as you go, with camp marks added where you have met them and blank where you have not. Unreadable while moving. The blankness is the feature.

**Inventory.** Six slots per peasant, physical, laid out on ground or cloth. Shared load negotiated in the fiction, not in a menu.

**Endings.** The chronicle continuing for twenty ticks after you leave, set in the display face, over the dark. The world does not stop when you leave, and this screen is the argument.

---

# PART 9 — What to prototype first

In order, and each one is cheap:

1. **One chamber, one fire, in the dark.** Answers whether 60–120 metres feels right and whether the dark reads as navigable. Everything in this document depends on that answer.
2. **Four camp silhouettes at forty metres in firelight**, desaturated. If they don't separate, fix it before anything else exists.
3. **The plate.** It is one asset, it sets the type system, and it is the main menu.
4. **The map screen**, because the paper layer is the only place the two palettes meet and it needs to feel like an object.

Do not produce a full art pass for anything until the legibility gate passes. A world nobody can read does not need to be beautiful yet.
