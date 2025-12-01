"""AoC 22, 2023: Sand Slabs."""

# Standard library imports
import collections
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    settled = settle([parse_brick(line) for line in puzzle_input.split("\n")])
    return len(settled), *is_supporting(settled)


def parse_brick(line):
    """Parse one brick into cubes.

    ## Example:

    >>> parse_brick("1,2,3~3,2,3")
    [(1, 2, 3), (2, 2, 3), (3, 2, 3)]
    """
    first, _, last = line.partition("~")
    xf, yf, zf = tuple(int(pos) for pos in first.split(","))
    xl, yl, zl = tuple(int(pos) for pos in last.split(","))

    if xf != xl:
        return [(p, yf, zf) for p in range(xf, xl + 1)]
    elif yf != yl:
        return [(xf, p, zf) for p in range(yf, yl + 1)]
    elif zf != zl:
        return [(xf, yf, p) for p in range(zf, zl + 1)]
    else:
        return [(xf, yf, zf)]


def part1(data):
    """Solve part 1."""
    num_bricks, supports, is_supported = data
    return sum(
        all(len(is_supported[j]) >= 2 for j in supports[i]) for i in range(num_bricks)
    )


def part2(data):
    """Solve part 2."""
    num_bricks, supports, is_supported = data

    total = 0
    for i in range(num_bricks):
        queue = collections.deque(j for j in supports[i] if len(is_supported[j]) == 1)
        falling = set(queue)
        falling.add(i)

        while queue:
            j = queue.popleft()
            for k in supports[j] - falling:
                if is_supported[k] <= falling:
                    queue.append(k)
                    falling.add(k)
        total += len(falling) - 1
    return total


def settle(bricks):
    """Let bricks fall to the ground to settle.

    ## Example

    >>> bricks = [[(2, 2, 1)], [(2, 2, 2)], [(1, 1, 3)]]
    >>> settle(bricks)
    [[(2, 2, 1)], [(2, 2, 2)], [(1, 1, 1)]]
    """
    levels = collections.defaultdict(set)
    settled = []

    def fits(brick, offset=0):
        for x, y, z in brick:
            if (x, y) in levels[z - offset]:
                return False
        return True

    def fit(brick, offset=0):
        for x, y, z in brick:
            levels[z - offset].add((x, y))
        return [(x, y, z - offset) for x, y, z in brick]

    for brick in sorted(bricks, key=lambda xyzs: min(z for _, _, z in xyzs)):
        level = min(z for _, _, z in brick)
        if level == 1:
            settled.append(fit(brick))
        else:
            for offset in range(1, level):
                if not fits(brick, offset):
                    settled.append(fit(brick, offset - 1))
                    break
            else:
                settled.append(fit(brick, level - 1))
    return settled


def is_supporting(bricks):
    """Identify supporting bricks."""
    supports = collections.defaultdict(set)
    is_supported = collections.defaultdict(set)
    for idx_b, brick in enumerate(bricks):
        for idx_s, support in enumerate(bricks):
            if idx_b == idx_s:
                continue
            for x, y, z in brick:
                if any(x == xs and y == ys and z + 1 == zs for xs, ys, zs in support):
                    supports[idx_b].add(idx_s)
                    is_supported[idx_s].add(idx_b)
    return supports, is_supported


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
