"""Tests for AoC 10, 2024: Hoof It."""

# Standard library imports
import pathlib

# Third party imports
import aoc202410
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202410.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202410.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == {
        (0, 0): 0,
        (0, 1): 1,
        (0, 2): 2,
        (0, 3): 3,
        (1, 0): 1,
        (1, 1): 2,
        (1, 2): 3,
        (1, 3): 4,
        (2, 0): 8,
        (2, 1): 7,
        (2, 2): 6,
        (2, 3): 5,
        (3, 0): 9,
        (3, 1): 8,
        (3, 2): 7,
        (3, 3): 6,
    }


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202410.part1(example1) == 1


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202410.part2(example1) == 16


def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc202410.part1(example2) == 36


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc202410.part2(example2) == 81
