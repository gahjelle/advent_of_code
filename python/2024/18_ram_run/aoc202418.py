"""AoC 18, 2024: RAM Run."""

# Standard library imports
import collections
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return [
        tuple(int(number) for number in line.split(","))
        for line in puzzle_input.split("\n")
    ]


def part1(data, size=71, wait=1024):
    """Solve part 1."""
    grid = {(x, y): "." for x in range(size) for y in range(size)} | {
        pos: "#" for pos in data[:wait]
    }
    return len(find_path(grid, (0, 0), (size - 1, size - 1)))


def part2(data, size=71, wait=1024):
    """Solve part 2."""
    start, target = (0, 0), (size - 1, size - 1)
    grid = {(x, y): "." for x in range(size) for y in range(size)} | {
        pos: "#" for pos in data[:wait]
    }

    path = find_path(grid, start, target)
    for pos in data[wait:]:
        grid |= {pos: "#"}
        if pos in path:
            path = find_path(grid, start, target)
            if not path:
                return ",".join(str(coord) for coord in pos)


def find_path(grid, start, target):
    """Find a path from start to target"""
    queue = collections.deque([(start, [])])
    seen = set()
    while queue:
        pos, path = queue.popleft()
        if pos == target:
            return path
        if pos in seen:
            continue
        seen.add(pos)

        x, y = pos
        for new_pos in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
            if grid.get(new_pos) != "." or new_pos in seen:
                continue
            queue.append((new_pos, path + [new_pos]))
    return []


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
