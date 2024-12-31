"""Tests for AoC 18, 2019: Many-Worlds Interpretation."""

# Standard library imports
import pathlib

# Third party imports
import aoc201918
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201918.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc201918.parse_data(puzzle_input)


@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().rstrip()
    return aoc201918.parse_data(puzzle_input)


@pytest.fixture
def example4():
    puzzle_input = (PUZZLE_DIR / "example4.txt").read_text().rstrip()
    return aoc201918.parse_data(puzzle_input)


@pytest.fixture
def example5():
    puzzle_input = (PUZZLE_DIR / "example5.txt").read_text().rstrip()
    return aoc201918.parse_data(puzzle_input)


@pytest.fixture
def example6():
    puzzle_input = (PUZZLE_DIR / "example6.txt").read_text().rstrip()
    return aoc201918.parse_data(puzzle_input)


@pytest.fixture
def example7():
    puzzle_input = (PUZZLE_DIR / "example7.txt").read_text().rstrip()
    return aoc201918.parse_data(puzzle_input)


@pytest.fixture
def example8():
    puzzle_input = (PUZZLE_DIR / "example8.txt").read_text().rstrip()
    return aoc201918.parse_data(puzzle_input)


@pytest.fixture
def example9():
    puzzle_input = (PUZZLE_DIR / "example9.txt").read_text().rstrip()
    return aoc201918.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    grid, start, keys, locks = example1
    assert grid == {(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)}
    assert start == (1, 5)
    assert keys == {(1, 7): "a", (1, 1): "b"}
    assert locks == {(1, 3): "a"}


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201918.part1(example1) == 8


def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc201918.part1(example2) == 86


def test_part1_example3(example3):
    """Test part 1 on example input."""
    assert aoc201918.part1(example3) == 132


def test_part1_example4(example4):
    """Test part 1 on example input."""
    assert aoc201918.part1(example4) == 136


def test_part1_example5(example5):
    """Test part 1 on example input."""
    assert aoc201918.part1(example5) == 81


def test_part1_example6(example6):
    """Test part 1 on example input."""
    assert aoc201918.part1(example6) == 26


def test_part1_example7(example7):
    """Test part 1 on example input."""
    assert aoc201918.part1(example7) == 50


def test_part1_example8(example8):
    """Test part 1 on example input."""
    assert aoc201918.part1(example8) == 127


def test_part1_example9(example9):
    """Test part 1 on example input."""
    assert aoc201918.part1(example9) == 114


def test_part2_example6(example6):
    """Test part 2 on example input."""
    assert aoc201918.part2(example6) == 8


def test_part2_example7(example7):
    """Test part 2 on example input."""
    assert aoc201918.part2(example7) == 24


def test_part2_example8(example8):
    """Test part 2 on example input."""
    assert aoc201918.part2(example8) == 32


def test_part2_example9(example9):
    """Test part 2 on example input."""
    assert aoc201918.part2(example9) == 72
