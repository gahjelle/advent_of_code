import gleam/dict.{type Dict}
import gleam/int
import gleam/list
import gleam/option.{None, Some}
import gleam/regex
import gleam/result
import gleam/set
import gleam/string

pub type Claim {
  Claim(id: Int, xs: List(Int), ys: List(Int))
}

pub type Fabric =
  Dict(#(Int, Int), List(Int))

pub fn parse(input: String) -> Fabric {
  let assert Ok(parser) =
    regex.from_string("#(\\d+) @ (\\d+),(\\d+): (\\d+)x(\\d+)")
  input
  |> string.trim()
  |> string.split(on: "\n")
  |> list.map(parse_claim(_, parser))
  |> list.fold(dict.new(), add_claim_to_fabric)
}

pub fn parse_claim(claim: String, parser: regex.Regex) -> Claim {
  case regex.scan(with: parser, content: claim) {
    [
      regex.Match(
        _,
        [Some(id), Some(left), Some(top), Some(width), Some(height)],
      ),
    ] -> {
      let left = left |> int.parse() |> result.unwrap(or: 0)
      let top = top |> int.parse() |> result.unwrap(or: 0)
      let width = width |> int.parse() |> result.unwrap(or: 0)
      let height = height |> int.parse() |> result.unwrap(or: 0)
      Claim(
        id: id |> int.parse() |> result.unwrap(or: 0),
        xs: list.range(from: left, to: left + width - 1),
        ys: list.range(from: top, to: top + height - 1),
      )
    }
    _ -> panic as { "unknown claim: " <> claim }
  }
}

pub fn add_claim_to_fabric(fabric: Fabric, claim: Claim) -> Fabric {
  use fabric, x <- list.fold(claim.xs, fabric)
  use fabric, y <- list.fold(claim.ys, fabric)
  dict.upsert(fabric, #(x, y), fn(claims_on_square) {
    case claims_on_square {
      Some(claims) -> [claim.id, ..claims]
      None -> [claim.id]
    }
  })
}

pub fn pt_1(input: Fabric) -> Int {
  input |> dict.values() |> list.count(fn(claims) { list.length(claims) >= 2 })
}

pub fn pt_2(input: Fabric) -> Int {
  let all_claims = input |> dict.values() |> list.concat() |> set.from_list()
  let overlapping_claims =
    input
    |> dict.values()
    |> list.filter(fn(claims) { list.length(claims) >= 2 })
    |> list.concat()
    |> set.from_list()

  all_claims
  |> set.difference(minus: overlapping_claims)
  |> set.to_list()
  |> list.first()
  |> result.unwrap(or: 0)
}
