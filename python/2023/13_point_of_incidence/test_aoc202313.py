"""Tests for AoC 13, 2023: Point of Incidence."""

# Standard library imports
import pathlib

# Third party imports
import aoc202313
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202313.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202313.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        {
            (3, 1),
            (4, 9),
            (2, 5),
            (1, 3),
            (2, 8),
            (7, 1),
            (6, 8),
            (4, 2),
            (3, 9),
            (5, 6),
            (5, 3),
            (1, 8),
            (6, 4),
            (7, 3),
            (6, 7),
            (7, 6),
            (3, 2),
            (4, 1),
            (5, 5),
            (5, 8),
            (1, 1),
            (1, 4),
            (2, 3),
            (1, 7),
            (2, 6),
            (7, 5),
            (6, 3),
            (7, 8),
        },
        {
            (3, 4),
            (4, 3),
            (3, 7),
            (5, 4),
            (5, 1),
            (5, 7),
            (1, 6),
            (1, 9),
            (7, 1),
            (6, 8),
            (4, 2),
            (4, 5),
            (3, 3),
            (3, 9),
            (4, 8),
            (5, 3),
            (2, 1),
            (1, 5),
            (6, 4),
            (7, 9),
            (6, 7),
            (7, 6),
            (4, 1),
            (4, 7),
            (5, 2),
            (4, 4),
            (3, 8),
            (5, 5),
            (5, 8),
            (1, 1),
            (2, 9),
            (2, 6),
            (6, 3),
            (6, 9),
        },
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202313.part1(example1) == 405


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202313.part2(example1) == 400
