import gleam/dict.{type Dict}
import gleam/int
import gleam/result
import gleam/string

pub type Data =
  List(String)

pub fn parse(input: String) -> Data {
  input |> string.to_graphemes()
}

pub fn pt_1(input: Data) -> Int {
  input |> find_marker(4)
}

pub fn pt_2(input: Data) -> Int {
  input |> find_marker(14)
}

pub fn find_marker(sequence: List(String), marker_length: Int) -> Int {
  find_marker_(sequence, 0, 0, marker_length, dict.new())
}

fn find_marker_(
  sequence: List(String),
  pos: Int,
  run: Int,
  marker_length: Int,
  last_seen: Dict(String, Int),
) {
  case run == marker_length {
    True -> pos
    False -> {
      let assert [char, ..tail] = sequence
      let chars_since_last =
        pos - { dict.get(last_seen, char) |> result.unwrap(or: -1) }
      let new_run = case chars_since_last > marker_length {
        True -> run + 1
        False -> int.min(run + 1, chars_since_last)
      }
      find_marker_(
        tail,
        pos + 1,
        new_run,
        marker_length,
        dict.insert(last_seen, char, pos),
      )
    }
  }
}
