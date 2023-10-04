import unittest
from two_sum import Solution

class TwoSumTestCase(unittest.TestCase):
  def test_input_1(self):
    solution = Solution()
    result = solution.twoSum([2,7,11,15], 9)
    self.assertEqual(result, [0,1])

  def test_input_2(self):
    solution = Solution()
    result = solution.twoSum([3,2,4], 6)
    self.assertEqual(result, [1,2])

  def test_input_3(self):
    solution = Solution()
    result = solution.twoSum([3,3], 6)
    self.assertEqual(result, [0,1])


if __name__ == '__main__':
    unittest.main()
