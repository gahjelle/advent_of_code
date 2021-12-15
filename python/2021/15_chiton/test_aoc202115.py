"""Tests for AoC 15, 2021: Chiton"""

# Standard library imports
import pathlib

# Third party imports
import aoc202115
import numpy as np
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202115.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert np.all(
        example1
        == np.array(
            [
                [1, 1, 6, 3, 7, 5, 1, 7, 4, 2],
                [1, 3, 8, 1, 3, 7, 3, 6, 7, 2],
                [2, 1, 3, 6, 5, 1, 1, 3, 2, 8],
                [3, 6, 9, 4, 9, 3, 1, 5, 6, 9],
                [7, 4, 6, 3, 4, 1, 7, 1, 1, 1],
                [1, 3, 1, 9, 1, 2, 8, 1, 3, 7],
                [1, 3, 5, 9, 9, 1, 2, 4, 2, 1],
                [3, 1, 2, 5, 4, 2, 1, 6, 3, 9],
                [1, 2, 9, 3, 1, 3, 8, 5, 2, 1],
                [2, 3, 1, 1, 9, 4, 4, 5, 8, 1],
            ]
        )
    )


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc202115.part1(example1) == 40


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc202115.part2(example1) == 315
