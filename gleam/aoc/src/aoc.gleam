import gladvent
import gladvent/internal/input
import gleam/int
import gleam/result
import gleam/string
import pprint
import simplifile

pub fn main() {
  gladvent.main()
}

pub fn to_int(text: String) -> Int {
  text |> int.parse() |> result.unwrap(or: 0)
}

fn get_input(year: Int, day: Int) -> String {
  let input_path = input.get_file_path(year, day, input.Puzzle)
  input_path
  |> simplifile.read()
  |> result.map(string.trim(_))
  |> result.unwrap(or: "")
}

pub fn solve(
  year: Int,
  day: Int,
  parse_fn: fn(String) -> data,
  pt_1_fn: fn(data) -> a,
  pt_2_fn: fn(data) -> b,
) -> String {
  let parsed_input =
    get_input(year, day)
    |> parse_fn()

  let pt_1 = pt_1_fn(parsed_input)
  let pt_2 = pt_2_fn(parsed_input)
  pprint.format(pt_1) <> "\n" <> pprint.format(pt_2)
}
