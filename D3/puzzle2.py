def puzzle2():
    file1 = open('D3/input.txt', 'r')
    Lines = file1.readlines()

    priorityvalues = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sumofpriorities = 0
    count = 0
    groups = [[]]
    groupcount = 0
    for line in Lines:
        if count == 3:
            groupcount += 1
            groups.append([])
            count = 0
        count += 1
        groups[groupcount].append(line.strip())

    for group in groups:
        firstsack = group[0]
        secondsack = group[1]
        thirdsack = group[2]
        for Letter in firstsack:
            if not secondsack.find(Letter) == -1 and not thirdsack.find(Letter) == -1:
                sumofpriorities += priorityvalues.index(Letter) + 1
                break
    return sumofpriorities

print(puzzle2()) # 2703