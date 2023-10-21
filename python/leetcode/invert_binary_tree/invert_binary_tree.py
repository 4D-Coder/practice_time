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

    # Create a root node to start
    root = TreeNode(values.pop(0))

    # Initialize a re-usable queue for referencing and adding to
    # the tree
    queue = deque([root])

    # while loop for the values list, as its state will eventually
    # become None once all values are added to the tree, breaking
    # the loop
    while values:
      # queue object pops leftmost value, which is always going to
      # be a node
      current_node = queue.popleft()

      # Creating the left value for the current node by popping it
      # out of the list
      left_value = values.pop(0)

      if left_value is not None:
        # Instantiate a new TreeNode object with the variable as
        # it's value, and assign it to the current node's left
        # attribute, also adding the new node to the queue to be
        # built

        current_node.left = TreeNode(left_value)
        queue.append(current_node.left)

      if values: # Check if there is another value for a right node
        right_value = values.pop(0) # Take the next value from list
        # Same process if there is a value in the list at this point
        if right_value is not None:
          current_node.right = TreeNode(right_value)
          queue.append(current_node.right)

      # Finally returning root node along with its branches
    return root
