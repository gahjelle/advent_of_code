import gleam/dict.{type Dict}
import gleam/int
import gleam/list
import gleam/option.{None, Some}
import gleam/string

pub type Data =
  List(List(String))

pub fn parse(input: String) -> Data {
  input
  |> string.trim()
  |> string.split(on: "\n")
  |> list.map(string.to_graphemes)
}

pub fn pt_1(input: Data) -> Int {
  count_repeats(input, 2) * count_repeats(input, 3)
}

pub fn pt_2(input: Data) -> String {
  input |> find_matching_ids()
}

pub fn count_repeats(input: List(List(String)), num_repeats: Int) -> Int {
  input
  |> list.map(fn(line) {
    let has_repeat =
      line
      |> count_letters()
      |> dict.values()
      |> list.contains(num_repeats)
    case has_repeat {
      True -> 1
      False -> 0
    }
  })
  |> int.sum()
}

pub fn count_letters(input: List(String)) -> Dict(String, Int) {
  input
  |> list.fold(dict.new(), fn(counts, char) {
    dict.upsert(counts, update: char, with: fn(count) {
      case count {
        Some(count) -> count + 1
        None -> 1
      }
    })
  })
}

pub fn find_matching_ids(input: List(List(String))) -> String {
  let assert [box_id, ..box_ids] = input
  case list.find_map(box_ids, check_similar(_, box_id, [], 0)) {
    Error(_) -> find_matching_ids(box_ids)
    Ok(common) -> common
  }
}

pub fn check_similar(
  first: List(String),
  second: List(String),
  common: List(String),
  num_diffs: Int,
) -> Result(String, Nil) {
  case first, second {
    [], [] -> common |> list.reverse() |> string.concat() |> Ok()
    [head_1, ..tail_1], [head_2, ..tail_2] if head_1 == head_2 ->
      check_similar(tail_1, tail_2, [head_1, ..common], num_diffs)
    [head_1, ..tail_1], [head_2, ..tail_2]
      if head_1 != head_2 && num_diffs == 0
    -> check_similar(tail_1, tail_2, common, 1)
    _, _ -> Error(Nil)
  }
}
