"""Tests for AoC 25, 2017: The Halting Problem."""

# Standard library imports
import pathlib

# Third party imports
import aoc201725
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201725.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == (
        "A",
        6,
        {
            "A": {0: (1, 1, "B"), 1: (0, -1, "B")},
            "B": {0: (1, -1, "A"), 1: (1, 1, "A")},
        },
    )


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201725.part1(example1) == 3
