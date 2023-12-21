"""Tests for AoC 21, 2023: Step Counter."""

# Standard library imports
import pathlib

# Third party imports
import aoc202321
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202321.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202321.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    start, grid = example1
    assert start == (5, 5)
    assert grid == {
        (0, 0),
        (0, 1),
        (0, 10),
        (0, 2),
        (0, 3),
        (0, 4),
        (0, 5),
        (0, 6),
        (0, 7),
        (0, 8),
        (0, 9),
        (1, 0),
        (1, 1),
        (1, 10),
        (1, 2),
        (1, 3),
        (1, 4),
        (1, 8),
        (10, 0),
        (10, 1),
        (10, 10),
        (10, 2),
        (10, 3),
        (10, 4),
        (10, 5),
        (10, 6),
        (10, 7),
        (10, 8),
        (10, 9),
        (2, 0),
        (2, 10),
        (2, 4),
        (2, 7),
        (2, 8),
        (3, 0),
        (3, 1),
        (3, 10),
        (3, 3),
        (3, 5),
        (3, 6),
        (3, 7),
        (3, 9),
        (4, 0),
        (4, 1),
        (4, 10),
        (4, 2),
        (4, 3),
        (4, 5),
        (4, 7),
        (4, 8),
        (4, 9),
        (5, 0),
        (5, 10),
        (5, 3),
        (5, 4),
        (5, 5),
        (6, 0),
        (6, 10),
        (6, 3),
        (6, 4),
        (6, 6),
        (6, 7),
        (6, 8),
        (7, 0),
        (7, 1),
        (7, 10),
        (7, 2),
        (7, 3),
        (7, 4),
        (7, 5),
        (7, 6),
        (7, 9),
        (8, 0),
        (8, 10),
        (8, 3),
        (8, 5),
        (9, 0),
        (9, 10),
        (9, 3),
        (9, 4),
        (9, 7),
    }


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202321.part1(example1, 6) == 16


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc202321.part2(example2, 16) == 288
