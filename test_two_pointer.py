import unittest

from two_pointer import TwoPointer

class TestArraysAndHashing(unittest.TestCase):
    def setUp(self):
        self.solver = TwoPointer()
    
    def test_is_palindrome(self):
        self.assertTrue(self.solver.isPalindrome("Was it a car or a cat I saw?"), True)
    
    def test_two_pointer_II(self):
        self.assertEqual(self.solver.twoSumII([1,2,3,4], 3), [1,2])
    
    def test_three_sum(self):
        self.assertEqual(self.solver.threeSum([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])

    def test_max_area(self):
        self.assertEqual(self.solver.maxArea([1,7,2,5,4,7,3,6]), 36)
    
    def test_trap(self):
        self.assertEqual(self.solver.trap([0,2,0,3,1,0,1,3,2,1]), 9)

if __name__ == '__main__':
    unittest.main()