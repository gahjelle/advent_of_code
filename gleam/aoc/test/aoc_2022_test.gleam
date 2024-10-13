import aoc_2022/day_6
import gleeunit
import gleeunit/should

pub fn main() {
  gleeunit.main()
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
