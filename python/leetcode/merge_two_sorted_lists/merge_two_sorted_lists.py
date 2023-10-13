from typing import Optional, List
import ipdb

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def toSortedList(self, values: List[int]) -> Optional[ListNode]:
    if not values:
      return None

    head = ListNode(values[0])
    current_node = head

    for i in values[1:]:
      current_node.next = ListNode(i)
      current_node = current_node.next

      return head

  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    list1 = self.toSortedList(list1)
    list2 = self.toSortedList(list2)

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







