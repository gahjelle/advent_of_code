# Standard library imports
import pathlib
import sys


def solve(puzzle_input):
    data = [
        [int(xyz) for xyz in line.split()[2][3:-1].split(",")]
        for line in puzzle_input.split("\n")
    ]
    min_acc = min(abs(x) + abs(y) + abs(z) for x, y, z in data)
    return [
        idx for idx, (x, y, z) in enumerate(data) if abs(x) + abs(y) + abs(z) == min_acc
    ]


# 279: p=<-1103,92,1785>, v=<49,-4,-97>, a=<1,0,0>
#      x: -1103 + 49t + t²
#      y: 92 - 4t
#      z: 1785 - 97t         => d/t ~ (49 + 4 + 97) + t = 150 + t
#
# 308: p=<2978,2082,4280>, v=<-135,-88,-178>, a=<1,0,0>
#      x: 2978 - 135t + t²
#      y: 2082 - 88t
#      z: 4280 - 178t        => d/t ~ (-135 + 88 + 178) + t = 131 + t
#
# 435: p=<2030,-4343,-355>, v=<-69,145,25>, a=<0,0,-1>
#      x: 2030 - 69t
#      y: -4343 + 145t
#      z: -355 + 25t - t²    => d/t ~ (69 + 145 - 25) + t = 189 + t

if __name__ == "__main__":
    for path in [pathlib.Path(arg) for arg in sys.argv[1:]]:
        print(solve(path.read_text(encoding="utf-8")))
