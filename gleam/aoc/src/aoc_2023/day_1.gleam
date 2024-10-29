import gleam/int
import gleam/list
import gleam/regex
import gleam/result
import gleam/string

pub type Data =
  List(String)

pub fn parse(input: String) -> Data {
  input |> string.trim() |> string.split("\n")
}

pub fn pt_1(input: Data) -> Int {
  input |> list.map(find_digits) |> int.sum()
}

pub fn pt_2(input: Data) -> Int {
  input
  |> list.map(fn(line) { line |> words_to_digits() |> find_digits() })
  |> int.sum()
}

pub fn find_digits(line: String) -> Int {
  let assert Ok(filter_numbers) = regex.from_string("[^0-9]")

  line
  |> regex.replace(filter_numbers, _, "")
  |> fn(digits) {
    case string.first(digits), string.last(digits) {
      Ok(first), Ok(last) ->
        { first <> last } |> int.parse() |> result.unwrap(or: 0)
      _, _ -> panic as { "found no number" <> line }
    }
  }
}

pub fn words_to_digits(line: String) -> String {
  line
  |> string.replace("zero", "z0o")
  |> string.replace("one", "o1e")
  |> string.replace("two", "t2o")
  |> string.replace("three", "t3e")
  |> string.replace("four", "f4r")
  |> string.replace("five", "f5e")
  |> string.replace("six", "s6x")
  |> string.replace("seven", "s7n")
  |> string.replace("eight", "e8t")
  |> string.replace("nine", "n9e")
}
