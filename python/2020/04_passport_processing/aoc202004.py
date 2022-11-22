"""AoC 4, 2020: Passport Processing"""

# Standard library imports
import pathlib
import re
import sys

VALIDATORS = {}


def register_validator(func):
    """Decorator to register field validators"""
    VALIDATORS[func.__name__] = func
    return func


def parse(puzzle_input):
    """Parse input"""
    return [
        dict(field.split(":") for field in passport.split())
        for passport in puzzle_input.split("\n\n")
    ]


def part1(data):
    """Solve part 1"""
    return sum(not (set(VALIDATORS) - set(passport)) for passport in data)


def part2(data):
    """Solve part 2"""
    return sum(
        all(
            validate(passport[field]) if field in passport else False
            for field, validate in VALIDATORS.items()
        )
        for passport in data
    )


@register_validator
def byr(value):
    """byr (Birth Year) - four digits; at least 1920 and at most 2002

    ## Examples:

    >>> byr("1977")
    True
    >>> byr("1919")
    False
    """
    return 1920 <= int(value) <= 2002


@register_validator
def iyr(value):
    """iyr (Issue Year) - four digits; at least 2010 and at most 2020

     ## Examples:

    >>> iyr("2020")
    True
    >>> iyr("2006")
    False
    """
    return 2010 <= int(value) <= 2020


@register_validator
def eyr(value):
    """eyr (Expiration Year) - four digits; at least 2020 and at most 2030

    ## Examples:

    >>> eyr("2022")
    True
    >>> eyr("2034")
    False
    """
    return 2020 <= int(value) <= 2030


@register_validator
def hgt(value):
    """hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.

    ## Examples:

    >>> hgt("174cm")
    True
    >>> hgt("272cm")
    False
    >>> hgt("69in")
    True
    >>> hgt("23in")
    False
    """
    match = re.match(r"^(?P<number>\d+)(?P<unit>cm|in)", value)
    if not match:
        return False

    parsed = match.groupdict()
    if parsed["unit"] == "cm":
        return 150 <= int(parsed["number"]) <= 193
    else:
        return 59 <= int(parsed["number"]) <= 76


@register_validator
def hcl(value):
    """hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f

    ## Examples:

    >>> hcl("#c0ffee")
    True
    >>> hcl("brown")
    False
    """
    return bool(re.match(r"^#[0-9a-f]{6}$", value))


@register_validator
def ecl(value):
    """ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.

    ## Examples:

    >>> ecl("brn")
    True
    >>> ecl("eye")
    False
    """
    return value in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


@register_validator
def pid(value):
    """pid (Passport ID) - a nine-digit number, including leading zeroes.

    ## Examples:
    >>> pid("123456789")
    True
    >>> pid("76141806")
    False
    """
    return bool(re.match("^[0-9]{9}$", value))


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
