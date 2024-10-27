# Advent of Code in Gleam

Solutions to [Advent of Code](https://adventofcode.com/) in [Gleam](https://gleam.run/) (32⭐):

|   Day | [2015](aoc/src/aoc_2015)                 | [2016](aoc/src/aoc_2016)                 | [2017](aoc/src/aoc_2017)                 | [2018](aoc/src/aoc_2018)                 | [2019](aoc/src/aoc_2019)                 | [2020](aoc/src/aoc_2020)                 | [2021](aoc/src/aoc_2021)                 | [2022](aoc/src/aoc_2022)                 |
|------:|:-----------------------------------------|:-----------------------------------------|:-----------------------------------------|:-----------------------------------------|:-----------------------------------------|:-----------------------------------------|:-----------------------------------------|:-----------------------------------------|
|     1 | [⭐⭐](aoc/src/aoc_2015/README_day_1.md) | [⭐⭐](aoc/src/aoc_2016/README_day_1.md) | [⭐⭐](aoc/src/aoc_2017/README_day_1.md) | [⭐⭐](aoc/src/aoc_2018/README_day_1.md) | [⭐⭐](aoc/src/aoc_2019/README_day_1.md) | [⭐⭐](aoc/src/aoc_2020/README_day_1.md) | [⭐⭐](aoc/src/aoc_2021/README_day_1.md) | [⭐⭐](aoc/src/aoc_2022/README_day_1.md) |
|     2 | [⭐⭐](aoc/src/aoc_2015/README_day_2.md) |                                          |                                          | [⭐⭐](aoc/src/aoc_2018/README_day_2.md) |                                          |                                          | [⭐⭐](aoc/src/aoc_2021/README_day_2.md) | [⭐⭐](aoc/src/aoc_2022/README_day_2.md) |
|     3 |                                          |                                          |                                          | [⭐⭐](aoc/src/aoc_2018/README_day_3.md) |                                          |                                          |                                          | [⭐⭐](aoc/src/aoc_2022/README_day_3.md) |
|     4 |                                          |                                          |                                          |                                          |                                          |                                          |                                          | [⭐⭐](aoc/src/aoc_2022/README_day_4.md) |
|     5 |                                          |                                          |                                          |                                          |                                          |                                          |                                          |                                          |
|     6 |                                          |                                          |                                          |                                          |                                          |                                          |                                          | [⭐⭐](aoc/src/aoc_2022/README_day_6.md) |
|     7 |                                          |                                          |                                          |                                          |                                          |                                          |                                          |                                          |
|     8 |                                          |                                          |                                          |                                          |                                          |                                          |                                          |                                          |
|     9 |                                          |                                          |                                          |                                          |                                          |                                          |                                          |                                          |
|    10 |                                          |                                          |                                          |                                          |                                          |                                          |                                          |                                          |
|    11 |                                          |                                          |                                          |                                          |                                          |                                          |                                          |                                          |
|    12 |                                          |                                          |                                          |                                          |                                          |                                          |                                          |                                          |
|    13 |                                          |                                          |                                          |                                          |                                          |                                          |                                          |                                          |
|    14 |                                          |                                          |                                          |                                          |                                          |                                          |                                          |                                          |
|    15 |                                          |                                          |                                          |                                          |                                          |                                          |                                          |                                          |
|    16 |                                          |                                          |                                          |                                          |                                          |                                          |                                          |                                          |
|    17 |                                          |                                          |                                          |                                          |                                          |                                          |                                          |                                          |
|    18 |                                          |                                          |                                          |                                          |                                          |                                          |                                          |                                          |
|    19 |                                          |                                          |                                          |                                          |                                          |                                          |                                          |                                          |
|    20 |                                          |                                          |                                          |                                          |                                          |                                          |                                          |                                          |
|    21 |                                          |                                          |                                          |                                          |                                          |                                          |                                          |                                          |
|    22 |                                          |                                          |                                          |                                          |                                          |                                          |                                          |                                          |
|    23 |                                          |                                          |                                          |                                          |                                          |                                          |                                          |                                          |
|    24 |                                          |                                          |                                          |                                          |                                          |                                          |                                          |                                          |
|    25 |                                          |                                          |                                          |                                          |                                          |                                          |                                          |                                          |

## Running the Solutions

We use the great [`gladvent`](https://github.com/TanklesXL/gladvent/) project to run the AoC Gleam solutions

```console
$ gleam run run 1 --year=2015
```

You can also run on example input:

```console
$ gleam run run 1 --year=2015 --example
```

## Bootstrap a Puzzle Solution

Use `gladvent` to invoke the Gleam template and set up files for a new solution:

```console
$ gleam run new 1 --year=2015
```

Add input and example input files inside the relevant `input` subdirectory

## Test a solution

You can run tests with `gleam test`:

```console
$ gleam test
```

Additionally, `gladvent` uses expectations registered in `gleam.toml` to check
that each solution gives the correct answer.

## Adding a Solution to GitHub

Follow these steps after solving a puzzle:

1. Store the expected results in the `gleam.toml` project file.

2. Add a snapshot test with title `"Puzzle 2015-01"` (with appropriate numbers),
run it, and accept it:

    ```console
    $ gleam test
    $ gleam run -m birdie
    ```

3. Update READMEs across all projects:

    ```console
    $ cd ..
    $ make
    ```
