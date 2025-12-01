"""AoC 22, 2015: Wizard Simulator 20XX."""

# Standard library imports
import functools
import heapq
import pathlib
import sys
from dataclasses import dataclass, field


@dataclass(order=True)
class Player:
    hit_points: int
    mana: int
    armor: int = 0
    effects: dict[str, int] = field(default_factory=dict, compare=False)


@dataclass(order=True)
class Boss:
    hit_points: int
    damage: int


@dataclass(order=True)
class Attack:
    cost: int
    effect: int
    damage: int
    heal: int
    armor: int
    poison: int
    mana: int


ATTACKS = {
    "missile": Attack(53, effect=0, damage=4, heal=0, armor=0, poison=0, mana=0),
    "drain": Attack(73, effect=0, damage=2, heal=2, armor=0, poison=0, mana=0),
    "shield": Attack(113, effect=6, damage=0, heal=0, armor=7, poison=0, mana=0),
    "poison": Attack(173, effect=6, damage=0, heal=0, armor=0, poison=3, mana=0),
    "recharge": Attack(229, effect=5, damage=0, heal=0, armor=0, poison=0, mana=101),
}


def parse_data(puzzle_input):
    """Parse input."""
    return Boss(
        **{
            key.replace(" ", "_").lower(): int(value)
            for key, value in [line.split(": ") for line in puzzle_input.split("\n")]
        }
    )


def part1(data, hit_points=50, mana=500):
    """Solve part 1."""
    return fight(player=Player(hit_points=hit_points, mana=mana), boss=data)


def part2(data, hit_points=50, mana=500):
    """Solve part 2."""
    return fight(
        player=Player(hit_points=hit_points, mana=mana), boss=data, level_hard=True
    )


def fight(player, boss, level_hard=False):
    """Find the cheapest way for the player to defeat the boss."""
    attacks = [(0, player, boss, [])]
    while True:
        cost, player, boss, names = heapq.heappop(attacks)
        if boss.hit_points <= 0:
            return cost
        if player.hit_points <= 0:
            continue

        for attack_name, attack in ATTACKS.items():
            if attack.cost <= player.mana and player.effects.get(attack_name, 0) <= 1:
                heapq.heappush(
                    attacks,
                    (
                        cost + attack.cost,
                        *do_attacks(player, boss, attack_name, level_hard),
                        names + [attack_name],
                    ),
                )


def do_attacks(player, boss, attack_name, level_hard):
    """Perform one player and one boss attack, including hard level and other
    effects."""
    attacks = ([hard_attack] if level_hard else []) + [
        apply_effects,
        functools.partial(player_attack, attack_name=attack_name),
        apply_effects,
        boss_attack,
    ]
    for attack in attacks:
        player, boss = attack(player, boss)
        if player.hit_points <= 0 or boss.hit_points <= 0:
            break
    return player, boss


def hard_attack(player, boss):
    """Perform a hard attack."""
    return (
        Player(
            hit_points=player.hit_points - 1,
            mana=player.mana,
            armor=player.armor,
            effects=player.effects,
        ),
        boss,
    )


def player_attack(player, boss, attack_name):
    """Perform player attack."""
    attack = ATTACKS[attack_name]
    return Player(
        hit_points=player.hit_points + attack.heal,
        mana=player.mana - attack.cost,
        armor=0,
        effects=(
            player.effects | ({attack_name: attack.effect} if attack.effect else {})
        ),
    ), Boss(hit_points=boss.hit_points - attack.damage, damage=boss.damage)


def boss_attack(player, boss):
    """Perform boss attack."""
    return (
        Player(
            hit_points=player.hit_points - (boss.damage - player.armor),
            mana=player.mana,
            armor=0,
            effects=player.effects,
        ),
        boss,
    )


def apply_effects(player, boss):
    """Apply effects to player and boss."""
    for effect_name in player.effects:
        effect = ATTACKS[effect_name]
        player = Player(
            hit_points=player.hit_points,
            armor=max(player.armor, effect.armor),
            mana=player.mana + effect.mana,
            effects=player.effects,
        )
        boss = Boss(
            hit_points=boss.hit_points - effect.poison,
            damage=boss.damage,
        )
    return (
        Player(
            hit_points=player.hit_points,
            armor=player.armor,
            mana=player.mana,
            effects={
                name: timer - 1 for name, timer in player.effects.items() if timer > 1
            },
        ),
        boss,
    )


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
