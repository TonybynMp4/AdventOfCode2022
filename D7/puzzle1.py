def puzzle1():
    file = open('D7/input.txt', 'r')
    Lines = []

    for line in file.readlines():
        Lines.append(line.strip().split())

# Variables
    paths = dict()
    pathsizes = dict()
    totalsize = dict()
    currentpath = []
    result = 0
#

    #probably should be moved outside the function but im too tired to figure that out
    def searchbot6000(path):
        if len(paths[path]) > 0:
            for j in paths[path]:
                searchbot6000(j)
        counter.append(pathsizes[path])
        return counter

    for line in Lines:
        if line[1] == "ls":
            continue

        if line[1] == "cd":
            if line[2] == "..":
                currentpath.pop()
            else:
                currentpath.append(line[2])
                paths["".join(currentpath)] = []
                pathsizes["".join(currentpath)] = 0
        elif line[0] == "dir":
            paths["".join(currentpath)].append("".join(currentpath) + line[1])
        else:
            pathsizes["".join(currentpath)] += int(line[0])

    for path in paths:
        totalsize[path] = 0

    for path in paths:
        counter = []
        counter = searchbot6000(path)
        totalsize[path] += sum(counter)

    for path in totalsize:
        if totalsize[path] <= 100000:
            result += totalsize[path]

    return result, totalsize, pathsizes

if __name__ == "__main__":
    print(puzzle1()[0]) # 1454188 beep boop beep boop