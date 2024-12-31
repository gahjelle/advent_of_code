"""AoC 18, 2019: Many-Worlds Interpretation."""

# Standard library imports
import collections
import functools
import pathlib
import sys


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
        next(pos for pos, char in grid.items() if char == "@"),
        {pos: char for pos, char in grid.items() if "a" <= char <= "z"},
        {pos: char.lower() for pos, char in grid.items() if "A" <= char <= "Z"},
    )


def part1(data):
    """Solve part 1."""
    grid, start, keys, locks = data
    shortest = shortest_factory(find_paths(grid, {start: 0} | keys, locks))
    return shortest(frozenset([0]), frozenset(keys.values()), frozenset())


def part2(data):
    """Solve part 2."""
    grid, (row, col), keys, locks = data
    starts = {
        (row - 1, col - 1): 0,
        (row - 1, col + 1): 1,
        (row + 1, col - 1): 2,
        (row + 1, col + 1): 3,
    }
    grid -= {(row - 1, col), (row, col - 1), (row, col), (row, col + 1), (row + 1, col)}
    shortest = shortest_factory(find_paths(grid, starts | keys, locks))
    return shortest(frozenset(starts.values()), frozenset(keys.values()), frozenset())


def find_paths(grid, targets, locks):
    """Use BFS to find shortest paths between all nodes."""
    paths = {name: {} for name in targets.values()}
    for start, name in targets.items():
        queue = collections.deque([(start, 0, set())])
        seen = set()
        while queue:
            pos, num_steps, doors = queue.popleft()
            if pos in targets and pos != start:
                paths[name][targets[pos]] = (num_steps, doors)
            if pos in seen:
                continue
            seen.add(pos)

            for dpos in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_pos = (pos[0] + dpos[0], pos[1] + dpos[1])
                if new_pos in grid and new_pos not in seen:
                    new_doors = doors | {locks[new_pos]} if new_pos in locks else doors
                    queue.append((new_pos, num_steps + 1, new_doors))
    return paths


def shortest_factory(paths):
    """Create a function finding shortest paths"""

    @functools.cache
    def shortest(starts, remaining, keys):
        """Find the shortest path visiting remaining nodes"""
        if not remaining:
            return 0

        min_num_steps = 999_999
        for start in starts:
            for node in remaining:
                if node not in paths[start]:
                    continue
                steps_to_node, doors = paths[start][node]
                if doors - keys:
                    continue
                steps_from_node = shortest(
                    starts - {start} | {node}, remaining - {node}, keys | {node}
                )
                min_num_steps = min(min_num_steps, steps_to_node + steps_from_node)

        return min_num_steps

    return shortest


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
