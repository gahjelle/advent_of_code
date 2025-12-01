"""Tests for AoC 20, 2024: Race Condition."""

# Standard library imports
import pathlib

# Third party imports
import aoc202420
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202420.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202420.parse_data(puzzle_input)


def test_parse_example2(example2):
    """Test that input is parsed properly."""
    assert example2 == {
        (1, 1): 0,
        (2, 1): 1,
        (3, 1): 2,
        (3, 2): 3,
        (3, 3): 4,
        (2, 3): 5,
        (1, 3): 6,
    }


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202420.part1(example1, 20) == 5


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202420.part2(example1, 70) == 41


def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc202420.part1(example2, 4) == 1
