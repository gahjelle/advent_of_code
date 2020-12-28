# Allergen Assessment
#
# Advent of Code 2020, day 21
# Solution by Geir Arne Hjelle, 2020-12-21

module AOC21

using Pipe


function parse_food(lines)
    ingredients, allergens = [], []
    for line in lines
        m = match(r"(?<ingredients>.+) \(contains (?<allergens>.+)\)", line)
        food_ingredients = Set()
        for ingredient in split(m[:ingredients], " ")
            push!(food_ingredients, ingredient)
        end
        push!(ingredients, food_ingredients)

        food_allergens = Set()
        for allergen in split(m[:allergens], ", ")
            push!(food_allergens, allergen)
        end
        push!(allergens, food_allergens)
    end
    (ingredients = ingredients, allergens = allergens)
end


function find_candidates(ingredients, allergens)
    candidates = Dict()
    for allergen in foldl(union, allergens)
        ingredient_candidates = foldl(union, ingredients)
        for (food_ingredients, food_allergens) in zip(ingredients, allergens)
            if allergen ∈ food_allergens
                ingredient_candidates = intersect(ingredient_candidates, food_ingredients)
            end
        end
        candidates[allergen] = ingredient_candidates
    end
    
    candidates
end


function prune_candidates(candidates)
    allergens = Dict(a => i |> first for (a, i) in candidates if i |> length == 1)
    leftover = filter(c -> c.second |> length > 1, candidates)

    while !isempty(leftover)
        for (allergen, ingredients) in leftover
            unknown = setdiff(ingredients, allergens |> values)
            if unknown |> length == 1
                allergens[allergen] = unknown |> first
                pop!(leftover, allergen)
            end
        end
    end
    
    allergens
end


function list_safe_ingredients(ingredients, allergens)
    [i for fi in ingredients for i in fi if i ∉ allergens |> values]
end


function list_dangerous_ingredients(allergens)
    @pipe allergens |> collect |> sort |> map(a -> a.second, _)
end


# Solve the problem for one file
function solve(input)
    # Parse input
    ingredients, allergens = split(input, "\n") |> parse_food

    # Part 1
    allergens_by_ingredient = find_candidates(ingredients, allergens) |> prune_candidates
    part_1 = list_safe_ingredients(ingredients, allergens_by_ingredient) |> length

    # Part 2
    part_2 = @pipe list_dangerous_ingredients(allergens_by_ingredient) |> join(_, ",")

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
