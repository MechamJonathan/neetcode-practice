import unittest
from stacks import Stacks

class TestStacks(unittest.TestCase):
    def setUp(self):
        self.solver = Stacks()

    def test_is_valid_parenthesis(self):
        self.assertEqual(self.solver.isValidParenthesis("([{}])"), True)

if __name__ == '__main__':
    unittest.main()