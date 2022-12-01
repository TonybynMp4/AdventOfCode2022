local function lines_from(file)
    local lines = {}
    for line in io.lines(file) do
        lines[#lines + 1] = line
    end
    return lines
end

local file = 'D1/input1.txt'

function puzzle1()
    local input = lines_from(file)
    local totaltable = {}
    local temptable = {}

    for _, v in pairs(input) do
        if string.len(v) > 0 then
            temptable[#temptable+1] = v
        else
            totaltable[#totaltable+1] = temptable
            temptable = {}
        end
    end
    local totals = {}
    for _, value in pairs(totaltable) do
        local temptotal = 0
        for _, v in pairs(value) do
            temptotal = temptotal + v
        end
        totals[#totals+1] = temptotal
    end
    table.sort( totals, function(a,b) return b < a end)
    return totals
end

print(puzzle1()[1]) -- 70369