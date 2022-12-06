def puzzle2():
    file = open('D6/input.txt', 'r')
    Line = file.read()

    for i in range(0, len(Line) - 1):
        Letters = []
        Letters.append(Line[i:i+14])
        LetterString = ''.join(Letters)
        check = []
        for u in LetterString:
            if LetterString.count(u) == 1:
                check.append(u)
        if len(check) == 14:
            return Line.find(LetterString) + 14

print(puzzle2())