"""Tests for AoC 20, 2017: Particle Swarm."""

# Standard library imports
import pathlib

# Third party imports
import aoc201720
import pytest
from aoc201720 import XYZ, Particle

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201720.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc201720.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        Particle(pos=XYZ(3, 0, 0), vel=XYZ(2, 0, 0), acc=XYZ(-1, 0, 0)),
        Particle(pos=XYZ(4, 0, 0), vel=XYZ(0, 0, 0), acc=XYZ(-2, 0, 0)),
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201720.part1(example1) == 0


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201720.part2(example1) == 2


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc201720.part2(example2) == 1
