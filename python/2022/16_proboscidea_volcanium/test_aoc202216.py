"""Tests for AoC 16, 2022: Proboscidea Volcanium."""

# Standard library imports
import pathlib

# Third party imports
import aoc202216
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202216.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly.

    +-- B --+
    A+      C
    | +- D -+
    |    +---- E -- F -- G -- H
    |
    +-- I -- J
    """
    assert example1 == (
        {
            "AA": {"BB": 1, "CC": 2, "DD": 1, "EE": 2, "HH": 5, "JJ": 2},
            "BB": {"CC": 1, "DD": 2, "EE": 3, "HH": 6, "JJ": 3},
            "CC": {"BB": 1, "DD": 1, "EE": 2, "HH": 5, "JJ": 4},
            "DD": {"BB": 2, "CC": 1, "EE": 1, "HH": 4, "JJ": 3},
            "EE": {"BB": 3, "CC": 2, "DD": 1, "HH": 3, "JJ": 4},
            "HH": {"BB": 6, "CC": 5, "DD": 4, "EE": 3, "JJ": 7},
            "JJ": {"BB": 3, "CC": 4, "DD": 3, "EE": 4, "HH": 7},
        },
        {"AA": 0, "BB": 13, "CC": 2, "DD": 20, "EE": 3, "HH": 22, "JJ": 21},
    )


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202216.part1(example1) == 1651


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202216.part2(example1) == 1707
