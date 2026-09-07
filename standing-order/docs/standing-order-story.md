# Standing Order — Story

*Narrative architecture, v0.1. Companion to the design document.*

---

## 1. How to read this

This is not a plot. A plot would fight the game.

The moment we write "and then the Sporewardens betray you in chapter three," we've committed to the Sporewardens being alive, devout, and adjacent to the player in chapter three — and our simulation cheerfully starves them out on tick forty for reasons nobody scripted. Either we constrain the simulation until it can't surprise anyone, or we write scenes that never fire. Both are worse than what we have.

So this document defines four things instead:

- **Invariants** — the handful of events that happen in every playthrough, because we make them happen.
- **Act thresholds** — the story's shape, expressed as world-state conditions rather than scene numbers.
- **A beat library** — authored dramatic situations, each with a trigger. The simulation decides which ones fire and when. Most playthroughs will see maybe a third of them.
- **Dialogue architecture** — how camps talk, and what changes what they say.

The story is then *assembled* per playthrough, from the same parts, in an order the world chose. That is the product.

---

## 2. Invariants

Five things are true every single time. Everything else is negotiable.

**You fall.** Four peasants, an earthquake, a hole. No preamble, no character creation lore dump, no tutorial cave. Under two minutes from launch to standing in the dark with a pitchfork.

**The way back closes.** Not a cutscene of rubble — you can *see* the light for the first few minutes, and then the aftershock comes. Players should have already started planning to climb out before that option is removed.

**The camps felt it too.** Every camp gets a fear spike on tick zero: arming, fortifying, arguing. The first thing the player overhears from any camp is panic about something that just happened to *them*. This establishes, before any dialogue, that the world is not waiting.

**Someone recognises you.** Within the first hour, a camp treats the party as significant for reasons the party cannot possibly understand. Not explained. Just weird.

**The Gate is the ending.** Wherever the playthrough goes, it resolves at the Sealed Gate, and it cannot be resolved without the Cistern.

That is the entire authored spine. Everything below is conditional.

---

## 3. The four acts, as thresholds

Acts aren't chapters. They're states the world enters, and the player can spend wildly different amounts of time in each.

### Act I — Down here
**Begins:** on landing.
**Ends:** first sustained contact with any camp.

The player's problem is immediate and stupid: they are hungry, it is dark, and something is moving. They must eat, which means hunting, which means entering the food web as a competitor before they know there *is* a food web.

The design job of Act I is to make hunger teach ecology. You eat the easy prey near where you landed. The consequences of that arrive in Act III, and by then nobody will remember doing it. That is the joke and the thesis.

### Act II — They know something
**Begins:** first sustained camp contact.
**Ends:** the party learns the prophecy exists.

The register here is confusion. Camps react to the party with intensity out of all proportion — one shelters them, another wants them driven off, a third wants to sell them. Nobody explains why. The chronicle is visibly discussing something the player can't read.

Act II ends when someone tells them. Usually the hermit in the Kiln, who is the only literate creature in Deepholt. Occasionally a Mirelurk, who will charge for it. Rarely a Sporewarden, who will get it wrong in an interesting way.

### Act III — Consequence
**Begins:** the prophecy is known.
**Ends:** the first irreversible change the party caused — a camp collapses, a faith breaks, a leader falls, a chamber is hunted out.

The longest act and the real game. The party now knows they have leverage and no idea how much. Everything they do lands in a political system they only half understand.

Crucially, Act III's ending condition is *something the player did*, not something we scheduled. Some groups will trigger it in twenty minutes by being reckless. Some will spend hours being careful and trigger it by being careful in the wrong place.

### Act IV — The Gate
**Begins:** the party understands that the Cistern controls the Gate.
**Ends:** at the Gate.

The endgame is a political question wearing a puzzle's clothes. The Gate opens for whoever controls the Cistern. Controlling the Cistern means either holding it, or having whoever holds it owe you.

So the final act is: who do you back, and what do you owe them?

---

## 4. The cast as dramatic engines

Each camp is here to produce a different *kind* of story. If two camps produce the same kind, one of them is redundant.

**The Sporewardens — tragedy.** Devout, generous, defenceless, and wrong about you. They are the camp that helps first and asks nothing, which is exactly why disappointing them is the game's cruellest possible outcome. Their arc is almost always downward, and the player almost always causes it without meaning to.

**The Ashfang — farce and escalation.** Belligerent, stupid, and infinitely imitative. Every interaction with them makes them more dangerous in a way that is funny right up until it isn't. Give them anything and they will use it on you.

**The Mirelurks — transaction.** The only camp that negotiates as an equal. Everything is available and everything has a price, including you. They generate the plot's leverage: they know things, they'll sell things, and they remember debts.

**The Assayers — obstacle and mirror.** A rival faith that reads you as heresy. Mechanically the hardest camp to move, narratively the most useful, because they demonstrate that devotion isn't a bug in the Sporewardens — it's how everyone down here works.

**The hermit of the Kiln — the exposition valve.** Belongs to no camp, holds no territory, can read. He is how the player learns anything they can't infer. He should be unhelpful, specific, and clearly hiding which side he's on, largely because he isn't on one.

**Ovik the walker — the news wire.** A trader with a fixed circuit. In a real-time game the chronicle can't be a text dump, so Ovik is the delivery mechanism: he tells you what happened three chambers away, for a price, with his own spin on it.

---

## 5. The beat library

Authored situations. Each has a trigger expressed in world state, a shape, and consequences that feed back into the simulation. The simulation fires them; we never schedule them.

Aim is roughly forty beats at ship. Sixteen sketched here.

### Contact beats

**B01 — The offering.** *Trigger:* first contact with the Sporewardens, standing ≥ 0. They feed the party, unprompted, from stores they can't spare, and become measurably hungrier for it. *Consequence:* Sporewarden food drops; the party's standing rises; a debt exists that the party doesn't know about.

**B02 — Priced.** *Trigger:* first contact with the Mirelurks. They immediately try to establish what the party is worth, to whom. *Consequence:* opens the information economy. They will name a price for the prophecy.

**B03 — Test by arrow.** *Trigger:* first contact with the Ashfang at standing < 0. They attack, badly, and lose interest if the party runs. *Consequence:* the Ashfang have now seen whatever the party used to defend themselves, and their tech track advances toward it.

**B04 — Heretic.** *Trigger:* first contact with the Assayers. They name the party as false and refuse to trade. *Consequence:* permanent hostile floor unless the party engages with their faith on its own terms.

### Revelation beats

**B05 — The placard.** *Trigger:* party reaches the Kiln. The hermit reads them the dwarven text. Flat, literal, without ceremony. *Consequence:* Act II ends. The player now knows it's a maintenance notice. The camps never will.

**B06 — Four gospels.** *Trigger:* party has heard the prophecy from two different camps. The versions don't match. *Consequence:* unlocks the ability to *lie* about the prophecy — quote one camp's version at another.

**B07 — The plumbing.** *Trigger:* party reaches the Cistern. Dwarven signage everywhere, all of it mundane, all of it revered by whoever is standing guard. *Consequence:* the player understands the endgame before any character does.

### Political beats

**B08 — The poaching complaint.** *Trigger:* the party has hunted a chamber inside another camp's range twice. A delegation arrives to object. *Consequence:* comply and go hungry, or refuse and take a standing hit that pushes the camp toward raiding.

**B09 — The ambitious one.** *Trigger:* any camp's notable has ambition > loyalty. That notable approaches the party privately with an offer. *Consequence:* backing them triggers a succession; refusing means they may act anyway and blame the party.

**B10 — Broker.** *Trigger:* two camps at standing < −40 with each other, both ≥ 20 with the party. Both separately ask the party to help against the other. *Consequence:* the party's first genuine political choice with no correct answer.

**B11 — The gift that shoots back.** *Trigger:* the party has given the Ashfang any tool or weapon, eight or more ticks ago. The Ashfang use it, on someone. *Consequence:* whoever it was used against learns where it came from.

### Ecological beats

**B12 — Empty ground.** *Trigger:* any chamber's prey falls below 12% while a camp depends on it. That camp's delegation, or a raid, arrives somewhere. *Consequence:* migration or war, decided by the simulation, not by us.

**B13 — The dragon thins.** *Trigger:* Dragonspine prey below 25% for ten ticks. The Assayers's god is visibly starving, and they blame the party regardless of cause. *Consequence:* Assayers creed hardens; a faith-break path opens for a camp we'd otherwise never break.

**B14 — Bad water.** *Trigger:* the Cistern is damaged, blocked or seized. Flora regrowth drops across multiple chambers. *Consequence:* the whole map gets hungrier at once. This is the single most destabilising thing the party can do and it should be available early enough to do by accident.

### Faith beats

**B15 — The sign misread.** *Trigger:* Sporewarden faith drops below the break threshold. They do not renounce the prophecy. They conclude the party is a false claimant sent to test them. *Consequence:* zealotry. Foraging suppressed, pursuit prioritised, camp begins to starve.

**B16 — The remnant.** *Trigger:* two to four ticks after B15. A minority splits off, insisting the sign still holds. *Consequence:* a small, weak, permanently loyal faction — and the party's only route back into the Fungal Deep.

---

## 6. Dialogue architecture

Conversations are assembled, not authored line by line, from four inputs.

**Who is speaking** — camp voice, plus whether it's the leader, a notable, or a nobody. Leaders speak for the camp; notables leak their own ambitions.

**Standing** — where the party sits on that camp's scale. This governs tone, not content: the same refusal is delivered as apology, as sneer, or as threat.

**Creed** — how the camp reads the party's actions. Devout camps interpret; opportunists evaluate; rival faiths condemn. Same event, three readings, three lines.

**World state** — what has just happened to them. A camp that lost a raid two ticks ago talks about that, unprompted. This is what makes dialogue feel alive, and it's nearly free because the simulation already knows.

The rule: **every conversation must surface at least one fact the player couldn't have got from looking.** A rumour about a third camp, a grievance, a price, a fear. If a dialogue node is pure flavour, cut it — flavour is what the chronicle is for.

Handwritten dialogue should be structured as fragments with slots, not paragraphs. Roughly two hundred fragments gives thousands of distinct exchanges once creed, standing and world state are combined. Runtime AI generation stays off the critical path; if it's added later it should write *garnish*, never facts, because a hallucinated grievance corrupts the political state the player is reasoning about.

---

## 7. Quests from world state

The simulation is already a quest generator. It knows every one of these without being asked:

- who is hungry, and which chamber they're hungry *for*
- who has a grievance against whom, and how old it is
- which notable is close to moving against their leader
- what technology a camp lacks and has recently seen
- which chamber is collapsing and who depends on it
- who owes whom, including the party

Template against those facts and the quests write themselves. "The Ashfang have run out of arrows" isn't a quest we wrote — it's the tech system reporting a shortfall, wrapped in a request.

**Three rules.**

Quests must be *refusable*, and refusal must be interesting. A quest you can only accept is a corridor.

Quests must have a *cost to somebody else*. If fetching food for the Sporewardens doesn't take it from somewhere, the player is playing a menu.

Quests must be *chainable through the world, not through a script*. Completing one shifts standing and resources, which produces the conditions for the next. Never write quest chains by hand — write the state changes and let the chain fall out.

---

## 8. Endings

All at the Gate. All require the Cistern. None are good.

**Consent.** A camp with control of the Cistern opens the Gate for you because they choose to. Requires high standing and usually that you've made them dominant. You leave; the cavern you leave behind has a winner, and you put them there.

**Purchase.** The Mirelurks open it, for a price you will not enjoy paying. Cleanest exit, worst taste.

**Force.** You take or wreck the Cistern and leave through the resulting chaos. Fast, available to any party, and it kills Deepholt over the following seasons — which the epilogue reports in the same flat register as everything else.

**Inheritance.** You don't leave. You end up running the waterworks, which is precisely what the placard said would happen, four hundred years and one mistranslation ago.

**Nobody leaves.** Starved, hunted, or pursued to the last by a faith you broke. Should be genuinely reachable.

Every ending closes with the chronicle continuing for twenty ticks after the party's exit. The world does not stop when you leave. That last screen is the whole game's argument.

---

## 9. Three playthroughs

Same seed, same starting world, three groups. This is the section to show people.

### Group A — the kind ones
They meet the Sporewardens first and are fed (B01). They reciprocate, hunting for them rather than themselves, which strips the Fungal Deep faster than the Sporewardens ever did alone. Around tick 30 the glowslugs collapse (B12). The Sporewardens starve, and because the party has been *so present*, the collapse is read as judgement. Faith breaks (B15). The gentlest party in the cavern is hunted across the map by the people they fed, while a small remnant (B16) shelters them out of loyalty. They end with Purchase, having sold the remnant's location to the Mirelurks to afford the Gate.

### Group B — the reckless ones
They meet the Ashfang, get shot at (B03), and fight back with a dwarven tool scavenged from the Ember Galleries. Eight ticks later that tool is Ashfang standard issue (B11). The Ashfang, newly armed, take Grimhollow, then the Ashvents' old rivals, then keep going. The party spends the midgame frantically arming everyone else to contain a monster they created. They end with Force, breaking the Cistern to escape an Ashfang hegemony, and the epilogue reports the cavern's slow death by thirst.

### Group C — the careful ones
They avoid all four camps for two hours, living off the unclaimed Grimhollow herd. This is the "correct" play and it goes wrong differently: Grimhollow was the buffer everyone else migrates into during a bad season. When the Black Sump collapses on schedule, the Mirelurks arrive at Grimhollow to find it empty and four peasants living well. B08 fires, then B10, and the most cautious party in the game becomes the centre of a war over a chamber they thought was nobody's. They end with Consent, having backed the Mirelurks, and leave behind a cavern with a trading empire in it.

None of those were written. All three are producible by the systems in this document.

---

## 10. What to write by hand

Ranked by value per hour of writing.

1. **The forty beats.** Highest leverage in the entire project. Each one is a page and produces dozens of situations.
2. **Camp voices.** Four distinct registers, plus the hermit and Ovik. Get these wrong and every generated line sounds the same.
3. **The four gospels.** Four corrupted versions of one maintenance placard. Short, funny, and load-bearing for B06.
4. **The five endings.** Fixed text, world-state epilogues appended.
5. **Dialogue fragments.** Roughly two hundred, slotted. Grind work, do last.

Do not write: a linear plot, scripted quest chains, or scene text that assumes any camp is alive.

---

## Open questions carried forward

- Does the village above know? A rescue clock changes Act III's pressure and gives the camps a much sharper reason to care about the party.
- Are the four peasants pre-written characters or player-made?
- Does the party ever get to tell a camp the truth about the placard — and would any of them believe it?
- What does the Cistern do physically, in enough detail that damaging it has predictable consequences?
