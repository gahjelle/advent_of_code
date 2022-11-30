"""Tests for AoC 3, 2021: Binary Diagnostic"""

# Standard library imports
import pathlib

# Third party imports
import aoc202103
import numpy as np
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202103.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert np.allclose(
        np.array(example1),
        np.array(
            [
                [0, 0, 1, 0, 0],
                [1, 1, 1, 1, 0],
                [1, 0, 1, 1, 0],
                [1, 0, 1, 1, 1],
                [1, 0, 1, 0, 1],
                [0, 1, 1, 1, 1],
                [0, 0, 1, 1, 1],
                [1, 1, 1, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 1],
                [0, 0, 0, 1, 0],
                [0, 1, 0, 1, 0],
            ]
        ),
    )


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc202103.part1(example1) == 198


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc202103.part2(example1) == 230
