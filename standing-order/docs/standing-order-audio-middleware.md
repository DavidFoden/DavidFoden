# Standing Order — Audio Middleware Research

*Decision note, September 2026. Verify licensing terms directly before signing anything — they change.*

---

## Why this decision is unusual for us

In most games audio is presentation. In this one **audio carries world state**: direction and distance of a war band, whether a chamber's herd is alive, what a camp is doing three rooms away. The production notes already put audio ahead of art for that reason.

That moves us across the line the industry generally draws. The practical boundary for adopting middleware is <cite index="12-1">whether a game can keep treating audio as clips triggered by code, or whether audio behaviour must become independently authored data that designers can edit, package, profile and validate</cite>. Ours must, because the mix is a gameplay system — the absence of a life bed is a signal, and that has to survive every mixing decision.

## The decisive finding

Our world model **is already a rooms-and-portals graph.** Sixteen chambers, twenty-five tunnels, with occlusion defined as attenuation per tunnel traversed rather than by raycast.

That is precisely the topology Wwise's spatial audio system is built around. The relevant guidance is blunt about where it wins: <cite index="14-1">for horror, stealth or VR games where sound propagation through the environment is a gameplay mechanic, Wwise's room and portal system is unmatched</cite>. That sentence describes this game almost exactly.

The usual objection doesn't apply to us either. <cite index="14-1">The big variable cost of Wwise spatial audio is that rooms, portals and diffraction scale with scene geometry complexity</cite> — but our scene is sixteen rooms and twenty-five portals, hand-authored, and it never grows.

## Licensing

Both have workable indie terms.

**Wwise.** <cite index="1-1">A free Indie licence is available for projects under $250K total production budget, with full platform access and no sound asset limit; only the bare trial path retains the 200-asset cap</cite>. Comfortably inside our budget.

**FMOD.** Budget and revenue-tiered per-title licensing, <cite index="3-1">free under the relevant thresholds</cite>.

Neither costs money at our scale. Cost is not the deciding factor.

## The honest case against Wwise

<cite index="3-1">FMOD is generally considered friendlier to learn and lighter for small teams, while Wwise scales deeper and is the larger AAA standard; for a first middleware project on a small team FMOD is the common recommendation, and teams with a dedicated audio person or complex adaptive ambitions often justify Wwise</cite>.

You are a solo developer with no audio specialist, working one day a week. That is textbook FMOD territory.

**But the thing we need is the specific thing FMOD would make us build ourselves.** Choosing FMOD means hand-rolling portal-based propagation — the exact system Wwise ships. Trading a steeper tool for less bespoke code is the right trade when the bespoke code is load-bearing gameplay.

## Recommendation

**Wwise, provisionally** — with a one-day test before committing, because <cite index="3-1">both decisions are reversible early and painful late</cite>.

## The test to run

<cite index="3-1">Prototype your most complex audio scenario in both free tiers for a day each; the tool that lets your team iterate fastest wins, and you will know within hours</cite>.

Our most complex scenario is already written as a test condition:

> **A war band two chambers away is audible and directionally identifiable by a blindfolded tester.**

Build exactly that in both. Three rooms in a line, two portals, one moving sound source, a listener in the far room. Nothing else. The question is how much work it takes to make the direction readable through two closed portals — and whether closing one portal produces the silence we need.

Add a second check that matters as much: **can a life bed be removed from one room and the absence be obvious** without ambience rushing in to fill it.

## The risk to design out now

**Two sources of truth.** Wwise rooms are usually authored from scene geometry. Ours must be authored from the **same chamber and tunnel data the simulation uses** — ideally generated from it, never hand-placed independently.

If a level designer moves a wall and the audio graph no longer matches the simulation graph, a player will hear a war band through a tunnel that does not exist. The tunnel graph is the authority; audio geometry is downstream of it.

That constraint belongs in the project setup document as a hard rule, and it is a good reason to generate the Wwise room and portal layout from the chamber tables rather than build it by hand.

## What this does not decide

Unity's built-in audio remains viable for everything that is *not* propagation — UI, foley, music cues. Middleware is being adopted for one reason, and it should not be allowed to swallow the whole audio pipeline just because it is there.
