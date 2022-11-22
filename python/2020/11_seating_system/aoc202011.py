"""AoC 11, 2020: Seating System"""

# Standard library imports
import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return {
        (row, col)
        for row, line in enumerate(puzzle_input.split("\n"))
        for col, seat in enumerate(line)
        if seat == "L"
    }


def part1(data):
    """Solve part 1"""
    return len(musical_chairs(closest_neighbors(data), tolerance=4))


def part2(data):
    """Solve part 2"""
    return len(musical_chairs(visible_neighbors(data), tolerance=5))


def closest_neighbors(seat_map):
    """Calculate closest neighbors for each seat

    ## Example:

        .LLL
        LL..
        .L.L

    >>> seat_map = [(0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (2, 1), (2, 3)]
    >>> closest_neighbors(seat_map)  # doctest: +NORMALIZE_WHITESPACE
    {(0, 1): [(0, 2), (1, 0), (1, 1)],
     (0, 2): [(0, 1), (0, 3), (1, 1)],
     (0, 3): [(0, 2)],
     (1, 0): [(0, 1), (1, 1), (2, 1)],
     (1, 1): [(0, 1), (0, 2), (1, 0), (2, 1)],
     (2, 1): [(1, 0), (1, 1)],
     (2, 3): []}
    """
    adjacent = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return {
        (row, col): [
            seat
            for drow, dcol in adjacent
            if (seat := (row + drow, col + dcol)) in seat_map
        ]
        for row, col in seat_map
    }


def visible_neighbors(seat_map):
    """Calculate visible neighbors for each seat

    ## Example:

        .LLL
        LL..
        .L.L

    >>> seat_map = [(0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (2, 1), (2, 3)]
    >>> visible_neighbors(seat_map)  # doctest: +NORMALIZE_WHITESPACE
    {(0, 1): [(0, 2), (1, 0), (1, 1), (2, 3)],
     (0, 2): [(0, 1), (0, 3), (1, 1)],
     (0, 3): [(0, 2), (2, 1), (2, 3)],
     (1, 0): [(0, 1), (1, 1), (2, 1)],
     (1, 1): [(0, 1), (0, 2), (1, 0), (2, 1)],
     (2, 1): [(1, 0), (1, 1), (0, 3), (2, 3)],
     (2, 3): [(0, 1), (0, 3), (2, 1)]}
    """
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    dimensions = (
        max(row for row, _ in seat_map) + 1,
        max(col for _, col in seat_map) + 1,
    )
    return {
        seat: [
            neighbor
            for direction in directions
            if (neighbor := visible_seat(seat_map, seat, direction, dimensions))
        ]
        for seat in seat_map
    }


def visible_seat(seat_map, seat, direction, dimensions):
    """Calculate first visible neighbor for one seat in one direction

    ## Example:

    >>> seat_map = [(0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (2, 1), (2, 3)]
    >>> visible_seat(seat_map, (0, 3), (1, 0), (3, 4))
    (2, 3)
    >>> visible_seat(seat_map, (1, 1), (0, 1), (3, 4))  # Returns None
    """
    row, col = seat
    drow, dcol = direction
    max_row, max_col = dimensions

    while 0 <= row < max_row and 0 <= col < max_col:
        row += drow
        col += dcol
        if (row, col) in seat_map:
            return (row, col)


def musical_chairs(neighbors, tolerance):
    """Simulate the seating dance until it reaches equlibrium

    ## Example:

        .LLL -> .### -> .### -> .###
        LL.. -> ##.. -> #L.. -> #L..
        .L.L -> .#.# -> .#.# -> .#.#

    >>> seat_map = [(0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (2, 1), (2, 3)]
    >>> neighbors = closest_neighbors(seat_map)
    >>> musical_chairs(neighbors, 4)
    [(0, 1), (0, 2), (0, 3), (1, 0), (2, 1), (2, 3)]
    """
    previous, current = None, {seat: False for seat in neighbors.keys()}
    while current != previous:
        previous, current = current, move_seats(current, neighbors, tolerance)

    return sorted(seat for seat, occupied in current.items() if occupied)


def move_seats(seats, neighbors, tolerance):
    """Move all seats once over

    ## Example:

        .#.L -> .L.#
        ##.L -> LL.L
        ...# -> ...#

    >>> seats = {(0, 1): 1, (0, 3): 0, (1, 0): 1, (1, 1): 1, (1, 3): 0, (2, 3): 1}
    >>> neighbors = {
    ...     (0, 1): [(1, 0), (1, 1)],
    ...     (0, 3): [(1, 3)],
    ...     (1, 0): [(0, 1), (1, 1)],
    ...     (1, 1): [(0, 1), (1, 0)],
    ...     (1, 3): [(0, 3), (2, 3)],
    ...     (2, 3): [(1, 3)],
    ... }
    >>> move_seats(seats, neighbors, tolerance=2) # doctest: +NORMALIZE_WHITESPACE
    {(0, 1): False, (0, 3): True, (1, 0): False, (1, 1): False,
     (1, 3): False, (2, 3): True}
    """
    return {
        seat: (occupied and num_nbs < tolerance) or (not occupied and num_nbs == 0)
        for seat, occupied in seats.items()
        for num_nbs in [sum(seats[nb] for nb in neighbors[seat])]
    }


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
