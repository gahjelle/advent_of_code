"""AoC 24, 2019: Planet of Discord."""

# Standard library imports
import collections
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return {
        (row, col)
        for row, line in enumerate(puzzle_input.split("\n"))
        for col, char in enumerate(line)
        if char == "#"
    }


def part1(layout):
    """Solve part 1."""
    seen = set()
    while (rating := biodiversity_rating(layout)) not in seen:
        seen.add(rating)
        layout = evolve(layout, adjacent=adjacent_4)
    return rating


def part2(layout, minutes=200):
    """Solve part 2."""
    layout = {(0, row, col) for row, col in layout}
    for _ in range(minutes):
        layout = evolve(layout, adjacent=adjacent_recursive)
    return len(layout)


def adjacent_4(row, col):
    """Return all cells adjacent to the given cell."""
    return {
        (nr, nc)
        for nr, nc in [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]
        if 0 <= nr < 5 and 0 <= nc < 5
    }


def adjacent_recursive(level, row, col):
    """Return all cells adjacent to the given cell, taking recursive levels into account"""
    neighbors = set()
    for nr, nc in [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]:
        if (nr, nc) == (2, 2):
            if (row, col) == (1, 2):
                neighbors |= {(level + 1, 0, c) for c in range(5)}
            elif (row, col) == (2, 3):
                neighbors |= {(level + 1, r, 4) for r in range(5)}
            elif (row, col) == (3, 2):
                neighbors |= {(level + 1, 4, c) for c in range(5)}
            elif (row, col) == (2, 1):
                neighbors |= {(level + 1, r, 0) for r in range(5)}
        elif nr == -1:
            neighbors |= {(level - 1, 1, 2)}
        elif nr == 5:
            neighbors |= {(level - 1, 3, 2)}
        elif nc == -1:
            neighbors |= {(level - 1, 2, 1)}
        elif nc == 5:
            neighbors |= {(level - 1, 2, 3)}
        else:
            neighbors |= {(level, nr, nc)}
    return neighbors


def evolve(layout, adjacent=adjacent_4):
    """Evolve the given layout one generation.

    - A bug dies (becoming an empty space) unless there is exactly one bug
      adjacent to it.
    - An empty space becomes infested with a bug if exactly one or two bugs are
      adjacent to it.

    ## Example:

        #.#..      13010      #..#.
        ##...      21200      .##..
        .....  ->  11000  ->  ##...
        .....      00000      .....
        .....      00000      .....


    >>> sorted(evolve({(0, 0), (0, 2), (1, 0), (1, 1)}))
    [(0, 0), (0, 3), (1, 1), (1, 2), (2, 0), (2, 1)]
    """
    neighbors = collections.defaultdict(int)
    for bug in layout:
        for pos in adjacent(*bug):
            neighbors[pos] += 1

    stay_alive = {bug for bug, count in neighbors.items() if count == 1} & layout
    come_alive = {
        empty for empty, count in neighbors.items() if count in [1, 2]
    } - layout
    return stay_alive | come_alive


def biodiversity_rating(layout):
    """Calculate the biodiversity rating of a given layout.

    ## Example:

    >>> biodiversity_rating({(3, 0), (4, 1)})
    2129920
    """
    return sum(2 ** (row * 5 + col) for row, col in layout)


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
