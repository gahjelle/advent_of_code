import gleam/int
import gleam/list
import gleam/result
import gleam/set.{type Set}
import gleam/string

pub type Data =
  Set(Int)

pub fn parse(input: String) -> Data {
  input
  |> string.split("\n")
  |> list.map(fn(number) { number |> int.parse() |> result.unwrap(or: 0) })
  |> set.from_list()
}

pub fn pt_1(input: Data) -> Int {
  input |> find_summand_product(2020) |> result.unwrap(or: 0)
}

pub fn pt_2(input: Data) -> Int {
  input
  |> set.map(fn(first: Int) -> Int {
    case find_summand_product(input, 2020 - first) {
      Ok(second_third) -> first * second_third
      Error(Nil) -> 0
    }
  })
  |> set.filter(fn(number) { number > 0 })
  |> set.to_list()
  |> list.first()
  |> result.unwrap(or: 0)
}

pub fn find_summand_product(input: Set(Int), target: Int) -> Result(Int, Nil) {
  case
    set.filter(input, fn(number) { set.contains(input, target - number) })
    |> set.to_list()
  {
    [] -> Error(Nil)
    [first, ..] -> Ok(first * { target - first })
  }
}
