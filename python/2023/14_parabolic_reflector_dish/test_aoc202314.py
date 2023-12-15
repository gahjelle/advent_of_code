"""Tests for AoC 14, 2023: Parabolic Reflector Dish."""

# Standard library imports
import pathlib

# Third party imports
import aoc202314
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202314.parse_data(puzzle_input)


@pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == ...


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202314.part1(example1) == 136


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202314.part2(example1) == 64
