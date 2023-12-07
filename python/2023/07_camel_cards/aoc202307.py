"""AoC 7, 2023: Camel Cards."""

# Standard library imports
import collections
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    data = []
    for line in puzzle_input.split("\n"):
        cards, bid = line.split()
        data.append((cards, int(bid)))
    return data


def part1(data):
    """Solve part 1."""
    cards = sorted(((rank_cards(cards), bid) for cards, bid in data), reverse=True)
    return sum(rank * bid for rank, (_, bid) in enumerate(cards, start=1))


def part2(data):
    """Solve part 2."""
    cards = sorted(
        ((rank_cards(cards, use_joker=True), bid) for cards, bid in data), reverse=True
    )
    return sum(rank * bid for rank, (_, bid) in enumerate(cards, start=1))


def rank_cards(cards, use_joker=False):
    """Create a tuple that can be used to sort cards.

    ## Examples:

    >>> rank_cards("2345J", use_joker=False)
    (7, 12, 11, 10, 9, 3)
    >>> rank_cards("2345J", use_joker=True)
    (6, 11, 10, 9, 8, 12)
    >>> rank_cards("KJKKJ", use_joker=False)
    (3, 1, 3, 1, 1, 3)
    >>> rank_cards("KJKKJ", use_joker=True)
    (1, 1, 12, 1, 1, 12)
    """
    order = "AKQT98765432J" if use_joker else "AKQJT98765432"
    return (classify(cards, use_joker=use_joker),) + tuple(
        order.index(card) for card in cards
    )


def classify(cards, use_joker):
    """Classify poker hand.

    Returns a rank for each kind of hand.

    ## Examples:

    >>> classify("2345J", use_joker=False)
    7
    >>> classify("2345J", use_joker=True)
    6
    >>> classify("KJKKJ", use_joker=False)
    3
    >>> classify("KJKKJ", use_joker=True)
    1
    """
    if use_joker:
        card_counts = collections.Counter(cards)
        if "J" in card_counts:
            common, _ = collections.Counter(card_counts | {"J": 0}).most_common(1)[0]
            return classify(cards.replace("J", common), use_joker=False)

    counts = sorted(collections.Counter(cards).values())
    match counts:
        case [5]:  # Five of a kind
            return 1
        case [1, 4]:  # Four of a kind
            return 2
        case [2, 3]:  # Full house
            return 3
        case [1, 1, 3]:  # Three of a kind
            return 4
        case [1, 2, 2]:  # Two pairs
            return 5
        case [1, 1, 1, 2]:  # One pair
            return 6
        case [1, 1, 1, 1, 1]:  # High card
            return 7
        case _:
            raise ValueError(f"couldn't classify {cards}")


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
