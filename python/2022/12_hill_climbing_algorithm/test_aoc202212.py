"""Tests for AoC 12, 2022: Hill Climbing Algorithm."""

# Standard library imports
import pathlib

# Third party imports
import aoc202212
import numpy as np
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202212.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    asserts = example1 == np.array(
        [
            [-1, 1, 2, 17, 16, 15, 14, 13],
            [1, 2, 3, 18, 25, 24, 24, 12],
            [1, 3, 3, 19, 26, -26, 24, 11],
            [1, 3, 3, 20, 21, 22, 23, 10],
            [1, 2, 4, 5, 6, 7, 8, 9],
        ]
    )
    assert np.all(asserts)


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202212.part1(example1) == 31


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202212.part2(example1) == 29
