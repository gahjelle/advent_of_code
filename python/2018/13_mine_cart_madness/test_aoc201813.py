"""Tests for AoC 13, 2018: Mine Cart Madness."""

# Standard library imports
import pathlib

# Third party imports
import aoc201813
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201813.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc201813.parse_data(puzzle_input)


@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().rstrip()
    return aoc201813.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    track, carts = example1
    assert track == {
        0j: "/",
        -1j: "v",
        -2j: "|",
        -3j: "|",
        -4j: "|",
        -5j: "^",
        -6j: "\\",
        (1 - 6j): "-",
        (2 - 6j): "/",
        (2 - 5j): "|",
        (2 - 4j): "|",
        (2 - 3j): "|",
        (2 - 2j): "|",
        (2 - 1j): "|",
        (2 + 0j): "\\",
        (1 + 0j): "-",
    }
    assert carts == [(-1j, -1j), (-5j, 1j)]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201813.part1(example1) == "0,3"


def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc201813.part1(example2) == "7,3"


def test_part1_example3(example3):
    """Test part 1 on example input."""
    assert aoc201813.part1(example3) == "2,0"


def test_part2_example3(example3):
    """Test part 2 on example input."""
    assert aoc201813.part2(example3) == "6,4"
