"""
Test ch1/random_connect.py
"""

import unittest
import ch1.random_connect as rc



# print(__file__)
class TestRandomConnect(unittest.TestCase):
    def test_draw(self):
        rc.set_no_show()
        rc.draw(5, 0.3)
        self.assertEqual(True, True)
