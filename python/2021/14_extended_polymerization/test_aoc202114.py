"""Tests for AoC 14, 2021: Extended Polymerization."""

# Standard library imports
import pathlib

# Third party imports
import aoc202114
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202114.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1.first == "N"
    assert example1.pairs == {"NN": 1, "NC": 1, "CB": 1}
    assert example1.rules == {
        "CH": ["CB", "BH"],
        "HH": ["HN", "NH"],
        "CB": ["CH", "HB"],
        "NH": ["NC", "CH"],
        "HB": ["HC", "CB"],
        "HC": ["HB", "BC"],
        "HN": ["HC", "CN"],
        "NN": ["NC", "CN"],
        "BH": ["BH", "HH"],
        "NC": ["NB", "BC"],
        "NB": ["NB", "BB"],
        "BN": ["BB", "BN"],
        "BB": ["BN", "NB"],
        "BC": ["BB", "BC"],
        "CC": ["CN", "NC"],
        "CN": ["CC", "CN"],
    }


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202114.part1(example1) == 1588


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202114.part2(example1) == 2_188_189_693_529
