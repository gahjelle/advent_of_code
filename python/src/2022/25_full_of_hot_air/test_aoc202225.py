"""Tests for AoC 25, 2022: Full of Hot Air."""

# Standard library imports
import pathlib

# Third party imports
import aoc202225
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202225.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        "1=-0-2",
        "12111",
        "2=0=",
        "21",
        "2=01",
        "111",
        "20012",
        "112",
        "1=-1=",
        "1-12",
        "12",
        "1=",
        "122",
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202225.part1(example1) == "2=-1=0"
