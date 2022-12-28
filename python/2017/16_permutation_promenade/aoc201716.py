"""AoC 16, 2017: Permutation Promenade."""

# Standard library imports
import itertools
import pathlib
import string
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return [parse_move(move) for move in puzzle_input.split(",")]


def parse_move(move):
    """Parse one dance move.

    ## Examples:

    >>> parse_move("s12")
    ('s', 12, 0)
    >>> parse_move("x1/11")
    ('x', 1, 11)
    >>> parse_move("pf/a")
    ('p', 'f', 'a')
    """
    if move[0] == "s":
        return "s", int(move[1:]), 0
    elif move[0] == "x":
        return "x", *[int(arg) for arg in move[1:].split("/")]
    else:
        return "p", *move[1:].split("/")


def part1(moves, num_programs=16):
    """Solve part 1."""
    programs = list(string.ascii_lowercase[:num_programs])
    return "".join(dance(programs, moves))


def part2(moves, num_programs=16):
    """Solve part 2."""
    programs = list(string.ascii_lowercase[:num_programs])
    dances = {"".join(programs): 0}
    for count in itertools.count(1):
        programs = dance(programs, moves)
        program_hash = "".join(programs)
        if program_hash in dances:
            break
        dances[program_hash] = count

    dance_id = 1_000_000_000 % count
    return next(dance for dance, id in dances.items() if id == dance_id)


def dance(programs, moves):
    """Shuffle the programs based on the dance moves.

    ## Example:

    >>> dance(["a", "b", "c", "d", "e"], [("s", 1, 0), ("x", 3, 4), ("p", "e", "b")])
    ['b', 'a', 'e', 'd', 'c']
    """
    for move, first, second in moves:
        if move == "s":
            programs = programs[-first:] + programs[:-first]
        elif move == "x":
            programs[first], programs[second] = programs[second], programs[first]
        elif move == "p":
            idx_1, idx_2 = programs.index(first), programs.index(second)
            programs[idx_1], programs[idx_2] = programs[idx_2], programs[idx_1]
    return programs


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
