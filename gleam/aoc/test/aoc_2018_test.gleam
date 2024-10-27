import aoc
import aoc_2018/day_1
import aoc_2018/day_2
import aoc_2018/day_3
import birdie
import gleam/dict
import gleam/list
import gleam/regex
import gleam/string
import gleeunit
import gleeunit/should

pub fn main() {
  gleeunit.main()
}

pub fn day_02_count_repeats_test() {
  let input =
    ["abcaba", "abcdef", "aaaaaa", "abbaba"]
    |> list.map(string.to_graphemes)

  day_2.count_repeats(input, 1) |> should.equal(2)
  day_2.count_repeats(input, 2) |> should.equal(1)
  day_2.count_repeats(input, 3) |> should.equal(2)
  day_2.count_repeats(input, 4) |> should.equal(0)
}

pub fn day_02_count_letters_test() {
  day_2.count_letters(["a", "b", "c", "a", "b", "a"])
  |> should.equal(dict.from_list([#("a", 3), #("b", 2), #("c", 1)]))
}

pub fn day_02_find_matching_ids_test() {
  ["abcaba", "abcdef", "aaaaaa", "abbaba"]
  |> list.map(string.to_graphemes)
  |> day_2.find_matching_ids()
  |> should.equal("ababa")
}

pub fn day_02_check_similar_test() {
  day_2.check_similar(["a", "b", "c", "d"], ["d", "c", "b", "a"], [], 0)
  |> should.be_error()

  day_2.check_similar(["a", "b", "c", "d"], ["a", "e", "c", "d"], [], 0)
  |> should.equal(Ok("acd"))
}

pub fn day_03_parse_claim_test() {
  let assert Ok(parser) =
    regex.from_string("#(\\d+) @ (\\d+),(\\d+): (\\d+)x(\\d+)")

  day_3.parse_claim("#281 @ 258,327: 11x4", parser)
  |> should.equal(
    day_3.Claim(281, list.range(from: 258, to: 268), [327, 328, 329, 330]),
  )
}

pub fn day_03_add_claim_to_fabric_test() {
  dict.new()
  |> day_3.add_claim_to_fabric(day_3.Claim(1, [2, 3], [1, 2]))
  |> day_3.add_claim_to_fabric(day_3.Claim(2, [1, 2], [2, 3]))
  |> day_3.add_claim_to_fabric(day_3.Claim(3, [3], [3]))
  |> should.equal(
    dict.new()
    |> dict.insert(#(2, 1), [1])
    |> dict.insert(#(2, 2), [2, 1])
    |> dict.insert(#(3, 1), [1])
    |> dict.insert(#(3, 2), [1])
    |> dict.insert(#(1, 2), [2])
    |> dict.insert(#(1, 3), [2])
    |> dict.insert(#(2, 3), [2])
    |> dict.insert(#(3, 3), [3]),
  )
}

// SNAPSHOT TESTS
pub fn day_01_snapshot_test() {
  aoc.solve(2018, 1, day_1.parse, day_1.pt_1, day_1.pt_2)
  |> birdie.snap("Puzzle 2018-01")
}

pub fn day_02_snapshot_test() {
  aoc.solve(2018, 2, day_2.parse, day_2.pt_1, day_2.pt_2)
  |> birdie.snap("Puzzle 2018-02")
}

pub fn day_03_snapshot_test() {
  aoc.solve(2018, 3, day_3.parse, day_3.pt_1, day_3.pt_2)
  |> birdie.snap("Puzzle 2018-03")
}
