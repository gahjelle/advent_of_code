"""Tests for AoC 22, 2022: Monkey Map."""

# Standard library imports
import pathlib

# Third party imports
import aoc202222
import numpy as np
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202222.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    map, path = example1
    assert np.allclose(
        map,
        np.array(
            [
                [2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 0, 2, 2, 2, 2],
                [2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 1, 2, 2, 2, 2],
                [2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 1, 1, 2, 2, 2, 2],
                [2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2],
                [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2],
                [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 2, 2, 2, 2],
                [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 2, 2, 2, 2],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2, 2, 2, 2],
                [2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 0, 1, 1, 1, 1],
                [2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0, 1, 1],
                [2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 1, 1, 1, 1, 1],
                [2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 0, 1],
            ]
        ),
    )
    assert path == [
        ("RIGHT", 10),
        ("RIGHT", 5),
        ("LEFT", 5),
        ("RIGHT", 10),
        ("LEFT", 4),
        ("RIGHT", 5),
        ("LEFT", 5),
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202222.part1(example1) == 6032


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202222.part2(example1) == 5031
