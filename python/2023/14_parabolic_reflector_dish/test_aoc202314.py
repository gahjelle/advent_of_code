"""Tests for AoC 14, 2023: Parabolic Reflector Dish."""

# Standard library imports
import pathlib

# Third party imports
import aoc202314
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202314.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    rolling, obstacles = example1
    assert rolling == {
        (6, 2),
        (1, 2),
        (5, 5),
        (3, 4),
        (7, 7),
        (0, 0),
        (3, 1),
        (4, 1),
        (6, 9),
        (6, 6),
        (9, 2),
        (3, 0),
        (3, 9),
        (5, 0),
        (1, 0),
        (9, 1),
        (1, 3),
        (4, 7),
    }
    assert obstacles == {
        (9, 0),
        (6, 5),
        (8, 7),
        (1, 4),
        (5, 7),
        (8, 0),
        (8, 5),
        (9, 5),
        (3, 3),
        (2, 6),
        (0, 5),
        (4, 8),
        (8, 6),
        (5, 9),
        (2, 5),
        (1, 9),
        (5, 2),
    }


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202314.part1(example1) == 136


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202314.part2(example1) == 64
