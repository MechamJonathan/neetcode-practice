import unittest
from stacks import Stacks

class TestStacks(unittest.TestCase):
    def setUp(self):
        self.solver = Stacks()

    def test_is_valid_parenthesis(self):
        self.assertEqual(self.solver.isValidParenthesis("([{}])"), True)
    
    def test_eval_RPN(self):
        tokens=["2","1","+","3","*"]
        self.assertEqual(self.solver.evalRPN(tokens), 9)

if __name__ == '__main__':
    unittest.main()