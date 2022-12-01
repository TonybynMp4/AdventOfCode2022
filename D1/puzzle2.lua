require("D1/puzzle1")

local top3 = {}

local function puzzle2(table)
    for i = 1, 3, 1 do
        top3[#top3+1] = table[i]
    end

    local totaltop3 = 0

    for _, v in pairs(top3) do
        totaltop3 = totaltop3 + v
    end

    return totaltop3
end

local result = puzzle2(puzzle1())

if result then
    print("Top 3:\n    1: " .. top3[1] .. " 2: " ..  top3[2] .. " 3: " .. top3[3]) --     1: 70369 2: 66781 3: 65852
    print("Total Calories:\n    " .. result) --   203002
end