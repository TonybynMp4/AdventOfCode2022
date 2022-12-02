local function lines_from(file)
    local lines = {}
    for line in io.lines(file) do
        lines[#lines + 1] = line
    end
    return lines
end

local file = 'D2/input1.txt'

function puzzle1()
    local input = lines_from(file)
    local totalscore = 0

    for _, v in pairs(input) do
        local match = {}
        for Letter in string.gmatch(v, "%S+") do
            if match.adversary then
                match.shouldplay = Letter
            else
                match.adversary = Letter
            end
        end

        -- Adversary plays -> A: Rock B: Paper C: Scissors
        -- You should play -> X: Rock Y: Paper Z: Scissors

        local outcome
        if match.adversary == 'A' then
            outcome = (match.shouldplay == 'Y' and 'win') or (match.shouldplay == 'X' and 'draw') or 'lost'
        elseif match.adversary == 'B' then
            outcome = (match.shouldplay == 'Z' and 'win') or (match.shouldplay == 'Y' and 'draw') or 'lost'
        elseif match.adversary == 'C' then
            outcome = (match.shouldplay == 'X' and 'win') or (match.shouldplay == 'Z' and 'draw') or 'lost'
        end
        totalscore = totalscore + ((outcome == 'win' and 6) or (outcome == 'draw' and 3) or (outcome == 'lost' and 0)) + ((match.shouldplay == 'X' and 1) or (match.shouldplay == 'Y' and 2) or (match.shouldplay == 'Z' and 3))
        match = {}
    end
    return totalscore
end

print("Total Score: " .. puzzle1()) -- 13924 Points