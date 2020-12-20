"""Balance Bots

Advent of Code 2016, day 10
Solution by Geir Arne Hjelle, 2016-12-10
"""

# Standard library imports
import pathlib
import sys

debug = print if "--debug" in sys.argv else lambda *_: None

MICROCHIPS = dict(bot=dict(), output=dict())


def add(value, target, name):
    if target == "bot":
        add_to_bot(name, value)
    else:
        MICROCHIPS["output"].setdefault(name, list()).append(value)


def add_to_bot(bot, value):
    MICROCHIPS["bot"].setdefault(bot, dict()).setdefault("all", list()).append(value)
    if len(MICROCHIPS["bot"][bot]["all"]) >= 2:
        MICROCHIPS["bot"][bot]["low"] = min(MICROCHIPS["bot"][bot]["all"])
        MICROCHIPS["bot"][bot]["high"] = max(MICROCHIPS["bot"][bot]["all"])


def give_microchips(instructions):
    for bot, (low, high) in instructions.copy().items():
        if bot in MICROCHIPS["bot"] and "low" in MICROCHIPS["bot"][bot]:
            chip = MICROCHIPS["bot"][bot]
            if chip["low"] == 17 and chip["high"] == 61:
                print(
                    f"Bot {bot} gives {chip['low']}-chip to {low[0]} {low[1]} and "
                    f"{chip['high']}-chip to {high[0]} {high[1]}"
                )
            add(MICROCHIPS["bot"][bot]["low"], *low)
            add(MICROCHIPS["bot"][bot]["high"], *high)
            del instructions[bot]


def parse_instructions(instructions):
    give_instructions = dict()
    for instruction in instructions:
        tokens = instruction.split()
        if instruction.startswith("value"):
            value, bot = int(tokens[1]), int(tokens[5])
            add_to_bot(bot, value)
        else:
            give_instructions[int(tokens[1])] = (
                (tokens[5], int(tokens[6])),
                (tokens[10], int(tokens[11])),
            )

    return give_instructions


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    with file_path.open(mode="r") as fid:
        instructions = parse_instructions(i.strip() for i in fid)

    while instructions:
        give_microchips(instructions)

    outputs = [v[0] for k, v in sorted(MICROCHIPS["output"].items())]
    print(
        f"The first three outputs are {outputs[0]}, {outputs[1]} and {outputs[2]}. "
        f"Their product is {outputs[0] * outputs[1] * outputs[2]}"
    )


if __name__ == "__main__":
    main(sys.argv[1:])
