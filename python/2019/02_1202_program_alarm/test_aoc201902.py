"""Tests for AoC 2, 2019: 1202 Program Alarm."""

# Standard library imports
import pathlib

# Third party imports
import aoc201902
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201902.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201902.intcode.run_program(example1) == {
        0: 3500,
        1: 9,
        2: 10,
        3: 70,
        4: 2,
        5: 3,
        6: 11,
        7: 0,
        8: 99,
        9: 30,
        10: 40,
        11: 50,
    }
