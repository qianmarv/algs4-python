"""
Test ch1/evaluate.py
"""

import unittest
from ch1.evaluate import evaluate



# print(__file__)
class TestEvaluate(unittest.TestCase):
    """
    Test Evaluate
    """

    def test_bad_fib(self):
        self.assertEqual(evaluate('( 1 + 1 )'), 1.0+1.0)
        self.assertEqual(evaluate('( ( 1 + 1 ) * 5 )'), 10.0)
        self.assertEqual(evaluate('( ( 31 - ( ( 1 + 1 ) * 5 ) ) / 3 )'), 7.0)
