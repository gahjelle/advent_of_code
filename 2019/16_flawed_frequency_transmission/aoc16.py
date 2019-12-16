"""Flawed Frequency Transmission

Advent of Code 2019, day 16
Solution by Geir Arne Hjelle, 2019-12-16
"""
import itertools
import pathlib
import sys
from dataclasses import dataclass, field

import numpy as np

debug = print if "--debug" in sys.argv else lambda *_: None

BASE_PATTERN = [0, 1, 0, -1]


@dataclass
class Pattern:
    num: int
    _state: int = field(default=None, init=False)
    _value: int = field(default=None, init=False)
    _pattern: list = field(default=None, init=False, repr=False)

    def __iter__(self):
        self._state = 0
        self._pattern = itertools.cycle(BASE_PATTERN)
        self._value = next(self._pattern)
        return self

    def __next__(self):
        if self._state >= self.num:
            self._state = -1
            self._value = next(self._pattern)
        self._state += 1

        return self._value


def fft(sequence, repeats=100):
    seq_len = len(sequence)
    pattern = np.array(
        [list(itertools.islice(Pattern(idx), seq_len)) for idx in range(seq_len)]
    )
    seq_array = np.array(sequence)
    for _ in range(repeats):
        seq_array = np.abs(np.sum(pattern * seq_array, axis=1)) % 10

    return seq_array.tolist()


def digit_sum(sequence, repeats=100):
    seq_array = np.array(sequence[::-1])
    for _ in range(repeats):
        seq_array = seq_array.cumsum() % 10

    return seq_array[::-1].tolist()


def main(args):
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        print(f"\n{file_path}:")
        sequence = [int(digit) for digit in file_path.read_text().strip()]

        # Part 1
        part_1 = fft(sequence, 100)[:8]
        print(f"The test signal is {''.join(str(d) for d in part_1)}")

        # Part 2
        long_sequence = sequence * 10_000
        offset = int("".join(str(d) for d in long_sequence[:7]))
        if offset < len(long_sequence) // 2:
            print("Don't know how to handle such short offsets")
            continue

        part_2 = digit_sum(long_sequence[offset:])[:8]
        print(f"The clean signal is {''.join(str(d) for d in part_2)}")


if __name__ == "__main__":
    main(sys.argv[1:])
