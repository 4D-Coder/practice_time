import unittest
from valid_palindrome import Solution

class IsPalindromeTestCase(unittest.TestCase):
  def test_input_1(self):
    solution = Solution()
    result = solution.isPalindrome("A man, a plan, a canal: Panama")
    self.assertTrue(result)

  def test_input_2(self):
    solution = Solution()
    result = solution.isPalindrome("race a car")
    self.assertFalse(result)

  def test_input_3(self):
    solution = Solution()
    result = solution.isPalindrome(" ")
    self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
