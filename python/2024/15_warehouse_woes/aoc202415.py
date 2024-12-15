"""AoC 15, 2024: Warehouse Woes."""

# Standard library imports
import enum
import pathlib
import sys

# Third party imports
import colorama

colorama.init()


class Map(enum.StrEnum):
    EMPTY = "."
    WALL = "#"
    ROBOT = "@"
    BOX = "O"
    BOX_LEFT = "["
    BOX_RIGHT = "]"


NORTH = (-1, 0)
EAST = (0, 1)
SOUTH = (1, 0)
WEST = (0, -1)
MOVES = {"^": NORTH, ">": EAST, "v": SOUTH, "<": WEST}


def parse_data(puzzle_input):
    """Parse input."""
    grid, moves = puzzle_input.split("\n\n")
    return {
        (row, col): Map(char)
        for row, line in enumerate(grid.split("\n"))
        for col, char in enumerate(line)
    }, [MOVES[char] for char in moves.replace("\n", "")]


def part1(data):
    """Solve part 1."""
    grid, moves = data
    robot = next(pos for pos, char in grid.items() if char == Map.ROBOT)
    return sum(gps_coords(move(grid | {robot: Map.EMPTY}, robot, moves)))


def part2(data):
    """Solve part 2."""
    grid, moves = data
    grid = enlarge_grid(grid)
    robot = next(pos for pos, char in grid.items() if char == Map.ROBOT)
    return sum(gps_coords(move(grid | {robot: Map.EMPTY}, robot, moves)))


def enlarge_grid(grid):
    """Double width of grid"""
    new_grid = {}
    for (row, col), char in grid.items():
        match char:
            case Map.WALL | Map.EMPTY:
                new_grid[row, 2 * col] = char
                new_grid[row, 2 * col + 1] = char
            case Map.ROBOT:
                new_grid[row, 2 * col] = Map.ROBOT
                new_grid[row, 2 * col + 1] = Map.EMPTY
            case Map.BOX:
                new_grid[row, 2 * col] = Map.BOX_LEFT
                new_grid[row, 2 * col + 1] = Map.BOX_RIGHT
    return new_grid


def move(grid, robot, moves):
    """Try to move robot around grid while pushing boxes"""
    for dir in moves:
        new_pos = (robot[0] + dir[0], robot[1] + dir[1])
        match grid[new_pos]:
            case Map.EMPTY:
                robot = new_pos
            case Map.WALL:
                pass
            case Map.BOX | Map.BOX_LEFT | Map.BOX_RIGHT:
                if grid[new_pos] == Map.BOX or dir in [EAST, WEST]:
                    grid = push_simple(grid, new_pos, dir)
                else:
                    grid = push_double(grid, {new_pos}, dir)
                if grid[new_pos] == Map.EMPTY:
                    robot = new_pos
        if "--show" in sys.argv:
            show(grid, robot)
    return grid


def push_simple(grid, pos, dir):
    """Try to push a box in a given direction"""
    new_pos = (pos[0] + dir[0], pos[1] + dir[1])
    match grid[new_pos]:
        case Map.EMPTY:
            return grid | {pos: Map.EMPTY, new_pos: grid[pos]}
        case Map.WALL:
            return grid
        case Map.BOX | Map.BOX_LEFT | Map.BOX_RIGHT:
            grid = push_simple(grid, new_pos, dir)
            if grid[new_pos] == Map.EMPTY:
                return grid | {pos: Map.EMPTY, new_pos: grid[pos]}
    return grid


def push_double(grid, positions, dir):
    """Try to push a wide box north or south"""
    row = next(row for row, _ in positions)
    new_row = next(row + dir[0] for row, _ in positions)
    cols = set.union(
        *[
            {col, col + 1 if grid[row, col] == Map.BOX_LEFT else col - 1}
            for row, col in positions
            if grid[row, col] != Map.EMPTY
        ]
    )
    if all(grid[new_row, col] == Map.EMPTY for col in cols):
        return (
            grid
            | {(row, col): Map.EMPTY for col in cols}
            | {(new_row, col): grid[row, col] for col in cols}
        )
    elif all(grid[new_row, col] != Map.WALL for col in cols):
        grid = push_double(grid, {(new_row, col) for col in cols}, dir)
        if all(grid[new_row, col] == Map.EMPTY for col in cols):
            return (
                grid
                | {(row, col): Map.EMPTY for col in cols}
                | {(new_row, col): grid[row, col] for col in cols}
            )
    return grid


def gps_coords(grid):
    """Get Goods Positioning System coordinates of all boxes"""
    return [
        int(100 * row + col)
        for (row, col), char in grid.items()
        if char in [Map.BOX, Map.BOX_LEFT]
    ]


def show(grid, robot=None):
    """Display the grid in the terminal"""
    if robot is not None:
        grid = grid | {robot: Map.ROBOT}

    num_rows = int(max(row for row, _ in grid) + 1)
    num_cols = int(max(col for _, col in grid) + 1)
    print(colorama.Cursor.POS(1, 1))
    for row in range(num_rows):
        for col in range(num_cols):
            print(grid[row, col], end="")
        print()


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path.startswith("-"):
            continue
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
