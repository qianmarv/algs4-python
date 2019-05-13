"""
Exercise 1.1.32 Histogram. Suppose that the standard input stream is a sequence
of double values. Write a program that takes an integer N and two double values
l and r from the command line and uses StdDraw to plot a histogram of the count
of the numbers in the standard input stream that fall in each of the N intervals
deﬁned by dividing (l , r) into N equal-sized intervals.
"""
from matplotlib import pyplot as plt
import numpy as np


def draw(N, l, r, arr):
    bins = [l + (r - l) * i / N for i in range(N + 1)]
    print(bins)
    plt.hist(arr, bins)
    plt.show()


if __name__ == "__main__":
    import sys
    arr = [float(elem) for elem in sys.stdin.readline().split()]
    print(arr)
    draw(int(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), arr)
