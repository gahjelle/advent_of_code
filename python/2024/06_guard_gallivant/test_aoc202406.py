"""Tests for AoC 6, 2024: Guard Gallivant."""

# Standard library imports
import itertools
import pathlib

# Third party imports
import aoc202406
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202406.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    grid = (
        {col - row * 1j: "." for row, col in itertools.product(range(10), range(10))}
        | {pos: "#" for pos in [4, 9 - 1j, 2 - 3j, 7 - 4j, 1 - 6j, 8 - 7j, -8j, 6 - 9j]}
        | {4 - 6j: "^"}
    )
    assert example1 == grid


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202406.part1(example1) == 41


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202406.part2(example1) == 6
