local function lines_from(file)
    local lines = {}
    for line in io.lines(file) do
        lines[#lines + 1] = line
    end
    return lines
end

local file = 'input1.txt'

local function day1()
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
    table.sort( totals )
    return totals[#totals]
end

print(day1())