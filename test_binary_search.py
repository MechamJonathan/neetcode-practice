

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

    def test_search_matrix(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target = 3
        self.assertTrue(self.solver.search_matrix(matrix, target), 3)


if __name__ == '__main__':
    unittest.main()