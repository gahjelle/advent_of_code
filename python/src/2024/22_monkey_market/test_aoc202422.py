"""Tests for AoC 22, 2024: Monkey Market."""

# Standard library imports
import pathlib

# Third party imports
import aoc202422
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202422.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202422.parse_data(puzzle_input)


@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().rstrip()
    return aoc202422.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [1, 10, 100, 2024]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202422.part1(example1) == 37_327_623


def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc202422.part1(example2, num_steps=10) == 5_908_254


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc202422.part2(example2, num_steps=10) == 6


def test_part2_example3(example3):
    """Test part 2 on example input."""
    assert aoc202422.part2(example3) == 23
