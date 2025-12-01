"""AoC 10, 2016: Balance Bots."""

# Standard library imports
import collections
import pathlib
import sys

# Third party imports
import parse

PATTERN_INPUT = parse.compile("value {value:d} goes to bot {bot:d}")
PATTERN_COMPARISON = parse.compile("bot {bot:d} gives low to {low} and high to {high}")
PATTERN_BOT = parse.compile("bot {bot:d}")
PATTERN_OUTPUT = parse.compile("output {output:d}")


def parse_data(puzzle_input):
    """Parse input."""
    bots = collections.defaultdict(list)
    comparisons = {}

    for line in puzzle_input.split("\n"):
        bots = parse_input(bots, line)
        comparisons = parse_comparison(comparisons, line)

    return bots, comparisons


def parse_input(bots, line):
    """Parse one line with input instructions.

    ## Examples:

    >>> parse_input({1: [4]}, "value 3 goes to bot 1")
    {1: [4, 3]}
    >>> parse_input({}, "bot 2 gives low to bot 1 and high to bot 0")
    {}
    """
    if match := PATTERN_INPUT.parse(line):
        return bots | {match["bot"]: bots[match["bot"]] + [match["value"]]}
    else:
        return bots


def parse_comparison(comparisons, line):
    """Parse one line with comparison instructions.

    >>> parse_comparison({}, "value 3 goes to bot 1")
    {}
    >>> parse_comparison({}, "bot 2 gives low to bot 1 and high to bot 0")
    {2: (1, 0)}
    >>> parse_comparison({2: (1, 0)}, "bot 1 gives low to output 1 and high to bot 0")
    {2: (1, 0), 1: (1001, 0)}
    """
    if match := PATTERN_COMPARISON.parse(line):
        return comparisons | {
            match["bot"]: (
                parse_bot_or_output(match["low"]),
                parse_bot_or_output(match["high"]),
            )
        }
    else:
        return comparisons


def parse_bot_or_output(bot_or_output):
    """Parse a bot or an output specification.

    ## Examples:

    >>> parse_bot_or_output("bot 4")
    4
    >>> parse_bot_or_output("output 7")
    1007
    """
    if match := PATTERN_BOT.parse(bot_or_output):
        return match["bot"]
    elif match := PATTERN_OUTPUT.parse(bot_or_output):
        return match["output"] + 1000


def part1(data, chips=(17, 61)):
    """Solve part 1."""
    return distribute(*data, stop_at=chips)


def part2(data):
    """Solve part 2."""
    outputs = distribute(*data)
    return outputs[0] * outputs[1] * outputs[2]


def distribute(bots, comparisons, stop_at=None):
    """Distribute chips according to instructions.

    Yield comparisons so they can be monitored from the outside.

    ## Examples:

    >>> distribute({2: [9, 4], 1: [6]}, {2: (1, 0), 1: (1001, 0), 0: (1002, 1000)}, (6, 9))
    0
    >>> distribute({2: [9, 4], 1: [6]}, {2: (1, 0), 1: (1001, 0), 0: (1002, 1000)})
    {1: 4, 2: 6, 0: 9}
    """
    outputs = {}
    while comparisons:
        for bot, chips in bots.items():
            if len(chips) < 2:
                continue
            low, high = min(chips), max(chips)
            if (low, high) == stop_at:
                return bot

            bots_and_chips = list(zip(comparisons[bot], (low, high)))
            bots = {b: c for b, c in bots.items() if b != bot} | {
                b: bots.get(b, []) + [c] for b, c in bots_and_chips if b < 1000
            }
            outputs = outputs | {o: c for o, c in bots_and_chips if o >= 1000}
            comparisons = {b: c for b, c in comparisons.items() if b != bot}

    return {output - 1000: value for output, value in outputs.items()}


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
