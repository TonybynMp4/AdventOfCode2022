
def puzzle1():
    file1 = open('D3/input.txt', 'r')
    Lines = file1.readlines()

    priorityvalues = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sumofpriorities = 0
    for line in Lines:
        lineslength = len(line.strip())
        compartment1 = line.strip()[:int(lineslength/2)]
        compartment2 = line.strip()[int(lineslength/2):]
        for Letter in compartment1:
            if not compartment2.find(Letter) == -1:
                sumofpriorities += priorityvalues.index(Letter) + 1
                break
    return sumofpriorities

print(puzzle1()) # 7795