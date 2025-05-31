

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

    # group anagrams
    def test_group_anagrams(self):
        result = self.solver.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
        self.assertEqual(result, [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])

    # top k frequent items
    def test_top_k_frequent_items(self):
        result = self.solver.topKFrequentItems([1,2,2,3,3,3], 2)
        self.assertEqual(result, [2,3])

if __name__ == '__main__':
    unittest.main()