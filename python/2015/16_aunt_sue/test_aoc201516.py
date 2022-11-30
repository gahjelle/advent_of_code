"""Tests for AoC 16, 2015: Aunt Sue."""

# Standard library imports
import pathlib

# Third party imports
import aoc201516
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201516.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc201516.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == {
        1: {"children": 1, "cars": 8, "vizslas": 7},
        2: {"children": 3, "goldfish": 5, "vizslas": 0},
        3: {"akitas": 10, "perfumes": 10, "children": 5},
        4: {"vizslas": 4, "akitas": 7, "cars": 9},
        5: {"perfumes": 1, "trees": 6, "goldfish": 0},
    }


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201516.part1(example1) == 2


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201516.part2(example1) == 5
