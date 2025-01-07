"""AoC 11, 2018: Chronal Charge."""

# Standard library imports
import itertools
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return int(puzzle_input)


def part1(serial_number, grid_size=300):
    """Solve part 1."""
    grid = calculate_grid(serial_number, size=grid_size)
    sums = sum_grid(grid)
    _, ulx, uly = find_largest_sum(sums, 3)
    return f"{ulx},{uly}"


def part2(serial_number, grid_size=300):
    """Solve part 2."""
    grid = calculate_grid(serial_number, size=grid_size)
    sums = sum_grid(grid)

    ulx, uly, max_value, best_size = 0, 0, 0, 0
    for size in range(1, grid_size + 1):
        value, x, y = find_largest_sum(sums, size)
        if value > max_value:
            ulx, uly, max_value, best_size = x, y, value, size
        if value < 0:
            return f"{ulx},{uly},{best_size}"


def calculate_grid(serial_number, size):
    """Create the grid of fuel cells

    - Find the fuel cell's rack ID, which is its X coordinate plus 10.
    - Begin with a power level of the rack ID times the Y coordinate.
    - Increase the power level by the value of the grid serial number (your puzzle input).
    - Set the power level to itself multiplied by the rack ID.
    - Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
    - Subtract 5 from the power level.

    ## Examples:

    >>> calculate_grid(8, 5)[3, 5]
    4

    >>> calculate_grid(57, 122)[122, 79]
    -5

    >>> calculate_grid(39, 217)[217, 196]
    0

    >>> calculate_grid(71, 153)[101, 153]
    4
    """
    grid = {}
    for x, y in itertools.product(range(1, size + 1), range(1, size + 1)):
        grid[x, y] = (((x + 10) * y + serial_number) * (x + 10) // 100) % 10 - 5
    return grid


def sum_grid(grid):
    """Convert a grid of numbers into accumulated sums.

    Start the accumulation in the bottom right corner to simplify calculations
    later.

    ## Example:

     4  1   ->   5  3
    -2  2        0  2

    >>> sum_grid({(1, 1): 4, (2, 1): 1, (1, 2): -2, (2, 2): 2})
    {(2, 2): 2, (1, 2): 0, (2, 1): 3, (1, 1): 5}
    """
    max_x, max_y = max(grid)

    sums = {}
    for y in range(max_y, 0, -1):
        row = 0
        for x in range(max_x, 0, -1):
            row += grid[x, y]
            sums[x, y] = sums.get((x, y + 1), 0) + row
    return sums


def find_largest_sum(sums, sz):
    """Find the square with the largest sum, based on accumulated sums."""
    mx, my = max(sums)
    idx_x, idx_y, max_value = 0, 0, -5 * sz**2
    for x, y in itertools.product(range(1, mx - sz + 1), range(1, my - sz + 1)):
        value = sums[x, y] + sums[x + sz, y + sz] - sums[x + sz, y] - sums[x, y + sz]
        if value > max_value:
            idx_x, idx_y, max_value = x, y, value
    return max_value, idx_x, idx_y


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
