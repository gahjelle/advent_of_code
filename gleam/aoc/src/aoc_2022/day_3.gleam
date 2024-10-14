import gleam/int
import gleam/list
import gleam/result
import gleam/set
import gleam/string

pub type Data =
  List(List(Int))

pub fn parse(input: String) -> Data {
  input
  |> string.trim()
  |> string.split("\n")
  |> list.map(string_to_priorities)
}

fn string_to_priorities(text: String) -> List(Int) {
  text
  |> string.to_utf_codepoints()
  |> list.map(fn(codepoint) {
    case string.utf_codepoint_to_int(codepoint) {
      ascii if ascii >= 97 && ascii <= 122 -> ascii - 96
      ascii if ascii >= 65 && ascii <= 90 -> ascii - 38
      ascii -> panic as { "unknown codepoint: " <> int.to_string(ascii) }
    }
  })
}

pub fn pt_1(input: Data) -> Int {
  input |> list.map(find_item) |> int.sum()
}

pub fn pt_2(input: Data) -> Int {
  input |> list.sized_chunk(into: 3) |> list.map(find_common) |> int.sum()
}

fn find_item(rucksack: List(Int)) -> Int {
  let per_compartment = list.length(rucksack) / 2
  rucksack |> list.sized_chunk(into: per_compartment) |> find_common()
}

fn find_common(compartments: List(List(Int))) -> Int {
  let assert Ok(common) =
    compartments
    |> list.map(set.from_list)
    |> list.reduce(set.intersection)

  common |> set.to_list() |> list.first() |> result.unwrap(or: 0)
}
