"""Tests for AoC 15, 2018: Beverage Bandits."""

# Standard library imports
import pathlib

# Third party imports
import aoc201815
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201815.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc201815.parse_data(puzzle_input)


@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().rstrip()
    return aoc201815.parse_data(puzzle_input)


@pytest.fixture
def example4():
    puzzle_input = (PUZZLE_DIR / "example4.txt").read_text().rstrip()
    return aoc201815.parse_data(puzzle_input)


@pytest.fixture
def example5():
    puzzle_input = (PUZZLE_DIR / "example5.txt").read_text().rstrip()
    return aoc201815.parse_data(puzzle_input)


@pytest.fixture
def example6():
    puzzle_input = (PUZZLE_DIR / "example6.txt").read_text().rstrip()
    return aoc201815.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    grid, initial_pos = example1
    assert grid == {
        (1, 1),
        (1, 2),
        (1, 3),
        (1, 4),
        (1, 5),
        (2, 1),
        (2, 2),
        (2, 3),
        (2, 4),
        (2, 5),
        (3, 1),
        (3, 3),
        (3, 5),
        (4, 1),
        (4, 2),
        (4, 3),
        (4, 5),
        (5, 1),
        (5, 2),
        (5, 3),
        (5, 4),
        (5, 5),
    }
    assert initial_pos == {
        ((1, 2), "G"),
        ((2, 4), "E"),
        ((2, 5), "G"),
        ((3, 5), "G"),
        ((4, 3), "G"),
        ((4, 5), "E"),
    }


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201815.part1(example1) == 27_730


def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc201815.part1(example2) == 36_334


def test_part1_example3(example3):
    """Test part 1 on example input."""
    assert aoc201815.part1(example3) == 39_514


def test_part1_example4(example4):
    """Test part 1 on example input."""
    assert aoc201815.part1(example4) == 27_755


def test_part1_example5(example5):
    """Test part 1 on example input."""
    assert aoc201815.part1(example5) == 28_944


def test_part1_example6(example6):
    """Test part 1 on example input."""
    assert aoc201815.part1(example6) == 18_740


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201815.part2(example1) == 4_988


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc201815.part2(example2) == 29_064


def test_part2_example3(example3):
    """Test part 2 on example input."""
    assert aoc201815.part2(example3) == 31_284


def test_part2_example4(example4):
    """Test part 2 on example input."""
    assert aoc201815.part2(example4) == 3_478


def test_part2_example5(example5):
    """Test part 2 on example input."""
    assert aoc201815.part2(example5) == 6_474


def test_part2_example6(example6):
    """Test part 2 on example input."""
    assert aoc201815.part2(example6) == 1_140
