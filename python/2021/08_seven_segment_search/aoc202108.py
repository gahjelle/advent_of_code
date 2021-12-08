"""AoC 8, 2021: Seven Segment Search"""

# Standard library imports
import pathlib
import sys

DIGITS = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}


def parse(puzzle_input):
    """Parse input"""
    return [parse_line(line) for line in puzzle_input.split("\n")]


def parse_line(line):
    """Parse one line of input

    >>> parse_line("acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | "
    ...            "cdfeb fcadb cdfeb cdbaf")  # doctest: +NORMALIZE_WHITESPACE
    {'input': ['abcdefg', 'bcdef', 'acdfg', 'abcdf', 'abd', 'abcdef', 'bcdefg',
               'abef', 'abcdeg', 'ab'],
     'output': ['bcdef', 'abcdf', 'bcdef', 'abcdf']}
    """
    input, output = line.split(" | ")
    return {
        "input": ["".join(sorted(word)) for word in input.split()],
        "output": ["".join(sorted(word)) for word in output.split()],
    }


def part1(data):
    """Solve part 1"""
    return sum(count_unique(line["output"]) for line in data)


def count_unique(words):
    """Count words with unique digit lengths

    >>> count_unique(["abcdefg", "bcdef", "abd", "abef"])
    3
    """
    return sum(len(word) in {2, 3, 4, 7} for word in words)


def part2(data):
    """Solve part 2"""
    return sum(
        convert_digits(line["output"], deduce_digits(line["input"] + line["output"]))
        for line in data
    )


def convert_digits(digits, mapping):
    """Use mapping to convert digits into a number

    >>> convert_digits(["bcdef", "abcdf", "bcdef", "abcdf"], "deafgbc")
    5353
    """
    wire_map = dict(zip(mapping, "abcdefg"))
    mapped_digits = ["".join(sorted(wire_map[c] for c in digit)) for digit in digits]
    return int("".join(str(DIGITS.get(digit, 99)) for digit in mapped_digits))


def deduce_digits(digits):
    """Deduce the mapping that works for the given digits

    >>> deduce_digits(
    ...     ["abcdefg", "bcdef", "acdfg", "abcdf", "abd", "abcdef", "bcdefg",
    ...      "abef", "abcdeg", "ab"]
    ... )
    'deafgbc'
    """
    alternatives = build_alternatives(digits)
    mapping = {}

    while alternatives:
        for char, maps in alternatives.items():
            if len(maps) == 1:
                mapping[maps.pop()] = char

        for map, char in mapping.items():
            if char in alternatives:
                del alternatives[char]
                for maps in alternatives.values():
                    maps.discard(map)

    return "".join([mapping[c] for c in "abcdefg"])


def build_alternatives(digits):
    """Set up alternatives for each mapping, based on the given digits

    >>> alternatives = build_alternatives(
    ...     ["abcdefg", "bcdef", "acdfg", "abcdf", "abd", "abcdef", "bcdefg",
    ...      "abef", "abcdeg", "ab"]
    ... )
    >>> sorted(alternatives["d"])
    ['a', 'c', 'f']
    >>> len(alternatives["c"])
    7
    """
    alternatives = {c: set("abcdefg") for c in "abcdefg"}
    for digit in digits:
        match len(digit):
            case 2:  # digit is 1
                for c in digit:
                    alternatives[c] &= {"c", "f"}
            case 3:  # digit is 7
                for c in digit:
                    alternatives[c] &= {"a", "c", "f"}
            case 4:  # digit is 4
                for c in digit:
                    alternatives[c] &= {"b", "c", "d", "f"}
            case 5:  # digit is 2, 3, or 5
                for c in set("abcdefg") - set(digit):
                    alternatives[c] &= {"b", "c", "e", "f"}
            case 6:  # digit is 0, 6, or 9
                for c in set("abcdefg") - set(digit):
                    alternatives[c] &= {"c", "d", "e"}
            case 8:  # digit is 8 -> no information
                pass

    return alternatives


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
