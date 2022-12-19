"""Tests for AoC 19, 2022: Not Enough Minerals."""

# Standard library imports
import pathlib

# Third party imports
import aoc202219
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202219.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202219.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == {
        1: ((4, 0, 0, 0), (2, 0, 0, 0), (3, 14, 0, 0), (2, 0, 7, 0)),
        2: ((2, 0, 0, 0), (3, 0, 0, 0), (3, 8, 0, 0), (3, 0, 12, 0)),
    }


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202219.part1(example1) == 1 * 9 + 2 * 12


@pytest.mark.skip(reason="slow")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202219.part2(example1, ids=(2,)) == 62
