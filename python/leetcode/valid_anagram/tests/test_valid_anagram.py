import unittest
from valid_anagram import Solution

class IsPalindromeTestCase(unittest.TestCase):
  def test_input_1(self):
    solution = Solution()
    s = "anagram"
    t = "nagaram"
    result = solution.isAnagram(s, t)
    self.assertTrue(result)

  def test_input_2(self):
    solution = Solution()
    s = "rat"
    t = "car"
    result = solution.isAnagram(s, t)
    self.assertFalse(result)

  def test_input_3(self):
    solution = Solution()
    s = "ab"
    t = "a"
    result = solution.isAnagram(s, t)
    self.assertFalse(result)



if __name__ == '__main__':
    unittest.main()
