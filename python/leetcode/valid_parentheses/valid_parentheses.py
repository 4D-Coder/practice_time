import ipdb

class Solution:
    def isValid(self, s: str) -> bool:
      matcher = { "]": "[", "}": "{", ")": "(" }
      stack = []

      for char in s:
        if char in matcher:
          top_element = stack.pop() if stack else '.'
          if matcher[char] != top_element:
            return False
        else:
          stack.append(char)
      return not stack
