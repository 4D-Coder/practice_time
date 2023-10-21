import ipdb
from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  # def __str__(self):
    # return "<TreeNode> val:{}".format(self.val)

class Solution:
  def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
      return None

    queue = deque([root])
    while queue:
      current_node = queue.popleft()

      current_node.left, current_node.right = current_node.right, current_node.left

      if current_node.left:
        queue.append(current_node.left)

      if current_node.right:
        queue.append(current_node.right)

    return root

  def toBinaryTree(self, values: List[int]) -> Optional[TreeNode]:
    if not values:
      return None

    root = TreeNode(values.pop(0))
    queue = deque([root])

    while values:
      current_node = queue.popleft()
      left_value = values.pop(0)

      if left_value is not None:
        current_node.left = TreeNode(left_value)
        queue.append(current_node.left)

      if values:
        right_value = values.pop(0)
        if right_value is not None:
          current_node.right = TreeNode(right_value)
          queue.append(current_node.right)
    return root
