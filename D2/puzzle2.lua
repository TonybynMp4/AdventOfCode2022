local function lines_from(file)
    local lines = {}
    for line in io.lines(file) do
        lines[#lines + 1] = line
    end
    return lines
end

local file = 'D2/input1.txt'

function puzzle2()
    local input = lines_from(file)
    local totalscore = 0

    for _, v in pairs(input) do
        local match = {}
        for Letter in string.gmatch(v, "%S+") do
            if match.adversary then
                match.shouldend = Letter
            else
                match.adversary = Letter
            end
        end

        -- A: Rock B: Paper C: Scissors
        -- X: lose Y: draw Z: win

        local response
        if match.adversary == 'A' then
            response = (match.shouldend == 'Y' and 'A') or (match.shouldend == 'X' and 'C') or 'B'
        elseif match.adversary == 'B' then
            response = (match.shouldend == 'Z' and 'C') or (match.shouldend == 'Y' and 'B') or 'A'
        elseif match.adversary == 'C' then
            response = (match.shouldend == 'X' and 'B') or (match.shouldend == 'Z' and 'A') or 'C'
        end
        totalscore = totalscore + ((match.shouldend == 'Z' and 6) or (match.shouldend == 'Y' and 3) or (match.shouldend == 'X' and 0)) + ((response == 'A' and 1) or (response == 'B' and 2) or (response == 'C' and 3))
        match = {}
    end
    return totalscore
end

print("Total Score: " .. puzzle1()) -- 13448 Points
