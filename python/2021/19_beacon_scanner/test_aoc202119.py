"""Tests for AoC 19, 2021: Beacon Scanner"""

# Standard library imports
import pathlib

# Third party imports
import aoc202119
import numpy as np
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202119.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202119.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert len(example1) == 2
    assert np.allclose(
        example1[0],
        np.array(
            [
                [0, 2, 0],
                [4, 1, 0],
                [3, 3, 0],
            ]
        ),
    )
    assert np.allclose(
        example1[1],
        np.array(
            [
                [-1, -1, 0],
                [-5, 0, 0],
                [-2, 1, 0],
            ]
        ),
    )


def test_part1_example2(example2):
    """Test part 1 on example input"""
    assert aoc202119.part1(example2) == 79


def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc202119.part2(example2) == 3621
