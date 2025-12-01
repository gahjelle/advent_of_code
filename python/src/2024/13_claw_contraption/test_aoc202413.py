"""Tests for AoC 13, 2024: Claw Contraption."""

# Standard library imports
import pathlib

# Third party imports
import aoc202413
import pytest
from aoc202413 import Coordinate

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202413.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        [Coordinate(x=94, y=34), Coordinate(x=22, y=67), Coordinate(x=8400, y=5400)],
        [Coordinate(x=26, y=66), Coordinate(x=67, y=21), Coordinate(x=12748, y=12176)],
        [Coordinate(x=17, y=86), Coordinate(x=84, y=37), Coordinate(x=7870, y=6450)],
        [Coordinate(x=69, y=23), Coordinate(x=27, y=71), Coordinate(x=18641, y=10279)],
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202413.part1(example1) == 480


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202413.part2(example1) == 875_318_608_908
