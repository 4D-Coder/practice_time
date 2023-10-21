import unittest
import ipdb
from invert_binary_tree import Solution, TreeNode
import json

class InvertTreeTestCase(unittest.TestCase):
  def test_input_1(self):
    solution = Solution()
    input = solution.toBinaryTree([4,2,7,1,3,6,9])
    inverted = solution.invertTree(input)

    expected = [4,7,2,9,6,3,1]
    result = solution.toList(inverted)

    self.assertEqual(result, expected)

  def test_input_2(self):
    solution = Solution()
    input = solution.toBinaryTree([2,1,3])
    inverted = solution.invertTree(input)

    expected = [2,3,1]
    result = solution.toList(inverted)

    self.assertEqual(result, expected)

  def test_input_3(self):
    solution = Solution()
    input = solution.toBinaryTree([])
    inverted = solution.invertTree(input)

    expected = []
    result = solution.toList(inverted)

    self.assertEqual(result, expected)

if __name__ == '__main__':
  unittest.main()
