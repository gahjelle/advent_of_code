import gleam/dict.{type Dict}
import gleam/int
import gleam/list
import gleam/option.{None, Some}
import gleam/result
import gleam/string

pub type Data =
  #(List(Int), List(Int))

pub fn parse(input: String) -> Data {
  let data =
    input
    |> string.trim()
    |> string.split("\n")
    |> list.map(fn(line) {
      line
      |> string.split("   ")
      |> list.map(fn(number) { number |> int.parse() |> result.unwrap(or: 0) })
    })
    |> list.transpose()

  case data {
    [left, right] -> #(left, right)
    _ -> panic as "bad input"
  }
}

pub fn pt_1(input: Data) -> Int {
  let #(left, right) = input
  list.zip(list.sort(left, by: int.compare), list.sort(right, by: int.compare))
  |> list.map(fn(pair) {
    let #(first, second) = pair
    int.absolute_value(second - first)
  })
  |> int.sum()
}

pub fn pt_2(input: Data) -> Int {
  let #(left, right) = input
  let count = right |> count_numbers()

  left
  |> list.map(fn(number) {
    number * { dict.get(count, number) |> result.unwrap(or: 0) }
  })
  |> int.sum()
}

pub fn count_numbers(numbers: List(Int)) -> Dict(Int, Int) {
  numbers
  |> list.fold(dict.new(), fn(counts, number) {
    dict.upsert(counts, update: number, with: fn(count) {
      case count {
        Some(count) -> count + 1
        None -> 1
      }
    })
  })
}
