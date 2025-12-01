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


def walk(grid, start, target):
    """Find the path from start to target in the grid"""
    queue = collections.deque([(start, 0, {start: 0})])
    seen = set()
    while queue:
        pos, step, path = queue.popleft()
        if pos == target:
            return path
        if pos in seen:
            continue
        seen.add(pos)

        row, col = pos
        for new_pos in [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]:
            if grid.get(new_pos, "#") != "#" and new_pos not in seen:
                queue.append((new_pos, step + 1, path | {new_pos: step + 1}))
    return []


def part1(path, min_cheat_save=100):
    """Solve part 1."""
    return find_short_cheats(path, min_cheat_save)


def part2(path, min_cheat_save=100):
    """Solve part 2."""
    return find_long_cheats(path, min_cheat_save, max_dist=20)


def find_short_cheats(path, min_save):
    """Find the number of cheats walking through a single wall (2 steps)"""
    num_cheats = 0
    for (row, col), time in path.items():
        for cheat in [(row - 2, col), (row, col + 2), (row + 2, col), (row, col - 2)]:
            if path.get(cheat, 0) - time - 2 >= min_save:
                num_cheats += 1
    return num_cheats


def find_long_cheats(path, min_save, max_dist=20):
    """Find the number of cheats within the given distance"""
    cheats = set()
    for (row, col), time in path.items():
        for r in range(max_dist + 1):
            for c in range(max_dist - r + 1):
                for cheat in [
                    (row - r, col - c),
                    (row + r, col - c),
                    (row - r, col + c),
                    (row + r, col + c),
                ]:
                    if path.get(cheat, 0) - time - (r + c) >= min_save:
                        cheats.add(((row, col), cheat))
    return len(cheats)


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
