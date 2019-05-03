import unittest
from ch1 import BinarySearch

class TestBinarySearch(unittest.TestCase):
    def test_rank(self):
        arr = [1,2,3,5,9]
        key = 5
        self.assertEqual(BinarySearch.rank(key, arr),3)
