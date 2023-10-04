from typing import List
import ipdb

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      for i, v in enumerate(nums):
        for j, w in enumerate(nums):
          if i != j and v + w == target:
            return [i, j]
