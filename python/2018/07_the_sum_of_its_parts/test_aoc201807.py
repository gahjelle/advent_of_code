"""Tests for AoC 7, 2018: The Sum of Its Parts."""

# Standard library imports
import pathlib

# Third party imports
import aoc201807
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201807.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == {
        "A": {"C"},
        "B": {"A"},
        "D": {"A"},
        "E": {"B", "D", "F"},
        "F": {"C"},
    }


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201807.part1(example1) == "CABDFE"


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201807.part2(example1, num_workers=2, basetime=0) == 15
