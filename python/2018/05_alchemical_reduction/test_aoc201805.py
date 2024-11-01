"""Tests for AoC 5, 2018: Alchemical Reduction."""

# Standard library imports
import pathlib

# Third party imports
import aoc201805
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201805.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc201805.parse_data(puzzle_input)


@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().rstrip()
    return aoc201805.parse_data(puzzle_input)


@pytest.fixture
def example4():
    puzzle_input = (PUZZLE_DIR / "example4.txt").read_text().rstrip()
    return aoc201805.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1.tolist() == [4, 1, 2, -3, -2, -1, 3, 1, -4, -1]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201805.part1(example1) == 10


def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc201805.part1(example2) == 0


def test_part1_example3(example3):
    """Test part 1 on example input."""
    assert aoc201805.part1(example3) == 4


def test_part1_example4(example4):
    """Test part 1 on example input."""
    assert aoc201805.part1(example4) == 6


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201805.part2(example1) == 4
