"""Tests for AoC 4, 2018: Repose Record."""

# Standard library imports
import pathlib

# Third party imports
import aoc201804
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201804.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == {
        10: {
            5: 1,
            6: 1,
            7: 1,
            8: 1,
            9: 1,
            10: 1,
            11: 1,
            12: 1,
            13: 1,
            14: 1,
            15: 1,
            16: 1,
            17: 1,
            18: 1,
            19: 1,
            20: 1,
            21: 1,
            22: 1,
            23: 1,
            24: 2,
            25: 1,
            26: 1,
            27: 1,
            28: 1,
            30: 1,
            31: 1,
            32: 1,
            33: 1,
            34: 1,
            35: 1,
            36: 1,
            37: 1,
            38: 1,
            39: 1,
            40: 1,
            41: 1,
            42: 1,
            43: 1,
            44: 1,
            45: 1,
            46: 1,
            47: 1,
            48: 1,
            49: 1,
            50: 1,
            51: 1,
            52: 1,
            53: 1,
            54: 1,
        },
        99: {
            36: 1,
            37: 1,
            38: 1,
            39: 1,
            40: 2,
            41: 2,
            42: 2,
            43: 2,
            44: 2,
            45: 3,
            46: 2,
            47: 2,
            48: 2,
            49: 2,
            50: 1,
            51: 1,
            52: 1,
            53: 1,
            54: 1,
        },
    }


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201804.part1(example1) == 240


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201804.part2(example1) == 4455
