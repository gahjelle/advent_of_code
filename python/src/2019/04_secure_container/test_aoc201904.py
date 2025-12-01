"""Tests for AoC 4, 2019: Secure Container."""

# Standard library imports
import pathlib

# Third party imports
import aoc201904
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201904.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc201904.parse_data(puzzle_input)


@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().strip()
    return aoc201904.parse_data(puzzle_input)


@pytest.fixture
def example4():
    puzzle_input = (PUZZLE_DIR / "example4.txt").read_text().strip()
    return aoc201904.parse_data(puzzle_input)


@pytest.fixture
def example5():
    puzzle_input = (PUZZLE_DIR / "example5.txt").read_text().strip()
    return aoc201904.parse_data(puzzle_input)


@pytest.fixture
def example6():
    puzzle_input = (PUZZLE_DIR / "example6.txt").read_text().strip()
    return aoc201904.parse_data(puzzle_input)


@pytest.fixture
def example7():
    puzzle_input = (PUZZLE_DIR / "example7.txt").read_text().strip()
    return aoc201904.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == ["123454", "123455", "123456"]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201904.part1(example1) == 1


def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc201904.part1(example2) == 1


def test_part1_example3(example3):
    """Test part 1 on example input."""
    assert aoc201904.part1(example3) == 0


def test_part1_example4(example4):
    """Test part 1 on example input."""
    assert aoc201904.part1(example4) == 0


def test_part1_example5(example5):
    """Test part 1 on example input."""
    assert aoc201904.part1(example5) == 1


def test_part1_example6(example6):
    """Test part 1 on example input."""
    assert aoc201904.part1(example6) == 1


def test_part1_example7(example7):
    """Test part 1 on example input."""
    assert aoc201904.part1(example7) == 1


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201904.part2(example1) == 1


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc201904.part2(example2) == 0


def test_part2_example3(example3):
    """Test part 2 on example input."""
    assert aoc201904.part2(example3) == 0


def test_part2_example4(example4):
    """Test part 2 on example input."""
    assert aoc201904.part2(example4) == 0


def test_part2_example5(example5):
    """Test part 2 on example input."""
    assert aoc201904.part2(example5) == 1


def test_part2_example6(example6):
    """Test part 2 on example input."""
    assert aoc201904.part2(example6) == 0


def test_part2_example7(example7):
    """Test part 2 on example input."""
    assert aoc201904.part2(example7) == 1
