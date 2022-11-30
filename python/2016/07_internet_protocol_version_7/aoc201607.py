"""AoC 7, 2016: Internet Protocol Version 7"""

# Standard library imports
import pathlib
import re
import sys


def parse(puzzle_input):
    """Parse input."""
    return [parse_ipv7(line) for line in puzzle_input.split("\n")]


def parse_ipv7(address):
    """Parse one IPv7 address.

    ## Examples:

    >>> parse_ipv7("abba[mnop]qrst")
    (['abba', 'qrst'], ['mnop'])
    >>> parse_ipv7("aoc[gah]easter[bunny]noon")
    (['aoc', 'easter', 'noon'], ['gah', 'bunny'])
    """
    tokens = re.split(r"\[|\]", address)
    return tokens[::2], tokens[1::2]


def part1(addresses):
    """Solve part 1."""
    return sum(supports_tls(*address) for address in addresses)


def part2(addresses):
    """Solve part 2."""
    return sum(supports_ssl(*address) for address in addresses)


def supports_tls(supernet, hypernet):
    """Check if IPv7 address supports TLS.

    An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or
    ABBA. However, the IP also must not have an ABBA within any hypernet
    sequences, which are contained by square brackets.

    ## Examples:

    >>> supports_tls(["abba", "qrst"], ["mnop"])
    True
    >>> supports_tls(["qrst", "noon"], ["abba"])
    False
    """
    if any(has_abba(token) for token in hypernet):
        return False
    return any(has_abba(token) for token in supernet)


def has_abba(token):
    """Check if a token has an ABBA.

    An ABBA is any four-character sequence which consists of a pair of two
    different characters followed by the reverse of that pair, such as xyyx or
    abba.

    ## Examples:

    >>> has_abba("noon")
    True
    >>> has_abba("nono")
    False
    >>> has_abba("afternoons")
    True
    """
    return any(
        first == fourth and second == third and first != second
        for first, second, third, fourth in zip(token, token[1:], token[2:], token[3:])
    )


def supports_ssl(supernet, hypernet):
    """Check if IPv7 address supports SSL.

    An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in
    the supernet sequences (outside any square bracketed sections), and a
    corresponding Byte Allocation Block, or BAB, anywhere in the hypernet
    sequences.

    ## Examples:

    >>> supports_ssl(["aba"], ["bab"])
    True
    >>> supports_ssl(["zazbz", "cdb"], ["bzb"])
    True
    >>> supports_ssl(["xyx", "yxy"], ["bob"])
    False
    """
    return any(
        bab in hypertoken
        for supertoken in supernet
        for bab in find_aba_bab(supertoken)
        for hypertoken in hypernet
    )


def find_aba_bab(token):
    """Check if a token has an ABA and yield the corresponding BAB.

    An ABA is any three-character sequence which consists of the same
    character twice with a different character between them, such as xyx or aba.
    A corresponding BAB is the same characters but in reversed positions: yxy
    and bab, respectively.

    ## Examples:

    >>> list(find_aba_bab("aba"))
    ['bab']
    >>> list(find_aba_bab("nono"))
    ['ono', 'non']
    >>> list(find_aba_bab("honolulu"))
    ['non', 'ulu', 'lul']
    """
    for first, second, third in zip(token, token[1:], token[2:]):
        if first == third and first != second:
            yield f"{second}{first}{second}"


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
