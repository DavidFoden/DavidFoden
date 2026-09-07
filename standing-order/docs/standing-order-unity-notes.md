# Standing Order — Unity Notes

*Engine-specific concerns. v0.1. Read with the project setup document.*

None of this changes the design. All of it will cost days if discovered late.

---

## 1. Keeping Core out of Unity, practically

The rule is "Core has no engine references." In Unity that means one specific thing:

**Core lives in its own assembly definition with no Unity references, and is mirrored as a standalone .NET project for CI.** The Unity project references the compiled library; the test runner does not go anywhere near Unity.

If Core is written as ordinary scripts in `Assets/Scripts`, it will acquire a `using UnityEngine` within a fortnight — usually for `Mathf`, `Random` or `Vector2` — and the headless test suite dies quietly.

**Ban list inside Core:** `UnityEngine.*`, `Mathf`, `Vector2/3`, `Random`, `Time`, `Debug`, coroutines, `MonoBehaviour`, `ScriptableObject`. Use `System.Math`, plain structs, the seeded generator, and an injected logger.

`ScriptableObject` is the tempting one for the chamber and camp tables. **Don't.** Keep the static data as plain serialised files that both Core and the editor read. Otherwise the tables are only loadable inside Unity and the headless tests can't run the real world.

---

## 2. Determinism — the good news

Cross-platform floating-point determinism is normally a nightmare in Unity. **We are largely exempt, and it is worth understanding why.**

The architecture is host-authoritative: the host computes every outcome and clients render what they are told. There is no lockstep, no client-side simulation, no replay of inputs. Two machines never need to independently arrive at the same float.

**Where determinism does matter is one machine, twice:** the test suite, the seed survey, and reproducing a bug from a seed. That only requires same-binary reproducibility, which plain C# gives you as long as iteration order is fixed.

**So the rule is narrow:** stable iteration order everywhere, one seeded source, no wall-clock or frame-rate input into Core. Do not spend time on fixed-point arithmetic — it would be solving a problem the architecture already avoids.

**But if lockstep is ever considered**, this exemption disappears entirely. Treat "clients simulate too" as a design change, not an optimisation.

---

## 3. Time

Core has no concept of seconds. The Adapter holds an accumulator, adds `Time.deltaTime` each frame, and calls the tick when 90 seconds have elapsed.

**Never call the tick from `FixedUpdate`.** It is tempting because it sounds like a fixed step, and it will couple the simulation to the physics rate.

Pausing, session end and save all happen on tick boundaries, so the accumulator is also the pause point.

---

## 4. Bands, movement and NavMesh

**The simulation is the authority on where a band is** — chamber, leg, progress along the route. Presentation interpolates a visual position from that.

Do not let a NavMesh agent drive a band's position and report back. The moment presentation drives simulation, LOD invariance breaks: a band in the Present tier walks around a rock and arrives late, while a band in the Far tier does not. Test condition 31 exists to catch this and it will fail.

NavMesh is for the last few metres of local movement inside a chamber — looking natural — not for getting anywhere.

---

## 5. Scenes and streaming

Sixteen chambers with three LOD tiers maps naturally onto **additive scene loading, one scene per chamber**, with the Present tier loaded and the rest unloaded.

Two cautions:

**Audio must not unload with the scene.** Near-tier chambers still emit cues at range, so the Wwise room and its sound sources need a lifetime independent of the visual scene. This is the most likely source of "the war band went silent when I walked away."

**Loading must not stall the tick.** The accumulator keeps counting during a load; make sure a hitch produces one late tick, not a skipped one.

---

## 6. Wwise integration

**Pin the Unity version and the Wwise version together and freeze both.** Wwise integration is version-coupled and upgrading either mid-project is a known time sink.

**Generate rooms and portals from the chamber and tunnel tables** — the hard rule from the master specification. In practice: an editor script that reads the same data file Core reads and creates or updates the Wwise room and portal objects. Never hand-place them, and never let a level designer add a portal that has no tunnel behind it.

Budget real time for the initial integration. It is not a package import; it is a pipeline.

---

## 7. Networking

Only movement is predicted. Everything else is authoritative state pushed on tick boundaries — 90 seconds is enormously generous by netcode standards, so **send full camp state and do not optimise early.**

The genuinely important constraint is not bandwidth, it is **filtering on the host**. Per-player knowledge must be assembled server-side. A client that receives the full chronicle and filters it locally has the information in memory, and packet inspection is not hard.

Transport choice is open. Steam's relay avoids server costs and matches friends-list joining. Whatever is chosen, it should be swappable — wrap it rather than scattering its types through Presentation.

---

## 8. Version control

Unity plus Git needs setting up correctly on day one:

- Force text serialisation and visible meta files
- Git LFS for anything binary — audio and art arrive later but the config should exist first
- A proper Unity `.gitignore` (`Library/`, `Temp/`, `Logs/`, `Build/`)
- Wwise's generated `SoundBanks` are build artefacts, not source

---

## 9. Editor traps

**Disable domain reload at your peril.** Fast enter-play-mode hides static state that would be reset in a build, and this project has a lot of static tables.

**Do not test balance in the editor.** The headless runner is the measurement tool; the editor is for feel. Every balance claim in the documents came from twelve seeds run headless, and that standard should hold.

**Editor-only debug views are worth building early** — the graph with band positions, standing values, faith levels. The player never sees numbers, so the developer needs somewhere that does.

---

## 10. What to set up first, in order

1. Repo, `.gitignore`, LFS, text serialisation
2. Core as a standalone .NET project with the test runner, before Unity exists
3. Unity project referencing it, with the assembly definition boundary enforced
4. CI running the headless tests on push
5. One chamber, first person, in the dark
6. Wwise integration and the generated room graph
7. Everything else

Steps 1–4 are perhaps two days and they are what make every later claim in this project verifiable.
