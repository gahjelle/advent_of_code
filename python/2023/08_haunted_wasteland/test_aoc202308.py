"""Tests for AoC 8, 2023: Haunted Wasteland."""

# Standard library imports
import pathlib

# Third party imports
import aoc202308
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202308.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202308.parse_data(puzzle_input)


@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().rstrip()
    return aoc202308.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    path, nodes = example1
    assert path == [1, 0]
    assert nodes == {
        "AAA": ("BBB", "CCC"),
        "BBB": ("DDD", "EEE"),
        "CCC": ("ZZZ", "GGG"),
        "DDD": ("DDD", "DDD"),
        "EEE": ("EEE", "EEE"),
        "GGG": ("GGG", "GGG"),
        "ZZZ": ("ZZZ", "ZZZ"),
    }


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202308.part1(example1) == 2


def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc202308.part1(example2) == 6


def test_part2_example3(example3):
    """Test part 2 on example input."""
    assert aoc202308.part2(example3) == 6
