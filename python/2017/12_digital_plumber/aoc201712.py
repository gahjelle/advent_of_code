"""AoC 12, 2017: Digital Plumber"""

# Standard library imports
import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return dict(parse_pipe(line) for line in puzzle_input.split("\n"))


def parse_pipe(pipe):
    """Parse a line describing pipes from one program to others

    >>> parse_pipe("1 <-> 1")
    (1, [1])

    >>> parse_pipe("3 <-> 2, 4")
    (3, [2, 4])
    """
    from_id, _, to_id = pipe.partition(" <-> ")
    return int(from_id), [int(id) for id in to_id.split(", ")]


def part1(data):
    """Solve part 1"""
    return len(find_cluster(data, root_id=0))


def part2(data):
    """Solve part 2"""
    return len(find_clusters(data))


def find_cluster(pipes, root_id):
    """Find cluster containing root

    >>> cluster = find_cluster({0: [1, 2], 1: [0, 2], 2: [0, 1], 3: [3]}, 0)
    >>> sorted(cluster)
    [0, 1, 2]

    >>> find_cluster({0: [1, 2], 1: [0, 2], 2: [0, 1], 3: [3]}, 3)
    {3}
    """
    cluster = {root_id}
    to_add = set(pipes[root_id])
    while to_add:
        id = to_add.pop()
        cluster.add(id)
        to_add |= set(pipes[id]) - cluster

    return cluster


def find_clusters(pipes):
    """Find all clusters

    >>> clusters = find_clusters({0: [1, 2], 1: [0, 2], 2: [0, 1], 3: [3]})
    >>> [sorted(cluster) for cluster in clusters]
    [[0, 1, 2], [3]]
    """
    clusters = []
    remaining_roots = set(pipes)
    while remaining_roots:
        root_id = remaining_roots.pop()
        cluster = find_cluster(pipes, root_id)
        remaining_roots -= cluster
        clusters.append(cluster)

    return clusters


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
