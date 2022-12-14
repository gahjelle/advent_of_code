"""AoC 12, 2022: Hill Climbing Algorithm."""

# Standard library imports
import collections
import pathlib
import sys

# Third party imports
import numpy as np

START, END = -1, -26


def parse_data(puzzle_input):
    """Parse input."""
    grid = np.array(
        [
            [ord(char) - ord("a") + 1 for char in line]
            for line in puzzle_input.split("\n")
        ]
    )
    grid[grid == ord("S") - ord("a") + 1] = START
    grid[grid == ord("E") - ord("a") + 1] = END
    return grid


def part1(grid):
    """Solve part 1."""
    return find_path(
        grid=grid,
        start=tuple(coord.item() for coord in np.where(grid == START)),
        step_test=lambda current, step: abs(step) - abs(current) <= 1,
        goal_test=lambda current: current == END,
    )


def part2(grid):
    """Solve part 2."""
    return find_path(
        grid=np.abs(grid),
        start=tuple(coord.item() for coord in np.where(grid == END)),
        step_test=lambda current, step: step - current >= -1,
        goal_test=lambda current: current == abs(START),
    )


def find_path(grid, start, step_test, goal_test):
    """Find the best path from start until the goal test succeeds."""
    best = {start: 0}
    queue = collections.deque([(0, start, [start])])

    while queue:
        num_steps, current, path = queue.popleft()
        if goal_test(grid[current]):
            break

        row, col = current
        max_row, max_col = grid.shape
        neighbors = [
            (next_row, next_col)
            for next_row, next_col in [
                (row, col - 1),
                (row, col + 1),
                (row - 1, col),
                (row + 1, col),
            ]
            if 0 <= next_row < max_row and 0 <= next_col < max_col
            if step_test(grid[current], grid[next_row, next_col])
        ]

        for next_step in neighbors:
            if next_step in best and best[next_step] <= num_steps + 1:
                continue
            queue.append((num_steps + 1, next_step, path + [next_step]))
            best[next_step] = num_steps + 1
    else:
        raise ValueError("could not find a valid path")

    if "--viz" in sys.argv:
        visualize_path(grid, path)
    return num_steps


def visualize_path(grid, path):
    """Visualize the path."""
    # Third party imports
    import colorama
    from colorama import Fore

    colorama.init(autoreset=True)
    print("-" * grid.shape[1])
    print(
        "\n".join(
            "".join(line)
            for line in [
                [
                    f"{Fore.BLUE}{chr(height + ord('A') - 1)}"
                    if height < 0
                    else f"{Fore.RED}{chr(height + ord('A') - 1)}"
                    if (row, col) in path
                    else f"{Fore.LIGHTGREEN_EX}{chr(abs(height) + ord('a') - 1)}"
                    for col, height in enumerate(line)
                ]
                for row, line in enumerate(grid)
            ]
        )
    )


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
