"""Some Assembly Required

Advent of Code 2015, day 7
Solution by Geir Arne Hjelle, 2016-12-04
"""
import sys
import numpy as np

COMMANDS = dict(NOT=lambda x: ~x,
                AND=lambda x, y: x & y,
                OR=lambda x, y: x | y,
                LSHIFT=lambda x, s: x << s,
                RSHIFT=lambda x, s: x >> s,
               )

SIGNALS = dict()


def read_circuit(filename):
    circuit = dict()
    with open(filename, mode='r') as fid:
        for line in fid:
            connection, output = [w.strip() for w in line.split('->')]
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


def main():
    filename = sys.argv[1]   # Only read one file since SIGNALS is global
    print('\n{}:'.format(filename))

    # part 1
    circuit = read_circuit(filename)
    while circuit:
        read_signals(circuit)

    signal_a = SIGNALS.get('a')
    for wire, signal in sorted(SIGNALS.items()):
#        print('{:>5s}: {}'.format(wire, signal))
        del SIGNALS[wire]

    print('The signal at a is {}'.format(signal_a))

    if signal_a is None:
        return

    # part 2
    circuit = read_circuit(filename)
    circuit['b'] = signal_a
    while circuit:
        read_signals(circuit)

    print('The modified signal at a is {}'.format(SIGNALS.get('a')))


if __name__ == '__main__':
    main()
