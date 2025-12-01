"""Tests for AoC 19, 2017: A Series of Tubes."""

# Standard library imports
import pathlib

# Third party imports
import aoc201719
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201719.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert aoc201719.TUBES[example1] == (
        {(0, 4): "s", (1, 4): "s", (1, 7): "t", (1, 8): "s", (1, 9): "s", (1, 10): "t"}
        | {(2, 4): "A", (2, 7): "s", (2, 10): "C", (3, 0): "F", (3, 1): "s"}
        | {(3, 2): "s", (3, 3): "s", (3, 4): "s", (3, 5): "s", (3, 6): "s"}
        | {(3, 7): "s", (3, 8): "s", (3, 9): "E", (3, 10): "s", (3, 11): "s"}
        | {(3, 12): "s", (3, 13): "t", (4, 4): "s", (4, 7): "s", (4, 10): "s"}
        | {(4, 13): "D", (5, 4): "t", (5, 5): "B", (5, 6): "s", (5, 7): "t"}
        | {(5, 10): "t", (5, 11): "s", (5, 12): "s", (5, 13): "t"}
    )


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201719.part1(example1) == "ABCDEF"


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201719.part2(example1) == 38
