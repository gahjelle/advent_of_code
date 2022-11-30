"""AoC 5, 2015: Doesn't He Have Intern-Elves For This?"""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input"""
    return puzzle_input.split("\n")


def part1(data):
    """Solve part 1"""
    return len(
        [s for s in data if enough_vowels(s) and repeated(s) and not naughty_chars(s)]
    )


def part2(data):
    """Solve part 2"""
    return len([s for s in data if has_pair(s) and split_repeated(s)])


def enough_vowels(string, min_vowels=3):
    """Check that a string contains enough vowels

    ## Examples:

    >>> enough_vowels("adventofcode")
    True
    >>> enough_vowels("twoo")
    False
    >>> enough_vowels("threee")
    True
    >>> enough_vowels("threee", min_vowels=4)
    False
    """
    return sum(c in "aeiou" for c in string) >= min_vowels


def repeated(string):
    """Check that a string contains repeated characters

    ## Examples:

    >>> repeated("adventofcode")
    False
    >>> repeated("twoo")
    True
    >>> repeated("threee")
    True
    """
    return any(c1 == c2 for c1, c2 in zip(string[:-1], string[1:]))


def naughty_chars(string):
    """Check if a string contains naughty character combinations

    ## Examples:

    >>> naughty_chars("adventofcode")
    False
    >>> naughty_chars("about")
    True
    >>> naughty_chars("abcdpqxy")
    True
    """
    return any(nc in string for nc in ("ab", "cd", "pq", "xy"))


def has_pair(string):
    """Check if string has a repeated, non-overlapping pair of characters

    ## Examples:

    >>> has_pair("adventofcode")
    False
    >>> has_pair("adventofadvent")
    True
    >>> has_pair("threee")
    False
    >>> has_pair("foooour")
    True
    """
    num_chars = len(string)
    return any(string[idx : idx + 2] in string[idx + 2 :] for idx in range(num_chars))


def split_repeated(string):
    """Check if string contains repeated letters with exactly one letter between them

    ## Examples:

    >>> split_repeated("adventofcode")
    False
    >>> split_repeated("hohoho")
    True
    >>> split_repeated("threee")
    True
    """
    return any(c1 == c2 for c1, c2 in zip(string[:-2], string[2:]))


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
