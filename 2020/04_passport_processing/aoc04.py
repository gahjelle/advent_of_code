"""Passport Processing

Advent of Code 2020, day 4
Solution by Geir Arne Hjelle, 2020-12-04
"""
# Standard library imports
import pathlib
import re
import sys

debug = print if "--debug" in sys.argv else lambda *_: None


def byr(value):
    """byr (Birth Year) - four digits; at least 1920 and at most 2002"""
    return 1920 <= int(value) <= 2002


def iyr(value):
    """iyr (Issue Year) - four digits; at least 2010 and at most 2020"""
    return 2010 <= int(value) <= 2020


def eyr(value):
    """eyr (Expiration Year) - four digits; at least 2020 and at most 2030"""
    return 2020 <= int(value) <= 2030


def hgt(value):
    """hgt (Height) - a number followed by either cm or in:

    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    """
    match = re.match(r"^(?P<number>\d+)(?P<unit>cm|in)", value)
    if not match:
        return False

    parsed = match.groupdict()
    if parsed["unit"] == "cm":
        return 150 <= int(parsed["number"]) <= 193
    else:
        return 59 <= int(parsed["number"]) <= 76


def hcl(value):
    """hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f"""
    return bool(re.match(r"^#[0-9a-f]{6}$", value))


def ecl(value):
    """ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth."""
    return value in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def pid(value):
    """pid (Passport ID) - a nine-digit number, including leading zeroes."""
    return bool(re.match("^[0-9]{9}$", value))


required = {
    "byr": byr,
    "iyr": iyr,
    "eyr": eyr,
    "hgt": hgt,
    "hcl": hcl,
    "ecl": ecl,
    "pid": pid,
}


def parse_passport(text):
    """Parse one passport"""
    return dict(f.split(":") for f in text.split())


def is_valid_1(passport):
    """Check that all required fields are present"""
    return not (set(required) - set(passport))


def is_valid_2(passport):
    """Check that all required fields satisfy extra conditions"""
    for field in required:
        if field not in passport:
            return False

        if not required[field](value=passport[field]):
            return False

    return True


def main(args):
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        print(f"\n{file_path}:")
        passports = [parse_passport(pp) for pp in file_path.read_text().split("\n\n")]

        # Part 1
        num_valid = sum(is_valid_1(pp) for pp in passports)
        print(f"{num_valid} passports have all required fields")

        # Part 2
        num_valid = sum(is_valid_2(pp) for pp in passports)
        print(f"{num_valid} passports satisfy all requirements")


if __name__ == "__main__":
    main(sys.argv[1:])
