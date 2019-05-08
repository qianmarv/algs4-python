"""
Binary Search
For testting with large data size, try below shell commands:

$ python binary_search.py ../data/largeW.txt < ../data/largeT.txt
$ python binary_search.py ../data/tinyW.txt < ../data/tinyT.txt

"""


def search(target, sorted_list):
    """
    The sorted_list should really be sorted
    """
    low_idx = 0
    high_idx = len(sorted_list) - 1
    while low_idx <= high_idx:
        mid_idx = int(low_idx + (high_idx - low_idx) / 2)
        if target < sorted_list[mid_idx]:
            high_idx = mid_idx - 1
        elif target > sorted_list[mid_idx]:
            low_idx = mid_idx + 1
        else:
            return mid_idx
    return -1


def _rec_search(target, sorted_list, low_idx, high_idx):
    if low_idx <= high_idx:
        mid_idx = int(low_idx + (high_idx - low_idx) / 2)
        if target < sorted_list[mid_idx]:
            return _rec_search(target, sorted_list, low_idx, mid_idx - 1)
        elif target > sorted_list[mid_idx]:
            return _rec_search(target, sorted_list, mid_idx + 1, high_idx)
        else:
            return mid_idx
    else:
        return -1

def recursive_search(target, sorted_list):
    """
    The sorted_list should really be sorted
    Recursive way
    """
    return _rec_search(target, sorted_list, 0, len(sorted_list) - 1)


if __name__ == "__main__":
    import sys

    TOTAL_LIST = []
    FP = open(sys.argv[1])
    for line in FP.readlines():
        TOTAL_LIST.append(int(line))

    TOTAL_LIST.sort()

    for key in sys.stdin:
        if search(int(key), TOTAL_LIST) != -1:
            print(key)
