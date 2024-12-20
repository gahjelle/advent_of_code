"""AoC 20, 2024: Race Condition."""

# Standard library imports
import collections
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    grid = {
        (row, col): char
        for row, line in enumerate(puzzle_input.split("\n"))
        for col, char in enumerate(line)
    }
    start = next(pos for pos, char in grid.items() if char == "S")
    target = next(pos for pos, char in grid.items() if char == "E")
    return walk(grid, start, target)


def part1(path, min_cheat_save=100):
    """Solve part 1."""
    return find_short_cheats(path, min_cheat_save)


def part2(path, min_cheat_save=100):
    """Solve part 2."""
    return find_long_cheats(path, min_cheat_save, max_dist=20)


def walk(grid, start, target):
    """Find the path from start to target in the grid"""
    queue = collections.deque([(start, [start])])
    seen = set()
    while queue:
        pos, path = queue.popleft()
        if pos == target:
            return path
        if pos in seen:
            continue
        seen.add(pos)

        row, col = pos
        for new_pos in [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]:
            if grid.get(new_pos, "#") != "#" and new_pos not in seen:
                queue.append((new_pos, path + [new_pos]))
    return []


def find_short_cheats(path, min_save):
    """Find the number of cheats walking through a single wall (2 steps)"""
    positions = {pos: time for time, pos in enumerate(path)}
    num_cheats = 0
    for (row, col), time in positions.items():
        for cheat in [(row - 2, col), (row, col + 2), (row + 2, col), (row, col - 2)]:
            if positions.get(cheat, 0) - time - 2 >= min_save:
                num_cheats += 1
    return num_cheats


def find_long_cheats(path, min_save, max_dist=20):
    """Find the number of cheats within the given distance"""
    num_cheats = 0
    for time, pos in enumerate(path):
        for cheat_time, cheat_pos in enumerate(
            path[time + min_save :], start=time + min_save
        ):
            dist = abs(cheat_pos[0] - pos[0]) + abs(cheat_pos[1] - pos[1])
            if dist <= max_dist and cheat_time - time - dist >= min_save:
                num_cheats += 1
    return num_cheats


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
