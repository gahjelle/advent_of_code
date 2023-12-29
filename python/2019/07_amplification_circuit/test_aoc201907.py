"""Tests for AoC 7, 2019: Amplification Circuit."""

# Standard library imports
import pathlib

# Third party imports
import aoc201907
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201907.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc201907.parse_data(puzzle_input)


@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().rstrip()
    return aoc201907.parse_data(puzzle_input)


@pytest.fixture
def example4():
    puzzle_input = (PUZZLE_DIR / "example4.txt").read_text().rstrip()
    return aoc201907.parse_data(puzzle_input)


@pytest.fixture
def example5():
    puzzle_input = (PUZZLE_DIR / "example5.txt").read_text().rstrip()
    return aoc201907.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201907.part1(example1) == 43_210


def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc201907.part1(example2) == 54_321


def test_part1_example3(example3):
    """Test part 1 on example input."""
    assert aoc201907.part1(example3) == 65_210


def test_part2_example4(example4):
    """Test part 2 on example input."""
    assert aoc201907.part2(example4) == 139_629_729


def test_part2_example5(example5):
    """Test part 2 on example input."""
    assert aoc201907.part2(example5) == 18_216
