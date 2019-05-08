"""
Test ch1/binary_search.py
"""

import unittest
from ch1.binary_search import search
from ch1.binary_search import recursive_search

#sys.path.append(os.path.dirname(__file__)+"/../")


# print(__file__)
class TestBinarySearch(unittest.TestCase):
    """
    Test binary_search
    """

    def test_search(self):
        """
        Test search method
        """
        self.assertEqual(search(5, [1, 2, 3, 5, 9]), 3)
        self.assertEqual(search(9, [1, 2, 3, 5, 9]), 4)
        self.assertEqual(search(1, [1, 2, 3, 5, 9]), 0)
        self.assertEqual(search(7, [1, 2, 3, 5, 9]), -1)

    def test_recursive_search(self):
        """
        Test search method
        """
        self.assertEqual(recursive_search(5, [1, 2, 3, 5, 9]), 3)
        self.assertEqual(recursive_search(9, [1, 2, 3, 5, 9]), 4)
        self.assertEqual(recursive_search(1, [1, 2, 3, 5, 9]), 0)
        self.assertEqual(recursive_search(7, [1, 2, 3, 5, 9]), -1)
