"""
Test ch1/fibonacci.py
"""

import unittest
from ch1.fibonacci import bad_fib
from ch1.fibonacci import better_fib
from ch1.fibonacci import good_fib

#sys.path.append(os.path.dirname(__file__)+"/../")


# print(__file__)
class TestFibonacci(unittest.TestCase):
    """
    Test Fibonacci
        1 2 3 4 5 6 7  8
        -----------------
        1 1 2 3 5 8 13 21
    """

    def test_bad_fib(self):
        self.assertEqual(bad_fib(1), 1)
        self.assertEqual(bad_fib(6), 8)

    def test_better_fib(self):
        self.assertEqual(better_fib(1), 1)
        self.assertEqual(better_fib(6), 8)

    def test_good_fib(self):
        self.assertEqual(good_fib(1), 1)
        self.assertEqual(good_fib(6), 8)
