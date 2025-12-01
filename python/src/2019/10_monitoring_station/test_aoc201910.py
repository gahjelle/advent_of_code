"""Tests for AoC 10, 2019: Monitoring Station."""

# Standard library imports
import pathlib

# Third party imports
import aoc201910
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201910.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc201910.parse_data(puzzle_input)


@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().rstrip()
    return aoc201910.parse_data(puzzle_input)


@pytest.fixture
def example4():
    puzzle_input = (PUZZLE_DIR / "example4.txt").read_text().rstrip()
    return aoc201910.parse_data(puzzle_input)


@pytest.fixture
def example5():
    puzzle_input = (PUZZLE_DIR / "example5.txt").read_text().rstrip()
    return aoc201910.parse_data(puzzle_input)


@pytest.fixture
def example6():
    puzzle_input = (PUZZLE_DIR / "example6.txt").read_text().rstrip()
    return aoc201910.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        (7, 0, 1),
        (7, 4, 4),
        (5, 2, 4),
        (7, 0, 4),
        (7, 2, 1),
        (7, 3, 4),
        (8, 4, 3),
        (6, 2, 0),
        (7, 2, 3),
        (7, 2, 2),
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201910.part1(example1) == 8


def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc201910.part1(example2) == 33


def test_part1_example3(example3):
    """Test part 1 on example input."""
    assert aoc201910.part1(example3) == 35


def test_part1_example4(example4):
    """Test part 1 on example input."""
    assert aoc201910.part1(example4) == 41


def test_part1_example5(example5):
    """Test part 1 on example input."""
    assert aoc201910.part1(example5) == 210


def test_part2_example5(example5):
    """Test part 2 on example input."""
    assert aoc201910.part2(example5) == 802


def test_part2_example6(example6):
    """Test part 2 on example input."""
    assert aoc201910.part2(example6) == 1403
