def puzzle1():
    file = open('D4/input.txt', 'r')
    Lines = file.readlines()

    overlapping = 0
    for pair in Lines:
        pair = pair.strip()
        assignement1, assignement2 = pair.split(',')
        assignement1_1, assignement1_2 = map(int, assignement1.split('-'))
        assignement2_1, assignement2_2 = map(int, assignement2.split('-'))
        if (assignement1_1 <= assignement2_1 and assignement1_2 >= assignement2_2) or (assignement2_1 <= assignement1_1 and assignement2_2 >= assignement1_2):
            overlapping += 1
    return overlapping

print(puzzle1())