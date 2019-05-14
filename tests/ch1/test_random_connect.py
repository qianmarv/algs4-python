"""
Test ch1/random_connect.py
"""

import unittest
import ch1.random_connect as rc



# print(__file__)
class TestRandomConnect(unittest.TestCase):
    def test_draw(self):
        rc.draw(5, 0.3, False)
        self.assertEqual(True, True)
