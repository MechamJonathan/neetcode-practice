

import unittest
from binary_search import BinarySearch


class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.solver = BinarySearch()
    
    # contains duplicates
    def test_binary_search(self):
        nums=[-1,0,2,4,6,8]
        target = 4
        self.assertTrue(self.solver.search(nums, target), 3)

if __name__ == '__main__':
    unittest.main()