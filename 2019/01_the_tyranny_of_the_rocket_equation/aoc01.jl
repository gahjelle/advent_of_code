# The Tyranny of the Rocket Equation
#
# Advent of Code 2019, day 1
# Solution by Geir Arne Hjelle, 2020-11-30

"""
    fuel(mass)

Calculate fuel based on mass
"""
function fuel(mass)
    return Int64(floor(mass / 3) - 2)
end


"""
    recursive_fuel(mass)

Calculate fuel based on mass, include fuel to cover mass of fuel
"""
function recursive_fuel(mass)
    fuel_for_mass = fuel(mass)
    if fuel_for_mass <= 0
        return 0
    else
        return fuel_for_mass + recursive_fuel(fuel_for_mass)
    end
end


"""
    main(filename)

Solve the problem for one file
"""
function main(filename)
    println("\n$(filename)")

    # Read from file
    input = open(filename) do fid
        parse.(Int64, readlines(fid))
    end

    # Part 1
    total_fuel = sum(fuel.(input))
    println("Total fuel:  $(total_fuel)")

    # Part 2
    rec_fuel = sum(recursive_fuel.(input))
    println("Total fuel, including fuel for fuel:  $(rec_fuel)")
end


# Run main on each file
main.(ARGS)