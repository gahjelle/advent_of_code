"""Tests for AoC 9, 2021: Smoke Basin."""

# Standard library imports
import pathlib

# Third party imports
import aoc202109
import numpy as np
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202109.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert np.all(
        example1
        == np.array(
            [
                [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
                [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
                [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
                [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
                [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
            ]
        )
    )


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202109.part1(example1) == 15


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202109.part2(example1) == 1134
