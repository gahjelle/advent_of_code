"""Tests for AoC 11, 2024: Plutonian Pebbles."""

# Standard library imports
import pathlib

# Third party imports
import aoc202411
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202411.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202411.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == {0: 1, 1: 1, 10: 1, 99: 1, 999: 1}


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202411.part1(example1, rounds=1) == 7
    assert aoc202411.part1(example1) == 125_681


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202411.part2(example1) == 149_161_030_616_311


def test_parts_example2(example2):
    """Test parts on example input."""
    assert aoc202411.part1(example2, rounds=1) == 3
    assert aoc202411.part1(example2, rounds=2) == 4
    assert aoc202411.part1(example2, rounds=3) == 5
    assert aoc202411.part1(example2, rounds=4) == 9
    assert aoc202411.part1(example2, rounds=5) == 13
    assert aoc202411.part1(example2, rounds=6) == 22
    assert aoc202411.part1(example2) == 55_312
    assert aoc202411.part2(example2) == 65_601_038_650_482
