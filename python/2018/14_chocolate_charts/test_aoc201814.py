"""Tests for AoC 14, 2018: Chocolate Charts."""

# Standard library imports
import pathlib

# Third party imports
import aoc201814
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201814.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc201814.parse_data(puzzle_input)


@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().rstrip()
    return aoc201814.parse_data(puzzle_input)


@pytest.fixture
def example4():
    puzzle_input = (PUZZLE_DIR / "example4.txt").read_text().rstrip()
    return aoc201814.parse_data(puzzle_input)


@pytest.fixture
def example5():
    puzzle_input = (PUZZLE_DIR / "example5.txt").read_text().rstrip()
    return aoc201814.parse_data(puzzle_input)


@pytest.fixture
def example6():
    puzzle_input = (PUZZLE_DIR / "example6.txt").read_text().rstrip()
    return aoc201814.parse_data(puzzle_input)


@pytest.fixture
def example7():
    puzzle_input = (PUZZLE_DIR / "example7.txt").read_text().rstrip()
    return aoc201814.parse_data(puzzle_input)


@pytest.fixture
def example8():
    puzzle_input = (PUZZLE_DIR / "example8.txt").read_text().rstrip()
    return aoc201814.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == "9"


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201814.part1(example1) == "5158916779"


def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc201814.part1(example2) == "0124515891"


def test_part1_example3(example3):
    """Test part 1 on example input."""
    assert aoc201814.part1(example3) == "9251071085"


def test_part1_example4(example4):
    """Test part 1 on example input."""
    assert aoc201814.part1(example4) == "5941429882"


def test_part2_example5(example5):
    """Test part 2 on example input."""
    assert aoc201814.part2(example5) == 9


def test_part2_example6(example6):
    """Test part 2 on example input."""
    assert aoc201814.part2(example6) == 5


def test_part2_example7(example7):
    """Test part 2 on example input."""
    assert aoc201814.part2(example7) == 18


def test_part2_example8(example8):
    """Test part 2 on example input."""
    assert aoc201814.part2(example8) == 2018
