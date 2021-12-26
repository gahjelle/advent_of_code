"""AoC 23, 2021: Amphipod"""

from __future__ import annotations

# Standard library imports
import heapq
import pathlib
import sys
from dataclasses import dataclass, field
from typing import ClassVar, NamedTuple

ENERGIES = {"A": 1, "B": 10, "C": 100, "D": 1000}


def parse(puzzle_input):
    """Parse input"""
    return (
        puzzle_input.replace("#", "").replace(".", "").replace(" ", "").strip().split()
    )


def part1(data):
    """Solve part 1"""
    return move_to_target(*generate_burrow(data))


def part2(data):
    """Solve part 2"""
    lines = [data[0], "DCBA", "DBAC", data[1]]
    return move_to_target(*generate_burrow(lines))


class Neighbor(NamedTuple):
    id: int
    distance: int
    blocked_by: list[int]


class Room(NamedTuple):
    target: str
    neighbors: list[Neighbor]
    related: list[int] = []


def generate_burrow(amphipods):
    """Generate the layout of the burrow with the given start positions

    #############
    #.. . . . ..#
    ###B#C#B#D###
      #A#D#C#A#
      #########

    >>> layout, positions = generate_burrow(["BCBD", "ADCA"])
    >>> positions
    '.......BCBDADCA'
    """
    num_rows = len(amphipods)
    layout = {}
    positions = {}

    # Amphipod rooms
    for row, line in enumerate(amphipods):
        for col, (amphipod, target) in enumerate(zip(line, "ABCD")):
            room_id = 7 + row * 4 + col
            positions[room_id] = amphipod
            layout[room_id] = Room(
                target,
                get_hallway(row, col),
                [7 + pos * 4 + col for pos in range(num_rows)],
            )

    # Hallway
    layout[0] = Room(
        ".",
        get_rooms(
            num_rows,
            [
                (3, [1]),
                (5, [1, 2]),
                (7, [1, 2, 3]),
                (9, [1, 2, 3, 4]),
            ],
        ),
    )
    layout[1] = Room(
        ".",
        get_rooms(num_rows, [(2, []), (4, [2]), (6, [2, 3]), (8, [2, 3, 4])]),
    )
    layout[2] = Room(
        ".", get_rooms(num_rows, [(2, []), (2, []), (4, [3]), (6, [3, 4])])
    )
    layout[3] = Room(".", get_rooms(num_rows, [(4, [2]), (2, []), (2, []), (4, [4])]))
    layout[4] = Room(
        ".", get_rooms(num_rows, [(6, [2, 3]), (4, [3]), (2, []), (2, [])])
    )
    layout[5] = Room(
        ".",
        get_rooms(num_rows, [(8, [2, 3, 4]), (6, [3, 4]), (4, [4]), (2, [])]),
    )
    layout[6] = Room(
        ".",
        get_rooms(
            num_rows,
            [
                (9, [2, 3, 4, 5]),
                (7, [3, 4, 5]),
                (5, [4, 5]),
                (3, [5]),
            ],
        ),
    )

    return layout, "".join(
        positions.get(idx) or "." for idx in range(max(positions) + 1)
    )


def get_hallway(row, col):
    """Set up hallway neighbors"""
    blocking_rooms = [7 + 4 * pos + col for pos in range(row)]
    match col:
        case 0:
            return [
                Neighbor(1, 2 + row, blocking_rooms),
                Neighbor(2, 2 + row, blocking_rooms),
                Neighbor(0, 3 + row, [1] + blocking_rooms),
                Neighbor(3, 4 + row, [2] + blocking_rooms),
                Neighbor(4, 6 + row, [2, 3] + blocking_rooms),
                Neighbor(5, 8 + row, [2, 3, 4] + blocking_rooms),
                Neighbor(6, 9 + row, [2, 3, 4, 5] + blocking_rooms),
            ]
        case 1:
            return [
                Neighbor(2, 2 + row, blocking_rooms),
                Neighbor(3, 2 + row, blocking_rooms),
                Neighbor(1, 4 + row, [2] + blocking_rooms),
                Neighbor(4, 4 + row, [3] + blocking_rooms),
                Neighbor(0, 5 + row, [1, 2] + blocking_rooms),
                Neighbor(5, 6 + row, [3, 4] + blocking_rooms),
                Neighbor(6, 7 + row, [3, 4, 5] + blocking_rooms),
            ]
        case 2:
            return [
                Neighbor(3, 2 + row, blocking_rooms),
                Neighbor(4, 2 + row, blocking_rooms),
                Neighbor(2, 4 + row, [3] + blocking_rooms),
                Neighbor(5, 4 + row, [4] + blocking_rooms),
                Neighbor(6, 5 + row, [4, 5] + blocking_rooms),
                Neighbor(1, 6 + row, [2, 3] + blocking_rooms),
                Neighbor(0, 7 + row, [1, 2, 3] + blocking_rooms),
            ]
        case 3:
            return [
                Neighbor(4, 2 + row, blocking_rooms),
                Neighbor(5, 2 + row, blocking_rooms),
                Neighbor(6, 3 + row, [5] + blocking_rooms),
                Neighbor(3, 4 + row, [4] + blocking_rooms),
                Neighbor(2, 6 + row, [3, 4] + blocking_rooms),
                Neighbor(1, 8 + row, [2, 3, 4] + blocking_rooms),
                Neighbor(0, 9 + row, [1, 2, 3, 4] + blocking_rooms),
            ]


def get_rooms(num_rows, hallway):
    """Set up room neighbors"""
    neighbors = []
    for col, (distance, blocked_by) in enumerate(hallway):
        room_blockers = []
        for row in range(num_rows):
            room_id = 7 + row * 4 + col
            neighbors.append(
                Neighbor(room_id, distance + row, blocked_by + room_blockers)
            )
            room_blockers.append(room_id)

    return sorted(neighbors, key=lambda nb: nb.distance)


def all_at_target(layout, positions):
    """Check if all amphipods are at their target locations"""
    return all(
        layout[position].target == amphipod
        for position, amphipod in enumerate(positions)
    )


def move_to_target(layout, positions):
    """Move amphipods to their target spaces"""
    moves = []
    current_cost = 0
    handled = set()
    while not all_at_target(layout, positions):
        for cost, move in possible_moves(layout, positions):
            heapq.heappush(moves, (current_cost + cost, move))

        handled.add(positions)
        while positions in handled:
            current_cost, positions = heapq.heappop(moves)

    return current_cost


def possible_moves(layout, positions, energies=ENERGIES):
    """List possible next moves from a given game state"""
    for position, amphipod in enumerate(positions):
        target, neighbors, related = layout[position]
        if amphipod == ".":
            continue  # No amphipod to move
        if target == amphipod and all(
            positions[pos] in {".", amphipod} for pos in related
        ):
            continue  # The amphipod is where it should be

        for to_pos, distance, blocked_by in neighbors:
            to_target = layout[to_pos].target
            if to_target != "." and amphipod != to_target:
                continue  # Amphipod is not allowed to move here
            if positions[to_pos] != ".":
                continue  # Position is occupied
            if any(positions[pos] != "." for pos in blocked_by):
                continue  # Path is blocked
            if any(
                positions[pos] not in {".", amphipod} for pos in layout[to_pos].related
            ):
                continue  # Strangers are still present in column
            if any(
                positions[pos] != amphipod
                for pos in layout[to_pos].related
                if pos > to_pos
            ):
                continue  # Make sure to fill column from bottom

            # Construct new position string
            if to_pos < position:
                i1, p1, i2, p2 = to_pos, amphipod, position, "."
            else:
                i1, p1, i2, p2 = position, ".", to_pos, amphipod
            new_positions = (
                positions[:i1] + p1 + positions[i1 + 1 : i2] + p2 + positions[i2 + 1 :]
            )

            yield distance * energies[amphipod], new_positions


def show_burrow(layout, positions):
    """Print out the current burrow"""
    p = {k: "." if not (a := positions.get(k)) else a for k in layout.keys()}
    print(f"{p[0]}{p[1]}.{p[2]}.{p[3]}.{p[4]}.{p[5]}{p[6]}")
    for idx in range(7, 23, 4):
        if idx not in p:
            continue
        print(f"  {p[idx]} {p[idx + 1]} {p[idx + 2]} {p[idx + 3]}  ")


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
