import unittest
from valid_parentheses import Solution

class TwoSumTestCase(unittest.TestCase):
  def test_input_1(self):
    solution = Solution()
    result = solution.isValid("()")
    self.assertTrue(result)

  def test_input_2(self):
    solution = Solution()
    result = solution.isValid("()[]{}")
    self.assertTrue(result)

  def test_input_3(self):
    solution = Solution()
    result = solution.isValid("(]")
    self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
