"""Tests for AoC 21, 2024: Keypad Conundrum."""

# Standard library imports
import pathlib

# Third party imports
import aoc202421
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202421.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    codes, _number_pad, arrow_pad = example1
    assert codes == ["029", "980", "179", "456", "379"]
    assert arrow_pad == {
        ("^", "^"): ["A"],
        ("^", "<"): ["v<A"],
        ("^", ">"): [">vA", "v>A"],
        ("^", "A"): [">A"],
        ("^", "v"): ["vA"],
        ("<", "^"): [">^A"],
        ("<", "<"): ["A"],
        ("<", ">"): [">>A"],
        ("<", "A"): [">^>A", ">>^A"],
        ("<", "v"): [">A"],
        (">", "^"): ["^<A", "<^A"],
        (">", "<"): ["<<A"],
        (">", ">"): ["A"],
        (">", "A"): ["^A"],
        (">", "v"): ["<A"],
        ("A", "^"): ["<A"],
        ("A", "<"): ["v<<A", "<v<A"],
        ("A", ">"): ["vA"],
        ("A", "A"): ["A"],
        ("A", "v"): ["v<A", "<vA"],
        ("v", "^"): ["^A"],
        ("v", "<"): ["<A"],
        ("v", ">"): [">A"],
        ("v", "A"): ["^>A", ">^A"],
        ("v", "v"): ["A"],
    }


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202421.part1(example1) == 126_384


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202421.part2(example1) == 154_115_708_116_294
