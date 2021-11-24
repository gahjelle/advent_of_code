"""AoC 5, 2015: Doesn't He Have Intern-Elves For This?"""

# Standard library imports
import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return puzzle_input.split("\n")


def part1(data):
    """Solve part 1"""
    return len(
        [s for s in data if enough_vowels(s) and repeated(s) and not naughty_chars(s)]
    )


def enough_vowels(string, min_vowels=3):
    """Check that a string contains enough vowels"""
    vowels = set("aeiou")
    return len([c for c in string if c in vowels]) >= min_vowels


def repeated(string):
    """Check that a string contains repeated characters"""
    return any(c1 == c2 for c1, c2 in zip(string[:-1], string[1:]))


def naughty_chars(string):
    """Check if a string contains naughty character combinations"""
    return any(nc in string for nc in ["ab", "cd", "pq", "xy"])


def part2(data):
    """Solve part 2"""
    return len([s for s in data if has_pair(s) and split_repeated(s)])


def has_pair(string):
    """Check if string has a repeated, non-overlapping pair of characters"""
    num_chars = len(string)
    return any(string[idx : idx + 2] in string[idx + 2 :] for idx in range(num_chars))


def split_repeated(string):
    """Check if string contains repeated letters with exactly one letter between them"""
    return any(c1 == c2 for c1, c2 in zip(string[:-2], string[2:]))


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
