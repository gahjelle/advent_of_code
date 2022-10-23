# Third party imports
import pytest

# Advent of Code imports
from aoc import intcode

END_STATES = [
    (
        "aoc201902_example1",
        [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50],
        [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50],
    ),
    ("aoc201902_example2", [1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
    ("aoc201902_example3", [2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
    ("aoc201902_example4", [2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
    (
        "aoc201902_example5",
        [1, 1, 1, 4, 99, 5, 6, 0, 99],
        [30, 1, 1, 4, 2, 5, 6, 0, 99],
    ),
    ("aoc201905_example2", [1002, 4, 3, 4, 33], [1002, 4, 3, 4, 99]),
    ("aoc201905_example3", [1101, 100, -1, 4, 0], [1101, 100, -1, 4, 99]),
]

INPUT_OUTPUT = [
    ("aoc201905_example1", [3, 0, 4, 0, 99], [12321], [12321]),
    ("aoc201905_example4a", [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], [8], [1]),
    ("aoc201905_example4b", [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], [42], [0]),
    ("aoc201905_example5a", [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], [6], [1]),
    ("aoc201905_example5b", [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], [42], [0]),
    ("aoc201905_example6a", [3, 3, 1108, -1, 8, 3, 4, 3, 99], [8], [1]),
    ("aoc201905_example6b", [3, 3, 1108, -1, 8, 3, 4, 3, 99], [42], [0]),
    ("aoc201905_example7a", [3, 3, 1107, -1, 8, 3, 4, 3, 99], [6], [1]),
    ("aoc201905_example7b", [3, 3, 1107, -1, 8, 3, 4, 3, 99], [42], [0]),
    (
        "aoc201905_example8a",
        ex201905_08 := [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9],
        [0],
        [0],
    ),
    ("aoc201905_example8b", ex201905_08, [42], [1]),
    (
        "aoc201905_example9a",
        ex201905_09 := [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1],
        [0],
        [0],
    ),
    ("aoc201905_example9b", ex201905_09, [42], [1]),
    (
        "aoc201905_example10a",
        ex201905_10 := (
            [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31]
            + [1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104]
            + [999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
        ),
        [3],
        [999],
    ),
    ("aoc201905_example10b", ex201905_10, [8], [1000]),
    ("aoc201905_example10c", ex201905_10, [42], [1001]),
]


@pytest.mark.parametrize(
    ["program", "end_state"],
    [p[1:] for p in END_STATES],
    ids=[p[0] for p in END_STATES],
)
def test_end_states(program, end_state):
    """Test that the end state of a full program is as expected"""
    computer = intcode.IntcodeComputer(program)
    computer.run()
    assert computer.program == end_state


@pytest.mark.parametrize(
    ["program", "input", "output"],
    [p[1:] for p in INPUT_OUTPUT],
    ids=[p[0] for p in INPUT_OUTPUT],
)
def test_input_output(program, input, output):
    """Test that a given input gives the expected output"""
    computer = intcode.IntcodeComputer(program, input=input)
    assert computer.run() == output
