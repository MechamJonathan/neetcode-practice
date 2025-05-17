

import unittest

from arrays_and_hashing import ArraysAndHashing

# python3 -m unittest test_arrays_and_hashing.py

class TestArraysAndHashing(unittest.TestCase):
    def setUp(self):
        self.solver = ArraysAndHashing()
    
    # contains duplicates
    def test_contains_duplicate_true(self):
        self.assertTrue(self.solver.contains_duplicate([1, 2, 3, 1]))

    def test_contains_duplicate_false(self):
        self.assertFalse(self.solver.contains_duplicate([1, 2, 3, 4]))

    # valid anagrams
    def test_valid_anagram_true(self):
        self.assertTrue(self.solver.isAnagram("racecar", "carrace"))

    def test_valid_anagram_false(self):
        self.assertFalse(self.solver.isAnagram("jar", "jam"))
    
    # two sum
    def test_two_sum_basic(self):
        result = self.solver.twoSum([2, 7, 11, 15], 9)
        self.assertEqual(sorted(result), [0,1])

if __name__ == '__main__':
    unittest.main()