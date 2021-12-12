"""AoC 12, 2021: Passage Pathing"""

# Standard library imports
import collections
import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    caves = collections.defaultdict(list)
    for segment in puzzle_input.split("\n"):
        cave1, _, cave2 = segment.partition("-")
        caves[cave1].append(cave2)
        caves[cave2].append(cave1)

    return caves


def part1(data):
    """Solve part 1"""
    return len(find_paths(data, start="start", end="end"))


def part2(data):
    """Solve part 2"""
    paths = set()
    for extra in data:
        if extra.isupper() or extra == "start" or extra == "end":
            continue
        paths |= find_paths(data, start="start", end="end", extra=extra)
    return len(paths)


def find_paths(caves, start, end, extra=""):
    """Find all paths from start to end"""
    paths = set()
    visit(start, caves, [], end, extra, paths)
    return paths


def visit(
    current: str,
    caves: dict[str, list[str]],
    path: list[str],
    end: str,
    extra: str,
    paths: list[str],
):
    """Visit next cave"""
    if current == end:
        paths.add(",".join(path + [current]))
        return

    for cave in caves[current]:
        cave_extra = extra
        if cave.islower() and cave in path:
            if cave == extra:
                cave_extra = ""
            else:
                continue
        visit(cave, caves, path + [current], end, cave_extra, paths)


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
