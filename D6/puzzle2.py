def puzzle2():
    file = open('D6/input.txt', 'r')
    Line = file.read()

    for i in range(0, len(Line) - 1):
        Letters = [Line[i], Line[i+1], Line[i+2], Line[i+3], Line[i+4], Line[i+5], Line[i+6], Line[i+7], Line[i+8], Line[i+9], Line[i+10], Line[i+11], Line[i+12], Line[i+13]]
        LetterString = ''.join(Letters)
        check = []
        for u in LetterString:
            if LetterString.count(u) == 1:
                check.append(u)
        if len(check) == 14:
            return Line.find(LetterString) + 14

print(puzzle1())
