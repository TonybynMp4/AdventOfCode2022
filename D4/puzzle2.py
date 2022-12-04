
def puzzle1():
    file = open('D4/input.txt', 'r')
    Lines = file.readlines()

    overlapping = 0
    for pair in Lines:
        pair = pair.strip()
        assignement1, assignement2 = pair.split(',')
        assignement1_start, assignement1_end = assignement1.split('-')
        assignement2_start, assignement2_end = assignement2.split('-')
        if assignement1_start <= assignement2_start  <= assignement1_end or assignement1_start <= assignement2_end  <= assignement1_end or assignement1_start <= assignement1_end  <= assignement2_end or assignement2_start <= assignement1_start  <= assignement2_end:
            overlapping += 1
    return overlapping

print(puzzle1())