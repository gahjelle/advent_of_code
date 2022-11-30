"""AoC 5, 2016: How About a Nice Game of Chess?"""

# Standard library imports
import collections
import functools
import hashlib
import itertools
import pathlib
import sys

DIGESTS = collections.defaultdict(list)


def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input


def part1(door_id, num_zeros=5, num_chars=8):
    """Solve part 1."""
    return "".join(
        md5[num_zeros]
        for _, md5 in zip(
            range(num_chars),
            itertools.chain(DIGESTS[door_id], generate_md5(door_id, "0" * num_zeros)),
        )
    )


def part2(door_id, num_zeros=5, num_chars=8):
    """Solve part 2."""
    hex_digits = "0123456789abcdef"

    prefix = "0" * num_zeros
    password = [""] * num_chars
    for md5 in itertools.chain(DIGESTS[door_id], generate_md5(door_id, prefix)):
        pos, char = hex_digits.index(md5[num_zeros]), md5[num_zeros + 1]
        if pos < num_chars and not password[pos]:
            password[pos] = char
            if all(password):
                break
    return "".join(password)


@functools.cache
def generate_md5(door_id, prefix):
    """Generate md5 hashes starting with prefix.

    ## Example:

    >>> next(generate_md5("aoc", "a0c"))
    'a0cb0f23b6a8313b2155b725ed59b452'
    >>> next(generate_md5("aoc", "a0c"))
    'a0c640ed60ef8bedca35bfd3db45ca8c'
    """
    md5_master = hashlib.md5()
    md5_master.update(door_id.encode("ascii"))
    for counter in itertools.count(start=1, step=1):
        md5 = md5_master.copy()
        md5.update(str(counter).encode("ascii"))
        digest = md5.hexdigest()

        if digest.startswith(prefix):
            DIGESTS[door_id].append(digest)
            yield digest


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
