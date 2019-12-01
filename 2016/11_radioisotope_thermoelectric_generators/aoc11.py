"""Radioisotope Thermoelectric Generators

Advent of Code 2016, day 11
Solution by Geir Arne Hjelle, 2016-12-11
"""
import itertools
import re
import sys

DUPLICATES = set()
SYMMETRIC_MAPS = list()


def read_starting_position(fid):
    re_generators = re.compile(r"a (\w+) generator")
    re_microchips = re.compile(r"a (\w+)-compatible microchip")

    position = list()
    for line in fid:
        floor = [g[:2].title() + "G" for g in re_generators.findall(line)] + [
            m[:2].title() + "M" for m in re_microchips.findall(line)
        ]
        position.append(floor)

    return (0, position)


def find_shortest_path(position):
    setup_symmetric_maps(position)
    positions = [position]
    for num_moves in itertools.count(1):
        positions = next_positions(positions)
        positions = remove_duplicates(positions)
        print("Move {:3d}, {:6d} possible positions".format(num_moves, len(positions)))

        if any(is_done(p) for p in positions):
            return num_moves


def next_positions(positions):
    new_positions = list()
    for position in positions:
        for new_position in generate_positions(position):
            if is_valid(new_position):
                new_positions.append(new_position)

    return new_positions


def generate_positions(position):
    elevator, floors = position

    if elevator + 1 < len(floors):
        # Move 1 object up
        for thing in floors[elevator]:
            new_floors = [f.copy() for f in floors]
            new_floors[elevator].remove(thing)
            new_floors[elevator + 1].append(thing)
            yield elevator + 1, new_floors

        # Move 2 objects up
        for things in itertools.combinations(floors[elevator], 2):
            new_floors = [f.copy() for f in floors]
            new_floors[elevator].remove(things[0])
            new_floors[elevator].remove(things[1])
            new_floors[elevator + 1] += things
            yield elevator + 1, new_floors

    if elevator > 0:
        # Move 1 object down
        for thing in floors[elevator]:
            new_floors = [f.copy() for f in floors]
            new_floors[elevator].remove(thing)
            new_floors[elevator - 1].append(thing)
            yield elevator - 1, new_floors

        # Move 2 objects down
        for things in itertools.combinations(floors[elevator], 2):
            new_floors = [f.copy() for f in floors]
            new_floors[elevator].remove(things[0])
            new_floors[elevator].remove(things[1])
            new_floors[elevator - 1] += things
            yield elevator - 1, new_floors


def is_valid(position):
    elevator, floors = position

    if not (0 <= elevator < len(floors)):
        return False

    for floor in floors:
        for chip in [o for o in floor if o.endswith("M")]:
            if not chip[:2] + "G" in floor and [o for o in floor if o.endswith("G")]:
                return False

    return True


def remove_duplicates(positions):
    unique_positions = list()
    for position in positions:
        description = describe_position(position)
        if description not in DUPLICATES:
            for sym_map in SYMMETRIC_MAPS:
                DUPLICATES.add(describe_position(position, map=sym_map.get))
            unique_positions.append(position)

    #    for i, d in enumerate(DUPLICATES):
    #        print(str(i) + '\n' + d, end='\n\n')
    return unique_positions


def is_done(position):
    for floor in position[1][:-1]:
        if floor:
            return False
    return True


def setup_symmetric_maps(position):
    for m in range(len(SYMMETRIC_MAPS)):
        SYMMETRIC_MAPS.pop()

    all_names = sorted(n[:2] for f in position[1] for n in f if n.endswith("G"))
    for perm_names in itertools.permutations(all_names):
        SYMMETRIC_MAPS.append({k + "G": v + "G" for k, v in zip(all_names, perm_names)})
        SYMMETRIC_MAPS[-1].update(
            {k + "M": v + "M" for k, v in zip(all_names, perm_names)}
        )


def describe_position(position, map=lambda x: x):
    all_names = sorted(n for f in position[1] for n in f)
    num_floors = len(position[1])
    floor_txt = list()
    for idx, floor in enumerate(position[1][::-1]):
        floor_num = num_floors - idx
        floor_txt.append(
            "{}: {} {}".format(
                floor_num,
                "E" if position[0] == floor_num - 1 else ".",
                " ".join(
                    n if n in [map(f) for f in floor] else "..." for n in all_names
                ),
            )
        )
    return "\n".join(floor_txt)


def main():
    for filename in sys.argv[1:]:
        print("\n{}:".format(filename))
        with open(filename, mode="r") as fid:
            position = read_starting_position(fid)

        # Part one
        print("Starting position\n{}".format(describe_position(position)))
        print("Can be completed in {} moves".format(find_shortest_path(position)))

        # Part two
        position[1][0] += ["ElG", "ElM", "DiG", "DiM"]
        print("Starting position\n{}".format(describe_position(position)))
        print("Can be completed in {} moves".format(find_shortest_path(position)))


if __name__ == "__main__":
    main()
