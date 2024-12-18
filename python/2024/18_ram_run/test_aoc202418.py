"""Tests for AoC 18, 2024: RAM Run."""

# Standard library imports
import pathlib

# Third party imports
import aoc202418
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202418.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        (5, 4),
        (4, 2),
        (4, 5),
        (3, 0),
        (2, 1),
        (6, 3),
        (2, 4),
        (1, 5),
        (0, 6),
        (3, 3),
        (2, 6),
        (5, 1),
        (1, 2),
        (5, 5),
        (2, 5),
        (6, 5),
        (1, 4),
        (0, 4),
        (6, 4),
        (1, 1),
        (6, 1),
        (1, 0),
        (0, 5),
        (1, 6),
        (2, 0),
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202418.part1(example1, size=7, wait=12) == 22


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202418.part2(example1, size=7, wait=12) == "6,1"
