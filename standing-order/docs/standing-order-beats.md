# Standing Order — The Beat Library

*Forty authored situations. v0.1.*

---

## How beats work

A beat is a dramatic situation with a **trigger written in simulation terms**. The simulation fires it; nothing is scheduled.

**Four rules, all load-bearing:**

1. **One beat per tick maximum.** If several qualify, take the highest priority; the rest stay eligible.
2. **Once per playthrough** unless marked *repeatable*.
3. **Beats never modify world state.** They present a situation; only the player's response changes anything. A beat that acts on its own is a cutscene.
4. **Every beat needs a no-response path**, because players walk away and that has to be a real outcome.

A playthrough sees roughly a third of these. That's correct — groups should compare notes and find they saw different games.

**Priority** is 1 (highest) to 3. Use it only when several could fire at once.

---

## Contact — meeting the camps

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

## Revelation — learning what's going on

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

## Political — the camps against each other

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

## Ecological — the world eating itself

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

## Faith — the Sporewardens, mostly

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

## Capture — being taken

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

## Tools and technology

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

## Trade and debt

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

## Bands in the field

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

## The Gate

**B40 · The last argument** · *Pri 1*
**Trigger** Party has the means to open the Gate.
**Shape** Every camp with a stake arrives, or sends word. The controlled drain is possible; the fast one is easier.
**Consequence** The ending. And then the chronicle runs twenty ticks past your exit, because the world does not stop when you leave.

---

## Writing budget

Forty beats at roughly a page each is the single highest-value writing in the project — each one produces dozens of distinct situations depending on world state.

**Write them in this order:** contact (B01–B05) → revelation (B06–B09) → bands (B36–B39, because embodiment makes them the most visible) → faith (B21–B25) → political → capture → ecological → tools and trade → B40.

Dialogue fragments stay thin until the beats are proven in play.
