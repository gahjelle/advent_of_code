"""AoC 21, 2015: RPG Simulator 20XX"""

# Standard library imports
import itertools
import pathlib
import sys
from math import ceil
from typing import NamedTuple


class Fighter(NamedTuple):
    hit_points: int
    damage: int
    armor: int


class Item(NamedTuple):
    name: str
    cost: int
    damage: int
    armor: int


WEAPONS = [
    Item("Dagger", cost=8, damage=4, armor=0),
    Item("Shortsword", cost=10, damage=5, armor=0),
    Item("Warhammer", cost=25, damage=6, armor=0),
    Item("Longsword", cost=40, damage=7, armor=0),
    Item("Greataxe", cost=74, damage=8, armor=0),
]
ARMOR = [
    Item("No armor", cost=0, damage=0, armor=0),
    Item("Leather", cost=13, damage=0, armor=1),
    Item("Chainmail", cost=31, damage=0, armor=2),
    Item("Splintmail", cost=53, damage=0, armor=3),
    Item("Bandedmail", cost=75, damage=0, armor=4),
    Item("Platemail", cost=102, damage=0, armor=5),
]
RINGS = [
    Item("No ring 1", cost=0, damage=0, armor=0),
    Item("No ring 2", cost=0, damage=0, armor=0),
    Item("Damage+1", cost=25, damage=1, armor=0),
    Item("Damage+2", cost=50, damage=2, armor=0),
    Item("Damage+3", cost=100, damage=3, armor=0),
    Item("Defense+1", cost=20, damage=0, armor=1),
    Item("Defense+2", cost=40, damage=0, armor=2),
    Item("Defense+3", cost=80, damage=0, armor=3),
]
FIGHTERS = {
    (
        weapon.cost + armor.cost + ring1.cost + ring2.cost,
        weapon.damage + ring1.damage + ring2.damage,
        armor.armor + ring1.armor + ring2.armor,
    )
    for weapon in WEAPONS
    for armor in ARMOR
    for ring1, ring2 in itertools.combinations(RINGS, 2)
}


def parse_data(puzzle_input):
    """Parse input"""
    return Fighter(
        **{
            key.replace(" ", "_").lower(): int(value)
            for key, value in [line.split(": ") for line in puzzle_input.split("\n")]
        }
    )


def part1(data, hit_points=100):
    """Solve part 1"""
    for cost, damage, armor in sorted(FIGHTERS):
        if player_win_fight(Fighter(hit_points, damage, armor), data):
            return cost


def part2(data, hit_points=100):
    """Solve part 2"""
    for cost, damage, armor in sorted(FIGHTERS, reverse=True):
        if not player_win_fight(Fighter(hit_points, damage, armor), data):
            return cost


def player_win_fight(player, boss):
    """Simulate a fight between the player and the boss.

    ## Examples

    >>> player_win_fight(Fighter(6, 1, 0), Fighter(6, 1, 0))
    True
    >>> player_win_fight(Fighter(6, 1, 0), Fighter(7, 1, 0))
    False
    >>> player_win_fight(Fighter(1, 1, 0), Fighter(1, 99, 99))
    True
    >>> player_win_fight(Fighter(1, 11, 11), Fighter(10, 1, 1))
    True
    >>> player_win_fight(Fighter(1, 11, 11), Fighter(11, 1, 1))
    False
    >>> player_win_fight(Fighter(10, 11, 11), Fighter(100, 1, 1))
    True
    >>> player_win_fight(Fighter(10, 11, 11), Fighter(101, 1, 1))
    False
    >>> player_win_fight(Fighter(8, 5, 5), Fighter(12, 7, 2))
    True
    """
    player_hit = max(1, player.damage - boss.armor)
    boss_hit = max(1, boss.damage - player.armor)

    return ceil(player.hit_points / boss_hit) >= ceil(boss.hit_points / player_hit)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
