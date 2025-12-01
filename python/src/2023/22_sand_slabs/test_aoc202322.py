"""Tests for AoC 22, 2023: Sand Slabs."""

# Standard library imports
import pathlib

# Third party imports
import aoc202322
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202322.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    num_bricks, supports, is_supported = example1
    assert num_bricks == 7
    assert supports == {0: {1, 2}, 1: {3, 4}, 2: {3, 4}, 3: {5}, 4: {5}, 5: {6}}
    assert is_supported == {1: {0}, 2: {0}, 3: {1, 2}, 4: {1, 2}, 5: {3, 4}, 6: {5}}


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202322.part1(example1) == 5


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202322.part2(example1) == 7
