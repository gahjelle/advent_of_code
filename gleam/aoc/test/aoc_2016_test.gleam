import aoc
import aoc_2016/day_1
import birdie
import gleam/list.{Continue, Stop}
import gleam/set
import gleeunit
import gleeunit/should

pub fn main() {
  gleeunit.main()
}

pub fn day_01_move_test() {
  day_1.East(day_1.Location(-3, 2))
  |> day_1.move(day_1.Order(day_1.Left, 5))
  |> should.equal(day_1.North(day_1.Location(-3, 7)))

  day_1.West(day_1.Location(99, 99))
  |> day_1.move(day_1.Order(day_1.None, 10))
  |> should.equal(day_1.West(day_1.Location(89, 99)))
}

pub fn day_01_trace_steps_test() {
  #(day_1.North(day_1.Location(-3, 2)), set.new())
  |> day_1.trace_steps(day_1.Order(day_1.Right, 2))
  |> should.equal(
    Continue(#(
      day_1.East(day_1.Location(-1, 2)),
      set.from_list([day_1.Location(-3, 2), day_1.Location(-2, 2)]),
    )),
  )

  #(day_1.South(day_1.Location(1, 1)), set.from_list([day_1.Location(1, 0)]))
  |> day_1.trace_steps(day_1.Order(day_1.None, 2))
  |> should.equal(
    Stop(#(
      day_1.South(day_1.Location(1, 0)),
      set.from_list([day_1.Location(1, 0), day_1.Location(1, 1)]),
    )),
  )
}

pub fn day_01_distance_to_hq_test() {
  day_1.Location(0, 0) |> day_1.distance_to_hq() |> should.equal(0)
  day_1.Location(12, 34) |> day_1.distance_to_hq() |> should.equal(46)
  day_1.Location(-1, 1) |> day_1.distance_to_hq() |> should.equal(2)
  day_1.Location(-123, -345) |> day_1.distance_to_hq() |> should.equal(468)
}

// SNAPSHOT TESTS
pub fn day_01_snapshot_test() {
  aoc.solve(2016, 1, day_1.parse, day_1.pt_1, day_1.pt_2)
  |> birdie.snap("Puzzle 2016-01")
}
