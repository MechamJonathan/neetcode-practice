

import unittest

from arrays_and_hashing import ArraysAndHashing

# python3 -m unittest test_arrays_and_hashing.py

class TestArraysAndHashing(unittest.TestCase):
    def setUp(self):
        self.solver = ArraysAndHashing()
    
    def test_contains_duplicate_true(self):
        self.assertTrue(self.solver.contains_duplicate([1, 2, 3, 1]))

    def test_contains_duplicate_false(self):
        self.assertFalse(self.solver.contains_duplicate([1, 2, 3, 4]))

if __name__ == '__main__':
    unittest.main()