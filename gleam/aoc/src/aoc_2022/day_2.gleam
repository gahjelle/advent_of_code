import gleam/int
import gleam/list
import gleam/string

pub type Hand {
  Rock
  Paper
  Scissors
}

pub type Outcome {
  Loss
  Draw
  Win
}

pub type Data =
  List(#(Hand, Hand, Outcome))

pub fn parse(input: String) -> Data {
  input
  |> string.trim_right
  |> string.split(on: "\n")
  |> list.map(fn(round) {
    round
    |> string.split(on: " ")
    |> fn(symbols) {
      case symbols {
        [first, second] -> #(
          parse_hand(first),
          parse_hand(second),
          parse_outcome(second),
        )
        _ -> panic as { "Not a round: " <> round }
      }
    }
  })
}

fn parse_hand(char: String) -> Hand {
  case char {
    "A" | "X" -> Rock
    "B" | "Y" -> Paper
    "C" | "Z" -> Scissors
    _ -> panic as { "Unknown hand: " <> char }
  }
}

fn parse_outcome(char: String) -> Outcome {
  case char {
    "X" -> Loss
    "Y" -> Draw
    "Z" -> Win
    _ -> panic as { "Unknown outcome: " <> char }
  }
}

pub fn pt_1(input: Data) -> Int {
  input
  |> list.map(fn(round) {
    let #(opponent_hand, hand, _) = round
    [
      hand |> score_hand(),
      determine_outcome(hand, opponent_hand) |> score_outcome(),
    ]
    |> int.sum()
  })
  |> int.sum()
}

pub fn pt_2(input: Data) -> Int {
  input
  |> list.map(fn(round) {
    let #(opponent_hand, _, outcome) = round
    [
      opponent_hand |> determine_hand(outcome) |> score_hand(),
      outcome |> score_outcome(),
    ]
    |> int.sum()
  })
  |> int.sum()
}

fn determine_outcome(hand: Hand, opponent_hand: Hand) -> Outcome {
  case hand, opponent_hand {
    Rock, Paper | Paper, Scissors | Scissors, Rock -> Loss
    Rock, Rock | Paper, Paper | Scissors, Scissors -> Draw
    Rock, Scissors | Paper, Rock | Scissors, Paper -> Win
  }
}

fn determine_hand(opponent_hand: Hand, outcome: Outcome) -> Hand {
  case opponent_hand, outcome {
    Rock, Draw | Paper, Loss | Scissors, Win -> Rock
    Rock, Win | Paper, Draw | Scissors, Loss -> Paper
    Rock, Loss | Paper, Win | Scissors, Draw -> Scissors
  }
}

fn score_hand(hand: Hand) -> Int {
  case hand {
    Rock -> 1
    Paper -> 2
    Scissors -> 3
  }
}

fn score_outcome(outcome: Outcome) -> Int {
  case outcome {
    Loss -> 0
    Draw -> 3
    Win -> 6
  }
}
