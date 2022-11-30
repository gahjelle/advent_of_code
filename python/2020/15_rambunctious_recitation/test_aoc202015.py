"""Tests for AoC 15, 2020: Rambunctious Recitation"""

# Standard library imports
import pathlib

# Third party imports
import aoc202015
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202015.parse_data(puzzle_input)


extra_input = [
    ([1, 3, 2], 1, 2578),
    ([2, 1, 3], 10, 3544142),
    ([1, 2, 3], 27, 261214),
    ([2, 3, 1], 78, 6895259),
    ([3, 2, 1], 438, 18),
    ([3, 1, 2], 1836, 362),
]


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [0, 3, 6]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc202015.part1(example1) == 436


@pytest.mark.skip(reason="slow")
def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc202015.part2(example1) == 175_594


@pytest.mark.parametrize(["puzzle_input", "part1", "_part2"], extra_input)
def test_part1_extra_input(puzzle_input, part1, _part2):
    """Test part 1 on extra input"""
    assert aoc202015.part1(puzzle_input) == part1


@pytest.mark.skip(reason="slow")
@pytest.mark.parametrize(["puzzle_input", "_part1", "part2"], extra_input)
def test_part2_extra_input(puzzle_input, _part1, part2):
    """Test part 2 on extra input"""
    assert aoc202015.part2(puzzle_input) == part2
