"""AoC 10, 2021: Syntax Scoring."""

# Standard library imports
import pathlib
import statistics
import sys

PAIRS = {"(": ")", "[": "]", "{": "}", "<": ">"}


def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input.split("\n")


def part1(data):
    """Solve part 1."""
    return sum(score_char(illegal_char(chunk)) for chunk in data)


def part2(data):
    """Solve part 2."""
    chunks = [
        left_over
        for chunk in data
        if (left_over := illegal_char(chunk)) not in PAIRS.values()
    ]
    return statistics.median([score_chunk(chunk) for chunk in chunks])


def illegal_char(chunk):
    """Find the first illegal character, or close up chunk if there are no
    illegal characters.

    >>> illegal_char("({}<)>")
    ')'

    >>> illegal_char("<([]<")
    ['>', ')', '>']
    """
    closing = []
    for char in chunk:
        match (char, closing):
            case char, closing if char in PAIRS:
                closing.append(PAIRS[char])
            case char, [*_, prev] if char == prev:
                closing.pop()
            case char, _:  # Illegal character
                return char

    # No illegal characters, return closing chunk
    return closing[::-1]


def score_char(char):
    """Score illegal character.

    >>> score_char("}")
    1197

    >>> score_char(["]", ")", "}", ">"])
    0
    """
    match char:
        case ")":
            return 3
        case "]":
            return 57
        case "}":
            return 1197
        case ">":
            return 25137

    return 0


def score_chunk(chunk, score=0):
    """Score left over chunk.

    >>> score_chunk(["]", ")", "}", ">"])
    294
    """
    match chunk:
        case [")", *tail]:
            return score_chunk(tail, score * 5 + 1)
        case ["]", *tail]:
            return score_chunk(tail, score * 5 + 2)
        case ["}", *tail]:
            return score_chunk(tail, score * 5 + 3)
        case [">", *tail]:
            return score_chunk(tail, score * 5 + 4)
        case []:
            return score


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
