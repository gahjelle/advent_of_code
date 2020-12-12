"""Some Assembly Required

Advent of Code 2015, day 7
Solution by Geir Arne Hjelle, 2016-12-04
"""
import pathlib
import sys
import numpy as np

COMMANDS = dict(
    NOT=lambda x: ~x,
    AND=lambda x, y: x & y,
    OR=lambda x, y: x | y,
    LSHIFT=lambda x, s: x << s,
    RSHIFT=lambda x, s: x >> s,
)

SIGNALS = {}


def read_circuit(filename):
    circuit = {}
    with open(filename, mode="r") as fid:
        for line in fid:
            connection, output = [w.strip() for w in line.split("->")]
            circuit[output] = connection

    return circuit


def read_signals(circuit):
    for wire, signal in circuit.copy().items():
        try:
            SIGNALS[wire] = _parse_signal(signal)
            del circuit[wire]
        except (TypeError, IndexError):
            pass


def _parse_signal(signal):
    value = SIGNALS.get(signal, _int(signal))
    if value is None:
        words = signal.split()
        command = words.pop(-2)
        value = COMMANDS[command](*[SIGNALS.get(w, _int(w)) for w in words])

    return value


def _int(string):
    """Convert to uint16 without ValueErrors, because dict.get() does not handle
    errors very gracefully...
    """
    try:
        return np.uint16(string)
    except ValueError:
        return None


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")

    # Part 1
    circuit = read_circuit(file_path)
    while circuit:
        read_signals(circuit)

    signal_a = SIGNALS.get("a")
    for wire, signal in sorted(SIGNALS.items()):
        del SIGNALS[wire]

    print(f"The signal at a is {signal_a}")

    if signal_a is None:
        return

    # Part 2
    circuit = read_circuit(file_path)
    circuit["b"] = signal_a
    while circuit:
        read_signals(circuit)

    print(f"The modified signal at a is {SIGNALS.get('a')}")


if __name__ == "__main__":
    main(sys.argv[1:])
