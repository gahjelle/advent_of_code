"""AoC 15, 2018: Beverage Bandits."""

# Standard library imports
import itertools
import pathlib
import sys
import time
from dataclasses import dataclass, replace

# Third party imports
import colorama

colorama.init()

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


@dataclass(order=True)
class Unit:
    health: int
    pos: tuple[int, int]
    team: str
    power: int


def parse_data(puzzle_input):
    """Parse input."""
    grid = {
        (row, col): char
        for row, line in enumerate(puzzle_input.split("\n"))
        for col, char in enumerate(line)
        if char != "#"
    }
    return (
        set(grid),
        {(pos, char) for pos, char in grid.items() if char in "EG"},
    )


def part1(data):
    """Solve part 1."""
    round_num, units = play_battle(*data)
    return round_num * sum(unit.health for unit in units.values())


def part2(data):
    """Solve part 2."""
    grid, initial_pos = data
    num_elfs = sum(team == "E" for _, team in initial_pos)
    for elf_power in itertools.count(start=4):
        round_num, units = play_battle(
            grid, initial_pos, elf_power=elf_power, min_num_elfs=num_elfs
        )
        if {unit.team for unit in units.values()} == {"E"}:
            return round_num * sum(unit.health for unit in units.values())


def play_battle(
    grid, initial_pos, health=200, goblin_power=3, elf_power=3, min_num_elfs=0
):
    """Play one battle with the given goblin and elf attack powers."""
    attack_power = {"G": goblin_power, "E": elf_power}
    units = {
        id: Unit(pos=pos, team=team, health=health, power=attack_power[team])
        for id, (pos, team) in enumerate(initial_pos)
    }
    for round_num in itertools.count(start=0):
        both_alive, units = play_round(grid, units)
        if sum(unit.team == "E" for unit in units.values()) < min_num_elfs:
            return 0, {}
        if not both_alive:
            if "--show" in sys.argv:
                draw_board(grid, units)
            return round_num, units


def play_round(grid, units):
    """Carry out one round of fighting"""
    turn_order = [id for _, id in sorted((unit.pos, id) for id, unit in units.items())]
    for unit_id in turn_order:
        if len({unit.team for unit in units.values()}) == 1:
            return False, units
        units = play_turn(grid, units, unit_id)
    if "--show" in sys.argv:
        draw_board(grid, units)
        time.sleep(0.1)
    return True, units


def play_turn(grid, units, unit_id):
    """Play the turn of one fighter"""
    # Unit already killed earlier in the round
    if unit_id not in units:
        return units

    # Find space to target, adjacent to an enemy
    unit = units[unit_id]
    empty_spaces = grid - {unit.pos for unit in units.values()}
    target_pos = target_enemy(empty_spaces, units, unit.pos, unit.team)
    if target_pos is None:
        return units

    # Move one step towards the target space
    units = units | {
        unit_id: replace(
            unit, pos=make_move(empty_spaces, unit.pos, target_pos) or unit.pos
        )
    }

    # Attack adjacent enemy
    units = attack(units, unit_id)

    # Remove dead units
    return {id: unit for id, unit in units.items() if unit.health > 0}


def target_enemy(grid, units, friend_pos, friend_team):
    """Find an enemy to target."""
    # Already adjacent to enemy: stay in current position
    if any(
        is_adjacent(friend_pos, unit.pos)
        for unit in units.values()
        if unit.team != friend_team
    ):
        return friend_pos

    # Find available target positions: all empty spaces adjacent to enemy
    targets = grid & {
        (unit.pos[0] + drow, unit.pos[1] + dcol)
        for unit in units.values()
        for drow, dcol in DIRECTIONS
        if unit.team != friend_team
    }

    # Find closest available target position
    return bfs(grid, friend_pos, targets)


def make_move(grid, pos, target_pos):
    """Move one step towards the target pos."""
    if pos == target_pos:
        return pos

    next_steps = grid & {(pos[0] + drow, pos[1] + dcol) for drow, dcol in DIRECTIONS}
    return bfs(grid, target_pos, next_steps)


def attack(units, unit_id):
    """Attack all nearby enemies"""
    unit = units[unit_id]
    targets = [
        (enemy, id)
        for id, enemy in units.items()
        if enemy.team != unit.team and is_adjacent(enemy.pos, unit.pos)
    ]
    if not targets:
        return units

    target, target_id = min(targets)
    return units | {target_id: replace(target, health=target.health - unit.power)}


def bfs(grid, start, targets):
    """Run a breadth-first search from start until it reaches one of the targets

    Sort positions in each new layer to prioritize positions based on reading order.
    """
    layer = [start]
    seen = set()
    while layer:
        new_layer = []
        for pos in layer:
            if pos in targets:
                return pos
            if pos in seen:
                continue
            seen.add(pos)
            for drow, dcol in DIRECTIONS:
                new_pos = (pos[0] + drow, pos[1] + dcol)
                if new_pos in grid and new_pos not in seen:
                    new_layer.append(new_pos)
        layer = sorted(new_layer)


def is_adjacent(pos, other_pos):
    """Check if two positions are adjacent"""
    return abs(pos[0] - other_pos[0]) + abs(pos[1] - other_pos[1]) == 1


def draw_board(grid, units):
    """Draw the board to the console"""
    num_rows = max(row for row, _ in grid) + 2
    num_cols = max(col for _, col in grid) + 2
    egs = {unit.pos: unit.team for unit in units.values()}

    board = []
    for row in range(num_rows):
        line = []
        info = []
        for col in range(num_cols):
            line.append("#" if (row, col) not in grid else egs.get((row, col), "."))
            info.extend(
                [
                    f" {unit.team}({unit.health}/{unit.power})"
                    for unit in units.values()
                    if unit.pos == (row, col)
                ]
            )
        board.append("".join(line) + ",".join(info) + " " * 30)

    print(colorama.Cursor.POS(1, 1))
    print("\n".join(board))


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path.startswith("-"):
            continue
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
