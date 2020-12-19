"""Inverse Captcha

Advent of Code 2017, day 1
Solution by Geir Arne Hjelle, 2017-12-01
"""
# Standard library imports
import sys


def calculate_next_captcha(line):
    digits = line + line[0]
    return sum(int(a) for a, b in zip(digits[:-1], digits[1:]) if a == b)


def calculate_halfway_captcha(line):
    num_dig = len(line)
    digits = line * 2
    return sum(
        int(a) for a, b in zip(digits[:num_dig], digits[num_dig // 2 :]) if a == b
    )


def main(args):
    for filename in args:
        print(f"\n{filename}:")
        with open(filename, mode="r") as fid:
            for line in fid:
                digits = line.strip()
                digits_repr = digits if len(digits) < 9 else digits[:6] + "..."
                next_captcha = calculate_next_captcha(digits)
                halfway_captcha = calculate_halfway_captcha(digits)
                print(f"{digits_repr:<10} {next_captcha:6d} {halfway_captcha:6d}")


if __name__ == "__main__":
    main(sys.argv[1:])
