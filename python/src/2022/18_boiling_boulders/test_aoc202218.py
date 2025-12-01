"""Tests for AoC 18, 2022: Boiling Boulders."""

# Standard library imports
import pathlib

# Third party imports
import aoc202218
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202218.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == {
        (1, 2, 2),
        (1, 2, 5),
        (2, 1, 2),
        (2, 1, 5),
        (2, 2, 1),
        (2, 2, 2),
        (2, 2, 3),
        (2, 2, 4),
        (2, 2, 6),
        (2, 3, 2),
        (2, 3, 5),
        (3, 2, 2),
        (3, 2, 5),
    }


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202218.part1(example1) == 64


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202218.part2(example1) == 58
