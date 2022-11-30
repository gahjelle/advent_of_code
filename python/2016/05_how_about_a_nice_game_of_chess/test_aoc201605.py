"""Tests for AoC 5, 2016: How About a Nice Game of Chess?"""

# Standard library imports
import pathlib

# Third party imports
import aoc201605
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201605.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == "abc"


def test_part1_example1_small(example1):
    """Test part 1 on example input."""
    assert aoc201605.part1(example1, num_zeros=2, num_chars=5) == "35675"


@pytest.mark.skip(reason="slow")
def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201605.part1(example1) == "18f47a30"


def test_part2_example1_small(example1):
    """Test part 2 on example input."""
    assert aoc201605.part2(example1, num_zeros=2, num_chars=5) == "d7342"


@pytest.mark.skip(reason="slow")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201605.part2(example1) == "05ace8e3"
