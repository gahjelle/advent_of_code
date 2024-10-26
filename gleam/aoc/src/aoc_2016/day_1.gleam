import gleam/int
import gleam/list.{type ContinueOrStop, Continue, Stop}
import gleam/result
import gleam/set.{type Set}
import gleam/string

pub type Rotation {
  Left
  Right
  None
}

pub type Order {
  Order(rotation: Rotation, step: Int)
}

pub type Location {
  Location(x: Int, y: Int)
}

pub type Position {
  North(location: Location)
  East(location: Location)
  South(location: Location)
  West(location: Location)
}

pub fn parse(input: String) -> List(Order) {
  input
  |> string.split(on: ", ")
  |> list.map(fn(order: String) -> Order {
    case order {
      "R" <> step -> Order(Right, step |> int.parse() |> result.unwrap(or: 0))
      "L" <> step -> Order(Left, step |> int.parse() |> result.unwrap(or: 0))
      _ -> panic as { "bad order: " <> order }
    }
  })
}

pub fn pt_1(input: List(Order)) -> Int {
  input
  |> list.fold(North(Location(0, 0)), move)
  |> fn(position) { position.location }
  |> distance_to_hq()
}

pub fn pt_2(input: List(Order)) -> Int {
  input
  |> list.fold_until(#(North(Location(0, 0)), set.new()), trace_steps)
  |> fn(acc) { { acc.0 }.location }
  |> distance_to_hq()
}

pub fn move(position: Position, order: Order) -> Position {
  case order {
    Order(rotation, step) ->
      case rotation, position {
        Right, West(location) | Left, East(location) | None, North(location) ->
          go_north(location, step)
        Right, North(location) | Left, South(location) | None, East(location) ->
          go_east(location, step)
        Right, East(location) | Left, West(location) | None, South(location) ->
          go_south(location, step)
        Right, South(location) | Left, North(location) | None, West(location) ->
          go_west(location, step)
      }
  }
}

fn go_north(location: Location, step: Int) -> Position {
  North(Location(..location, y: location.y + step))
}

fn go_east(location: Location, step: Int) -> Position {
  East(Location(..location, x: location.x + step))
}

fn go_south(location: Location, step: Int) -> Position {
  South(Location(..location, y: location.y - step))
}

fn go_west(location: Location, step: Int) -> Position {
  West(Location(..location, x: location.x - step))
}

pub fn trace_steps(
  acc: #(Position, Set(Location)),
  order: Order,
) -> ContinueOrStop(#(Position, Set(Location))) {
  let #(position, seen) = acc
  case set.contains(seen, position.location) {
    True -> Stop(#(position, seen))
    False -> {
      case order.step == 0 {
        True -> Continue(#(position, seen))
        False ->
          trace_steps(
            #(
              position |> move(Order(..order, step: 1)),
              set.insert(seen, position.location),
            ),
            Order(rotation: None, step: order.step - 1),
          )
      }
    }
  }
}

pub fn distance_to_hq(location: Location) -> Int {
  int.absolute_value(location.x) + int.absolute_value(location.y)
}
