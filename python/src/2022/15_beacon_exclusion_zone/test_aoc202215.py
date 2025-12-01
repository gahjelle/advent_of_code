"""Tests for AoC 15, 2022: Beacon Exclusion Zone."""

# Standard library imports
import pathlib

# Third party imports
import aoc202215
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202215.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        (2, 18, -2, 15, 7, -23, 13, -9, 27),
        (9, 16, 10, 16, 1, -8, 24, -6, 26),
        (13, 2, 15, 3, 3, 8, 12, 14, 18),
        (12, 14, 10, 16, 4, -6, 22, 2, 30),
        (10, 20, 10, 16, 4, -14, 26, -6, 34),
        (14, 17, 10, 16, 5, -8, 26, 2, 36),
        (8, 7, 2, 10, 9, -8, 6, 10, 24),
        (2, 0, 2, 10, 10, -8, -8, 12, 12),
        (0, 11, 2, 10, 3, -14, 8, -8, 14),
        (20, 14, 25, 17, 8, -2, 26, 14, 42),
        (17, 20, 21, 22, 6, -9, 31, 3, 43),
        (16, 7, 15, 3, 5, 4, 18, 14, 28),
        (14, 3, 15, 3, 1, 10, 16, 12, 18),
        (20, 1, 15, 3, 7, 12, 14, 26, 28),
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202215.part1(example1, row=10) == 26


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202215.part2(example1) == 56_000_011


def test_slowpart2_example1(example1):
    """Test slow implementation of part 2 on example input."""
    assert aoc202215.slow_part2(example1, rows=20) == 56_000_011
