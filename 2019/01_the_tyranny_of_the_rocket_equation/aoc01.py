"""The Tyranny of the Rocket Equation

Advent of Code 2019, day 1
Solution by Geir Arne Hjelle, 2019-12-01
"""
import sys


def fuel(mass):
    """Calculate fuel based on mass"""
    return max(mass // 3 - 2, 0)


def recursive_fuel(mass):
    """Calculate fuel based on mass, include fuel to cover mass of fuel"""
    return 0 if (fuel := mass // 3 - 2) <= 0 else fuel + recursive_fuel(fuel)


def main():
    for filename in sys.argv[1:]:
        if filename.startswith("--"):
            continue

        print(f"\n{filename}:")

        # Part 1
        with open(filename, mode="r") as fid:
            total_fuel = sum(fuel(int(line)) for line in fid)
        print(f"Total fuel:  {total_fuel}")

        # Part 2
        with open(filename, mode="r") as fid:
            rec_fuel = sum(recursive_fuel(int(line)) for line in fid)
        print(f"Total fuel, including fuel for fuel:  {rec_fuel}")


if __name__ == "__main__":
    debug = print if "--debug" in sys.argv else lambda *_: None
    main()
