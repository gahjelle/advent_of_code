import aoc
import aoc_2020/day_1
import birdie
import gleam/set
import gleeunit
import gleeunit/should

pub fn main() {
  gleeunit.main()
}

pub fn day_01_find_summand_product_test() {
  [1, 3, 5, 9]
  |> set.from_list()
  |> day_1.find_summand_product(8)
  |> should.equal(Ok(3 * 5))
}

// SNAPSHOT TESTS
pub fn day_01_snapshot_test() {
  aoc.solve(2020, 1, day_1.parse, day_1.pt_1, day_1.pt_2)
  |> birdie.snap("Puzzle 2020-01")
}
