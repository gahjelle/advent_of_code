"""AoC 15, 2015: Science for Hungry People."""

# Standard library imports
import itertools
import math
import pathlib
import sys

import parse

INGREDIENT_PATTERN = parse.compile(
    "{}: capacity {capacity:d}, durability {durability:d}, "
    "flavor {flavor:d}, texture {texture:d}, calories {calories:d}"
)


def parse_data(puzzle_input):
    """Parse input."""
    return [
        match.named
        for ingredient in puzzle_input.split("\n")
        if (match := INGREDIENT_PATTERN.parse(ingredient))
    ]


def part1(data):
    """Solve part 1."""
    return best_score(
        data,
        [
            (*spoons, 100 - total)
            for spoons in itertools.product(range(101), repeat=len(data) - 1)
            if (total := sum(spoons)) <= 100
        ],
    )


def part2(data):
    """Solve part 2."""
    return best_score(
        data,
        [
            variant
            for spoons in itertools.product(range(101), repeat=len(data) - 1)
            if (total := sum(spoons)) <= 100
            and calories(data, (variant := (*spoons, 100 - total))) == 500
        ],
    )


def best_score(ingredients, variants):
    """Find the best score among all cookie variants.

    ## Example:

    >>> ingredients = [
    ...     {"capacity": -1, "durability": -2, "flavor": 6, "texture": 3},
    ...     {"capacity": 2, "durability": 3, "flavor": -2, "texture": -1},
    ... ]
    >>> best_score(ingredients, [(30, 70), (50, 50), (70, 30)])
    50000000
    >>> (-50 + 100) * (-100 + 150) * (300 - 100) * (150 - 50)
    50000000
    """
    return max(math.prod(score_cookie(ingredients, spoons)) for spoons in variants)


def score_cookie(ingredients, spoons):
    """Score the composition of one cookie.

    ## Example:

    >>> ingredients = [
    ...     {"capacity": -1, "durability": -2, "flavor": 6, "texture": 3},
    ...     {"capacity": 2, "durability": 3, "flavor": -2, "texture": -1},
    ... ]
    >>> score_cookie(ingredients, (30, 70))
    [110, 150, 40, 20]
    """
    return [
        max(
            sum(
                num_spoons * per_spoon[property]
                for num_spoons, per_spoon in zip(spoons, ingredients)
            ),
            0,
        )
        for property in ("capacity", "durability", "flavor", "texture")
    ]


def calories(ingredients, spoons):
    """Find the number of calories in a cookie.

    ## Example:

    >>> ingredients = [{"calories": 8}, {"calories": 3}]
    >>> calories(ingredients, (30, 70))
    450
    """
    return sum(
        num_spoons * per_spoon["calories"]
        for num_spoons, per_spoon in zip(spoons, ingredients)
    )


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
