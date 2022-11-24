# Advent of Code in Julia

Solutions to [Advent of Code](https://adventofcode.com/) in [Julia](https://julialang.org/) (12⭐):

|   Day | [2015](2015)                      | [2019](2019)                                       | [2020](2020)                        |
|------:|:----------------------------------|:---------------------------------------------------|:------------------------------------|
|     1 |                                   | [⭐⭐](2019/01_the_tyranny_of_the_rocket_equation) | [⭐⭐](2020/01_report_repair)       |
|     2 |                                   |                                                    | [⭐⭐](2020/02_password_philosophy) |
|     3 |                                   |                                                    | [⭐⭐](2020/03_toboggan_trajectory) |
|     4 |                                   |                                                    |                                     |
|     5 |                                   |                                                    |                                     |
|     6 |                                   |                                                    |                                     |
|     7 |                                   |                                                    |                                     |
|     8 |                                   |                                                    |                                     |
|     9 |                                   |                                                    |                                     |
|    10 |                                   |                                                    |                                     |
|    11 |                                   |                                                    |                                     |
|    12 |                                   |                                                    |                                     |
|    13 |                                   |                                                    |                                     |
|    14 | [⭐⭐](2015/14_reindeer_olympics) |                                                    |                                     |
|    15 |                                   |                                                    |                                     |
|    16 | [⭐⭐](2015/16_aunt_sue)          |                                                    |                                     |
|    17 |                                   |                                                    |                                     |
|    18 |                                   |                                                    |                                     |
|    19 |                                   |                                                    |                                     |
|    20 |                                   |                                                    |                                     |
|    21 |                                   |                                                    |                                     |
|    22 |                                   |                                                    |                                     |
|    23 |                                   |                                                    |                                     |
|    24 |                                   |                                                    |                                     |
|    25 |                                   |                                                    |                                     |

## Install Dependencies

Start the Julia REPL (make sure the environment is activated) and download and compile dependencies:

```
julia> ]
(julia) pkg> instantiate
(julia) pkg> precompile
```

## Run the Solutions

Enter the puzzle directory, and run the Julia solution file:

```console
$ cd 2015/01_not_quite_lisp/
$ julia aoc201501.jl input.txt
```

## Bootstrap a Puzzle Solution

TODO: Create a Copier task that creates a new Julia puzzle template

## Run Tests

You can test all solutions by running:

```console
$ julia test_all_puzzles.jl
```

Note that the tests are done by running the puzzle solutions on the `input.txt` file in each puzzle directory and comparing the output to a `output.jl.txt` file in the same directory.

You can include a benchmarking report by adding the `-r` option:

```console
$ julia test_all_puzzles.jl -r
```

This will create a file named `timings.jl.md` that contains timing information for each puzzle.

## Adding a Solution to GitHub

Follow these steps after solving a puzzle:

1. Store the solution to an output file:

    ```console
    $ cd 2015/01_not_quite_lisp/
    $ julia aoc201501.jl input.txt > output.jl.txt
    ```

2. Run benchmarks and add them to the README:

    ```console
    $ cd ../..
    $ julia test_all_puzzles.jl -r
    ```

3. Update READMEs across all projects:

    ```console
    $ cd ..
    $ make
    ```
