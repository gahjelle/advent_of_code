"""Tests for AoC 21, 2017: Fractal Art."""

# Standard library imports
import pathlib

# Third party imports
import aoc201721
import numpy as np
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201721.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc201721.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert np.allclose(
        example1[(2, 1, 1, 2, 2, 4, 4, 8, 8)],
        np.array([[1, 1, 0], [1, 0, 0], [0, 0, 0]]),
    )
    assert np.allclose(
        example1[(3, 107, 143, 167, 233, 302, 428, 458, 482)],
        np.array([[1, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1]]),
    )


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201721.part1(example1, num_iterations=2) == 12
