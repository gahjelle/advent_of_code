"""Tests for AoC 11, 2021: Dumbo Octopus"""

# Standard library imports
import pathlib

# Third party imports
import aoc202111
import pytest
import numpy as np

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202111.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert np.all(
        example1
        == np.array(
            [
                [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
                [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
                [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
                [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
                [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
                [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
                [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
                [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
                [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
                [5, 2, 8, 3, 7, 5, 1, 5, 2, 6],
            ]
        )
    )


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc202111.part1(example1) == 1656


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc202111.part2(example1) == 195
