from typing import Optional, List
import ipdb

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

  # Definition for testing object value, bypassing object identity during `isEqual` testing assertions
  # def __eq__(self, other):
  #     if not other or not isinstance(other, ListNode):
  #         return False
  #     return self.val == other.val and self.next == other.next

class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy

    while list1 or list2:
      if not list1:
          current.next = list2
          break
      if not list2:
          current.next = list1
          break

      if list1.val < list2.val:
          current.next, list1 = list1, list1.next
      else:
          current.next, list2 = list2, list2.next

      current = current.next
    return dummy.next







