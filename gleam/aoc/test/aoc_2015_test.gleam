import aoc
import aoc_2015/day_1
import aoc_2015/day_2
import birdie
import gleeunit
import gleeunit/should

pub fn main() {
  gleeunit.main()
}

pub fn day_02_surface_area_test() {
  day_2.Box(1, 5, 8) |> day_2.surface_area() |> should.equal(106)
}

pub fn day_02_smallest_side_area_test() {
  day_2.Box(1, 5, 8) |> day_2.smallest_side() |> should.equal(5)
}

pub fn day_02_smallest_perimeter_test() {
  day_2.Box(1, 5, 8) |> day_2.smallest_perimeter() |> should.equal(12)
}

pub fn day_02_volume_test() {
  day_2.Box(1, 5, 8) |> day_2.volume() |> should.equal(40)
}

// SNAPSHOT TESTS
pub fn day_01_snapshot_test() {
  aoc.solve(2015, 1, day_1.parse, day_1.pt_1, day_1.pt_2)
  |> birdie.snap("Puzzle 2015-01")
}

pub fn day_02_snapshot_test() {
  aoc.solve(2015, 2, day_2.parse, day_2.pt_1, day_2.pt_2)
  |> birdie.snap("Puzzle 2015-02")
}
