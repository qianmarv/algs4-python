def rank(key, arr):
    lo = 0
    hi = len(arr) - 1
    while (lo <= hi):
        mid = int(lo + (hi - lo)/2)
        if key < arr[mid]:
            hi = mid - 1
        elif key > arr[mid]:
            lo = mid + 1
        else:
            return mid
    return -1

if __name__ == "__main__":
    # $> python BinarySearch.py ../data/largeW.txt < ../data/largeT.txt
    # $> python BinarySearch.py ../data/tinyW.txt < ../data/tinyT.txt
    import sys
    arr = []
    fp = open(sys.argv[1])
    for line in fp.readlines():
        arr.append(int(line))

    arr.sort()

    for key in sys.stdin:
        print(rank(int(key), arr))
