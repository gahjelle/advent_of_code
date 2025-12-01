"""Tests for AoC 12, 2019: The N-Body Problem."""

# Standard library imports
import pathlib

# Third party imports
import aoc201912
import pytest
from aoc201912 import Moon

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201912.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc201912.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        Moon(x=-1, y=0, z=2, vx=0, vy=0, vz=0),
        Moon(x=2, y=-10, z=-7, vx=0, vy=0, vz=0),
        Moon(x=4, y=-8, z=8, vx=0, vy=0, vz=0),
        Moon(x=3, y=5, z=-1, vx=0, vy=0, vz=0),
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201912.part1(example1, num_steps=10) == 179


def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc201912.part1(example2, num_steps=100) == 1940


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201912.part2(example1) == 2772


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc201912.part2(example2) == 4_686_774_924
