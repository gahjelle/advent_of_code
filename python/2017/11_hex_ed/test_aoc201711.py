"""Tests for AoC 11, 2017: Hex Ed"""

# Standard library imports
import pathlib

# Third party imports
import aoc201711
import numpy as np
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201711.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc201711.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert np.allclose(
        example1,
        np.array(
            [
                [-1, 0, 1],  # se
                [0, 1, -1],  # sw
                [-1, 0, 1],  # se
                [0, 1, -1],  # sw
                [0, 1, -1],  # sw
            ]
        ),
    )


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc201711.part1(example1) == 3


def test_part1_example2(example2):
    """Test part 1 on example input"""
    assert aoc201711.part1(example2) == 0


def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc201711.part2(example2) == 2
