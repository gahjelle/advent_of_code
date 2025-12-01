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
    (pat_1, rep_1), (pat_2, rep_2) = example1

    assert np.allclose(pat_1, np.array([[0, 0], [0, 1]]))
    assert np.allclose(rep_1, np.array([[1, 1, 0], [1, 0, 0], [0, 0, 0]]))
    assert np.allclose(pat_2, np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]]))
    assert np.allclose(
        rep_2, np.array([[1, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1]])
    )


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201721.part1(example1, num_iterations=2) == 12
