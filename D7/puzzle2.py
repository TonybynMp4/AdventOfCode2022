from puzzle1 import puzzle1

def puzzle2():
    puzzle1result = puzzle1()
    totalsize, pathsizes = puzzle1result[1], list(puzzle1result[2].values())
    UsedSpace = sum(pathsizes)
    DiskSpace, UnusedSpace = 70000000, 30000000
    SmallestFileToDelete = DiskSpace

    for path in totalsize:
        FileSize = totalsize[path]
        if DiskSpace - UnusedSpace >= UsedSpace - FileSize and FileSize < SmallestFileToDelete:
            SmallestFileToDelete = FileSize
    return SmallestFileToDelete

if __name__ == "__main__":
    print(puzzle2()) # Smallest file's size: 4183246