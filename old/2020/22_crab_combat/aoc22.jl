# Crab Combat
#
# Advent of Code 2020, day 22
# Solution by Geir Arne Hjelle, 2020-12-22

module AOC22

using Pipe


function parse_cards(lines)
    @pipe lines |> split(_, "\n") |> _[2:end] |> map(n -> parse(Int, n), _)
end


function regular_combat(deck1, deck2)
    while !isempty(deck1) && !isempty(deck2)
        card1 = popfirst!(deck1)
        card2 = popfirst!(deck2)

        if card1 > card2
            append!(deck1, [card1, card2])
        else
            append!(deck2, [card2, card1])
        end
    end

    vcat(deck1, deck2)
end


function recursive_combat(deck1, deck2)
    seen = Set()
    while !isempty(deck1) && !isempty(deck2)
        if (deck1, deck2) ∈ seen
            return (winning_deck = deck1, winner = 1)
        end
        push!(seen, (deck1 |> copy, deck2 |> copy))

        card1 = popfirst!(deck1)
        card2 = popfirst!(deck2)

        if card1 <= length(deck1) && card2 <= length(deck2)
            winning_deck, winner = recursive_combat(deck1[1:card1] |> copy, deck2[1:card2] |> copy)
            if winner == 1
                append!(deck1, [card1, card2])
            else
                append!(deck2, [card2, card1])
            end
        else
            if card1 > card2
                append!(deck1, [card1, card2])
            else
                append!(deck2, [card2, card1])
            end
        end
    end
    (winning_deck = vcat(deck1, deck2), winner = isempty(deck2) ? 1 : 2)
end


function score_deck(num_cards)
    function _score_deck(deck)
        @pipe zip(deck, num_cards:-1:1) |> map(c -> prod(c), _) |> sum
    end
end


# Solve the problem for one file
function solve(input)
    # Parse input
    deck1, deck2 = @pipe split(input, "\n\n") |> map(c -> parse_cards(c), _)
    num_cards = length(deck1) + length(deck2)

    # Part 1
    part_1 = (
        regular_combat(deck1 |> copy, deck2 |> copy)
        |> score_deck(num_cards)
    )

    # Part 2
    part_2 = @pipe (
        recursive_combat(deck1 |> copy, deck2 |> copy)
        |> _.winning_deck
        |> score_deck(num_cards)
    )

    part_1, part_2
end


# Solve the problem for one file
function solve_file(file_path)
    println("\n$(file_path)")
    input = open(file_path) do fid
        read(fid, String) |> strip
    end
    input .|> solve
end

# Solve the problem for each file
[a for a in ARGS if a[1] != '-'] .|> solve_file .|> s -> join(s, "\n") |> println

end  # module
