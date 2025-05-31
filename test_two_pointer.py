import unittest

from two_pointer import TwoPointer

class TestArraysAndHashing(unittest.TestCase):
    def setUp(self):
        self.solver = TwoPointer()
    
    def test_is_palindrome(self):
        self.assertTrue(self.solver.isPalindrome("Was it a car or a cat I saw?"), True)
    
    def test_two_pointer_II(self):
        self.assertEqual(self.solver.twoSumII([1,2,3,4], 3), [1,2])


if __name__ == '__main__':
    unittest.main()