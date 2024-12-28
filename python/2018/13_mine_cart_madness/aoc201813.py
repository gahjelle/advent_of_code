"""AoC 13, 2018: Mine Cart Madness."""

# Standard library imports
import collections
import itertools
import pathlib
import sys

DIRECTION = {"^": 1j, ">": 1, "v": -1j, "<": -1}
TURN = {"L": 1j, "S": 1, "R": -1j}
CURVE = {
    (1j, "/"): 1,
    (1j, "\\"): -1,
    (1, "/"): 1j,
    (1, "\\"): -1j,
    (-1j, "/"): -1,
    (-1j, "\\"): 1,
    (-1, "/"): -1j,
    (-1, "\\"): 1j,
}


def parse_data(puzzle_input):
    """Parse input."""
    track = {
        col - row * 1j: char
        for row, line in enumerate(puzzle_input.split("\n"))
        for col, char in enumerate(line)
        if char != " "
    }
    return track, [
        (pos, DIRECTION[char]) for pos, char in track.items() if char in DIRECTION
    ]


def part1(data):
    """Solve part 1."""
    track, initial_carts = data
    carts = {
        idx: (pos, dir, itertools.cycle("LSR"))
        for idx, (pos, dir) in enumerate(initial_carts)
    }
    (x, y), _ = next_crash(track, carts)
    return f"{x},{y}"


def part2(data):
    """Solve part 2."""
    track, initial_carts = data
    carts = {
        idx: (pos, dir, itertools.cycle("LSR"))
        for idx, (pos, dir) in enumerate(initial_carts)
    }
    while len(carts) >= 2:
        _, carts = next_crash(track, carts)

    final_pos, _, _ = next(iter(carts.values()), (0, None, None))
    x, y = int(final_pos.real), -int(final_pos.imag)
    return f"{x},{y}"


def next_crash(track, carts):
    """Find the first crash as the carts race around the track.

    Return location of crash and current status of remaining carts.
    """
    while True:
        cart_order = [
            idx
            for *_, idx in sorted(
                (-pos.imag, pos.real, idx) for idx, (pos, _, _) in carts.items()
            )
        ]
        crashes = []
        for cart_id in cart_order:
            if cart_id not in carts:  # Cart has crashed
                continue

            pos, dir, turns = carts[cart_id]
            if track[pos] in r"\/":  # Turn at a curve
                dir = CURVE[dir, track[pos]]
            elif track[pos] == "+":  # Turn at an intersection
                dir *= TURN[next(turns)]
            carts[cart_id] = (pos + dir, dir, turns)

            # Detect crash
            if len({pos for pos, _, _ in carts.values()}) < len(carts):
                crash_pos, _ = collections.Counter(
                    pos for pos, _, _ in carts.values()
                ).most_common()[0]
                crashes.append((int(crash_pos.real), -int(crash_pos.imag)))
                carts = {
                    cart_id: (pos, dir, turns)
                    for cart_id, (pos, dir, turns) in carts.items()
                    if pos != crash_pos
                }

        if crashes:
            return crashes[0], carts


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
