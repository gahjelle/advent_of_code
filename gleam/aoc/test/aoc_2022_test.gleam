import aoc
import aoc_2022/day_1
import aoc_2022/day_2
import aoc_2022/day_3
import aoc_2022/day_6
import birdie
import gleeunit
import gleeunit/should

pub fn main() {
  gleeunit.main()
}

pub fn day_01_snapshot_test() {
  aoc.solve(2022, 1, day_1.parse, day_1.pt_1, day_1.pt_2)
  |> birdie.snap("Puzzle 2022-01")
}

pub fn day_02_snapshot_test() {
  aoc.solve(2022, 2, day_2.parse, day_2.pt_1, day_2.pt_2)
  |> birdie.snap("Puzzle 2022-02")
}

pub fn day_03_snapshot_test() {
  aoc.solve(2022, 3, day_3.parse, day_3.pt_1, day_3.pt_2)
  |> birdie.snap("Puzzle 2022-03")
}

pub fn day_06_find_marker_test() {
  day_6.find_marker(["g", "e", "i", "r", "a", "r", "n", "e"], 5)
  |> should.equal(5)

  day_6.find_marker(
    ["a", "a", "a", "a", "a", "a", "a", "b", "c", "c", "c", "c"],
    3,
  )
  |> should.equal(9)
}

pub fn day_06_snapshot_test() {
  aoc.solve(2022, 6, day_6.parse, day_6.pt_1, day_6.pt_2)
  |> birdie.snap("Puzzle 2022-06")
}
