"""
cavern_sim.py — headless prototype of the reactive cavern world.

Run 100 ticks, read the log. If the log reads like a history you'd want to
explore, the design works. If it reads like noise, tune WEIGHTS before you
spend an hour on art.

    python cavern_sim.py                    # default run
    python cavern_sim.py --ticks 80 --seed 12
    python cavern_sim.py --no-player        # world with no player interference

Everything you'd want to tune lives in the TUNING block near the top.
"""

import argparse
import random
from dataclasses import dataclass, field

# ---------------------------------------------------------------------------
# TUNING — this is the dial board. Change these, re-run, re-read the log.
# ---------------------------------------------------------------------------

WEIGHTS = {
    # How strongly each need pushes each action's score.
    "hunger_drives_raid": 1.4,
    "hunger_drives_forage": 2.2,
    "weak_neighbour_tempts_raid": 1.6,
    "recent_loss_drives_fortify": 1.8,
    "recent_win_drives_raid": 0.9,      # snowballing dominance comes from this
    "safety_drives_grow": 1.0,
    "curiosity_drives_scout": 0.5,
    # A raid must clear this bar before it's worth the blood. Raise it and the
    # cavern turns cold-war; drop it to zero and everyone dies in seven ticks.
    "raid_reluctance": 0.75,
    "war_weariness": 1.2,
    "loot_tempts_raid": 1.2,      # a fat neighbour is a target   # appetite for another fight right after one
    "hunger_drives_migration": 2.0,   # a stripped chamber pushes a camp to move
}

NOISE = 0.35        # randomness added to every score. 0 = robotic, 1 = chaotic.
FOOD_PER_POP = 0.7  # each pop eats this much per tick
RAID_LOOT = 0.45    # share of the loser's food the winner takes
CASUALTY_RATE = (0.08, 0.18)   # share of the loser's pop killed in a raid
START_TICK_FOR_PLAYER_EVENT = 18   # when the player knocks the wall through


# ---------------------------------------------------------------------------
# WORLD MODEL
# ---------------------------------------------------------------------------

@dataclass
class Chamber:
    """A node in the cavern. Camps sit in chambers; tunnels connect them."""
    key: str
    name: str
    food_yield: float          # max harvested per tick
    defensible: float          # 0..1, how much it favours the defender
    stock: float = 0.0         # what's actually left to harvest right now
    regen: float = 0.0         # how fast it recovers

    def __post_init__(self):
        # A chamber starts full and regrows a fraction of its yield each tick.
        self.stock = self.food_yield * 4
        self.regen = self.food_yield * 0.8


@dataclass
class Camp:
    key: str
    name: str
    home: str                  # chamber key
    pop: float
    food: float
    defence: float
    temperament: float         # 0 = cautious, 1 = belligerent (personality)
    # short-term memory — this is what makes them feel reactive
    last_result: str = "none"  # "won" | "lost" | "none"
    ticks_since_fight: int = 99
    known: set = field(default_factory=set)   # chambers it has scouted
    alive: bool = True

    @property
    def strength(self) -> float:
        return self.pop * (1.0 + self.defence)


class World:
    def __init__(self, seed: int):
        self.rng = random.Random(seed)
        self.tick_no = 0
        self.log: list[str] = []

        self.chambers = {c.key: c for c in [
            Chamber("hollow",  "Grimhollow",       food_yield=7.0, defensible=0.5),
            Chamber("ashvent", "The Ashvents",     food_yield=4.0, defensible=0.2),
            Chamber("fungal",  "The Fungal Deep",  food_yield=11.0, defensible=0.1),
            Chamber("spine",   "Dragonspine Ridge", food_yield=2.0, defensible=0.8),
            Chamber("sump",    "The Black Sump",   food_yield=5.0, defensible=0.3),
            Chamber("gate",    "The Sealed Gate",  food_yield=1.0, defensible=0.6),
        ]}

        # Tunnels. The player will later punch a new one through.
        self.tunnels = {
            frozenset(("hollow", "ashvent")),
            frozenset(("ashvent", "fungal")),
            frozenset(("fungal", "sump")),
            frozenset(("spine", "sump")),
            frozenset(("spine", "gate")),
        }

        self.camps = {c.key: c for c in [
            Camp("ashfang", "the Ashfang goblins", "ashvent",
                 pop=12, food=14, defence=0.2, temperament=0.8),
            Camp("mire",    "the Mirelurk clan",   "sump",
                 pop=9,  food=20, defence=0.4, temperament=0.3),
            Camp("spore",   "the Sporewardens",    "fungal",
                 pop=15, food=26, defence=0.1, temperament=0.2),
            Camp("wyrm",    "the Wyrmcult",        "spine",
                 pop=6,  food=8,  defence=0.7, temperament=0.6),
        ]}

        for camp in self.camps.values():
            camp.known.add(camp.home)

    # -- helpers ------------------------------------------------------------

    def neighbours(self, chamber_key: str) -> list[str]:
        out = []
        for t in self.tunnels:
            if chamber_key in t:
                out.append(next(k for k in t if k != chamber_key))
        return sorted(out)

    def camp_at(self, chamber_key: str):
        for c in self.camps.values():
            if c.alive and c.home == chamber_key:
                return c
        return None

    def living(self) -> list[Camp]:
        return [c for c in self.camps.values() if c.alive]

    def say(self, text: str):
        self.log.append(f"[{self.tick_no:>3}] {text}")

    def open_passage(self, a: str, b: str):
        """The player's tool. All it does is edit the map — the camps do the rest."""
        self.tunnels.add(frozenset((a, b)))
        self.say(f"** The party breaks through the wall between "
                 f"{self.chambers[a].name} and {self.chambers[b].name}. **")

    # -- 1. SENSE -----------------------------------------------------------

    def sense(self, camp: Camp) -> dict:
        upkeep = camp.pop * FOOD_PER_POP
        adjacent = self.neighbours(camp.home)
        rivals = [self.camp_at(k) for k in adjacent]
        rivals = [r for r in rivals if r is not None]
        depleted = 1.0 - (self.chambers[camp.home].stock
                          / max(1.0, self.chambers[camp.home].food_yield * 4))
        return {
            # hungry, or sitting on a stripped-out chamber — both push outward
            "hunger": min(1.0, max(0.0, (upkeep * 3 - camp.food) / (upkeep * 3))
                          + depleted * 0.5),
            "safety": 1.0 if not rivals else 0.4,
            "rivals": rivals,
            "unexplored": [k for k in adjacent if k not in camp.known],
            # empty adjacent chambers this camp knows about, best larder first
            "larder": min(1.0, self.chambers[camp.home].stock
                          / max(1.0, self.chambers[camp.home].food_yield)),
            "open_ground": sorted(
                [k for k in adjacent
                 if k in camp.known and self.camp_at(k) is None],
                key=lambda k: -self.chambers[k].stock),
        }

    # -- 2. SCORE -----------------------------------------------------------

    def score(self, camp: Camp, s: dict) -> dict:
        w = WEIGHTS
        scores = {
            "grow":    w["safety_drives_grow"] * s["safety"] * (1.0 if camp.food > camp.pop * 1.4 else 0.0),
            # Score the expected RETURN, not just the need. A stripped chamber
            # makes foraging worthless, which is what lets raiding win.
            "forage":  0.2 + w["hunger_drives_forage"] * s["hunger"] * s["larder"],
            "fortify": 0.3,
            "scout":   w["curiosity_drives_scout"] * bool(s["unexplored"]),
        }

        if camp.last_result == "lost" and camp.ticks_since_fight < 4:
            scores["fortify"] += w["recent_loss_drives_fortify"]

        # Move house — the single most important action for a living world.
        here = self.chambers[camp.home]
        for target_key in s["open_ground"][:2]:
            there = self.chambers[target_key]
            better = (there.stock - here.stock) / max(4.0, here.food_yield * 4)
            scores[f"migrate:{target_key}"] = (
                w["hunger_drives_migration"] * s["hunger"] * better - 0.3)

        # One raid option per adjacent rival, scored separately.
        for rival in s["rivals"]:
            weakness = camp.strength / max(0.5, camp.strength + rival.strength)
            v = (w["hunger_drives_raid"] * s["hunger"]
                 + w["weak_neighbour_tempts_raid"] * (weakness - 0.5) * 2
                 + camp.temperament * 0.6
                 + w["loot_tempts_raid"] * min(1.0, rival.food
                                               / max(4.0, camp.pop * 2))
                 - w["raid_reluctance"])
            if camp.last_result == "won" and camp.ticks_since_fight < 4:
                v += w["recent_win_drives_raid"]
            if camp.ticks_since_fight < 3:
                v -= w["war_weariness"]   # nobody fights three ticks running
            scores[f"raid:{rival.key}"] = v

        # Noise so it never feels like a spreadsheet.
        for k in scores:
            scores[k] += self.rng.uniform(-NOISE, NOISE)
        return scores

    # -- 3. PICK ------------------------------------------------------------

    def pick(self, scores: dict) -> str:
        return max(scores, key=scores.get)

    # -- 4. RESOLVE ---------------------------------------------------------

    def resolve(self, intents: dict):
        resolved_fights = set()

        for camp_key, action in intents.items():
            camp = self.camps[camp_key]
            if not camp.alive:
                continue

            if action == "grow":
                camp.pop += 1
                camp.food -= 2
                self.say(f"{camp.name} swell in number.")

            elif action == "forage":
                ch = self.chambers[camp.home]
                gain = min(ch.stock, ch.food_yield)
                ch.stock -= gain
                camp.food += gain
                if gain < ch.food_yield * 0.4:
                    self.say(f"{camp.name} scrape {ch.name} bare.")
                else:
                    self.say(f"{camp.name} forage {ch.name}.")

            elif action == "fortify":
                camp.defence = min(1.2, camp.defence + 0.15)
                self.say(f"{camp.name} shore up their defences.")

            elif action == "scout":
                s = self.sense(camp)
                if s["unexplored"]:
                    target = self.rng.choice(s["unexplored"])
                    camp.known.add(target)
                    self.say(f"{camp.name} scout {self.chambers[target].name}.")

            elif action.startswith("migrate:"):
                target_key = action.split(":", 1)[1]
                if self.camp_at(target_key) is None:
                    old = self.chambers[camp.home].name
                    camp.home = target_key
                    camp.known.add(target_key)
                    camp.defence = max(0.0, camp.defence - 0.2)  # unfamiliar ground
                    self.say(f"{camp.name} abandon {old} and settle "
                             f"{self.chambers[target_key].name}.")

            elif action.startswith("raid:"):
                target_key = action.split(":", 1)[1]
                pair = frozenset((camp_key, target_key))
                if pair in resolved_fights:
                    continue
                resolved_fights.add(pair)
                self.battle(camp, self.camps[target_key])

        # Chambers recover a little each tick.
        for ch in self.chambers.values():
            ch.stock = min(ch.food_yield * 4, ch.stock + ch.regen)

        # Upkeep: everyone eats.
        for camp in self.living():
            camp.food -= camp.pop * FOOD_PER_POP
            if camp.food < 0:
                lost = min(camp.pop, 1 + abs(camp.food) / 4)
                camp.pop -= lost
                camp.food = 0
                self.say(f"{camp.name} go hungry and lose {lost:.0f}.")
            if camp.pop < 1:
                camp.alive = False
                self.say(f"** {camp.name} are no more. **")

    def battle(self, attacker: Camp, defender: Camp):
        home_bonus = 1.0 + self.chambers[defender.home].defensible
        a = attacker.strength * self.rng.uniform(0.8, 1.2)
        d = defender.strength * home_bonus * self.rng.uniform(0.8, 1.2)

        winner, loser = (attacker, defender) if a > d else (defender, attacker)
        losses = max(1.0, loser.pop * self.rng.uniform(*CASUALTY_RATE))
        loser.pop -= losses
        winner.pop -= max(0.3, losses * 0.4)

        loot = loser.food * RAID_LOOT
        loser.food -= loot
        winner.food += loot

        # -- 5. PROPAGATE: memory is what makes next tick different ---------
        winner.last_result, loser.last_result = "won", "lost"
        winner.ticks_since_fight = loser.ticks_since_fight = 0
        loser.defence = max(0.0, loser.defence - 0.1)

        self.say(f"{attacker.name} raid {defender.name} at "
                 f"{self.chambers[defender.home].name} — "
                 f"{winner.name} take the field.")

        if loser.pop < 1:
            loser.alive = False
            self.say(f"** {loser.name} are wiped out; "
                     f"{self.chambers[loser.home].name} falls silent. **")

    # -- the heartbeat ------------------------------------------------------

    def step(self):
        self.tick_no += 1
        intents = {}
        for camp in self.living():
            camp.ticks_since_fight += 1
            s = self.sense(camp)
            intents[camp.key] = self.pick(self.score(camp, s))
        self.resolve(intents)

    def summary(self) -> str:
        lines = ["", "--- state of the cavern ---"]
        for c in sorted(self.camps.values(), key=lambda c: -c.pop):
            if c.alive:
                lines.append(f"  {c.name:<24} pop {c.pop:>5.1f}  "
                             f"food {c.food:>6.1f}  def {c.defence:.2f}  "
                             f"at {self.chambers[c.home].name}")
            else:
                lines.append(f"  {c.name:<24} destroyed")
        return "\n".join(lines)


# ---------------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--ticks", type=int, default=60)
    p.add_argument("--seed", type=int, default=7)
    p.add_argument("--no-player", action="store_true",
                   help="run the world with no player interference, for comparison")
    args = p.parse_args()

    world = World(args.seed)
    for _ in range(args.ticks):
        if (not args.no_player) and world.tick_no == START_TICK_FOR_PLAYER_EVENT:
            # The single player action in this prototype: open a new tunnel
            # from the Sealed Gate into the Fungal Deep. Watch what it does.
            world.open_passage("gate", "fungal")
        world.step()

    print("\n".join(world.log))
    print(world.summary())


if __name__ == "__main__":
    main()
