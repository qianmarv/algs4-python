import unittest
from ch1.BinarySearch  import rank
#sys.path.append(os.path.dirname(__file__)+"/../")

print(__file__)
class TestBinarySearch(unittest.TestCase):
    def test_rank(self):
        arr = [1,2,3,5,9]
        key = 5
        self.assertEqual(rank(key, arr),3)
