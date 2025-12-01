"""AoC 7, 2015: Some Assembly Required."""

# Standard library imports
import pathlib
import sys

COMMANDS = {
    "SET": lambda value: value,
    "NOT": lambda value: ~value % (1 << 16),  # 2¹⁶ = 1 << 16 = 65536
    "AND": lambda first, second: first & second,
    "OR": lambda first, second: first | second,
    "LSHIFT": lambda value, shift: value << shift,
    "RSHIFT": lambda value, shift: value >> shift,
}


def parse_data(puzzle_input):
    """Parse input."""
    return dict(parse_signal(line) for line in puzzle_input.split("\n"))


def parse_signal(line):
    """Parse one line describing a signal.

    ## Examples:

    >>> parse_signal("1 -> a")
    ('a', ('SET', 1))
    >>> parse_signal("b -> cc")
    ('cc', ('SET', 'b'))
    >>> parse_signal("NOT x -> y")
    ('y', ('NOT', 'x'))
    >>> parse_signal("f OR g -> h")
    ('h', ('OR', 'f', 'g'))
    >>> parse_signal("p RSHIFT 3 -> q")
    ('q', ('RSHIFT', 'p', 3))
    >>> parse_signal("1 AND z -> ga")
    ('ga', ('AND', 1, 'z'))
    """
    signal, wire = line.split(" -> ")
    match signal.split():
        case [op1, op, op2]:
            return wire, (op, maybe_int(op1), maybe_int(op2))
        case [op, op1]:
            return wire, (op, maybe_int(op1))
        case [op1]:
            return wire, ("SET", maybe_int(op1))
        case _:
            raise ValueError(f"invalid signal: {signal}")


def maybe_int(text):
    """Convert strings to integers, if possible.

    ## Examples:

    >>> maybe_int("one")
    'one'
    >>> maybe_int("2")
    2
    """
    return int(text) if text.isnumeric() else text


def part1(data):
    """Solve part 1."""
    signals, gates = {}, data
    while "a" not in signals:
        signals, gates = resolve(signals, gates)
    return signals["a"]


def part2(data):
    """Solve part 2."""
    signals, gates = {}, data | {"b": ("SET", part1(data))}
    while "a" not in signals:
        signals, gates = resolve(signals, gates)
    return signals["a"]


def resolve(signals, gates):
    """Resolve gates by using known signals.

    ## Example:

    >>> resolve({"a": 1}, {"c": ("OR", "a", "b"), "b": ("NOT", "a")})
    ({'a': 1, 'b': 65534}, {'c': ('OR', 'a', 'b')})
    >>> resolve({"a": 1}, {"b": ("NOT", "a"), "c": ("OR", "a", "b")})
    ({'a': 1, 'b': 65534}, {'c': ('OR', 'a', 'b')})
    """
    new_signals, remaining_gates = {}, {}
    for wire, (cmd, *args) in gates.items():
        if all(arg in signals for arg in args if isinstance(arg, str)):
            new_signals[wire] = COMMANDS[cmd](*(signals.get(arg, arg) for arg in args))
        else:
            remaining_gates[wire] = (cmd, *args)
    return signals | new_signals, remaining_gates


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
