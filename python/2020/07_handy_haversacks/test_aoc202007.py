"""Tests for AoC 7, 2020: Handy Haversacks."""

# Standard library imports
import pathlib

# Third party imports
import aoc202007
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202007.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202007.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == (
        ("light red", (("bright white", 1), ("muted yellow", 2))),
        ("dark orange", (("bright white", 3), ("muted yellow", 4))),
        ("bright white", (("shiny gold", 1),)),
        ("muted yellow", (("shiny gold", 2), ("faded blue", 9))),
        ("shiny gold", (("dark olive", 1), ("vibrant plum", 2))),
        ("dark olive", (("faded blue", 3), ("dotted black", 4))),
        ("vibrant plum", (("faded blue", 5), ("dotted black", 6))),
        ("faded blue", ()),
        ("dotted black", ()),
    )


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202007.part1(example1) == 4


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202007.part2(example1) == 32


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc202007.part2(example2) == 126
