"""Tests for AoC 24, 2017: Electromagnetic Moat."""

# Standard library imports
import pathlib

# Third party imports
import aoc201724
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201724.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == {
        0: [(2, (0, 2)), (1, (0, 1))],
        1: [(0, (0, 1)), (10, (10, 1))],
        2: [(2, (2, 2)), (0, (0, 2)), (3, (2, 3))],
        3: [(2, (2, 3)), (4, (3, 4)), (5, (3, 5))],
        4: [(3, (3, 4))],
        5: [(3, (3, 5))],
        9: [(10, (9, 10))],
        10: [(1, (10, 1)), (9, (9, 10))],
    }


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201724.part1(example1) == 31


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201724.part2(example1) == 19
