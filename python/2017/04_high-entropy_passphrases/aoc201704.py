"""AoC 4, 2017: High-Entropy Passphrases"""

# Standard library imports
import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [line.split() for line in puzzle_input.split("\n")]


def part1(data):
    """Solve part 1"""
    return sum(unique_words(words) for words in data)


def part2(data):
    """Solve part 2"""
    return sum(unique_anagrams(words) for words in data)


def unique_words(words):
    """Check if words are unique

    >>> unique_words(["abc", "cab", "bcd"])
    True

    >>> unique_words(["abc", "def", "abc"])
    False
    """
    return len(words) == len(set(words))


def unique_anagrams(words):
    """Check if anagrams of words are unique

    >>> unique_anagrams(["abc", "def", "ghi"])
    True

    >>> unique_anagrams(["abc", "cab", "bcd"])
    False
    """
    anagrams = ["".join(sorted(word)) for word in words]
    return len(anagrams) == len(set(anagrams))


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
