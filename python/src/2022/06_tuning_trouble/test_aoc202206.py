"""Tests for AoC 6, 2022: Tuning Trouble."""

# Standard library imports
import pathlib

# Third party imports
import aoc202206
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202206.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202206.parse_data(puzzle_input)


@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().rstrip()
    return aoc202206.parse_data(puzzle_input)


@pytest.fixture
def example4():
    puzzle_input = (PUZZLE_DIR / "example4.txt").read_text().rstrip()
    return aoc202206.parse_data(puzzle_input)


@pytest.fixture
def example5():
    puzzle_input = (PUZZLE_DIR / "example5.txt").read_text().rstrip()
    return aoc202206.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == "mjqjpqmgbljsphdztnvjfqwrcgsmlb"


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202206.part1(example1) == 7


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202206.part2(example1) == 19


def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc202206.part1(example2) == 5


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc202206.part2(example2) == 23


def test_part1_example3(example3):
    """Test part 1 on example input."""
    assert aoc202206.part1(example3) == 6


def test_part2_example3(example3):
    """Test part 2 on example input."""
    assert aoc202206.part2(example3) == 23


def test_part1_example4(example4):
    """Test part 1 on example input."""
    assert aoc202206.part1(example4) == 10


def test_part2_example4(example4):
    """Test part 2 on example input."""
    assert aoc202206.part2(example4) == 29


def test_part1_example5(example5):
    """Test part 1 on example input."""
    assert aoc202206.part1(example5) == 11


def test_part2_example5(example5):
    """Test part 2 on example input."""
    assert aoc202206.part2(example5) == 26
