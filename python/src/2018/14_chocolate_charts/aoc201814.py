"""AoC 14, 2018: Chocolate Charts."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input


def part1(num_recipies):
    """Solve part 1."""
    _, last_ten = create_recipies([3, 7], num_recipies=int(num_recipies))
    return "".join(str(recipe) for recipe in last_ten)


def part2(pattern):
    """Solve part 2."""
    round, _ = create_recipies([3, 7], target=[int(recipe) for recipe in pattern])
    return round


def create_recipies(recipies, num_recipies=999_999_999, target=None):
    """Create recipies."""
    elves = [0, 1]
    target_len = 0 if target is None else len(target)
    while len(recipies) < num_recipies + 10:
        new_recipe = sum(recipies[elf] for elf in elves)
        if new_recipe < 10:
            recipies.append(new_recipe)
        else:
            recipies.extend(divmod(new_recipe, 10))
        elves = [(elf + 1 + recipies[elf]) % len(recipies) for elf in elves]

        if target_len:
            if recipies[-target_len:] == target:
                return len(recipies) - target_len, []
            if recipies[-target_len - 1 : -1] == target:
                return len(recipies) - target_len - 1, []

    return len(recipies), recipies[num_recipies : num_recipies + 10]


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
