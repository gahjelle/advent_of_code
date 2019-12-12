"""The N-Body Problem

Advent of Code 2019, day 12
Solution by Geir Arne Hjelle, 2019-12-12
"""
from dataclasses import dataclass
import itertools
import pathlib
import sys

import numpy as np

debug = print if "--debug" in sys.argv else lambda *_: None


@dataclass
class Moon:
    x: int
    y: int
    z: int
    vx: int = 0
    vy: int = 0
    vz: int = 0

    @classmethod
    def from_str(cls, text):
        param_tpl = [
            p.partition("=") for p in text.strip("<>").replace(",", " ").split()
        ]
        params = {p[0]: int(p[2]) for p in param_tpl}
        return cls(**params)

    def apply_gravity(self, other):
        self.vx += 1 if self.x < other.x else -1 if self.x > other.x else 0
        self.vy += 1 if self.y < other.y else -1 if self.y > other.y else 0
        self.vz += 1 if self.z < other.z else -1 if self.z > other.z else 0

    def apply_velocity(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    @property
    def energy(self):
        pot = abs(self.x) + abs(self.y) + abs(self.z)
        kin = abs(self.vx) + abs(self.vy) + abs(self.vz)
        return pot * kin

    def get_hash(self, xyz):
        if xyz == "x":
            return f"{self.x}:{self.vx}"
        elif xyz == "y":
            return f"{self.y}:{self.vy}"
        elif xyz == "z":
            return f"{self.z}:{self.vz}"

    def copy(self):
        return self.__class__(
            **{f: getattr(self, f) for f in self.__dataclass_fields__}
        )


def simulate(moons, steps=None):
    seen = {"x": set(), "y": set(), "z": set()}
    step_num = 0
    while True:
        for moon_1, moon_2 in itertools.combinations(moons, 2):
            moon_1.apply_gravity(moon_2)
            moon_2.apply_gravity(moon_1)

        for moon in moons:
            moon.apply_velocity()

        if steps is None:
            # Check each axis independently
            for xyz, seen_xyz in seen.items():
                if isinstance(seen_xyz, int):
                    continue
                hash = "|".join(moon.get_hash(xyz) for moon in moons)
                if hash in seen_xyz:
                    debug(f"Moons repeat their {xyz}-coordinate at step {step_num}")
                    seen[xyz] = step_num

                    if all(isinstance(v, int) for v in seen.values()):
                        return seen
                seen_xyz.add(hash)

        elif step_num >= steps - 1:
            break

        step_num += 1

    return moons


def main(args):
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        print(f"\n{file_path}:")
        moons = [Moon.from_str(ln) for ln in file_path.read_text().strip().split("\n")]

        # Part 1
        steps = 1000
        part_1 = simulate([m.copy() for m in moons], steps=steps)
        energy = sum(moon.energy for moon in part_1)
        print(f"After {steps} steps, the total energy is {energy}")

        # Part 2
        part_2 = simulate([m.copy() for m in moons], steps=None)
        repeat_step = np.lcm.reduce(list(part_2.values()))
        print(f"Universe repeats at time step {repeat_step}")


if __name__ == "__main__":
    main(sys.argv[1:])
