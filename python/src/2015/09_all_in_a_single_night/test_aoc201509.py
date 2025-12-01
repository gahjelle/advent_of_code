"""Tests for AoC 9, 2015: All in a Single Night."""

# Standard library imports
import pathlib

# Third party imports
import aoc201509
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201509.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == {
        "London": {"Dublin": 464, "Belfast": 518},
        "Dublin": {"London": 464, "Belfast": 141},
        "Belfast": {"London": 518, "Dublin": 141},
    }


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201509.part1(example1) == 605


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201509.part2(example1) == 982
