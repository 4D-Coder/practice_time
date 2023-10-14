import unittest
from max_profit import Solution

class MaxProfitTestCase(unittest.TestCase):
  def test_input_1(self):
    prices = [7,1,5,3,6,4]
    solution = Solution()
    result = solution.maxProfit(prices)
    self.assertEqual(result, 5)

  def test_input_2(self):
    prices = [7,6,4,3,1]
    solution = Solution()
    result = solution.maxProfit(prices)
    self.assertEqual(result, 0)

  def test_input_3(self):
    prices = [1]
    solution = Solution()
    result = solution.maxProfit(prices)
    self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
