"""AoC 24, 2017: Electromagnetic Moat."""

# Standard library imports
import collections
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    component_list = [
        tuple(int(num) for num in line.split("/")) for line in puzzle_input.split("\n")
    ]
    components = collections.defaultdict(list)
    for start, end in component_list:
        if start == end:  # Only add symmetric bridges once, put them first
            components[start].insert(0, (end, (start, end)))
        else:
            components[start].append((end, (start, end)))
            components[end].append((start, (start, end)))
    return components


def part1(components):
    """Solve part 1."""
    return max(
        sum(start + end for start, end in path) for path in find_paths(components, 0)
    )


def part2(components):
    """Solve part 2."""
    return max(
        (len(path), sum(start + end for start, end in path))
        for path in find_paths(components, 0)
    )[1]


def find_paths(components, start):
    """Find all paths that can be built with the given components."""
    queue = collections.deque([(start, [], set())])

    while queue:
        current, path, seen = queue.popleft()

        component_added = False
        for step, component in components[current]:
            if component not in seen:
                queue.append((step, path + [component], seen | {component}))
                component_added = True
                if step == current:  # Eagerly use symmetric bridges when possible
                    break

        if not component_added:
            yield path


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
