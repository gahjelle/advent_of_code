import aoc
import aoc_2024/day_1
import birdie
import gleam/dict
import gleeunit
import gleeunit/should

pub fn main() {
  gleeunit.main()
}

pub fn day_01_count_numbers_test() {
  day_1.count_numbers([1, 2, 2, 3, 3, 3, 3])
  |> should.equal(dict.from_list([#(1, 1), #(2, 2), #(3, 4)]))
}

// SNAPSHOT TESTS

pub fn day_01_snapshot_test() {
  aoc.solve(2024, 1, day_1.parse, day_1.pt_1, day_1.pt_2)
  |> birdie.snap("Puzzle 2024-01")
}
