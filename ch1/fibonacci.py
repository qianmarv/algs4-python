"""
Exercise 1.1.19
A bad implementation of fibonacci as an example.
Try to implement a better way to calculate fibonacci and compare performance with
the bad way.
"""


def bad_fib(num):
    """
    Normal recursive way to calculate fibonacci
    """
    if num < 3:
        return 1
    else:
        return bad_fib(num - 1) + bad_fib(num - 2)


fib_map = {}


def _better_fib(num):
    result = 0
    if num < 3:
        result = 1
    else:
        if num in fib_map:
            result = fib_map[num]
        else:
            result = _better_fib(num - 1) + _better_fib(num - 2)

    fib_map[num] = result
    return result


def better_fib(num):
    """
    Follow the instruction in algs4 to save the calculated results
    """
    if num < 3:
        return 1
    else:
        return _better_fib(num - 1) + _better_fib(num - 2)

def _good_fib(num, count, prev_1, prev_2):
    current = prev_1 + prev_2
    if num == count:
        return current
    else:
        return _good_fib(num, count+1, current, prev_1)

def good_fib(num):
    if num < 3:
        return 1
    else:
        return _good_fib(num, 3, 1, 1)

def nice_fib(num):
    n, pre_2, pre_1 = 1, 1, 1
    while n < num:
        pre_2,pre_1 = pre_1, pre_2 + pre_1
        n += 1
    return pre_2

if __name__ == "__main__":
    import sys
    from timeit import default_timer as timer

    NUM = int(sys.argv[1])

    START = timer()
    result = bad_fib(NUM)
    END = timer()
    print("bad_fib    = %d ; total elapse: %f" % (result, END - START))

    START = timer()
    result = better_fib(NUM)
    END = timer()
    print("better_fib = %d ; total elapse: %f" % (result, END - START))

    START = timer()
    result = good_fib(NUM)
    END = timer()
    print("good_fib   = %d ; total elapse: %f" % (result, END - START))


    START = timer()
    result = nice_fib(NUM)
    END = timer()
    print("nice_fib   = %d ; total elapse: %f" % (result, END - START))
