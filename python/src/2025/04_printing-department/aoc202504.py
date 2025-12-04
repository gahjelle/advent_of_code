"""AoC day 4, 2025: Printing Department."""

type Coordinate = tuple[int, int]
type Grid = set[Coordinate]


def parse_data(puzzle_input: str) -> Grid:
    """Parse puzzle input."""
    return {
        (row, col)
        for row, line in enumerate(puzzle_input.split("\n"))
        for col, char in enumerate(line)
        if char == "@"
    }


def part1(grid: Grid) -> int:
    """Solve part 1."""
    return sum(count_neighbours(grid, pos) < 4 for pos in grid)


def part2(grid: Grid) -> int:
    """Solve part 2."""
    paper = grid
    while True:
        if remove := {pos for pos in paper if count_neighbours(paper, pos) < 4}:
            paper = paper - remove
        else:
            break
    return len(grid - paper)


def count_neighbours(grid: Grid, pos: Coordinate) -> int:
    """Count the number of neighbours to the given position.

    ## Examples

        @@..
        .@@@
        ..@.

    >>> grid = {(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (2, 2)}
    >>> count_neighbours(grid, (0, 1))
    3
    >>> count_neighbours(grid, (1, 1))
    4
    >>> count_neighbours(grid, (2, 0))
    1
    """
    r, c = pos
    return sum(
        nbh in grid
        for nbh in [
            (r - 1, c - 1),
            (r - 1, c),
            (r - 1, c + 1),
            (r, c - 1),
            (r, c + 1),
            (r + 1, c - 1),
            (r + 1, c),
            (r + 1, c + 1),
        ]
    )
