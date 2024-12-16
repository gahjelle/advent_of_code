"""AoC 16, 2024: Reindeer Maze."""

# Standard library imports
import heapq
import pathlib
import sys

INFTY = 999_999_999
NORTH, EAST, SOUTH, WEST = (-1, 0), (0, 1), (1, 0), (0, -1)
TURNS = {
    (row, col): [(1, (row, col)), (1001, (col, row)), (1001, (-col, -row))]
    for row, col in [NORTH, EAST, SOUTH, WEST]
}


def parse_data(puzzle_input):
    """Parse input."""
    grid = {
        (row, col): char
        for row, line in enumerate(puzzle_input.split("\n"))
        for col, char in enumerate(line)
        if char != "#"
    }
    start = next(pos for pos, char in grid.items() if char == "S")
    target = next(pos for pos, char in grid.items() if char == "E")
    return grid, start, target


def part1(data):
    """Solve part 1."""
    return find_target(*data)


def part2(data):
    """Solve part 2."""
    return find_paths(*data)


def find_target(grid, start, target):
    """Find the lowest cost for getting to the target"""
    queue = [(0, start, EAST)]
    seen = set()
    while queue:
        cost, pos, dir = heapq.heappop(queue)
        if pos == target:
            return cost
        if pos in seen:
            continue
        seen.add(pos)

        for dcost, new_dir in TURNS[dir]:
            new_pos = (pos[0] + new_dir[0], pos[1] + new_dir[1])
            if new_pos in grid and new_pos not in seen:
                heapq.heappush(queue, (cost + dcost, new_pos, new_dir))


def find_paths(grid, start, target):
    """Find all paths to the target that have the lowest cost"""
    queue = [(0, start, EAST, [start])]
    best = {}
    locs_in_paths = set()
    target_cost = None
    while queue:
        cost, pos, dir, path = heapq.heappop(queue)
        if cost > best.get((pos, dir), INFTY):
            continue
        if target_cost and cost > target_cost:
            break
        best[(pos, dir)] = cost
        if pos == target:
            locs_in_paths |= set(path)
            target_cost = cost
            continue

        for dcost, new_dir in TURNS[dir]:
            new_pos = (pos[0] + new_dir[0], pos[1] + new_dir[1])
            if new_pos in grid and cost + dcost <= best.get((new_pos, new_dir), INFTY):
                heapq.heappush(
                    queue, (cost + dcost, new_pos, new_dir, path + [new_pos])
                )
    return len(locs_in_paths)


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
