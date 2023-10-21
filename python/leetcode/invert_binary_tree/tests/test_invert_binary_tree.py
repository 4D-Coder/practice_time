import unittest
import ipdb
from invert_binary_tree import Solution, TreeNode

class InvertTreeTestCase(unittest.TestCase):
  def test_input_1(self):
    solution = Solution()
    sorted_tree = solution.toBinaryTree([4,2,7,1,3,6,9])

    expected = solution.toBinaryTree([4,7,2,9,6,3,1])
    result = solution.invertTree(sorted_tree)

    self.assertEqual(result, expected)

  def test_input_2(self):
    solution = Solution()
    sorted_tree = solution.toBinaryTree([2,1,3])

    expected = solution.toBinaryTree([2,3,1])
    result = solution.invertTree(sorted_tree)

    self.assertEqual(result, expected)

  def test_input_3(self):
    solution = Solution()
    sorted_tree = solution.toBinaryTree([])

    expected = solution.toBinaryTree([])
    result = solution.invertTree(sorted_tree)

    self.assertEqual(result, expected)

if __name__ == '__main__':
  unittest.main()
