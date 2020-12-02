# Report Repair
#
# Advent of Code 2020, day 1
# Solution by Geir Arne Hjelle, 2020-12-01

"""
    find_adders(numbers, target)

Find two numbers that add up to target. Will return all numbers that are part
of such pairs.
"""
function find_adders(numbers, target=2020)
    lookup = Set(numbers)
    return [n for n in numbers if target - n in lookup]
end


"""
    main(filename)

Solve the problem for one file
"""
function main(filename)
    println("\n$(filename)")

    # Read from file
    input = open(filename) do fid
        parse.(Int32, readlines(fid))
    end

    # Part 1
    println(prod(find_adders(input)))

    # Part 2
    for (idx, first) in enumerate(input)
        pairs = find_adders(input[idx + 1:end], 2020 - first)
        if !isempty(pairs)
            println(prod([[first]; pairs]))
            break
        end
    end
end


# Run main on each file
main.(ARGS)
