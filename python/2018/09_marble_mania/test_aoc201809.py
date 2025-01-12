"""Tests for AoC 9, 2018: Marble Mania."""

# Standard library imports
import pathlib

# Third party imports
import aoc201809
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201809.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc201809.parse_data(puzzle_input)


@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().rstrip()
    return aoc201809.parse_data(puzzle_input)


@pytest.fixture
def example4():
    puzzle_input = (PUZZLE_DIR / "example4.txt").read_text().rstrip()
    return aoc201809.parse_data(puzzle_input)


@pytest.fixture
def example5():
    puzzle_input = (PUZZLE_DIR / "example5.txt").read_text().rstrip()
    return aoc201809.parse_data(puzzle_input)


@pytest.fixture
def example6():
    puzzle_input = (PUZZLE_DIR / "example6.txt").read_text().rstrip()
    return aoc201809.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == (9, 25)


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201809.part1(example1) == 32


def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc201809.part1(example2) == 8_317


def test_part1_example3(example3):
    """Test part 1 on example input."""
    assert aoc201809.part1(example3) == 146_373


def test_part1_example4(example4):
    """Test part 1 on example input."""
    assert aoc201809.part1(example4) == 2_764


def test_part1_example5(example5):
    """Test part 1 on example input."""
    assert aoc201809.part1(example5) == 54_718


def test_part1_example6(example6):
    """Test part 1 on example input."""
    assert aoc201809.part1(example6) == 37_305


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201809.part2(example1) == 22_563
