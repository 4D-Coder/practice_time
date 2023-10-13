import unittest
from merge_two_sorted_lists import Solution, ListNode
from typing import List, Optional

class TwoSumTestCase(unittest.TestCase):
  def test_input_1(self):
    list1 = self.toSortedList([1,2,4])
    list2 = self.toSortedList([1,3,4])
    desired = self.toSortedList([1,1,2,3,4,4])

    solution = Solution()
    result = solution.mergeTwoLists(list1, list2)

    # self.assertEqual(result, desired)

  def test_input_2(self):
    list1 = self.toSortedList([])
    list2 = self.toSortedList([])
    desired = self.toSortedList([])

    solution = Solution()
    result = solution.mergeTwoLists(list1, list2)
    self.assertLinkedListsEqual(result, desired)

  def test_input_3(self):
    list1 = self.toSortedList([])
    list2 = self.toSortedList([0])
    desired = self.toSortedList([0])
    
    solution = Solution()
    result = solution.mergeTwoLists(list1, list2)
    self.assertLinkedListsEqual(result, desired)


  # Helper methods
  def toSortedList(self, values: List[int]) -> Optional[ListNode]:
    if not values:
      return None

    head = ListNode(values[0])
    current_node = head

    for i in values[1:]:
      current_node.next = ListNode(i)
      current_node = current_node.next

      return head

  def assertLinkedListsEqual(self, list1, list2):
    while list1 is not None and list2 is not None:
      self.assertEqual(list1.val, list2.val)
      list1 = list1.next
      list2 = list2.next
    # Ensures both lists are now None (otherwise, they are of unequal length)
    # self.assertIsNone(list1)
    # self.assertIsNone(list2)

if __name__ == '__main__':
  unittest.main()
